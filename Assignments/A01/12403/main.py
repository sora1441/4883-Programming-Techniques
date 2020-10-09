def main():
    fund = 0    
    K = int(input())
    for i in range (K):
        command = input()
        if command == 'report':
            print(fund)
        else:
          command1,amount = command.split()
          fund += int(amount)
if __name__ == "__main__":
  main()
