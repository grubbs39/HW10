import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


#Chart_1
df = pd.read_excel('Grantt_Chart_1.xlsx')
df

# project start date
proj_start = df.Start.min()# number of days from project start to task start
df['start_num'] = (df.Start-proj_start).dt.days# number of days from project start to end of tasks
df['end_num'] = (df.End-proj_start).dt.days# days between start and end of each task
df['days_start_to_end'] = df.end_num - df.start_num

def color(row):
    c_dict = {'James':'#E64646', 'John':'#E69646', 'Avery':'#34D05C', 'Jeffrey':'#34D0C3', 'Nick':'#3475D0'}
    return c_dict[row['Department']]
df['color'] = df.apply(color, axis=1)

# days between start and current progression of each task
df['current_num'] = (df.days_start_to_end * df.Completion)

fig, ax = plt.subplots(1, figsize=(16,6))

# bars
ax.barh(df.Task, df.current_num, left=df.start_num, color=df.color)
ax.barh(df.Task, df.days_start_to_end, left=df.start_num, color=df.color, alpha=0.5)

# texts
for idx, row in df.iterrows():
    ax.text(row.end_num+0.1, idx,
            f"{int(row.Completion*100)}%",
            va='center', alpha=0.8)

##### LEGENDS #####
c_dict = {'James':'#E64646', 'John':'#E69646', 'Avery':'#34D05C', 'Jeffrey':'#34D0C3', 'Nick':'#3475D0'}
legend_elements = [Patch(facecolor=c_dict[i], label=i)  for i in c_dict]
plt.legend(handles=legend_elements)

##### TICKS #####
xticks = np.arange(0, df.end_num.max()+1, 3)
xticks_labels = pd.date_range(proj_start, end=df.End.max()).strftime("%m/%d")
xticks_minor = np.arange(0, df.end_num.max()+1, 1)

ax.set_xticks(xticks)
ax.set_xticks(xticks_minor, minor=True)
ax.set_xticklabels(xticks_labels[::3])
plt.title("Game Data Management")
plt.show()



#Chart_2
df = pd.read_excel('Grantt_Chart_2.xlsx')
df

# project start date
proj_start = df.Start.min()# number of days from project start to task start
df['start_num'] = (df.Start-proj_start).dt.days# number of days from project start to end of tasks
df['end_num'] = (df.End-proj_start).dt.days# days between start and end of each task
df['days_start_to_end'] = df.end_num - df.start_num

def color(row):
    c_dict = {'James':'#E64646', 'John':'#E69646', 'Avery':'#34D05C', 'Jeffrey':'#34D0C3', 'Nick':'#3475D0'}
    return c_dict[row['Department']]
df['color'] = df.apply(color, axis=1)

# days between start and current progression of each task
df['current_num'] = (df.days_start_to_end * df.Completion)

fig, ax = plt.subplots(1, figsize=(16,6))

# bars
ax.barh(df.Task, df.current_num, left=df.start_num, color=df.color)
ax.barh(df.Task, df.days_start_to_end, left=df.start_num, color=df.color, alpha=0.5)

# texts
for idx, row in df.iterrows():
    ax.text(row.end_num+0.1, idx,
            f"{int(row.Completion*100)}%",
            va='center', alpha=0.8)

##### LEGENDS #####
c_dict = {'James':'#E64646', 'John':'#E69646', 'Avery':'#34D05C', 'Jeffrey':'#34D0C3', 'Nick':'#3475D0'}
legend_elements = [Patch(facecolor=c_dict[i], label=i)  for i in c_dict]
plt.legend(handles=legend_elements)

##### TICKS #####
xticks = np.arange(0, df.end_num.max()+1, 3)
xticks_labels = pd.date_range(proj_start, end=df.End.max()).strftime("%m/%d")
xticks_minor = np.arange(0, df.end_num.max()+1, 1)

ax.set_xticks(xticks)
ax.set_xticks(xticks_minor, minor=True)
ax.set_xticklabels(xticks_labels[::3])
plt.title("User Interface")
plt.show()
