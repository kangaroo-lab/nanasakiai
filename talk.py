with open('data-in_out/input.txt',mode='r',encoding='utf-8')as input_f,\
    open('data-in_out/output.txt',mode='r',encoding='utf-8')as output:
    in_text = input_f.read()
    out_text = output.read()

chars = in_text + out_text + '\t'
chars_list =  sorted(list(set(list(chars))))
chars_list.append('\t')

char_indices = {}  # 文字がキーでインデックスが値
for i, char in enumerate(chars_list):
    char_indices[char] = i
indices_char = {}  # インデックスがキーで文字が値
for i, char in enumerate(chars_list):
    indices_char[i] = char

n_char = len(chars_list)  # 文字の種類の数

import numpy as np

n_char = len(chars_list)
max_length_x = 84

# 文章をone-hot表現に変換する関数
def sentence_to_vector(sentence):
    vector = np.zeros((1, max_length_x, n_char), dtype=np.bool)
    for j, char in enumerate(sentence):
        vector[0][j][char_indices[char]] = 1
    return vector


from tensorflow.keras.models import load_model

encoder_model = load_model('encoder_model.h5')
decoder_model = load_model('decoder_model.h5')

def respond(message, beta=5):
    vec = sentence_to_vector(message)  # 文字列をone-hot表現に変換
    state_value = encoder_model.predict(vec)
    y_decoder = np.zeros((1, 1, n_char))  # decoderの出力を格納する配列
    y_decoder[0][0][char_indices['\t']] = 1  # decoderの最初の入力はタブ。one-hot表現にする。

    respond_sentence = ""  # 返答の文字列
    while True:
        y, h = decoder_model.predict([y_decoder, state_value])
        p_power = y[0][0] ** beta  # 確率分布の調整
        next_index = np.random.choice(len(p_power), p=p_power/np.sum(p_power))
        next_char = indices_char[next_index]  # 次の文字

        if (next_char == "\n" or len(respond_sentence) >= max_length_x):
            break  # 次の文字が改行のとき、もしくは最大文字数を超えたときは終了

        respond_sentence += next_char
        y_decoder = np.zeros((1, 1, n_char))  # 次の時刻の入力
        y_decoder[0][0][next_index] = 1

        state_value = h  # 次の時刻の状態

    return respond_sentence

def is_invalid(message):
    is_invalid =False
    for char in message:
        if char not in chars_list:
            is_invalid = True
    return is_invalid

bot_name = "七咲"
your_name = 'けん'
print()

print(bot_name + ": " + "こんにちは、先輩!")
message = ""
while message != "おやすみ。":

    while True:
        message = input(your_name + ": ")
        if not is_invalid(message):
            break
        else:
            print(bot_name + ": ふふふ、本当におかしな人ですね")

    response = respond(message)
    print(bot_name + ": " + response)
