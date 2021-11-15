def find_paper_authors(people, papers):
    # build a map from author name representations to Person objects
    name2person = {}
    for person in people.values():
        for name in [person.name]+person.author_names:
            name = name.strip().lower()
            name2person[name] = person
    # scan through papers and add all authors to paper, and all papers to authors
    for paper in papers.values():
        pubauths = [a.strip() for a in paper.authors.split(',')]
        paper.author_objects = [name2person.get(auth.lower(), auth) for auth in pubauths]
        # create HTML representation of author list
        newpubauths = []
        for authname, author in zip(pubauths, paper.author_objects):
            if isinstance(author, str):
                newpubauths.append(author)
            else:
                newpubauths.append(f'<a href="{author.key}.html">{authname}</a>')
        paper.authors_list_text = pubauths
        paper.authors = ', '.join(newpubauths)
        if len(pubauths)<=6:
            paper.authors_short = paper.authors
            paper.authors_short_list_text = paper.authors_list_text
        else:
            paper.authors_short = pubauths[0]+', et al.'
            paper.authors_short_list_text = [pubauths[0], 'et al.']
        # add paper to all authors
        for author in paper.author_objects:
            if not isinstance(author, str):
                if not hasattr(author, 'papers'):
                    author.papers = []
                author.papers.append(paper)