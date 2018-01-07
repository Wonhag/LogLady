import pyperclip, subprocess, os, webbrowser
storage = {}
def retrieval():
  next = raw_input('my log has something to tell you: ').lower()
  if next in storage:
    webbrowser.open('http://www.' + next + '.com')
    pyperclip.copy(storage[next])
  else:
    no_such_account = raw_input("I don't know that one, would you like to add it? ").lower()
    if no_such_account == "n":
      print "goodbye"
      retrieval()
    elif no_such_account == "y":
        add()
def add():
  u_n = raw_input('what is the website you want to save the login info of? ')
  password = raw_input('and its password? ')
  storage[u_n] = password
  retrieval()
retrieval()
