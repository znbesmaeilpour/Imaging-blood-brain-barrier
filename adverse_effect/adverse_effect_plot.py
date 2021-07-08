import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


#load behavioral data
pre_data=pd.read_excel(r'F:\BBB project\Analysis\adverse effect\pre_BBB_experiment_reporting.xlsx')
post_data=pd.read_excel(r'F:\BBB project\Analysis\adverse effect\post_BBB_experiment_reporting.xlsx')


# find the rows related to different conditions
def find_condition(filename,condition):
    inx=np.where(filename.condition==condition)
    inx=inx[0]
    return inx

inx_sham=find_condition(pre_data,'sham')
inx_active=find_condition(pre_data,'active')
inx_active2=find_condition(pre_data,'active2')


def plot_scatter(pre_data,post_data):
    x1=np.random.rand(inx_sham.shape[0])
    x2=np.random.rand(inx_active.shape[0])
    x3=np.random.rand(inx_active2.shape[0])
    k=0
    plt.scatter(x1+k,pre_data.iloc[inx_sham],c='g',label='sham')
    plt.scatter(x2+1+k,pre_data.iloc[inx_active],c='b',label='2 mA')
    plt.scatter(x3+k+2,pre_data.iloc[inx_active2],c='r',label='4 mA')
    k+=6
    plt.scatter(x1+k,post_data.iloc[inx_sham],c='g',label='sham')
    plt.scatter(x2+1+k,post_data.iloc[inx_active],c='b',label='2 mA')
    plt.scatter(x3+k+2,post_data.iloc[inx_active2],c='r',label='4 mA')
        
    plt.legend(['sham','2 mA', '4 mA'])
    plt.xlabel('pre-stimulation             post-stimulation')
    plt.show()

#Headache
plt.title('Headache')
plt.ylabel('Discomfort level')
plot_scatter(pre_data.Headache,post_data.Headache)


#Burning sensation
plt.title('Skin Burning sensation')
plt.ylabel('Discomfort level')
plot_scatter(pre_data.Burning,post_data.Headache)


#Tingling sensation
plt.title('Skin Tingling sensation')
plt.ylabel('Discomfort level')
plot_scatter(pre_data.Tingling,post_data.Headache)











