import hashlib, os

from wordcloud import WordCloud

from cache import cached

# wordcloud: explicitly delete docs/wordcloud.png to recalculate
def make_wordcloud(papers=None, member=None, width=350, height=350):
    if member is None:
        fname = 'docs/wordcloud.png'
    else:
        fname = 'docs/wordcloud_{author}.png'.format(author=member.key)
    if member is None:
        mpubs = papers.values()
    else:
        mpubs = member.things['Paper']
    if len(mpubs)==0:
        if not hasattr(member, 'external_publications') or not member.external_publications or len(member.external_publications)==0:
            return
        all_abstracts = ' '.join(pub.title for pub in member.external_publications if hasattr(pub, 'title'))
    else:
        mpubs = list(mpubs)
        mpubs.sort(key=lambda x: getattr(x, 'abstract', ''))
        all_abstracts = ' '.join(getattr(pub, 'abstract', '') for pub in mpubs)
    m = hashlib.md5()
    m.update(all_abstracts.encode("utf-8"))
    abstract_hash = m.hexdigest()
    if os.path.exists(fname) and fname in cached and cached[fname]==abstract_hash:
        return
    print('recomputing wordcloud', (member.name if member is not None else 'all'))
    wordcloud = WordCloud(background_color="white", width=width, height=height).generate(all_abstracts)
    wordcloud.to_file(fname)
    cached[fname] = abstract_hash


def make_wordclouds(people, papers):
    make_wordcloud(papers=papers, width=1000, height=400)
    for member in people.values():
        make_wordcloud(member=member)
