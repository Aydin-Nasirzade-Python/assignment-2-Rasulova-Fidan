#import libraries here

def main():
  herf=input("Enter a letter og the alphabet: ")
  if herf=="a" or herf=="e" or herf=="i" or herf=="o" or herf=="u":
    print("Entered alphabet is a vowel!")
  elif herf=="y":
    print("Sometimes it is a vowel, and sometimes it is a constant!")
  else:
    print("Entered alphabet is a consonant!")
    

  pass

if __name__ == "__main__":
  main()
