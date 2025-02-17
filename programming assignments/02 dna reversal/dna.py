dna_seq = input("Enter a DNA sequence: ")
pattern = input("Enter the pattern: ")

marker = pattern
reversed_marker = marker[::-1]

prefix = dna_seq[0:dna_seq.find(marker)]

middle = dna_seq[dna_seq.find(marker) + len(marker): dna_seq.rfind(reversed_marker)]
# marker + length of marker to the first occurence of the reversed marker (searching from the right)

reversed_middle = middle[::-1]

suffix = dna_seq[dna_seq.find(reversed_marker, dna_seq.find(marker) + len(marker)) + len(reversed_marker):]
# search for the last index of the reversed marker only when it occurs after the marker
# everything that comes after is the suffix

result = prefix + marker + reversed_middle + reversed_marker + suffix

print(f'Prefix: {prefix}')
print(f'Marker: {marker}')
print(f'Middle: {middle}')
print(f'Reversed Middle: {reversed_middle}')
print(f'Reversed Marker: {reversed_marker}')
print(f'Suffix: {suffix}')
print(f'Result: {result}')


