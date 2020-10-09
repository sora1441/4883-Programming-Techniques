def main():
    K=1
    while K>0:
        K = int(input())
        if (K == 0):
            break
        N,  M = map(int,input().split())
        for i in range (K):
            X, Y = map(int,input().split())
            if (M<Y):       #north
                if (N<X):   #northeast
                    print('NE')
                elif (N>X): #northwest
                    print('NO')
                elif (N==X):       #equal
                    print('divisa')
            elif (M>Y):     #south
                if (N<X):   #southeast
                    print('SE')
                elif (N>X): #southwest
                    print('SO')
                elif (N==X):       #equal
                    print('divisa')
            else:           #equal
                print('divisa')
if __name__ == "__main__":
    main()
