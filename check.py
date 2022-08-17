import pickle
from janome.tokenizer import Tokenizer

t = Tokenizer()

with open('data-in_out/input.pickle',mode='rb') as f,\
    open('data-in_out/output.pickle',mode='rb') as o_f:
    ss_in_word = pickle.load(f)
    ss_out_word = pickle.load(o_f)


def write(file,name):
        with open('data-in_out/'+name+'.txt',mode='w')as f:
            for word in file:
                word.append('\n')
                f.writelines(t.tokenize(word,wakati=True))

write(ss_in_word,name='input')
print('IN Clear')
write(ss_out_word,name='output')
print('OUT Clear')
