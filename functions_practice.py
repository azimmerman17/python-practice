def hello(name):
  print(f'Hello {name}')

def pack(item_1, item_2, item_3):
  return [item_1, item_2, item_3]


def eat_lunch(lunch):
  for x in lunch:

    if x == lunch[0]:
      print(f'First I eat {x}' )
    else:
      print(f'Next I eat {x}')
  print('My lunchbox is empty!')
  

hello('Andrew')
lunch = pack('sandwich', 'apple', 'water')
print(lunch)
eat_lunch(lunch)