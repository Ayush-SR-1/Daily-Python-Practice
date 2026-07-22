import requests
import string
    

url = "https://api.api-ninjas.com/v1/sudokugenerate?difficulty=medium&width=3&height=3"

headers = {
    "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2" 
}

a = requests.get(url, headers=headers)
data = a.json()

def display(grid):
  num = [1,2,3,"|",4,5,6,"|",7,8,9]
  print("  ", end= " ")
  for i in num:
    print(i, end=" ")
  print("\n")

  letters = string.ascii_uppercase 

  for row_index, row in enumerate(grid):
    
      line = letters[row_index] + "  " 
      for col_index, val in enumerate(row):
        
          line += "_" if val is None else str(val)
          if col_index in (2, 5):
              line += " | "
          elif col_index != 8:
              line += " "
          
      print(line)
      if row_index in (2, 5):
        print(f"{'':3}{'-' * 21}")

def play():
  
  display(data["puzzle"])
  while True:
    try:
      b = input("Enter the place u want to fill (example: A3) or quit: ").upper()
      
      if b == "QUIT":
        display(data["solution"])
        break
      
      row = ord(b[0]) - ord('A')
      col = int(b[1:]) - 1
      
      if not (0 <= row <= 8) or not (0 <= col <= 8):
        print("That's outside the board — try again (e.g. A3).")
        continue
      
      if data["puzzle"][row][col] is None:
        d = int(input("Enter the number u want to fill: "))
        
        if d == data["solution"][row][col]:
          data["puzzle"][row][col] = d
          display(data["puzzle"])
          print(f"Placed {d} as {b}")
          
        else:
          print(f"\nWrong number - {d} doesn't belong to {b}. Try again.")
          
        if data["puzzle"] == data["solution"]:
          print("You have Won the game !!!")
          break

      
      else:
        print(f"{b} is already filled with {data['puzzle'][row][col]}.")
        
    except (IndexError, ValueError):
        print("That wasn't a valid cell — try something like A3.")
    
    

if __name__ == "__main__":
  play()