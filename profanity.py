from profanity_check import predict

def sentence_check(sentence):
    sentence_p_cat = predict([sentence])
    
    return sentence, sentence_p_cat
