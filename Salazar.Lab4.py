def main():
    
  make_tags('i', 'Yay')
  make_tags('i', 'Hello')
  make_tags('cite', 'Yay')

  
def make_tags(tag, word):
  result = ('<',tag,'>',word,'</',tag,'>')
  return result

  
main()
