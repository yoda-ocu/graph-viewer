# -*- coding: utf-8 -*-
"""サンプルデータの生成"""
import os
import numpy as np
import pandas as pd

if __name__ == '__main__':
    seed = 10
    data_length = 50
    save_file_path = './data/SampleData1.zip'

    np.random.seed(seed)  # Set random seed

    test_data = {'Time': np.linspace(0, 10, data_length), 'Value': np.random.rand(data_length), 'Value2': np.random.rand(data_length)}    
    df = pd.DataFrame.from_dict(test_data).set_index('Time').sort_index(ascending=True)    
    print(df)

    if not os.path.exists(os.path.dirname(save_file_path)): os.makedirs(os.path.dirname(save_file_path))
    df.to_pickle(save_file_path)