import wikipedia
import os
print('This is a search engine created by aman anand using the Wikipedia API.')
search=True
while search:
  what=input('What would you like to search up? ')
  print (wikipedia.summary(what))
  again=input('\nSearch again? y/n ')
  search_again=True
  while search_again:
    if again==('y'):
      os.system('clear')
      search_again=False
      search=True
    elif again==('n'):
      print('Come back soon!')
      search=False
