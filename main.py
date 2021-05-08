from csv import reader
from email.utils import parseaddr

# open file in read mode
with open('import.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    headers = next(csv_reader)
    row_1 = next(csv_reader)
    print(headers)
    print(row_1)
    model_row = ''
    
    print('last_updated = models.DateTimeField(auto_now=True, editable=False)')
    print('created = models.DateTimeField(auto_now_add=True, editable=False)')
    for i, col in enumerate(row_1):
        field_name = headers[i].strip().lower().replace(' ', '_')
        model_row = field_name + ' = models.'
        if col.isnumeric():
            model_row += 'IntegerField()'
        elif '@' in col:
            model_row += 'EmailField()'
        else:
            model_row += 'TextField(max_length=100)'
        print(model_row)