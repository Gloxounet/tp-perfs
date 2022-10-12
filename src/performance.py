import grequests
import matplotlib.pyplot as plt

from custom_time import timeit

urls = {
    '4services':'http://localhost:8000',
    '9services':'http://localhost:8001'
}

@timeit(verbose=False)
def getX(url,nb):
    rs = (grequests.get(url) for _ in range(nb))
    grequests.map(rs)


def compareTimes(url):
    N = [x**3 for x in range(5,12)]
    execution_times = [getX(url,n) for n in N]
    return N,execution_times
  
def main():
    print("Getting times for 4 services being loadbalanced")
    N,T = compareTimes(urls['4services'])
    print("Done.")

    print("Getting times for 9 services being loadbalanced")
    N2,T2 = compareTimes(urls['9services'])
    print("Done.")
    
    # Plotting things
    plt.plot(N,T,label="4")
    plt.plot(N2,T2,label="9")

    plt.ylabel('ellapsed time')
    plt.yscale('linear')
    plt.legend(loc='upper left')

    plt.show()



if __name__ == '__main__':
    main()