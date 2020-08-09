import os


def isbinod(filename):
    """This method checks for Binod presence in file """
    with open(filename, "r") as f:
        file_item = f.read()
        if "binod" in file_item.lower():
            return True
        else:
            return False


if __name__ == "__main__":

    list_dir = os.listdir()  # List all the directory of the current folder
    nBinod = 0
    for item in list_dir:
        if item.endswith("txt"):  # Check for .txt extention file
            print(f"Detecting binod in {item}")
            flag = isbinod(item)  # Detecting binod in item
            if flag:
                print(f"Binod found in {item}")
                nBinod += 1
            else:
                print(f"Binod not found in {item}")

    print("Binod detector summary")
    print(f"{nBinod} files found with hidden binod")
