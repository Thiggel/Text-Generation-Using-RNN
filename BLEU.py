from nltk.translate.bleu_score import sentence_bleu

if __name__ == '__main__':
    filename = 'NN_LN_text.txt'
    latex = open(filename, 'rb').read().decode(encoding='utf-8')

    filename2 = 'output.txt'
    gen = open(filename2, 'rb').read().decode(encoding='utf-8')

    sentences = latex.split(".")
    corpus = []
    for i in range(len(sentences)):
        corpus.append(sentences[i].split(" "))

    sentences = gen.split(".")
    candidate = []
    for i in range(len(sentences)):
        candidate.append(sentences[i].split(" "))

    corpus = corpus[0:len(candidate)]

    sum_score = []
    for i in range(len(corpus)):
        score = sentence_bleu(corpus, candidate[i])
        sum_score.append(score)

    print(sum(sum_score)/len(sum_score))