#remove the vowels from the string
def anti_vowel(text):
  new_word = text.translate(None, "aeiouAEIOU")
  return new_word
  
  
print anti_vowel("Hey look Words!")  