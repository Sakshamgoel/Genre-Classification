import json, os

def main():
  with open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\genre-count.json') as f:
    data = json.load(f)


  #new_data = {k: v for k, v in sorted(data.items(), key = lambda item: item[1], reverse = True)}

  x = 0
  for key, value in data.items():
    print(key, ': ', value)
    x += 1

    if x > 20:
      break



main()