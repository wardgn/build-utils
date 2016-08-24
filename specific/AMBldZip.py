#!/usr/bin/python3
###!/usr/bin/env python3
'''
#Created on Jul 13, 2015

#@author: gwa
'''
import re
import shutil
import sys

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
    
def get_arc_name(version,buildnum):
    
    components = {'hpux':'Applications.Manager_AM.Image_',
                  'solaris':'Applications.Manager_AM.Image_',
                  'guides':'Applications.Manager_Documentation_Guides_',
                  'relnotes':'Applications.Manager_Documentation_Release.Notes_'}
                
    subcomponents = {'8':{'hpux':'HPUX_HPIA64_HPVMS_LINUX_WINDOWS',
                          'solaris':'SOLARIS_AIX_LINUX_WINDOWS'},
                     '9':{'hpux':'HPIA64.LINUX.WINDOWS',
                          'solaris':'SOLARIS.AIX.LINUX.WINDOWS'}}

    ver, hf, p = nameit(version)  # extract version, patch and hotfix numbers
    
    pat1 = re.compile(r'^[8,9]')  # is this AM 8 or AM 9?
    vmajor = (pat1.match(ver)).group(0)
     
    pat2 = re.compile(r'.*?trunk')
    if pat2.match(version) :
        print("do not zip for trunk builds")
        exit()
    
    suffix='_'
    if vmajor == '8':
        suffix += ver + '_' + p
    else:
        suffix += ver.replace('.', '_')
    suffix += '_' + hf
    suffix += '+build.' + buildnum #+ '.zip'
    
    subcomps = 'hpux', 'solaris'  # ,'guides','relnotes'
    dirname = r'/chasm/nt4_e/invent/NT' + version 
    arcnames={}
    for subcomp in subcomps:
        arcname = dirname + '/' + components[subcomp] + subcomponents[vmajor][subcomp] + suffix  
        rootdir = dirname + '/' + subcomponents[vmajor][subcomp]
        shutil.make_archive(arcname, 'zip', rootdir)
        arcnames[subcomp]=arcname

    return arcnames
    
if __name__ == '__main__':

    v=sys.argv[1] # version (branch)
    b=sys.argv[2] # build number 
    arcnames = get_arc_name(v,b)

    print (arcnames['hpux']+'.zip',arcnames['solaris']+'.zip',sep='\n')
