import os
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PATH = 'D:\Magistrale\CV & ML\Progetto Mancini\Progetto CV - AIcereals\dataset/'
#FIELD_NUMBER = 13

def read_list_files(path):
    out = os.listdir(PATH)
    #print(out)
    return out

def filename_split(file):
    field = list()
    file_split = file.split('_',2)
    if '-' in file_split[0] :
        fields = [file_split[0].split('-')[len(file_split[0].split('-'))-1],file_split[1],file_split[2].split('.')[0],str(file)]
    else :
        fields = [file_split[0],file_split[1],file_split[2].split('.')[0],str(file)]
    return fields


def file_array():
    out = read_list_files(PATH)
    fields = list()
    for i in range(0,len(out)):
        fields.append(filename_split(out[i]))
    fields_array = np.array(fields)
    return fields_array

def read_file(path):
    df = pd.read_csv(path,header = 0, sep = ' ')
    ar = np.array(df)
    #print(ar[0,:]) #first row
    #print(ar[0,0]) #first element
    return ar



def index_compute(n,fa,band1,band2):
    temp = fa[fa[:,0] == str(n)]
    print(str(temp[temp[:,1] == str(band1),3][0]))
    a = read_file(PATH + str(temp[temp[:,1] == str(band1),3][0]))
    print(str(temp[temp[:,1] == str(band2),3][0]))
    b = read_file(PATH + str(temp[temp[:,1] == str(band2),3][0]))
    num = np.empty(a.shape)
    num = a - b
    den = np.empty(a.shape)
    den = b + a
    index = np.empty(a.shape)
    index = num / den
    return index
    
def ndvi_view(fa, FIELD_NUMBER):
    ndvi = index_compute(FIELD_NUMBER, fa, 8, 4)
    #plt.plot(ndvi)
    #plt.show()
    index_to_csv(ndvi, 'ndvi', FIELD_NUMBER)
    return ndvi

def ndre_view(fa, FIELD_NUMBER):
    ndre = index_compute(FIELD_NUMBER, fa, 8, 5)
    #plt.plot(ndre)
    #plt.show()
    index_to_csv(ndre, 'ndre', FIELD_NUMBER)
    return ndre

def gndvi_view(fa, FIELD_NUMBER):
    gndvi = index_compute(FIELD_NUMBER, fa, 9, 3)
    #plt.plot(gndvi)
    #plt.show()
    index_to_csv(gndvi, 'gndvi', FIELD_NUMBER)
    print(gndvi.shape)
    return gndvi
    

def show(fa, FIELD_NUMBER):
    figure,axs = plt.subplots(1,3,sharey=True)
    figure.suptitle('Field number: '+ str(FIELD_NUMBER))
    axs[0].plot(ndvi_view(fa, FIELD_NUMBER))
    axs[0].set_title('NDVI')
    axs[1].plot(ndre_view(fa, FIELD_NUMBER))
    axs[1].set_title('NDRE')
    axs[2].plot(gndvi_view(fa, FIELD_NUMBER))
    axs[2].set_title('GNDVI')
    plt.savefig("D:\Magistrale\CV & ML\Progetto Mancini\Progetto CV - AIcereals\output\ " + str(FIELD_NUMBER) + '.png')
    
    

def index_to_csv(index_name, ind, N):
    df = pd.DataFrame(index_name)
    filename = "D:\Magistrale\CV & ML\Progetto Mancini\Progetto CV - AIcereals\output\ " + str(N) + str("_") + str(ind) + ".csv"
    df.to_csv(filename , index = False)
    #np.savetxt("gndvi.csv", index_name, delimiter=",")

def main():
    fa = file_array()
    for i in range (5 , 17):
        show(fa, i)
    #ndvi_view(fa)
    #ndre_view(fa)
    #gndvi_view(fa)
    

main()