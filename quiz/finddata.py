'''
to find answers in latex file (which are quizzes)

ADD INCORRECt NESTING:
\begin{answerlong}
\begin{answercode}
\end{answerlong}
\end{answercode}
'''
import re

def getcourse(s):
    p = re.compile(r'\\newcommand\\COURSE\{(ciss\d*|math\d*)\}')
    return p.search(s).group(1)

def getassessment(s):
    p = re.compile(r'\\newcommand\\ASSESSMENT{(q\d*)}')
    return p.search(s).group(1)

def getauthor(s):
    p = re.compile(r'\\renewcommand\\AUTHOR{([a-z@0-9.]*)}')
    return p.search(s).group(1)

def getanswers(s):
    p = re.compile(r'\\begin\{answercode\}|\\answerbox\{|\\begin\{answerlong\}')
    xs = []
    for m in re.finditer(p, s):
        subs = s[m.start(0): m.end(0)]
        if subs == r'\begin{answercode}':
            i = s[m.end(0):].find(r'\end{answercode}')
            t = s[m.end(0):][:i]
        elif subs == r'\answerbox{':
            i = s[m.end(0):].find('}')
            t = s[m.end(0):][:i]
        elif subs == r'\begin{answerlong}':
            i = s[m.end(0):].find(r'\end{answerlong}')
            t = s[m.end(0):][:i]
        t = t.strip()
        xs.append(t)        
    return xs


def getanswers2(s):
    p = re.compile(r'\\begin\{answercode\}(.*)\\end\{answercode\}' + '|' + \
                   r'\\answerbox\{(.*)\}' + '|' + \
                   r'\\begin\{answerlong\}(.*)\\end\{answerlong\}')
    xs = []
    for m in re.finditer(p, s):
        t = m.group(0)
        print(m.group(0))
        print(m.group(1))
        xs.append(t)
    return xs

def finddata(thispreamble='questions/thispreamble.tex',
             main='questions/main.tex'):
    t = open(thispreamble, 'r').read()
    m = open(main, 'r').read()
    return {"course": getcourse(t),
            "assessment": getassessment(t),
            "author": getauthor(m),
            "answers": getanswers(m)}

def addanswers(s, answers):
    p = re.compile(r'\\begin\{answercode\}\n|\\answerbox\{|\\begin\{answerlong\}\n')
    xs = []
    kinds = []
    indices = []
    for m in re.finditer(p, s):
        subs = s[m.start(0): m.end(0)]
        #print("subs:", subs)
        #for c in subs:
        #    print("c: (%s,%s) " % (c, ord(c)), end="")
        #print()
        if subs == '\\begin{answercode}\n':
            i = s[m.end(0):].find(r'\end{answercode}')
            t = s[m.end(0):][:i]
            # if ends with '\n', remove last '\n'
            if t[-1] == '\n': t = t[:-1]
            kinds.append('answercode')
        elif subs == r'\answerbox{':
            i = s[m.end(0):].find('}')
            t = s[m.end(0):][:i]
            kinds.append('answerbox')
        elif subs == '\\begin{answerlong}\n':
            i = s[m.end(0):].find(r'\end{answerlong}')
            t = s[m.end(0):][:i]
            # if ends with '\n', remove last '\n'
            if t[-1] == '\n': t = t[:-1]
            kinds.append('answerlong')
        else:
            print("ERROR!")
        
        indices.append((m.end(0), m.end(0) + i))
        xs.append(t)        

    #return xs
    #print("xs:", xs)
    #print("number indices:", len(indices))
    #print(indices)
    #print("number answers:", len(answers))
    #print(answers)
    new_s = ""
    previous_index = 0
    for index, answer, kind in zip(indices, answers, kinds):
        new_s += s[previous_index: index[0]]
        new_s += answer
        if kind in ['answercode', 'answerlong']:
            new_s += '\n'
        previous_index = index[1]
    new_s += s[previous_index:]
    print(new_s)
    
if __name__ == '__main__':
    #data = finddata()
    #print("course:", data['course'])
    #print("assessment:", data['assessment'])    
    #print("author:", data['author'])
    #print("answers:", data['answers'])

    from answers import answers
    s = open('questions/main.tex', 'r').read()
    addanswers(s, answers)

    #t = open('questions/main.tex', 'r').read()
    #print(getanswers2(t))
