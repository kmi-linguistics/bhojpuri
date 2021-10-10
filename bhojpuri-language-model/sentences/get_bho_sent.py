'''
    Script to create sentences file after preprocessing.
'''

import re

def get_bho_sent(readfilepath):
    '''
        INPUT:
            readfilepath: file path to corpus
        OUTPUT:
            sentences: List of sentences
    '''

    with open(readfilepath, 'r') as readfile:
        sentences = []
        for line in readfile:
            
            if ('vardial2018' in readfilepath):
                # for vardial2018
                if ('BHO' in line):
                    # print(line)
                    sentences.append(line.strip())
            
            elif ('UD_Bhojpuri-BHTB' in readfilepath):
                # for UD_Bhojpuri-BHTB
                if ('text' in line):
                    # print(line)
                    sentences.append(line.strip())
            
            elif ('loresmt-2020' in readfilepath or 'bho-resources' in readfilepath):
            # for loresmt-2020 and bho-resources
                sentences.append(line.strip())

    return list(set(sentences))


readfilepath = ['corpora/bho-resources/mono-bho-corpus/monolingual-v0.2.bho',\
                'corpora/bho-resources/mono-bho-corpus/monolingual.bho',\
                'corpora/loresmt-2020/dev/dev.bho',\
                'corpora/loresmt-2020/monolingual/mono.loresmt-2020.bho',\
                'corpora/loresmt-2020/bho2hi.test.bho',\
                'corpora/loresmt-2020/hi2bho.test.bho',\
                'corpora/vardial2018/dataset/dev.txt',\
                'corpora/vardial2018/dataset/gold.txt',\
                'corpora/vardial2018/dataset/train.txt',\
                'corpora/UD_Bhojpuri-BHTB/bho_bhtb-ud-test.conllu']

writefilepath = 'sentences/bhojpuriSentences.txt'
pattern = r'[=।’,/;:<>!@#$%&*\[\]_³\.\?\(\)‘0-9…”“a-zA-Z-\"\'=|°′″”–१२३४५६७८९०دبي男性連帶Сталин°′“॰é−ø″”–#+הסלעΜεγασθένηςберезень微信əˈʌəΖωροάτρالصخرة華碩電腦股份有限公司a-zA-z0-9بر*👉☸️👈—ōē……ː।’,/;:<>!@#$%&*\[\]_³\.\?\(\)‘0-9…”“a-zA-Z-\"\'१२३४५६७८९०دبي男性連帶Сталин°′“॰é−ø″”–#+=הסלעΜεγασθένηςберезень微信əˈʌəΖωροάτρالصخرة華碩電腦股份有限公司a-zA-z0-9بر*👉☸️👈—ōē……]'
sentences = []
for filepath in readfilepath:
    print(f'Working on file: {filepath}')
    sentences.append(get_bho_sent(filepath))

# flatten list of list
sentences = [sent for sublist in sentences for sent in sublist]

with open(writefilepath, 'w') as writefile:
    print(f'Writing sentences(one sentence each line) to: {writefilepath}')
    for sentence in set(sentences):
        sentence = re.sub(pattern, '', sentence)
        # write if sentence has atleast two words
        if (len(sentence.strip().split()) > 1):
            writefile.write(f'{sentence.strip()}\n')