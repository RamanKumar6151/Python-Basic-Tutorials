import file1
print(f"file2 __name__={__name__}")
if __name__=="__main__":
    print("file2 is being run directly")
else:
    print("file2 is being run indirectly ")