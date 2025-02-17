dna_seq = input("Enter a DNA sequence: ")
pattern = input("Enter the pattern: ")

marker = pattern
reversed_marker = marker[::-1]

split_seq = dna_seq.split(marker)
prefix = split_seq[0]
remainder = split_seq[1]

split_result = remainder.split(reversed_marker)
middle = split_result[0]
suffix = split_result[1]
reversed_middle = middle[::-1]

result = prefix + marker + reversed_middle + reversed_marker + suffix

print(f'Prefix: {prefix}')
print(f'Marker: {marker}')
print(f'Middle: {middle}')
print(f'Reversed Middle: {reversed_middle}')
print(f'Reversed Marker: {reversed_marker}')
print(f'Suffix: {suffix}')
print(f'Result: {result}')
