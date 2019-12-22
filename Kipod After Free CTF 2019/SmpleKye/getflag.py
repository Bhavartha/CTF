import hashlib
from itertools import product


alphabets ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321'
keywords = [''.join(i) for i in product(alphabets, repeat = 4)]
_=17
for i in keywords:
  r= hashlib.sha256(f'{_}{i}'.encode())
  # print(f'{_}{i}')
  if f'{_}{i}' in r.hexdigest():
    print(f'{_}{i}')
    print(r.hexdigest())
    break


#Submit op to webpage it gives the key
