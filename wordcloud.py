import hashlib
from wordcloud import WordCloud

# # wordcloud: explicitly delete docs/wordcloud.png to recalculate
# def make_wordcloud(member=None, width=350, height=350):
#     if member is None:
#         fname = 'docs/wordcloud.png'
#     else:
#         fname = 'docs/wordcloud_{author}.png'.format(author=member.id)
#     if member is None:
#         mpubs = publications
#     else:
#         mpubs = member_publications(member)
#     if len(mpubs)==0:
#         return
#     all_abstracts = ' '.join(getattr(pub, 'abstract', '') for pub in mpubs)
#     m = hashlib.md5()
#     m.update(all_abstracts.encode("utf-8"))
#     abstract_hash = m.hexdigest()
#     if os.path.exists(fname) and fname in cached and cached[fname]==abstract_hash:
#         return
#     print('recomputing wordcloud', (member.name if member is not None else 'all'))
#     wordcloud = WordCloud(background_color="white", width=width, height=height).generate(all_abstracts)
#     wordcloud.to_file(fname)
#     cached[fname] = abstract_hash

# make_wordcloud(width=1000, height=400)
# for member in members:
#     make_wordcloud(member)
