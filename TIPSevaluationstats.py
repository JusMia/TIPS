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


fn_help = ["200", "400", "600", "800", "1000", "1200", "1400", "1600", "1800", "2000", "2200"]

ile_bierzemy = 31
nazwa_pliku_wynikow = "wyniki_statystyki_all_RN50"
for ile_bierzemy in range(1,101):#[1, 2, 3, 10, 20, 31, 50, 100]:
    print(ile_bierzemy)
    union_len = []
    max_score = []
    img_index = []
    l_intersect = []
    l_m12 = []
    l_m13 = []
    for my_part in fn_help:
        #print(my_part)

        image_features_0ViT_B32 = pd.DataFrame(
            pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_VITB32.pkl", "rb")))
        image_features_0ViT_B16 = pd.DataFrame(
            pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_VITB16.pkl", "rb")))
        image_features_0RN101 = pd.DataFrame(
            pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_RN101.pkl", "rb")))
        image_features_0RN50 = pd.DataFrame(pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_RN50.pkl", "rb")))
        image_features_0RN50x4 = pd.DataFrame(
            pickle.load(open("d:\\dane\\image_text\\wyniki\\text_image_match_" + my_part + "_RN50x4.pkl", "rb")))
        #labels = pd.read_csv("d:\\dane\\image_text\\Kopia image_list_Vit32_14.09.csv", sep=";")
        iter_count = int(len(image_features_0ViT_B32.index) / 24996)
        #union_len_all = []
        #max_score_all = []
        #img_index_all = []
        #l_intersect_all = []

        for ile_bierzemy_help in [ile_bierzemy]:

            for text_index in range(1, iter_count):
                #print(text_index)
                ViT_B32 = zwroc_n_najlepszych(text_index, ile_bierzemy_help, image_features_0ViT_B32)
                ViT_B16 = zwroc_n_najlepszych(text_index, ile_bierzemy_help, image_features_0ViT_B16)
                RN101 = zwroc_n_najlepszych(text_index, ile_bierzemy_help, image_features_0RN101)
                RN50 = zwroc_n_najlepszych(text_index, ile_bierzemy_help, image_features_0RN50)
                RN50x4 = zwroc_n_najlepszych(text_index, ile_bierzemy_help, image_features_0RN50x4)

                #all_lists = [ViT_B32, ViT_B16, RN101, RN50x4, RN50]
                all_lists = [RN50]
                [l_scores, l_union, l_int, max_scores, max_scores_index] = znajdz_najlepsze(all_lists)
                #print(l_int)
                union_len.append(len(l_union))
                max_score.append(max_scores)
                #img_index.append(max_scores_index)
                l_intersect.append(len(l_int))

                sort_ret = np.argsort(l_scores)

                # print(sort_ret[ile_bierzemy_help-1])

                SC1 = l_scores[sort_ret[ile_bierzemy_help - 1]]
                SC2 = 0
                if ile_bierzemy > 1:
                    SC2 = l_scores[sort_ret[ile_bierzemy_help - 2]]

                SC3 = 0
                if ile_bierzemy > 2:
                    SC3 = l_scores[sort_ret[ile_bierzemy_help - 3]]

                M12 = (SC1 - SC2) / SC1
                M13 = (SC1 - SC3) / SC1
                l_m12.append(M12)
                l_m13.append(M13)
            #union_len_all.append(union_len)
            #max_score_all.append(max_score)

            #img_index_all.append(img_index)
            #l_intersect_all.append(l_intersect)

    str_help = str(ile_bierzemy) + ";"
    str_help += str(np.mean(np.asarray(l_intersect))) + ";"
    str_help += str(np.std(np.asarray(l_intersect))) + ";"
    str_help += str(np.mean(np.asarray(union_len))) + ";"
    str_help += str(np.std(np.asarray(union_len))) + ";"
    str_help += str(np.mean(np.asarray(max_score))) + ";"
    str_help += str(np.std(np.asarray(max_score))) + ";"

    str_help += str(np.median(np.asarray(max_score))) + ";"
    str_help += str(np.max(np.asarray(max_score))) + ";"
    str_help += str(np.min(np.asarray(max_score))) + ";"

    str_help += str(np.mean(np.asarray(l_m12))) + ";"
    str_help += str(np.std(np.asarray(l_m12))) + ";"

    str_help += str(np.mean(np.asarray(l_m13))) + ";"
    str_help += str(np.std(np.asarray(l_m13))) + "\n"

    print(str_help)

    import csv
    with open(nazwa_pliku_wynikow + '.txt', 'a') as f:
        # using csv.writer method from CSV package
        #write = csv.writer(f)
        f.write(str_help)


