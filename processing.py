import pandas as pd
import numpy as np
import glob

for i in range(1, 8):
    df_player_names = np.array([])
    for filename in glob.glob(r'D:\intelligence-systems\origin_data_base\*1.csv'):
        df_gen = pd.read_csv(filename, index_col=0).drop_duplicates()
        cur = pd.unique(df_gen[['0', '1']].values.ravel('K'))
        df_player_names = np.concatenate((df_player_names, cur), axis=0)

    df_player_names = np.unique(df_player_names)
    passes_gen = pd.DataFrame(columns=df_player_names, index=df_player_names).fillna(0.0)
    games_gen = pd.DataFrame(columns=df_player_names, index=df_player_names).fillna(0.0)
    avg_gen = pd.DataFrame(columns=df_player_names, index=df_player_names).fillna(0.0)

    for filename in glob.glob(r'D:\intelligence-systems\origin_data_ps\*%s.csv' % i):
        df_gen = pd.read_csv(filename, index_col=0)
        for index, row in df_gen.iterrows():
            for column, columns in df_gen.items():
                passes_gen[column][index] += df_gen[column][index]
                games_gen[column][index] += 1

    for index, row in avg_gen.iterrows():
        for column, columns in avg_gen.items():
            if games_gen[column][index] > 0:
                avg_gen[column][index] = (passes_gen[column][index] / games_gen[column][index]).round(6)

    pd.DataFrame(avg_gen).round(6).to_csv(r'D:\intelligence-systems\gen_matrix\avg_gen_%s.csv' % i)
    pd.DataFrame(passes_gen).round(6).to_csv(r'D:\intelligence-systems\gen_matrix\passes_gen_%s.csv' % i)
    pd.DataFrame(games_gen).round(6).to_csv(r'D:\intelligence-systems\gen_matrix\games_gen_%s.csv' % i)