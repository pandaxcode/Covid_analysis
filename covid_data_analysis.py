import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def showData():
  df=pd.read_csv("covid_19.csv")
  print(df)
  input("Press any key to continue....")

def dataNoIndex():
  df=pd.read_csv("covid_19.csv",index_col=0)
  print(df)
  input("Press any key to continue...")

def data_sorted():
  df=pd.read_csv('covid_19.csv')
  print(df.sort_values(by=['Confirmed']))
  
def write_data():
  print("Insert data of particular districts in list form:")
  di=eval(input("Enter Districts:"))
  con_cases=eval(input("Enter no. of confirmed cases:"))
  rec=eval(input("Enter no. of recovered cases:"))
  deaths=eval(input("Enter deaths:"))
  active=eval(input("Enter active cases:"))
  d={'Districts':di,'Confirmed':con_cases,'Recovered':rec,'Deaths':deaths,'Active':active}
  df=pd.DataFrame(d)
  df.to_csv('covid_19.csv', mode='a', index=False, header=False)
  print("Data has been added.")
  input("Press any key to continue...")

def edit_data():
  df=pd.read_csv("covid_19.csv")
  di=input("Enter district to edit:")
  col=input("Enter column name to update:")
  val=input("Enter new value")
  df.loc[df[df['Districts']==di].index.values,col]=val
  df.to_csv("covid_19.csv",index=False)
  print("Record has been updated...")
  input("Press any key to continue...")

def delete_data():
  di=input("Enter district to delete data:")
  df=pd.read_csv("covid_19.csv")
  df=df[df.Districts!=di]
  df.to_csv('covid_19.csv',index=False)
  print("Record deleted...")

  
def line_chart():
  df=pd.read_csv('covid_19.csv')
  District=df["Districts"]
  Confirmed=df["Confirmed"]
  Recovered=df["Recovered"]
  Deaths=df["Deaths"]
  Active=df["Active"]
  plt.xlabel("Districts")
  Y=0
  while Y!=6:
      print("                     ==============================")
      print("                             Line Graph Menu")
      print("                     ==============================")
      print("1.District wise Confirmed Cases ")
      print("2.District wise Recovered Cases ")
      print("3.District wise Death Cases")
      print("4.District wise Active Cases")
      print("5.All data")
      print("6.Return to main menu.")
      Y = int(input("Enter your choice to get line graph: "))
      if Y == 1:
          plt.ylabel("Confirmed Cases")
          plt.figure(figsize=(15,7))
          plt.title("Districts Wise Confirmed Cases")
          plt.plot(District, Confirmed, color='b')
          plt.show()
      elif Y == 2:
          plt.ylabel("Recovered Cases")
          plt.title("Districts Wise Recovered Cases")
          plt.plot(District, Recovered, color='g')
          plt.show()
      elif Y == 3:
          plt.ylabel("Death Cases")
          plt.title("Districts Wise Death Cases")
          plt.plot(District, Deaths, color='r')
          plt.show()
      elif Y == 4:
          plt.ylabel("Active Cases")
          plt.title("Districts Wise Active Cases")
          plt.plot(District, Active, color='c')
          plt.show()
      elif Y == 5:
          
          plt.ylabel("Number of cases")
          plt.plot(District, Confirmed, color='b', label = "Districts Wise Confirmed Cases")
          plt.plot(District, Recovered, color='g', label = "Districts Wise Recovered Cases")
          plt.plot(District, Deaths, color='r', label = "Districts Wise Death Cases")
          plt.plot(District, Active, color='c', label = "Districts Wise Active Cases")
          plt.legend()

          plt.show()
      elif Y==6:
          print("Line Graph Closed.....")
          main_menu()
      else:
          print("Sorry!! Invalid Option! Try Again!!!")
          main_menu()
  
def bar_chart():
  df=pd.read_csv('covid_19.csv')
  District=df["Districts"]
  Confirmed=df["Confirmed"]
  Recovered=df["Recovered"]
  Deaths=df["Deaths"]
  Active=df["Active"]
  plt.figure(figsize=(15, 7))
  plt.xlabel("Districts")
  print("                     ==============================")
  print("                             Bar Graph Menu")
  print("                     ==============================")
  print("1. District Wise Confirmed Cases")
  print("2. District Wise Recovered Cases")
  print("3. District Wise Death Cases")
  print("4. District Wise Active Cases")
  print("5. All data")
  print("6. Combine Bar Graph")
  print("7. Return to main menu.")
  Y=0
  while Y!=5:
      Y = int(input("Enter your choice to get bar graph: "))
      if Y == 1:
          plt.ylabel("Confirmed Cases")
          plt.title("Districts Wise Confirmed Cases")
          plt.bar(District, Confirmed, color='b', width = 0.5)
          plt.show()
      elif Y == 2:
          plt.ylabel("Recovered Cases")
          plt.title("Districts Wise Recovered Cases")
          plt.bar(District, Recovered, color='g', width = 0.5)
          plt.show()
      elif Y == 3:
          plt.ylabel("Death Cases")
          plt.title("Districts Wise Death Cases")
          plt.bar(District, Deaths, color='r', width = 0.5)
          plt.show()
      elif Y == 4:
          plt.ylabel("Active Cases")
          plt.title("Districts Wise Active Cases")
          plt.bar(District, Active, color='c', width = 0.5)
          plt.show()
      elif Y == 5:
          plt.bar(District, Confirmed, color='b', width = 0.5, label = "Districts Wise Confirmed Cases")
          plt.bar(District, Recovered, color='g', width = 0.5, label = "Districts Wise Recovered Cases")
          plt.bar(District, Deaths, color='r', width = 0.5, label = "Districts Wise Death Cases")
          plt.bar(District, Active, color='c',width = 0.5, label = "Districts Wise Active Cases")
          plt.legend()
          plt.show()
      elif Y == 6:
          D=np.arange(len(District))
          width=0.25
          plt.bar(D,Confirmed, width, color='b', label = "Districts Wise Confirmed Cases")
          plt.bar(D+0.25, Recovered, width, color='g', label = "Districts Wise Recovered Cases")
          plt.bar(D+0.50, Deaths, width, color='r', label = "Districts Wise Death Cases")
          plt.bar(D+0.75, Active ,width, color='c', label = "Districts Wise Active Cases")
          plt.legend()
          plt.show()
      elif Y==7:
        print("Bar Graph Closed.....")
        main_menu()
      else:
        print("Sorry!! Invalid Option! Try Again!!!")
        main_menu()

def main_menu():
  ch=0
  print("                     ==============================")
  print("                     |         Main Menu          |")
  print("                     ==============================")
  while ch!=9:
    print("""
          1. Show DataFrame
          2. Data without index
          3. Data in Ascending order of Confirmed cases
          4. Add district data into CSV
          5. Edit a record
          6. Delete a record
          7. Line Graph
          8. Bar Graph
          9. Exit
          """)
    ch=int(input("Enter your choice:"))
    if ch==1:
      showData()
    elif ch==2:
      dataNoIndex()
    elif ch==4:
      write_data()
    elif ch==3:
      data_sorted()
    elif ch==5:
      edit_data()
    elif ch==6:
      delete_data()
    elif ch==7:
      line_chart()
    elif ch==8:
      bar_chart()
    elif ch==9:
      print("Thank you for using our App, Bye Bye, See you again!!")
      break
main_menu()
