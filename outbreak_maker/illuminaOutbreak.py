import os
import sys

from outbreak_maker import utils
from outbreak_maker import evalKmaResults

def determine_illumina_outbreak(illumina, output, epi_dict, threads):
    print (illumina)
    for i in range(0, len(illumina), 2):
        name = illumina[i].split('/')[-1].split('.')[0]
        os.system('mkdir -p {}/{}'.format(output, name))
        output_dir = '{}/{}'.format(output, name)
        cmd = 'kma -ipe {} {} -o {}/reference_templates -t_db {} -t {} -mem_mode -Sparse'\
            .format(illumina[i], illumina[i+1], output_dir, epi_dict['cluster_mapping_database'], threads)
        print (cmd)
        os.system(cmd)
        spa_file = '{}/reference_templates.spa'.format(output_dir)
        #TBD add original pointer to draft genome
        #Save draft genome with a to the concatnated genome. Use concatnated genome for reference search only!
        template_number, template_score, reference_header_text = utils.find_best_template_from_spa_file(spa_file, epi_dict['cluster_mapping_database'])

        with open('{}/{}.fa'.format(output_dir, reference_header_text), 'w') as f:
            print (epi_dict['draft_genome'][reference_header_text], file = f)

        cmd = 'kma index -i {}/{}.fa -o {}/{}/{}_db -Sparse ATG'.format(output_dir, reference_header_text, output_dir, name, reference_header_text)
        print (cmd)
        os.system(cmd)

        cmd = 'kma -ipe {} {} -o {}/{} -t_db {}/{}/{}_db -mint3 -Mt1 {} -t {}'\
            .format(illumina[i], illumina[i+1], output_dir, name, output, name, reference_header_text, template_number, threads)
        print (cmd)
        os.system(cmd)
        sys.exit()

    cluster_id, score = evalKmaResults.derive_kma_alignment_results()

    if cluster_id in args.epi_dict['clusters']:
        #Add as child to cluster
        pass
    else:
        epi_dict = assemble_illumina_reads(args)

    return epi_dict