import os
import sys

from outbreak_maker import utils
from outbreak_maker import kma
from outbreak_maker import evalKmaResults

def determine_illumina_outbreak(args):
    cmd = 'kma -ipe {} {} -o {}/reference_templates -t_db {} -t {} -mem_mode -Sparse'.format(args.illumina[0], args.illumina[1], args.output,args.epi_dict['database'], args.threads)
    os.system(cmd)
    spa_file = '{}/reference_templates.spa'.format(args.output)
    template_number, template_score, reference_header_text = utils.find_best_template_from_spa_file(spa_file, args.epi_dict['database'])
    print (template_number, template_score, reference_header_text)

    input_string = " ".join(args.illumina)
    kma.KMARunner(input_string,
                  args.output + "/reference_alignment",
                  args.db_dir + "/bac_db",
                  "-mint3 -Mt1 {} -t {}".format(template_number, args.threads)).run()

    cluster_id, score = evalKmaResults.derive_kma_alignment_results()

    if cluster_id in args.epi_dict['clusters']:
        #Add as child to cluster
        pass
    else:
        epi_dict = assemble_illumina_reads(args)

    return epi_dict