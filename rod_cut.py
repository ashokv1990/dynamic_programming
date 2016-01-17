import sys

class rod:
	def __init__(self , length , price):
		self.length = length
		self.price = price


def outer(func ):
	def inner(rods):
		sorted(rods , key = lambda rod :rod.length)
		for item in gen(rods):
			rods_repr[item[0]] = item[1]
		func(rods_repr)
	return inner


def gen(rods):
	for item in rods:
		yield (item.length , item.price)


def top_down_helper(rods , revenue , split , length):
	if length in revenue:
		return revenue[length]
	rev = 0
	if length == 0:
		revenue[length] = rev
	else:
		for i in range(1 , length+1):
			if rev < rods[i] + top_down_helper(rods , revenue , split , length-i):
				rev = rods[i] + top_down_helper(rods , revenue , split , length-i)
				split[length] = i
		revenue[length] = rev
	return rev




def top_down(rods , length):
	revenue = dict()
	split = dict()
	
	rods_repr = dict()
	sorted(rods , key = lambda rod :rod.length)
	for item in gen(rods):
		rods_repr[item[0]] = item[1]
	
	top_down_helper(rods_repr , revenue , split , length)
	
	print " Max revenue is {0}".format(revenue[length])
	n = length
	while n > 0:
		print "{0}".format(split[n])
		n = n - split[n]


def bottom_up(rods , length):
	revenue = dict()
	split = dict()
	rods_repr = dict()
	
	sorted(rods , key = lambda rod :rod.length)
	for item in gen(rods):
		rods_repr[item[0]] = item[1]
	
	revenue[0] = 0
	for i in range(1 , length + 1):
		rev = 0
		for j in range(1 , i+1):
			if rev < rods_repr[j] + revenue[i-j]:
				rev = rods_repr[j] + revenue[i-j]
				split[i] = j
		revenue[i] = rev
	print " Max revenue is {0}".format(revenue[length])
	n = length
	while n > 0:
		print "{0}".format(split[n])
		n = n - split[n]


'''
Reference Cormen recurrence relation
{p0 , p1 , ..pn} n matrix a chain of n matrixes A1A2..An
dict of tuples m[(i,j)] Number of Scalar Multiplications
Index k of breakup
n inclusive
j-i+1 should be totalmatrixes in chain
i to j-1
'''
def matrix_bottom_up(p): 
	m = dict() 
	s = dict() 
	n = len(p) - 1
	for i in range(1,n+1):
		m[(i,i)] = 0
	for chainlen in range(2,n+1):
		endofi = n-chainlen+1 
		for i in range(1 , endofi + 1):
			j = chainlen+i-1 
			m[(i,j)] = sys.maxint
			for k in range(i,j):
				q = m[(i,k)] + m[(k+1,j)] + p[i-1]*p[k]*p[j]
				if q < m[(i,j)]:
					m[(i,j)] = q
					s[(i,j)] = k
	return (m[(1,n)] , s)


def print_matrix(s , i , j):
	if i == j:
		sys.stdout.write( "A%s" %i)
	else:
		sys.stdout.write( "(")
		print_matrix(s , i , s[(i,j)]) #s[(i,j)] = k
		print_matrix(s,s[(i,j)] + 1 , j)
		sys.stdout.write(")")


def main():
	rods = [ rod(4,9) , rod(5,10) , rod(6,17) , rod(7,17) , rod(8,20) , rod(9,24) , rod(10,30) , rod(0,0) , rod(1,1) , rod(2,5) , rod(3,8)]

	for r in gen(rods):
		print "length {0} of price {1}".format(r[0],r[1])
	top_down(rods , 7)
	bottom_up(rods , 7)
	p = [30,35,15,5,10,20,25]
	result = matrix_bottom_up(p)
	print "Maximum Scalar operations is {0}".format(result[0])
	print_matrix(result[1] , 1 , len(p)-1)

if __name__ == "__main__":
	main()

