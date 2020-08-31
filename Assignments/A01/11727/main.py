if __name__ == "__main__":
    K = int(input())
    for i in range(K):
       a = int(input())
       b = int(input()) 
       c = int(input())
       d = max(a,b,c)
       print("Case ", i+1,": ", d)