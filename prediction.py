from validator import Validador
import pickle
import pandas as pd

# BBPD
# Cluster
cluster_model_bbpd = pickle.load(open('models/cluster_model_bbpd.pkl','rb'))
#Regresion
model_rbbpd_low = pickle.load(open('models/model_rbbpd_low.pkl','rb'))
export_model_rbbpd_mid = pickle.load(open('models/model_rbbpd_mid.pkl','rb'))
model_rbbpd_high = pickle.load(open('models/model_rbbpd_high.pkl','rb'))

#AYS
# Cluster
cluster_model_asyc = pickle.load(open('models/cluster_model_asyc.pkl','rb'))
#Regresion
export_model_rays_low = pickle.load(open('models/model_rays_low.pkl','rb'))
export_model_rays_mid = pickle.load(open('models/model_rays_mid.pkl','rb'))
export_model_rays_high = pickle.load(open('models/model_rays_high.pkl','rb'))

def predict_well_conditions(data:Validador):

    predict = pd.DataFrame(columns=['XCOORD','YCOORD','Prof','Dpiston'])
    predict2 = pd.DataFrame(columns=['XCOORD','YCOORD','Prof'])

    data = data.dict()

    Prof = data['Prof']
    XCOORD = data['XCOORD']
    YCOORD = data['YCOORD']
    Dpiston  = data['Dpiston']

    predict = predict.append({'XCOORD':XCOORD,'YCOORD':YCOORD,'Dpiston':Dpiston,'Prof':Prof},ignore_index=True)
    predict2 = predict2.append({'XCOORD':XCOORD,'YCOORD':YCOORD,'Prof':Prof},ignore_index=True)

    bbpd_group = cluster_model_bbpd.predict(predict)
    bbpd_value = 0; 

    ays_group = cluster_model_asyc.predict(predict)
    ays_value = 0; 




    if (bbpd_group[0]<1):        
        bbpd_value = model_rbbpd_low.predict(predict2)
    elif (bbpd_group[0]<2):        
        bbpd_value = export_model_rbbpd_mid.predict(predict2)
    else:        
        bbpd_value = model_rbbpd_high.predict(predict2)

    
    if (ays_group[0]<1):        
        ays_value = export_model_rays_low.predict(predict2)
    elif (ays_group[0]<2):        
        ays_value = export_model_rays_mid.predict(predict2)
    else:        
        ays_value = export_model_rays_high.predict(predict2)

    if (bbpd_value[0]<100):
        bbpd_group= 'low'
    elif (bbpd_value[0]<200):
        bbpd_group= 'mid'
    else:
        bbpd_group= 'high'

    if (ays_value[0]<20):
        ays_group= 'low'
    elif (ays_value[0]<40):
        ays_group= 'mid'
    else:
        ays_group= 'high'





    return {'bbpd_group':str(bbpd_group),'bbpd_value':str(bbpd_value[0]),'ays_group':str(ays_group),'ays_value':str(ays_value[0])}