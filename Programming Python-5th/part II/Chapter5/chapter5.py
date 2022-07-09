from decimal import Decimal

print(0.1 + 0.1 + 0.1 - 0.3)
print(.1+.1)
print(.1-.3)

b= Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(b)
a=Decimal(0.1)+Decimal(0.1)+Decimal(0.1)-Decimal(0.3)
print(a)
b=Decimal('1')/Decimal('3')
print(b)

b= Decimal('0.1') + Decimal('0.100') + Decimal('0.1') - Decimal('0.3')
print(b)