fund_num=500
period=31

from app import *
db.drop_all()
db.create_all()

import akshare as ak
import tqdm

tmp=ak.fund_em_aum().astype('str')
insert_company(tmp['基金公司'].values,tmp['成立时间'].values,tmp['全部基金数'].values,tmp['更新日期'].values)


import datetime

start_time=(datetime.datetime.now() - datetime.timedelta(days = period))
start_time=start_time.strftime("%Y%m%d")

end_time=(datetime.datetime.now() - datetime.timedelta(days = 1))
end_time=end_time.strftime("%Y%m%d")


import numpy as np
tmp1=ak.fund_name_em()[['基金代码','基金类型','拼音缩写']]
tmp1.replace({'':None},inplace=True)
tmp1.dropna(inplace=True)
tmp2=ak.fund_em_open_fund_rank()
tmp2.drop(columns=['近6月','近1年','近2年','近3年','今年来','自定义','手续费','序号'],inplace=True)
tmp2.replace({'':None},inplace=True)
tmp2.dropna(inplace=True)
tmp2=tmp2.sample(fund_num)
tmp1=tmp2=tmp2.merge(tmp1,on='基金代码').reset_index(drop=True)
tmp1=tmp1.astype('str')

dates=[]
rates=[]
values=[]
all_values=[]
for i in tqdm.tqdm(tmp1['基金代码'].values):
    tmp=ak.fund_etf_fund_info_em(i,start_date=start_time,end_date=end_time)
    tmp.sort_values('净值日期',inplace=True)
    tmp=tmp.astype('str')
    tmp_dates=list(tmp['净值日期'].values)
    tmp_rates=list(tmp['日增长率'].values)
    tmp_values=list(tmp['单位净值'].values)
    tmp_all_values=list(tmp['累计净值'].values)
    dates.append(','.join(tmp_dates))
    rates.append(','.join(tmp_rates))
    values.append(','.join(tmp_values))
    all_values.append(','.join(tmp_all_values))
tmp1['dates']=dates
tmp1['rates']=rates
tmp1['values']=values
tmp1['all_values']=all_values

tmp1['dates_lenth']=tmp1['dates'].apply(lambda x:len(x))
tmp=tmp1['dates_lenth'].mode().values[0]
tmp1.drop(index=tmp1[tmp1['dates_lenth']!=tmp].index,inplace=True)

def cal_profit_std(rates):#收益率标准差
    tmp=rates.split(',')
    tmp=[float(i) for i in tmp]
    return str(np.std(tmp))

market=ak.fund_etf_fund_info_em('050002',start_date=start_time,end_date=end_time)#市场收益率
market.sort_values('净值日期',inplace=True)
market=list(market['日增长率'].values)

def cal_beta(rates):#贝塔系数
    tmp=rates.split(',')
    tmp=[float(i) for i in tmp]
    return str(np.cov(tmp,market)[0][1]/np.var(tmp))

country=ak.fund_etf_fund_info_em('511010',start_date=start_time,end_date=end_time)#平均无风险收益率
country.sort_values('净值日期',inplace=True)
country=list(country['日增长率'].values)
country=np.mean(country)

def cal_rates_mean(rates):#平均收益率
    tmp=rates.split(',')
    tmp=[float(i) for i in tmp]
    return str(np.mean(tmp))

tmp1['profit_std']=tmp1['rates'].apply(cal_profit_std)
tmp1['beta']=tmp1['rates'].apply(cal_beta)
tmp1['r_mean']=tmp1['rates'].apply(cal_rates_mean)
tmp1['treynor']=((tmp1['r_mean'].astype('float')-country)/tmp1['beta'].astype('float')).astype('str')
tmp1['sharpe']=((tmp1['r_mean'].astype('float')-country)/tmp1['profit_std'].astype('float')).astype('str')
tmp1['jense']=((tmp1['r_mean'].astype('float')-country)-tmp1['beta'].astype('float')*(np.mean(market)-country)).astype('str')

insert_fund(
    tmp1['基金代码'].values,
    tmp1['基金简称'].values,
    tmp1['拼音缩写'].values,
    tmp1['基金类型'].values,
    tmp1['日期'].values,
    tmp1['单位净值'].values,
    tmp1['累计净值'].values,
    tmp1['日增长率'].values,
    tmp1['近1周'].values,
    tmp1['近1月'].values,
    tmp1['近3月'].values,
    tmp1['成立来'].values,
    tmp1['dates'].values,
    tmp1['rates'].values,
    tmp1['values'].values,
    tmp1['all_values'].values,
    tmp1['profit_std'].values,
    tmp1['beta'].values,
    tmp1['r_mean'].values,
    tmp1['treynor'].values,
    tmp1['sharpe'].values,
    tmp1['jense'].values,
)
