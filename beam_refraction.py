import matplotlib.pyplot as plt

def beam_refraction (h=1, F=1, k=1):
    '''
        Функция по преломлению луча линзой
    '''
    
    plt.plot([0],[-2], marker="^",color="b")
    plt.plot([0],[2], marker="v", color="b")
    plt.plot([0,0],[-2,2], color="b")
    plt.plot([-5,5], [0,0], color="k")
    plt.plot([-5,0],[h,h], color="r", marker=">")
    plt.plot([0, h],[F, 0], color="r",marker=".")
    plt.plot([F],[0], marker="o",ms="5",label="focus")
    plt.legend()
    
    plt.show()

beam_refraction()
