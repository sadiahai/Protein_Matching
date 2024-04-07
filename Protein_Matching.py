""" 
Compares multiple markers to a singular protein in order identify which alignment of the marker relative to the protein produces the least amount of errors/the most matches.

Inputs:
  PROTEIN, MARKERS

Output:
  the best starting alignment and the errors for each MARKER at the given alignment.

 """
def match(PROTEIN, MARKERS):
	#Outer loop goes through each individual marker in list MARKERS
	for MARKER in MARKERS:
		#Sets values of errorsand bestErrors to a baseline in order to create a baseline and a variable for initial comparison
		errors=0
		bestErrors=10000
		#First inner for loop goes through each position in PROTEIN, such that  x does not continue to run after MARKER has ended 
		for x in range ((len(PROTEIN))-(len(MARKER))):
			#Second inner for loop goes through each letter of MARKER in position m to evaluate 
			errors=0
			for m in range ((len(MARKER))):
				if MARKER[m]==PROTEIN[m+x]:
					errors=errors
				if MARKER[m]!=PROTEIN[m+x]:
					errors=errors+1
			if errors<bestErrors:
				bestErrors=errors
				alignment=x
		print ("Marker", MARKER, "has", bestErrors, "errors at starting position", alignment)
def main():
	match('STTECQLKDNRAWTSLFIHTGHTECA',['TECQRKMN', 'ALFHHTTGT', 'TTECQ', 'HT', 'ZZZ', 'TTZZZRAWT'])
if __name__ == '__main__':
  main()

