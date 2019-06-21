from profanity_check import predict

def sentence_check(sentence):
    # predict the sentence using the pretrained model
    sentence_p_cat = predict([sentence])
    return sentence, sentence_p_cat
