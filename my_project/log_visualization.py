import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


csv_file_path = r"D:\my_project\parsed_log_output.csv"
df = pd.read_csv(csv_file_path)


print("Columns in CSV:", df.columns)
print(df.head())


print("\nMissing values in the dataset:")
print(df.isnull().sum())


df.dropna(subset=['action', 'user', 'timestamp'], inplace=True)


df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')


fig, axs = plt.subplots(2, 2, figsize=(12, 12))  
fig.tight_layout(pad=4.0)


if 'action' in df.columns:
    action_counts = df['action'].value_counts()
    axs[0, 0].bar(action_counts.index, action_counts.values, color='skyblue')
    axs[0, 0].set_title('Count of Different Actions')
    axs[0, 0].set_xlabel('Action')
    axs[0, 0].set_ylabel('Count')
    axs[0, 0].tick_params(axis='x', rotation=45)


if 'action' in df.columns:
    action_counts = df['action'].value_counts()
    axs[0, 1].pie(action_counts, labels=action_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel", len(action_counts)))
    axs[0, 1].set_title('Action Distribution')


if 'timestamp' in df.columns:
    action_time_series = df.set_index('timestamp')['action'].resample('D').count()
    axs[1, 0].plot(action_time_series.index, action_time_series.values, color='green')
    axs[1, 0].set_title('Actions Count Over Time (Daily)')
    axs[1, 0].set_xlabel('Date')
    axs[1, 0].set_ylabel('Action Count')
    axs[1, 0].tick_params(axis='x', rotation=45)


if 'timestamp' in df.columns:
    actions_per_day = df.groupby(df['timestamp'].dt.date)['action'].count()
    axs[1, 1].bar(actions_per_day.index, actions_per_day.values, color='lightseagreen')
    axs[1, 1].set_title('Actions Count Per Day')
    axs[1, 1].set_xlabel('Date')
    axs[1, 1].set_ylabel('Number of Actions')
    axs[1, 1].tick_params(axis='x', rotation=45)


output_image_path = r"D:\my_project\combined_visualizations.png"
plt.savefig(output_image_path, bbox_inches='tight')
plt.close()

print(f"All visualizations saved to {output_image_path}")
