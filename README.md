# Website for Neural Reckoning group

http://neural-reckoning.org

Install GraphViz https://graphviz.org/

Create an environment with

    conda create --name nrweb python=3 jinja2 pillow wordcloud
    conda activate nrweb
    pip install tweepy orcid

Create a file ``twitter_secrets.py`` with ``api_key = '...'`` and ``api_secret_key = '...'``. Do not commit this file!

Same for ``orcid_secrets.py`` with ``client_id`` and ``client_secrets``.