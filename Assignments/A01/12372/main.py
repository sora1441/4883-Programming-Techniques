if __name__ == "__main__":
    K = int(input())
    for i in range(K):
        l = int(input())
        w = int(input())
        h = int(input())
        if l > 20 or w > 20 or h > 20:
            print("Case ", i+1,": bad")
        else:
            print("Case ", i+1,": good")