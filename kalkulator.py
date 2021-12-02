import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def add(num1, num2):
    """
    def add(text: num1, text: num2): -> :float
    """
    logging.info("Dodaję składniki: %s %s" % (num1, num2))
    wynik=float(num1)+float(num2)
    return wynik

def sub(num1, num2):
    """
    def sub(text: num1, text: num2): -> :float
    """
    logging.info("Odejmuje %s od %s" % (num2, num1))
    wynik=float(num1)-float(num2)
    return wynik

def mult(num1, num2):
    """
    def mult(text: num1, text: num2): -> :float
    """
    logging.info("Mnożę mnożniki: %s, %s " % (num1, num2))
    wynik=float(num1)*float(num2)
    return wynik

def div(num1,num2):
    """
    def div(text: num1, text: num2) -> :float / text if / 0
    """
    if float(num2)==0:
        logging.info("Próba dzielenia przez zero !")
        return 'brak wyniku'
    else:
        logging.info("Dzielę %s przez %s" % (num1, num2))
        wynik=float(num1)/float(num2)
        return wynik

def operation(oper):
    """
    def operation(char: oper): -> :text
    oper: 1 - dodawanie
          2 - odejmowanie
          3 - mnożenie
          4 - dzielenie
    """
    if oper=="1":
       num1=input("Podaj składnik 1: ")
       num2=input("Podaj składnik 2: ")
       # num_text=input("Podaj składniki rozdzielone przecinkiem: ")   
       # nums = num_text.split(',')
       return add(num1, num2)
    elif oper=="2":
       num1=input("Podaj odjemną : ")
       num2=input("Podaj odjemnik: ")
       return sub(num1,num2)
    elif oper=="3":
       num1=input("Podaj mnożnik 1: ")
       num2=input("Podaj mnożnik 2: ")
       #num_text=input("Podaj mnożniki rozdzielone przecinkiem: ")
       #nums = num_text.split(',')
       return mult(num1, num2)
    elif oper=="4":
        num1=input("Podaj dzielną:  ")
        num2=input("Podaj dzielnik: ")
        return div(num1,num2)
    else: 
        logging.info("Nieznana operacja")
    return ''

if __name__ == "__main__":
    oper=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    print("Wynik to %s" % operation(oper))
    


