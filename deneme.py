# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:54:55 2021

@author: ramazan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

samples=pd.read_csv('sample_submission.csv')

test=pd.read_csv('test.csv')
#print(test.columns)

train=pd.read_csv('train.csv')

#veri birleştirme


#print(toplam.info()) bilgi verir strin yada int diye 

#print(train.describe().T)

# print(toplam.shape) verikaç satır kaç sütun

# tip=toplam.dtypes veride hangi tipler var
#dolu=toplam.count() verinin doluluğu



#toplam veriyi bulmak için birleştirme yaptım
merged = pd.merge(test, samples,on=None)
toplam=train.append(merged)

string_veri=pd.DataFrame(toplam.GarageCars  .value_counts())
#toplam kaç tane boş veri var
bos=toplam.isnull().sum()










#print(sns.heatmap(toplam.isnull(),yticklabels=False,cbar=False)) #ısı haritası 
#string_veri=pd.DataFrame(toplam.MSZoning.value_counts());


#üzerinde çalışmak için veri1 diye yeni dataframe oluşturdum.
veri1=pd.DataFrame(toplam)

#2000 den daha fazla değeri boşları veriden sildim.

veri1.drop('Alley',axis=1,inplace=True)
veri1.drop('PoolQC',axis=1,inplace=True)
veri1.drop('Fence',axis=1,inplace=True)
veri1.drop('MiscFeature',axis=1,inplace=True)

#sayısal veride min max durumları
sayilar=veri1.describe().T  

bos_satir=veri1[veri1.isnull().any(axis=1)]

#veri1 üzerinde string verilerin içini sayısal verilere dönüştürme fillna ile
#veri1.MSZoning=veri1.MSZoning.str.replace('RL','1')
#veri1.MSZoning=veri1.MSZoning.str.replace('RM','2')
#veri1.MSZoning=veri1.MSZoning.str.replace('FV','3')
#dd=veri1.iloc[:,5].value_counts().index[0]
#veri1.MSZoning=veri1.MSZoning.str.replace('RH','4')
#veri1.MSZoning=veri1.MSZoning.str.replace('C (all)','5',regex=False)
#veri1['MSZoning'] = pd.to_numeric(veri1['MSZoning'])
#ff=veri1.iloc[:,5].value_counts().name
#veriyi değiştirdim Allaha şükürler
#veri1[ff]=veri1[ff].str.replace(dd,'4')

#veri 1 deki string verilerini ayrı bir dataframe e aldım.
#string_veri=pd.DataFrame(veri1.RoofMatl.value_counts())
kolon_sayi=sayilar.index
veri2=pd.DataFrame(veri1)
veri2.drop(kolon_sayi,axis=1,inplace=True)
veri2['RoofMatl']=veri2['RoofMatl'].str.replace('ClyTile','3323',regex=False)
veri2['RoofMatl']=veri2['RoofMatl'].str.replace('Roll','roasaab',regex=False)
veri2['RoofMatl']=veri2['RoofMatl'].str.replace('Metal','mmaal',regex=False)
veri2['RoofMatl']=veri2['RoofMatl'].str.replace('Membran','memran',regex=False)
veri2['Exterior2nd']=veri2['Exterior2nd'].str.replace('BrkFace','233',regex=False)
veri2['Exterior2nd']=veri2['Exterior2nd'].str.replace('BrkFace','233',regex=False)
veri2['Condition2']=veri2['Condition2'].str.replace('PosN','pson',regex=False)
veri2['Condition2']=veri2['Condition2'].str.replace('PosA','psaab',regex=False)

#for için kaç tane kolon döndüreceğime bakıyorum
kolon_sayisi=veri2.columns
#print(kolon_sayisi)
#print(veri1.iloc[:,5].value_counts().index)
b=0

for a in kolon_sayisi:
    
    
    
    #b sayisi hangi kolnda kaldık onu tutuyor
    
    
     #şimdi bir kolonu aldık daha sonra içindeki verileri almak için for yapalım.
    d_veri=veri2.iloc[:,b].value_counts().index
    
    f=0
    
    for c in d_veri:
       
        #içindeki hangi veride olduğumuzu anlamak için f değişkeni
        
        
       # print(veri2.iloc[:,b].value_counts())
        kolon=veri2.iloc[:,b].value_counts().name
        #değiştireceğimizin replace değeri rep değişkeni 
        
        #replace metodu sayıları string istiyor o yüzden 1 den 20 kadar bir dizi yaptım.
        dizi=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','37','38','39','40']
      #  print(dizi[f])
        rep=veri2.iloc[:,b].value_counts().index[f]
        #print(rep)
        
        veri2[kolon]=veri2[kolon].str.replace(rep,dizi[f],regex=False)
        
        
        
        f=f+1
    #burada sayıları stringten integer dönüşüm yaptım    
    
    
    veri2[kolon] = pd.to_numeric(veri2[kolon])
    b=b+1
    
#print(f)


sayi=pd.DataFrame(veri1)
sayi.drop(veri2.columns,axis=1,inplace=True)

veri3=pd.DataFrame(veri2)
veri3=pd.concat([veri3, sayi], axis=1)



#print(veri2.iloc[:,0].value_counts())
#for x in a:
 #   b=0
  #  veri_ici=veri2.iloc[:,b].value_counts()
    
   # for d in veri_ici :
    #   f=veri_ici.count
       
     #  d=veri2.iloc[:,f]
      # print(d)
       #veri2.iloc[:,b]=veri2.iloc[:,b].str.replace(d,'1')
       
   # b=b+1    
   






#kolon_sayisi2=veri2.columns
#b=0
#for a in kolon_sayisi2:
     
 #    d_veri=veri2.iloc[:,b].value_counts().index
  #   c=0
   #  for f in d_veri:
          
    #      kolon2=veri2.iloc[:,b].value_counts().name
     #     veri2[kolon2] = pd.to_numeric(veri2[kolon2])
      #    c=c+1
     #b=b+1



#veri1.iloc[:,2]
#a=veri1.MSZoning.value_counts().index
#veri1.iloc[:,2].iloc[0]=0
#veri1.MSZoning.value_counts().replace('RL',0)
#string_veri=pd.DataFrame(veri1.MSZoning.value_counts());
   # for(x in len(a)):
       #sayac=len(a)
     #   b=0
     #  veri1.iloc[2]
            
       
    
# df['Problems'] = pd.to_numeric(df['Problems'])


#string_veri=pd.DataFrame(veri2.RoofMatl.value_counts())
