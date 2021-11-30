#!/usr/bin/env python3
import urllib.request
import sys
import json
import os
# from config import known_PETases_uniprot_entry

def run_hmm_search(dataset_name,dataset_file):
    os.system("pwd")
    os.system("hmmsearch -T 150 -A ./data/" + dataset_file + "_hmmersearch.out" + " ./data/known_PETases.hmm ./data/metagenomic_datasets/" + dataset_file) ## " > ./data/" + dataset_name + "_hmmersearch.out")
    os.system("esl-reformat fasta ./data/" + dataset_file + "_hmmersearch.out > ./data/" + dataset_file + "_hmmersearch.out.fa")

with open(sys.argv[1]) as json_file:
    metagenomic_datasets = json.load(json_file)["metagenomic_datasets"]
    print(metagenomic_datasets)
    
for dataset_name, dataset_file in metagenomic_datasets.items():
	run_hmm_search(dataset_name,dataset_file)

#f = open(sys.argv[2], "a")
#run_hmm_search(metagenomic_datasets)
#f.write(get_protein_sequences(known_PETases_uniprot_entry))
#f.close()