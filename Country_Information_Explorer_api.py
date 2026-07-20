import requests

search_history = []
favorite_countries = []

while True:
  
  print("======== Country Information Explorer ======== \n\n1. Search for a country\n2. Compare two countries\n3. View favorite countries. \n4. Search History\n5. Remove History. \n6. Exit\n")
  choice = int(input("Enter your choice (1-6): "))

  if choice == 1:
    
      country = input("Enter the name of the country to get the information: ")
      url = f"https://api.api-ninjas.com/v1/country?name={country}" 
      header = {
        "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
      }
      a = requests.get(url, headers=header)
      data = a.json()
      
      print(f"---------- Country: {country.upper()} Information ----------")
      print("Fundamental Infomation:\n")
      print("Name:", data[0]["name"] )
      print("Capital City:", data[0]["capital"])
      print("Region:", data[0]["region"])
      print("Currency Code:", data[0]["currency"]["code"])
      print("Currency Name:", data[0]["currency"]["name"])
      print("\n")
      
      print("Economic Infomation:\n")
      print("GDP:", data[0]["gdp"])
      print("GDP growth rate:", data[0]["gdp_growth"])
      print("GDP per capita:", data[0]["gdp_per_capita"])
      print("Unemployment:", data[0]["unemployment"])
      print("\n")
      
      print("Population Statistics:\n")
      print("Population:", data[0]["population"])
      print("Population Density:", data[0]["pop_density"])
      print("Area:", data[0]["surface_area"])
      print("Sex Ratio:", data[0]["sex_ratio"])
      print("Life Expectancy Male:", data[0]["life_expectancy_male"])
      print("Life Expectancy Female:" , data[0]["life_expectancy_female"])

      search_history.append(f"Information of {country}")

  elif choice == 2:
      country1 = input("Enter the name of the first country to compare: ")
      country2 = input("Enter the name of the second country to compare: ")
      print("\n")
      
      url1 = f"https://api.api-ninjas.com/v1/country?name={country1}" 
      url2 = f"https://api.api-ninjas.com/v1/country?name={country2}" 
      header = {
        "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
      }
      
      a1 = requests.get(url1, headers=header)
      data1 = a1.json()
      
      a2 = requests.get(url2, headers=header)
      data2 = a2.json()
      
      print(f"---------- Country Comparison: {country1.upper()} vs {country2.upper()} ----------\n")
      
      print(f"{country1.upper()} Information:", "vs", f"{country2.upper()} Information:\n")
      
      print(f"{'Name:':<22}{str(data1[0]['name']):<15} | {str(data2[0]['name']):<15}")
      print(f"{'Capital City:':<22}{str(data1[0]['capital']):<15} | {str(data2[0]['capital']):<15}")
      print(f"{'Region:':<22}{str(data1[0]['region']):<15} | {str(data2[0]['region']):<15}")
      print(f"{'Currency Code:':<22}{str(data1[0]['currency']['code']):<15} | {str(data2[0]['currency']['code']):<15}")
      print(f"{'Currency Name:':<22}{str(data1[0]['currency']['name']):<15} | {str(data2[0]['currency']['name']):<15}\n")
      
      print(f"{'GDP:':<22}{str(data1[0]['gdp']):<15} | {str(data2[0]['gdp']):<15}")
      print(f"{'GDP growth rate:':<22}{str(data1[0]['gdp_growth']):<15} | {str(data2[0]['gdp_growth']):<15}")
      print(f"{'GDP per capita:':<22}{str(data1[0]['gdp_per_capita']):<15} | {str(data2[0]['gdp_per_capita']):<15}")
      print(f"{'Unemployment:':<22}{str(data1[0]['unemployment']):<15} | {str(data2[0]['unemployment']):<15}\n")

      print(f"{'Population:':<22}{str(data1[0]['population']):<15} | {str(data2[0]['population']):<15}")
      print(f"{'Population Density:':<22}{str(data1[0]['pop_density']):<15} | {str(data2[0]['pop_density']):<15}")
      print(f"{'Area:':<22}{str(data1[0]['surface_area']):<15} | {str(data2[0]['surface_area']):<15}")
      print(f"{'Sex Ratio:':<22}{str(data1[0]['sex_ratio']):<15} | {str(data2[0]['sex_ratio']):<15}")
      print(f"{'Life Expectancy Male:':<22}{str(data1[0]['life_expectancy_male']):<15} | {str(data2[0]['life_expectancy_male']):<15}")
      print(f"{'Life Expectancy Female:':<22}{str(data1[0]['life_expectancy_female']):<15} | {str(data2[0]['life_expectancy_female']):<15}")
      
      search_history.append(f"Comparison between: {country1} vs {country2}")


  elif choice == 3:
    
    while True:
    
      print("--------- Favorite Countries ----------\n")
      print("Choices:\n1. View the Favorite Countries\n2. Add Favorite Countries\n3. Back to Main Menu\n")
      choice = int(input("Enter your choice (1-3): "))
      print("\n")
    
      if choice == 1:
        
        if not favorite_countries:
          print("\nNo favorite countries found.\n")
        else:
          print("\n--------- Favorite Countries ----------\n")
          for i, country in enumerate(favorite_countries, start = 1):
            print(f"{i}. {country}")
      
      if choice == 2:
        
        while True:
          
          fav = input("Enter the name of the country to add to favorites: ")
          if fav.lower() == "done":
            break
          else:
            favorite_countries.append(fav)
          
      if choice == 3:
          break
    
  elif choice == 4:
    
    if not search_history:
        print("No search history found.")
    else:
        print("\n---------- Search History ---------- \n")
        for i, element in enumerate(search_history, start=1):
            print(f"{i}. {element}")
    print("\n")
  
  elif choice == 5:
    search_history.clear()
    print("\nSearch history cleared successfully.\n")
  
  elif choice == 6:
    print("\nExiting the program. Goodbye!\n")
    break
  
  else:
    print("Invalid choice. Please enter a number between 1 and 6.")
