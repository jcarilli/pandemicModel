import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import model as F
#import funcs as F

def millions(x, pos):
    return '%1.1fM' % (x*1e-6)

def commonFlu():
    p0 = (372*(10**6))
    k = .35
    months = 12
    totalTime = 30*months
    lifeTime = 3
    quarRate = .01

    TTI = .5

    deathRate = 0.0005
    p1 = 10000

    data = F.virus(p0, k, lifeTime, totalTime, quarRate, deathRate, TTI, p1)

    formatter = FuncFormatter(millions)

    fig, ax = plt.subplots()

    plt.plot(data.p1Cnt, 'k--',linewidth=1 , label = 'People Currently Infected')
    plt.plot(data.totalInfected, 'r-',linewidth=3 ,label= 'Total People Infected')

    maxIndx = np.argwhere(data.p1Cnt == np.max(data.p1Cnt))[0][0]
    plt.plot(maxIndx, data.p1Cnt[maxIndx], 'c o')
    plt.text(maxIndx, data.p1Cnt[maxIndx] + 10**5, 'Max Infected: '+ str(data.p1Cnt[maxIndx]/(10**6))[:6]+'e6')
    #plt.plot(data.deathToll, label= 'Total People Killed')

    print('total infected: ', data.totalInfected[-1]/(10**6), ' million')
    print('total killed: ', data.killed/(10**3), ' thousand')



    #plt.plot(data.p3Cnt, label = 'P3(t)')

    plt.legend()

    plt.ylabel('People (log scale)')
    plt.title('Flu, total infected: '+ r"$\bf{" + str( sum(data.newlySickCnt)/(10**6))[:6]+ ' e6,' +  "}$" + ' total killed: ' + r"$\bf{" + str(data.killed/(10**3))[:6]+ ' e3' +  "}$" )

    plt.yscale('log')
    plt.xlabel('Days')
    plt.show()


def caronaKvTTM():
    p0 = (372*(10**6))

    months = 12
    totalTime = 30*months
    lifeTime = 8
    quarRate = .01

    TTI = 0.625

    deathRate = 0.0005
    p1 = 10

    res = 100

    timeToMax = []
    totalSick = []
    maxInfected= []

    kmin = 0.1
    kmax = 0.4

    ks = []
    for kCnt, k in enumerate(np.linspace(kmin, kmax, res)):
            ks.append(k)
            data = F.virus(p0, k, lifeTime, totalTime, quarRate, deathRate, TTI, p1)

            maxIndx = np.argwhere(data.p1Cnt == np.max(data.p1Cnt))[0][0]
            timeToMax.append(maxIndx)
            totalSick.append(data.totalInfected[-1])
            maxInfected.append(data.p1Cnt[maxIndx])


    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

    ax3.set_title('Days To Max Infected')
    ax3.plot(ks, timeToMax, 'k--', linewidth=1)
    ax3.set_ylabel('Days')
    ax3.set_xlabel('k')

    ax2.set_title('Max Infected at Once')
    ax2.plot(ks, maxInfected, 'm-', linewidth=2)
    ax2.set_ylabel('People')


    ax1.set_title('Total Poeple Infected')
    ax1.plot(ks, totalSick, 'r-', linewidth=2 )
    ax1.set_ylabel('People', )

    plt.show()



def caronaGrid():

    p0 = (372*(10**6))

    months = 12
    totalTime = 30*months
    lifeTime = 8
    quarRate = .01
    k = .3
    TTI = 0.625

    deathRate = 0.0005
    p1 = 10

    res = 30

    timeToMax = []
    totalSick = []
    maxInfected= []

    qRmin = 1/1000
    qRmax = 4/10

    tImin = 1/8
    tImax = 7/8


    maxSick = np.zeros([res, res])
    timeTillMax= np.zeros([res, res])
    totalSick = np.zeros([res, res])

    for qCnt, qr in enumerate(np.linspace(qRmin, qRmax, res)):
        for tCnt, tI in enumerate(np.linspace(tImin, tImax, res)):

            data = F.virus(p0, k, lifeTime, totalTime, qr, deathRate, tI, p1)

            maxIndx = np.argwhere(data.p1Cnt == np.max(data.p1Cnt))[0][0]

            maxSick[qCnt,tCnt]= data.p1Cnt[maxIndx]
            timeTillMax[qCnt,tCnt] = maxIndx
            totalSick[qCnt, tCnt] = data.totalInfected[-1]

    #print(totalSick)
    plt.imshow(maxSick, origin = 'lower', cmap='inferno', extent=[tImin, tImax, qRmin, qRmax])
    plt.ylabel('Mr')
    plt.xlabel('Ft')
    plt.title('Intesity = Max Sick at Once')
    plt.colorbar()
    plt.show()

    plt.imshow(timeTillMax, origin = 'lower', cmap='inferno', extent=[tImin, tImax, qRmin, qRmax])
    plt.ylabel('Mr')
    plt.xlabel('Ft')
    plt.title('Intesity = Time Till Max Sick at Once')
    plt.colorbar()
    plt.show()

    plt.imshow(totalSick, origin = 'lower', cmap='inferno', extent=[tImin, tImax, qRmin, qRmax])
    plt.ylabel('Mr')
    plt.xlabel('Ft')
    plt.title('Intesity = Total Infected')
    plt.colorbar()
    plt.show()

#commonFlu()
#caronaKvTTM()
#caronaGrid()
