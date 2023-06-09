import pandas as pd

filelist = []
labellist = []
N = 50 #全データ数(地形生成データ)
n = int(N*0.9) #9割分のデータを学習用として利用

##################学習用データセット#############################

for i in range(n):
    filename = r"C:\Users\marot\Documents\MATLAB\script\DEM\64pix_(0-3deg)_dem(noisy)\image(t-10)/image_"+str(i)
    filelist.append(filename)

    labelname = r"C:\Users\marot\Documents\MATLAB\script\DEM\64pix_(0-3deg)_dem(noisy)\label/label_"+str(i)
    labellist.append(labelname)

df_learn = pd.DataFrame(
    {
        "id":filelist,
        "label":labellist
    }
)



######################評価用データセット####################################
filelist_eval = []
labellist_eval = []
for i in range(n, N):
    filename = r"C:\Users\marot\Documents\MATLAB\script\DEM\64pix_(0-3deg)_dem(noisy)\image(t-10)/image_"+str(i)
    filelist_eval.append(filename)

    labelname = r"C:\Users\marot\Documents\MATLAB\script\DEM\64pix_(0-3deg)_dem(noisy)\label/label_"+str(i)
    labellist_eval.append(labelname)
# print(filelist)
df_eval = pd.DataFrame(
    {
        "id":filelist_eval,
        "label":labellist_eval
    }
)
#########################################################################


df_learn.to_csv('snn_semanticseg/data/csv_data/semantic_train_loc.csv')
df_eval.to_csv('snn_semanticseg/data/csv_data/semantic_eval_loc.csv')

#dataname = 'snn_semanticseg/data/csv_data/semantic_img_loc.csv'
#df = pd.read_csv(dataname)
#print(df.head())

