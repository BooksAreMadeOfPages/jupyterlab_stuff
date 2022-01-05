import math

class Particle:
    d2r =  math.pi / 180;
    
    def __init__(self, x0=0, y0=0, v0=0,v0_angle=0, a=0, a_angle=0, mru=True):
        self.x0 = x0  # initial (t=0 s) x pos in m
        self.y0 = y0  # initial (t=0 s) y pos in m
        self.v0 = v0   # constant speed in m/s
        self.v0_angle = v0_angle   # speed direction in degree
        self.v0x = self.v0*math.cos(self.v0_angle*self.d2r)
        self.v0y = self.v0*math.sin(self.v0_angle*self.d2r)
        self.mru = mru
        if self.mru == False:
            self.a = a   # constant speed in m/s
            self.a_angle = a_angle   # speed direction in degree
            self.ax = self.a*math.cos(self.a_angle*self.d2r)
            self.ay = self.a*math.sin(self.a_angle*self.d2r)
        else:
            self.a = 0   # constant speed in m/s
            self.a_angle = 0   # speed direction in degree
            self.ax = 0
            self.ay = 0

    # return x-pos at time t
    def get_x(self, t):
        return self.x0 + self.v0x*t + 0.5*self.ax*(t**2)
            
    # return y-pos at time t
    def get_y(self, t):
        return self.y0 + self.v0y*t + 0.5*self.ay*(t**2)

    # return x-vel at time t
    def get_vx(self, t):
        if self.mru == True:
            return self.v0x
        else:
            return self.v0x + self.ax*t
            
    # return y-vel at time t
    def get_vy(self, t):
        if self.mru == True:
            return self.v0y
        else:
            return self.v0y + self.ay*t
