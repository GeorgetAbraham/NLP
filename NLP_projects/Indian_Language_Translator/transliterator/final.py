import segmenter
import romanization

if __name__ == "__main__":
    inp = input("Enter Hinglish Text: ")
    out1 = segmenter.hindi(inp)
    lst = []
    if (out1 == None):
        print ("Some incorrect spelling used. Check documentation for instructions on how to use Transliterator")
    else:
        for i in out1:
            lst.append("0" + str((hex(ord(i))))[2:].upper())
        out2 = romanization.roman(lst)
        print ("Hindi output : ", out1)
        print ("Romanized output: ", out2)
