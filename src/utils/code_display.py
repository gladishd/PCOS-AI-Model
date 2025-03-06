import matplotlib.pyplot as plt
import numpy as np
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import BBCodeFormatter
from pygments.styles import monokai

def create_code_snapshot(code, filename, title="Code Snapshot"):
    """Create a visually appealing code snapshot using matplotlib"""
    # Format the code with syntax highlighting
    formatter = BBCodeFormatter(style='monokai')
    highlighted = highlight(code, PythonLexer(), formatter)
    
    # Split into lines
    lines = highlighted.strip().split('\n')
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, len(lines) * 0.3))
    
    # Set background color
    ax.set_facecolor('#272822')  # Monokai background color
    fig.patch.set_facecolor('#272822')
    
    # Add code lines
    for i, line in enumerate(lines):
        # Remove BBCode formatting and add text
        clean_line = line.replace('[color=#', '').replace(']', '').replace('[/color]', '')
        ax.text(0.05, 1 - (i+1)/(len(lines)+1), clean_line,
                color='white',
                fontfamily='monospace',
                fontsize=10,
                transform=ax.transAxes)
    
    # Remove axes
    ax.axis('off')
    
    # Save the figure
    plt.savefig(f'images/{filename}.png',
                bbox_inches='tight',
                dpi=300,
                facecolor='#272822',
                edgecolor='none')
    plt.close() 