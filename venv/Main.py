import pandas as pd
import matplotlib.pyplot as plt

df_sii = pd.read_csv('107_sii.csv')
df_otc = pd.read_csv('107_sii.csv')

df_sii.shape
# (853, 13) 共有 853 家上市公司資料，13 個欄位
df_otc.shape
# (733, 13) 共有 733 家上市公司資料，13 個欄位
df_sii.index
# RangeIndex(start=0, stop=853, step=1)
#df_sii.values
#df_sii.columns
#df_sii.info()
#df_sii.head()

headers = ['industry','company_code', 'company_people_count', 'company_name', 'company_total_salary', 'company_average_salary', 'company_eps', 'industry_average_salary', 'industry_average_eps', 'is_under_50', 'high_eps_low_salary', 'growth_but_low_salary', 'low_salary_reason']
df_sii.columns = headers
df_otc.columns = headers

#df_sii.columns

df_sii['company_average_salary'] = df_sii['company_average_salary'].str.replace(',', '').astype(int)
df_otc['company_average_salary'] = df_otc['company_average_salary'].str.replace(',', '').astype(int)

df_sii.head()
df_sii.describe()
df_sii.sort_values(['company_average_salary'], ascending=False)
df_sii.sort_values(['company_average_salary'], ascending=True)

top20_valuable_stock_list = [2330, 2317, 6505, 2412, 1301, 3008, 1303, 1326, 2882, 2454, 1216, 2881, 2886, 2891, 2308,
                             2002, 3045, 2912, 3711, 2892]
df_sii[df_sii['company_code'].isin(top20_valuable_stock_list)]

df_otc_ec = df_otc[df_otc['industry'].isin(['電子商務'])]
df_otc_ec.company_average_salary = pd.to_numeric(df_otc_ec.company_average_salary)
df_otc_ec.loc[:, ['company_code', 'company_average_salary']].plot(kind='bar', x='company_code', y='company_average_salary', title ="TW EC", figsize=(15, 10), legend=True, fontsize=12)