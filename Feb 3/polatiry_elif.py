def polarity(x):
  if x > 0:
    message = "positive"
  elif x < 0:
    message = "negative"
  else:
    message = "zero"
    
  return message

def main():
    print( polarity(-3) )
    print( polarity(0) )
    print( polarity(3) )

main()