import os
import sys
import shutil

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graphics.create_banner import create_project_banner
from charts.progress_tracker import create_progress_chart
from charts.risk_matrix import create_risk_matrix
from charts.model_performance import create_model_performance
from diagrams.architecture import create_architecture_diagram
from charts.dataset_viz import create_dataset_visualization
from charts.timeline import create_timeline

def ensure_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_directory(path):
    """Remove all files in directory"""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def generate_image(generator_func, image_name):
    """Generate image with error handling"""
    try:
        generator_func()
        print(f"Successfully generated {image_name}")
    except Exception as e:
        print(f"Error generating {image_name}: {str(e)}")
        raise e

def main():
    # Clean and recreate images directory
    clean_directory('images')
    
    # Generate all images with error handling
    image_generators = [
        (create_project_banner, 'project_banner.png'),
        (create_progress_chart, 'progress_chart.png'),
        (create_risk_matrix, 'risk_matrix.png'),
        (create_model_performance, 'model_performance.png'),
        (create_architecture_diagram, 'architecture.png'),
        (create_dataset_visualization, 'dataset_visualization.png'),
        (create_timeline, 'timeline.png'),
    ]
    
    for generator_func, image_name in image_generators:
        generate_image(generator_func, image_name)
        print(f"Generated {image_name}")

if __name__ == "__main__":
    main() 