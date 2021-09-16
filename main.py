from conjunto import Conjunto

a = Conjunto()
a.nomear('A')
b = Conjunto()
b.nomear('B')
c = Conjunto()
c.nomear('C')
g = Conjunto()
g.nomear('Gama')
d = Conjunto()
d.nomear('Delta')
s = Conjunto()
s.nomear('Sigma')


b.inserir(0)
b.inserir(1)
b.inserir(2)
b.inserir(3)
b.inserir(4)

a.inserir("a")
a.inserir("b")
a.inserir("c")

g.inserir("b")
g.inserir("a")
g.inserir("c")


d.inserir('a')
d.inserir('b')
d.inserir(1)
d.inserir(2)

s.inserir('a')
s.inserir(5)
s.inserir('b')
s.inserir(4)


'''print('União')
print(a.uniao(b))

print('\nContido')
print(b.contem(a))
print(b.contem(c))
print(c.contem(b))

print('\nIgual')
print(c.igual(b))
print(a.igual(c))
print(b.igual(c))

print('\nConjunto D')
d = a.interseccao(c)
d.nomear('D')
d.inserir(5)

print('\nDiferença')
e = a.diferenca(b)
e.nomear('E')

print('\n\nContido propriamente')
print(a.contidoPropriamente(b))

print('\n\nConjunto das partes')
x = b.conjuntoDasPartes()
#print(x.toString())

print('\n\ntoString')
l = Conjunto()
z = Conjunto(1,2,a,l)
print(z.toString()) '''

print('\n\nConjunto Universo')
u = a.uniao(b).uniao(c).uniao(d).uniao(g).uniao(s)
print (u.toString())

print('\n\nProduto cartesiano')
p = b.produto_cartesiano(d)
print(p.toString())

print('\n\nComplemento')
r = a.complemento(u)
print(r.toString())