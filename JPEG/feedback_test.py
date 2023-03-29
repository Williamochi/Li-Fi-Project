import random
import numpy as np
import matplotlib.pyplot as plt
import hamming_code
import repetition_code
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
