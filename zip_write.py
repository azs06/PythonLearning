import zipfile

print('creating archive')
with zipfile.ZipFile('write.zip', mode='w') as zf:
    print('adding readme.txt')
    zf.write('readme.txt')
    print('success')

print()
