import os

def batch_to_hex(input_batch_file, output_file_with_hex):
    out_hex = []
    
    out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A"])
    
    with open(input_batch_file, 'rb') as f:
        batch_content = f.read()
    
    out_hex.extend(['{:02X}'.format(b) for b in batch_content])
    
    with open(output_file_with_hex, 'wb') as f:
        for i in out_hex:
            f.write(bytes.fromhex(i))
    
    return os.path.abspath(input_batch_file), os.path.abspath(output_file_with_hex)

input_batch_file = input(f'Batch file path: ')
input_batch_filename = input_batch_file.split('\\')
output_file_with_hex = input_batch_filename[-1].split('.')[0] + '_hex.bat'

input_file_path, output_file_path = batch_to_hex(input_batch_file, output_file_with_hex)

print(f"File with hex header saved at: {output_file_path}")
