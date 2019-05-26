from profanity_check import predict, predict_prob

def sentence_check(sentence):
    sentence_p_lvl = predict_prob([sentence])
    sentence_p_cat = predict([sentence])
    
    return sentence, sentence_p_cat, sentence_p_lvl
