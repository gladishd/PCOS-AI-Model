import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles import monokai
import os

def create_plot_with_code(plot_func, code_snippet, title, filename, figsize=(15, 10)):
    """Creates a figure combining the plot and its code"""
    # Ensure images directory exists
    os.makedirs('images', exist_ok=True)
    
    # First, create code image
    formatter = ImageFormatter(style='monokai', 
                             line_numbers=True,
                             font_size=14,
                             line_pad=3)
    
    code_image = highlight(code_snippet, PythonLexer(), formatter)
    code_image_path = 'images/temp_code.png'
    with open(code_image_path, 'wb') as f:
        f.write(code_image)
    
    # Create figure with grid
    fig = plt.figure(figsize=figsize)
    gs = GridSpec(2, 1, height_ratios=[2, 1])
    
    # Add title
    fig.suptitle(title, fontsize=16, y=0.95)
    
    # Create plot in top subplot
    ax1 = fig.add_subplot(gs[0])
    plot_func(ax1)
    
    # Create code snippet in bottom subplot
    ax2 = fig.add_subplot(gs[1])
    ax2.text(0.05, 0.95, code_snippet,
             family='monospace',
             fontsize=8,
             verticalalignment='top',
             horizontalalignment='left',
             transform=ax2.transAxes,
             bbox=dict(facecolor='#272822',
                      edgecolor='none',
                      alpha=0.6))
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    # Clean up temporary file
    if os.path.exists(code_image_path):
        os.remove(code_image_path) 