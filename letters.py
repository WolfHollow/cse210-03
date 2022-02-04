def letters(startword, letter_guessed)

  word = ""
  for i in startword:
      for j in letter_guessed:
          if j == i:
              word = word + i
      else:
          word = word + "_"
  return word
