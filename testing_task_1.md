### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 
#! INCLUDING THIS THERE ARE 15 ERRORS IN TOTAL AND ONE BIT OF INCORRECT CASING
```python

class CardGame:

  def checkforAce(self, card): # CAMEL CASE PROBABLY NOT AN ERROR JUST WRONG
    if card.value = 1: # SHOULD BE == NOT =
      return true
    else # MISSING COLON
      return false

  dif highest_card(self, card1 card2) # FUNCTION SHOULD START WITH DEF NOT DIF -- MISSING COMMA BETWEEN card1 AND card2 -- MISSING COLON AT END OF FUNCTION DEFINITION
    if card1.value > card2.value # MISSING COLON
      return card # SHOULD BE card1
    else # MISSING COLON
      return card2
 
# THE ENTIRE FUNCTION BELOW IS NOT INDENTED CORRECTLY
 def cards_total(cards): # MISSING SELF FROM LIST OF PARAMETERS
   total # TOTAL HAS NOT BEEN DEFINED
   for card in cards:
     total += card.value
     return "You have a total of" + total # RETURN SHOULDN'T BE INDENTED TO WORK AS REQUESTED -- MISSING SPACE AT END OF SENTENCE -- TOTAL NEEDS TO BE CONVERTED TO A STRING


```
