import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="",
  database="login",
)

def new_user(A, B):
    mycursor2 = mydb.cursor()
    sql = "INSERT INTO users2 (name, passwd, coins, money) VALUES (%s, %s, %s, %s)"
    val = (A, B, 10, 0)
    mycursor2.execute(sql, val)
    mydb.commit()


def ekonomi(C):
    mycursor = mydb.cursor()
    sql = "SELECT coins, money FROM users2 WHERE name = %s"
    name = (C, )
    mycursor.execute(sql, name)
    myresult = mycursor.fetchall()
    clean_result2 = ""
    for x in myresult:
      coins = clean_result2 + x[0]
      money = clean_result2 + x[1]
      coins2 = int(coins)
      money2 = int(money)
    return (coins2, money2, coins, money)


def buy_coins(money2, coins2, anvnamn, K1):
  if money2 >= 6:
    if K1 * 6 < money2:
      inpcoins = K1 + coins2
      inpmoney = money2 - K1 * 6
      mycursor = mydb.cursor()
      sql = "UPDATE users2 SET coins = %s, money = %s WHERE name = %s"
      val = (inpcoins, inpmoney, anvnamn)
      mycursor.execute(sql, val)
      mydb.commit()
    else:
      print("du har inte råd")
  else:
    print("du har inte råd")

def sell_coins(coins2, money2, anvnamn, S1):
  if coins2 > 0:

    if S1 < coins2:
      inpcoins = coins2 - S1
      inpmoney = S1 * 5 + money2
      mycursor = mydb.cursor()
      sql = "UPDATE users2 SET coins = %s, money = %s WHERE name = %s"
      val = (inpcoins, inpmoney, anvnamn)
      mycursor.execute(sql, val)
      mydb.commit() 
    else:
      print("du har inte råd")
  else:
    print("du har inte råd")

def Take_Coins(anvnamn):
    mycursor = mydb.cursor()
    sql = "SELECT coins FROM users2 WHERE name = %s"
    name = (anvnamn, )
    mycursor.execute(sql, name)
    myresult = mycursor.fetchall()
    clean_result2 = ""
    for x in myresult:
      coins = clean_result2 + x[0]
    return(coins)




def bet(newcoins, coins2, anvnamn, B1):
  newcoins2 = coins2 - B1 + newcoins
  mycursor = mydb.cursor()
  sql = "UPDATE users2 SET coins = %s WHERE name = %s"
  val = (newcoins2, anvnamn)
  mycursor.execute(sql, val)
  mydb.commit()