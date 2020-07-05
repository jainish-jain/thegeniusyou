#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:38:07 2020

@author: jainish
"""

import tkinter as tk
import numpy as np
import pandas as pd
#import sklearn
import pymysql
import datetime
#import timedelta
import operator
import pyfpgrowth
#from mlxtend.preprocessing import TransactionEncoder
#from mlxtend.frequent_patterns import fpgrowth

root = tk.Tk()
root.geometry('340x300+300+250')
frame = tk.Frame(root)
frame.pack()

db = pymysql.connect(host='localhost',user='root',passwd='',database='genius')
cursor = db.cursor()
query=("select *from user_goal_data")
df = pd.read_sql_query(query,db)
df1=df.copy()
nan =float("NaN")
nanstr="NaN"
# df1['s_year']=nan
# df1['s_month']=nan
# df1['s_date']=nan
# df1['e_year']=nan
# df1['e_month']=nan
# df1['e_date']=nan
df1['days']=nan
#df1['imp_days']=nan
x=int(df1.user_id.count())
#i=0
#j=0
# for i in range(x):
#     df1['s_year'][i]=int(str(df1['start_date'][i][0:4]))
#     df1['s_month'][i]=int(str(df1['start_date'][i][5:7]))
#     df1['s_date'][i]=int(str(df1['start_date'][i][8:]))
#     i=i+1
   
    
# for j in range(x):
#     df1['e_year'][j]=int(df1['end_date'][j][0:4])
#     df1['e_month'][j]=int(df1['end_date'][j][5:7])
#     df1['e_date'][j]=int(df1['end_date'][j][8:])
#     j=j+1
    

for k in range(x):
    start_date=datetime.date(int(df1['start_date'][k][0:4]),int(df1['start_date'][k][5:7]),int(df1['start_date'][k][8:]))
    end_date=datetime.date(int(df1['end_date'][k][0:4]),int(df1['end_date'][k][5:7]),int(df1['end_date'][k][8:])) 
    diff=end_date-start_date
    diff+= datetime.timedelta(days=(1))
    df1['days'][k]=diff.days
    #df1['imp_days'][k]=int(df1['imp'][k])*int(df1['days'][k])
    k=k+1
df1['start_date']=pd.to_datetime(df1['start_date'])
df1['end_date']=pd.to_datetime(df1['end_date'])   
dff=df1.copy()
mask=dff['user_id']==usrl
global df_4
df_4= dff.loc[mask]
print(df_4)
#df1.info()
l_cat=list(df1.goal_cat_id.unique())
l_cat.sort()
cat={"carrer & education":1,"family":2,"finnaces":3,"friends & social life":4,"fun & recreation":5,"health & fitness":6,"love & relationships":7,"personal development":8}
'''for i in test_dict : 
    print(i, test_dict[i]) '''
list_cat = Listbox(root)
list_cat.pack()

list_cat.insert(0, "List of categories :")
i=0
for item in cat:
    list_cat.insert(END,item)
    i+=1

def cat():
    root = tk.Tk()
    root.geometry('340x300+300+250')
    frame = tk.Frame(root)
    frame.pack()
    n_cat=list_cat.curselection()
    n_cat=int(n_cat[0])
    catl=l_cat[n_cat-1]
    mask=df1['goal_cat_id']==catl
    global df_2 
    df_2= df1.loc[mask]
    global l_uid
    l_uid=list(df_2.user_id.unique())
    l_uid.sort()

    global list_uid
    list_uid = Listbox(root)
    list_uid.pack()

    list_uid.insert(0, "List of Users")
    i=0
    for item in l_uid:
        list_uid.insert(END, l_uid[i])
        i+=1
    
    cat1 = tk.Button(frame,
                     text="Select the Users",
                     command=cat2)
    cat1.pack(side=tk.LEFT)
    
    
def cat2():
    root = tk.Tk()
    root.geometry('340x300+300+250')
    frame = tk.Frame(root)
    frame.pack()
    n_usr=list_uid.curselection()
    n_usr=int(n_usr[0])
    global usrl
    usrl=l_uid[n_usr-1]
    mask=df_2['user_id']==usrl
    global df_3
    df_3= df_2.loc[mask]
    global l_gid
    l_gid=list(df_3.goal_id.unique())
    l_gid.sort()


    global list_gid
    list_gid= Listbox(root)
    list_gid.pack()

    list_gid.insert(0, "List of Goals")
    i=0
    for item in l_gid:
        list_gid.insert(END, l_gid[i])
        i+=1
    '''
    cat1 = tk.Button(frame,
                     text="Select the Goals",
                     command=cat_2)
    cat1.pack(side=tk.LEFT)
    '''
    
    
    
    
    
def cat3():
    k=0
    i=0
    j=0

    mask=dff['user_id']==usrl
    global df_4
    df_4= dff.loc[mask]
    print(df_4)
    goal_id=list(df_4['goal_id'])
    user_id=list(df_4['user_id'])
    date=list(df_4['start_date'])
#imp=list(df2['imp'])
#imp_days=list(df2['imp_days'])
    days=list(df_4['days'])
    status=list(df_4['status'])
    '''print(goal_id)
    print(user_id[0])
    print(date)
    print(imp)
    print(imp_days)
    print(df3.info())'''

    df_goal_id=[]
    df_user_id=[]
    df_date=[]
#df_imp=[]
#df_imp_days=[]
    df_days=[]
    df_diff_date=[]
    df_status=[]
    for i in range(len(user_id)):
        l = int(days[i])
        for j in range(l):
            df_goal_id.append(goal_id[i])
            df_user_id.append(user_id[i])
            df_date.append(date[i])
        #df_imp.append(imp[i])
        #df_imp_days.append(imp_days[i])
            df_days.append(days[i])
            date1=date[i]
            date1+= datetime.timedelta(days=(j))
            df_diff_date.append(date1)
            df_status.append(status[i])
    #         print(j)
            j=j+1
            k=k+1
        i=i+1
    # print(df_diff_date)
    # list_columns=['df_goal_id','df_user_id','df_date','df_imp','df_imp_days']
    df3 = pd.DataFrame(list(zip(df_goal_id,df_user_id,df_date,df_days,df_diff_date,df_status)) ,columns=['df_goal_id','df_user_id','df_date','df_days','df_diff_date','df_status'])    
    f_df=pd.DataFrame()

    f_df['goals']=df3.groupby('df_diff_date')['df_goal_id'].unique()
    print(f_df)
    transactions = []
    for sublist in f_df.goals.tolist():
        clean_sublist = [item for item in sublist if item is not np.nan]
        transactions.append(clean_sublist)
    patterns = pyfpgrowth.find_frequent_patterns(transactions,2)
    s = dict( sorted(patterns.items(), key=operator.itemgetter(1),reverse=True))
    s1=list(s.keys())
    s2=s1[:10]
    #print(s2)
    rules = pyfpgrowth.generate_association_rules(s,0.33)
    k = dict( sorted(rules.items(), key=operator.itemgetter(1),reverse=True))
    ls=list(k.keys())
    print(ls)
    lgid=list_gid.curselection()
    n_gid=int(lgid[0])
    gid=l_gid[n_gid-1]
    print("s :"+ str(s))
    print("rules : "+str(rules))
    print(gid)
    i=0
    for key, value in k.items(): 
        if gid == ls[i][0]: 
            print(k[gid][0]) 
            #print(value[i][0])
        #elif gif in value[][0]
        i+=1  
    #print(rules.items([gid][0]))
        

def cat_1():
    root = tk.Tk()
    root.geometry('340x300+300+250')
    frame = tk.Frame(root)
    frame.pack()
    n_cat=list_cat.curselection()
    n_cat=int(n_cat[0])
    catl=l_cat[n_cat-1]
    mask=df1['goal_cat_id']==catl
    global df_2 
    df_2= df1.loc[mask]
    global l_goal
    l_goal=list(df_2.goal_id.unique())
    l_goal.sort()
    global list_goal
    list_goal= Listbox(root)
    list_goal.pack()
    list_goal.insert(0, "List of goal id :")
    i=0
    for item in l_goal:
        list_goal.insert(END,l_goal[i])
        i+=1
    goal = tk.Button(frame,
                   text="List of goals most to least used",
                   command=cat_2) 
    goal.pack(side=tk.LEFT)
    

def cat_2():
    root = tk.Tk()
    root.geometry('340x300+300+250')
    frame = tk.Frame(root)
    frame.pack()
    k=0
    i=0
    j=0
    n_goal=list_goal.curselection()
    n_goal=int(n_goal[0])
    goall=l_goal[n_goal-1]
    df_4= df_2
    print(df_4)
    goal_id=list(df_4['goal_id'])
    user_id=list(df_4['user_id'])
    date=list(df_4['start_date'])
#imp=list(df2['imp'])
#imp_days=list(df2['imp_days'])
    days=list(df_4['days'])
    status=list(df_4['status'])
    '''print(goal_id)
    print(user_id[0])
    print(date)
    print(imp)
    print(imp_days)
    print(df3.info())'''

    df_goal_id=[]
    df_user_id=[]
    df_date=[]
#df_imp=[]
#df_imp_days=[]
    df_days=[]
    df_diff_date=[]
    df_status=[]
    for i in range(len(user_id)):
        l = int(days[i])
        for j in range(l):
            df_goal_id.append(goal_id[i])
            df_user_id.append(user_id[i])
            df_date.append(date[i])
        #df_imp.append(imp[i])
        #df_imp_days.append(imp_days[i])
            df_days.append(days[i])
            date1=date[i]
            date1+= datetime.timedelta(days=(j))
            df_diff_date.append(date1)
            df_status.append(status[i])
    #         print(j)
            j=j+1
            k=k+1
        i=i+1
    # print(df_diff_date)
    # list_columns=['df_goal_id','df_user_id','df_date','df_imp','df_imp_days']
    df3 = pd.DataFrame(list(zip(df_goal_id,df_user_id,df_date,df_days,df_diff_date,df_status)) ,columns=['df_goal_id','df_user_id','df_date','df_days','df_diff_date','df_status'])    
    f_df=pd.DataFrame()

    f_df['goals']=df3.groupby('df_diff_date')['df_goal_id'].unique()
    print(f_df)
    transactions = []
    for sublist in f_df.goals.tolist():
        clean_sublist = [item for item in sublist if item is not np.nan]
        transactions.append(clean_sublist)
    patterns = pyfpgrowth.find_frequent_patterns(transactions,2)
    global s
    s = dict( sorted(patterns.items(), key=operator.itemgetter(1),reverse=True))
    print(s)
    s1=list(s.keys())
    global s2
    s2=s1[:20]
    i=0
    global a
    a=[]
    for i in range(len(s2)):
       if len(s2[i])==1:
           a.append(s2[i])
           
           
    print(a)
    global list1_goal
    list1_goal= Listbox(root)
    list1_goal.pack()
    list1_goal.insert(0, "no. of count :")
    i=0
    for item in a:
        list1_goal.insert(END,"goal id :"+ str(a[i][0])+" count:  "+str(s[a[i]]))
        i+=1
    cat1 = tk.Button(frame,
                   text="Search suggestion",
                   command=popupmsg)
    cat1.pack(side=tk.LEFT)
    
    #print(rules.items([gid][0]))
            

def popupmsg():
    rules = pyfpgrowth.generate_association_rules(s,0.33)
    k = dict( sorted(rules.items(), key=operator.itemgetter(1),reverse=True))
    ls=list(k.keys())
    #print(ls)
    lgid=list1_goal.curselection()
    #print(lgid)
    n_gid=int(lgid[0])
    gid=a[n_gid-1]
    print("gid:" + str(gid))
    
    print("s :"+ str(s))
    print("rules : "+str(rules))
    
    sug="goal id :"+str(gid[0])+" suggestion: "+str(k[gid][0])+"probabilty :"+str(k[gid][1])
    '''for i in range(len(rules)):
        print(rules[gid][0][0])
        if rules[i][0][0]==gid:
            print(rules[i][1][1])'''
            
    '''i=0
    for key, value in k.items(): 
        if gid == ls[i][0]: 
            print(k[gid][0]) 
            #print(value[i][0])
        #elif gif in value[][0]
        i+=1  '''
    popup = tk.Tk()
    popup.wm_title("suggestion")
    label = tk.Label(popup, text=sug)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
    
cat1 = tk.Button(frame,
                   text="Search users",
                   command=cat)
cat1.pack(side=tk.LEFT)



cat3 = tk.Button(frame,
                   text="search goals",
                   command=cat_1)
cat3.pack(side=tk.LEFT)
'''
cat4 = tk.Button(frame,
                   text="4",
                   command=cat4)
cat4.pack(side=tk.LEFT)
'''
root.mainloop()