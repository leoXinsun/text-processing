"""\
------------------------------------------------------------
USE: python <PROGNAME> (options)
OPTIONS:
    -s char : for generating codes at the symbol level
    -s word : for generating codes at the word leve
------------------------------------------------------------\
"""
import time
import pickle
import array
import sys, getopt,re


text=open('infile.txt','r').read()
       
# count the frequencs for character base
def freq(text):
    chars = []
    chars_freqs = []
    for character in text:
        if character not in chars:            
            char_freq = (character, text.count(character))
            chars_freqs.append(char_freq)
            chars.append(character)
    return chars_freqs
                
 # count the frequencs for word base               
def freq_w(text):
    RE = re.compile(r'[^a-zA-Z]|[a-zA-Z]+')
    content = RE.findall(text)
    chars = []
    chars_freqs = []
    for i in content:
        if i not in chars:            
            char_freq = (i, text.count(i))
            chars_freqs.append(char_freq)
            chars.append(i)
    return chars_freqs
  

# create the Node class
class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.freq = freq
        self.father = None
    def isLeft(self):
        return self.father.left == self
    
def createNodes(freqs):
    return [Node(freq) for freq in freqs]

# create the Huffman tree
def buildHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq)
        temp1 = queue[0]
        temp2 = queue[1]
        queue = queue[2:]
        new_hufftree = Node(temp1.freq + temp2.freq)
        new_hufftree.left = temp1
        new_hufftree.right = temp2
        temp1.father = new_hufftree
        temp2.father = new_hufftree
        queue.append(new_hufftree) 
    return queue[0]

# Huffman encoding
def huffmanEncoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes
 
    
 
opts, args = getopt.getopt(sys.argv[1:],'s:')
for op,value in opts:
    if op == '-s' and value =='char':
        start1 = time.clock()
        c = freq(text)
        nodes = createNodes([item[1] for item in c])
        root = buildHuffmanTree(nodes)
        codes = huffmanEncoding(nodes,root)
        code_ = {}
        for i in range(len(codes)):
            code_[c[i][0]] = codes[i]
        # output the model file 
        output_ = open("infile-symbol-model.pkl", 'wb')    
        pickle.dump(code_ , output_)   
        elapsed1 = (time.clock() - start1)
        print('it takes',elapsed1,'s to build the symbol model')

        start2 = time.clock()
        # encode the txt file
        encoded_text = ""
        for character in text:
            encoded_text += code_[character]

        add = 8 - len(encoded_text) % 8
        for i in range(add):
            encoded_text += "0"

        padded_info = "{0:08b}".format(add)
        encoded_text = padded_info + encoded_text

        codearray = array.array('B')
        for i in range(0, len(encoded_text), 8):
            c = encoded_text[i:i+8]
            b= int(c, 2)
            codearray.append(b)

        #output the compress file
        with open('infile.bin', 'wb') as f:
            codearray.tofile(f) 

        elapsed2 = (time.clock() - start2)
        print('it takes',elapsed2,'s to encode the input file given the symbol model')

    if op == '-s' and value =='word':
        start1 = time.clock()
        c = freq_w(text)
        nodes = createNodes([item[1] for item in c])
        root = buildHuffmanTree(nodes)
        codes = huffmanEncoding(nodes,root)
        code_ = {}
        for i in range(len(codes)):
            code_[c[i][0]] = codes[i]        
        # output the model file 
        output_ = open("infile-symbol-model.pkl", 'wb')    
        pickle.dump(code_ , output_)   
        elapsed1 = (time.clock() - start1)
        print('it takes',elapsed1,'s to build the symbol model')

        start2 = time.clock()
        # encode the txt file
        RE = re.compile(r'[^a-zA-Z]|[a-zA-Z]+')
        content = RE.findall(text)
        encoded_text = ""
        for i in content:
            encoded_text += code_[i]

        add = 8 - len(encoded_text) % 8
        for i in range(add):
            encoded_text += "0"

        padded_info = "{0:08b}".format(add)
        encoded_text = padded_info + encoded_text

        codearray = array.array('B')
        for i in range(0, len(encoded_text), 8):
            c = encoded_text[i:i+8]
            b= int(c, 2)
            codearray.append(b)

        #output the compress file
        with open('infile.bin', 'wb') as f:
            codearray.tofile(f) 

        elapsed2 = (time.clock() - start2)
        print('it takes',elapsed2,'s to encode the input file given the symbol model')