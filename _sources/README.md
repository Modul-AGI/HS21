

## Jupyter Book setup

- 90 % can be found in the jupyter-book documentation on [jupyterbook.org](https://jupyterbook.org)
- to build the book, I implemented the approach "[Automatically host your book with GitHub Actions](https://jupyterbook.org/publish/gh-pages.html#automatically-host-your-book-with-github-actions)"
- this action needs to be activated manually, to accomodate for workflows with extensive pushes to master (people working with the github ide to make changes)
- gh pages is sourcing the gh-pages branch. To build and publish locally:

```bash
jb build .
ghp-import -n -p _build/html/
```

- A pdf version of the book is currently not built. To reimplement this, check out the gh-action workflow from hs20 and read [my question on this](https://github.com/executablebooks/meta/discussions/124)





## Similar reccources

Nice ressources on the subject (because I don't know where es to put it right now):

- https://geo-python-site.readthedocs.io/en/latest/
- https://pythongis.org/