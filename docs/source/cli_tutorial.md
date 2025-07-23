# nb4llm CLI Tutorial

The `nb4llm` command-line tool lets you convert Jupyter notebooks to and from a readable, LLM-friendly text format.

## Basic Usage

### Convert a notebook to text

```bash
nb4llm notebook.ipynb
# Output: notebook.txt
```

### Convert a notebook to a specific text file

```bash
nb4llm notebook.ipynb output.txt
```

### Convert text back to a notebook

```bash
nb4llm --reverse notebook.txt
# Output: notebook.ipynb
```

### Convert text to a specific notebook file

```bash
nb4llm --reverse notebook.txt output.ipynb
```

### Show help

```bash
nb4llm --help
```

## Options

- `--reverse`, `-r`: Convert from text to notebook (default is notebook to text)
- `--verbose`, `-v`: Print extra information about the conversion
- `input_file`: The file to convert (notebook or text)
- `output_file`: The output file (optional; auto-generated if not provided)

## Example Workflow

1. Convert a notebook to text:
   ```bash
   nb4llm my_analysis.ipynb
   # Creates my_analysis.txt
   ```
2. Edit or process the text file as needed (e.g., for LLM ingestion).
3. Convert the text file back to a notebook:
   ```bash
   nb4llm --reverse my_analysis.txt
   # Creates my_analysis.ipynb
   ```

## Advanced
- The tool preserves code cell language (e.g., Python, R, Julia).
- Handles nested code fences in markdown and code cells.
- Use in scripts or pipelines for batch conversion.

---

For more details, see the docstrings in the Python API or run `nb4llm --help`. 