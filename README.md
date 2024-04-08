# Protein Marker Alignment Comparator
This Python script compares multiple markers to a singular protein in order to identify which alignment of the marker relative to the protein produces the least amount of errors or the most matches.

### Inputs:
PROTEIN: The protein sequence to which markers are compared.
MARKERS: A list of marker sequences that will be compared to the protein.
### Output:
The script outputs the best starting alignment and the number of errors for each marker at the given alignment.

How it Works:
The match() function compares each marker to the protein sequence by iterating over each position of the protein. It calculates the number of errors for each possible alignment of the marker to the protein and keeps track of the best alignment (the one with the fewest errors).

Example Usage:
def main():
    match('STTECQLKDNRAWTSLFIHTGHTECA', ['TECQRKMN', 'ALFHHTTGT', 'TTECQ', 'HT', 'ZZZ', 'TTZZZRAWT'])

if __name__ == '__main__':
    main()
    
In this example, the script is executed with a protein sequence and a list of markers. It will compare each marker to the protein and output the best starting alignment and the number of errors for each marker at the given alignment.
