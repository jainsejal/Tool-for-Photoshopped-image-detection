# match phone nmber using regex conditions applied: input will be total number of phone numbers given. 1. number should be 10 digits and should start from 789

import re
i = int(raw_input())
for item in range(i):
    num = raw_input()
    match = re.match(r"[789]\d{9}$", num)
    if match:
        print "Yes"
    else:        
        print "No"