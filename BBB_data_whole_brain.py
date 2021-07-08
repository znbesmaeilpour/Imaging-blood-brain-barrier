import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#load dataset for CBF, ATT and KW
data_whole_brain_CBF=pd.read_excel(r'F:\BBB project\Analysis\data_whole_brain.xlsx',sheet_name='CBF')
data_whole_brain_ATT=pd.read_excel(r'F:\BBB project\Analysis\data_whole_brain.xlsx',sheet_name='ATT')
data_whole_brain_KW=pd.read_excel(r'F:\BBB project\Analysis\data_whole_brain.xlsx',sheet_name='kw')
data_whole_brain_KW.tail()


#Find data related to each stimulation condition (sham,2 mA and 4 mA)
def find_condition(dataname,condition):
    inx=np.where(dataname.condition==condition)
    inx=inx[0]
    return inx

inx_sham=find_condition(data_whole_brain_KW,'sham')    
inx_active=find_condition(data_whole_brain_KW,'active')
inx_active2=find_condition(data_whole_brain_KW,'active2')
print(inx_active2)

# violing plot for data
def plot_data(dataname,inx_sham,inx_active,inx_active2):
    t_1=dataname.t_1
    t_2=dataname.t_2
    t_3=dataname.t_3
    t_4=dataname.t_4
    t_5=dataname.t_5
    
    plt.violinplot([t_1[inx_sham],t_1[inx_active],t_1[inx_active2],
                    t_2[inx_sham],t_2[inx_active],t_2[inx_active2],
                    t_3[inx_sham],t_3[inx_active],t_3[inx_active2],
                    t_4[inx_sham],t_4[inx_active],t_4[inx_active2],
                    t_5[inx_sham],t_5[inx_active],t_5[inx_active2]]
                    ,data=data_whole_brain_KW,showmedians=True)


    plt.xticks(np.arange(0,15,1),['t1-sham','t1-active','t1-active2',
                                  't2-sham','t2-active','t2-active2',
                                  't3-sham','t3-active','t3-active2',
                                  't4-sham','t4-active','t4-active2',
                                  't5-sham','t5-active','t5-active2'])
    plt.show()
    


#plt.title('whole brain KW')
#plot_data(data_whole_brain_KW,inx_sham,inx_active,inx_active2)


#color coded scatter plot for sham, 2 mA and 4 mA stimulation
    
def scatter_data(filename):
    x1=np.random.rand(inx_sham.shape[0])
    x2=np.random.rand(inx_active.shape[0])
    x3=np.random.rand(inx_active2.shape[0])
    k=0
    for i in range(5):
        plt.scatter(x1+k,filename.iloc[inx_sham,i+1],c='g',label='sham')
        plt.scatter(x2+1+k,filename.iloc[inx_active,i+1],c='b',label='2 mA')
        plt.scatter(x3+k+2,filename.iloc[inx_active2,i+1],c='r',label='4 mA')
        k+=6
    plt.legend(['sham','2 mA', '4 mA'])
    plt.show()

plt.title('Water exchange rate(whole brain)for 5 time points')
scatter_data(data_whole_brain_KW)
plt.show()
plt.title('Cerebral blood flow(whole brain)for 5 time points')
scatter_data(data_whole_brain_CBF)

plt.title('Arterial transit time(whole brain)for 5 time points')
scatter_data(data_whole_brain_ATT)

    
    


