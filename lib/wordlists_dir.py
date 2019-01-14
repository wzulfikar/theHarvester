import sys
import os

"""
get wordlists directory from env var or 
use default 'wordlists'. stop program 
using `sys.exit()` on error.
"""
class wordlists_dir:
	dirname = ""
	@staticmethod
	def get():
		# ensure the wordlists dir checking is only run once
		if len(wordlists_dir.dirname) > 0:
			return wordlists_dir.dirname

		# default wordlists is 'wordlists'
		wordlists_dir.dirname = "wordlists"

		if "WORDLISTS_DIR" in os.environ and len(os.environ['WORDLISTS_DIR'].strip()) > 0:
		    wordlists_dir.dirname = os.environ['WORDLISTS_DIR']

		if not os.path.isdir(wordlists_dir.dirname):
		    print("Error: couldn't find wordlists directory at '"+ wordlists_dir.dirname + "'.")
		    print("verify that the directory exists or provide your own wordlists")
		    print("by specifying `WORDLISTS_DIR` environment variable")
		    sys.exit()

		return wordlists_dir.dirname