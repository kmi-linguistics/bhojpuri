# Bhojpuri n-gram language model(LM) created using [IRSTLM Toolkit](https://github.com/irstlm-team/irstlm "IRSTLM Toolkit")

### Data Sources
- [monolingual-v0.2.bho](https://github.com/shashwatup9k/bho-resources/blob/master/mono-bho-corpus/monolingual-v0.2.bho)
- [monolingual.bho](https://github.com/shashwatup9k/bho-resources/blob/master/mono-bho-corpus/monolingual.bho)
- [dev.bho](https://github.com/panlingua/loresmt-2020/blob/main/dev/dev.bho)
- [mono.loresmt-2020.bho](https://github.com/panlingua/loresmt-2020/blob/main/monolingual/mono.loresmt-2020.bho)
- [bho2hi.test.bho](https://github.com/panlingua/loresmt-2020/blob/main/bho2hi.test.bho)
- [hi2bho.test.bho](https://github.com/panlingua/loresmt-2020/blob/main/hi2bho.test.bho)
- [dev.txt](https://github.com/kmi-linguistics/vardial2018/blob/master/dataset/dev.txt)
- [gold.txt](https://github.com/kmi-linguistics/vardial2018/blob/master/dataset/gold.txt)
- [train.txt](https://github.com/kmi-linguistics/vardial2018/blob/master/dataset/train.txt)
- [bho_bhtb-ud-test.conllu](https://github.com/UniversalDependencies/UD_Bhojpuri-BHTB/blob/master/bho_bhtb-ud-test.conllu)

### model folder contains:
- irstlm toolkit (install irstlm in this folder)
- n_gram_LM (the created LM)
- ASR_LM.sh (the script to create LM)

### sentences folder contains:
- bhojpuriSentences.txt (the corpus use to create LM)
- get_bho_sent.py (Script to create sentences file after preprocessing.)

### To create LM run following script:
```
$> ./model/ASR_LM.sh
```
**NOTE:** This repo has 5-gram LM for bhojpuri. You can change the n in n-gram in ASR_LM.sh file.
