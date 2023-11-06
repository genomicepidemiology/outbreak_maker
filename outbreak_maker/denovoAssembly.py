import os
import sys

from outbreak_maker import draftGenome

def assemble_illumina_reads(illumina, output, epi_dict):
    "Runs spades.py to assemble illumina data"
    name = illumina[0].split('/')[-1].split('.')[0]
    if not os.path.exists(output + '/' + name):
        os.system('mkdir -p {}/{}'.format(output, name))
    cmd = 'spades.py -1 {} -2 {} -o {}/{}/assembly --threads 8'.format(illumina[0], illumina[1], output, name)
    os.system(cmd)

    #TBD test draft function
    #111 contigs for test_10
    #FastANI works on draftgenome. To save original and make a concatenated draft genome?
    draft_genome = draftGenome.concat_draft_genome(name, '{}/{}/assembly/scaffolds.fasta'.format(output, name), output)
    if len(epi_dict['clusters']) == 0:
        cmd = 'kma index -i {} -o {} -Sparse ATG'.format(draft_genome, epi_dict['cluster_mapping_database'])
        os.system(cmd)
    else:
        cmd = 'kma -i {} -t_db {} -Sparse ATG'.format(draft_genome, epi_dict['cluster_mapping_database'])
        os.system(cmd)
    epi_dict['clusters'][name] = []

    with open('{}/{}/assembly/scaffolds.fasta'.format(output, name), 'r') as f:
        content = f.read()
        epi_dict['draft_genome'][name] = content

    with open(draft_genome, 'r') as f:
        content = f.read()
        epi_dict['concat_draft_genome'][name] = content
    return epi_dict