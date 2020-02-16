import pandas as pd
import glob
for filename in glob.glob(r'D:\intelligence-systems\origin_data_base\*1.csv'):
    df_gen = pd.read_csv(filename, index_col=0).drop_duplicates()
    df_player_names = pd.unique(df_gen[['0', '1']].values.ravel('K'))
    matrix_gen = pd.DataFrame(columns=df_player_names, index=df_player_names)
    for index, row in df_gen.iterrows():
        matrix_gen[df_gen['0'][index]][df_gen['1'][index]] = df_gen['2'][index]
        matrix_gen[df_gen['1'][index]][df_gen['0'][index]] = df_gen['3'][index]
    matrix_gen = matrix_gen.fillna(0)
    pd.DataFrame(matrix_gen).to_csv(r'D:\intelligence-systems\origin_data_ps\mx_ps%s' % filename[filename.find('df') + 2:])

    for i in range(2, 8):
        temp = filename[filename.find('df'):len(filename) - 5] + str(i) + '.csv'
        df_loc = pd.read_csv(r'D:\intelligence-systems\origin_data_base\%s' % temp, index_col=0).drop_duplicates()
        df_player_names = pd.unique(df_loc[['0', '1']].values.ravel('K'))
        matrix_loc = pd.DataFrame(columns=matrix_gen.columns, index=matrix_gen.index)
        for index, row in df_loc.iterrows():
            matrix_loc[df_loc['0'][index]][df_loc['1'][index]] = df_loc['2'][index]
            matrix_loc[df_loc['1'][index]][df_loc['0'][index]] = df_loc['3'][index]
        matrix_loc = matrix_loc.fillna(0)
        pd.DataFrame(matrix_loc).to_csv(r'D:\intelligence-systems\origin_data_ps\mx_ps%s' % temp[temp.find('df') + 2:])