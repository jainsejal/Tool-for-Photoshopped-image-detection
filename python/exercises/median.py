# taking out the median from the list. Note: if total elements in the list is odd then median will the the middle number and if its even then take the sum of middle 2 elements and divide them by 2
import math
def median(seq):
  seq.sort()
  print seq
  length = len(seq)
  #mid = length/2.0
  #print length
  for i in seq:
    #for odd
    if len(seq)%2 != 0:
      index = int(math.ceil(length/2))
      #print index
      item = seq[index]
    #for even
    elif len(seq)%2 == 0:
      n = length/2
      #print n
      item = (seq[n] + seq[n-1]) / 2.0
    return item
print median([7, 12, 3, 1])

""" o/p: [1, 3, 7, 12]
5.0
"""