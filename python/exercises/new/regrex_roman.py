# regrex with python.. According to the string tell if it is roman numbers or not in boolean 
# thousand = M{0,3} hun = C[MD]| D?C{0,3} tens = X[CL]|L?{0,3} ones = I[VX]|V?I{0,3}
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)

import re
print(str(bool(re.match(regex_pattern, raw_input()))))