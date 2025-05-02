import Levenshtein
import sys


# removing punctuations and numbers
sym_and_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#removing stopwords


def tokenization(line):
    total_words = []
    for w in line:
        if w in sym_and_num:
            line = line.replace(w, "")
    if line.endswith('.'):
        line = line[:-1]
    line = line.lower()
    words = line.split()
    total_words += words
    return total_words

def tokenization1(line):
    total_words = []
    words = line.split()
    total_words += words
    return total_words


def moving_window_similarity1(target_words, total_words, size):

    min_score = float("inf")
    min_score_index = -1
    for i in range(len(total_words)-size+1):
        matrix = [[float("inf") for _ in range(size)] for _ in range(len(target_words))]
        source_words = total_words[i:i+size]
        for k in range(len(target_words)):
            for j in range(len(source_words)):
                score = Levenshtein.distance(target_words[k],source_words[j]) / max(len(target_words[k]), len(source_words[j]))

                matrix[k][j] = score



        # 接下来计算每个矩阵中的分数，选最小值
        score = sum(calculate_dissimilarity_score(matrix, size))
        if score < min_score:
            min_score = score
            min_score_index = i
        
        # 每个矩阵对应一个分数，保存这些分数，用字典记录 分数-索引

        # 找到最小的分数，即最匹配值，然后返回答案
    
    return min_score_index, min_score


def calculate_dissimilarity_score(matrix, window_size):

    results = []

    for _ in range(len(matrix)):
        current_min_val = float("inf")
        min_row, min_col = -1,-1
        for r in range(len(matrix)):
            for c in range(window_size):
                if matrix[r][c] < current_min_val:
                    current_min_val = matrix[r][c]
                    min_row = r
                    min_col = c
        
        if min_row == -1:
            print("所有元素被标记")
            break
        
        results.append(current_min_val)

        for c in range(len(matrix)):
            matrix[min_row][c] = float('inf')
        for r in range(window_size):
            matrix[r][min_col] = float('inf')
    return results


def main():
    
    if len(sys.argv) != 3:
        print("Usage: python script.py <search_text> <article>")
        sys.exit(1)
    article = sys.argv[2]
    query = tokenization(sys.argv[1])
    article_words = tokenization(sys.argv[2])
    original_words = tokenization1(sys.argv[2])
    window_size = len(query)
    min_score_index, min_score = moving_window_similarity1(query, article_words, window_size)
    result = " ".join(original_words[min_score_index:min_score_index+window_size])
    print(result)
            



if __name__ == "__main__":
    main()