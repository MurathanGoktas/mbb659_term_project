#!/usr/bin/env python3
import urllib.request
import sys
import json
# from config import known_PETases_uniprot_entry

def get_protein_sequences(known_PETases_uniprot_entry):
    """Retrieves the sequences from the UniProt database based on the list of
    UniProt ids.
    In general, 
        1. Compose your query here with the advanced search tool:
    https://www.uniprot.org/uniprot/?query=id%3Ap40925+OR+id%3Ap40926+OR+id%3Ao43175&sort=score
        2. Replace `&sort=score` with `&format=fasta`
        3. Edit this function as necessary
    Returns:
        protein_dict (dict): the updated dictionary
    """
    # This makes it so we match only the ENTRY field
    
    known_PETases_uniprot_entry_list = ['id%3A'+id for id in known_PETases_uniprot_entry]
    line = '+OR+'.join(known_PETases_uniprot_entry_list)
    url = f'https://www.uniprot.org/uniprot/?query={line}&format=fasta'
    with urllib.request.urlopen(url) as f:
        fasta = f.read().decode('utf-8').strip()
    return fasta
with open(sys.argv[1]) as json_file:
    known_PETases_uniprot_entry = json.load(json_file)["known_PETases_uniprot_entry"]
    print(known_PETases_uniprot_entry)
#print(json.load(sys.argv[1]))
#known_PETases_uniprot_entry = json.load(sys.argv[1])["known_PETases_uniprot_entry"]
f = open(sys.argv[2], "a")
f.write(get_protein_sequences(known_PETases_uniprot_entry))
f.close()