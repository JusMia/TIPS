import pickle
import numpy as np
import scipy.stats as stats
import scipy
import pandas as pd




def zwroc_n_najlepszych(index, ile_bierzemy, image_features_0):
    #print(image_features_0.shape)
    index_start = index * 24996
    index_stop = (index + 1) * 24996

    image_features_0.columns = ["cos_sim_help"]
    image_features_0 = image_features_0.iloc[index_start:index_stop]

    ind_diff = np.min(image_features_0.index)

    image_features_0 = image_features_0.sort_values(by=['cos_sim_help'], ascending=False)
    cos_sim_np = image_features_0["cos_sim_help"].to_numpy()[0:ile_bierzemy]
    #image_index_np = np.asarray(image_features_0.index[0:ile_bierzemy]).astype(int) - index_start
    image_index_np = np.asarray(image_features_0.index[0:ile_bierzemy]).astype(int) - ind_diff
    return [cos_sim_np, image_index_np]


#długość cześci wspólnej
#po jakim czasie przestaje się zmieniać proponowane zdjęcie
#punktacja najważniejszego zdjęcia



def znajdz_najlepsze(all_lists):
    l_union = set()
    l_intersect = set(all_lists[0][1])
    for lll in all_lists:
        l_union = l_union.union(lll[1])
        l_intersect = l_intersect.intersection(lll[1])
    l_union = list(l_union)
    l_scores = np.zeros(len(l_union))

    for my_id in range(len(l_union)):
        el1 = l_union[my_id]
        for lll in all_lists:
            pos_res = np.where(lll[1] == el1)
            if pos_res[0].shape[0] > 0:
                l_scores[my_id] = l_scores[my_id] + lll[0][pos_res[0][0]]

    max_scores = np.max(l_scores)
    max_scores_index = np.where(l_scores == max_scores)[0][0]
    return [l_scores, l_union, l_intersect, max_scores, max_scores_index]

text_index = 157#131
ile_bierzemy = 20

from statistics import mean, stdev
#ile_b = [1, 2]#, 5, 10, 15, 20, 25, 30]
ile_b = [105,106]
"""liczenie statystyki tych samych
lista_procentu_tych_samych = []
for a in range(100):
    print(a)
    union_len_all = []
    max_score_all = []
    img_index_all = []
    l_intersect_all = []
    for ile_bierzemy in [a+1,a+2]:
        union_len = []
        max_score = []
        img_index = []
        l_intersect = []
        for text_index in range(200):
            #print(text_index)
            ViT_B32 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0ViT_B32)
            ViT_B16 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0ViT_B16)
            RN101 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0RN101)
            RN50 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0RN50)
            RN50x4 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0RN50x4)

            all_lists = [ViT_B32, ViT_B16, RN101, RN50x4, RN50]
            [l_scores, l_union, l_int, max_scores, max_scores_index] = znajdz_najlepsze(all_lists)
            union_len.append(len(l_union))
            max_score.append(max_scores)
            img_index.append(max_scores_index)
            l_intersect_all.append(l_int)

        union_len_all.append(union_len)
        max_score_all.append(max_score)
        img_index_all.append(img_index)


    ile_takich_samych = 0
    for a in range(len(img_index_all[0])):
        if img_index_all[0][a] == img_index_all[1][a]:
            ile_takich_samych = ile_takich_samych + 1
    print(ile_takich_samych / len(img_index_all[0]))
    lista_procentu_tych_samych.append(ile_takich_samych / len(img_index_all[0]))

import csv
with open('lista_procentu_tych_samych.txt', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(lista_procentu_tych_samych)

"""


fn_help = ["200", "400", "600", "800", "1000", "1200", "1400", "1600", "1800", "2000", "2200"]
#liczenie statystyki tych samych
lista_procentu_tych_samych = []
for a in range(100):
    #print(a)
    union_len_all = []
    max_score_all = []
    img_index_all = []
    l_intersect_all = []

    for ile_bierzemy in [a + 1, a + 2]:
        union_len = []
        max_score = []
        img_index = []
        l_intersect = []

        for my_part in fn_help:
            #print(my_part)

            image_features_0ViT_B32 = pd.DataFrame(
                pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_VITB32.pkl", "rb")))
            image_features_0ViT_B16 = pd.DataFrame(
                pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_VITB16.pkl", "rb")))
            image_features_0RN101 = pd.DataFrame(
                pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_RN101.pkl", "rb")))
            image_features_0RN50 = pd.DataFrame(
                pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_RN50.pkl", "rb")))
            image_features_0RN50x4 = pd.DataFrame(
                pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_RN50x4.pkl", "rb")))
            # labels = pd.read_csv("d:\\dane\\image_text\\Kopia image_list_Vit32_14.09.csv", sep=";")
            iter_count = int(len(image_features_0ViT_B32.index) / 24996)


            for text_index in range(iter_count):
                #print(text_index)
                ViT_B32 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0ViT_B32)
                ViT_B16 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0ViT_B16)
                RN101 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0RN101)
                RN50 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0RN50)
                RN50x4 = zwroc_n_najlepszych(text_index, ile_bierzemy, image_features_0RN50x4)

                all_lists = [ViT_B32, ViT_B16, RN101, RN50x4, RN50]
                [l_scores, l_union, l_int, max_scores, max_scores_index] = znajdz_najlepsze(all_lists)
                union_len.append(len(l_union))
                max_score.append(max_scores)
                img_index.append(max_scores_index)
                l_intersect_all.append(l_int)


        union_len_all.append(union_len)
        max_score_all.append(max_score)
        img_index_all.append(img_index)


    ile_takich_samych = 0
    for a in range(len(img_index_all[0])):
        if img_index_all[0][a] == img_index_all[1][a]:
            ile_takich_samych = ile_takich_samych + 1
    print(ile_takich_samych / len(img_index_all[0]))
    lista_procentu_tych_samych.append(ile_takich_samych / len(img_index_all[0]))

import csv
with open('lista_procentu_tych_samych.txt', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(lista_procentu_tych_samych)
