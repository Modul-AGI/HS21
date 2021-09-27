import nbformat as nbf
from glob import glob
import re
# Collect a list of all notebooks in the content folder
notebooks_cog1 = glob("B_Coding_in_GIS_1/*.ipynb", recursive=False) # recursive = True to search in subfolders
notebooks_cog2 = glob("B_Coding_in_GIS_2/*.ipynb", recursive=False) # recursive = True to search in subfolders
notebooks_cog3 = glob("B_Coding_in_GIS_3/*.ipynb", recursive=False) # recursive = True to search in subfolders




def musterloesung(notebooks,tag = "remove-cell"):
    """
    takes 2 arguments: "notebook" and "tag"
    The first argument is a list of paths to the notebooks that should be processed
    the second argument is a single tag or a list of tags, which should be appended to each cell
    possible arguments for tags:
    - hide-cell: hides the whole code cell (both inputs and outputs)
    - remove-cell: removes the whole code cell (both inputs and outputs)
    see: https://jupyterbook.org/interactive/hiding.html?highlight=hide%20cell

    """
    # for loops works through each ipynb-file
    for ipath in notebooks:
        print(tag + " for all cells in "+ipath)
        ntbk = nbf.read(ipath, nbf.NO_CONVERT)
        # for loop works through each cell of a given file
        for cell in ntbk.cells:
            cell_tags = cell.get('metadata', {}).get('tags', [])
            # If the word "Musterlösung" contained in the cell content
            if "# Musterlösung" in cell["source"]:
                # removes all tags starting with "remove-" or "hide-"
                cell_tags = [i for i in cell_tags if not re.match("remove|hide-.+",i)]
                # if argument "tag" is not empty, append the given cell tag to the cell
                if tag != "": cell_tags.append(tag)    
                if len(cell_tags) > 0:
                    cell['metadata']['tags'] = cell_tags
                    print("changed cell metadata!")

        nbf.write(ntbk, ipath)

# Sort all the notebooks in order (so they can easily be selected / unselected)
notebooks_cog1.sort()
notebooks_cog2.sort()
notebooks_cog3.sort()

# first, remove all cells that contain musterlösung
musterloesung(notebooks_cog1, "remove-cell")
musterloesung(notebooks_cog2, "remove-cell")
musterloesung(notebooks_cog3, "remove-cell")

# selectivley add notebooks
musterloesung(notebooks_cog1, "hide-cell")
musterloesung(notebooks_cog2, "hide-cell")
musterloesung(notebooks_cog3, "hide-cell")




