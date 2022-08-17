'''
1 : dataをリスト化
2 : dataをinputデータとアウトプットデータに分ける
3 : それぞれのデータの表現を正規化
'''

import re
import pickle

data_len = 10
text = ""

# dara をリスト化する <- 改行に合わせてデータを分割する

for i in range(data_len):
    with open("dataset/nanasaki_ss"+str(i)+".txt", mode="r", encoding="utf-8") as f:
        text_ss = f.read()


    # text_ss = re.sub("《[^》]+》", "", text_ss) # ルビの削除
    # text_ss = re.sub("［[^］]+］", "", text_ss) # 読みの注意の削除
    # text_ss = re.sub("[｜ 　「」（）\n]", "", text_ss) # | と全角半角スペース、「」と改行の削除

    separator = "\n"

    ss_list = re.split(separator, text_ss)
    ss_list = [x for x in ss_list if x!='']
    print(ss_list)

    with open('clear-dataset/nanasaki_ss'+str(i)+'.pickle', mode='wb') as f:
        pickle.dump(ss_list, f)
