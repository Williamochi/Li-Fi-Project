import random
import numpy as np
import matplotlib.pyplot as plt
##############encoder################
def hamming_encoding(inp_list):
    p0 = p1 = p2 = 0
    d = 0
    m2 = []
    m = inp_list
    len_of_m = len(m)
    len_of_m1 = 0
    num_zero = 0
    bin_num_zero = ''
    while len_of_m != len_of_m1:
        m1 = m[0+d:4+d]
        len_of_m1 += len(m1)
        if len(m1) != 4:
            num_zero = 4-len(m1)#回傳補0位數並記錄
            bin_num_zero = '{:b}'.format(num_zero)
            for b in range(num_zero):
                m1 += '0'
            
            m1 = ''.join(m1)
        if m1[0] == '1':
            p0 += 1
            p1 += 1
        if m1[1] == '1':
            p1 += 1
            p2 += 1
        if m1[2] == '1':
            p0 += 1
            p1 += 1
            p2 += 1
        if m1[3] == '1':
            p0 += 1
            p2 += 1

        p0_num_one = p0 % 2
        p1_num_one = p1 % 2
        p2_num_one = p2 % 2

        if p0_num_one == 0:
            m1 += '0'
        else:
            m1 += '1'
        if p1_num_one == 0:
            m1 += '0'
        else:
            m1 += '1'
        if p2_num_one == 0:
            m1 += '0'
        else:
            m1 += '1'

        m1 = ''.join(m1)
        m1 += bin_num_zero#讓decoder知道有補幾個0
        m2 += m1
        p0 = p1 = p2 = 0
        d += 4
    m2 = ''.join(m2)
    return m2
#print(m2)
#  !!要補個偵測最後少於四個的標誌能讓decoder知道!!(完成)
###############decoder#################
hamming_743code = ['0000000','0001101','0010111','0011010','0100011','0101110','0110100','0111001',
                   '1000110','1001011','1010001','1011100','1100101','1101000','1110010','1111111']
def hamming_check(inp1):
    list001 = inp1
    for ff01 in range(16):
        if list001 == hamming_743code[ff01]:
            return list001[0:4]    #取前四個
def code_change(inp, i):
    temp = list(inp)
    if temp[i] == '0':
        temp[i] = temp[i].replace('0', '1')
    else:
        temp[i] = temp[i].replace('1', '0')
    temp = ''.join(temp)
    return temp
def errorcheck(inp):
    temp = inp
    synd_code0 = int(temp[4]) + int(temp[0]) + int(temp[2]) + int(temp[3])
    synd_code1 = int(temp[5]) + int(temp[0]) + int(temp[1]) + int(temp[2])
    synd_code2 = int(temp[6]) + int(temp[1]) + int(temp[2]) + int(temp[3])
    synd_code0 = synd_code0 % 2
    synd_code1 = synd_code1 % 2
    synd_code2 = synd_code2 % 2
    if  synd_code0 == 0 and synd_code1 == 0 and synd_code2 == 0:#沒有錯
        temp = temp
    elif synd_code0 == 1 and synd_code1 == 1 and synd_code2 == 0:#第1個錯
        temp = code_change(temp, 0)
    elif synd_code0 == 0 and synd_code1 == 1 and synd_code2 == 1:#第2個錯
        temp = code_change(temp, 1)
    elif synd_code0 == 1 and synd_code1 == 1 and synd_code2 == 1:#第3個錯
        temp = code_change(temp, 2)
    elif synd_code0 == 1 and synd_code1 == 0 and synd_code2 == 1:#第4個錯
        temp = code_change(temp, 3)
    elif synd_code0 == 1 and synd_code1 == 0 and synd_code2 == 0:#第5個錯
        temp = code_change(temp, 4)
    elif synd_code0 == 0 and synd_code1 == 1 and synd_code2 == 0:#第6個錯
        temp = code_change(temp, 5)
    elif synd_code0 == 0 and synd_code1 == 0 and synd_code2 == 1:#第7個錯
        temp = code_change(temp, 6)
    return temp

# m3 = '0000011'
# TEMP00 = errorcheck(m3)
# print(TEMP00)

def hamming_decoding(inp_list):
    decode_m1 = inp_list
    decode_m2 = ['']
    now = 0
    len_m2 = 0.
    block_decode_m1 = len(decode_m1)/7
    block_decode_m2 = len_m2/4
    num_zero = 0
    while block_decode_m1 != block_decode_m2:
        TEMP00 = decode_m1[now:now+7]
        if len(TEMP00) == 7: 
            TEMP00 = errorcheck(TEMP00)
            #解不回來的if-else

            decode_m2.append(hamming_check(TEMP00))
            decode_m2 = [''.join(decode_m2)]
            
            len_m2 = len(decode_m2[0])
            block_decode_m2 = len_m2/4
            now += 7
        else:   #根據最後回傳的補0位數切掉最後最後的0
            num_zero = int(TEMP00, 2)
            decode_m2[0] = decode_m2[0][:-num_zero]
            block_decode_m1 = block_decode_m2
    return decode_m2[0]

def repeatition(inp_list):
    temp3=''
    for i in range(len(inp_list)):
        temp1 = inp_list[i]
        temp2 = temp1*3
        temp3 += temp2
    return temp3

def inv_repeatition(inp_list):
    i = 0
    zero_count = 0
    one_count = 0
    temp2 = ''
    while True:
        temp1 = inp_list[i:i+3]
        for j in range(3):
            if temp1[j]=='0':
                zero_count+=1
            else:
                one_count+=1
        if zero_count > one_count:
            temp2+='0'
        else:
            temp2+='1'
        i+=3
        if i == len(inp_list):
            break
        zero_count = 0
        one_count = 0
    return temp2
inp_list = '10101100'
inp_list2 = repeatition(inp_list)
# print(inv_repeatition(inp_list2))

#print(decode_m2)
#m = '00110100'
#print(hamming_encoding(m))
def NoiseChannel(inp_array, error):  #(要產生錯誤的陣列, 錯誤率)
    inp_array = list(inp_array)
    for i in range(len(inp_array)):
        dice = random.uniform(0, 100)
        ErrorRate = error*100 # [百分比%]
        if dice <= ErrorRate:
            if inp_array[i] == '1':
                inp_array[i] = '0'
            else:
                inp_array[i] = '1'
    output_array = ''.join(inp_array)
    return output_array

codeword = ['0000', '0001', '0010','0011', '0100', '0101', '0110', '0111', 
            '1000', '1001', '1010', '1011','1100', '1101', '1110', '1111']

def feedback_test100():
    return_count = 0
    each_scuess_count=[]
    error = np.arange(0,0.55,0.05)
    for j in range(len(error)):
        for i in range(100):
            inp_array = codeword[0]
            #hamming_input = hamming_encoding(inp_array)
            repeat_input = repeatition(inp_array)
            while True:
                # channel_output = NoiseChannel(hamming_input, error[j])
                # hamming_output = hamming_decoding(channel_output)
                channel2_output = NoiseChannel(repeat_input, error[j])
                repeat_output = inv_repeatition(channel2_output)
                #if inp_array != hamming_output:
                if inp_array != repeat_output:
                    return_count+=1
                else:
                    break
        scuess_count = return_count/100
        each_scuess_count.append(scuess_count)
        return_count = 0
    return error,each_scuess_count
def feedback_test2():
    success_count = 0
    success_rate = 0
    each_scuess_rate=[]
    fail_count = 0
    fail_rate = 0
    each_fail_rate=[]
    runtimes_count = 0
    runtimes = np.arange(1,15,1)
    error = 0.2
    for h in range(len(runtimes)):
        for i in range(100):
            inp_array = codeword[0]
            hamming_input = hamming_encoding(inp_array)
            for j in range(runtimes[h]):
                runtimes_count += 1
                channel_output = NoiseChannel(hamming_input, error)
                hamming_output = hamming_decoding(channel_output)
                if inp_array == hamming_output:
                    success_count += 1
                    break
            if inp_array != hamming_output:
                fail_count += 1
        # fail_rate = (fail_count/runtimes_count)/len(hamming_743code)
        # each_scuess_rate.append(fail_rate)
        success_rate = (fail_count)/100
        each_scuess_rate.append(success_rate)
        fail_count = 0
        success_count = 0
        runtimes_count = 0
    return runtimes,each_scuess_rate
# plt.plot(feedback_test100()[0],feedback_test100()[1])
# plt.plot(feedback_test2()[0],feedback_test2()[1])
# plt.grid(True)
# plt.xlim(0,0.5,0.05)
# plt.ylim(0,16,1)
# plt.xlabel("error probability") # x label
# plt.ylabel("ratio of resending times with each codeword") # y label
# plt.xlim(0,15)
# plt.ylim(0,1.5)
# plt.xlabel("resending times") # x label
# plt.ylabel("ratio of successful times with each codeword") # y label
# plt.show()




