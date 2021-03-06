import math
import numpy as np
import IPython.display as ipd
import os

class AudioBuffer:
    def __init__(self, N, sample_rate, delta_time, bits):
        self.bits = bits
        self.delta_time = delta_time # durata (in secondi) di un intervallo
        self.N = N # numero di intervalli da considerare
        self.sample_rate = sample_rate # frequenza di campionamento
        self.n_samples = int(round(delta_time*sample_rate))  # dati campionati in ogni singolo intervallo
        self.phase_acc = 0  # differenza di fase cumulata
        self.audio_buffer = np.zeros((N*self.n_samples), dtype = np.int16)  # Audio buffer
        self.max_sample = 2**(bits - 1) - 1

    def updateAudioBuffer(self, i,f):  # i e' l'intervallo in considerazione, con la frequenza f
        for s in range(self.n_samples):
            tt = float(s)/self.sample_rate    # time in seconds
            #grab the x-coordinate of the sine wave at a given time, while constraining the sample to what our mixer is set to with "bits"
            self.audio_buffer[i*self.n_samples+s] = int(round(self.max_sample*math.sin(self.phase_acc + 2*math.pi*f*tt)))
    
        phase = (f*self.delta_time - np.floor(f*self.delta_time))*2*np.pi
        self.phase_acc += phase


    def makeSoundWithAudioBuffer(self):
        self.makeSoundWithAudioBuffer_ipd()
        
    # serve per il notebook
    def makeSoundWithAudioBuffer_ipd(self):
        sound = ipd.Audio(self.audio_buffer, rate=self.sample_rate, autoplay=True)
        ipd.display(sound)
