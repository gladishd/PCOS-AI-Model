import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from src.utils.code_display import create_code_snapshot
from src.utils.plot_utils import create_plot_with_code
from src.utils.markdown_to_image import create_markdown_image

def create_bacteria_distribution(ax):
    # Set style for this plot
    sns.set_theme(style="whitegrid")
    
    # Sample data
    microbiome_data = {
        'Bacteroidetes': np.random.normal(30, 5, 100),
        'Firmicutes': np.random.normal(40, 7, 100),
        'Proteobacteria': np.random.normal(15, 3, 100),
        'Actinobacteria': np.random.normal(10, 2, 100)
    }
    df = pd.DataFrame(microbiome_data)
    
    # Create violin plot
    sns.violinplot(data=df, ax=ax, palette="Set3")
    ax.set_ylabel('Relative Abundance (%)')
    ax.tick_params(axis='x', rotation=45)

def create_dataset_visualization():
    # Set the style
    sns.set_theme(style="whitegrid")
    
    # Sample microbiome data
    microbiome_data = {
        'Patient_ID': range(100),
        'Bacteroidetes': np.random.normal(30, 5, 100),
        'Firmicutes': np.random.normal(40, 7, 100),
        'Proteobacteria': np.random.normal(15, 3, 100),
        'Actinobacteria': np.random.normal(10, 2, 100),
        'PCOS': np.random.choice([0, 1], 100),
        'Prediabetes': np.random.choice([0, 1], 100)
    }
    
    df = pd.DataFrame(microbiome_data)
    
    # Create figure with custom style
    fig = plt.figure(figsize=(20, 15))
    
    # 1. Distribution of bacteria phyla with violin plots
    plt.subplot(2, 2, 1)
    bacteria_cols = ['Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria']
    sns.violinplot(data=df[bacteria_cols], palette="Set3")
    plt.title('Distribution of Bacteria Phyla', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.ylabel('Relative Abundance (%)', fontsize=12)
    
    # 2. Enhanced correlation heatmap
    plt.subplot(2, 2, 2)
    correlation_matrix = df[bacteria_cols + ['PCOS', 'Prediabetes']].corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, 
                mask=mask,
                annot=True, 
                cmap='coolwarm', 
                center=0,
                fmt='.2f',
                square=True,
                cbar_kws={"shrink": .5})
    plt.title('Correlation Matrix', fontsize=14, pad=20)
    
    # 3. Enhanced bacteria composition plot
    plt.subplot(2, 2, 3)
    df_melted = df.melt(id_vars=['PCOS'], value_vars=bacteria_cols)
    sns.boxplot(data=df_melted, x='variable', y='value', hue='PCOS',
                palette=['#2ecc71', '#e74c3c'])
    plt.title('Bacteria Composition by PCOS Status', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.xlabel('Bacteria Phyla', fontsize=12)
    plt.ylabel('Relative Abundance (%)', fontsize=12)
    plt.legend(title='PCOS Status', labels=['Negative', 'Positive'])
    
    # 4. Enhanced sample distribution
    plt.subplot(2, 2, 4)
    sample_info = pd.crosstab(df.PCOS, df.Prediabetes)
    sns.heatmap(sample_info, 
                annot=True, 
                fmt='d', 
                cmap='YlOrRd',
                square=True,
                cbar_kws={"shrink": .5})
    plt.title('Sample Distribution', fontsize=14, pad=20)
    plt.xlabel('Prediabetes Status', fontsize=12)
    plt.ylabel('PCOS Status', fontsize=12)
    
    # Adjust layout
    plt.tight_layout(pad=3.0)
    
    # Add overall title
    fig.suptitle('Gut Microbiome Dataset Analysis', 
                 fontsize=16, 
                 y=1.02)
    
    # Save with high quality
    plt.savefig('images/dataset_visualization.png', 
                dpi=300, 
                bbox_inches='tight',
                facecolor='white',
                edgecolor='none')
    plt.close()

    # Create enhanced dataset description
    dataset_info = '''
# Gut Microbiome Dataset Analysis

## Dataset Overview
This comprehensive dataset combines gut microbiome sequencing data with clinical 
information from PCOS patients and healthy controls.

## Microbiome Features
- Bacteroidetes: Primary bacteria phylum (30% ± 5%)
- Firmicutes: Second major phylum (40% ± 7%)
- Proteobacteria: Less abundant phylum (15% ± 3%)
- Actinobacteria: Minor phylum (10% ± 2%)

## Clinical Variables
- PCOS Status (Binary)
  * Positive: Diagnosed cases
  * Negative: Healthy controls
- Prediabetes Risk (Binary)
  * Positive: HbA1c ≥ 5.7%
  * Negative: HbA1c < 5.7%

## Sample Characteristics
- Total Samples: 100
- PCOS Distribution:
  * Positive: 50 samples
  * Negative: 50 samples
- Prediabetes Prevalence:
  * Overall: 30%
  * In PCOS group: 40%
  * In Control group: 20%

## Data Collection Methods
- 16S rRNA Gene Sequencing
  * V3-V4 regions
  * Illumina MiSeq platform
- Quality Control
  * QIIME2 pipeline
  * Denoising with DADA2
- Taxonomic Classification
  * SILVA database
  * 97% similarity threshold
'''

    # Save dataset info as markdown and create image
    with open('images/dataset_description.md', 'w') as f:
        f.write(dataset_info)
    
    # Create dataset description image
    create_markdown_image(dataset_info, 'images/dataset_description.png')
    
    # Code snippets for each visualization
    distribution_code = '''
def analyze_bacteria_distribution(data):
    """
    Analyze and visualize the distribution of bacterial phyla
    in the microbiome samples.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        Contains columns for each bacteria phylum with their
        relative abundance values
    """
    # Set visualization style
    sns.set_theme(style="whitegrid")
    
    # Create violin plot to show distribution
    sns.violinplot(data=data, palette="Set3")
    plt.ylabel('Relative Abundance (%)')
    plt.xticks(rotation=45)
    
    # Add statistical summary
    print("Statistical Summary:")
    for phylum in data.columns:
        mean = data[phylum].mean()
        std = data[phylum].std()
        print(f"{phylum}:")
        print(f"  Mean: {mean:.2f}%")
        print(f"  Std:  {std:.2f}%")
'''
    
    # Create plot with code
    create_plot_with_code(
        create_bacteria_distribution,
        distribution_code,
        "Gut Microbiome Data Distribution",
        "images/bacteria_distribution.png",
        figsize=(15, 10)
    ) 