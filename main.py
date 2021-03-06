import wfdb
import matplotlib.pyplot as plt
import numpy as np

import ReadSignals


def PAT_Features(PathSignal):
    N = 0
    signals, fields = wfdb.rdsamp(PathSignal)
    #print(np.shape(signals))	                    # Tamanho do sinal
    #print(fields)
    fs = fields['fs']
    sig_len = fields['sig_len']
    seconds = sig_len/fs
    t = np.arange(0., seconds, seconds/sig_len)
    names = fields['sig_name']                      # Pega o nome das variáveis
    #print(names)
    
    #Procura por um nome especifico
    for i, name in enumerate(names):
        if name == 'PLETH':
            N = i
    #Salva os dados
    signal = signals[:,N]
    fs = fields['fs']
    
 
   
    plt.title(names[N])                             # Define o nome do titulo
    plt.xlabel('segundos')
    plt.ylabel('mv')
    plt.plot(t, signal)
    plt.show()

    
    
def main():
    PAT_Features('3000063_0010')
    #ECG, PPG, ABP, FS = ReadSignals.Read('3000063_0010')
    #print(ECG)
    #print(PPG)
    #print(ABP)
    #print(FS)
	#signals, fields = wfdb.rdsamp('3000063_0010')
	#wfdb.plot_all_records(directory='matlab')
	

if __name__ == "__main__":
    main()