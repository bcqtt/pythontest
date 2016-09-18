'''
Created on 2016年9月18日
计算各属性的信息增益，找出最大者为根节点
先验熵：没有接收到其他属性时的平均不确定性
    样板数据中，先求出各种值出现的概率P(ui),再利用公式求熵
后验熵：接收到输出符号Vj时关于信源的不确定性
    对其他列，先求出各种值出现的概率P(vi),再求出先验列中各种值对本列取值为vi时的概率P(u|vi),再根据公式求熵H(U|vi),把u为各种值的情况下的H(U|vi)算出来
条件熵：对后验熵在输出符号集V中求期望，接收到全部符号后对信源的不确定性
  根据后验熵得到的P(vi)乘以H(U|vi)之和
互信息（信息增益）：先验熵与条件熵的差，是信宿端所获得信息量
  先验熵中求得的P(ui)减去条件熵
对剩余属性重复上述步骤
@author: laizhiwen
'''
from db import mysqlutils
import math
from caipiao.model.Entropy import Entropy

# 求样本记录总数
def getSummer():
    sql = "select count(*) sum from two_color_balls;"
    dbbean = mysqlutils.DBBean()
    cursor = dbbean.getCursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        dbbean.closeCursor()
    except :
        print("错误：未能读取数据库。")
    #print(data['sum'])
    return data['sum']



# red1 求先验熵
def prioriEntropy():
    sql = "select red1, count(red1) as coun from two_color_balls group by red1"
    dbbean = mysqlutils.DBBean()
    cursor = dbbean.getCursor()
    r1 = []
    p_r1 = []
    p_r1_u_list = []
    cursor.execute(sql)
    data = cursor.fetchall()
    dbbean.closeCursor()
    
    summer = getSummer()
    h_r1 = 0.0
    for row in data :
        r1.append(row['red1'])
        p_r1_u = row['coun']/summer
        p_r1_u_list.append(p_r1_u)
        h_r1 -= p_r1_u*math.log(p_r1_u,2)
        #print("%s : %s : %s" % (row['red1'], row['coun'],row['coun']/summer))
    
    entropy = Entropy(r1,h_r1,None,None)
    print("H(red1)=%s bit" % h_r1)
    return entropy

# 对red2求后验熵
def posteriorEntropy():
    sql = "select red2, count(red2) as coun from two_color_balls group by red2"
    dbbean = mysqlutils.DBBean()
    cursor = dbbean.getCursor()
    p_r2 = []
    p_r2_u_list = []
    cursor.execute(sql)
    data = cursor.fetchall()
    
    ent = prioriEntropy()
    summer = getSummer()
    r2 = 0.0
    h_red2 = []
    h_uv = 0.0  #条件熵
    for row in data :
        r2=row['red2']
        p_r2_u = row['coun']/summer
        p_r2_u_list.append(p_r2_u)
        
        #red2的后验熵
        huv = 0.0
        for r in ent.r:
            sql = "select count(*) as coun from two_color_balls where red1=%s and red2=%s ;" % (r,row['red2'])
            cursor.execute(sql)
            data = cursor.fetchone()
            puv = data['coun']/summer
            #print("值的后验概率：%s : %s : %s" % (r,r2,puv))
            if puv == 0:
                continue
            else :
                huv -= puv*math.log(puv,2)
        #print("值的后验熵：%s : %s " % (r2,huv))
        h_red2.append(huv)
        
        #red2的条件熵
        h_uv += p_r2_u*huv
    # red2的信息增益
    I_red2 = ent.H-h_uv
    print("red2的信息增益：%s" % I_red2)

    dbbean.closeCursor()

posteriorEntropy()
