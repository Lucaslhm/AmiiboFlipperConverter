"""
amiiboconvert.py
3/12/2022
Modified Amiibo Flipper Conversion Code

Original Code by Friendartiste
Modified by Lamp
Modified again by VapidAnt

Execute with Python amiiboconvert *path*
where path is either a single .bin file or a root directory containing amiibo bin files
"""

import sys
import os


def write_output(name, assemble):
    # with open(outputPath.split(".bin")[0] + ".nfc", "wt") as f:
    #    f.write(assemble)
    with open("nfcs/" + name + ".nfc", 'wt') as f:
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
    uid = " ".join(a + b for a, b in zip(uid, uid))

    assemble_arr = []
    assemble_arr.append("Filetype: Flipper NFC device")
    assemble_arr.append("Version: 2")
    assemble_arr.append("# Nfc device type can be UID, Mifare Ultralight, Bank card")
    assemble_arr.append("Device type: NTAG215")
    assemble_arr.append("# UID, ATQA and SAK are common for all formats")
    assemble_arr.append("UID: " + uid)
    assemble_arr.append("ATQA: 44 00")
    assemble_arr.append("SAK: 00")
    assemble_arr.append("# Mifare Ultralight specific data"),
    assemble_arr.append(
        "Signature: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
    assemble_arr.append("Mifare version: 00 04 04 02 01 00 11 03")
    assemble_arr.append("Counter 0: 0")
    assemble_arr.append("Tearing 0: 00")
    assemble_arr.append("Counter 1: 0")
    assemble_arr.append("Tearing 1: 00")
    assemble_arr.append("Counter 2: 0")
    assemble_arr.append("Tearing 2: 00")
    assemble_arr.append("Pages total: " + str(t) + "\n" + buffer)

    assemble = "\n".join(assemble_arr)

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
                name = os.path.split(newPath)[1]
                write_output(name.split('.bin')[0], assemble_code(contents))
                # write_output(newPath, assemble_code(contents))
        elif file.lower().endswith(".nfc"):
            print("Deleteing:", file)
            os.remove(newPath)
        elif os.path.isdir(newPath):
            print("Pathing into:", newPath)
            recursive_process(newPath)


def main():
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = './raw_amiibos'

    file = True
    path = None

    if os.path.isfile(user_input):
        path = user_input
    else:
        file = False

    if file:

        with open(path, "rb") as file:
            contents = file.read()
            name = os.path.split(path)[1]
            write_output(name.split('.bin')[0], assemble_code(contents))

    else:

        recursive_process(user_input)


if __name__ == '__main__':
    main()
    print("----Good Execution----")
