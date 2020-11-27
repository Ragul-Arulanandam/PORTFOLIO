import pickle
import numpy as np
def estimatePrice(a,b,c,d):
    with open ('./Resources/chennai_house_price.pickle','rb') as f:
        model = pickle.load(f)
    #arr = np.array([a,b,c,d])
    #newarr = arr.reshape(1,-1)
    return int(model.predict([[a,b,c,d]]))

#print(estimatePrice(1,1800,3,2))
print(estimatePrice(2,1230,3,3))
