"""
Usage: python show_pdbs_from_uniprotID.py [uniprotID1 [uniprotID2 [uniprotID3 ...]]]
"""

import sys
import requests

uniprot_ids = sys.argv[1:]
failed_ids = []

url = 'https://www.uniprot.org/uniprot/'
ids_to_pdb = {}
failed_ids = []
for id in uniprot_ids:
    params = {
        'format': 'tab',
        'query': 'ID:{}'.format(id),
        'columns': 'id,database(PDB)'
    }
    headers = {'User-Agent': 'Python Script'}
    try:
        r = requests.get(url, params=params, headers=headers)
        ids_to_pdb[id] = str(r.text).splitlines()[-1].split('\t')[-1].split(';')
        ids_to_pdb[id].pop(-1)
    except:
        failed_ids.append(id)

print(ids_to_pdb)
if failed_ids:
    print(f"Failed to show: {failed_ids}")