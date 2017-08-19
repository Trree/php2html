#!/usr/bin/env python
# coding=utf-8

import re
import glob
import os

for filename in glob.glob("./*.html"):
    with open(filename, "rt" ) as fin:
        file = os.path.basename(filename);
        with open("./php/"+file, "wt") as fout:
            for line in fin:
                if "<dd><a href" in line:
                    line = re.sub(r'\.php', r'.html', line, flags = re.M)
                fout.write(line)
    os.remove(filename)
