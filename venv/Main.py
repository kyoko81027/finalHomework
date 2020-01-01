import pandas as pd
import matplotlib.pyplot as plt

df_sii = pd.read_csv('t187ap05_L.csv')
df_otc = pd.read_csv('t187ap05_L.csv')

df_sii.shape
# (853, 13) 共有 853 家上市公司資料，13 個欄位
df_otc.shape
# (733, 13) 共有 733 家上市公司資料，13 個欄位
df_sii.index
# RangeIndex(start=0, stop=853, step=1)
df_sii.values
df_sii.columns