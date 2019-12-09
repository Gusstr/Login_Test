import mysql.connector, random, userdatabase

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="",
  database="login",
)


print("vad vill du göra? (ny användare /ny, loga in /login, visa konton /visa)")
do = input()

if do == "/visa":
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM users2")
  for x in mycursor:
    print(x)

elif do == "/ny":
  x = 0
  nyanv = input("nytt namn: ")
  nylos = input("nytt lösen: ")

  userdatabase.new_user(nyanv, nylos)

elif do == "/login":
  print("skriv in användarnamn")
  anvnamn = input()
  mycursor = mydb.cursor()

  sql = "SELECT passwd FROM users2 WHERE name = %s"
  name = (anvnamn, )
  mycursor.execute(sql, name)


  myresult = mycursor.fetchall()
  
  clean_result = ""
  for x in myresult:
    clean_result = clean_result + x[0]
  
  
  print("skriv in lösenord")
  inputlos = input()
  if inputlos != "":
    if clean_result == inputlos:
      print("inloggad")
      
      kop = False
      while kop == False:

        (coins2, money2, coins, money) = userdatabase.ekonomi(anvnamn)

        print("du har " + coins + " coins")
        print("du har " + money + " pengar")

        print("omvandla coins till pengar för ett värde på 1c = 5sek, Köp 1c = 6sek. För att omvandla skriv /sälj eller /köp")
        omv = input()
        if omv == "/köp":
          print("hur många vill du köpa?")
          K1 = int(input())
          userdatabase.buy_coins(money2, coins2, anvnamn, K1)
        elif omv == "/sälj":
          print("hur många vill du sälja?")
          S1 = int(input())
          userdatabase.sell_coins(coins2, money2, anvnamn, S1)
        
        print("vad vill du göra? (för att lämn /ut, för att betta /bet)")
        ans = input()
        if ans == "/ut" or ans == "/bet":
          kop = True
          if ans == "/bet":
            bet = False
            while bet == False:
              coins = userdatabase.Take_Coins(anvnamn)
              coins2 = int(coins)
              print("bet med coins, 1:2, 1:3, 1:5, Du har " + coins + " coins")
              odds = int(input())
              if odds == 2 or odds == 3 or odds ==5:
                if odds == 2:
                  B1 = int(input("Antal coins: "))
                  r1 = random.randint(1, 2)
                  if r1 == 1:
                    New_coins = B1 * 2
                    print("win")
                  else:
                    New_coins = 0
                    print("loose")
                elif odds == 3:
                  B1 = int(input("Antal coins: "))
                  r1 = random.randint(1, 3)
                  if r1 == 1:
                    New_coins = B1 * 3 
                    print("win")
                  else:
                    New_coins = 0
                    print("loose")
                elif odds == 5: 
                  B1 = int(input("Antal coins: "))
                  r1 = random.randint(1, 5)
                  if r1 == 1:
                    New_coins = B1 * 5 
                    print("win")
                  else:
                    New_coins = 0
                    print("loose")  
                userdatabase.bet(New_coins, coins2, anvnamn, B1)
              else:
                print("odds existerar inte")
       

  else:
    print("fel användarnamn eller lösenord")

  
  

