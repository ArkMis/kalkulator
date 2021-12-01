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
        num_text=input("Podaj składniki rozdzielone przecinkiem: ")
        logging.info("Dodaję składniki: %s " % num_text)
        nums = num_text.split(',')
        wynik=0
        for num in nums:
           wynik+=float(num)
        print("Wynik to %.2f" % wynik)
    elif oper=="2":
        num1=input("Podaj odjemną : ")
        num2=input("Podaj odjemnik: ")
        logging.info("Odejmuje %s od %s" % (num2, num1))
        wynik=float(num1)-float(num2)
        print("Wynik to %.2f" % wynik)
    elif oper=="3":
        num_text=input("Podaj mnożniki rozdzielone przecinkiem: ")
        logging.info("Mnożę mnożniki: %s " % num_text)
        nums = num_text.split(',')
        wynik=1
        for num in nums:
           wynik*=float(num)
        print("Wynik to %.2f" % wynik)
    elif oper=="4":
        num1=input("Podaj dzielną:  ")
        num2=input("Podaj dzielnik: ")
        if float(num2)==0:
            logging.info("Cholero nie dziel przez zero !")
        else:
            logging.info("Dzielę %s przez %s" % (num1, num2))
            wynik=float(num1)/float(num2)
            print("Wynik to %.2f" % wynik)
    else: 
        logging.info("Nieznana operacja") 


