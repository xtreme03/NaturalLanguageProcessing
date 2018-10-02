import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize
'''text = "Thomas A. Anderson is a man living two lives. By day he is an " + \
    "average computer programmer and by night a hacker known as " + \
    "Neo. Neo has always questioned his reality, but the truth is " + \
    "far beyond his imagination. Neo finds himself targeted by the " + \
    "police when he is contacted by Morpheus, a legendary computer " + \
    "hacker branded a terrorist by the government. Morpheus awakens " + \
    "Neo to the real world, a ravaged wasteland where most of " + \
    "humanity have been captured by a race of machines that live " + \
    "off of the humans' body heat and electrochemical energy and " + \
    "who imprison their minds within an artificial reality known as " + \
    "the Matrix. As a rebel against the machines, Neo must return to " + \
    "the Matrix and confront the agents: super-powerful computer " + \
    "programs devoted to snuffing out Neo and the entire human " + \\
    "rebellion. "'''
def summarize_func():
    f=open("plot.txt","r")
    g=open("summerizer.txt","w")
    temp_str=""
    for x in f:
        temp_str=temp_str+x
    

#text="In 1951, two policemen, Nock and Staehl, investigate the mathematician Alan Turing after an apparent break-in at his home. During his interrogation by Nock, Turing tells of his time working at Bletchley Park during the Second World War.In 1927, the young Turing is unhappy and bullied at boarding school. He develops a friendship with Christopher Morcom, who sparks his interest in cryptography. Turing develops romantic feelings for him, but Christopher soon dies from tuberculosis.When Britain declares war on Germany in 1939, Turing travels to Bletchley Park. Under the direction of Commander Alastair Denniston, he joins the cryptography team of Hugh Alexander, John Cairncross, Peter Hilton, Keith Furman and Charles Richards. The team are trying to decrypt the Enigma machine, which the Nazis use to send coded messagesTuring is difficult to work with, and considers his colleagues inferior; he works alone to design a machine to decipher Enigma. After Denniston refuses to fund construction of the machine, Turing writes to Prime Minister Winston Churchill, who puts Turing in charge of the team and funds the machine. Turing fires Furman and Richards and places a difficult crossword in newspapers to find replacements. Joan Clarke, a Cambridge graduate, passes Turing’s test but her parents will not allow her to work with the male cryptographers. Turing arranges for her to live and work with the female clerks who intercept the messages, and shares his plans with her. With clarke's help, Turing warms to the other colleagues, who begin to respect him.Turing’s machine, which he names Christopher, is constructed, but cannot determine the Enigma settings before the Germans reset the Enigma encryption each day. Denniston orders it destroyed and Turing fired, but the other cryptographers threaten to leave if Turing goes. After Clarke plans to leave on the wishes of her parents, Turing proposes marriage, which she accepts. During their reception, Turing confirms his homosexuality to Cairncross, who warns him to keep it secret. After overhearing a conversation with a female clerk about messages she receives, Turing has an epiphany, realising he can program the machine to decode words he already knows exist in certain messages. After he recalibrates the machine, it quickly decodes a message and the cryptographers celebrate. Turing realises they cannot act on every decoded message or the Germans will realise Enigma has been broken.Turing discovers that Cairncross is a Soviet spy. When Turing confronts him, Cairncross argues that the Soviets are allies working for the same goals, and threatens to retaliate by disclosing Turing’s sexuality. When the MI6 agent Stewart Menzies appears to threaten Clarke, Turing reveals that Cairncross is a spy. Menzies reveals he knew this already and planted Cairncross to leak messages to the Soviets for British benefit. Fearing for her safety, Turing tells Clarke to leave Bletchley Park, revealing that he is gay. Heartbroken, Clarke states she always suspected but insists they would have been happy together anyway. After the war, Menzies tells the cryptographers to destroy their work and that they can never see one another again or share what they have done.In the 1950s, Turing is convicted of gross indecency and, in lieu of a jail sentence, undergoes chemical castration so he can continue his work. Clarke visits him in his home and witnesses his physical and mental deterioration. She comforts him by saying that his work saved millions of lives"

#print ('Input text:')
#print (text)
    print ('Summary:')
    print (summarize(temp_str,ratio=0.5))
    g.write(temp_str)

flg=int(input("Enter the context you want to summarize in plot.txt file then press 1 to continue"))
if flg==1:
    summarize_func()
else:
    print("Wrong input")
    
