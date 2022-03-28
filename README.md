### 1. 文件结构

|-----app.py

|-----update_db.py

|-----README.md

|-----README.pdf

### 3. 参数

1. update_db.py文件中参数

> fund_nums=100 表示数据库存储100条基金信息，数量越多更新越慢
>
> period=7  表示收集基金7天内的数据

2. app.py文件中参数

> page_size=10 表示页面大小为10，查询所有基金和公司时一次返回10条数据

### 2. 使用

1. 在命令行使用命令pip安装相关依赖包

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask flask_sqlalchemy tqdm akshare
```

2. 运行update_db.py脚本，更新数据库数据，运行前根据需要调整参数
3. 运行app.py脚本

### 3.API

运行app.py脚本后，可在浏览器使用以下API:

> [localhost:5000](http://localhost:5000/)
>
> 跳转到主页，输出success表示成功
>
> [localhost:5000/all_company/2](http://localhost:5000/all_company/2)
>
> 查询所有的公司数据的第2页，以字典返回查询结果

```json
{"10":{"created_time":"1998-12-22","fund_num":381,"name":"鹏华基金管理有限公司","updated_time":"02-22"},
"11":{"created_time":"2002-12-27","fund_num":424,"name":"招商基金管理有限公司","updated_time":"03-07"},
"12":{"created_time":"2005-09-19","fund_num":228,"name":"建信基金管理有限责任公司","updated_time":"01-19"},
"13":{"created_time":"2001-05-28","fund_num":221,"name":"银华基金管理股份有限公司","updated_time":"03-07"},
"14":{"created_time":"2003-09-30","fund_num":71,"name":"兴证全球基金管理有限公司","updated_time":"01-13"},
"15":{"created_time":"1998-06-04","fund_num":309,"name":"华安基金管理有限公司","updated_time":"03-08"},
"16":{"created_time":"2006-07-19","fund_num":238,"name":"中欧基金管理有限公司","updated_time":"03-08"},
"17":{"created_time":"2003-06-12","fund_num":204,"name":"景顺长城基金管理有限公司","updated_time":"03-09"},
"18":{"created_time":"2005-08-04","fund_num":173,"name":"交银施罗德基金管理有限公司","updated_time":"03-02"},
"19":{"created_time":"1998-03-05","fund_num":310,"name":"国泰基金管理有限公司","updated_time":"03-08"}}
```

- 前面的序号表示对应的第几条，属性分别为公司的创建时间，公司基金数量，公司名称，数据更新时间

> [localhost:5000/all_fund/1](http://localhost:5000/all_fund/1)
>
> 查询所有的基金数据的第1页，以字典返回查询结果

```json
{"0":{"abbr":"HXCZHH","fund_type":"混合型-偏股","fund_value":1.019,"id":"000001","name":"华夏成长混合","updated_time":"2022-03-10"},
 "1":{"abbr":"HXCZHH","fund_type":"混合型-偏股","fund_value":null,"id":"000002","name":"华夏成长混合(后端)","updated_time":"近7天无相关信息"},
 "2":{"abbr":"ZHKZZZQA","fund_type":"债券型-可转债","fund_value":0.842,"id":"000003","name":"中海可转债债券A","updated_time":"2022-03-10"},
 "3":{"abbr":"ZHKZZZQC","fund_type":"债券型-可转债","fund_value":0.834,"id":"000004","name":"中海可转债债券C","updated_time":"2022-03-10"},
 "4":{"abbr":"JSZQXYDQZQ","fund_type":"债券型-长债","fund_value":1.0303,"id":"000005","name":"嘉实增强信用定期债券","updated_time":"2022-03-10"},
 "5":{"abbr":"XBLDLHCZHHA","fund_type":"混合型-偏股","fund_value":1.9517,"id":"000006","name":"西部利得量化成长混合A","updated_time":"2022-03-10"},
 "6":{"abbr":"JSZZ500ETFLJA","fund_type":"指数型-股票","fund_value":1.7727,"id":"000008","name":"嘉实中证500ETF联接A","updated_time":"2022-03-10"},
 "7":{"abbr":"YFDTTLCHBA","fund_type":"货币型","fund_value":0.5222,"id":"000009","name":"易方达天天理财货币A","updated_time":"2022-03-10"},
 "8":{"abbr":"YFDTTLCHBB","fund_type":"货币型","fund_value":0.5881,"id":"000010","name":"易方达天天理财货币B","updated_time":"2022-03-10"},
 "9":{"abbr":"HXDPJXHHA","fund_type":"混合型-偏股","fund_value":17.189,"id":"000011","name":"华夏大盘精选混合A","updated_time":"2022-03-10"}}
```

- 前面的序号表示对应的第几条，属性分别为基金的缩写，基金类型，基金净值，基金ID，基金名字，数据更新时间

> [localhost:5000/get_fund_by_id/000001](http://localhost:5000/get_fund_by_id/000001)
>
> 按ID查询基金，返回对应基金的信息

```json
{"abbr":"HXCZHH","fund_type":"混合型-偏股","fund_value":1.019,"id":"000001","name":"华夏成长混合","updated_time":"2022-03-10"}
```

> [localhost:5000/get_company_by_name/华宝基金管理有限公司](http://localhost:5000/get_company_by_name/华宝基金管理有限公司)
>
> 按name查询公司，返回对应公司的信息

```json
{"created_time":"2003-03-07","fund_num":176,"name":"华宝基金管理有限公司","updated_time":"02-11"}
```

> [localhost:5000/get_company_count](http://localhost:5000/get_company_count)
>
> 查询所有公司数量
>
> [localhost:5000/get_fund_count](http://localhost:5000/get_fund_count)
>
> 查询所有基金数量





