from collections import Counter, defaultdict
import random
import os


class RandomTextGenerator:

    def __init__(self, file_path):
        '''Constract object with trained Markov-chain model based on trigrams'''
    
        if os.path.exists(file_path) and os.path.isfile(file_path):
            if os.path.getsize(file_path):
                with open(file_path, "r", encoding="utf-8") as corpus_file:
                    self.tokens = corpus_file.read().split()
                self.ngrams = self.generate_trigrams()
                self.freq = self.count_frequencies()
            else:
                print('Empty file')
        else:
            print('Bad file path, please, check it')

    def generate_trigrams(self):
        result = []
        for i in range(len(self.tokens) - 2):
            result.append((f'{self.tokens[i]} {self.tokens[i + 1]}', self.tokens[i + 2]))
        return result

    def count_frequencies(self):
        result = defaultdict(Counter)
        for head, tail in self.ngrams:
            result[head][tail] += 1
        return result

    def get_token_by_index(self, index_):
        return self.tokens[index_]

    def get_head_and_tail(self, index_):
        return f'Head: {self.ngrams[index_][0]}\tTail: {self.ngrams[index_][1]}'

    def print_tail_by_head(self, head):
        for key, value in self.freq[head].most_common():
            print(f'Tail:{key} \tCount:{value}')

    def generate_random_sentence(self):
        '''
            Function to generate random sentence using Markov chain.
            Constraint are:
                — always start with capitalized words ("This is beautiful.", "You are a great programmer!", etc.);
                — not start with a word that ends with a sentence-ending punctuation
                mark ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
                — always end with a sentence-ending punctuation mark like ., !, or ?;
                — should not be shorter than 5 tokens.
        '''
        
        while True:
            head = random.choice(list(self.freq.keys()))
            head_parts = head.split()
            if (head_parts[0][0].isupper()) and (head_parts[0][-1] not in ['.', '!', '?']):
                break
        sentence = [head]

        while True:
            tail = random.choices(list(self.freq[head].keys()), list(self.freq[head].values()))[0]
            sentence.append(tail)
            head_parts = head.split()
            head = f'{head_parts[-1]} {tail}'
            if len(' '.join(sentence).split()) > 4 and sentence[-1][-1] in '.?!':
                break
        print(' '.join(sentence))

        
if __name__ == '__main__':
  
  PATH = 'corpus.txt'
  try:
      rtg = RandomTextGenerator(PATH)
      for _ in range(10):
          rtg.generate_random_sentence()
  except AttributeError:
      print('Exit')
