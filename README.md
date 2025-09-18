# Website for Neural Reckoning group

http://neural-reckoning.org

## Installation

Install GraphViz https://graphviz.org/

Create an environment with

    conda env create -f environment.yml

Create a file ``twitter_secrets.py`` with ``api_key = '...'`` and ``api_secret_key = '...'``. Do not commit this file!

**NOTE (2025/2/27):** sqlite version 3.49.1 has a bug that is not currently fixed and causes the scripts to fail. Temporary fix is to run the following after installing: ``conda install sqlite=3.48``.

## Editing and running

Edit ``.yaml`` files in ``people``, ``papers``, ``software``.

Run ``generate_html.py``.

## Upgrade packages

Because of the pip installed parts, to upgrade just delete the existing environment and recreate.

    conda remove -n nrweb --all
    conda env create -f environment.yml

## Local server when testing search

For the search functionality, the local copy needs to be run on a server using [http-server](https://www.npmjs.com/package/http-server) npm package. You can run

    http-server . --cors
