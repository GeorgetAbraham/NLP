  # Code To convert Hinglish text to Hindi.
consonant=['b','c','C','d','D','f','g','h','j','k',\
'l','m','n','N','p','q','r','R','s','S','t','T','v','w','x','y','z']

vowels=['a', 'e', 'i', 'o', 'u']


def dumb_seg(g):
    listee=[]
    pntr=0
    for x in g:
        if(x in consonant or pntr==0):
            pntr+=1;
            listee.append(x)
        # if(pntr>0 and x=='i' and listee[pntr-1][0]=='R'):
        #     pntr+=1
        #     listee[pntr-1]= listee[pntr-1]+x
        elif(x in vowels and  x==listee[pntr-1][-1] and len(listee[pntr-1])==3 ):

            pntr+=1;
            listee.append(x)
        elif(x in vowels and  x!=listee[pntr-1][-1] and (listee[pntr-1][-1] in vowels) ):
            pntr+=1;
            listee.append(x)
        else:
            #print(listee[pntr-1])
            if(x==listee[pntr-1][-1] and x in vowels) :
                listee[pntr-1]= listee[pntr-1]+x
            if(listee[pntr-1][-1] in consonant and x in vowels):
                listee[pntr-1]= listee[pntr-1]+x


    return listee

#join  t,ha to tha :s,h to sha etc

def dumb_joiner_ha(listee):
    pntr=0
    jo_list=[]
    tempo_list=['k','g','c','C','j','t','T','d','D','p','b','s','S']
    for i in range(0,len(listee)):
        if(listee[i] in tempo_list and i!=len(listee)-1):
            if(listee[i+1][0]=="h"):
                jo_list.append(listee[i]+listee[i+1])
                pntr+=1
                listee[i+1]="zorran"

            else:
                jo_list.append(listee[i])
                pntr+=1
        else:
            if(listee[i]=="zorran"):
                a=0
            else:
                jo_list.append(listee[i])
                pntr+=1
    return jo_list


#------------------------------------------------------

def splitts(listee):
    splitter=[]
    for i in range(0,len(listee)):
        if(i==0):
            if(listee[i][0] in vowels):
                splitter.append([listee[i]])
            else:
                tempora=[]
                for j in range(0,len(listee[0])):
                    if(listee[i][j] in vowels):
                        tempora.append(listee[i][0:j])
                        tempora.append(listee[i][j:])
                        break
                if(tempora!=[]):
                    splitter.append(tempora)
                if(tempora==[]):
                    splitter.append([listee[0]])
        if(i>0):
            tempora=[]
            for j in range(0,len(listee[i])):
                if(listee[i][j] not in consonant):
                    if(listee[i][0:j]!=''):
                        tempora.append(listee[i][0:j])
                    tempora.append(listee[i][j:])
                    break

                #print tempora
            if(tempora==[]):
                tempora.append(listee[i])
            splitter.append(tempora)

    return splitter


h_dict = { \
"a"    :u'\u0905',
"aa"   :u'\u0906',
"i"    :u'\u0907',
"ii"   :u'\u0908',
"u"    :u'\u0909',
"uu"   :u'\u090a',
####
"Ri"  :u'\u090b',
####
"e"    :u'\u090f',
"ee"   :u'\u0910',
"o"    :u'\u0913',
"oo"   :u'\u0914',
#
"ka"   :u'\u0915',
"kha"  :u'\u0916',
"ga"   :u'\u0917',
"gha"  :u'\u0918',
#
"cha"  :u'\u091a',
"Cha"  :u'\u091b',
"ja"   :u'\u091c',
"jha"  :u'\u091d',
#
"Ta"   :u'\u091f',
"Tha"  :u'\u0920',
"Da"   :u'\u0921',
"Dha"  :u'\u0922',
"Na"   :u'\u0923',
#
"ta"   :u'\u0924',
"tha"  :u'\u0925',
"da"   :u'\u0926',
"dha"  :u'\u0927',
"na"   :u'\u0928',
#
"pa"   :u'\u092a',
"fa"   :u'\u092b',
"ba"   :u'\u092c',
"bha"  :u'\u092d',
"ma"   :u'\u092e',
#
"ya"   :u'\u092f',
"ra"   :u'\u0930',
"la"   :u'\u0932',
"va"   :u'\u0935',
#
"sha"  :u'\u0936',
"Sha"  :u'\u0937',
"sa"   :u'\u0938',
"ha"   :u'\u0939',
#
"hlnt" :u'\u094d',
#
"za"    :u'\u095b',
#
"aX"   :u'\u093e',
"aaX"  :u'\u093e',
"iX"   :u'\u093f',
"iiX"  :u'\u0940',
"uX"   :u'\u0941',
"uuX"  :u'\u0942',
"eX"   :u'\u0947',
"eeX"  :u'\u0948',
"oX"   :u'\u094b',
"ooX"  :u'\u094c',
#####
"rrX"  :u'\u0943'
}

vowels = [ 'a', 'aa',\
    'i', 'ii','u', 'uu',\
    'e', 'ee','o', 'oo']



def hindi(inp):
    holder=dumb_seg(inp)
    tempo= dumb_joiner_ha(holder)
    l= splitts(tempo)

    s= ""
    i=0
    try:
        while i<len(l):
            if len(l[i])==1:
                if l[i][0] in vowels:
                    s += h_dict[l[i][0]]
                if(l[i][0] not in vowels):
                    if(i<len(l)-1 and l[i+1][0]=='r' and l[i]!=['r']):
                        if(len(l[i+1])==2):#kram
                            s += h_dict[l[i][0]+"a"]+h_dict["rrX"]

                            if(l[i+1][1]!='a'):
                                s+=h_dict[l[i+1][1]+"X"]
                            i+=2
                            continue
                        if(len(l[i+1])==1):
                            s += h_dict[l[i][0]+"a"]+h_dict["hlnt"]

                    else:
                        #print ('dido')
                        s += h_dict[l[i][0]+"a"]+h_dict["hlnt"]

            # ----------------------

            elif len(l[i])==2:
                if(l[i][0]=='R'):
                    s += h_dict["Ri"]
                elif l[i][1] == "a":
                    s += h_dict[l[i][0]+"a"]

                else:
                    s += h_dict[l[i][0]+"a"] + h_dict[l[i][1]+"X"]
            i+=1



        return s

    except:
        return (None)
