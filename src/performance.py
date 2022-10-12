import grequests
import matplotlib.pyplot as plt

from custom_time import timeit

urls = {
    'movie':'http://localhost:8000'
}

@timeit(verbose=True)
def getX(url,nb):
    rs = (grequests.get(url) for _ in range(nb))
    grequests.map(rs)


def compareTimes(url):
    N = [x**3 for x in range(10)]
    execution_times = [getX(url,n) for n in N]
    return N,execution_times

def plotAndShow(X,Y):
    plt.plot(X,Y)
    plt.ylabel('ellapsed time')
    plt.show()

def main():
    N,T = compareTimes(urls['movie'])
    plotAndShow(N,T)



if __name__ == '__main__':
    main()