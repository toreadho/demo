from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import json
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'oracle://wh:Admin135@127.0.0.1:1521/orcl'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 分类
class Category(db.Model):
    __tablename__ = "第十八批_医保医用耗材汇总"
    货物码 = db.Column(db.String(100),primary_key=True)
    原27位码 = db.Column(db.String(50))
    现27位码 = db.Column(db.String(50))
    单件产品名称 = db.Column(db.String(50))
    注册备案号 = db.Column(db.String(50))
    规格 = db.Column(db.String(50))
    型号 = db.Column(db.String(50))
    耗材企业 = db.Column(db.String(60))
    原码状态 = db.Column(db.String(50))
    类型 = db.Column(db.String(50))


#result = Category.query.filter(Category.规格 == '116cm*25cm').all()                        #单个查
from sqlalchemy import and_
result = Category.query.filter(and_(Category.规格 == '116cm*25cm',Category.耗材企业=='新乡市宏达卫材有限公司')).all()    #and

#from sqlalchemy import or_
#result = Category.query.filter(or_(Category.规格 == '116cm*25cm',Category.耗材企业=='新乡市宏达卫材有限公司')).all()    #OR
NLst = []
for x in range(len(result)):
    CLInfo = {'单件产品名称': result[x].单件产品名称,
              '原27位码': result[x].原27位码,
              '原码状态': result[x].原码状态,
              '27位码': result[x].现27位码,
              '类型': result[x].类型,
              '注册备案号': result[x].注册备案号,
              '规格': result[x].规格,
              '型号': result[x].型号,
              '耗材企业': result[x].耗材企业
              }
    NLst.append(CLInfo)
print(NLst)




