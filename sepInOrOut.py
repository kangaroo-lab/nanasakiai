import re
import pickle
from janome.tokenizer import Tokenizer

t = Tokenizer()

data_len = 10
input = ''
output = ''

# dara をリスト化する <- 改行に合わせてデータを分割する

for i in range(data_len):
    with open('clear-dataset/nanasaki_ss'+str(i)+'.pickle', mode="rb") as f:
        ss_word_list = pickle.load(f)

    for idx, ss_word in enumerate(ss_word_list):
        if(ss_word[0:2]=='七咲' and ss_word_list[idx-1][0:2]!='七咲'):
            input_word = ss_word_list[idx-1]
            output_word = ss_word
            input_word = re.findall("(?<=\「).+?(?=\」)",input_word)
            output_word = re.findall("(?<=\「).+?(?=\」)",output_word)
            if(len(input_word)<1 or len(output_word)<1):
                print("NONE")
            else:
                input+=input_word[0]+'\n'
                output+=output_word[0]+'\n'
                # input+=t.tokenize(input_word[0],wakati=True)
                # output+=t.tokenize(output_word[0],wakati=True
                #
print(len(input))
print(len(output))

input=t.tokenize(input,wakati=True)
output=t.tokenize(output,wakati=True)

with open('data-in_out/input.txt',mode="w") as f:
    f.writelines(input)
with open('data-in_out/output.txt',mode="w") as f:
    f.writelines(output)
