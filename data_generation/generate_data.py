import numpy as np
import pandas as pd
import datetime as dt
import gc
import argparse
import time

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate and save survival data.')
parser.add_argument('--n', type=int, default=100000, help='Number of individuals (N)')
parser.add_argument('--database', type=str, default='csv', choices=['mongodb', 'timescaledb', 'questdb', 'influxdb'],
                    help='Target database (mongodb, timescaledb, questdb, influxdb)')
args = parser.parse_args()

# Record the start time
start_time = time.time()

N = args.n
time0 = 0
start = np.random.random(size=N) * 150 - 50
death_probability = np.arange(1, 101) / (50 * 101)
lifetime = np.random.choice(np.arange(100), p=death_probability, replace=True, size=N) + np.random.random(size=N)
censor = np.random.exponential(70, size=N)

df = pd.DataFrame({
    'start_observed': np.maximum(start, time0),
    'age_start_observed': np.maximum(1, time0 - start).astype(int),  
    'age_end': (np.minimum(lifetime, censor) + 1).astype(int), 
    'is_truncated': (start < time0),
    'is_censored': (censor < lifetime),
    'is_dead': (censor >= lifetime)
})

df['end'] = df.age_end + start
df = df.loc[df.end >= time0].sample(frac=1)

del start, lifetime, censor
gc.collect()
date0 = dt.date(year=1950, month=1, day=1)

def convert_interval_to_date(x):
    date = date0 + dt.timedelta(days=int(x * 365.25))
    date = max(date, dt.date(year=1950, month=1, day=1))
    date = min(date, dt.date(year=2020, month=12, day=31))
    return date.strftime('%Y-%m-%d')  
    
df['date_start_observed'] = df.start_observed.apply(convert_interval_to_date)

df['date_end_observed'] = df.end.apply(convert_interval_to_date)

df.drop(columns=['start_observed', 'end'], inplace=True)

df = df[['age_start_observed','age_end','date_start_observed','date_end_observed','is_truncated','is_censored','is_dead']]

gc.collect()

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Dataset creation took {elapsed_time:.2f} seconds.")

# Save data based on the target database format
if args.database == 'mongodb':
    df.to_json('survival_data.json', orient='records', date_format='iso')
else:
    df.to_csv('survival_data.csv', index=False,date_format='%Y-%m-%d')

print(f"Data saved in {args.database} format.")
