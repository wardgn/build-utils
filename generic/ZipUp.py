    # !/usr/bin/python3
    ###!/usr/bin/env python3
    '''
    #Created on Aug 25, 2016
    @file       ZipUp.py
    @author     Greta Ward <gward.ward@crowdstrike.com>
    @brief      zip up build results and send to share (\\builds.cs.sys\Build\${bamboo.buildNumber})
    @copyright  Crowdstrike, Inc, 2016

    '''
    import re
    import shutil
    import sys
    import os

    def zipMe(buildnum):
        myCwd = os.getcwd()
        zipName = os.path.basename(myCwd)
        shutil.make_archive(zipName, 'zip', 'x:\WSFX\buildnum', myCwd)

        return zipName
    
if __name__ == '__main__':

    buildnum=sys.argv[1] # build number
    arcname = zipMe(buildnum)
    print (arcname)
