limite = 1000
saldo = 2000
saque = 1500
contaEspecial = True

print(True and True)  # True
print(True and False)  # False  
print(False and True)  # False
print(False and False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(not True)  # False
print(not False)  # True

print(saldo >= saque and saque <= limite or contaEspecial and saldo >= saque)  # True