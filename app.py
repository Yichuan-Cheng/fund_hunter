from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy

page_size=10

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path. join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JSON_AS_ASCII"] = False
db = SQLAlchemy(app)

class Fund(db.Model):
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
    fund_profit_std=db.Column(db.String(50))# 收益率标准差
    fund_beta=db.Column(db.String(50))# 贝塔系数
    fund_r_mean=db.Column(db.String(50))# 平均收益率
    fund_treynor=db.Column(db.String(50))# treynor系数
    fund_sharpe=db.Column(db.String(50))# sharpe系数
    fund_jense=db.Column(db.String(50))# jense系数

class Company(db.Model):
    company_name=db.Column(db.String(25), primary_key=True)# 公司名称
    company_created_time=db.Column(db.String(20))# 公司成立时间
    company_fund_num=db.Column(db.String(10))# 公司基金数量
    company_updated_time=db.Column(db.String(20))# 公司信息更新时间

def insert_fund(
    fund_id,
    fund_name,
    fund_abbr,
    fund_type,
    fund_updated_time,
    fund_unit_value,
    fund_accumulation_value,
    fund_day_rate,
    fund_week_rate,
    fund_month_rate,
    fund_3month_rate,
    fund_birth_rate,
    fund_dates,
    fund_rates,
    fund_values,
    fund_all_values,
    fund_profit_std,
    fund_beta,
    fund_r_mean,
    fund_treynor,
    fund_sharpe,
    fund_jense
    ):
    db.session.execute(
        Fund.__table__.insert(),
        [
            {
                "fund_id":fund_id[i],
                'fund_name':fund_name[i],
                'fund_abbr':fund_abbr[i],
                'fund_type':fund_type[i],
                'fund_updated_time':fund_updated_time[i],
                'fund_unit_value':fund_unit_value[i],
                'fund_accumulation_value':fund_accumulation_value[i],
                'fund_day_rate':fund_day_rate[i],
                'fund_week_rate':fund_week_rate[i],
                'fund_month_rate':fund_month_rate[i],
                'fund_3month_rate':fund_3month_rate[i],
                'fund_birth_rate':fund_birth_rate[i],
                'fund_dates':fund_dates[i],
                'fund_rates':fund_rates[i],
                'fund_values':fund_values[i],
                'fund_all_values':fund_all_values[i],
                'fund_profit_std':fund_profit_std[i],
                'fund_beta':fund_beta[i],
                'fund_r_mean':fund_r_mean[i],
                'fund_treynor':fund_treynor[i],
                'fund_sharpe':fund_sharpe[i],
                'fund_jense':fund_jense[i]
            } 
            for i in range(len(fund_id))
        ]
    )
    db.session.commit()

def insert_company(company_name,company_created_time,company_fund_num,company_updated_time):
    db.session.execute(Company.__table__.insert(),
        [
            {
                'company_name':company_name[i],
                'company_created_time':company_created_time[i],
                'company_fund_num':company_fund_num[i],
                'company_updated_time':company_updated_time[i]
            }
            for i in range(len(company_name))
        ]
    )
    db.session.commit()


@app.route('/')
def index_():
    return '成功!'

@app.route('/all_company/<int:page_num>',methods=['post','get'])
def get_all_company(page_num):
    tmp=Company.query.paginate(per_page=10,page=page_num,error_out=False).items
    return {
        i+(page_num-1)*page_size:{
            'company_name':tmp[i].company_name,
            'company_created_time':tmp[i].company_created_time,
            'company_fund_num':tmp[i].company_fund_num,
            'company_updated_time':tmp[i].company_updated_time
        } 
        for i in range(len(tmp))
    }

@app.route('/all_fund/<int:page_num>',methods=['post','get'])
def get_all_fund(page_num):
    tmp=Fund.query.paginate(per_page=10,page=page_num,error_out=False).items
    return {
        i+(page_num-1)*page_size:{
            "fund_id":tmp[i].fund_id,
            'fund_name':tmp[i].fund_name,
            'fund_abbr':tmp[i].fund_abbr,
            'fund_type':tmp[i].fund_type,
            'fund_updated_time':tmp[i].fund_updated_time,
            'fund_unit_value':tmp[i].fund_unit_value,
            'fund_accumulation_value':tmp[i].fund_accumulation_value,
            'fund_day_rate':tmp[i].fund_day_rate,
            'fund_week_rate':tmp[i].fund_week_rate,
            'fund_month_rate':tmp[i].fund_month_rate,
            'fund_3month_rate':tmp[i].fund_3month_rate,
            'fund_birth_rate':tmp[i].fund_birth_rate,
            'fund_dates':tmp[i].fund_dates,
            'fund_rates':tmp[i].fund_rates,
            'fund_values':tmp[i].fund_values,
            'fund_all_values':tmp[i].fund_all_values,
            'fund_profit_std':tmp[i].fund_profit_std[:5],
            'fund_beta':tmp[i].fund_beta[:5],
            'fund_r_mean':tmp[i].fund_r_mean[:5],
            'fund_treynor':tmp[i].fund_treynor[:5],
            'fund_sharpe':tmp[i].fund_sharpe[:5],
            'fund_jense':tmp[i].fund_jense[:5]
        } 
        for i in range(len(tmp))
    }

@app.route('/get_company_by_name/<string:name>',methods=['post','get'])
def get_company_by_name(name):
    tmp=Company.query.get(name)
    return {
        'company_name':tmp.company_name,
        'company_created_time':tmp.company_created_time,
        'company_fund_num':tmp.company_fund_num,
        'company_updated_time':tmp.company_updated_time
    } 

@app.route('/get_fund_by_id/<string:id>',methods=['post','get'])
def get_fund_by_name(id):
    tmp=Fund.query.get(id)
    return {
        "fund_id":tmp.fund_id,
        'fund_name':tmp.fund_name,
        'fund_abbr':tmp.fund_abbr,
        'fund_type':tmp.fund_type,
        'fund_updated_time':tmp.fund_updated_time,
        'fund_unit_value':tmp.fund_unit_value,
        'fund_accumulation_value':tmp.fund_accumulation_value,
        'fund_day_rate':tmp.fund_day_rate,
        'fund_week_rate':tmp.fund_week_rate,
        'fund_month_rate':tmp.fund_month_rate,
        'fund_3month_rate':tmp.fund_3month_rate,
        'fund_birth_rate':tmp.fund_birth_rate,
        'fund_dates':tmp.fund_dates,
        'fund_rates':tmp.fund_rates,
        'fund_values':tmp.fund_values,
        'fund_all_values':tmp.fund_all_values,
        'fund_profit_std':tmp.fund_profit_std[:5],
        'fund_beta':tmp.fund_beta[:5],
        'fund_r_mean':tmp.fund_r_mean[:5],
        'fund_treynor':tmp.fund_treynor[:5],
        'fund_sharpe':tmp.fund_sharpe[:5],
        'fund_jense':tmp.fund_jense[:5]
    } 

@app.route('/get_fund_count',methods=['post','get'])
def get_fund_count():
    return str(Fund.query.count())

@app.route('/get_company_count',methods=['post','get'])
def get_company_count():
    return str(Company.query.count())


if(__name__=='__main__'):
    app.run('0.0.0.0',port=80,debug=False)
