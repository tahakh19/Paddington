import sys
import pysrt
import obo 


srts={"paddington":"Paddington.srt", "corpse":"Corpse.Bride.2005.1080p.BrRip.x264.BOKUTOX.YIFY.srt"}
info={}

def write_freq(freqdict, output_name):
    counter = 0
    #for freq in range(5,1,-1):
    #    f = open("Corpse_word_freq-%d.txt"%freq)
    out = open(output_name, "w")
    freq = -1
    for c, w in freqdict:
        if freq != c:
            if freq != -1:
                msg= "-"*10 + " Summery: freq=%d count=%d "%(freq, counter) + "-"*10 + "\n"
                #print(msg)
                out.write(msg)
                counter = 0
                 
            freq = c
            
            msg="-"*10 + "Word with freq = %d"%c + "-"*10 + "\n"
            #print(msg)
            out.write(msg)
                
        counter += 1
        #if c >= 2:
        #print(c, str(w))
            #counter = counter + 1
            #print(counter, str(w))
        #if counter >= 1000 :
        #    break
        msg = str(w) + "\n"
        #print(msg)
        out.write(msg)


    msg= "-"*10 + " Summery: freq=%d count=%d "%(freq, counter) + "-"*10 + "\n"
    #print(msg)
    out.write(msg)
    out.close()

for name, file in srts.items():
    #print(name, file)
    wordstring = ""
    subs = pysrt.open(file)
    
    for i in subs:
        wordstring += i.text + " "

    
    text = wordstring.lower()

    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
    wordset = set(wordlist)
    dictionary = obo.wordListToFreqDict(wordlist)
    sorteddict = obo.sortFreqDict(dictionary)

    write_freq(sorteddict, name+"_word_freq.txt")

    info[name]={}
    info[name]["wordset"]=wordset
    info[name]["sorteddict"]=sorteddict

    
intersect = info['paddington']["wordset"].intersection(info["corpse"]["wordset"])

with open("intersection.txt", "w") as f:
    for i in intersect:
        f.write(i + "\n")
    
#print(len(intersect))

#sys.exit(-1)










