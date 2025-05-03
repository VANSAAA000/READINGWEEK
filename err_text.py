import sys
print(f"Python Version: {sys.version}")
try:
    import libmambapy
    print("Module 'libmambapy' is successfully imported.")
except ImportError as e:
    print(e)
