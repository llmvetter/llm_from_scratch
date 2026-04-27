from collections import Counter, defaultdict

#corpus = "low low low low low lower lower widest widest widest newest newest newest newest newest newest"
corpus = "abc"
def pretokenize(corpus: str) -> list[str]:
    return corpus.split(sep=" ")
pretokenized = pretokenize(corpus)
frequency = dict(Counter(pretokenized))

# convert to bytes representation
frequency: dict[tuple[bytes, ...], int] = {
    tuple(char.encode() for char in key): value for key, value in frequency.items()
}

def BPE(
        frequency_dict: dict[tuple[bytes, ...], int],
        n_merges: int,
) -> dict[tuple[bytes, ...], int]:

        def merge(frequency_dict):
            counter = defaultdict(int)
            for key, value in frequency_dict.items():
                for i in range(0, len(key)-1):
                    counter[(key[i], key[i+1])] += 1*value
            # short circuit is inefficient
            if not counter:
                return frequency_dict
            max_pair = max(counter, key=lambda k: (counter[k], k))
            out = defaultdict(int)
            for key, value in frequency_dict.items():
                new_word = []
                i = 0
                while i<len(key):
                    if key[i] == max_pair[0] and key[i+1]==max_pair[1]:
                        new_word.append(key[i]+key[i+1])
                        i+=2
                    else:
                        new_word.append(key[i])
                        i+=1
                out[tuple(new_word)] += value
            return out

        i=0
        while i < n_merges:
            frequency_dict = merge(frequency_dict)
            i+=1
        return frequency_dict

class BPEncoder:
    def __init__(self, vocab_size: int) -> None:
        self.vocab_size = vocab_size
    
    def train(
            self,
            input_path: str,
            special_tokes: list[str],
    ) -> tuple[dict[int, bytes], list[tuple[bytes, bytes]]]:
        '''
        Trains the BPEncoder Instance on a given vocab.
        Returns tuple(vocab, merges)
        '''

        assert isinstance(input_path, str), 'Input path is needed for BPE training.'

        


