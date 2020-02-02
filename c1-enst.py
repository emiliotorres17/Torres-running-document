#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is compute the index expansion for the SGS
    in the enstrophy equation, -(omega-del-cross-del-dot-tau).

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
#=========================================================================#
# Main                                                                    #
#=========================================================================#
if __name__ == "__main__":
    #---------------------------------------------------------------------#
    # Main preamble                                                       #
    #---------------------------------------------------------------------#
    call(["clear"])
    sep         = os.sep
    pwd         = os.getcwd()
    latex_path  = pwd + "%clatex-inputs%c"              %(sep, sep)
    #---------------------------------------------------------------------#
    # c1 -term                                                            #
    #---------------------------------------------------------------------#
    string = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += " -\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{S} ="
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        if l == 1:
                            string += "&"
                        if k !=l:
                            string  += "\t\t-\\varepsilon_{%i%i%i}" %(i,j,k)
                            string  += "\\tilde{\\omega}_{%i}"      %(i)
                            string  += "\\cancel{\\pdv{S_{%i}}"     %(k)
                            string  += "{x_{%i}}{x_{%i}}}"          %(j,l)
                        else:
                            string  += "\t\t-"
                            string  += "{\\color{red}"
                            string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                            string  += "\\tilde{\\omega}_{%i}"      %(i)
                            string  += "\\pdv{S_{%i}}"              %(k)
                            string  += "{x_{%i}}{x_{%i}}}"          %(j,l)
                        if l == 3:
                            string += "\\\\"
                        string  += "\n"
    string  += "\t\\end{split}\n"
    string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c1 -term                                                    #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c1-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c2 -term                                                            #
    #---------------------------------------------------------------------#
    string = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "&-\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{S}^2 =  \\\\ "
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if m == 1:
                                string += "&"
                            string  += "\t\t-"
                            if l!=m or m!=k:
                                string += "\\cancel{"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "S_{%i%i}"                   %(k,m)
                                string  += "S_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            else:
                                string += "{\\color{red}"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "S_{%i%i}"                   %(m,l)
                                string  += "S_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            if m == 3:
                                string += "\\\\"
                            string  += "\n"
    string  += "\t\\end{split}\n"
    string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c2 -term                                                    #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c2-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c3 -term                                                            #
    #---------------------------------------------------------------------#
    string = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "&-\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{R}^2 = \\\\"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if m == 1:
                                string += "&"
                            string  += "\t\t-"
                            if l==m or m==k:
                                string += "\\cancel{"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "R_{%i%i}"                   %(k,m)
                                string  += "R_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            else:
                                string += "{\\color{red}"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "R_{%i%i}"                   %(k,m)
                                string  += "R_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            if m == 3:
                                string += "\\\\"
                            string  += "\n"
    string  += "\t\\end{split}\n"
    string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c3-term                                                    #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c3-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c4 -term                                                            #
    #---------------------------------------------------------------------#
    string = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "&-\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{SR} = \\\\"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if m == 1:
                                string += "&"
                            string  += "\t\t-"
                            if  k!=m or m==l:
                                string  += "\\cancel{"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "S_{%i%i}"                   %(k,m)
                                string  += "R_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            else:
                                string  += "{\\color{red}"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "S_{%i%i}"                   %(k,m)
                                string  += "R_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            if m == 3:
                                string += "\\\\"
                            string  += "\n"
    string  += "\t\\end{split}\n"
    string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c4-term                                                     #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c4-1-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c4 -term                                                            #
    #---------------------------------------------------------------------#
    string = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "&\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{RS} = \\\\"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if m == 1:
                                string += "&"
                            if i==1 and j==2 and k==3 and l==1 and m==1:
                                string  += ""
                            else:
                                string  += "\t\t+"
                            if  k==m or m!=l:
                                string  += "\\cancel{"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "R_{%i%i}"                   %(k,m)
                                string  += "S_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            else:
                                string  += "{\\color{red}"
                                string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                string  += "\\tilde{\\omega}_{%i}"      %(i)
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                string  += "\\left("
                                string  += "R_{%i%i}"                   %(k,m)
                                string  += "S_{%i%i}"                   %(m,l)
                                string  += "\\right)"
                                string  += "}"
                            if m == 3:
                                string += "\\\\"
                            string  += "\n"
    string  += "\t\\end{split}\n"
    string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c4-term                                                     #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c4-2-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c5 -term                                                            #
    #---------------------------------------------------------------------#
    string = ""
    for i in range(1,4):
        string  += "$-\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{RSR}$ for $i=%i$\n"             %(i) 
        string  += "\\begin{equation}\n"
        string  += "\t\\begin{split}\n"
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                string  += "\t\t-"
                                if k==m or m!=n or n==l:
                                    string += "\\cancel{"
                                    string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                    string  += "\\tilde{"
                                    string  += "\\omega}_{%i}"              %(i)
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                    string  += "\\left("
                                    string  += "R_{%i%i}"                   %(k,m)
                                    string  += "S_{%i%i}"                   %(m,n)
                                    string  += "R_{%i%i}"                   %(n,l)
                                    string  += "\\right)"
                                    string   += "}"
                                else:
                                    string += "{\\color{red}"
                                    string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                    string  += "\\tilde{"
                                    string  += "\\omega}_{%i}"              %(i)
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                    string  += "\\left("
                                    string  += "R_{%i%i}"                   %(k,m)
                                    string  += "S_{%i%i}"                   %(m,n)
                                    string  += "R_{%i%i}"                   %(n,l)
                                    string  += "\\right)"
                                    string   += "}"
                                if n == 3:
                                    string += "\\\\"
                                string  += "\n"
        string  += "\t\\end{split}\n"
        string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c5-term                                                     #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c5-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c6-1-term                                                           #
    #---------------------------------------------------------------------#
    string = ""
    for i in range(1,4):
        string  += "$-\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{S}^2 \\mathbf{R}$ for $i=%i$\n"     %(i)  
        string  += "\\begin{equation}\n"
        string  += "\t\\begin{split}\n"
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                string  += "\t\t-"
                                if k!=m or m!=n or n==l:
                                    string += "\\cancel{"
                                    string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                    string  += "\\tilde{"
                                    string  += "\\omega}_{%i}"              %(i)
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                    string  += "\\left("
                                    string  += "S_{%i%i}"                   %(k,m)
                                    string  += "S_{%i%i}"                   %(m,n)
                                    string  += "R_{%i%i}"                   %(n,l)
                                    string  += "\\right)"
                                    string   += "}"
                                else:
                                    string += "{\\color{red}"
                                    string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                    string  += "\\tilde{"
                                    string  += "\\omega}_{%i}"              %(i)
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                    string  += "\\left("
                                    string  += "S_{%i%i}"                   %(k,m)
                                    string  += "S_{%i%i}"                   %(m,n)
                                    string  += "R_{%i%i}"                   %(n,l)
                                    string  += "\\right)"
                                    string   += "}"
                                if n == 3:
                                    string += "\\\\"
                                string  += "\n"
        string  += "\t\\end{split}\n"
        string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c6-1-term                                                   #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c6-1-enst.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # c6-2-term                                                           #
    #---------------------------------------------------------------------#
    string = ""
    for i in range(1,4):
        string  += "$\\mathbf{\\tilde{\\omega}}\\cdot\\curl \\div \\mathbf{R} \\mathbf{S}^2$ for $i=%i$\n"  %(i) 
        string  += "\\begin{equation}\n"
        string  += "\t\\begin{split}\n"
        for j in range(1,4):
            for k in range(1,4):
                if i != j and j != k and i != k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if i==1 and j==2 and k==3 and l==1 and m==1 and n ==1:
                                    string  += ""
                                else:
                                    string  += "\t\t+"
                                if k==m or m!=n or n!=l:
                                    string += "\\cancel{"
                                    string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                    string  += "\\tilde{"
                                    string  += "\\omega}_{%i}"              %(i)
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                    string  += "\\left("
                                    string  += "R_{%i%i}"                   %(k,m)
                                    string  += "S_{%i%i}"                   %(m,n)
                                    string  += "S_{%i%i}"                   %(n,l)
                                    string  += "\\right)"
                                    string   += "}"
                                else:
                                    string += "{\\color{red}"
                                    string  += "\\varepsilon_{%i%i%i}"      %(i,j,k)
                                    string  += "\\tilde{"
                                    string  += "\\omega}_{%i}"              %(i)
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}{x_{%i}}"           %(j,l)
                                    string  += "\\left("
                                    string  += "R_{%i%i}"                   %(k,m)
                                    string  += "S_{%i%i}"                   %(m,n)
                                    string  += "S_{%i%i}"                   %(n,l)
                                    string  += "\\right)"
                                    string   += "}"
                                if n == 3:
                                    string += "\\\\"
                                string  += "\n"
        string  += "\t\\end{split}\n"
        string  += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Storing c6-2-term                                                   #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c6-2-enst.tex", "w")
    f.write(string)
    f.close()
