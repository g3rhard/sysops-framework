# Diagram Definitions

This directory contains individual diagram definition files for the SysOps Framework documentation.

## Structure

Each diagram file should contain:

1. **`create_diagram()`** function that returns a matplotlib figure
2. **`DIAGRAM_INFO`** dictionary with metadata:
   - `filename`: Output PNG filename
   - `description`: Human-readable description
   - `chapter`: Chapter number for ordering

## Example Structure

```python
"""
Description of what this diagram shows
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def create_diagram():
    """Create the diagram and return matplotlib figure"""
    fig = plt.figure(figsize=(16, 10))
    # ... diagram creation code ...
    return fig


# Diagram metadata
DIAGRAM_INFO = {
    "filename": "example-diagram.png",
    "description": "Example Diagram",
    "chapter": 1
}
```

## Usage

The `generate_diagrams.py` script automatically discovers all files in this directory and generates PNG files from them.

```bash
# Generate all diagrams to ../content/assets/
python generate_diagrams.py

# Generate to custom directory with custom DPI
python generate_diagrams.py --output-dir ../assets --dpi 300
```

## Adding New Diagrams

1. Create a new `.py` file in this directory
2. Implement the `create_diagram()` function
3. Define the `DIAGRAM_INFO` dictionary
4. Run `generate_diagrams.py` to generate the new PNG file

The script will automatically discover and include your new diagram.
