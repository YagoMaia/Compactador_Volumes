import os

filepath = os.path.dirname(os.path.realpath(__file__))

dirname = os.path.dirname(filepath)
print(dirname)
# ./dir/subdir

print(type(dirname))
# <class 'str'>

subdirname = os.path.basename(os.path.dirname(filepath))
print(subdirname)
# subdir
