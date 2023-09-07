import os
import sys

def concat_draft_genome(args, name, scaffold_file):
    sequence = ''
    header = '>concatenated_draft_genome_of_assembly:{}'.format(name)
    with open(scaffold_file, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                line = line.strip()
                sequence += line

    with open('{}/{}/{}'.format(args.output, name, 'draft_genome.fasta'), 'w') as f:
        print (header, file = f)
        print (sequence, file = f)

    return '{}/{}/{}'.format(args.output, name, 'draft_genome.fasta')