import os
import sys

from outbreak_maker import draftGenome

def assemble_illumina_reads(args):
    "Runs spades.py to assemble illumina data"
    name = args.illumina[0].split('/')[-1].split('.')[0]
    if not os.path.exists(args.output + '/' + name):
        os.system('mkdir -p {}/{}'.format(args.output, name))
    cmd = 'spades.py -1 {} -2 {} -o {}/{}/assembly --threads 8'.format(args.illumina[0], args.illumina[1], args.output, name)
    os.system(cmd)
    draft_genome = draftGenome.concat_draft_genome(args, name, '{}/{}/assembly/scaffolds.fasta'.format(args.output, name))
    print (draft_genome)
    sys.exit()
    # TBD
    return args.epi_dict

#def assemble_nanopore_reads(args):
##    os.system('RUN LONG READS ASSEMBLER')
    # TBD
 #   return epi_dict
