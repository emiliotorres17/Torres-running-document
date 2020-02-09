#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to construct and evaluate the enstrophy
    production term.

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
#-------------------------------------------------------------------------#
# User packages                                                           #
#-------------------------------------------------------------------------#
from common_tensors     import levi_civita
#=========================================================================#
# User defined functions                                                  #
#=========================================================================#
#-------------------------------------------------------------------------#
# Permutation sign                                                        #
#-------------------------------------------------------------------------#
def epsilon_sign(
        I,
        J,
        K):

    """ Determine the sign of the Levi-Civita epsilon """
    #---------------------------------------------------------------------#
    # Calculating the sign of the Levi-Civita tensor                      #
    #---------------------------------------------------------------------#
    val     = levi_civita(I,J,K)
    if val == 1.0:
        sign    = "+"
    elif val == -1.0:
        sign    = "-"

    return sign
#-------------------------------------------------------------------------#
# Rotation sign                                                           #
#-------------------------------------------------------------------------#
def rij_sign(
        I,
        J):

    """ Determining the sign of the rotation rate tensor """
    #---------------------------------------------------------------------#
    # Calculating the sign of the rotation rate tensor                    #
    #---------------------------------------------------------------------#
    if I == 2 and J == 1:
        r1      = 1
        r2      = 2
        sign    = "-"
    if I == 1 and J == 2:
        r1      = 1
        r2      = 2                     
        sign    = ""                    
    if I == 1 and J == 3:               
        r1      = 3                     
        r2      = 1                     
        sign    = "-"                   
    if I == 3 and J == 1:
        r1      = 3
        r2      = 1
        sign    = ""
    if I == 3 and J == 2:
        r1      = 2
        r2      = 3
        sign    = "-"
    if I == 2 and J == 3:
        r1      = 2
        r2      = 3
        sign    = ""

    return (sign, r1, r2)
#-------------------------------------------------------------------------#
# Total sign of the term                                                  #
#-------------------------------------------------------------------------#
def total_sign(
        sign1   = False,
        sign2   = False,
        sign3   = False,
        sign4   = False):

    """ Determining the total sign each term """
    #---------------------------------------------------------------------#
    # Assigning values to signs                                           #
    #---------------------------------------------------------------------#
    if sign1 == "-":
        c1  = -1.0
    else:
        c1  = 1.0
    if sign2 == "-":
        c2  = -1.0
    else:
        c2  = 1.0
    if sign3 == "-":
        c3  = -1.0
    else:
        c3  = 1.0
    if sign4 == "-":
        c4  = -1.0
    else:
        c4  = 1.0
    #---------------------------------------------------------------------#
    # Total sign                                                          #
    #---------------------------------------------------------------------#
    if c1*c2*c3*c4 < 0:
        tot_sign = "-"
    else:
        tot_sign = "+"

    return tot_sign
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
    latex_path  = pwd + "%c..%clatex-inputs%c"          %(sep,sep,sep)
    #---------------------------------------------------------------------#
    # C1 term                                                             #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "S_{kl}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for  l in range(1,4):
                        if k==l:
                            count   += 1
                            string  += "\t\t"
                            #-----------------------------------------------------#
                            # Writing the beginning of the line                   #
                            #-----------------------------------------------------#
                            if count > 3:
                                string  += "&"
                                count   = 0
                            #-----------------------------------------------------#
                            # Sign of the equation                                #
                            #-----------------------------------------------------#
                            var_sign    = epsilon_sign(i,j,k)
                            if var_sign == "+" and term1 is True:
                                var_sign    = ""
                                term1       = False
                            #-----------------------------------------------------#
                            # Writing the LaTeX                                   #
                            #-----------------------------------------------------#
                            string  += var_sign
                            string  += "\\pdv{"
                            string  += "\\widetilde{\omega}_{%i}}"  %(i)
                            string  += "{x_{%i}}"                   %(l)
                            string  += "\\cdot"
                            string  += "\\pdv{S_{%i}}"              %(k)
                            string  += "{x_{%i}}"                   %(j)
                            #-----------------------------------------------------#
                            # Writing the end of  the line                        #
                            #-----------------------------------------------------#
                            if count > 2:
                                string  += "\\\\"
                            string += "\n"
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\\end{split}\n"
    string  += "}"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C2 term                                                             #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}\n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "S_{km}"
    string  += "S_{ml}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for  l in range(1,4):
                        for m in range(1,4):
                            if k==m and m==l:
                                count   += 1
                                string  += "\t\t"
                                #-----------------------------------------------------#
                                # Writing the beginning of the line                   #
                                #-----------------------------------------------------#
                                if count > 3:
                                    string  += "&"
                                    count   = 0
                                #-----------------------------------------------------#
                                # Sign of the equation                                #
                                #-----------------------------------------------------#
                                var_sign    = epsilon_sign(i,j,k)
                                if var_sign == "+" and term1 is True:
                                    var_sign    = ""
                                    term1       = False
                                #-----------------------------------------------------#
                                # Writing the LaTeX                                   #
                                #-----------------------------------------------------#
                                string  += var_sign
                                string  += "\\pdv{"
                                string  += "\\widetilde{"
                                string  += "\omega}_{%i}}"          %(i)
                                string  += "{x_{%i}}"               %(l)
                                string  += "\\cdot"
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}"               %(j)
                                string  += "S_{%i}"                 %(k)
                                string  += "S_{%i}"                 %(m)
                                #-----------------------------------------------------#
                                # Writing the end of  the line                        #
                                #-----------------------------------------------------#
                                if count > 2:
                                    string  += "\\\\"
                                string += "\n"
                                #-----------------------------------------------------#
                                # Turning off the term1 flag                          #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C3 term                                                             #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "R_{ml}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if k!=m and m!=l:
                                count   += 1
                                end     += 1
                                string  += "\t\t"
                                #-----------------------------------------------------#
                                # Adding the ampersand                                #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    string  += ""
                                #-----------------------------------------------------#
                                # Writing the beginning of the line                   #
                                #-----------------------------------------------------#
                                if count == 2:
                                    if term1 is not True:
                                       string  += "&"
                                    count   = 0
                                #-----------------------------------------------------#
                                # Sign of the equation                                #
                                #-----------------------------------------------------#
                                eps_sign                = epsilon_sign(i,j,k)
                                (rsign1, k1, m1)        = rij_sign(k,m)
                                (rsign2, m2, l2)        = rij_sign(m,l)
                                var_sign                = total_sign(eps_sign, rsign1, rsign2)
                                if var_sign == "+" and term1 is True:
                                    var_sign    = ""
                                    term1       = False
                                #-----------------------------------------------------#
                                # Writing the LaTeX                                   #
                                #-----------------------------------------------------#
                                string  += var_sign
                                string  += "\\pdv{"
                                string  += "\\widetilde{"
                                string  += "\omega}_{%i}}"      %(i)
                                string  += "{x_{%i}}"           %(l)
                                string  += "\\cdot"
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}"           %(j)
                                string  += "R_{%i%i}"           %(k1, m1)
                                string  += "R_{%i%i}"           %(m2, l2)
                                #-----------------------------------------------------#
                                # Writing the end of  the line                        #
                                #-----------------------------------------------------#
                                if end == 2:
                                    string  += "\\\\"
                                    end     = 0
                                string += "\n"
                                #-----------------------------------------------------#
                                # Turning off the term1 flag                          #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c3-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C4-1 term                                                           #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "S_{km}"
    string  += "R_{ml}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if k==m and m!=l:
                                count   += 1
                                end     += 1
                                string  += "\t\t"
                                #-----------------------------------------------------#
                                # Adding the ampersand                                #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    string  += ""
                                #-----------------------------------------------------#
                                # Writing the beginning of the line                   #
                                #-----------------------------------------------------#
                                if count == 2:
                                    if term1 is not True:
                                       string  += "&"
                                    count   = 0
                                #-----------------------------------------------------#
                                # Sign of the equation                                #
                                #-----------------------------------------------------#
                                eps_sign                = epsilon_sign(i,j,k)
                                (rsign1, m2, l2)        = rij_sign(m,l)
                                var_sign                = total_sign(eps_sign, rsign1)
                                if var_sign == "+" and term1 is True:
                                    var_sign    = ""
                                    term1       = False
                                #-----------------------------------------------------#
                                # Writing the LaTeX                                   #
                                #-----------------------------------------------------#
                                string  += var_sign
                                string  += "\\pdv{"
                                string  += "\\widetilde{"
                                string  += "\omega}_{%i}}"      %(i)
                                string  += "{x_{%i}}"           %(l)
                                string  += "\\cdot"
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}"           %(j)
                                string  += "S_{%i}"             %(k)
                                string  += "R_{%i%i}"           %(m2, l2)
                                #-----------------------------------------------------#
                                # Writing the end of  the line                        #
                                #-----------------------------------------------------#
                                if end == 2:
                                    string  += "\\\\"
                                    end     = 0
                                string += "\n"
                                #-----------------------------------------------------#
                                # Turning off the term1 flag                          #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c4-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C4-2 term                                                           #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "S_{ml}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            if k!=m and m==l:
                                count   += 1
                                end     += 1
                                string  += "\t\t"
                                #-----------------------------------------------------#
                                # Adding the ampersand                                #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    string  += ""
                                #-----------------------------------------------------#
                                # Writing the beginning of the line                   #
                                #-----------------------------------------------------#
                                if count == 2:
                                    if term1 is not True:
                                       string  += "&"
                                    count   = 0
                                #-----------------------------------------------------#
                                # Sign of the equation                                #
                                #-----------------------------------------------------#
                                eps_sign                = epsilon_sign(i,j,k)
                                (rsign1, k1, m1)        = rij_sign(k,m)
                                var_sign                = total_sign(eps_sign, rsign1)
                                if var_sign == "+" and term1 is True:
                                    var_sign    = ""
                                    term1       = False
                                #-----------------------------------------------------#
                                # Writing the LaTeX                                   #
                                #-----------------------------------------------------#
                                string  += var_sign
                                string  += "\\pdv{"
                                string  += "\\widetilde{"
                                string  += "\omega}_{%i}}"      %(i)
                                string  += "{x_{%i}}"           %(l)
                                string  += "\\cdot"
                                string  += "\\pdv{}"
                                string  += "{x_{%i}}"           %(j)
                                string  += "R_{%i%i}"           %(k1, m1)
                                string  += "S_{%i}"             %(l)
                                #-----------------------------------------------------#
                                # Writing the end of  the line                        #
                                #-----------------------------------------------------#
                                if end == 2:
                                    string  += "\\\\"
                                    end     = 0
                                string += "\n"
                                #-----------------------------------------------------#
                                # Turning off the term1 flag                          #
                                #-----------------------------------------------------#
                                if term1 is True:
                                    term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c4-2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C5 term                                                             #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "S_{mn}"
    string  += "R_{nl}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if k!=m and m==n and n!=l:
                                    count   += 1
                                    end     += 1
                                    string  += "\t\t"
                                    #-----------------------------------------------------#
                                    # Adding the ampersand                                #
                                    #-----------------------------------------------------#
                                    if term1 is True:
                                        string  += ""
                                    #-----------------------------------------------------#
                                    # Writing the beginning of the line                   #
                                    #-----------------------------------------------------#
                                    if count == 2:
                                        if term1 is not True:
                                           string  += "&"
                                        count   = 0
                                    #-----------------------------------------------------#
                                    # Sign of the equation                                #
                                    #-----------------------------------------------------#
                                    eps_sign                = epsilon_sign(i,j,k)
                                    (rsign1, k1, m1)        = rij_sign(k,m)
                                    (rsign2, n2, l2)        = rij_sign(n,l)
                                    var_sign                = total_sign(eps_sign, rsign1, rsign2)
                                    if var_sign == "+" and term1 is True:
                                        var_sign    = ""
                                        term1       = False
                                    #-----------------------------------------------------#
                                    # Writing the LaTeX                                   #
                                    #-----------------------------------------------------#
                                    string  += var_sign
                                    string  += "\\pdv{"
                                    string  += "\\widetilde{"
                                    string  += "\omega}_{%i}}"      %(i)
                                    string  += "{x_{%i}}"           %(l)
                                    string  += "\\cdot"
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}"           %(j)
                                    string  += "R_{%i%i}"           %(k1, m1)
                                    string  += "S_{%i}"             %(m)
                                    string  += "R_{%i%i}"           %(n2, l2)
                                    #-----------------------------------------------------#
                                    # Writing the end of  the line                        #
                                    #-----------------------------------------------------#
                                    if end == 2:
                                        string  += "\\\\"
                                        end     = 0
                                    string += "\n"
                                    #-----------------------------------------------------#
                                    # Turning off the term1 flag                          #
                                    #-----------------------------------------------------#
                                    if term1 is True:
                                        term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c5-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C6-1 term                                                           #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "S_{km}"
    string  += "S_{mn}"
    string  += "R_{nl}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if k==m and m==n and n!=l:
                                    count   += 1
                                    end     += 1
                                    string  += "\t\t"
                                    #-----------------------------------------------------#
                                    # Adding the ampersand                                #
                                    #-----------------------------------------------------#
                                    if term1 is True:
                                        string  += ""
                                    #-----------------------------------------------------#
                                    # Writing the beginning of the line                   #
                                    #-----------------------------------------------------#
                                    if count == 2:
                                        if term1 is not True:
                                           string  += "&"
                                        count   = 0
                                    #-----------------------------------------------------#
                                    # Sign of the equation                                #
                                    #-----------------------------------------------------#
                                    eps_sign                = epsilon_sign(i,j,k)
                                    (rsign1, n1, l1)        = rij_sign(n,l)
                                    var_sign                = total_sign(eps_sign, rsign1)
                                    if var_sign == "+" and term1 is True:
                                        var_sign    = ""
                                        term1       = False
                                    #-----------------------------------------------------#
                                    # Writing the LaTeX                                   #
                                    #-----------------------------------------------------#
                                    string  += var_sign
                                    string  += "\\pdv{"
                                    string  += "\\widetilde{"
                                    string  += "\omega}_{%i}}"      %(i)
                                    string  += "{x_{%i}}"           %(l)
                                    string  += "\\cdot"
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}"           %(j)
                                    string  += "S_{%i}"             %(k)
                                    string  += "S_{%i}"             %(m)
                                    string  += "R_{%i%i}"           %(n1,l1)
                                    #-----------------------------------------------------#
                                    # Writing the end of  the line                        #
                                    #-----------------------------------------------------#
                                    if end == 2:
                                        string  += "\\\\"
                                        end     = 0
                                    string += "\n"
                                    #-----------------------------------------------------#
                                    # Turning off the term1 flag                          #
                                    #-----------------------------------------------------#
                                    if term1 is True:
                                        term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c6-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C6-2 term                                                           #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "S_{mn}"
    string  += "S_{nl}"
    string  += " = & \n"
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                if k!=m and m==n and n==l:
                                    count   += 1
                                    end     += 1
                                    string  += "\t\t"
                                    #-----------------------------------------------------#
                                    # Adding the ampersand                                #
                                    #-----------------------------------------------------#
                                    if term1 is True:
                                        string  += ""
                                    #-----------------------------------------------------#
                                    # Writing the beginning of the line                   #
                                    #-----------------------------------------------------#
                                    if count == 2:
                                        if term1 is not True:
                                           string  += "&"
                                        count   = 0
                                    #-----------------------------------------------------#
                                    # Sign of the equation                                #
                                    #-----------------------------------------------------#
                                    eps_sign                = epsilon_sign(i,j,k)
                                    (rsign1, k1, m1)        = rij_sign(k,m)
                                    var_sign                = total_sign(eps_sign, rsign1)
                                    if var_sign == "+" and term1 is True:
                                        var_sign    = ""
                                        term1       = False
                                    #-----------------------------------------------------#
                                    # Writing the LaTeX                                   #
                                    #-----------------------------------------------------#
                                    string  += var_sign
                                    string  += "\\pdv{"
                                    string  += "\\widetilde{"
                                    string  += "\omega}_{%i}}"      %(i)
                                    string  += "{x_{%i}}"           %(l)
                                    string  += "\\cdot"
                                    string  += "\\pdv{}"
                                    string  += "{x_{%i}}"           %(j)
                                    string  += "R_{%i%i}"           %(k1,m1)
                                    string  += "S_{%i}"             %(m)
                                    string  += "S_{%i}"             %(l)
                                    #-----------------------------------------------------#
                                    # Writing the end of  the line                        #
                                    #-----------------------------------------------------#
                                    if end == 2:
                                        string  += "\\\\"
                                        end     = 0
                                    string += "\n"
                                    #-----------------------------------------------------#
                                    # Turning off the term1 flag                          #
                                    #-----------------------------------------------------#
                                    if term1 is True:
                                        term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c6-2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-1-1 term                                                         #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "S_{mn}"
    string  += "R_{np}"
    string  += "R_{pl}"
    string  += " = & \n"
    for i in range(1,2):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m==n and n!=p and p!=l:
                                        count   += 1
                                        end     += 1
                                        string  += "\t\t"
                                        #-----------------------------------------------------#
                                        # Adding the ampersand                                #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            string  += ""
                                        #-----------------------------------------------------#
                                        # Writing the beginning of the line                   #
                                        #-----------------------------------------------------#
                                        if count == 2:
                                            if term1 is not True:
                                               string  += "&"
                                            count   = 0
                                        #-----------------------------------------------------#
                                        # Sign of the equation                                #
                                        #-----------------------------------------------------#
                                        eps_sign                = epsilon_sign(i,j,k)
                                        (rsign1, k1, m1)        = rij_sign(k,m)
                                        (rsign2, n2, p2)        = rij_sign(n,p)
                                        (rsign3, p3, l3)        = rij_sign(p,l)
                                        var_sign                = total_sign(eps_sign, rsign1, rsign2, rsign3)
                                        if var_sign == "+" and term1 is True:
                                            var_sign    = ""
                                            term1       = False
                                        #-----------------------------------------------------#
                                        # Writing the LaTeX                                   #
                                        #-----------------------------------------------------#
                                        string  += var_sign
                                        string  += "\\pdv{"
                                        string  += "\\widetilde{"
                                        string  += "\omega}_{%i}}"      %(i)
                                        string  += "{x_{%i}}"           %(l)
                                        string  += "\\cdot"
                                        string  += "\\pdv{}"
                                        string  += "{x_{%i}}"           %(j)
                                        string  += "R_{%i%i}"           %(k1,m1)
                                        string  += "S_{%i}"             %(m)
                                        string  += "R_{%i%i}"           %(n2,p2)
                                        string  += "R_{%i%i}"           %(p3,l3)
                                        #-----------------------------------------------------#
                                        # Writing the end of  the line                        #
                                        #-----------------------------------------------------#
                                        if end == 2:
                                            string  += "\\\\"
                                            end     = 0
                                        string += "\n"
                                        #-----------------------------------------------------#
                                        # Turning off the term1 flag                          #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c7-1-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-1-2 term                                                         #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "S_{mn}"
    string  += "R_{np}"
    string  += "R_{pl}"
    string  += " = & \n"
    for i in range(2,3):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m==n and n!=p and p!=l:
                                        count   += 1
                                        end     += 1
                                        string  += "\t\t"
                                        #-----------------------------------------------------#
                                        # Adding the ampersand                                #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            string  += ""
                                        #-----------------------------------------------------#
                                        # Writing the beginning of the line                   #
                                        #-----------------------------------------------------#
                                        if count == 2:
                                            if term1 is not True:
                                               string  += "&"
                                            count   = 0
                                        #-----------------------------------------------------#
                                        # Sign of the equation                                #
                                        #-----------------------------------------------------#
                                        eps_sign                = epsilon_sign(i,j,k)
                                        (rsign1, k1, m1)        = rij_sign(k,m)
                                        (rsign2, n2, p2)        = rij_sign(n,p)
                                        (rsign3, p3, l3)        = rij_sign(p,l)
                                        var_sign                = total_sign(eps_sign, rsign1, rsign2, rsign3)
                                        if var_sign == "+" and term1 is True:
                                            var_sign    = ""
                                            term1       = False
                                        #-----------------------------------------------------#
                                        # Writing the LaTeX                                   #
                                        #-----------------------------------------------------#
                                        string  += var_sign
                                        string  += "\\pdv{"
                                        string  += "\\widetilde{"
                                        string  += "\omega}_{%i}}"      %(i)
                                        string  += "{x_{%i}}"           %(l)
                                        string  += "\\cdot"
                                        string  += "\\pdv{}"
                                        string  += "{x_{%i}}"           %(j)
                                        string  += "R_{%i%i}"           %(k1,m1)
                                        string  += "S_{%i}"             %(m)
                                        string  += "R_{%i%i}"           %(n2,p2)
                                        string  += "R_{%i%i}"           %(p3,l3)
                                        #-----------------------------------------------------#
                                        # Writing the end of  the line                        #
                                        #-----------------------------------------------------#
                                        if end == 2:
                                            string  += "\\\\"
                                            end     = 0
                                        string += "\n"
                                        #-----------------------------------------------------#
                                        # Turning off the term1 flag                          #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c7-1-2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-1-3 term                                                         #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "S_{mn}"
    string  += "R_{np}"
    string  += "R_{pl}"
    string  += " = & \n"
    for i in range(3,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m==n and n!=p and p!=l:
                                        count   += 1
                                        end     += 1
                                        string  += "\t\t"
                                        #-----------------------------------------------------#
                                        # Adding the ampersand                                #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            string  += ""
                                        #-----------------------------------------------------#
                                        # Writing the beginning of the line                   #
                                        #-----------------------------------------------------#
                                        if count == 2:
                                            if term1 is not True:
                                               string  += "&"
                                            count   = 0
                                        #-----------------------------------------------------#
                                        # Sign of the equation                                #
                                        #-----------------------------------------------------#
                                        eps_sign                = epsilon_sign(i,j,k)
                                        (rsign1, k1, m1)        = rij_sign(k,m)
                                        (rsign2, n2, p2)        = rij_sign(n,p)
                                        (rsign3, p3, l3)        = rij_sign(p,l)
                                        var_sign                = total_sign(eps_sign, rsign1, rsign2, rsign3)
                                        if var_sign == "+" and term1 is True:
                                            var_sign    = ""
                                            term1       = False
                                        #-----------------------------------------------------#
                                        # Writing the LaTeX                                   #
                                        #-----------------------------------------------------#
                                        string  += var_sign
                                        string  += "\\pdv{"
                                        string  += "\\widetilde{"
                                        string  += "\omega}_{%i}}"      %(i)
                                        string  += "{x_{%i}}"           %(l)
                                        string  += "\\cdot"
                                        string  += "\\pdv{}"
                                        string  += "{x_{%i}}"           %(j)
                                        string  += "R_{%i%i}"           %(k1,m1)
                                        string  += "S_{%i}"             %(m)
                                        string  += "R_{%i%i}"           %(n2,p2)
                                        string  += "R_{%i%i}"           %(p3,l3)
                                        #-----------------------------------------------------#
                                        # Writing the end of  the line                        #
                                        #-----------------------------------------------------#
                                        if end == 2:
                                            string  += "\\\\"
                                            end     = 0
                                        string += "\n"
                                        #-----------------------------------------------------#
                                        # Turning off the term1 flag                          #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c7-1-3-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-2-1 term                                                         #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "R_{mn}"
    string  += "S_{np}"
    string  += "R_{pl}"
    string  += " = & \n"
    for i in range(1,2):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m!=n and n==p and p!=l:
                                        count   += 1
                                        end     += 1
                                        string  += "\t\t"
                                        #-----------------------------------------------------#
                                        # Adding the ampersand                                #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            string  += ""
                                        #-----------------------------------------------------#
                                        # Writing the beginning of the line                   #
                                        #-----------------------------------------------------#
                                        if count == 2:
                                            if term1 is not True:
                                               string  += "&"
                                            count   = 0
                                        #-----------------------------------------------------#
                                        # Sign of the equation                                #
                                        #-----------------------------------------------------#
                                        eps_sign                = epsilon_sign(i,j,k)
                                        (rsign1, k1, m1)        = rij_sign(k,m)
                                        (rsign2, m2, n2)        = rij_sign(m,n)
                                        (rsign3, p4, l4)        = rij_sign(p,l)
                                        var_sign                = total_sign(eps_sign, rsign1, rsign2, rsign3)
                                        if var_sign == "+" and term1 is True:
                                            var_sign    = ""
                                            term1       = False
                                        #-----------------------------------------------------#
                                        # Writing the LaTeX                                   #
                                        #-----------------------------------------------------#
                                        string  += var_sign
                                        string  += "\\pdv{"
                                        string  += "\\widetilde{"
                                        string  += "\omega}_{%i}}"      %(i)
                                        string  += "{x_{%i}}"           %(l)
                                        string  += "\\cdot"
                                        string  += "\\pdv{}"
                                        string  += "{x_{%i}}"           %(j)
                                        string  += "R_{%i%i}"           %(k1,m1)
                                        string  += "R_{%i%i}"           %(m2,n2)
                                        string  += "S_{%i}"             %(n)
                                        string  += "R_{%i%i}"           %(p4,l4)
                                        #-----------------------------------------------------#
                                        # Writing the end of  the line                        #
                                        #-----------------------------------------------------#
                                        if end == 2:
                                            string  += "\\\\"
                                            end     = 0
                                        string += "\n"
                                        #-----------------------------------------------------#
                                        # Turning off the term1 flag                          #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c7-2-1-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-2-2 term                                                         #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "R_{mn}"
    string  += "S_{np}"
    string  += "R_{pl}"
    string  += " = & \n"
    for i in range(2,3):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m!=n and n==p and p!=l:
                                        count   += 1
                                        end     += 1
                                        string  += "\t\t"
                                        #-----------------------------------------------------#
                                        # Adding the ampersand                                #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            string  += ""
                                        #-----------------------------------------------------#
                                        # Writing the beginning of the line                   #
                                        #-----------------------------------------------------#
                                        if count == 2:
                                            if term1 is not True:
                                               string  += "&"
                                            count   = 0
                                        #-----------------------------------------------------#
                                        # Sign of the equation                                #
                                        #-----------------------------------------------------#
                                        eps_sign                = epsilon_sign(i,j,k)
                                        (rsign1, k1, m1)        = rij_sign(k,m)
                                        (rsign2, m2, n2)        = rij_sign(m,n)
                                        (rsign3, p4, l4)        = rij_sign(p,l)
                                        var_sign                = total_sign(eps_sign, rsign1, rsign2, rsign3)
                                        if var_sign == "+" and term1 is True:
                                            var_sign    = ""
                                            term1       = False
                                        #-----------------------------------------------------#
                                        # Writing the LaTeX                                   #
                                        #-----------------------------------------------------#
                                        string  += var_sign
                                        string  += "\\pdv{"
                                        string  += "\\widetilde{"
                                        string  += "\omega}_{%i}}"      %(i)
                                        string  += "{x_{%i}}"           %(l)
                                        string  += "\\cdot"
                                        string  += "\\pdv{}"
                                        string  += "{x_{%i}}"           %(j)
                                        string  += "R_{%i%i}"           %(k1,m1)
                                        string  += "R_{%i%i}"           %(m2,n2)
                                        string  += "S_{%i}"             %(n)
                                        string  += "R_{%i%i}"           %(p4,l4)
                                        #-----------------------------------------------------#
                                        # Writing the end of  the line                        #
                                        #-----------------------------------------------------#
                                        if end == 2:
                                            string  += "\\\\"
                                            end     = 0
                                        string += "\n"
                                        #-----------------------------------------------------#
                                        # Turning off the term1 flag                          #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c7-2-2-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
    #---------------------------------------------------------------------#
    # C7-2-3 term                                                         #
    #---------------------------------------------------------------------#
    term1   = True
    count   = 1
    end     = 0
    string  = ""
    string  += "\\begin{equation}\n"
    string  += "\\colorboxed{red}{\n"
    string  += "\t\\begin{split}  \n"
    string  += "\t\t\\varepsilon_{ijk}"
    string  += "\\pdv{\\widetilde{\\omega}_{i}}{x_{l}} \\cdot"
    string  += "\\pdv{}{x_{j}}"
    string  += "R_{km}"
    string  += "R_{mn}"
    string  += "S_{np}"
    string  += "R_{pl}"
    string  += " = & \n"
    for i in range(3,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and i!=k:
                    for l in range(1,4):
                        for m in range(1,4):
                            for n in range(1,4):
                                for p in range(1,4):
                                    if k!=m and m!=n and n==p and p!=l:
                                        count   += 1
                                        end     += 1
                                        string  += "\t\t"
                                        #-----------------------------------------------------#
                                        # Adding the ampersand                                #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            string  += ""
                                        #-----------------------------------------------------#
                                        # Writing the beginning of the line                   #
                                        #-----------------------------------------------------#
                                        if count == 2:
                                            if term1 is not True:
                                               string  += "&"
                                            count   = 0
                                        #-----------------------------------------------------#
                                        # Sign of the equation                                #
                                        #-----------------------------------------------------#
                                        eps_sign                = epsilon_sign(i,j,k)
                                        (rsign1, k1, m1)        = rij_sign(k,m)
                                        (rsign2, m2, n2)        = rij_sign(m,n)
                                        (rsign3, p4, l4)        = rij_sign(p,l)
                                        var_sign                = total_sign(eps_sign, rsign1, rsign2, rsign3)
                                        if var_sign == "+" and term1 is True:
                                            var_sign    = ""
                                            term1       = False
                                        #-----------------------------------------------------#
                                        # Writing the LaTeX                                   #
                                        #-----------------------------------------------------#
                                        string  += var_sign
                                        string  += "\\pdv{"
                                        string  += "\\widetilde{"
                                        string  += "\omega}_{%i}}"      %(i)
                                        string  += "{x_{%i}}"           %(l)
                                        string  += "\\cdot"
                                        string  += "\\pdv{}"
                                        string  += "{x_{%i}}"           %(j)
                                        string  += "R_{%i%i}"           %(k1,m1)
                                        string  += "R_{%i%i}"           %(m2,n2)
                                        string  += "S_{%i}"             %(n)
                                        string  += "R_{%i%i}"           %(p4,l4)
                                        #-----------------------------------------------------#
                                        # Writing the end of  the line                        #
                                        #-----------------------------------------------------#
                                        if end == 2:
                                            string  += "\\\\"
                                            end     = 0
                                        string += "\n"
                                        #-----------------------------------------------------#
                                        # Turning off the term1 flag                          #
                                        #-----------------------------------------------------#
                                        if term1 is True:
                                            term1   = False
    #---------------------------------------------------------------------#
    # End of the equation                                                 #
    #---------------------------------------------------------------------#
    string  += "\t\\end{split}\n"
    string  += "}\n"
    string  += "\\end{equation}"
    #---------------------------------------------------------------------#
    # Writing the output                                                  #
    #---------------------------------------------------------------------#
    f   = open(latex_path + "c7-2-3-enstrophy-production.tex", "w")
    f.write(string)
    f.close()
