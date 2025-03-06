import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from src.utils.code_display import create_code_snapshot
from src.utils.plot_utils import create_plot_with_code

def create_performance_plot(ax):
    # Set style for this plot
    sns.set_theme(style="whitegrid")
    
    # Performance data
    metrics = {
        'Model': ['Random Forest', 'XGBoost', 'DNN'] * 4,
        'Metric': ['Accuracy', 'Accuracy', 'Accuracy',
                  'Precision', 'Precision', 'Precision',
                  'Recall', 'Recall', 'Recall',
                  'F1', 'F1', 'F1'],
        'Score': [0.85, 0.87, 0.83,
                 0.84, 0.86, 0.82,
                 0.83, 0.85, 0.81,
                 0.83, 0.85, 0.81]
    }
    df = pd.DataFrame(metrics)
    
    # Create plot
    sns.barplot(data=df, x='Model', y='Score', hue='Metric', ax=ax)
    ax.set_ylabel('Score')
    ax.grid(True, alpha=0.3)
    
    # Customize legend
    ax.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

def create_model_performance():
    # Code snippet
    performance_code = '''
def train_and_evaluate_models(X, y):
    # Initialize models with optimized parameters
    models = {
        'Random Forest': RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        ),
        'XGBoost': XGBClassifier(
            n_estimators=100,
            max_depth=10,
            learning_rate=0.1
        ),
        'DNN': Sequential([
            Dense(64, activation='relu'),
            Dropout(0.3),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
    }
    
    # Train and evaluate each model
    results = {}
    for name, model in models.items():
        # Train model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        results[name] = {
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred),
            'Recall': recall_score(y_test, y_pred),
            'F1': f1_score(y_test, y_pred)
        }
    return results
'''
    
    # Create plot with code
    create_plot_with_code(
        create_performance_plot,
        performance_code,
        "Model Performance Analysis",
        "images/model_performance.png",
        figsize=(15, 12)
    )

    # Create code snapshot
    code = '''
# Model Training Code Snippet
def train_model(X_train, y_train, model_type='rf'):
    if model_type == 'rf':
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
    elif model_type == 'xgb':
        model = XGBClassifier(
            n_estimators=100,
            max_depth=10,
            learning_rate=0.1
        )
    else:
        model = Sequential([
            Dense(64, activation='relu'),
            Dropout(0.3),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
    
    return model.fit(X_train, y_train)
'''
    create_code_snapshot(code, 'model_training_code') 