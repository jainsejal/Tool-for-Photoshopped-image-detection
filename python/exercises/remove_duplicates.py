#removing duplicates from the list. ifyou have string then u can use split to change to list so that one can iterate and we can join bach using join()
def remove_duplicates(seq):
  result = []
  for item in seq:
    if item not in result:
      result.append(item)
  return result
print remove_duplicates([1, 1, 2, 2])

"""o/p: [1, 2]"""