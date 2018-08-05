import sys, getopt, re, math
import copy
class Retrieve:

    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index,termWeighting):
        self.index = index
        self.termWeighting = termWeighting

    # Method to apply query to index
    def forQuery(self,query):
        b = list(self.index.keys())
        list1 = []
        list2 = []
        for i in range(len(b)):
            list1.append(b[i])
            list2.append(self.index[b[i]])
            
        d_1 = 0    
        for i in range (len(list2)):
            n = list2[i]
            z = list(n.keys())
            for j in range(len(z)):
                x = z[j]
                if x > d_1:
                    d_1= x
                else:
                    d_1 =d_1
        D = d_1
        
        if self.termWeighting == 'binary':
            a = list(query.keys())
            l= (len(a))
            q = 0
            for i in range (l):
                q_0 = 0
                if query[a[i]] != 0:
                    query[a[i]] = 1
                else:
                    query[a[i]] =0
                q_0 = (query[a[i]])*(query[a[i]])
                q = q + q_0
                
            dd = []
            index_1 = self.index
            for i in range(D):
                self.index = copy.deepcopy(index_1)
                list1 = list(self.index.keys())
                list2 = list(self.index.values())
                for m in range(len(list1)): 
                    list3 = list2[m]
                    list4 = list(list3.keys())
                    if i+1 not in list4:
                        del self.index[list1[m]]
                dd = []
                d = 0
                for m in range(len(self.index)): 
                    d_1 = 0
                    list_2 = list(self.index.values())
                    list_3 = list_2[m]
                    list_4 = list(list_3.keys())
                    list_5 = list(list_3.values())
                    for n in range(len(list_4)):
                        if list_5[n] != 0:
                            list_5[n] =1
                        else:
                            list_5[n] =0
                        o = list_4[n]
                        if o == i+1:
                            d_1 = (list_5[n])*(list_5[n])
                            d = d + d_1
                        else:
                            d_1 = 0
                            d = d + d_1
                dd.append(d)
                
            adict = {}
            for i in range(D):       
                up = 0
                for j in range(l):    
                    w = 0
                    x = 0
                    z = 0
                    q_1 = a[j]
                    f = query[a[j]]
                    if f != 0:
                        f = 1
                    else:
                        f = 0
        
                    if q_1 in list1:
                        m = list1.index(q_1)
                        list3 = list2[m]
                        list4 = list(list3.keys())
                        if i+1 in list4:
                            n = list4.index(i+1)
                            z = list3[i+1]
                            if z != 0:
                                z = 1
                            else:
                                z = 0
                            x = z*f
                            w = w+x
                        else:
                            x = 0
                            w = w+x
                    else:
                        x = 0
                        w = w+x
                    up = up + w
                   
                down = (q**0.5)*((dd[i])**0.5)
                similarity = up/down
                adict[i+1] = similarity
    
            sort = sorted(adict.items(), key = lambda x:x[1], reverse = True)
            store=[]
            for i in sort:
                store.append(i[0])
            return store
    
    
        if self.termWeighting == 'tf':
            a = list(query.keys())
            l= (len(a))
            q = 0
            for i in range (l):                
                q_0 = (query[a[i]])*(query[a[i]])
                q = q + q_0
                
            dd = []
            index_1 = self.index
            for i in range(D):
                self.index = copy.deepcopy(index_1)
                list1 = list(self.index.keys())
                list2 = list(self.index.values())
                for m in range(len(list1)): 
                    list3 = list2[m]
                    list4 = list(list3.keys())
                    if i+1 not in list4:
                        del self.index[list1[m]]
                d = 0
                for m in range(len(self.index)): 
                    d_1 = 0
                    list_2 = list(self.index.values())
                    list_3 = list_2[m]
                    list_4 = list(list_3.keys())
                    list_5 = list(list_3.values())
                    for n in range(len(list_4)):                    
                        o = list_4[n]
                        if o == i+1:
                            d_1 = (list_5[n])*(list_5[n])
                            d = d + d_1
                        else:
                            d_1 = 0
                            d = d + d_1
                dd.append(d)
                
            adict = {}
            for i in range(D):       
                up = 0
                for j in range(l):    
                    w = 0
                    x = 0
                    z = 0
                    q_1 = a[j]
                    f = query[a[j]]
                    if f != 0:
                        f = 1
                    else:
                        f = 0
        
                    if q_1 in list1:
                        m = list1.index(q_1)
                        list3 = list2[m]
                        list4 = list(list3.keys())
                        if i+1 in list4:
                            n = list4.index(i+1)
                            z = list3[i+1]
                            x = z*f
                            w = w+x
                        else:
                            x = 0
                            w = w+x
                    else:
                        x = 0
                        w = w+x
                    up = up + w
                   
                down = (q**0.5)*((dd[i])**0.5)
                similarity = up/down
                adict[i+1] = similarity
    
            sort = sorted(adict.items(), key = lambda x:x[1], reverse = True)
            store=[]
            for i in sort:
                store.append(i[0])
            return store

        if self.termWeighting == 'tfidf':    
            a = list(query.keys())
            l= (len(a))
            q = 0
            idf={}
            for i in range (len(b)):
                idf_0 = D/(len(list2[i]))
                idf_1 = math.log10(idf_0)
                idf[b[i]] = len(idf_1)
                
                
            for i in range (l):
                q_0 = 0
                if a[i] in list(idf.keys()):        
                    q_0 = ((query[a[i]]) * (idf[a[i]]))*((query[a[i]]) * (idf[a[i]]))
                if a[i] not in list(idf.keys()):
                    q_0 =  0
                q_0 = (query[a[i]])*(query[a[i]])
                q = q + q_0
                
            dd = []
            index_1 = self.index
            for i in range(D):
                self.index = copy.deepcopy(index_1)
                list1 = list(self.index.keys())
                list2 = list(self.index.values())
                for m in range(len(list1)): 
                    list3 = list2[m]
                    list4 = list(list3.keys())
                    if i+1 not in list4:
                        del self.index[list1[m]]
                d = 0
                for m in range(len(self.index)): 
                    d_1 = 0
                    list_2 = list(self.index.values())
                    list_3 = list_2[m]
                    list_4 = list(list_3.keys())
                    list_5 = list(list_3.values())
                    for n in range(len(list_4)):                       
                        o = list_4[n]
                        if o == i+1:
                            d_1 = ((list_5[n]) *(idf[list1[m]]))*((list_5[n])*(idf[list1[m]]))
                            d = d + d_1
                        else:
                            d_1 = 0
                            d = d + d_1
                dd.append(d)
                
            adict = {}
            for i in range(D):       
                up = 0
                for j in range(l):    
                    w = 0
                    x = 0
                    z = 0
                    q_1 = a[j]
                    f = query[a[j]] * idf[q_1]
                    if f != 0:
                        f = 1
                    else:
                        f = 0
        
                    if q_1 in list1:
                        m = list1.index(q_1)
                        list3 = list2[m]
                        list4 = list(list3.keys())
                        if i+1 in list4:
                            n = list4.index(i+1)
                            z = list3[i+1] * idf[i+1]
                            x = z*f
                            w = w+x
                        else:
                            x = 0
                            w = w+x
                    else:
                        x = 0
                        w = w+x
                    up = up + w
                   
                down = (q**0.5)*((dd[i])**0.5)
                similarity = up/down
                adict[i+1] = similarity
    
            sort = sorted(adict.items(), key = lambda x:x[1], reverse = True)
            store=[]
            for i in sort:
                store.append(i[0])
            return store
            
    

            
    
    
    
    
    
    

    
