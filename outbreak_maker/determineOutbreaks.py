import os
import sys
import json

from outbreak_maker import illuminaOutbreak
from outbreak_maker import denovoAssembly
from outbreak_maker import nanoporeOutbreak

def determine_outbreaks(args):
    os.system('mkdir -p {}'.format(args.output))

    #sort nanopore and illumina
    if args.epi_file is not None:
        with open(args.epi_file) as f:
            args.epi_dict = json.load(f)
    else:
        args.epi_dict = {}
        args.epi_dict['cluster_mapping_database'] = args.output + '/reference_database'
        args.epi_dict['clusters'] = {}
        args.epi_dict['draft_genome'] = {}
        args.epi_dict['concat_draft_genome'] = {}
        #Remake this. Assemble index 0 and pop from list. continue
        if args.illumina != []:
            #Assembly first illumina
            args.epi_dict = denovoAssembly.assemble_illumina_reads([args.illumina[0], args.illumina[1]], args.output, args.epi_dict)
            args.illumina = args.illumina[2:]
        elif args.nanopore != []:
            #Assembly first nanopore
            args.epi_dict = denovoAssembly.assemble_nanopore_reads(args)
            args.nanopore = args.nanopore[1:]
        print (args.epi_dict['clusters'])
        #with open(args.output + '/epi_dict.json', 'w') as f:
        #    json.dump(args.epi_dict, f)



    if args.illumina != []:
        epi_dict = illuminaOutbreak.determine_illumina_outbreak(args.illumina, args.output, args.epi_dict, args.threads)



    #if args.nanopore != []:
    #    name = args.nanopore[0].split('/')[-1].split('.')[0]
    ##    os.system('mkdir -p {}/{}'.format(args.output, name))
    #    args.output = '{}/{}'.format(args.output, name)
    #    epi_dict = illuminaOutbreak.determine_illumina_break(args)

    with open(args.output + '/epi_dict.json', 'w') as f:
        json.dump(epi_dict, f)
