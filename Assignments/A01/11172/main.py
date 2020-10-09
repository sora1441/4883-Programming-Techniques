def main():
  loop = int(input())
  for i in range(loop):
      a, b = map(int,input().split())
      if (a<b):
        print('<')
      elif (a>b):
        print('>')
      else:
        print('=')
if __name__ == "__main__":
    main()
