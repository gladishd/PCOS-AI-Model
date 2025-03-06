import matplotlib.pyplot as plt
import numpy as np

def create_progress_chart():
    # Define completion percentages
    components = ['Data Collection', 'ML Pipeline', 'RAG System', 'UI Development', 'Testing']
    completion = [80, 65, 55, 30, 20]  # Update these percentages based on your progress
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create horizontal bars
    bars = ax.barh(components, completion, 
                   color=['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f1c40f'])
    
    # Add percentage labels
    for i, v in enumerate(completion):
        ax.text(v + 1, i, f'{v}%', va='center')
    
    # Customize chart
    ax.set_xlim(0, 100)
    ax.set_title('Project Progress Overview', pad=20)
    ax.set_xlabel('Completion Percentage')
    
    plt.tight_layout()
    plt.savefig('progress_chart.png', dpi=300, bbox_inches='tight')
    plt.close() 