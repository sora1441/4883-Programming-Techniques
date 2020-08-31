def main():
  l=int(input())
  for i in range(l):
    a=int(input())
    b=int(input())
    if (a<b):
      print('<')
    elif (a>b):
      print('>')
    else:
      print('=')
if __name__ == "__main__":
    main()