import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '4_6041881815570974780.mkv')


with open(file_path, 'rb') as f:
    data = f.read()
    print("Read bytes:", len(data))
    print("First 64 bytes:", data[:64])
    
