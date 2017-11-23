import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1


if __name__ == "__main__":
    a = input()
    b = input()

    # print(type(a),a,type(b),b)
    print(AND( int(a), int(b) ))
