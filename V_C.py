"""
This small programs counts the amount of vowels in an
inputted word with y optionally being included by the user.
"""

print "Welcome to my vowel-counter program!" # Welcome statement

def vowel_counter():
    while True:
      word = raw_input("Enter a word/sentence to determine"
      " its number of vowels by individual vowel: ")
      if word != str(word):
          print "Did you enter a sentence?"
          continue
      else:
          break
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    y_count = 0
    total_count = 0
    for w in word: # Looks over every letter and adds to vowel if needed
        if w == "A" or w == "a":
            a_count += 1
        elif w == "E" or w == "e":
            e_count += 1
        elif w == "I" or w == "i":
            i_count += 1
        elif w == "O" or w == "o":
            o_count += 1
        elif w == "U" or w == "u":
            u_count += 1
        elif w == "Y" or w == "y":
            y_count += 1
    while True:
        y_choice = raw_input("Do you want to include 'y' as a vowel? (Y/N)")
        if y_choice in ["Y", "y", "N", "n"]:
            break
        else:
            print ("Sorry, I can't understand you. Please enter a valid "
            "answer. (Y/N))")
            continue
    if y_choice in ["Y", "y"]:
        total_count = a_count + e_count + i_count + o_count + u_count + \
        y_count
        print ("Your phrase had a total of %s vowels. Of these, you had %s "
        "a's, %s e's, %s i's, %s o's, %s u's, and %s y's.") % \
        (total_count, a_count, e_count, i_count, o_count, u_count, y_count)
    elif y_choice == "N" or y_choice == "n":
        total_count = a_count + e_count + i_count + o_count + u_count
        print ("Your phrase had a total of %s vowels. Of these, you had %s "
        "a's, %s e's, %s i's, %s o's, and %s u's.") % \
        (total_count, a_count, e_count, i_count, o_count, u_count)
            
vowel_counter()
