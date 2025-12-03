"""Demonstrate slicing operations on strings."""

def main():
	s = 'As in books on geography, Sossius Senecio, the writers crowd the\n' \
'countries of which they know nothing into the furthest margins of their\n' \
'maps, and write upon them legends such as, "In this direction lie\n' \
'waterless deserts full of wild beasts;" or, "Unexplored morasses;" or,\n' \
'"Here it is as cold as Scythia;" or, "A frozen sea;" so I, in my\n' \
'writings on Parallel Lives, go through that period of time where history\n' \
'rests on the firm basis of facts, and may truly say, "All beyond this is\n' \
'portentous and fabulous, inhabited by poets and mythologers, and there\n' \
'is nothing true or certain."\n' \
'\tFrom "Life of Theseus", Plutarch\'s Lives, Vol. I\n'
	
	# Print entire string
	print(f'Print entire string:\n {s}\n')

	# Print first 10 characters (index values 0 - 9)
	print(f'Print first 10 characters:\n {s[:10]}\n')

	# Print section of string from index 10 to 19
	print(f'Print section of string from index 10 to 19:\n {s[10:20]}\n')

	newline = '\n'
	# Print first line
	print(f'Print first line:\n {s[:s.find(newline)]}')
	

if __name__ == '__main__':
	main()