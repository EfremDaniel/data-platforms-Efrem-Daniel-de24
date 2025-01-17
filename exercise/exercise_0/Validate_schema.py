
record: dict = {
    'ID': 101,
    'Name': 'Erika',
    'Is_active': True,
    'Age': 45        
   }


#--------------------------
schema:dict = {'ID':int, 'Name': str, 'Is_active':True, 'Age': int}
schema.keys



record_validation = {
    'ID': isinstance(record.get('ID'), int),
    'Name':isinstance(record.get('name'), str),
    'Is_active': isinstance(record.get('Is_active'), bool),
    'Age': isinstance(record.get('Age'), int)        
   }

for i, j in record_validation.items():
    print(f"{i}: {j}")

#-----------------------------------

