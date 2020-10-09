def main():
    K = int(input())
    for i in range(K):
      a, b, c = map (int, input().split())
      if(a<b<c):
        e=b
      elif(a<c<b):
        e=c
      elif(b<a<c):
        e=a
      elif(b<c<a):
        e=c
      elif(c<a<b):
        e=a
      elif(c<b<a):
        e=b
      print("Case ", i+1,": ", e, sep='')
if __name__ == "__main__":
    main()
