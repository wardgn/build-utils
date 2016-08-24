#!/usr/bin/python3
###!/usr/bin/env python3
'''
#Created on Aug 25, 2016

#@author: gward
'''
import re
import shutil
import sys
import os

# extract version and HF number for archive name
def nameit(version):  
    regex1 = re.compile(r'(\d\.){1,2}\d{1,}')
    regex2 = re.compile(r'(hf)(?i)\d')
    regex3 = re.compile(r'(P\d{1,2})(?i)')
    v1 = (regex1.search(version)).group(0)  # extract formatted version
    x2 = regex2.search(version)  # extract hf number, if available
    x3 = regex3.search(version)  # extract patch number, if available
    v2 = v3 = '0' 
    if x2:
        v2 = (x2.group(0)).lstrip(r'HF')
    if x3:
        v3 = (x3.group(0)).lstrip(r'P')
    return (v1, v2, v3)


    
def zipMe(mydir):

    zipName=os.path.basename(mydir)
    for subcomp in subcomps:
        arcname = dirname + '/' + components[subcomp] + subcomponents[vmajor][subcomp] + suffix  
        rootdir = dirname + '/' + subcomponents[vmajor][subcomp]
        shutil.make_archive(arcname, 'zip', mydir)
        arcnames[subcomp]=arcname

    return arcnames
    
if __name__ == '__main__':

    v=sys.argv[1] # version (branch)
    b=sys.argv[2] # build number 
    arcnames = get_arc_name(v,b)

    print (arcnames['hpux']+'.zip',arcnames['solaris']+'.zip',sep='\n')
