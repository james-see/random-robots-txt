"""
Author: James Campbell
What: Generates a random robots.txt on OSX 
Notes: Only works on Python 3.6+. If gshuf doesnt work do brew install coreutils
"""
import subprocess

# change this for the number of words you want
numberofwords = 500

r = subprocess.Popen(f"gshuf -n{numberofwords} /usr/share/dict/words",stdout=subprocess.PIPE,shell=True).stdout.read().splitlines()
print(r)
print(r[1].decode('utf8'))
with open('robots.txt','w') as f:
    f.write('User-agent: *\nDisallow: /\n')
    for word in r:
        f.write(f'Disallow: /{word.decode("utf8")}/\n')
exit('successfully created robots.txt, enjoy')
