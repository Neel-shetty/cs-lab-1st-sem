#i think this is not the right way to do this program, based on the aim and objectives of lab 4
exit = False
while exit == False:
  print("-----------choose an operation-----------")
  print("1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Remainder\n6.division floor\n7.power\n8.exit\n")
  operation = input()

  if operation!="8":
    num_one = float(input("enter the first number - "))
    num_two = float(input("enter the first number - "))
    print("------answer------ ")

  match operation:
    case "1":
      print(num_one+num_two)  
    case "2":
      print(num_one-num_two)
    case "3":
      print(num_one*num_two)
    case "4":
      print(num_one/num_two)
    case "5": 
      print(num_one%num_two)
    case "6": 
      print(num_one//num_two)
    case "7": 
      print(num_one**num_two)
    case "8":
      exit = True
    case _:
      print('wrong operation input')
  
