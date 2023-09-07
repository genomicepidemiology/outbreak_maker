import os
import sys

def assemble_illumina_reads(args):
    "Runs spades.py to assemble illumina data"
    cmd = 'spades.py -1 {} -2 {} -o {}/assembly --threads 8'.format(args.illumina[0], args.illumina[1], args.output)
    os.system(cmd)
    # TBD
    return args.epi_dict

#def assemble_nanopore_reads(args):
##    os.system('RUN LONG READS ASSEMBLER')
    # TBD
 #   return epi_dict
