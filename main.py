def sum_list(list1):
  total = 0
  for a in list1:
    total += a 
  return total 

def sum(num1,num2):
  return num1 + num2

def one():
  print("1")

if __name__ == "__main__":
  print("My first python")
  one()
  print(sum(5,6))
  total = sum(1,2)
  print(total) 
  list1 = [1,2,3,4,5]
  print(sum_list(list1))
    
