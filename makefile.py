from os import environ

platform = environ["MATRIX_PLATFORM"]
print("platform:", platform)
with open("C:/ProxSpace/pm3/proxmark3/Makefile.platform", "w") as f:
    if platform == "PM3RDV4":
        f.write("PLATFORM=PM3RDV4\n")
    elif platform == "RDV4BTADDON":
        f.write("PLATFORM=PM3RDV4\n")
        f.write("PLATFORM_EXTRAS=BTADDON\n")
    elif platform == "PM3GENERIC":
        f.write("PLATFORM=PM3GENERIC\n")
    elif platform == "GENERICWITHFLASH":
        f.write("PLATFORM=PM3GENERIC\n")
        f.write("PLATFORM_DEFS=-DWITH_FLASH\n")

with open("C:/ProxSpace/pm3/proxmark3/Makefile.platform", "r") as f:
    print(f.read())
