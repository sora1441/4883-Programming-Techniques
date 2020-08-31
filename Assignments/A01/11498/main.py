if __name__ == "__main__":
    K=1
    while K!=0:
        K = int(input())
        N = int(input())
        M = int(input())
        for i in range (K):
            X = int(input())
            Y = int(input())
            if (N<X):       #north
                if (M<Y):   #northeast
                    print('NE')
                elif (M>Y): #northwest
                    print('NO')
                else:       #equal
                    print('divisa')
            elif (N>X):     #south
                if (M<Y):   #southeast
                    print('SE')
                elif (M>Y): #southwest
                    print('SO')
                else:       #equal
                    print('divisa')
            else:           #equal
                print('divisa')