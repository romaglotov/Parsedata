import pandas as pd
import glob
for filename in glob.glob(r'D:\intelligence-systems\origin_data_ps\*1.csv'):
    df_gen = pd.read_csv(filename, index_col=0)
    for i in range(2, 8):
        temp = filename[filename.find('mx_ps'):len(filename) - 5] + str(i) + '.csv'
        df_loc = pd.read_csv(r'D:\intelligence-systems\origin_data_ps\%s' % temp, index_col=0)
        df_percent = pd.DataFrame(columns=df_gen.columns, index=df_gen.index)
        df_percent = df_percent.fillna(0.0)
        for index, row in df_gen.iterrows():
            for column, columns in df_gen.items():
                if df_gen[column][index] > 0:
                    df_percent[column][index] = (df_loc[column][index] / df_gen[column][index]).round(6)
                    print(df_percent[column][index])
        pd.DataFrame(df_percent).round(6).to_csv(r'D:\intelligence-systems\origin_data_ps_prc\mx_ps_pc%s' % temp[temp.find('mx_ps') + 4:])