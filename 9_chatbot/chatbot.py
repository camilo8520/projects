from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

text = open("9_chatbot\dorian_gray.txt",encoding='utf-8').read().lower()

word_tokenized_text = word_sentence_tokenize(text)

single_word_tokenized_sentence = word_tokenized_text
#print(single_word_tokenized_sentence)

pos_tagged_text = []

for w in word_tokenized_text:
  pos_tagged_text.append(pos_tag(w))


single_pos_sentence = pos_tagged_text
#print(single_pos_sentence)

np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

np_chunk_parser = RegexpParser(np_chunk_grammar)

vp_chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"

vp_chunk_parser = RegexpParser(vp_chunk_grammar)

np_chunked_text = []
vp_chunked_text = []

for i in pos_tagged_text:
  np_chunked_text.append(np_chunk_parser.parse(i))
  vp_chunked_text.append(vp_chunk_parser.parse(i))

most_common_np_chunks = np_chunk_counter(np_chunked_text)
#print(most_common_np_chunks)

most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)