import pyperclip, subprocess, os, webbrowser
def retrieval():
  storage = {'username':"password"}
  next = raw_input('my log has something to tell you: ').lower()
	if next in storage:
		webbrowser.open('http://www.' + next + '.com')
		pyperclip.copy(storage[next])
	else:
		"""print raw_input("I don't know that one, would you like to add it? ").lower()"""
		retrieval()
retrieval()
