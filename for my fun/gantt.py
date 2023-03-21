import matplotlib.pyplot as plt
import pandas as pd

def make_gantt(new_name, new_start, new_finish):
    data = {'Task': ['Task A', 'Task B', 'Task C', 'Task D'],
            'Start': [0, 5, 15, 25],
            'Finish': [5, 15, 25, 35]}
    
    data["Task"].append(new_name)
    data["Start"].append(new_start)
    data["Finish"].append(new_finish)
    
    df = pd.DataFrame(data)

    plt.barh(df['Task'], df['Finish'] - df['Start'], left=df['Start'])
    plt.xlabel('Time')
    plt.ylabel('Task')
    plt.show()


make_gantt("New Task", 35, 50)
