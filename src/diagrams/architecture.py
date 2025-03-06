import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    # Create layers
    data_layer = patches.Rectangle((1, 6), 10, 1.5, facecolor='lightblue', alpha=0.3)
    ai_layer = patches.Rectangle((1, 3.5), 10, 1.5, facecolor='lightgreen', alpha=0.3)
    app_layer = patches.Rectangle((1, 1), 10, 1.5, facecolor='lightpink', alpha=0.3)

    # Add components
    ax.add_patch(data_layer)
    ax.add_patch(ai_layer)
    ax.add_patch(app_layer)

    # Add labels
    ax.text(5.5, 7.2, 'Data Layer', horizontalalignment='center', fontsize=12)
    ax.text(5.5, 4.7, 'AI Layer', horizontalalignment='center', fontsize=12)
    ax.text(5.5, 2.2, 'Application Layer', horizontalalignment='center', fontsize=12)

    # Add components text
    ax.text(3, 6.5, 'Microbiome DB', fontsize=10)
    ax.text(8, 6.5, 'Research Papers', fontsize=10)
    ax.text(2, 4, 'ML Models', fontsize=10)
    ax.text(5.5, 4, 'RAG System', fontsize=10)
    ax.text(9, 4, 'GenAI', fontsize=10)
    ax.text(3, 1.5, 'API', fontsize=10)
    ax.text(8, 1.5, 'Web UI', fontsize=10)

    # Remove axes
    ax.axis('off')

    # Save the diagram
    plt.savefig('architecture.png', bbox_inches='tight', dpi=300)
    plt.close()

if __name__ == "__main__":
    create_architecture_diagram() 