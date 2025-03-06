import matplotlib.pyplot as plt
import numpy as np

def create_project_banner():
    fig, ax = plt.subplots(figsize=(15, 3))
    
    # Create gradient background
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X*10) * np.cos(Y*10)
    
    plt.imshow(Z, cmap='Blues', aspect='auto', alpha=0.3)
    
    # Add project title
    plt.text(0.5, 0.5, 'PCOS-Driven Gut Microbiome AI Model', 
             horizontalalignment='center',
             fontsize=24, 
             fontweight='bold',
             transform=ax.transAxes)
    
    # Remove axes
    plt.axis('off')
    
    # Save banner
    plt.savefig('project_banner.png', bbox_inches='tight', dpi=300)
    plt.close() 