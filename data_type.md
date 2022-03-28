```python
    fund_id=db.Column(db.String(6), primary_key=True) #基金代码
    fund_name=db.Column(db.String(25))#基金简称
    fund_abbr=db.Column(db.String(25))#基金缩写
    fund_type=db.Column(db.String(20))#基金类型
    fund_updated_time=db.Column(db.String(20))#基金信息更新时间
    fund_unit_value=db.Column(db.String(6))#基金单位净值
    fund_accumulation_value=db.Column(db.String(6))#基金累计净值
    fund_day_rate=db.Column(db.String(6))#基金日增长率
    fund_week_rate=db.Column(db.String(6))#基金周增长率
    fund_month_rate=db.Column(db.String(6))#基金月增长率
    fund_3month_rate=db.Column(db.String(6))#基金3月增长率
    fund_birth_rate=db.Column(db.String(6))#基金成立来增长率
    fund_dates=db.Column(db.String(300))#基金日期序列
    fund_rates=db.Column(db.String(300))#基金增长率序列
    fund_values=db.Column(db.String(300))#基金单位净值序列
    fund_all_values=db.Column(db.String(300))#基金累计净值序列
    fund_profit_std=db.Column(db.String(6))# 收益率标准差
    fund_beta=db.Column(db.String(15))# 贝塔系数
    fund_r_mean=db.Column(db.String(15))# 平均收益率
    fund_treynor=db.Column(db.String(15))# treynor系数
    fund_sharpe=db.Column(db.String(15))# sharpe系数
    fund_jense=db.Column(db.String(15))# jense系数
```

