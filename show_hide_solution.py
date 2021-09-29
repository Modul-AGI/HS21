import nbformat as nbf
from glob import glob
import re
import os
import pandas as pd
# Collect a list of all notebooks in the content folder


def add_tag(notebook,tag = "remove-cell", keyword = "# Musterlösung"):
    """
    takes 2 arguments: "notebook" and "tag"
    The first argument is a SINGLE notebook that should be processed
    the second argument is a single tag or a list of tags, which should be appended to each cell
    possible arguments for tags:
    - "hide-cell": hides the code cell (both inputs and outputs) with the option that readers can reveal them if they wish
    - "remove-cell": removes the whole code cell (both inputs and outputs) without the option of revealing them
    - "" (empty string): just removes the current tags 
    see: https://jupyterbook.org/interactive/hiding.html?highlight=hide%20cell

    """
    ntbk = nbf.read(notebook, nbf.NO_CONVERT)
    # for loop works through each cell of a given file
    for cell in ntbk.cells:
        cell_tags = cell.get('metadata', {}).get('tags', [])
        # If the word "Musterlösung" contained in the cell content
        if keyword in cell["source"]:
            # creats a new list of tags
            #cell_tags = [i for i in cell_tags if not re.match("|".join(tag), i)]
            cell_tags = [i for i in cell_tags if not re.match("remove|hide-.+",i)]
            # if argument "tag" is not empty, append the given cell tag to the cell
            if tag != "": cell_tags.append(tag)    
            if len(cell_tags) > 0:
                cell['metadata']['tags'] = cell_tags
                print("changed cell metadata!")

    nbf.write(ntbk, notebook)


def glob_dict(coding_in_gis_dir, globpattern_files):
    notebooks = glob(os.path.join(coding_in_gis_dir, globpattern_files))
    dirs = [os.path.dirname(x) for x in notebooks]
    pathnames = [os.path.basename(x) for x in notebooks]

    filenr = [float(re.findall("_(\d*?)/", x)[0]+"."+re.findall("/(\d*?)_", x)[0]) for x in notebooks]


    mydict = {
        "notebook":notebooks,
        "dir":dirs, 
        "filenr": filenr
        }
    return(mydict)



def get_notebooks(globpattern_dirs = "[A-Z]_Coding_in_GIS_[1-9]", globpattern_files = "*.ipynb"):
    coding_in_gis_dirs = glob(globpattern_dirs)

    files_dict = [glob_dict(x, globpattern_files) for x in coding_in_gis_dirs]

    files_df_list = [pd.DataFrame(x) for x in files_dict]
    files_df = pd.concat(files_df_list)
    files_df = files_df.sort_values(by = "filenr")

    return(files_df)

notebooks_df = get_notebooks()


notebooks_df = notebooks_df.assign(tag = lambda x: ["hide-cell" if y <1.3 else "remove-cell" for y in x["filenr"]])

for index, row in notebooks_df.iterrows():
    add_tag(row["notebook"], row["tag"])









