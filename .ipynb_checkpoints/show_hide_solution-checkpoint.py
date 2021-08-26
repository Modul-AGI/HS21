import nbformat as nbf
from glob import glob
import re
# Collect a list of all notebooks in the content folder
notebooks_cog1 = glob("./01_*.ipynb", recursive=False) # recursive = True to search in subfolders
notebooks_cog2 = glob("./02_*.ipynb", recursive=False) # recursive = True to search in subfolders
notebooks_cog3 = glob("./03_*.ipynb", recursive=False) # recursive = True to search in subfolders
notebooks_cog4 = glob("./04_*.ipynb", recursive=False) # recursive = True to search in subfolders

# Search through each notebook and look for the text, add a tag if necessary

def musterloesung(notebooks,tag = "remove-cell"):
    # for loops works through each ipynb-file
    for ipath in notebooks:
        print(tag + "for all cells in "+ipath)
        ntbk = nbf.read(ipath, nbf.NO_CONVERT)
        # for loop works through each cell of a given file
        for cell in ntbk.cells:
            cell_tags = cell.get('metadata', {}).get('tags', [])
            # If the word "Musterlösung" contained in the cell content
            if "# Musterlösung" in cell["source"]:
                # removes all tags starting with "remove-" or "hide-"
                cell_tags = [i for i in cell_tags if not re.match("remove|hide-.+",i)]
                if tag != "": cell_tags.append(tag)    
                if len(cell_tags) > 0:
                    cell['metadata']['tags'] = cell_tags

        nbf.write(ntbk, ipath)

# Sort all the notebooks in order (so they can easily be selected / unselected)
notebooks_cog1.sort()
notebooks_cog2.sort()
notebooks_cog3.sort()

# first, remove all cells that contain musterlösung
musterloesung(notebooks_cog1, "remove-cell")
musterloesung(notebooks_cog2, "remove-cell")
musterloesung(notebooks_cog3, "remove-cell")
musterloesung(notebooks_cog4, "remove-cell")

# selectivley add notebooks
musterloesung(notebooks_cog1, "hide-cell")
musterloesung(notebooks_cog2, "hide-cell")


def remove_slidetags(notebooks):
    # for loops works through each ipynb-file   
#notebooks = ["./03_06_Raeumliche_Operationen.ipynb"]
    for ipath in notebooks:
        ntbk = nbf.read(ipath, nbf.NO_CONVERT)
        # for loop works through each cell of a given file
        for cell in ntbk.cells:
            slideshow = cell.get('metadata', {}).get('slideshow', [])
            # If the word "Musterlösung" contained in the cell content
            # removes all tags starting with "remove-" or "hide-"
            if slideshow:
                del cell["metadata"]["slideshow"]

            nbf.write(ntbk, ipath)



#remove_slidetags(glob("./0*_*.ipynb", recursive=False))


