import os
import numpy as np
import re

class Exp:
    def __init__(self,path,header=120452):
        self.files=[x for x in os.listdir(path) if 'ecd' in x]
        data=[]
        ilocs=[]
        patrones=[]
        for file in self.files:
            f = open(path+'/'+file, "r")
            a = np.fromfile(f, dtype=np.int8 , offset=header )
            f.close()
            if re.search('F(\d\d\d)C(\d\d\d)',file).group(1) == '999':
                tubo=TuboPatron(file,np.reshape(a,(int(len(a)/16),16)))
                patrones.append(tubo)
            else:
                tubo=Tubo(file,np.reshape(a,(int(len(a)/16),16)))
                data.append(tubo)
                ilocs.append(str(tubo.fila)+','+str(tubo.columna))
        self.patrones=patrones
        self.data=data
        self.ilocs=ilocs   

    def loc(self,fila,columna):
        index=self.ilocs.index(str(fila)+','+str(columna))
        return self.data[index]
    
    def iloc(self,index):
        return self.data[index]

    def patron(self,index):
        return self.patrones[index]
                
class Tubo:
    def __init__(self,file,data):
        self.data = data
        self.fila=int(re.search('F(\d\d\d)C(\d\d\d)',file).group(1))
        self.columna=int(re.search('F(\d\d\d)C(\d\d\d)',file).group(2))
        

    def __repr__(self) -> str:
        return 'TUBO_F'+str(self.fila)+'C'+ str(self.columna)

class TuboPatron(Tubo):
    def __init__(self,file,data):
        self.data = data
        self.id=re.search('F(\d\d\d)C(\d\d\d)I(\d\d\d)',file).group(3)
    def __repr__(self) -> str:
        return 'TUBO_PATRON ' + self.id
