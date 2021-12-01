#kalkulator
"""
   kalkulator - działania: dodawanie i odejmowanie
"""
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    oper=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    if oper=="1":
        num1=input("Podaj składnik 1: ")
        num2=input("Podaj składnik 2: ")
        #print(type(num1))
        logging.info("Dodaję %s i %s" % (num1, num2))
        wynik=float(num1)+float(num2)
        print("Wynik to %.2f" % wynik)
    elif oper=="2":
        num1=input("Podaj odjemną : ")
        num2=input("Podaj odjemnik: ")
        logging.info("Odejmuje %s od %s" % (num2, num1))
        wynik=float(num1)-float(num2)
        print("Wynik to %.2f" % wynik)
    elif oper=="3":
        num1=input("Podaj mnożnik 1: ")
        num2=input("Podaj mnożnik 2: ")
        logging.info("Mnożę %s i %s" % (num1, num2))
        wynik=float(num1)*float(num2)
        print("Wynik to %.2f" % wynik)
    elif oper=="4":
        num1=input("Podaj dzielną:  ")
        num2=input("Podaj dzielnik: ")
        logging.info("Dzielę %s przez %s" % (num1, num2))
        wynik=float(num1)/float(num2)
        print("Wynik to %.2f" % wynik)
    else: 
        logging.info("Nieznana operacja") 


