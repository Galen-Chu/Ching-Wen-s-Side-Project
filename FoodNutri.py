# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:20:02 2024

@author: student
"""
import MySQLdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 設定中文
plt.rcParams["font.family"]="Microsoft JhengHei"  # 微軟正黑體
plt.rcParams["font.size"]=10
plt.rcParams["axes.unicode_minus"]=False
# 資料庫連接取得data
try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",     # 主機名稱
                            user="root",         # 帳號
                            password="c415sc415sCSCS!?", # 密碼
                            database="project_nutrition",   # 資料庫
                            port=3306,           # port
                            charset="utf8")      # 資料庫編碼
    # 使用cursor()方法操作資料庫
    cursor=conn.cursor()
    try:
        sql="SELECT * FROM project_nutrition._2023_update1_v2_"
        # "SELECT col_0,col_1,col_2,col_3 FROM project_nutrition.food_nutrition_calories"
        cursor.execute(sql)
        data=cursor.fetchall()
        food_need_data=pd.DataFrame(data)
        cursor.close()
        conn.close()
    except Exception as e:
        print("錯誤訊息：", e)
except Exception as e:
    print("資料庫連接失敗：", e)
fooddata=set(food_need_data[1])
food_list_s=[]
cal_list_s=[]
water_list_s=[]
food_list_p=[]
cal_list_p=[]
water_list_p=[]
food_list_o=[]
cal_list_o=[]
water_list_o=[]
food_list_v=[]
cal_list_v=[]
water_list_v=[]
food_list_f=[]
cal_list_f=[]
water_list_f=[]
food_list_m=[]
cal_list_m=[]
water_list_m=[]
for i in range(len(food_need_data.index)):
    if food_need_data.iloc[i,1]=='穀物類' or food_need_data.iloc[i,1]=='澱粉類' or food_need_data.iloc[i,1]=='糕餅點心類'  or food_need_data.iloc[i,1]=='糖類':
        food_list_s.append(food_need_data.iloc[i,2])
        cal_list_s.append(eval(food_need_data.iloc[i,6]))
        water_list_s.append(eval(food_need_data.iloc[i,8]))
    if food_need_data.iloc[i,1]=='魚貝類' or food_need_data.iloc[i,1]=='蛋類' or food_need_data.iloc[i,1]=='豆類' or food_need_data.iloc[i,1]=='肉類':
        food_list_p.append(food_need_data.iloc[i,2])
        cal_list_p.append(eval(food_need_data.iloc[i,6]))
        water_list_p.append(eval(food_need_data.iloc[i,8]))
    if food_need_data.iloc[i,1]=='堅果及種子類' or food_need_data.iloc[i,1]=='油脂類':
        food_list_o.append(food_need_data.iloc[i,2])
        cal_list_o.append(eval(food_need_data.iloc[i,6]))
        water_list_o.append(eval(food_need_data.iloc[i,8]))
    if food_need_data.iloc[i,1]=='蔬菜類' or food_need_data.iloc[i,1]=='菇類' or food_need_data.iloc[i,1]=='藻類':
        food_list_v.append(food_need_data.iloc[i,2])
        cal_list_v.append(eval(food_need_data.iloc[i,6]))
        water_list_v.append(eval(food_need_data.iloc[i,8]))
    if food_need_data.iloc[i,1]=='水果類':
        food_list_f.append(food_need_data.iloc[i,2])
        cal_list_f.append(eval(food_need_data.iloc[i,6]))
        water_list_f.append(eval(food_need_data.iloc[i,8]))
    if food_need_data.iloc[i,1]=='乳品類':
        food_list_m.append(food_need_data.iloc[i,2])
        cal_list_m.append(eval(food_need_data.iloc[i,6]))
        water_list_m.append(eval(food_need_data.iloc[i,8]))
print(food_list_s)
print(cal_list_s)
print(water_list_s)
print('==========================')        
print(food_list_p)
print(cal_list_p)
print(water_list_p)
print('==========================')        
print(food_list_o)
print(cal_list_o)
print(water_list_o)
print('==========================')        
print(food_list_v)
print(cal_list_v)
print(water_list_v)
print('==========================')
print(food_list_f)
print(cal_list_f)
print(water_list_f)
print('==========================')        
print(food_list_m)
print(cal_list_m)
print(water_list_m)
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
import matplotlib.font_manager as fm
fm.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
plt.rc('font',family='Taipei Sans TC Beta')
# Read CSV File in Binary Mode
with open('食品營養成分資料庫2023版UPDATE1(V2).csv','rb') as f:
    data=f.read()
# Detect Encoding using chardet Library
encoding_result=chardet.detect(data)
# Retrieve Encoding Information
encoding=encoding_result['encoding']
# Print Detected Encoding Information
print("Detected Encoding:",encoding)

food_need_data=pd.read_csv('食品營養成分資料庫2023版UPDATE1(V2).csv',encoding='utf-8')
# food_data=food_need_data.drop(index=[2,3,9,10],axis=0)
# food_data.reset_index(drop=True,inplace=True)
# food_data.columns=food_data.iloc[0,:]
# food_data.index=food_data.iloc[:,0]
# food_data=food_data.drop(index=['Column1'],axis=0)
# food_data=food_data.drop(columns=['Column1'],axis=1)

# food_data=food_need_data.drop(index=[0],axis=0)
# food_data.columns=food_data.iloc[0,:]
# food_data=food_data.drop(index=[1],axis=0)

food_need_data.columns=food_need_data.iloc[0,:]
food_data=food_need_data.drop(index=[0],axis=0)
food_data.reset_index(drop=True,inplace=True)
# food_data=food_data.dropna(subset=['整合編號','食品分類'],axis='index')
food_data=food_data.iloc[0:2171,:]
# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
label=np.array(list(set(food_data.iloc[:,1].values)))
count=np.zeros(18)
for i,ii in zip(label,range(18)):
    for n in food_data.iloc[:,1].values:
        if n==i:
            count[ii]+=1      
lc=pd.DataFrame([label,count]).T
lc=lc.sort_values(by=[1],ascending=False)
e=np.zeros(18)
# color_names=['red','orange','yellow','green','blue','purple']
# tickdict={1200:'1200大卡',1500:'1500大卡',1800:'1800大卡',2000:'2000大卡',2200:'2200大卡',2500:'2500大卡',2700:'2700大卡'}
# labeldict={0:'全榖雜糧類(碗)',1:'豆魚蛋肉類(份)',2:'乳品類(杯)',3:'蔬菜類(份)',4:'水果類(份)',5:'油脂與堅果種子類(份)'}
# 圓餅圖
plt.pie(lc[1],
        radius=0.9,
        explode=e,
        startangle=225,
        autopct='%.1f%%',
        textprops={'weight':'bold','size':22},
        pctdistance=1.1,
        labeldistance=1.5,
        wedgeprops={'linewidth':3,'edgecolor':'w'},
        colors=sns.color_palette("husl",18))
# 設定標題
plt.title('食品成份資料集之類別佔比',size=40,loc="center")
plt.legend(title="類別",labels=lc[0],loc="center left",fontsize=25,bbox_to_anchor=(1,0,0.5,1))
plt.savefig('pie.jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()

#長條圖作圖之資料(平均熱量)
food_data_bar=pd.DataFrame([food_data.iloc[:,1],food_data.iloc[:,7].astype('Int32')]).T
# food_data_bar=food_data_bar.sort_values(by=['修正熱量(kcal)'],ascending=False)
# food_data_bar=food_data_bar.groupby(by=['食品分類'])
# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
# data=food_data_bar.groupby(by=['食品分類']).食品分類
data=pd.DataFrame(food_data_bar.groupby(by=['食品分類']).mean())
# seaborn顏色參數
color_names=sns.color_palette("husl",18)
# 長條圖
ax=plt.bar(data.index,data['修正熱量(kcal)'],color=color_names,label=data.index)
plt.bar_label(ax,padding=2,fontsize=20)
# 將x,y軸標籤
plt.xticks(rotation=45,fontsize=20)
plt.xlabel('檢測食物之類別',fontsize=20)
plt.ylabel('平均卡路里量值(kcals)',fontsize=20)
# 調整y軸刻度
plt.ylim(0,900)
# 設定標題
plt.title('食品成份資料集之類別平均卡路里',size=40)
# 設定網格
plt.grid(axis="y", zorder=0)
plt.legend(loc='right',fontsize=20,shadow=True,title='類別',title_fontsize=20,bbox_to_anchor=(1,0,0.3,1))
plt.savefig('bar(cals).jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()

#長條圖作圖之資料(含水量)
food_data_bar=pd.DataFrame([food_data.iloc[:,1],food_data.iloc[:,8].astype('Float64')]).T
# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
# data=food_data_bar.groupby(by=['食品分類']).食品分類
data=pd.DataFrame(food_data_bar.groupby(by=['食品分類']).mean())
# seaborn顏色參數
color_names=sns.color_palette("husl",18)
# 長條圖
ax=plt.bar(data.index,data['水分(g)'],color=color_names,label=data.index)
plt.bar_label(ax,padding=2,fontsize=20)
# 將x,y軸標籤
plt.xticks(rotation=45,fontsize=20)
plt.xlabel('檢測食物之類別',fontsize=20)
plt.ylabel('平均含水量值(g)',fontsize=20)
# 調整y軸刻度
plt.ylim(0,100)
# 設定標題
plt.title('食品成份資料集之類別平均含水量值',size=40)
# 設定網格
plt.grid(axis="y", zorder=0)
plt.legend(loc='right',fontsize=20,shadow=True,title='類別',title_fontsize=20,bbox_to_anchor=(1,0,0.3,1))
plt.savefig('bar(water).jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()
'''
熱功當量
1 cal(卡)=4.186 J(焦耳)=4.186 N·m (牛頓 米)
1 cal(卡)=1g 水升溫 1℃ 
W(瓦，電功率)=Mg(克)*T(℃)=Mg(克)*(Tmax-Tmin)
=0.24*P(電功率)*t(sec) cal(卡)。
mg(熱電偶前端金屬球及導線的質量)*(Tmax-Tmin)=0.24*P(電功率視為不變)*t(ms) cal(卡)
'''
#堆疊長條圖作圖之資料(宏量營養素)
food_data_bar=pd.DataFrame([food_data.iloc[:,1],food_data.iloc[:,9].astype('Float64'),food_data.iloc[:,10].astype('Float64'),food_data.iloc[:,13].astype('Float64')]).T
# food_data_bar=food_data_bar.groupby(by=['食品分類'])
# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
# data=food_data_bar.groupby(by=['食品分類']).食品分類
data=pd.DataFrame(food_data_bar.groupby(by=['食品分類']).mean())
# 堆疊長條圖變數設定
bottom=np.zeros((18,1))
color_names=['coral','magenta','lightgreen']
# seaborn顏色參數
# color_names=sns.color_palette("husl",3)
labeldict={0:'粗蛋白(g)',1:'粗脂肪(g)',2:'總碳水化合物(g)'}
# data.index
# data['總碳水化合物(g)'].values
# 堆疊長條圖
for i,v in labeldict.items():
    plt.bar(data.index,data[v].values,color=color_names[i],label=labeldict[i],bottom=bottom[:,0])
    for key,num in zip(data.index,range(18)):
        bottom[num,0]=bottom[num,0]+data.loc[key,v]
# 將x,y軸標籤
plt.xticks(rotation=45,fontsize=20)
plt.xlabel('檢測食物之類別',fontsize=20)
plt.ylabel('宏量營養素之公克數(g)',fontsize=20)
# 調整y軸刻度
plt.ylim(0,100)
# 設定標題
plt.title('食品成份資料集之類別之宏量營養素量值',size=40)
# 設定網格
plt.grid(axis="y", zorder=0)
plt.legend(loc='right',fontsize=20,shadow=True,title='類別',title_fontsize=20,bbox_to_anchor=(1,0,0.3,1))
plt.savefig('stackbar(macro).jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()

#長條圖作圖之資料(微量營養素)
food_data_bar=food_data.iloc[:,22:55].astype('Float64')
food_data_bar.index=food_data.iloc[:,1]
# food_data_bar=food_data_bar.groupby(by=['食品分類'])
#18項食品類別之標籤
type_amount=pd.DataFrame(count,index=label,columns=['類別總數'])
#長條圖之資料處理、計算次數作為營養素出現之比例
data_times=pd.DataFrame(food_data_bar.groupby(by=['食品分類']).count())
data_times_total=np.zeros((18,1))
for index,num in zip(data_times.index,range(18)):
    for key in data_times.columns:
        data_times_total[num,0]=data_times_total[num,0]+data_times.loc[index,key]
data_times_total=pd.DataFrame(data_times_total,index=data_times.index,columns=['計次比例'])

data_times_total_rate=pd.DataFrame(np.zeros((18,1)),index=data_times.index,columns=['計次比例'])
for key in data_times_total.index:
    data_times_total_rate.loc[key,'計次比例']=data_times_total.loc[key,'計次比例']/type_amount.loc[key,'類別總數']
# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
# data=food_data_bar.groupby(by=['食品分類']).食品分類
# seaborn顏色參數
color_names=sns.color_palette("husl",18)
# 長條圖
plt.bar(data_times_total.index,data_times_total['計次比例'],color=color_names,label=data_times_total.index)
plt.plot(data_times_total_rate.index,data_times_total_rate['計次比例']*100,color='m',marker='o',linewidth=5,markersize=10)
# 將x,y軸標籤
plt.xticks(rotation=45,fontsize=20)
plt.xlabel('檢測食物之類別',fontsize=20)
plt.ylabel('微量營養素之含量累計次數(次數)',fontsize=20)
# 調整y軸刻度
plt.ylim(0,8000)
# 設定標題
plt.title('食品成份資料集之類別之微量營養素含量比重',size=40)
# 設定網格
plt.grid(axis="y", zorder=0)
plt.legend(loc='right',fontsize=20,shadow=True,title='類別',title_fontsize=20,bbox_to_anchor=(1,0,0.35,1))
# 設定第二條y軸
ax=plt.twinx()
ax.set_ylabel('微量營養素之含量比重',color='m')
plt.savefig('linebar(micro).jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()

#18項食品類別之標籤
type_amount=pd.DataFrame(count,index=label,columns=['類別總數'])
#長條圖之資料處理、計算含量平均值作為攝取營養素之參照數值
food_data_bar=food_data.iloc[:,22:55].astype('Float64')
food_data_bar.index=food_data.iloc[:,1]
data_grams=pd.DataFrame(food_data_bar.groupby(by=['食品分類']).mean())
#區分礦物質及維生素
#計算礦物質總量(mg)
data_grams_min=data_grams.iloc[:,0:9]
data_grams_min_tot=pd.DataFrame(np.zeros((18,1)),index=data_grams_min.index,columns=['礦物質總量'])
for index in data_grams_min.index:
    for key in data_grams_min.columns:
        data_grams_min_tot.loc[index,'礦物質總量']=data_grams_min_tot.loc[index,'礦物質總量']+data_grams_min.loc[index,key]
# data_grams_min_tot=data_grams_min_tot/10
#計算礦物質總量比例
data_grams_min_tot_rate=pd.DataFrame(np.zeros((18,1)),index=data_grams_min_tot.index,columns=['總量比例'])
for key in data_grams_min_tot.index:
    data_grams_min_tot_rate.loc[key,'總量比例']=data_grams_min_tot.loc[key,'礦物質總量']/type_amount.loc[key,'類別總數']
#處理維生素資料
#單位換算、全部轉為微克(ug)
data_grams_vit=data_grams.iloc[:,9:]
for index in data_grams_vit.index:
    for key in data_grams_vit.columns:
        if 'IU' in key:
            data_grams_vit.loc[index,key]=data_grams_vit.loc[index,key]*0.025
        elif 'mg' in key:
            data_grams_vit.loc[index,key]=data_grams_vit.loc[index,key]*1000
        else:
            continue
# 1國際單位(IU)=0.025微克(mcg)
#計算維生素總量(ug)
data_grams_vit_tot=pd.DataFrame(np.zeros((18,1)),index=data_grams_vit.index,columns=['維生素總量'])
for index in data_grams_vit.index:
    for key in data_grams_vit.columns:
        data_grams_vit_tot.loc[index,'維生素總量']=data_grams_vit_tot.loc[index,'維生素總量']+data_grams_vit.loc[index,key]
data_grams_vit_tot=data_grams_vit_tot.fillna(0.0)
# data_grams_vit_tot=data_grams_vit_tot/1000
data_grams_vit_tot=data_grams_vit_tot/100
#計算維生素總量比例
data_grams_vit_tot_rate=pd.DataFrame(np.zeros((18,1)),index=data_grams_vit_tot.index,columns=['總量比例'])
for key in data_grams_vit_tot.index:
    data_grams_vit_tot_rate.loc[key,'總量比例']=data_grams_vit_tot.loc[key,'維生素總量']/type_amount.loc[key,'類別總數']

# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
# data=food_data_bar.groupby(by=['食品分類']).食品分類
# seaborn顏色參數
color_names_min=sns.color_palette("hls",18)
color_names_vit=sns.color_palette("husl",18)
# 長條圖
ax_min=plt.bar(data_grams_min_tot.index,data_grams_min_tot['礦物質總量'],width=0.3,align='edge',color=color_names_min)
ax_vit=plt.bar(data_grams_vit_tot.index,data_grams_vit_tot['維生素總量'],width=-0.3,align='edge',color=color_names_vit)
plt.bar_label(ax_min,padding=-8,rotation=45)
plt.bar_label(ax_vit,padding=-12,rotation=45)
# plt.plot(data_grams_min_tot_rate.index,data_grams_min_tot_rate['總量比例'],color='b',marker='o',linewidth=3,markersize=5)
# plt.plot(data_grams_vit_tot_rate.index,data_grams_vit_tot_rate['總量比例'],color='g',marker='o',linewidth=3,markersize=5)
# plt.legend(loc='right',fontsize=12,shadow=True,title='類別',title_fontsize=20,bbox_to_anchor=(1,0,0.3,1))
# 將x,y軸標籤
plt.xticks(rotation=45,fontsize=20)
plt.xlabel('檢測食物之類別',fontsize=20)
plt.ylabel('維生素之平均含量(0.1mg|100ug)',fontsize=20)
ax=plt.twinx()
ax.set_ylabel('礦物質之平均含量(1mg)',fontsize=20)
# 調整y軸刻度
plt.ylim(0,5000)
# 設定標題
plt.title('食品成份資料集之類別之維生素及礦物質',size=40)
# 設定網格
plt.grid(axis="y",zorder=0)
plt.savefig('groupbar(micro).jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()

#18項食品類別之標籤
type_amount=pd.DataFrame(count,index=label,columns=['類別總數'])
#長條圖之資料處理、計算含量平均值作為攝取營養素之參照數值
food_data_bar=food_data.iloc[:,22:55].astype('Float64')
food_data_bar.index=food_data.iloc[:,1]
data_grams=pd.DataFrame(food_data_bar.groupby(by=['食品分類']).mean())
#區分礦物質及維生素
#計算礦物質總量(mg)
data_grams_min=data_grams.iloc[:,0:9]
data_grams_min_tot=pd.DataFrame(np.zeros((18,1)),index=data_grams_min.index,columns=['礦物質總量'])
for index in data_grams_min.index:
    for key in data_grams_min.columns:
        data_grams_min_tot.loc[index,'礦物質總量']=data_grams_min_tot.loc[index,'礦物質總量']+data_grams_min.loc[index,key]
# data_grams_min_tot=data_grams_min_tot/10
#計算礦物質總量比例
data_grams_min_tot_rate=pd.DataFrame(np.zeros((18,1)),index=data_grams_min_tot.index,columns=['總量比例'])
for key in data_grams_min_tot.index:
    data_grams_min_tot_rate.loc[key,'總量比例']=data_grams_min_tot.loc[key,'礦物質總量']/type_amount.loc[key,'類別總數']
#處理維生素資料
#單位換算、全部轉為微克(ug)
data_grams_vit=data_grams.iloc[:,9:]
for index in data_grams_vit.index:
    for key in data_grams_vit.columns:
        if 'IU' in key:
            data_grams_vit.loc[index,key]=data_grams_vit.loc[index,key]*0.025
        elif 'mg' in key:
            data_grams_vit.loc[index,key]=data_grams_vit.loc[index,key]*1000
        else:
            continue
# 1國際單位(IU)=0.025微克(mcg)
#計算維生素總量(ug)
data_grams_vit_tot=pd.DataFrame(np.zeros((18,1)),index=data_grams_vit.index,columns=['維生素總量'])
for index in data_grams_vit.index:
    for key in data_grams_vit.columns:
        data_grams_vit_tot.loc[index,'維生素總量']=data_grams_vit_tot.loc[index,'維生素總量']+data_grams_vit.loc[index,key]
data_grams_vit_tot=data_grams_vit_tot.fillna(0.0)
# data_grams_vit_tot=data_grams_vit_tot/1000
data_grams_vit_tot=data_grams_vit_tot/20
#計算維生素總量比例
data_grams_vit_tot_rate=pd.DataFrame(np.zeros((18,1)),index=data_grams_vit_tot.index,columns=['總量比例'])
for key in data_grams_vit_tot.index:
    data_grams_vit_tot_rate.loc[key,'總量比例']=data_grams_vit_tot.loc[key,'維生素總量']/type_amount.loc[key,'類別總數']

# 繪製圖表
plt.figure(figsize=(30,24),facecolor='thistle')
# x與y軸
# data=food_data_bar.groupby(by=['食品分類']).食品分類
# seaborn顏色參數
color_names_min=sns.color_palette("hls",18)
color_names_vit=sns.color_palette("husl",18)
# 長條圖
ax_min=plt.bar(data_grams_min_tot.index,data_grams_min_tot['礦物質總量'],width=0.3,align='edge',color=color_names_min)
ax_vit=plt.bar(data_grams_vit_tot.index,data_grams_vit_tot['維生素總量'],width=-0.3,align='edge',color=color_names_vit)
plt.bar_label(ax_min,padding=-4,rotation=45)
plt.bar_label(ax_vit,padding=-13,rotation=45)
plt.plot(data_grams_min_tot_rate.index,data_grams_min_tot_rate['總量比例']*10,color='b',marker='o',linewidth=3,markersize=5,label='礦物質比例')
plt.plot(data_grams_vit_tot_rate.index,data_grams_vit_tot_rate['總量比例']*10,color='g',marker='o',linewidth=3,markersize=5,label='維生素比例')
plt.legend(loc='upper center',fontsize=12,shadow=True,title='類別',title_fontsize=20)
# 將x,y軸標籤
plt.xticks(rotation=45,fontsize=20)
plt.xlabel('檢測食物之類別',fontsize=20)
plt.ylabel('維生素之平均含量(0.02mg|20ug)',fontsize=20)
ax=plt.twinx()
ax.set_ylabel('礦物質之平均含量(1mg)',fontsize=20)
# 調整y軸刻度
plt.ylim(0,5000)
# 設定標題
plt.title('食品成份資料集之類別之維生素及礦物質',size=40)
# 設定網格
plt.grid(axis="y",zorder=0)
plt.savefig('grouplinebar(microamount).jpg',transparent=None,dpi='figure',format=None,
        metadata=None,bbox_inches=None,pad_inches=0.1,
        facecolor='auto',edgecolor='auto',backend=None)
plt.show()