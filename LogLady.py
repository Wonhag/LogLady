import pyperclip, subprocess, os, webbrowser
def retrieval():
  storage = {'username':"password"}
  next = raw_input('my log has something to tell you: ').lower()
	if next in storage:
		webbrowser.open('http://www.' + next + '.com')
		pyperclip.copy(storage[next])
	else:
		print "I don't know that one"
		retrieval()
retrieval()
