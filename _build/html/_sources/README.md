
For others, and for future me, here some notes on how I created this (jupyter-) book

- 90 % can be found in the jupyter-book documentation on [jupyterbook.org](https://jupyterbook.org)
- to build the book, I implemented the approach "[Automatically host your book with GitHub Actions](https://jupyterbook.org/publish/gh-pages.html#automatically-host-your-book-with-github-actions)" which means that I dont need a local installation of jupyter books
- I modified the github action yaml file in such a way that:
  - latex dependencies are installed on the server instance
  - a pdf version of the book is also built [using Latex](https://jupyterbook.org/advanced/pdf.html#id5)
  - this pdf version (which has a default location \_build/latex/python.pdf) is renamed, commited and pushed using github actions (read [my question on this](https://github.com/executablebooks/meta/discussions/124))


## Similar reccources

Nice ressources on the subject (because I don't know where es to put it right now):

- https://geo-python-site.readthedocs.io/en/latest/
- https://pythongis.org/