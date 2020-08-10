import numpy as np
import pandas as pd
import os
from pathlib import Path

output = "/home/alex/data/time_series/archives/synthetic/experiment_1"

dirname = Path(__file__)
dirname = dirname.parent.parent

ts_base_dir = os.path.join(dirname, "timeseries")


file_names = {}
for filename in os.listdir(ts_base_dir):
    if filename.endswith(".csv"):
        if filename[0] not in file_names:
            file_names[filename[0]] = []
        file_names[filename[0]].append(filename)


def read_and_merge_ts(ts_base_dir, file_names):
    dfs = [pd.read_csv(os.path.join(ts_base_dir, fn), index_col=0) for fn in file_names]
    df_ts = pd.concat(dfs, axis=1, sort=False, ignore_index=True)
    np_df = df_ts.to_numpy()
    return np_df


np_ts = [read_and_merge_ts(ts_base_dir, file_names) for file_names in file_names.values()]
stacked_np_ts = np.stack(np_ts, axis=0)

labels = np.array(list(file_names.keys()))

np.save(os.path.join(output, "x_train.npy"), stacked_np_ts)
np.save(os.path.join(output, "y_train.npy"), labels)
