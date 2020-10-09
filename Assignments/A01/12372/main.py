def main():
    K = int(input())
    for i in range(K):
        l, w, h = map(int,input().split())
        if l > 20 or w > 20 or h > 20:
            print("Case ", i+1,": bad",sep='')
        else:
            print("Case ", i+1,": good",sep='')
if __name__ == "__main__":
  main()
