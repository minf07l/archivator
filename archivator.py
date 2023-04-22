from tkinter import Tk
from tkinter.filedialog import askopenfilename
import ctypes
import sys
import struct
from ctypes import c_int32


def file_pack_rle_1(filename, filetype):
    with open(filename, 'rb') as file:
        data = file.read(1)
        s = ""
        while (data):
            x = struct.unpack('<b', data)
            y = x[0] + 128
            s += (str(bin(y))[2:])
            data = file.read(1)

        a = [5, 7, 4, 1]
        if (s[0] == "1"):
            a += [1]
        else:
            a += [0]
        ind = 1
        c = 1
        while(ind < len(s)):
            if (s[ind] != s[ind - 1]):
                a += [c]
                c = 1
            else:
                c += 1
            ind += 1
        a += [c]
        length = 0
        with open("rle_1_save.dat", 'wb') as file_1:
            for item in a:
                d = struct.pack('<b', item)
                file_1.write(d)
                length += 1

        return length



def file_unpack_rle_1(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)
        x = struct.unpack('<i', data)
        y = x[0]
        if (y == 1196314761):
            ff111 = "rle_1.png"
        elif (y == 70468681):
            ff111 = "rle_1.mp3"
        else:
            ff111 = "rle_1.txt"

        with open(ff111, "wb") as ff11:
            data = file.read(1)
            x = struct.unpack('<b', data)
            adding = x[0]
            data = file.read(1)
            s = ""
            while (data):
                x = struct.unpack('<b', data)
                y = x[0]
                s += str(adding) * y
                adding = (adding + 1) % 2
                data = file.read(1)


            for i in range (len(s) // 8):
                s1 = s[8 * i : 8 * (i + 1)]
                int_file = int(s1, 2)
                int_file = int_file - 128
                d = struct.pack('<b', int_file)
                ff11.write(d)



def file_pack_rle_2(filename, filetype):
    with open(filename, 'rb') as file:
        data = file.read(1)
        a = [4, 1, 1, 2]
        x = struct.unpack('<b', data)
        y_prev = x[0]
        c = 1
        data = file.read(1)
        while (data):
            x = struct.unpack('<b', data)
            y = x[0]
            if (y == y_prev):
                c += 1
            else:
                a += [c]
                c = 1
                a += [y_prev]
                y_prev = y * 1
            data = file.read(1)
        a += [c]
        a += [y_prev]
        length = 0
        with open("rle_2_save.dat", 'wb') as file_1:
            for i in range(len(a)):
                xx = a[i] * 1
                while (xx > 127):
                    d = struct.pack('<b', 127)
                    file_1.write(d)
                    d = struct.pack('<b', a[i + 1])
                    file_1.write(d)
                    xx -= 127
                    length += 2

                d = struct.pack('<b', xx)
                file_1.write(d)
                length += 1

        return length




def file_unpack_rle_2(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)
        x = struct.unpack('<i', data)
        y = x[0]
        if (y == 1196314761):
            fone = "rle_2.png"
        elif (y == 70468681):
            fone = "rle_2.mp3"
        else:
            fone = "rle_2.txt"

        with open(fone, "wb") as f_to:
            data = file.read(1)
            data1 = file.read(1)
            while (data1):
                x1 = struct.unpack('<b', data)
                y1 = x1[0]
                x2 = struct.unpack('<b', data1)
                y2 = x2[0]
                for i in range(y1):
                    d = struct.pack('<b', y2)
                    f_to.write(d)

                data = file.read(1)
                data1 = file.read(1)



def file_pack_rle_3(filename, filetype):
    with open(filename, 'rb') as file:
        data = file.read(1)


def file_unpack_rle_3(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)


def file_pack_huffman(filename, filetype):
    with open(filename, 'rb') as file:
        data = file.read(1)


def file_unpack_huffman(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)


Tk().withdraw()
filename = askopenfilename()

with open(filename, 'rb') as file:
    data = file.read(4)
    x = struct.unpack('<i', data)
    y = x[0]
    if (y == 1196314761):
        #print("PNG")
        x1 = file_pack_rle_1(filename, "png")
        x2 = file_pack_rle_2(filename, "png")
        x3 = file_pack_rle_3(filename, "png")
        x4 = file_pack_huffman(filename, "png")
        print("The output files are:")
        print("After RLE-1 - rle_1_save.dat and its length is " + str(x1) + " bytes")
        print("After RLE-2 - rle_2_save.dat and its length is " + str(x2) + " bytes")
        print("After RLE-3 - rle_3_save.dat and its length is " + str(x3) + " bytes")
        print("After Huffman Algorithm - huffman_save.dat and its length is " + str(x4) + " bytes")
    elif (y == 70468681):
        #print("MP3")
        x1 = file_pack_rle_1(filename, "mp3")
        x2 = file_pack_rle_2(filename, "mp3")
        x3 = file_pack_rle_3(filename, "mp3")
        x4 = file_pack_huffman(filename, "mp3")
        print("The output files are:")
        print("After RLE-1 - rle_1_save.dat and its length is " + str(x1) + " bytes")
        print("After RLE-2 - rle_2_save.dat and its length is " + str(x2) + " bytes")
        print("After RLE-3 - rle_3_save.dat and its length is " + str(x3) + " bytes")
        print("After Huffman Algorithm - huffman_save.dat and its length is " + str(x4) + " bytes")
    elif (y == 17041157):
        #print("UNPACK_rle_1")
        file_unpack_rle_1(filename)
        print("The output file is in the file: rle_1.X")
        print("X - is the filetype that you have submitted before")
    elif (y == 33620228):
        #print("UNPACK_rle_2")
        file_unpack_rle_2(filename)
        print("The output file is in the file: rle_2.X")
        print("X - is the filetype that you have submitted before")
    else:
        #print("TXT")
        x1 = file_pack_rle_1(filename, "txt")
        x2 = file_pack_rle_2(filename, "txt")
        #x3 = file_pack_rle_3(filename, "txt")
        #x4 = file_pack_huffman(filename, "txt")
        with open (filename, 'rb') as fff:
            data11 = fff.read(1)
            cc = 0
            while(data11):
                cc += 1
                data11 = fff.read(1)

        print("The size of you file is " + str(cc) + " bytes")
        print()
        print("The output files are:")
        print("After RLE-1 - rle_1_save.dat and its length is " + str(x1) + " bytes")
        print("After RLE-2 - rle_2_save.dat and its length is " + str(x2) + " bytes")
        #print("After RLE-3 - rle_3_save.dat and its length is " + str(x3) + " bytes")
        #print("After Huffman Algorithm - huffman_save.dat and its length is " + str(x4) + " bytes")