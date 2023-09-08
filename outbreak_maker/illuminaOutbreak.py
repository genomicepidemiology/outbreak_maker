import os
import sys

from outbreak_maker import utils
from outbreak_maker import evalKmaResults

def determine_illumina_outbreak(args):
    for i in range(0, len(args.illumina), 2):
        name = args.illumina[i].split('/')[-1].split('.')[0]
        print (args.output)
        cmd = 'kma -ipe {} {} -o {}/reference_templates -t_db {} -t {} -mem_mode -Sparse'\
            .format(args.illumina[i], args.illumina[i+1], args.output, args.epi_dict['database'], args.threads)
        print (cmd)
        os.system(cmd)
        spa_file = '{}/reference_templates.spa'.format(args.output)
        template_number, template_score, reference_header_text = utils.find_best_template_from_spa_file(spa_file, args.epi_dict['database'])
        print (template_number, template_score, reference_header_text)

        #Determine ANI to best template
        cmd = 'kma -ipe {} {} -o {}/{} -t_db {} -mint3 -Mt1 {} -t {}'\
            .format(args.illumina[i], args.illumina[i+1], args.output, name, args.epi_dict['database'], template_number, args.threads)
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