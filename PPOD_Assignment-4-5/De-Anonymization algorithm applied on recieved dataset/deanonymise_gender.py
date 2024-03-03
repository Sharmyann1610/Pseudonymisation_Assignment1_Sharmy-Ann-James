import pandas as pd

# Load the anonymized dataset
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Identify the most frequent 'gender' for each group
mode_gender_per_state = anonymized_df.groupby('state')['gender'].agg(lambda x: x.mode().iloc[0] if not x.empty else None).to_dict()

# Replace the anonymized 'gender' with the mode for each group
anonymized_df['gender'] = anonymized_df.apply(lambda row: mode_gender_per_state.get(row['state'], None), axis=1)

# Save the deanonymized dataset
anonymized_df.to_csv('deanonymized_output_task_gender.csv', index=False)