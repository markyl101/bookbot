def get_word_count(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def stats(file_contents: str) -> dict:
    freq = {}
    for char in file_contents.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def dict_sort(freq):
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq