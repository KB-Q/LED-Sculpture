import numpy as np

'''defining all the variables used'''

# cube is a dummy 3D matrix used for storing a single frame of an animation/pattern.
cube = np.zeros(shape=(12, 12, 8), dtype=int)

# the following are 4D matrices, which are a collection of 3D matrices. The first index represents the number of frames in that animation.
cube_xz = np.zeros(shape=(12, 12, 12, 8), dtype=int)
cube_xy = np.zeros(shape=(12, 12, 12, 8), dtype=int)
cube_yz = np.zeros(shape=(8, 12, 12, 8), dtype=int)
cube_xy_ff = np.zeros(shape=(24, 12, 12, 8), dtype=int)
cube_xz_ff = np.zeros(shape=(24, 12, 12, 8), dtype=int)
cube_yz_ff = np.zeros(shape=(16, 12, 12, 8), dtype=int)
cube_rainfall = np.zeros(shape=(40, 12, 12, 8), dtype=int)
cube_xzboing = np.zeros(shape=(24, 12, 12, 8), dtype=int)
cube_xyboing = np.zeros(shape=(24, 12, 12, 8), dtype=int)
cube_yzboing = np.zeros(shape=(16, 12, 12, 8), dtype=int)
cube_shrink_grow = np.zeros(shape=(64, 12, 12, 8), dtype=int)
cube_woop = np.zeros(shape=(10, 12, 12, 8), dtype=int)
cube_shuffle = np.zeros(shape=(48, 12, 12, 8), dtype=int)
cube_arrow = np.zeros(shape=(40, 12, 12, 8), dtype=int)
cube_edgefill = np.zeros(shape=(36, 12, 12, 8), dtype=int)
cube_helix = np.zeros(shape=(50, 12, 12, 8), dtype=int)
cube_sine = np.zeros(shape=(12, 12, 12, 8), dtype=int)
cube_socure = np.zeros(shape=(12, 12, 12, 8), dtype=int)
cube_socureletters = np.zeros(shape=(54, 12, 12, 8), dtype=int)
cube_heart = np.zeros(shape=(10, 12, 12, 8), dtype=int)
cube_pac = np.zeros(shape=(56, 12, 12, 8), dtype=int)
cube_pokeball = np.zeros(shape=(16, 12, 12, 8), dtype=int)
cube_snake = np.zeros(shape=(68, 12, 12, 8), dtype=int)
cube_dice = np.zeros(shape=(20, 12, 12, 8), dtype=int)
cube_countdown = np.zeros(shape=(40, 12, 12, 8), dtype=int)
cube_bouncing = np.zeros(shape=(40, 12, 12, 8), dtype=int)
cube_ending = np.zeros(shape=(70, 12, 12, 8), dtype=int)
cube_loading = np.zeros(shape=(15, 12, 12, 8), dtype=int)
cube_crab = np.zeros(shape=(14, 12, 12, 8), dtype=int)
cube_gangnam = np.zeros(shape=(17, 12, 12, 8), dtype=int)
cube_running = np.zeros(shape=(12, 12, 12, 8), dtype=int)
cube_ind = np.zeros(shape=(13, 12, 12, 8), dtype=int)
# strings to store the data to be written in the text file
strxy = ''
strxz = ''
stryz = ''
strxyff = ''
stryzff = ''
strxzff = ''
str_rain = ''
strxzboing = ''
strxyboing = ''
stryzboing = ''
strshrink = ''
strwoop = ''
strshuffle = ''
strarrow = ''
stredgefill = ''
strhelix = ''
strsine = ''
strsocure = ''
strsocureletters = ''
strheart = ''
strpac = ''
strpokeball = ''
strsnake = ''
strdice = ''
strcountdown = ''
strbounce = ''
strending = ''
strloading = ''
strcrab = ''
strgangnam = ''
strrunning = ''
strtaki = ''
str_ind = ''

# opening the FFT data sent from MATLAB and storing it in a separate string
taki = open(r'C:\Users\karth\OneDrive\Desktop\taki.txt', 'r')
takilist = taki.readlines()
for ctr in takilist:
    strtaki += ctr

'''Defining the functions in which the animation/pattern data is generated. At the end of each function, all the frame-data is stored in a 4D matrix. In some functions like pokeball(), pacman(), etc, the hard code data in the text file is read and stored in a 4D matrix.'''

def xz():
    for i in range(12):
        cube[:, :, :] = 0
        cube[i, :, :] = 1
        cube_xz[i, :, :, :] = cube

def xy():
    for i in range(12):
        cube[:, :, :] = 0
        cube[:, i, :] = 1
        cube_xy[i, :, :, :] = cube

def yz():
    for i in range(8):
        cube[:, :, :] = 0
        cube[:, :, i] = 1
        cube_yz[i, :, :, :] = cube

def xzboing():
    for i in range(12):
        cube[:, :, :] = 0
        cube[i, :, :] = 1
        cube_xzboing[i, :, :, :] = cube
    for i in reversed(range(12)):
        cube[:, :, :] = 0
        cube[i, :, :] = 1
        cube_xzboing[23-i, :, :, :] = cube

def xyboing():
    for i in range(12):
        cube[:, :, :] = 0
        cube[:, i, :] = 1
        cube_xyboing[i, :, :, :] = cube
    for i in reversed(range(12)):
        cube[:, :, :] = 0
        cube[:, i, :] = 1
        cube_xyboing[23-i, :, :, :] = cube

def yzboing():
    for i in range(8):
        cube[:, :, :] = 0
        cube[:, :, i] = 1
        cube_yzboing[i, :, :, :] = cube
    for i in reversed(range(8)):
        cube[:, :, :] = 0
        cube[:, :, i] = 1
        cube_yzboing[15-i, :, :, :] = cube

def xy_ff():
    cube[:, :, :] = 0
    for i in range(12):
        cube[:, i, :] = 1
        cube_xy_ff[i, :, :, :] = cube
    for i in range(12):
        cube[:, i, :] = 0
        cube_xy_ff[i, :, :, :] = cube

def xz_ff():
    cube[:, :, :] = 0
    for i in range(12):
        cube[i, :, :] = 1
        cube_xy_ff[i, :, :, :] = cube

    for i in range(12):
        cube[i, :, :] = 0
        cube_xy_ff[i, :, :, :] = cube

def yz_ff():
    cube[:, :, :] = 0
    for i in range(8):
        cube[:, :, i] = 1
        cube_xy_ff[i, :, :, :] = cube

    for i in range(8):
        cube[:, :, i] = 0
        cube_xy_ff[i, :, :, :] = cube

def rainfall():
    cube[:, :, :] = 0
    for i in range(40):
        if i >= 1:
            for j in reversed(range(1, 12)):
                cube[:, j, :] = cube[:, j - 1, :]

        cube[:, 0, :] = np.random.randint(2, size=(12, 8))
        cube_rainfall[i, :, :, :] = cube

def shrink_grow():
    for i in range(8):  # (0,11,0)
        cube[:, :, :] = 0

        cube[0, i:12, 0] = 1
        cube[11-i, i:12, 0] = 1
        cube[11-i, i:12, 7-i] = 1
        cube[0, i:12, 7-i] = 1

        cube[0:12-i, i, 0] = 1
        cube[0, i, 0:8-i] = 1
        cube[0:12-i, i, 7-i] = 1
        cube[11-i, i, 0:8-i] = 1

        cube[0:12-i, 11, 0] = 1
        cube[0, 11, 0:8-i] = 1
        cube[0:12-i, 11, 7-i] = 1
        cube[11-i, 11, 0:8-i] = 1

        cube_shrink_grow[i, :, :, :] = cube

    for i in reversed(range(8)):  # (0,11,0)
        cube[:, :, :] = 0

        cube[0, i:12, 0] = 1
        cube[11-i, i:12, 0] = 1
        cube[11-i, i:12, 7-i] = 1
        cube[0, i:12, 7-i] = 1

        cube[0:12-i, i, 0] = 1
        cube[0, i, 0:8-i] = 1
        cube[0:12-i, i, 7-i] = 1
        cube[11-i, i, 0:8-i] = 1

        cube[0:12-i, 11, 0] = 1
        cube[0, 11, 0:8-i] = 1
        cube[0:12-i, 11, 7-i] = 1
        cube[11-i, 11, 0:8-i] = 1

        cube_shrink_grow[15-i, :, :, :] = cube

    for i in range(8):  # (0,11,7)
        cube[:, :, :] = 0

        cube[0, i:12, i] = 1
        cube[11-i, i:12, i] = 1
        cube[11-i, i:12, 7] = 1
        cube[0, i:12, 7] = 1

        cube[0, i, i:8] = 1
        cube[11-i, i, i:8] = 1
        cube[0:12-i, i, i] = 1
        cube[0:12-i, i, 7-i] = 1

        cube[0, 11, i:8] = 1
        cube[11-i, 11, i:8] = 1
        cube[0:12-i, 11, i] = 1
        cube[0:12-i, 11, 7-i] = 1

        cube_shrink_grow[16+i, :, :, :] = cube

    for i in reversed(range(8)):  # (0,11,7)
        cube[:, :, :] = 0

        cube[0, i:12, i] = 1
        cube[11-i, i:12, i] = 1
        cube[11-i, i:12, 7] = 1
        cube[0, i:12, 7] = 1

        cube[0, i, i:8] = 1
        cube[11-i, i, i:8] = 1
        cube[0:12-i, i, i] = 1
        cube[0:12-i, i, 7-i] = 1

        cube[0, 11, i:8] = 1
        cube[11-i, 11, i:8] = 1
        cube[0:12-i, 11, i] = 1
        cube[0:12-i, 11, 7-i] = 1

        cube_shrink_grow[16+15-i, :, :, :] = cube

    for i in range(8):  # (0,0,0)
        cube[:, :, :] = 0
        cube[0, 0:12-i, 0] = 1
        cube[0, 0:12-i, 7-i] = 1
        cube[11-i, 0:12-i, 0] = 1
        cube[11-i, 0:12-i, 7-i] = 1

        cube[0:12-i, 0, 0] = 1
        cube[0:12-i, 0, 7-i] = 1
        cube[0, 0, 0:8-i] = 1
        cube[11-i, 0, 0:8-i] = 1

        cube[0:12-i, 11-i, 0] = 1
        cube[0:12-i, 11-i, 7-i] = 1
        cube[0, 11-i, 0:8-i] = 1
        cube[11-i, 11-i, 0:8-i] = 1

        cube_shrink_grow[32+i, :, :, :] = cube

    for i in reversed(range(8)):  # (0,0,0)
        cube[:, :, :] = 0
        cube[0, 0:12 - i, 0] = 1
        cube[0, 0:12 - i, 7 - i] = 1
        cube[11 - i, 0:12 - i, 0] = 1
        cube[11 - i, 0:12 - i, 7 - i] = 1

        cube[0:12 - i, 0, 0] = 1
        cube[0:12 - i, 0, 7 - i] = 1
        cube[0, 0, 0:8 - i] = 1
        cube[11 - i, 0, 0:8 - i] = 1

        cube[0:12 - i, 11 - i, 0] = 1
        cube[0:12 - i, 11 - i, 7 - i] = 1
        cube[0, 11 - i, 0:8 - i] = 1
        cube[11 - i, 11 - i, 0:8 - i] = 1

        cube_shrink_grow[32+15-i, :, :, :] = cube

    for i in range(8):  # (0,0,7)
        cube[:, :, :] = 0
        cube[0, 0:12-i, i] = 1
        cube[0, 0:12-i, 7] = 1
        cube[11-i, 0:12-i, i] = 1
        cube[11-i, 0:12-i, 7] = 1

        cube[0, 0, i:8] = 1
        cube[11-i, 0, i:8] = 1
        cube[0:12-i, 0, i] = 1
        cube[0:12-i, 0, 7] = 1

        cube[0, 11-i, i:8] = 1
        cube[11-i, 11-i, i:8] = 1
        cube[0:12-i, 11-i, i] = 1
        cube[0:12-i, 11-i, 7] = 1

        cube_shrink_grow[48+i, :, :, :] = cube

    for i in reversed(range(8)):  # (0,0,7)
        cube[:, :, :] = 0
        cube[0, 0:12 - i, i] = 1
        cube[0, 0:12 - i, 7] = 1
        cube[11 - i, 0:12 - i, i] = 1
        cube[11 - i, 0:12 - i, 7] = 1

        cube[0, 0, i:8] = 1
        cube[11 - i, 0, i:8] = 1
        cube[0:12 - i, 0, i] = 1
        cube[0:12 - i, 0, 7] = 1

        cube[0, 11 - i, i:8] = 1
        cube[11 - i, 11 - i, i:8] = 1
        cube[0:12 - i, 11 - i, i] = 1
        cube[0:12 - i, 11 - i, 7] = 1

        cube_shrink_grow[48+15-i, :, :, :] = cube

def woop_woop():
    for i in range(5):
        cube[:, :, :] = 0
        cube[i:12-i, i, i] = 1
        cube[i:12-i, i, 7-i] = 1
        cube[i:12-i, 11-i, i] = 1
        cube[i:12-i, 11-i, 7-i] = 1

        cube[i, i:12-i, i] = 1
        cube[11-i, i:12-i, i] = 1
        cube[i, i:12-i, 7-i] = 1
        cube[11-i, i:12-i, 7-i] = 1

        cube[i, i, i:7-i] = 1
        cube[11-i, i, i:7-i] = 1
        cube[i, 11-i, i:7-i] = 1
        cube[11-i, 11-i, i:7-i] = 1

        cube_woop[i, :, :, :] = cube

    for i in reversed(range(5)):
        cube[:, :, :] = 0
        cube[i:12-i, i, i] = 1
        cube[i:12-i, i, 7-i] = 1
        cube[i:12-i, 11-i, i] = 1
        cube[i:12-i, 11-i, 7-i] = 1

        cube[i, i:12-i, i] = 1
        cube[11-i, i:12-i, i] = 1
        cube[i, i:12-i, 7-i] = 1
        cube[11-i, i:12-i, 7-i] = 1

        cube[i, i, i:8-i] = 1
        cube[11-i, i, i:8-i] = 1
        cube[i, 11-i, i:8-i] = 1
        cube[11-i, 11-i, i:8-i] = 1

        cube_woop[9-i, :, :, :] = cube

def shuffle_plane():
    for i in range(12):
        cube[:, :, :] = 0
        cube[:, 0, :] = 1
        cube[:, 11, :] = 1
        cube[0, :, :] = 1
        cube[11, :, :] = 1

        cube[i, :, :] = 1
        cube_shuffle[i, :, :, :] = cube

    for i in range(12):
        cube[:, :, :] = 0
        cube[:, 0, :] = 1
        cube[:, 11, :] = 1
        cube[0, :, :] = 1
        cube[11, :, :] = 1

        cube[:, i, :] = 1
        cube_shuffle[12+i, :, :, :] = cube

    for i in reversed(range(12)):
        cube[:, :, :] = 0
        cube[:, 0, :] = 1
        cube[:, 11, :] = 1
        cube[0, :, :] = 1
        cube[11, :, :] = 1

        cube[i, :, :] = 1
        cube_shuffle[24+11-i, :, :, :] = cube

    for i in reversed(range(12)):
        cube[:, :, :] = 0
        cube[:, 0, :] = 1
        cube[:, 11, :] = 1
        cube[0, :, :] = 1
        cube[11, :, :] = 1

        cube[:, i, :] = 1
        cube_shuffle[36+11-i, :, :, :] = cube

def arrow():
    s = '0000000000000000000000000000000000000001000001100011000011100111111111' \
           '00011111111100001100001110000100000110000000000000000000000000000000000000'
    cube2 = np.zeros(shape=(12, 40), dtype=int)
    for i in range(12):
        for j in range(12):
            cube2[i, j] = int(s[12*i+j])

    for i in range(40):
        cube[:, :, 0] = cube2[:, 0:12]
        cube[0, :, :] = cube2[:, 12:20]
        cube[:, :, 7] = cube2[:, 20:32]
        cube[11, :, :] = cube2[:, 32:40]
        cube2[:, i-1] = cube2[:, i]
        cube_arrow[i, :, :, :] = cube

def edgefill():
    file = open(r'C:\Users\karth\OneDrive\Desktop\edgefill.txt', 'r')
    # opening the file containing the hard code data generated using the website
    s = file.readlines()
    for i in range(36):
        s[i] = s[i].rstrip()
    for i in range(36):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_edgefill[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    file.close()

def helix():
    s = '000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000' \
        '000000110000000000000000000000000000000000000000000000000000000000000000000000000000000011000000' \
        '000000000000000000001000000000000000000000000000000000000000000000000000000100000000000000000000' \
        '000000000000000000000000000000000100000000000100001000000000001000000000000000000000000000000000' \
        '000000000000000000000000001000000000001000000000000000000100000000000100000000000000000000000000' \
        '000000000000000100000000000000000000000000000000000000000000000000000000000000001000000000000000'
    cube[:, :, :] = 0
    for i in range(6):
        for j in range(8):
            for x in range(12):
                cube[x, i, j] = int(s[12*8*i + 12*j + x])
                cube[x, 6+i, j] = int(s[12*8*i + 12*j + x])

    for j in range(50):
        for i in reversed(range(12)):
            cube[:, i, :] = cube[:, i-1, :]
        cube_helix[j, :, :, :] = cube

def sine():
    file = open(r'C:\Users\karth\OneDrive\Desktop\sine.txt', 'r')
    s = file.readlines()
    for i in range(12):
        s[i] = s[i].strip() # to remove all the newlines which can't be converted into integer.
    for i in range(12):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_sine[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    file.close()

def socure():
    file = open(r'C:\Users\karth\OneDrive\Desktop\socure.txt', 'r')
    s = file.readlines()
    for i in range(8):
        s[i] = s[i].rstrip()
    for i in range(8):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_socure[i, x, y, z] = int(s[i][12*12*z + 12*y + x])
    file.close()
    cube_socure[8, :, :, :] = cube_socure[9, :, :, :] = cube_socure[10, :, :, :] = cube_socure[11, :, :, :] \
        = cube_socure[7, :, :, :]

def socure_letters():
    cube[:, :, :] = 0
    s = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000001100011000110100101110011100000000000000000000000000010010100101000100101001' \
        '0100000000000000000000000000000100001001010001001010010100000000000000000000000000000011001001010001' \
        '00101110011100000000000000000000000000000010100101000100101100010000000000000000000000000000010010100' \
        '101000100101010010000000000000000000000000000001100011000110011001001011100000000000000000000000000000' \
        '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000'
    cube2 = np.zeros(shape=(12, 54), dtype=int)
    for i in range(12):
        for j in range(54):
            cube2[i, j] = int(s[12*i + j])

    for j in range(54):
        for i in range(12):
            cube[i, :, 0] = cube2[:, i]
            cube2[:, j] = cube2[:, j-1]
        cube_socureletters[j, :, :, :] = cube

def heart():
    file = open(r'C:\Users\karth\OneDrive\Desktop\heart.txt', 'r')
    s = file.readlines()
    for i in range(10):
        s[i] = s[i].rstrip()
    for i in range(10):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_heart[i, x, y, z] = int(s[i][12*12*z + 12*y + x])
    file.close()

def pacman():
    file = open(r'C:\Users\karth\OneDrive\Desktop\pacman.txt', 'r')
    s = file.readlines()
    for i in range(14):
        s[i] = s[i].rstrip()
    for i in range(14):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_pac[i, x, y, z] = int(s[i][12*12*z + 12*y + x])
    for i in range(14):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_pac[14+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(14):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_pac[28+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(14):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_pac[42+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])

    file.close()

def pokeball():
    file = open(r'C:\Users\karth\OneDrive\Desktop\pokeball.txt', 'r')
    s = file.readlines()
    for i in range(16):
        s[i] = s[i].rstrip()
    for i in range(16):
        for x in range(12):
            for y in range(12):
                cube_pokeball[i, x, y, 0] = int(s[i][12*y + x])
    file.close()

def gangnam():
    file = open(r'C:\Users\karth\OneDrive\Desktop\gangnam.txt', 'r')
    s = file.readlines()
    for i in range(6):
        s[i] = s[i].rstrip()
    for i in range(17):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_gangnam[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])

    file.close()

def running_man():
    file = open(r'C:\Users\karth\OneDrive\Desktop\runningman.txt', 'r')
    s = file.readlines()
    for i in range(12):
        s[i] = s[i].rstrip()
    for i in range(12):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_running[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])

    file.close()

def snake():
    file = open(r'C:\Users\karth\OneDrive\Desktop\snake_game.txt', 'r')
    s = file.readlines()
    for i in range(62):
        s[i] = s[i].rstrip()
    for i in range(62):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_snake[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    file.close()

def dice():
    file = open(r'C:\Users\karth\OneDrive\Desktop\shaastra_dice.txt', 'r')
    s = file.readline()
    cube2 = np.zeros(shape=(12, 20), dtype=int)
    for i in range(12):
        for j in range(20):
            cube2[i, j] = int(s[12*i + j])

    cube[:, :, :] = 0

    for i in range(20):
        cube2[:, i-1] = cube2[:, i]
        for j in range(12):
            cube[j, :, 0] = cube2[:, j]
        cube_dice[i, :, :, :] = cube

def countdown():
    s5 = '0000000000000000000000000001111100000001000000000001000000000001' \
         '11100000000000010000000000010000000100010000000011100000000000000000000000000000'
    s4 = '000000000000000000000000000100100000000100100000000100100000000' \
         '100100000000111111000000000100000000000100000000000100000000000000000000000000000'
    s3 = '000000000000000011100000000100010000000000010000000000010000000011' \
         '100000000000010000000000010000000100010000000011100000000000000000000000000000'
    s2 = '000000000000000001100000000010010000000000010000000000010000000001' \
         '100000000010000000000010000000000010000000000011110000000000000000000000000000'
    s1 = '000000000000000000100000000001100000000010100000000000100000000000100' \
         '000000000100000000000100000000000100000000011110000000000000000000000000000'

    c5 = np.zeros(shape=(12, 12), dtype=int)
    c4 = np.zeros(shape=(12, 12), dtype=int)
    c3 = np.zeros(shape=(12, 12), dtype=int)
    c2 = np.zeros(shape=(12, 12), dtype=int)
    c1 = np.zeros(shape=(12, 12), dtype=int)

    for i in range(12):
        for j in range(12):
            c5[j, i] = int(s5[12*i + j])
            c4[j, i] = int(s4[12*i + j])
            c3[j, i] = int(s3[12*i + j])
            c2[j, i] = int(s2[12*i + j])
            c1[j, i] = int(s1[12*i + j])

    for i in reversed(range(8)):
        cube[:, :, :] = 0
        cube[:, :, i] = c5
        cube_countdown[7-i, :, :, :] = cube
    for i in reversed(range(8)):
        cube[:, :, :] = 0
        cube[:, :, i] = c4
        cube_countdown[14-i, :, :, :] = cube
    for i in reversed(range(8)):
        cube[:, :, :] = 0
        cube[:, :, i] = c3
        cube_countdown[21-i, :, :, :] = cube
    for i in reversed(range(8)):
        cube[:, :, :] = 0
        cube[:, :, i] = c2
        cube_countdown[28-i, :, :, :] = cube
    for i in reversed(range(8)):
        cube[:, :, :] = 0
        cube[:, :, i] = c1
        cube_countdown[35-i, :, :, :] = cube

def cube_bounce():
    file = open(r'C:\Users\karth\OneDrive\Desktop\cube_bouncing.txt', 'r')
    s = file.readlines()
    for i in range(40):
        s[i] = s[i].rstrip()
    for i in range(40):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_bouncing[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    file.close()

def stack():
    for j in range(12):
        cube[:, 11-j, :] = 1
        for i in range(12):
            cube[:, :, 0:12-j] = 0
            cube[:, i, :] = 1
            cube[i, :, :, :] = cube

def ending():
    file = open(r'C:\Users\karth\OneDrive\Desktop\ending.txt', 'r')
    s = file.readlines()
    for i in range(7):
        s[i] = s[i].rstrip()

    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[7+i, x, y, z] = int(s[6-i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[14+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[21+i, x, y, z] = int(s[6-i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[28+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[35+i, x, y, z] = int(s[6-i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[42+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[49+i, x, y, z] = int(s[6-i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[56+i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    for i in range(7):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ending[63+i, x, y, z] = int(s[6-i][12 * 12 * z + 12 * y + x])
    file.close()


def loading():
    file = open(r'C:\Users\karth\OneDrive\Desktop\loading.txt', 'r')
    s = file.readlines()
    for i in range(12):
        s[i] = s[i].rstrip()
    for i in range(12):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_loading[i, x, y, z] = int(s[i][12*12*z + 12*y + x])
    file.close()


def crab():
    file = open(r'C:\Users\karth\OneDrive\Desktop\crab.txt', 'r')
    s = file.readlines()
    for i in range(14):
        s[i] = s[i].rstrip()
    for i in range(14):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_crab[i, x, y, z] = int(s[i][12*12*z + 12*y + x])
    file.close()


def indicator():
    file = open(r'C:\Users\karth\OneDrive\Desktop\indicator.txt', 'r')
    s = file.readlines()
    for i in range(13):
        s[i] = s[i].rstrip()
    for i in range(13):
        for x in range(12):
            for y in range(12):
                for z in range(8):
                    cube_ind[i, x, y, z] = int(s[i][12 * 12 * z + 12 * y + x])
    file.close()

'''Calling all the functions to generate the data for the animations.'''
xz()
xy()
yz()
xy_ff()
xz_ff()
yz_ff()
rainfall()
xzboing()
xyboing()
yzboing()
shrink_grow()
woop_woop()
shuffle_plane()
arrow()
edgefill()
helix()
sine()
socure()
snake()
crab()
socure_letters()
heart()
pacman()
pokeball()
dice()
countdown()
cube_bounce()
ending()
loading()
running_man()
gangnam()
indicator()

''' Conversion of the 3D image data into hex data'''

header = ['010', '020', '040', '080', '100', '200', '400', '800', '001', '002', '004', '008']
# This array contains the headers (in hexadecimal format) which need to be added at the beginning
# of each line. Each line has 27 nibbles (1 nibble = 1 hexadecimal digit), the first 3 nibbles is
# the header, the remaining 24 are the anode data.

''' The following for loops read the matrices frame by frame and convert the binary data into 
hex and then store it in the corresponding string'''

for k in range(12):
    for a in range(10): # repeating each frame 10 times
        for q in range(12):
            strxy += header[q] # adding the header in the beginning
            strxz += header[q]
            for p in range(12):
                # str1 and str2 are dummy variables used to store anode data in one layer
                # syntax for joining elements from a 1D array into a string
                str1 = ''.join(str(e) for e in cube_xy[k, p, q, :])
                str2 = ''.join(str(e) for e in cube_xz[k, p, q, :])
                strxy += "{0:0>2X}".format(int(str1, 2)) # syntax for converting binary string to hex
                strxz += "{0:0>2X}".format(int(str2, 2))
            strxy += '\n'
            strxz += '\n'

for k in range(8):
    for a in range(10):
        for q in range(12):
            stryz += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_yz[k, p, q, :])
                stryz += "{0:0>2X}".format(int(str1, 2))

            stryz += '\n'

for k in range(24):
    for a in range(10):
        for q in range(12):
            strxyff += header[q]
            strxzff += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_xy_ff[k, p, q, :])
                str2 = ''.join(str(e) for e in cube_xz_ff[k, p, q, :])
                strxyff += "{0:0>2X}".format(int(str1, 2))
                strxzff += "{0:0>2X}".format(int(str2, 2))

            strxyff += '\n'
            strxzff += '\n'

for k in range(16):
    for a in range(10):
        for q in range(12):
            stryzff += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_yz_ff[k, p, q, :])
                stryzff += "{0:0>2X}".format(int(str1, 2))

            stryzff += '\n'

for k in range(24):
    for a in range(10):
        for q in range(12):
            strxyboing += header[q]
            strxzboing += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_xyboing[k, p, q, :])
                str2 = ''.join(str(e) for e in cube_xzboing[k, p, q, :])
                strxyboing += "{0:0>2X}".format(int(str1, 2))
                strxzboing += "{0:0>2X}".format(int(str2, 2))

            strxyboing += '\n'
            strxzboing += '\n'

for k in range(16):
    for a in range(10):
        for q in range(12):
            stryzboing += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_yzboing[k, p, q, :])
                stryzboing += "{0:0>2X}".format(int(str1, 2))

            stryzboing += '\n'

for k in range(40):
    for a in range(10):
        for q in range(12):
            str_rain += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_rainfall[k, p, q, :])
                str_rain += "{0:0>2X}".format(int(str1, 2))

            str_rain += '\n'

for k in range(64):
    for a in range(8):
        for q in range(12):
            strshrink += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_shrink_grow[k, p, q, :])
                strshrink += "{0:0>2X}".format(int(str1, 2))
            strshrink += '\n'

for times in range(2): # repeating the whole animation 2 times
    for k in range(10):
        for a in range(10):
            for q in range(12):
                strwoop += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_woop[k, p, q, :])
                    strwoop += "{0:0>2X}".format(int(str1, 2))
                strwoop += '\n'

for times in range(1):
    for k in range(48):
        for a in range(10):
            for q in range(12):
                strshuffle += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_shuffle[k, p, q, :])
                    strshuffle += "{0:0>2X}".format(int(str1, 2))
                strshuffle += '\n'

for k in range(40):
    for a in range(10):
        for q in range(12):
            strarrow += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_arrow[k, p, q, :])
                strarrow += "{0:0>2X}".format(int(str1, 2))
            strarrow += '\n'

for k in range(36):
    for a in range(10):
        for q in range(12):
            stredgefill += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_edgefill[k, p, q, :])
                stredgefill += "{0:0>2X}".format(int(str1, 2))
            stredgefill += '\n'

for times in range(2): # repeating the whole animation twice
    for k in range(50):
        for a in range(10):
            for q in range(12):
                strhelix += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_helix[k, p, q, :])
                    strhelix += "{0:0>2X}".format(int(str1, 2))
                strhelix += '\n'

for times in range(6): # repeating the whole animation 6 times
    for k in range(12):
        for a in range(10):
            for q in range(12):
                strsine += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_sine[k, p, q, :])
                    strsine += "{0:0>2X}".format(int(str1, 2))
                strsine += '\n'

for k in range(12):
    for a in range(40):
        for q in range(12):
            strsocure += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_socure[k, p, q, :])
                strsocure += "{0:0>2X}".format(int(str1, 2))
            strsocure += '\n'

for k in range(54):
    for a in range(10):
        for q in range(12):
            strsocureletters += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_socureletters[k, p, q, :])
                strsocureletters += "{0:0>2X}".format(int(str1, 2))
            strsocureletters += '\n'

for times in range(6): # repeating the whole animation 6 times
    for k in range(10):
        for a in range(10):
            for q in range(12):
                strheart += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_heart[k, p, q, :])
                    strheart += "{0:0>2X}".format(int(str1, 2))

                strheart += '\n'

for k in range(56):
    for a in range(20):
        for q in range(12):
            strpac += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_pac[k, p, q, :])
                strpac += "{0:0>2X}".format(int(str1, 2))

            strpac += '\n'

for k in range(15):
    for a in range(21):
        for q in range(12):
            strpokeball += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_pokeball[k, p, q, :])
                strpokeball += "{0:0>2X}".format(int(str1, 2))
            strpokeball += '\n'

for k in range(62):
    for a in range(12):
        for q in range(12):
            strsnake += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_snake[k, p, q, :])
                strsnake += "{0:0>2X}".format(int(str1, 2))
            strsnake += '\n'

for k in range(20):
    for a in range(10):
        for q in range(12):
            strdice += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_dice[k, p, q, :])
                strdice += "{0:0>2X}".format(int(str1, 2))
            strdice += '\n'

for k in range(40):
    for a in range(10):
        for q in range(12):
            strcountdown += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_countdown[k, p, q, :])
                strcountdown += "{0:0>2X}".format(int(str1, 2))
            strcountdown += '\n'

for k in range(40):
    for a in range(10):
        for q in range(12):
            strbounce += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_bouncing[k, p, q, :])
                strbounce += "{0:0>2X}".format(int(str1, 2))

            strbounce += '\n'
f = 0
for k in range(70):
    if k in range(14): # This is done to make the animation to run faster after every 14 frames
        f = 10
    elif k in range(14, 28):
        f = 8
    elif k in range(28, 42):
        f = 7
    elif k in range(42, 56):
        f = 6
    elif k in range(56, 70):
        f = 4
    for a in range(f):
        for q in range(12):
            strending += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_ending[k, p, q, :])
                strending += "{0:0>2X}".format(int(str1, 2))
            strending += '\n'

for k in range(15):
    for a in range(25):
        for q in range(12):
            strloading += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_loading[k, p, q, :])
                strloading += "{0:0>2X}".format(int(str1, 2))
            strloading += '\n'

for k in range(14):
    for a in range(20):
        for q in range(12):
            strcrab += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_crab[k, p, q, :])
                strcrab += "{0:0>2X}".format(int(str1, 2))
            strcrab += '\n'

for times in range(4): # repeating the whole animation 4 times
    for k in range(17):
        for a in range(15):
            for q in range(12):
                strgangnam += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_gangnam[k, p, q, :])
                    strgangnam += "{0:0>2X}".format(int(str1, 2))

                strgangnam += '\n'

for times in range(2): # repeating the whole animation twice
    for k in range(12):
        for a in range(20):
            for q in range(12):
                strrunning += header[q]
                for p in range(12):
                    str1 = ''.join(str(e) for e in cube_running[k, p, q, :])
                    strrunning += "{0:0>2X}".format(int(str1, 2))

                strrunning += '\n'

for k in range(13):
    for a in range(25):
        for q in range(12):
            str_ind += header[q]
            for p in range(12):
                str1 = ''.join(str(e) for e in cube_ind[k, p, q, :])
                str_ind += "{0:0>2X}".format(int(str1, 2))
            str_ind += '\n'

'''Opening text file in write mode and writing the strings in order'''

f = open(r"C:\Users\karth\Documents\textfile.txt", "w")
f.writelines([str_ind, strloading, strcountdown, strxyboing,
              strxzboing, stryzboing, strshuffle, stredgefill, strtaki, str_rain, strshrink, strwoop,
              strhelix, strsine, strheart, strpac, strpokeball, strrunning, strgangnam, strsnake, strbounce, strcrab,
              strending, strsocure])

f.close()
