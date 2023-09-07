import os
import sys
import json

from outbreak_maker import illuminaOutbreak
from outbreak_maker import denovoAssembly
from outbreak_maker import nanoporeOutbreak

def determine_outbreaks(args):
    os.system('mkdir -p {}'.format(args.output))

    if args.epi_file is not None:
        with open(args.epi_file) as f:
            args.epi_dict = json.load(f)
    else:
        args.epi_dict = {}
        args.epi_dict['database'] = args.output + '/reference_database'
        args.epi_dict['clusters'] = {}
        #Remake this. Assemble index 0 and pop from list. continue
        if args.illumina != []:
            #args.epi_dict = denovoAssembly.assemble_illumina_reads(args)
            args.illumina = args.illumina[1:]
            print (args.illumina)
            sys.exit()
        elif args.nanopore != []:
            args.epi_dict = denovoAssembly.assemble_nanopore_reads(args)
        print (args.epi_dict)
        #with open(args.output + '/epi_dict.json', 'w') as f:
        #    json.dump(args.epi_dict, f)


    sys.exit()
    if args.illumina != []:
        name = args.illumina[0].split('/')[-1].split('.')[0]
        os.system('mkdir -p {}/{}'.format(args.output, name))
        args.output = '{}/{}'.format(args.output, name)
        epi_dict = illuminaOutbreak.determine_illumina_outbreak(args)
    if args.nanopore != []:
        name = args.nanopore[0].split('/')[-1].split('.')[0]
        os.system('mkdir -p {}/{}'.format(args.output, name))
        args.output = '{}/{}'.format(args.output, name)
        epi_dict = illuminaOutbreak.determine_illumina_break(args)
