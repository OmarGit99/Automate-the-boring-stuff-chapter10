
import os
import re


path = "."
dirs = os.listdir(path)

reg = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)

for file in dirs:

    if(reg.match(file)):
        a = file.split("-")

        if (int(a[1]) > 12):
            new_filename = a[1]+"-"+a[0]+"-"+a[2]
            os.rename(file, new_filename)


