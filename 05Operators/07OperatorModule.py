from os import system
import operator
system("cls")

"""
 1. add(a, b) :- This function returns addition of the given arguments. Operation-> a + b. 
 2. sub(a, b) :- This function returns difference of the given arguments. Operation-> a - b. 
 3. mul(a, b) :- This function returns product of the given arguments. Operation-> a * b.
 4. truediv(a,b) :- This function returns division of the given arguments. Operation-> a / b. 
 5. floordiv(a,b) :- This function also returns division of the given arguments. But the value is floored value i.e. returns greatest small integer. Operation-> a // b. 
 6. pow(a,b) :- This function returns exponentiation of the given arguments. Operation-> a ** b. 
 7. mod(a,b) :- This function returns modulus of the given arguments. Operation-> a % b.
 8. lt(a, b) :- This function is used to check if a is less than b or not. Returns true if a is less than b, else returns false. Operation-> a < b. 
 9. le(a, b) :- This function is used to check if a is less than or equal to b or not. Returns true if a is less than or equal to b, else returns false. Operation-> a <= b. 
 10. eq(a, b) :- This function is used to check if a is equal to b or not. Returns true if a is equal to b, else returns false. Operation-> a == b.
 11. gt(a,b) :- This function is used to check if a is greater than b or not. Returns true if a is greater than b, else returns false. Operation-> a > b. 
 12. ge(a,b) :- This function is used to check if a is greater than or equal to b or not. Returns true if a is greater than or equal to b, else returns false. Operation-> a >= b. 
 13. ne(a,b) :- This function is used to check if a is not equal to b or is equal. Returns true if a is not equal to b, else returns false. Operation-> a != b.
 """
a=4
b=3
print(f"operator.add({a}, {b})={operator.add(a,b)}")
print(f"operator.sub({a}, {b})={operator.sub(a,b)}")
print(f"operator.mul({a}, {b})={operator.mul(a,b)}")
print(f"operator.truediv({a}, {b})={operator.truediv(a,b)}")
print(f"operator.floordiv({a}, {b})={operator.floordiv(a,b)}")
print(f"operator.pow({a}, {b})={operator.pow(a,b)}")
print(f"operator.mod({a}, {b})={operator.mod(a,b)}")
print(f"operator.lt({a}, {b})={operator.lt(a,b)}")
print(f"operator.le({a}, {b})={operator.le(a,b)}")
print(f"operator.eq({a}, {b})={operator.eq(a,b)}")
print(f"operator.gt({a}, {b})={operator.gt(a,b)}")
print(f"operator.ge({a}, {b})={operator.ge(a,b)}")
print(f"operator.ne({a}, {b})={operator.ne(a,b)}")