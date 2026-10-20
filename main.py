import sys
from browser import document

# Redirect all future print() statements directly to the body of the web page
sys.stdout = document

print("hello")
print("This now shows up on the screen!")
