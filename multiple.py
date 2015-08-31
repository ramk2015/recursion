
def factorial(n):
    if n == 1:
        return n
    else: return n * factorial(n-1)
    
def summation(n):
    if n == 1:
        return 1
    else: return n + summation(n-1)

def valuation(n):
    if n == 1:
        return 10
    else: return 10 * valuation(n-1)

def palindrome(n):
    if len (n) <= 1:
        return "is palindrome"
    elif n[0] == n[len(n)-1]:
        return palindrome(n[1:-1])
    else: return "not palindrome"


input1 = int(raw_input("enter number to do recursion: "))
input2 = str(raw_input("enter a string to do recursion: "))
print "factorial is: "
print factorial(input1)
print "summation is: "
print summation(input1)
print "Ubers Valuation in million dollars is: " 
print  valuation(input1)
print input2
print palindrome(input2)