#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to build the LaTeX file for the temp
    file.

Author:
    Emilio Torres
========================================================================"""
#=========================================================================#
# Preamble                                                                #
#=========================================================================#
#-------------------------------------------------------------------------#
# Python packages                                                         #
#-------------------------------------------------------------------------#
import os
import sys
from subprocess import call
import time
import datetime
#=========================================================================#
# Main                                                                    #
#=========================================================================#
if __name__ == "__main__":
    #---------------------------------------------------------------------#
    # Main preamble                                                       #
    #---------------------------------------------------------------------#
    call(["clear"])
    sep     = os.sep
    pwd     = os.getcwd()
    py_path = pwd + "%cpython%c"            %(sep, sep)
    #---------------------------------------------------------------------#
    # Running Python                                                      #
    #---------------------------------------------------------------------#
    python_flag = False
    if python_flag is True:
        os.chdir(py_path)
        pyfile  = "enstrophy-production-2.py"
        call(["python3", pyfile])
        print("**** Successful Python run ****")
        time.sleep(3)
        os.chdir(pwd)
    #---------------------------------------------------------------------#
    # Running LaTeX                                                       #
    #---------------------------------------------------------------------#
    latex_file  = "Torres-doc"
    call(["pdflatex", latex_file + ".tex"])
    call(["clear"])
    print("**** Finished run 1 ****")
    time.sleep(2)
    call(["pdflatex", latex_file + ".tex"])
    call(["clear"])
    print("**** Finished run 2 ****")
    time.sleep(2)
    call(["pdflatex", latex_file + ".tex"])
    call(["clear"])
    print("**** Finished run 3 ****")
    time.sleep(2)
    #---------------------------------------------------------------------#
    # Changing the file name                                              #
    #---------------------------------------------------------------------#
    call(["clear"]) 
    now             = datetime.datetime.now()
    year            = '{:02d}'.format(now.year)
    month           = '{:02d}'.format(now.month)
    day             = '{:02d}'.format(now.day)
    day_month_year  = '{}_{}_{}'.format(year, month, day)
    name            = "Torres_" + day_month_year + ".pdf"
    call(['mv', latex_file + ".pdf", name])

    print("**** Successful LaTeX Run ****")
    time.sleep(1)
