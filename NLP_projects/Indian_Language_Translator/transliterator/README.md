## Indian Language Transliterator

# Introduction
A transliterator that takes "Hinglish" (hindi written in english script) as input, and converts it to native hindi script. Also, a romanization tool that converts that hindi script to romanized script. 

# Approach

1. 

2.

# Transliteration Scheme

* Hindi vowels (Hindi Swaron)
<pre>
a : अ   aa : आ
i : इ   ii : ई
u : उ   uu : ऊ
Ri : ऋ  
e : ए    ee : ऐ
o : ओ   oo : औ
</pre>

* Hindi consonants (Hindi Vyannjana)
<pre>
ka : क   kha: ख  ga : ग   gha: घ
cha: च   Cha: छ  ja : ज   jha: झ
Ta : ट   Tha: ठ   Da : ड   Dha: ढ  Na : ण
ta : त   tha: थ   da : द   dha: ध  na : न 
pa : प   fa : फ   ba : ब   bha: भ  ma : म 
ya : य   ra : र   la : ल   va : व
sha : श  Sha : ष  sa : स   ha : ह
za : ज़
</pre>

* Maathra
<pre>
aa : ◌ा
i : ि◌   ii : ◌ी
u : ◌ु    uu : ◌ू
e : ◌े    ee : ◌ै
o : ◌ो    oo : ◌ौ
</pre>

# How to Use

1. Run transliterator.py (preferably pipe the output to a .txt file)
2. Give your input in hinglish.

Example
<pre>
$ python3 transliterator.py
> shaktimaana
$ शक्तिमान
</pre>


