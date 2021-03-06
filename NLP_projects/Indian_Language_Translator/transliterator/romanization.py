trans_dict = {
    # "0900" : 
    # "0901" :
    # "0902" :
    # "0903" :
    # "0904" :
    "0905" : "a",
    "0906" : "ā",
    "0907" : "i",
    "0908" : "ī",
    "0909" : "u",
    "090A" : "ū",
    "090B" : "ṛ",
    "090C" : "ḻ",
    # "090D" : 
    # "090E" :
    "090F" : "e",
    "0910" : "ai",
    # "0911" : 
    "0912" : "ŏ",
    "0913" : "o",
    "0914" : "au",
    "0915" : "ka",
    "0916" : "kha",
    "0917" : "ga",
    "0918" : "gha",
    "0919" : "ṅa",
    "091A" : "ca",
    "091B" : "cha",
    "091C" : "ja",
    "091D" : "jha",
    "091E" : "ña",
    "091F" : "ṭa",
    "0920" : "ṭha",
    "0921" : "ḍa",
    "0922" : "ḍha",
    "0923" : "ṇa",
    "0924" : "ta",
    "0925" : "tha",
    "0926" : "da",
    "0927" : "dha",
    "0928" : "na",
    # "0929" : ""
    "092A" : "pa",
    "092B" : "pha",
    "092C" : "ba",
    "092D" : "bha",
    "092E" : "ma",
    "092F" : "ya",
    "0930" : "ra",
    # "0931" : 
    "0932" : "la",
    # "0933" :
    # "0934" :
    "0935" : "va",
    "0936" : "śa",
    "0937" : "sha",
    "0938" : "sa",
    "0939" : "ha",
    # "093A" :
    # "093B" :
    # "093C" :
    # "093D" :
    "093E" : "a",
    "093F" : "i",
    "0940" : "ī",
    "0941" : "u",
    "0942" : "ū",
    "0943" : "ṛ",
    "0944" : "ṝ",
    # "0945" : "",
    # "0946" : "",
    "0947" : "e",
    "0948" : "ê",
    "0949" : "ô",
    "094A" : "ău",
    "094B" : "o",
    "094C" : "au",
    # "094D" : "",
    # "094E" : "",
    # "094F" : "",


    "0958" : "qa",
    "0959" : "kha",
    "095A" : "gha",
    "095B" : "za",
    "095C" : "ṛa",
    "095D" : "ṛha",
    "095E" : "fa",
    # "095F" : "",
    "0960" : "ṝ",
    "0961" : "ḻ",
    " " : " "
}

def roman(lst):
    # inp = input("Enter list of unicode values of text: ")
    # inp = inp.strip().split(",")
    ans = ""
    for i in lst:
        if (i == "094D"):
            if (ans[len(ans)-1] == "a"):
                ans = ans[:len(ans)-1]
        else:
            ans = ans + trans_dict[i]
    if (ans[len(ans)-1] == "a"):
        ans = ans[:len(ans)-1]
    return ans
