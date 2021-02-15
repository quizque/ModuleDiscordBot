verbose_level = 0

VERBOSE_LOW  = 0
VERBOSE_MED  = 1
VERBOSE_HIGH = 2

def printV(str, lvl=0):
    if lvl >= VERBOSE_HIGH:
        print(f"[ERROR] {str}")
    elif lvl >= VERBOSE_MED:
        print(f"[WARNING] {str}")
    elif lvl == VERBOSE_LOW:
        print(f"[INFO] {str}")
    
def setVerbose(lvl):
    verbose_level = lvl