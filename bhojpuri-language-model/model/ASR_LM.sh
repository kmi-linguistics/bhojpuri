#!/bin/bash

# LM estimation starts with the collection of n-grams and their frequency counters. Then, 
# smoothing parameters are estimated for each n-gram level; infrequent n-grams are
# possibly pruned and, finally, a LM file is created containing n-grams with probabilities and 
# back-off weights.

basepath=`pwd`

# The environment variable {IRSTLM} is correctly set to {/path/to/install/irstlm}, and that environment variable {PATH} includes the command directory {/path/to/install/bin}
export IRSTLM=$basepath/model/irstlm
export PATH=${PATH}:${IRSTLM}/bin

# In order to estimate a Language Model, you first need to prepare your training corpus (as bhojpuriSentences.txt) here in sentences directory. The corpus just consists of a text.
# We assume that the text is already preprocessed according to the user needs; this means that lowercasing, uppercasing, tokenization, and any other text transformation has to be performed beforehand with other tools.


# n in n-gram
n_gram=5

echo ============================================================================
echo "                   Creating  n-gram LM               	        "
echo ============================================================================

# remove and make directory if already exist
rm -rf $basepath/model/n_gram_lm
mkdir $basepath/model/n_gram_lm

# The following script adds start and end symbols (<s> and </s>, respectively) to all lines in your training corpus.
# {IRSTLM} assumes that each line corresponds to a sentence, regardless the presence of punctuation inside or at the end of the line.
# {Start and end symbols (<s> and </s>) should be considered reserved symbols, and used only as sentence boundaries.
cat $basepath/sentences/bhojpuriSentences.txt | add-start-end.sh > $basepath/model/n_gram_lm/bhojpuriSentences.txt.se

# The script to generate the LM
$basepath/model/irstlm/bin/build-lm.sh -i $basepath/model/n_gram_lm/bhojpuriSentences.txt.se -n $n_gram -o $basepath/model/n_gram_lm/bhojpuriSentences.ilm.gz

# Notice that {build-lm.sh} produces a LM file {bhojpuriSentences.ilm.gz} that is NOT in the final ARPA format, but in
# an intermediate format called {iARPA}, that is recognized by the {compile-lm} 

# To convert the file into the standard ARPA format you can use the command
$basepath/model/irstlm/bin/compile-lm $basepath/model/n_gram_lm/bhojpuriSentences.ilm.gz $basepath/model/n_gram_lm/bhojpuriSentences.lm --text=yes


