import os
def readConfig(configName):
    if not os.path.exists(configName):
        print("aaa")
        return -1
    f = open(configName,"r")
    cc = "gcc"
    src = "main.c"
    out = "main"
    msg = True
    say = "Compiling done!"
    run = False
    mke = False
    mkf = "-j$(nproc)"

    for i in f:
        z = i.strip().split()
        if len(z) == 0:
            pass
        if len(z) >= 3:
            if z[0] == "cc":
                cc = z[2]
            if z[0] == "src":
                src = z[2]
            if z[0] == "out":
                out = z[2]
            if z[0] == "msg":
                if z[2] == "true":
                    msg = True
                if z[2] == "false":
                    msg = False
            if z[0] == "say":
                x = i.strip()
                while x[0] != "=":
                    x = x[1:]
                x = x[1:]
                while x[0] == " ":
                    x = x[1:]
                say = x
            if z[0] == "run":
                if z[2] == "true":
                    run = True
                if z[2] == "false":
                    run = False
            if z[0] == "mke":
                if z[2] == "false":
                    mke = False
                if z[2] == "true":
                    mke = True
            if z[0] == "mkf":
                x = i.strip()
                while x[0] != "=":
                    x = x[1:]
                x = x[1:]
                while x[0] == " ":
                    x = x[1:]

    return (cc,src,out,msg,say,run,mke,mkf)

def genConfig(fileName="make.fmake",overWrite=False,gCC="gcc",gSRC="main.c",gOUT="main",gMSG=True,gSAY="Compiling done!",gRUN=False):
    if os.path.exists(fileName) and not overWrite:
        return -1
    elif os.path.exists(fileName) and overWrite or not os.path.exists(fileName):
        f = open(fileName,"w")
        f.write(f"cc = {gCC}\nsrc = {gSRC}\nout = {gOUT}\nmsg = {str(gMSG).lower()}\nsay = {gSAY}\nrun = {str(gRUN).lower()}\nmke = {str(mke).lower()}\nmkf = {mkf}")
        f.close()
        return 0
        
