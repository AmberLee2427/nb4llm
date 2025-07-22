#converter.py

#convert .ipynb to .txt
def convert_ipynb_to_txt(ipynb_path, txt_path):
    nb = nbformat.read(ipynb_path, as_version=4)
    out_lines = []
    out_lines.append(f"# {Path(ipynb_path).name}\n")
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            out_lines.append("```markdown")
            out_lines.append(cell.source)
            out_lines.append("```\n")
        elif cell.cell_type == "code":
            out_lines.append("```python")
            out_lines.append(cell.source)
            out_lines.append("```\n")
    return "\n".join(out_lines)

# Usage
#ipynb_path = "note_book_name.ipynb"
#txt_path = "note_book_name.txt"
#with open(txt_path, "w") as f:
#    f.write(notebook_to_txt(ipynb_path))

#convert .txt to .ipynb
def convert_txt_to_ipynb(txt_path, ipynb_path):
    pass


