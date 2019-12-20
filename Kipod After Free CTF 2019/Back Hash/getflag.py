import hashlib


i=0

while True:
  r= hashlib.md5(f'{i}'.encode())
  if 'f1a9' in r.hexdigest():
    print(i)
    break

  i+=1
