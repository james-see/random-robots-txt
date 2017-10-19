"""
Author: James Campbell
What: Generates a random robots.txt on Ubuntu 
Notes: Only works on Python 3.6+. apt-get install wamerican if necessary
"""

import subprocess

# change this for the number of words you want
numberofwords = 500

r = subprocess.Popen(f"shuf -n{numberofwords} /usr/share/dict/words",stdout=subprocess.PIPE,shell=True).stdout.read().splitlines()
print(r)
print(r[1].decode('utf8'))
with open('robots.txt','w') as f:
    f.write('User-agent: *\nDisallow: /\n')
    for word in r:
        f.write(f'Disallow: /{word.decode("utf8")}/\n')
exit('successfully created robots.txt, enjoy')
