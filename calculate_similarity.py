import Levenshtein


def moving_window_similarity(target_words, total_words, size):
    # target is list, total_words is a list, size is a number
    # levnshtein takes 2 strings as arguments
    total_scores = {}

    for i in range(len(total_words)):
        source_words = total_words[i:i+size]
        similarity_score = 0
        for t in target_words:
            best_score = -1
            for s in source_words:
                score = Levenshtein.seqratio(t, s)
                if score > best_score:
                    best_score = score
                    source_words.remove(s)
            similarity_score += best_score
        if similarity_score not in total_scores:
            total_scores[similarity_score] = [total_words.index(s)-size+1]
        else:
            if total_words.index(s)-size+1 not in total_scores[similarity_score]:
                total_scores[similarity_score].append(total_words.index(s)-size+1) 
    return total_scores


def main():
    total_words = ['baili', 'findachta', 'rig', 'condacht', 'codlud', 'rochotail', 'findachta', 'mac', 'tomaltaich', 'iar', 'morsæthar', 'do', 'iar', 'toraind', 'cilli', 'lais', 'i', 'loimliuch', 'ainm', 'in', 'baile', 'hisin', 'iar', 'nelud', 'do', 'a', 'righi', 'connacht', 'iar', 'mbeth', 'do', 'bliadain', 'i', 'righi', 'conacht', 'co', 'rohercad', 'grad', 'de', 'and', 'gabhais', 'a', 'brathair', 'heseam', 'i', 'murges', 'mac', 'tomaltaig', 'dia', 'fastad', 'na', 'rigi', 'eloidhseom', 'asin', 'cuimriuch', 'co', 'riacht', 'gleand', 'corath', 'hi', 'crich', 'luigne', 'braithir', 'do', 'murghius', 'he', 'co', 'rithside', 'cethirn', 'dia', 'gabail', 'eloidseom', 'uaidib', 'co', 'dubglais', 'ar', 'bru', 'echtgi', 'in', 'baili', 'i', 'teit', 'sis', 'hi', 'luchait', 'brathir', 'beus', 'he', 'dia', 'brathair', 'eloid', 'co', 'riacht', 'bru', 'sinda', 'i', 'i', 'lleith', 'annuas', 'do', 'miliuc', 'is', 'annsin', 'tanic', 'ind', 'righan', 'oc', 'dul', 'do', 'phurt', 'ind', 'rig', 'co', 'bru', 'sinna', 'aifi', 'ingen', 'oengusa', 'a', 'caisil', 'muman', 'ind', 'rigan', 'scanlan', 'fili', 'maic', 'eoghain', 'do', 'uib', 'fiachrach', 'aidhne', 'brugaid', 'bai', 'aroen', 'friu', 'i', 'tuathal', 'mac', 'concobhuir', 'ni', 'thabrad', 'biad', 'do', 'rig', 'conacht', 'uair', 'sær', 'lais', 'he', 'fen', 'is', 'annsin', 'doraladar', 'a', 'triur', 'forsin', 'nuasal', 'ina', 'dithrub', 'robraithsead', 'a', 'triur', 'he', 'do', 'rig', 'conacht', 'i', 'do', 'murges', 'conid', 'andsin', 'forfacaibseom', 'na', 'mibriatrasa', 'doib', 'i', 'comdais', 'brecairi', 'filid', 'conacht', 'a', 'nirmor', 'is', 'andsin', 'didiu', 'rothairrngir', 'donus', 'dia', 'særthachaib', 'do', 'neoch', 'na', 'biathfad', 'ri', 'connacht', 'is', 'andsin', 'forfhacaib', 'dimblad', 'fora', 'rignaib', 'ni', 'roeascain', 'clanna', 'na', 'rigna', 'uair', 'nirb', 'ail', 'dó', 'cland', 'a', 'brathar', 'descaine', 'rotairrngir', 'go', 'ngebad', 'mac', 'rigna', 'a', 'caisiul', 'ordan', 'for', 'iath', 'nerenn', 'ba', 'mor', 'tra', 'ba', 'lond', 'ba', 'lesc', 'leis', 'dul', 'asin', 'baile', 'i', 'roibi', 'arai', 'tra', 'elaid', 'otha', 'sin', 'corici', 'crich', 'hua', 'cendselaich', 'gabais', 'inad', 'iter', 'senbotha', 'abaind', 'faillsigthir', 'do', 'techt', 'co', 'formail', 'combad', 'and', 'no', 'beth', 'a', 'annoit', 'in', 'tan', 'rosiacht', 'conici', 'isand', 'robadar', 'seasca', 'aigi', 'nallaig', 'ac', 'toraind', 'inaid', 'do', 'an', 'tan', 'rosiachtsom', 'sin', 'lenaid', 'a', 'cosa', 'don', 'talmain', 'inn', 'eo', 'osa', 'chind', 'i', 'cluicin', 'i', 'mind', 'bec', 'loigis', 'in', 'cloc', 'for', 'lar', 'adnaid', 'for', 'bemnigh', 'co',
                   'tarnic', 'in', 'trath', 'do', 'beim', 'saidhigh', 'findachta', 'a', 'lorg', 'isin', 'talmain', 'genid', 'buindi', 'asin', 'talmain', 'teid', 'dar', 'in', 'cloc', 'glasais', 'he', 'conid', 'de', 'raitir', 'glassan', 'fris', 'eirgid', 'in', 'clerech', 'tornid', 'in', 'chill', 'immalle', 'frisna', 'haigib', 'dofuit', 'suan', 'trom', 'fair', 'iarna', 'thoraind', 'is', 'andsin', 'dorighne', 'seo', 'ic', 'tairrngire', 'rig', 'condacht', 'ticfa', 'didiu', 'in', 'donn', 'derg', 'furthe', 'celg', 'ticfa', 'didiu', 'in', 'seng', 'losc', 'ri', 'cen', 'cosc', 'ticfa', 'didiu', 'teni', 'thuath', 'æd', 'for', 'bruach', 'ticfa', 'didiu', 'in', 'ban', 'glas', 'duirb', 'for', 'as', 'ticfa', 'adidiua', 'in', 'ri', 'ruad', 'bron', 'fris', 'buan', 'ticfa', 'didiu', 'in', 'ri', 'flann', 'fall', 'fri', 'gall', 'ticfa', 'in', 'find', 'feigh', 'ortbas', 'cach', 'tur', 'tren', 'tend', 'sluaig', 'clith', 'na', 'crich', 'craind', 'fri', 'ais', 'damach', 'dian', 'daine', 'flann', 'bidba', 'righ', 'leis', 'tuath', 'tocbaid', 'caith', 'ort', 'ait', 'giall', 'grinni', 'gabais', 'gall', 'isein', 'tur', 'delbach', 'tor', 'in', 'find', 'eó', 'flann', 'gona', 'frisgæd', 'is', 'ni', 'gai', 'dibairt', 'ai', 'ticfa', 'didiu', 'ri', 'for', 'delgi', 'tor', 'fergi', 'ticfa', 'didiu', 'aged', 'gel', 'cridi', 'broin', 'ticfa', 'didiu', 'domnach', 'tuath', 'nis', 'degera', 'tuath', 'ticfa', 'didiu', 'ri', 'anair', 'giall', 'cach', 'lis', 'bias', 'lais', 'ticfa', 'didiu', 'ri', 'aniar', 'gaillim', 'fri', 'dil', 'ticfa', 'didiu', 'ri', 'andes', 'fianna', 'les', 'saidfid', 'cath', 'leascfaid', 'rig', 'dofæth', 'fen', 'i', 'cuid', 'rig', 'doginn', 'ticfa', 'didiu', 'ri', 'aili', 'foræ', 'darai', 'cath', 'fer', 'tren', 'ticfa', 'didiu', 'ri', 'aili', 'failbæ', 'ri', 'gaetat', 'loman', 'ticfa', 'didiu', 'in', 'find', 'dond', 'ticfa', 'didiu', 'in', 'derg', 'tend', 'tren', 'animfora', 'ucht', 'ní', 'scel', 'ticfa', 'didiu', 'dibartach', 'set', 'ac', 'diabad', 'bed', 'ticfa', 'in', 'ri', '[', ']', 'adiana', 'mian', 'fell', 'for', 'achri', 'fland', 'maigi', 'ai', 'techtfaid', 'cach', 'congal', 'frisrai', 'fingal', 'lais', 'forith', 'cloc', 'techtfaid', 'rig', 'ticfa', 'didiu', 'fer', 'aile', 'na', 'bia', 'i', 'lleth', 'de', 'acht', 'a', 'gne', 'ticfa', 'didiu', 'æd', 'ban', 'særfuiglit', 'rain', 'techtfaid', 'cath', 'basengach', 'fri', 'cach', 'in', 'uair', 'rosiacht', 'conigi', 'sin', 'lais', 'is', 'and', 'rodusced', 'he', 'ba', 'holc', 'leis', 'a', 'duscad', 'rofacaib', 'facbail', 'do', 'i', 'do', 'cholman', 'i', 'erlom', 'aili', 'in', 'tan', 'bad', 'santachu', 'leis', 'cotlud', 'comad', 'ann', 'no', 'duiscithea', 'he', 'finit', 'amen']
    target = "tarnic trath in"
    # text preprocessing on target text
    target_words = target.split()
    window_size = 3
    total_scores = moving_window_similarity(
        target_words, total_words, window_size)
    print(max(total_scores.keys()))
    print(target)
    top_k = 5
    sorted_keys = sorted(total_scores, reverse=True)
    print(total_scores[sorted_keys[0]])

    for j in range(top_k):
        k = sorted_keys[j]
        v = total_scores[k]
        for i in v:
            print(" ".join(total_words[i:i+window_size]))


if __name__ == "__main__":
    main()
