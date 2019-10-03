# Python solution to CS50 ps1 - Mario pyramid 


def main():
  getData()
  
def getData():
  value=int(input('Enter value: '))
  while value not in range(1,9):
    value=int(input('Enter value: '))
  
  pyramid(value)

def pyramid(entry):
  for num in range(1,entry+1):
    print('.'*(entry-num),'#'*num)

main()

