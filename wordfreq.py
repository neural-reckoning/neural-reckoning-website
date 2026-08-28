from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Run once
# nltk.download("stopwords")
# nltk.download("wordnet")

# def word_frequencies(text, top_n=20):
#     stop_words = set(stopwords.words("english"))
#     lemmatizer = WordNetLemmatizer()

#     words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

#     cleaned = [
#         lemmatizer.lemmatize(word)
#         for word in words
#         if word not in stop_words
#     ]

#     return Counter(cleaned).most_common(top_n)

# # Example
# text = """
# The researchers were running experiments.
# A researcher runs many experiments and studied results.
# """

# for word, count in word_frequencies(text):
#     print(f"{word}: {count}")

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
    stop_words.update(['using'])
    lemmatizer = WordNetLemmatizer()

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    cleaned = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and len(word)>1]

    return Counter(cleaned).most_common(top_n)


def calculate_all_wordfreqs(people, papers):
    # setup NLTK
    nltk.download("stopwords", download_dir='temp', quiet=True)
    nltk.download("wordnet", download_dir='temp', quiet=True)

    # calculate_wordfreq(papers=papers)
    for member in people.values():
        wf = calculate_wordfreq(member=member)
        if wf is not None:
            member.word_frequencies = wf
        # print(f"Word frequencies for {member.name}: {wf}")
