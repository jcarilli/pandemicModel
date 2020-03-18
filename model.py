import numpy as np

class virus():
    def __init__(self, p0, k, lifeTime, totalTime, quarRate, deathRate, TTI, p1):
        self.p0 = p0
        self.p3 = 0
        self.p1 = p1
        self.pi = p1
        self.recovered = 0
        self.k = k

        self.lifeTime = lifeTime
        self.TTI =  int((1 - TTI)*lifeTime)

        self.piCnt = [p1]
        self.p1Cnt = [p1]

        self.newlySickCnt = []
        self.p3Cnt = []
        self.totalInfected= [self.p1]

        self.totalTime = totalTime
        self.quarRate = quarRate
        self.quar = 0
        self.quarNegate = 0
        self.quarCnt = []

        self.genP2()
        self.spin()
        self.killed = deathRate*self.totalInfected[-1]


    def genP2(self):
        self.p2 = self.p0 - self.p1 - self.p3


    def genNewlySick(self):

        self.newlySick = self.pi * self.k* (self.p2/self.p0)
        self.newlySickCnt.append(self.newlySick)


    def genRecovered(self, t):
        self.recovered = self.newlySickCnt[t - self.lifeTime]
        self.p3 = self.p3 + self.recovered
        self.quarNegate= self.quarCnt[t - self.lifeTime]

    def run(self, t):

        if t >= int(self.TTI):
            self.quar = self.newlySickCnt[t - self.TTI]*self.quarRate

        self.quarCnt.append(self.quar)

        if t >= self.lifeTime:
            self.genRecovered(t)

        self.p3Cnt.append(self.p3)

        self.genP2()
        self.genNewlySick()

        temp = self.newlySick - self.recovered - self.quar + self.quarNegate
        self.dp1dtCnt.append(temp)

        if t < 3:
            self.pi = self.pi + temp

        else:
            self.AdamBash()
            self.pi = self.pi + self.STEP

        self.p1 += self.newlySick - self.recovered

        self.p1Cnt.append(self.p1)
        self.piCnt.append(self.pi)


        self.totalInfected.append(self.totalInfected[t - 1] + self.p1)


    def AdamBash(self):
        self.STEP = (1/12)*(23*self.dp1dtCnt[-1] - 16*self.dp1dtCnt[-2] + 5*self.dp1dtCnt[-3])

    def spin(self):

        self.dp1dtCnt = []
        for t in range(0, self.totalTime):
            self.run(t)
