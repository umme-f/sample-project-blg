import pandas as pd,os

def merge_csv(folder):
    combine_cpu = pd.DataFrame()
    combine_mem = pd.DataFrame()
    combine_net = pd.DataFrame()

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            if 'cpu' in filename.lower():
                df = pd.read_csv(os.path.join(folder, filename), encoding_errors='ignore')
                combine_cpu = pd.concat([combine_cpu, df])
            elif 'mem' in filename.lower():
                df = pd.read_csv(os.path.join(folder, filename), encoding_errors='ignore')
                combine_mem = pd.concat([combine_mem, df])
            elif 'net' in filename.lower():
                df = pd.read_csv(os.path.join(folder, filename), encoding_errors='ignore')
                combine_net = pd.concat([combine_net, df])

    # Drop weekends
    combine_cpu['DateTime'] = pd.to_datetime(combine_cpu['DateTime'])
    combine_cpu = combine_cpu[combine_cpu['DateTime'].dt.dayofweek < 5]

    # Filter timestamps
    combine_cpu = combine_cpu[(combine_cpu['DateTime'].dt.time >= pd.to_datetime('08:30:00').time()) & 
                              (combine_cpu['DateTime'].dt.time <= pd.to_datetime('17:15:00').time())]

    combine_cpu.to_csv(os.path.join(folder, 'ap-combine.csv'), index=False)
    combine_mem.to_csv(os.path.join(folder, 'db-combine.csv'), index=False)
    combine_net.to_csv(os.path.join(folder, 'net-combine.csv'), index=False)
