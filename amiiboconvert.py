"""
amiiboconvert.py
3/12/2022
Modified Amiibo Flipper Conversion Code

Original Code by Lamp
Modified by VapidAnt

Execute with Python amiiboconvert *path*
where path is either a single .bin file or a root directory containing amiibo bin files
"""


import sys
import os


def write_output(outputPath, assemble):
    with open(outputPath.split(".bin")[0] + ".nfc", "wt") as f:
        f.write(assemble)

def assemble_code(contents):

    buffer = ""
    i = 0
    t = 0
    while i < len(contents.hex()) / 2:
        page = iter(contents[i:i + 4].hex().upper())
        value = "Page " + str(t) + ": " + " ".join(a + b for a, b in zip(page, page)) + "\n"
        buffer += value
        i += 4
        t += 1

    uid = iter(contents[0:3].hex().upper() + contents[4:8].hex().upper())
    assemble = """Filetype: Flipper NFC device
    Version: 2
    # Nfc device type can be UID, Mifare Ultralight, Bank card
    Device type: NTAG215
    # UID, ATQA and SAK are common for all formats
    UID: """ + " ".join(a + b for a, b in zip(uid, uid)) + """
    ATQA: 44 00
    SAK: 00
    # Mifare Ultralight specific data
    Signature: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    Mifare version: 00 04 04 02 01 00 11 03
    Counter 0: 0
    Tearing 0: 00
    Counter 1: 0
    Tearing 1: 00
    Counter 2: 0
    Tearing 2: 00
    Pages total: """ + str(t) + "\n" + buffer

    return assemble

def recursive_process(path):
    for file in os.listdir(path):

        print("Current file:", file)

        newPath = os.path.join(path, file)

        print("Current path:", newPath)

        if file.lower().endswith(".bin"):
            with open(newPath, 'rb') as file:
                contents = file.read()
                print("Writing:", file)
                write_output(newPath, assemble_code(contents))
        elif os.path.isdir(newPath):
            print("Pathing into:", newPath)
            recursive_process(newPath)

def main():

    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = '.'


    file = True
    path = None

    if os.path.isfile(user_input):
        path = user_input
    else:
        file = False

    if file:

        with open(path, "rb") as file:
            contents = file.read()
            write_output(path, assemble_code(contents))

    else:

        recursive_process(user_input)



if __name__ == '__main__':
    main()
    print("----Good Execution----")