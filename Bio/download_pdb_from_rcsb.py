'''
Usage: python download_pdb_from_rcsb.py PDBID1 [PDBID2 [PDBID3...]]
'''

import urllib.request
import sys

PDB_ids = sys.argv[1:]
failed_pdbs = []
for pdb in PDB_ids:
    url = f'https://files.rcsb.org/view/{pdb}.pdb'
    file_name = f'{pdb}.pdb'
    try:
        urllib.request.urlretrieve(url, file_name)
    except:
        failed_pdbs.append(pdb)
        pass
if failed_pdbs:
    print(f"Failed to download: {failed_pdbs}")