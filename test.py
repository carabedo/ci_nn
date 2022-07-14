import ecd
path='./CondU6SanNicSupCal101'
exp = ecd.loader.Exp(path)
print(exp.loc(10,1))
