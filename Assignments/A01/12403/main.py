if __name__ == "__main__":
    fund = 0    
    K = int(input())
    for i in range (K):
        command = input()
        if command == 'donate':
            m = int(input())
            fund += m
        if command == 'report':
            print(fund)