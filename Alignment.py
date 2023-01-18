#Simple program which does a quick alignment from two fasta files that can be either DNA or RNA
import Bio
import string
import random
from urllib.request import urlopen
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
from Bio.Seq import Seq
from Bio import Align

#The Score_Calculator takes in two RNA sequences and the scores that the user would like to apply and returns the alignment score
def Score_Calculator(RNA1,RNA2,match,mismatch,gap_s,gap_e):
    aligning = Align.PairwiseAligner()
    aligning.match_score = match

    aligning.mismatch_score = mismatch
    aligning.open_gap_score = gap_s

    aligning.extend_gap_score = gap_e

    alignment = aligning.align(RNA1,RNA2)
    print(alignment[0])
    score = aligning.score(RNA1, RNA2)
    print(score)


#Takes in DNA strings and outputs RNA strings
def DNA_to_RNA_Converter(x):
    q=""
    for i in range(len(x)):
        if x[i]=="T":
            q+="U"
        else:
            q+=x[i]
    return q

#Takes in a fasta file and reads it then converts it into a string to be used
def fasta_to_String(x):
    with open(x, 'r') as stringer:

        next(stringer)
        better_stringer = stringer.read()
    final_string = "".join(line.strip() for line in better_stringer.splitlines())
    final_string2 = DNA_to_RNA_Converter(final_string)
    return final_string2

#Asks the user to input 2 fasta files and some alignment scores to be used then prints out the results
def Alignment_function():

    fasta1 = input("Input first fasta file ")
    fasta1_2 = fasta_to_String(fasta1)


    fasta2 = input("Input second fasta file ")
    fasta2_2 = fasta_to_String(fasta2)

    match_score = float(input("Input the match score "))
    mismatch_score = float(input("Input the mismatch score "))
    gap_opening_score = float(input("Input the gap opening score "))
    gap_extending_score = float(input("Input the gap extending score "))

    Score_Calculator(fasta1_2,fasta2_2,match_score,mismatch_score,gap_opening_score,gap_extending_score)
if __name__ == "__main__":
    Alignment_function()
