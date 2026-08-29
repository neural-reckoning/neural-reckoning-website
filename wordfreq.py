from collections import Counter
import os
import re
import hashlib
import numpy as np
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from cache import cached

def calculate_wordfreq(papers=None, member=None, top_n=10):
    if member is None:
        mpubs = papers.values()
    else:
        mpubs = member.things['Paper']
    if len(mpubs)==0:
        if not hasattr(member, 'external_publications') or not member.external_publications or len(member.external_publications)==0:
            return
        text = ' '.join(pub.title for pub in member.external_publications if hasattr(pub, 'title'))
    else:
        mpubs = list(mpubs)
        mpubs.sort(key=lambda x: getattr(x, 'abstract', ''))
        text = ' '.join(getattr(pub, 'abstract', '') for pub in mpubs)

    stop_words = set(stopwords.words("english"))
    stop_words.update(['using', 'may', 'used', 'based', 'different', 'also'])
    lemmatizer = WordNetLemmatizer()

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    cleaned = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and len(word)>1]

    counter = Counter(cleaned)
    if top_n is not None:
        counter = counter.most_common(top_n)

    return counter


def calculate_all_wordfreqs(people, papers):
    # setup NLTK
    nltk.download("stopwords", download_dir='temp', quiet=True)
    nltk.download("wordnet", download_dir='temp', quiet=True)

    # calculate_wordfreq(papers=papers)
    for member in people.values():
        wf = calculate_wordfreq(member=member)
        if wf is not None:
            member.word_frequencies = wf

    # do it year-by-year for the theme analysis
    years = sorted(set(pub.last_updated.year for pub in papers.values() if hasattr(pub, 'last_updated') and pub.last_updated is not None and pub.last_updated.year>=2008))
    wf_all = calculate_wordfreq(papers=papers, top_n=30)
    words = [word for word, _ in wf_all]
    wf = {}
    data = []
    for year in years:
        year_pubs = {k:v for k,v in papers.items() if hasattr(v, 'last_updated') and v.last_updated is not None and v.last_updated.year==year}
        wf[year] = calculate_wordfreq(papers=year_pubs, top_n=None)
        data.append([wf[year].get(word, 0) for word, _ in wf_all])

    hashable_rep = ' '.join(words)+' '+''.join(f"{year}:{','.join(str(count) for count in row)};" for year, row in zip(years, data))
    hash = hashlib.md5(hashable_rep.encode()).hexdigest()
    fname = "docs/wordfreq.png"
    if os.path.exists(fname) and fname in cached and cached[fname]==hash:
        return

    data = np.array(data)
    freq = data.T * 1.0
    freq = freq / freq.max(axis=0, keepdims=True) # Normalize frequencies for each year

    # smoothing
    kernel = np.array([1, 2, 3, 2, 1], dtype=float)
    kernel /= kernel.sum()

    freq = np.array([
        np.convolve(row, kernel, mode="same")
        for row in freq
    ])

    freq = freq / freq.max(axis=0, keepdims=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    im = ax.imshow(
        freq,
        aspect="auto",
        cmap="viridis",
        origin="upper"
    )

    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years, rotation=45, ha="right")

    ax.set_yticks(range(len(words)))
    ax.set_yticklabels(words)

    ax.set_xlabel("Year")
    ax.set_title("Word frequency in abstracts")

    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("Relative frequency")

    plt.tight_layout()
    plt.savefig(fname, dpi=300, bbox_inches="tight")
    cached[fname] = hash
