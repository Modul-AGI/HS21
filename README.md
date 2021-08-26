
## Technical stuff

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




## Conventions

### Tables

Here is how we can create tables. We reference the tables like so: {numref}\`tablereference\`. What we get is something along the lines of [Tab. 3](link_to_html.html) (depending on the language specified in _config.yml)
````
```{list-table} We can place descriptions here
:header-rows: 1
:name: tablereference

* - First row of col 1(inkl. Link)
  - First row of col 2
* - Second row of col 1(inkl. Link)
  - Second row of col 2
```
````

### Figures 

Here is how we create figures. We reference the figures like so: {ref}\`imagereferece\` (_not_ numref_). What we get is something along the lines of [Abb. 9](link_to_html.html) (depending on the language specified in _config.yml)
````
```{figure} folder/image.jpg
:name: imagereferece

Image description
```
````

### Übungsziele

````
```{admonition} Übungsziele
:class: attention
- Ziel 1
- Ziel 2
- Ziel 3
```
````


### Chapter reference

We can create a label for a chapter using the following syntax

``` 
(chapter-label)=
## Chapter Title
```

To reference this chapter, you can use {ref}\`chapter-label\`