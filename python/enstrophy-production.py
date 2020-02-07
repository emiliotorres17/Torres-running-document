#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to write the latex for the enstrophy
    production term, namely,
        epsilon_{ijk}*d(omega_{i})/dx_{l}*d(tau_{kl})/dx_{j}

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
# User defined functions                                                  #
#=========================================================================#
#-------------------------------------------------------------------------#
# Cancelling term                                                         #
#-------------------------------------------------------------------------#
def latex_cancel(
        Term):

    """ Writing the cancelling term in latex """
    #---------------------------------------------------------------------#
    # Cancelling term                                                     #
    #---------------------------------------------------------------------#
    out = "\\cancel{" + Term + "}" 

    return out
#-------------------------------------------------------------------------#
# Color term                                                              #
#-------------------------------------------------------------------------#
def latex_color(
        Term,
        color = "red"):

    """ Writing the color term in latex, where the default is red """
    #---------------------------------------------------------------------#
    # Color term                                                          #
    #---------------------------------------------------------------------#
    out = "{\\color{" + color + "}" + Term + "}"

    return out
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
    latex_path  = pwd + "%c..%clatex-inputs%c"      %(sep,sep,sep)
    #---------------------------------------------------------------------#
    # C1 term                                                             #
    #---------------------------------------------------------------------#
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "S_{kl}"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        string  += "\t\t"
                        if l ==1:
                            string += "&"
                        if i ==1 and j==2 and k == 3 and l==1:
                            string += ""
                        else:
                            string += "+"
                        term    = "\\varepsilon_{%i%i%i}"  %(i,j,k)
                        term    += "\\pdv{\omega_{%i}}"     %(i)
                        term    += "{x_{%i}}"               %(l)
                        term    += "\\cdot"
                        term    += "\\pdv{S_{%i%i}}"        %(k,l)
                        term    += "{x_{%i}}"               %(j)
                        if k==l:
                            string  += latex_color(term)
                        else:
                            string  += latex_cancel(term)
                        string += "\n"
                    count += 1
                    string  += "\\\\"
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C2 term                                                             #
    #---------------------------------------------------------------------#
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(S_{km}S_{ml}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            string  += "\t\t"
                            if m == 1:
                                string += "&"
                            if i ==1 and j==2 and k == 3 and l==1 and m==1:
                                string += ""
                            else:
                                string += "+"
                            term    = "\\varepsilon_{%i%i%i}"  %(i,j,k)
                            term    += "\\pdv{\omega_{%i}}"     %(i)
                            term    += "{x_{%i}}"               %(l)
                            term    += "\\cdot"
                            term    += "\\pdv{}"
                            term    += "{x_{%i}}"               %(j)
                            term    += "\\left("
                            term    += "S_{%i%i}"               %(k,m)
                            term    += "S_{%i%i}"               %(m,l)
                            term    += "\\right)\n"
                            if k==m and m==l:
                                string  += latex_color(term)
                            else:
                                string  += latex_cancel(term)
                        count += 1
                        string  += "\\\\ \n"
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C3 term                                                             #
    #---------------------------------------------------------------------#
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(R_{km}R_{ml}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            string  += "\t\t"
                            if m == 1:
                                string += "&"
                            if i ==1 and j==2 and k == 3 and l==1 and m==1:
                                string += ""
                            else:
                                string += "+"
                            term    = "\\varepsilon_{%i%i%i}"  %(i,j,k)
                            term    += "\\pdv{\omega_{%i}}"     %(i)
                            term    += "{x_{%i}}"               %(l)
                            term    += "\\cdot"
                            term    += "\\pdv{}"
                            term    += "{x_{%i}}"               %(j)
                            term    += "\\left("
                            term    += "R_{%i%i}"               %(k,m)
                            term    += "R_{%i%i}"               %(m,l)
                            term    += "\\right)\n"
                            if k!=m and m!=l:
                                string  += latex_color(term)
                            else:
                                string  += latex_cancel(term)
                        count += 1
                        string  += "\\\\ \n"
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c3-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C4-1 term                                                           #
    #---------------------------------------------------------------------#
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(S_{km}R_{ml}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            string  += "\t\t"
                            if m == 1:
                                string += "&"
                            if i ==1 and j==2 and k == 3 and l==1 and m==1:
                                string += ""
                            else:
                                string += "+"
                            term    = "\\varepsilon_{%i%i%i}"  %(i,j,k)
                            term    += "\\pdv{\omega_{%i}}"     %(i)
                            term    += "{x_{%i}}"               %(l)
                            term    += "\\cdot"
                            term    += "\\pdv{}"
                            term    += "{x_{%i}}"               %(j)
                            term    += "\\left("
                            term    += "S_{%i%i}"               %(k,m)
                            term    += "R_{%i%i}"               %(m,l)
                            term    += "\\right)\n"
                            if k==m and m!=l:
                                string  += latex_color(term)
                            else:
                                string  += latex_cancel(term)
                        count += 1
                        string  += "\\\\ \n"
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c4-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C4-2 term                                                           #
    #---------------------------------------------------------------------#
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(R_{km}S_{ml}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            string  += "\t\t"
                            if m == 1:
                                string += "&"
                            string  += "-"
                            term    = "\\varepsilon_{%i%i%i}"  %(i,j,k)
                            term    += "\\pdv{\omega_{%i}}"     %(i)
                            term    += "{x_{%i}}"               %(l)
                            term    += "\\cdot"
                            term    += "\\pdv{}"
                            term    += "{x_{%i}}"               %(j)
                            term    += "\\left("
                            term    += "R_{%i%i}"               %(k,m)
                            term    += "S_{%i%i}"               %(m,l)
                            term    += "\\right)\n"
                            if k!=m and m==l:
                                string  += latex_color(term)
                            else:
                                string  += latex_cancel(term)
                        count += 1
                        string  += "\\\\ \n"
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c4-2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C5 term                                                             #
    #---------------------------------------------------------------------#
    crit    = False
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(R_{km}S_{mn}R_{nl}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if k!=m and m==n and n!=l:
                                    string  += "\t\t"
                                    if count == 2:
                                        string  += "\\\\ \n"
                                        string += "&"
                                        count   = 0
                                    if crit is not False:
                                        string  += ""
                                        crit    = True
                                    else:
                                        string  += "+"
                                    string    += "\\varepsilon_{%i%i%i}"  %(i,j,k)
                                    string    += "\\pdv{\omega_{%i}}"     %(i)
                                    string    += "{x_{%i}}"               %(l)
                                    string    += "\\cdot"
                                    string    += "\\pdv{}"
                                    string    += "{x_{%i}}"               %(j)
                                    string    += "\\left("
                                    string    += "R_{%i%i}"               %(k,m)
                                    string    += "S_{%i%i}"               %(m,n)
                                    string    += "R_{%i%i}"               %(n,l)
                                    string    += "\\right)\n"
                                    count       += 1
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c5-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C6-1 term                                                           #
    #---------------------------------------------------------------------#
    crit    = False
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(R_{km}S_{mn}R_{nl}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if k==m and m!=n and n==l:
                                    string  += "\t\t"
                                    if count == 2:
                                        string  += "\\\\ \n"
                                        string += "&"
                                        count   = 0
                                    if crit is not False:
                                        string  += ""
                                        crit    = True
                                    else:
                                        string  += "+"
                                    string    += "\\varepsilon_{%i%i%i}"  %(i,j,k)
                                    string    += "\\pdv{\omega_{%i}}"     %(i)
                                    string    += "{x_{%i}}"               %(l)
                                    string    += "\\cdot"
                                    string    += "\\pdv{}"
                                    string    += "{x_{%i}}"               %(j)
                                    string    += "\\left("
                                    string    += "S_{%i%i}"               %(k,m)
                                    string    += "R_{%i%i}"               %(m,n)
                                    string    += "S_{%i%i}"               %(n,l)
                                    string    += "\\right)\n"
                                    count       += 1
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c6-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C6-2 term                                                           #
    #---------------------------------------------------------------------#
    crit    = False
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t & \\varepsilon_{ijk}"
    string  += "\\pdv{\\omega}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "\\left(R_{km}S_{mn}S_{nl}\\right)"
    string  += " =  \\\\ \n"
    count   = 0
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if k!=m and m==n and n==l:
                                    string  += "\t\t"
                                    if count == 2:
                                        string  += "\\\\ \n"
                                        string += "&"
                                        count   = 0
                                    if crit is not False:
                                        string  += ""
                                        crit    = True
                                    else:
                                        string  += "+"
                                    string    += "\\varepsilon_{%i%i%i}"  %(i,j,k)
                                    string    += "\\pdv{\omega_{%i}}"     %(i)
                                    string    += "{x_{%i}}"               %(l)
                                    string    += "\\cdot"
                                    string    += "\\pdv{}"
                                    string    += "{x_{%i}}"               %(j)
                                    string    += "\\left("
                                    string    += "R_{%i%i}"               %(k,m)
                                    string    += "S_{%i%i}"               %(m,n)
                                    string    += "S_{%i%i}"               %(n,l)
                                    string    += "\\right)\n"
                                    count     += 1
    string += "\t\\end{split}\n"
    string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c6-2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-1 term                                                           #
    #---------------------------------------------------------------------#
    for i in range(1,4):
        crit    = False
        string  = ""
        string  += "\\begin{equation}\n"
        string  += "\t\\begin{split}\n"
        count   = 0
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m==n and n!=p and p!=l:
                                        string  += "\t\t"
                                        if count == 2:
                                            string  += "\\\\ \n"
                                            string += "&"
                                            count   = 0
                                        if crit is not False:
                                            string  += ""
                                            crit    = True
                                        else:
                                            string  += "+"
                                        string    += "\\varepsilon_{%i%i%i}"  %(i,j,k)
                                        string    += "\\pdv{\omega_{%i}}"     %(i)
                                        string    += "{x_{%i}}"               %(l)
                                        string    += "\\cdot"
                                        string    += "\\pdv{}"
                                        string    += "{x_{%i}}"               %(j)
                                        string    += "\\left("
                                        string    += "R_{%i%i}"               %(k,m)
                                        string    += "S_{%i%i}"               %(m,n)
                                        string    += "R_{%i%i}"               %(n,p)
                                        string    += "R_{%i%i}"               %(p,l)
                                        string    += "\\right)\n"
                                        count     += 1
        string += "\t\\end{split}\n"
        string += "\\end{equation}\n"
    #---------------------------------------------------------------------#
    # Writing file                                                        #
    #---------------------------------------------------------------------#
    f = open(latex_path + "c7-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
