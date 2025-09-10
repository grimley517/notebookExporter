import nbformat
from nbconvert import HTMLExporter

baseNotebook = "notebook.ipynb"
target = "notebook.html"

def exportNotebook():
    with open(baseNotebook) as file:
        contents = file.read()
        notebook = nbformat.reads(contents, as_version=4)
        exporter = HTMLExporter()
        (body, resources) = exporter.from_notebook_node(notebook)
        return body

def writeSite():
    body = exportNotebook()
    with open(target, 'wt') as file:
        file.write(body)


if __name__ == "__main__":
    writeSite()
