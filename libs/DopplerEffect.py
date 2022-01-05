import math
import numpy as np
import matplotlib.pyplot as plt
from libs.AudioBuffer import *
from libs.GraphBuffer import *

class DopplerEffect:
    def __init__(self, A, B, S, timing, bits=16, sample_rate=44100):
        self.A = A
        self.B = B
        self.S = S
        self.timing = timing # timing = tuple((start_time, end_time, N))
        self.N = timing[2]
        self.bits = bits
        self.sample_rate = sample_rate
        self.delta_time = (timing[1]-timing[0])/timing[2]
        # data buffer to sound
        self.buf = AudioBuffer(self.N, self.sample_rate, self.delta_time, self.bits)
        # data to be plotted
        self.graph_data = GraphBuffer(self.N)

    def updatePosAndFreq(self, t, A, B, S, i):
        A_x  = self.A.get_x(t)
        A_y  = self.A.get_y(t)
        A_vx = self.A.get_vx(t)
        A_vy = self.A.get_vy(t)

        B_x  = self.B.get_x(t)
        B_y  = self.B.get_y(t)
        B_vx = self.B.get_vx(t)
        B_vy = self.B.get_vy(t)

        d_0x = B_x - A_x
        d_0y = B_y - A_y
        d_0 = math.sqrt(d_0x**2 + d_0y**2)
    
        delta = (d_0*self.S.c)**2 - (d_0x*A_vy - d_0y*A_vx)**2
        
        Delta_t = ( -d_0x*A_vx - d_0y*A_vy + math.sqrt(delta) )/(self.S.c**2 - self.A.v0**2)

        A_xt = self.A.get_x(t-Delta_t)
        A_yt = self.A.get_y(t-Delta_t)

        d_x = B_x - A_xt;
        d_y = B_y - A_yt;
        d = math.sqrt(d_x**2 + d_y**2);

        v_Ad = (A_vx*d_x + A_vy*d_y)/d;
        v_Bd = (B_vx*d_x + B_vy*d_y)/d;

        f = (  (self.S.c - v_Bd) / (self.S.c-v_Ad)  ) * self.S.f0;

        updated_data = tuple((t, Delta_t, A_xt, A_yt, A_x, A_y, B_x, B_y, f))
        # f is updated_data[8]
        return updated_data


    def dopplerEffectSimulate(self):
        #  for (double t = start_time; t<end_time; t+=delta_time)
        for i in range(0,self.N):
            t = i*self.delta_time
            updated_data  = self.updatePosAndFreq(t, self.A, self.B, self.S, i)
            f = updated_data[8]

            self.graph_data.updateGraphBuffer(updated_data)
            self.buf.updateAudioBuffer(i,f)

    def dopplerEffectResults(self):
        self.graph_data.plotGraphBuffer()
        self.buf.makeSoundWithAudioBuffer()
