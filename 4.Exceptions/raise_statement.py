s = 'apple'

try:
	num = int(s)
except ValueError:
	raise ("String can't be changed into integer")
