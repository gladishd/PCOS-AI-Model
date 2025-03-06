import matplotlib.pyplot as plt
import numpy as np

def create_risk_matrix():
    # Define risks
    risks = [
        ('Data Sparsity', 3, 4),
        ('Model Integration', 4, 3),
        ('Computing Resources', 2, 4),
        ('Timeline', 3, 3)
    ]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create matrix
    for risk in risks:
        plt.plot(risk[1], risk[2], 'ro', markersize=10)
        plt.annotate(risk[0], (risk[1], risk[2]), xytext=(10, 10),
                    textcoords='offset points')
    
    # Customize plot
    plt.grid(True)
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.xlabel('Impact')
    plt.ylabel('Likelihood')
    plt.title('Risk Assessment Matrix')
    
    plt.savefig('risk_matrix.png', dpi=300, bbox_inches='tight')
    plt.close() 