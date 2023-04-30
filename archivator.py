import tkinter as tk1
from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import ctypes
import sys
import struct
from ctypes import c_int32




def huffmann_packing(vector_like_huffman_tree, string_for_nums):
    if (len(vector_like_huffman_tree) == 1):
        return [[vector_like_huffman_tree[0], string_for_nums]]
    else:
        ind = -1
        maxx = -1
        for i in range(len(vector_like_huffman_tree)):
            if (vector_like_huffman_tree[i] == str(vector_like_huffman_tree[i])):
                numm = int(vector_like_huffman_tree[i])
                if (numm > maxx):
                    maxx = numm * 1
                    ind = i * 1
        vector_for_least_common = huffmann_packing(vector_like_huffman_tree[:ind], string_for_nums + "0")
        vector_for_more_common = huffmann_packing(vector_like_huffman_tree[ind + 1:], string_for_nums + "1")
        v_ans = vector_for_least_common + vector_for_more_common
        return v_ans



def file_pack_rle_1(filename):
    with open(filename, 'rb') as file:
        data = file.read(1)
        binary_string_from_given_file = ""
        while (data):
            extracted_arr = struct.unpack('<b', data)
            extracted_num = extracted_arr[0] + 128
            binary_string_from_given_file += (str(bin(extracted_num))[2:])
            data = file.read(1)

        array_ans = [5, 7, 4, 1]
        if (binary_string_from_given_file[0] == "1"):
            array_ans += [1]
        else:
            array_ans += [0]
        ind = 1
        count_near_bytes = 1
        while(ind < len(binary_string_from_given_file)):
            if (binary_string_from_given_file[ind] != binary_string_from_given_file[ind - 1]):
                array_ans += [count_near_bytes]
                count_near_bytes = 1
            else:
                count_near_bytes += 1
            ind += 1
        array_ans += [count_near_bytes]
        length = 0
        print(binary_string_from_given_file)
        with open("rle_1_save.huff", 'wb') as file_answer:
            for item in array_ans:
                d = struct.pack('<b', item)
                file_answer.write(d)
                length += 1

        return length



def file_unpack_rle_1(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)
        extracted_arr = struct.unpack('<i', data)
        extracted_num = extracted_arr[0]

        data = file.read(1)
        extracted_arr = struct.unpack('<b', data)
        begin_with_1_or_2 = extracted_arr[0]
        data = file.read(1)
        byte_string = ""
        while (data):
            extracted_arr = struct.unpack('<b', data)
            extracted_num = extracted_arr[0]
            byte_string += str(begin_with_1_or_2) * extracted_num
            begin_with_1_or_2 = (begin_with_1_or_2 + 1) % 2
            data = file.read(1)


        int_file_arr = []
        for i in range(len(byte_string) // 8):
            str_to_int = byte_string[8 * i: 8 * (i + 1)]
            int_file = int(str_to_int, 2)
            int_file = int_file - 128
            int_file_arr += [int_file]

        if (int_file_arr[1] == 80):
            file_output_name = "rle_1.png"
        elif (int_file_arr[1] == 68):
            file_output_name = "rle_1.mp3"
        else:
            file_output_name = "rle_1.txt"

        with open(file_output_name, "wb") as file_output:
            for i in range(len(int_file_arr)):
                d = struct.pack('<b', int_file_arr[i])
                file_output.write(d)



def file_pack_rle_2(filename):
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
        with open("rle_2_save.huff", 'wb') as file_1:
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



def file_pack_rle_3(filename):
    with open(filename, 'rb') as file:
        data = file.read(1)


def file_unpack_rle_3(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)


def file_pack_huffman(filename):
    with open(filename, 'rb') as file:
        dictionaryy = {}
        v = []
        data = file.read(1)
        while (data):
            x = struct.unpack('<b', data)
            y = x[0]
            if (y in dictionaryy):
                dictionaryy[y] += 1
            else:
                v += [[0, y]]
                dictionaryy[y] = 1
            data = file.read(1)
    for i in range(len(v)):
        v[i][0] = dictionaryy[v[i][1]]
    v.sort()
    for i in range(len(v) - 1):
        v_add = [v[0][0] + v[1][0]]
        for j in range(len(v[0]) - 1):
            v_add += [v[0][j + 1]]
        v_add += [str(i)]
        for j in range(len(v[1]) - 1):
            v_add += [v[1][j + 1]]
        v = v[2:]
        v += [v_add]
        v.sort()
    v = v[0][1:]
    v1 = huffmann_packing(v, "")
    dict1 = {}
    for i in range(len(v1)):
        dict1[v1[i][0]] = v1[i][1]
    with open(filename, 'rb') as file:
        s = ""
        data = file.read(1)
        x = struct.unpack('<b', data)
        y = x[0]
        s += dict1[y]
        data = file.read(1)
        while (data):
            x = struct.unpack('<b', data)
            y = x[0]
            s += dict1[y]
            data = file.read(1)

    leftover = len(s) % 8
    archive_vector = [44, 32, 12, 1]
    arc1 = []
    for i in range(len(v1)):
        arc1 += [v1[i][0]]
        arc1 += [len(v1[i][1])]
        for i in range((len(v1[i][1]) - 1) // 8):
            arc1 += [int(v1[i][1][8 * i : 8 * (i + 1)], 2)]
        ind1 = (len(v1[i][1]) - 1) // 8
        arc1 += [int(v1[i][1][ind1 * 8:], 2)]
    archive_vector += [leftover]
    len_add = len(arc1)
    while (len_add > 127):
        archive_vector += [127]
        len_add -= 127

    archive_vector += [len_add]

    archive_vector += [0]

    for i in range(len(v1)):
        archive_vector += [v1[i][0]]
        str_code = v1[i][1] * 1
        archive_vector += [len(str_code) - 129]
        for j in range((len(str_code) - 1) // 8):
            add_num = int(str_code[8 * j + 1: 8 * (j + 1)], 2)
            if (str_code[8 * j] == "1"):
                add_num = (-1) * (add_num + 1)
            archive_vector += [add_num]
        if (len(str_code) % 8 != 0):
            ind1 = (len(str_code) - 1) // 8
            add_num = int(str_code[8 * ind1:], 2)
            archive_vector += [add_num]
        else:
            ind1 = (len(str_code) - 1) // 8
            add_num = int(str_code[8 * ind1 + 1:], 2)
            if (str_code[8 * ind1] == "1"):
                add_num = (-1) * (add_num + 1)
            archive_vector += [add_num]

    for i in range((len(s) - 1) // 8):
        add_num = int(s[8 * i + 1: 8 * (i + 1)], 2)
        if (s[8 * i] == "1"):
            add_num = (-1) * (add_num + 1)
        archive_vector += [add_num]
    if (len(s) % 8 != 0):
        ind1 = (len(s) - 1) // 8
        archive_vector += [int(s[ind1 * 8:], 2)]
    else:
        ind1 = (len(s) - 1) // 8
        add_num = int(s[8 * ind1 + 1:], 2)
        if (s[8 * ind1] == "1"):
            add_num = (-1) * (add_num + 1)
        archive_vector += [add_num]


    with open("huffman_save.huff", 'wb') as file_1:
        for i in range(len(archive_vector)):
            d = struct.pack('<b', archive_vector[i])
            file_1.write(d)

    return len(archive_vector)




def file_unpack_huffman(filename):
    with open(filename, 'rb') as file:
        data = file.read(4)
        x = struct.unpack('<i', data)
        y = x[0]
        data = file.read(1)
        x = struct.unpack('<b', data)
        leftover = x[0]
        dict1 = {}
        data = file.read(1)
        x = struct.unpack('<b', data)
        y = x[0]
        len_add = 0
        while (y != 0):
            len_add += y
            data = file.read(1)
            x = struct.unpack('<b', data)
            y = x[0]
        amount = 0
        while (amount < len_add):
            data = file.read(1)
            amount += 1
            x = struct.unpack('<b', data)
            byte_in_int = x[0]
            data = file.read(1)
            amount += 1
            x = struct.unpack('<b', data)
            len_str = x[0] + 129
            s1 = ""
            while (len_str > 8):
                data = file.read(1)
                amount += 1
                x = struct.unpack('<b', data)
                y = x[0]
                if (y < 0):
                    s1 += "1"
                    y = (-1) * (y + 1)
                else:
                    s1 += "0"
                ss = bin(y)
                ss = ss[2:]
                while (len(ss) != 7):
                    ss = "0" + ss
                s1 += ss
                len_str -= 8
            if (len_str == 8):
                data = file.read(1)
                amount += 1
                x = struct.unpack('<b', data)
                y = x[0]
                if (y < 0):
                    s1 += "1"
                    y = (-1) * (y + 1)
                else:
                    s1 += "0"
                ss = bin(y)
                ss = ss[2:]
                while (len(ss) != 7):
                    ss = "0" + ss
                s1 += ss
            else:
                data = file.read(1)
                amount += 1
                x = struct.unpack('<b', data)
                y = x[0]
                ss = bin(y)
                ss = ss[2:]
                while (len(ss) != len_str):
                    ss = "0" + ss
                s1 += ss
            dict1[s1] = byte_in_int
        s2 = ""
        data = file.read(1)
        x = struct.unpack('<b', data)
        y = x[0]
        data1 = file.read(1)
        while (data1):
            x = struct.unpack('<b', data)
            y = x[0]
            if (y < 0):
                s2 += "1"
                y = (-1) * (y + 1)
            else:
                s2 += "0"
            sss = bin(y)
            sss = sss[2:]
            while (len(sss) != 7):
                sss = "0" + sss
            s2 += sss
            data = data1 * 1
            data1 = file.read(1)
        if (leftover == 0):
            x = struct.unpack('<b', data)
            y = x[0]
            if (y < 0):
                s2 += "1"
                y = (-1) * (y + 1)
            else:
                s2 += "0"
            sss = bin(y)
            sss = sss[2:]
            while (len(sss) != 7):
                sss = "0" + sss
            s2 += sss
        else:
            x = struct.unpack('<b', data)
            y = x[0]
            sss = bin(y)
            sss = sss[2:]
            while (len(sss) != leftover):
                sss = "0" + sss
            s2 += sss
        array_ans = []
        s_try = ""
        for i in range(len(s2)):
            s_try += s2[i]
            if (s_try in dict1):
                array_ans += [dict1[s_try]]
                s_try = ""

        with open("huffman_unpack.txt", 'wb') as file_12:
            for i in range(len(array_ans)):
                d = struct.pack('<b', array_ans[i])
                file_12.write(d)




def define_var():
    global clicks
    clicks = 0
    global signature_of_a_file
    signature_of_a_file = 0



def main1():
    button1["text"] = f"Выберите файл..."
    Tk().withdraw()
    global filename1
    filename1 = askopenfilename()



def main2():
    global signature_of_a_file
    with open(filename1, 'rb') as file:
        data = file.read(4)
        extracted_arr = struct.unpack('<i', data)
        extracted_num = extracted_arr[0]
        signature_of_a_file = extracted_num * 1
        if (extracted_num == 1196314761):
            #print("PNG")
            button1["text"] = f"Архивировать ваш png файл"
        elif (extracted_num == 70468681):
            #print("MP3")
            button1["text"] = f"Архивировать ваш mp3 файл"
        elif (extracted_num == 17041157):
            #print("UNPACK_rle_1")
            button1["text"] = f"Разархивировать ваш файл (после применения алгоритма rle-1)"
        elif (extracted_num == 33620228):
            #print("UNPACK_rle_2")
            button1["text"] = f"Разархивировать ваш файл (после применения алгоритма rle-2)"
        elif (extracted_num == 17571884):
            #print("UNPACK_huffman")
            button1["text"] = f"Разархивировать ваш файл (после применения алгоритма Хаффмана)"
        else:
            #print("TXT")
            button1["text"] = f"Архивировать ваш txt файл"





def main_main():
    global clicks
    clicks += 1
    global signature_of_a_file
    if (clicks == 1):
        main1()
        main2()
    else:
        if (signature_of_a_file == 17041157):
            file_unpack_rle_1(filename1)
            print("The output file is in the file: rle_1.X")
            print("X - is the filetype that you have submitted before")
        elif (signature_of_a_file == 33620228):
            file_unpack_rle_2(filename1)
            print("The output file is in the file: rle_2.X")
            print("X - is the filetype that you have submitted before")
        elif (signature_of_a_file == 17571884):
            file_unpack_huffman(filename1)
            print("The output file is in the file: huffman.X")
            print("X - is the filetype that you have submitted before")
        else:
            bytese_after_rle1 = file_pack_rle_1(filename1)
            bytese_after_rle2 = file_pack_rle_2(filename1)
            # bytese_after_rle3 = file_pack_rle_3(filename)
            bytese_after_huffman = file_pack_huffman(filename1)
            with open(filename1, 'rb') as file_from_user:
                data_from_user = file_from_user.read(1)
                bytes_in_user_file = 0
                while (data_from_user):
                    bytes_in_user_file += 1
                    data_from_user = file_from_user.read(1)

            print("The size of your file is " + str(bytes_in_user_file) + " bytes")
            print()
            print("The output files are:")
            print("After RLE-1 - rle_1_save.huff and its length is " + str(bytese_after_rle1) + " bytes")
            print("After RLE-2 - rle_2_save.huff and its length is " + str(bytese_after_rle2) + " bytes")
            # print("After RLE-3 - rle_3_save.dat and its length is " + str(bytes_after_rle3) + " bytes")
            print("After Huffman Algorithm - huffman_save.huff and its length is " + str(bytese_after_huffman) + " bytes")
        root.destroy()
        sys.exit()





define_var()
root = tk1.Tk()
root.geometry('700x400')
root.resizable(False, False)
root.title('Window1')


button1 = ttk.Button(root, text = "Выбрать файл для архивации или разархивации", command = main_main)
button1.pack(ipadx = 5, ipady = 5, expand = True)


root.mainloop()
