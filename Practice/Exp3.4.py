'''Check if the given string is Abecedarian series or not.
(Abecedarian series refers to sequence or list in which the elements appear in alphabetical order.
E.g - “ABCFGIJK” is an abecedarian series but “BOA” is not)'''

def is_abcedrain(s):
    s = s.upper()
    return s == ''.join(sorted(s))

InputStr = input("Enter A String : ")

if is_abcedrain(InputStr):
    print(f"'{InputStr}' is in Abecedrian series")
else:
    print(f"'{InputStr}' is not in Abecedrian series")