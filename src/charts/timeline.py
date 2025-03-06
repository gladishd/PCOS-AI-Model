import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates

def create_timeline():
    # Define project phases and their dates
    phases = {
        'Phase 1: Initial Development': {
            'start': '2024-03-07',
            'end': '2024-03-21',
            'tasks': [
                'Data preprocessing',
                'Model training',
                'UI development'
            ],
            'color': '#3498db'
        },
        'Phase 2: Core Implementation': {
            'start': '2024-03-22',
            'end': '2024-04-05',
            'tasks': [
                'Data aggregation',
                'Pipeline validation',
                'Frontend dev'
            ],
            'color': '#2ecc71'
        },
        'Phase 3: Integration': {
            'start': '2024-04-06',
            'end': '2024-04-21',
            'tasks': [
                'Clinical partnerships',
                'System testing',
                'Optimization'
            ],
            'color': '#e74c3c'
        }
    }

    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), 
                                  gridspec_kw={'height_ratios': [3, 1]})

    # Convert dates to datetime
    for phase in phases.values():
        phase['start_date'] = datetime.strptime(phase['start'], '%Y-%m-%d')
        phase['end_date'] = datetime.strptime(phase['end'], '%Y-%m-%d')

    # Plot Gantt chart
    y_positions = np.arange(len(phases))
    
    for idx, (phase_name, phase_data) in enumerate(phases.items()):
        start_date = phase_data['start_date']
        end_date = phase_data['end_date']
        duration = (end_date - start_date).days
        
        # Plot phase bar
        ax1.barh(idx, duration, left=start_date, 
                color=phase_data['color'], alpha=0.8,
                height=0.3)
        
        # Calculate task dates by dividing the phase duration
        num_tasks = len(phase_data['tasks'])
        for i, task in enumerate(phase_data['tasks']):
            # Calculate task date as a proportion of the phase duration
            days_offset = (duration * (i + 1)) / (num_tasks + 1)
            task_date = start_date + timedelta(days=days_offset)
            
            # Add task marker
            ax1.scatter(task_date, idx, color='white', 
                       edgecolor='black', zorder=5)
            
            # Add task label with alternating positions
            y_offset = 0.2 if i % 2 == 0 else -0.2
            ax1.annotate(task, (task_date, idx + y_offset),
                        xytext=(0, 0), textcoords='offset points',
                        ha='center', va='center',
                        fontsize=8,
                        bbox=dict(facecolor='white', 
                                edgecolor='none',
                                alpha=0.7,
                                pad=1))

    # Customize Gantt chart
    ax1.set_yticks(y_positions)
    ax1.set_yticklabels(phases.keys())
    ax1.grid(True, alpha=0.3)

    # Format dates for Gantt chart
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.setp(ax1.get_xticklabels(), rotation=45)

    # Add milestone timeline
    milestones = [
        ('Project Start', '2024-03-07', '↑\nStart'),
        ('Pipeline Done', '2024-03-21', '↑\nPipeline'),
        ('Integration', '2024-04-05', '↑\nCore'),
        ('Completion', '2024-04-21', '↑\nDelivery')
    ]

    # Plot milestone timeline
    for milestone, date, label in milestones:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        ax2.scatter(date_obj, 0, color='red', zorder=5)
        ax2.annotate(label, (date_obj, 0),
                    xytext=(0, 10), textcoords='offset points',
                    ha='center', va='bottom')

    # Connect milestones with line
    milestone_dates = [datetime.strptime(m[1], '%Y-%m-%d') for m in milestones]
    ax2.plot(milestone_dates, [0] * len(milestone_dates), 
             color='gray', linestyle='--')

    # Customize milestone timeline
    ax2.grid(True, alpha=0.3)
    ax2.set_yticks([])

    # Format dates for milestone timeline
    ax2.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.setp(ax2.get_xticklabels(), rotation=45)

    # Add single title at the top
    fig.text(0.5, 0.95, 'Project Timeline', 
             fontsize=16, ha='center', va='bottom')

    # Adjust layout with more space at top for title
    plt.subplots_adjust(top=0.9, hspace=0.3)
    
    # Save the figure
    plt.savefig('images/timeline.png', 
                dpi=300, 
                bbox_inches='tight',
                facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_timeline() 