n = int(input("Podaj liczbę: "))

def czworacze(n):

   for i in range(1,10000000):

           lista_a = []
           a = n+i
           for i in range(1,a+1):
               if a%i == 0:
                   lista_a.append(i)
           if len(lista_a)>2:
               liczba_a = "złożona"
           else:
               liczba_a = "pierwsza"
           b = a+2
           lista_b = []
           for i in range(1,b+1):
               if b%i == 0:
                   lista_b.append(i)

           if len(lista_b)>2:
               liczba_b = "złożona"
           else:
               liczba_b = "pierwsza"

           c = a+6
           lista_c = []
           for  i in range(1,c+1):
               if c%i == 0:
                   lista_c.append(i)

           if len(lista_c)>2:
               liczba_c = "złożona"
           else:
               liczba_c = "pierwsza"

           d = a+8
           lista_d = []
           for  i in range(1,d+1):
               if d%i == 0:
                   lista_d.append(i)

           if len(lista_d)>2:
               liczba_d = "złożona"

           else:
               liczba_d = "pierwsza"
           if liczba_a == "pierwsza" and liczba_b == "pierwsza" and liczba_c == "pierwsza" and liczba_d == "pierwsza":
               lista = []
               lista.append(a)
               lista.append(b)
               lista.append(c)
               lista.append(d)

               print(lista)
               break

           else:
               continue

czworacze(n)




# A[]-tablica zawierająca liczby całkowite od 1 do 200 000
# n-liczba miejsc w tablicy
# liczby czworacze p,p+2,p+6,p+8, gdzie p to liczba p.

n = 199999
A = [True] * (n+1)
i = 2
p = 2

def czyPierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def Sito(A, n):
    for i in range(2, n):
        while i <= n:
            m = 2 * i
            while m <= n:
                A[m] = 0
                m += i
            i += i
    for i in range(2, n):
        if czyPierwsza(A[i]):
            A[i] == True
        else:
            A[i] == False

(Sito(A, n))

def liczbyCzworacze(A, n):
    print('Liczby czworacze to: ')
    for p in range(2, n - 8):
        if A[p] == True and A[p + 2] == True and A[p + 6] == True and A[p + 8] == True:
            print(f"{p}, {p + 2}, {p + 6}, {p + 8} ", end=' | ')


(liczbyCzworacze(A, n))
