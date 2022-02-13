"""
Copies relevant quiz/* to a questions/ directory of a course.

quiz/
    answers.py -- a dummy one
    makefile
    parser.py
    questions/instructions.tex
    questions/latexcircuit.py
    questions/latextool_basic.py
    questions/makefile
    questions/thispreamble.tex
    questions/main.tex

USAGE:

    * assume cwd is cissxxx/q/q1234/
    * run makequiz.py
      python /home/student/yliow/Documents/work/projects/latex-templates/makequiz.py
      which will
      * copy above files into cissxxx/q/q1234/. Omit main.tex if
        already exists.
      * substitute the "cissxxx" into thispreamble.tex
      * substitute the "q1234" into thispreamble.tex

"""
import os, shutil, re

DIR = os.path.dirname(os.path.abspath(__file__)) # dir of this file
DIR = os.path.join(DIR, 'quiz')

def cp(f0, f1):
    print('cp %s %s' % (f0, f1), flush=True)
    shutil.copy2(f0, f1)
def mv(f0, f1):
    print('mv %s %s' % (f0, f1), flush=True)
    shutil.move(f0, f1)
def readfile(fname):
    f = open(fname, 'r'); s = f.read(); f.close()
    return s
def writefile(fname, s):
    f = open(fname, 'w'); f.write(s); f.close()
def mkdir(dir_='questions'):
    print('mkdir %s' % dir_, flush=True)    
    os.makedirs(dir_)
def __dir__(x):
    """ return dir of this source file """
    return os.path.dirname(os.path.abspath(__file__))
    
# >>> FROM ALEX05
def getdefaultcourse():
    # get ciss??? or math??? from path
    p = re.compile(r'/((ciss|math)\d\d\d)(/|$)')
    s = os.getcwd()
    srch = p.search(s)
    if srch != None:
        return srch.group(1)
    else:
        return None
def getdefaultassessment():
    p = re.compile('/((a|q|p|t)[0-9]+[-0-9a-z]*)')
    s = os.getcwd()
    srch = p.search(s)
    t = None
    if srch != None:
        return srch.group(1)
    else:
        for root, dirs, files in os.walk('.'):
            for dir_ in dirs:
                path = os.path.abspath(dir_)
                srch = p.search(path)
                if srch != None:
                    return srch.group(1)
            break
        return None

def makequiz():
    s = r'''
    answers.py
    makefile
    parser.py
    questions/instructions.tex
    questions/latexcircuit.py
    questions/latextool_basic.py
    questions/makefile
    questions/thispreamble.tex
    questions/main.tex
    '''.strip()
    lines = [line.strip() for line in s.split('\n') \
             if line.strip() != '']
    lines0 = [os.path.join(DIR, line) \
              for line in lines]
    lines1 = lines[:]

    if os.path.isdir('questions'):
        print('questions/ not found ... creating ...', flush=True)
    else:
        mkdir('questions')
        
    for line0,line1 in zip(lines0, lines1):

        # Copy from latex-templates to current directory, except that
        # for files in questions/, make a copy is the file exists
        if os.path.exists(line1) and line1.startswith('questions'):
            t = line1
            while os.path.exists(t):
                print('>>> %s exists' % t)
                t = line1 + '.old'
            mv(line1, t)
        cp(line0, line1)
            
        if line1.endswith('thispreamble.tex'):
            course = getdefaultcourse()
            assessment = getdefaultassessment()
            #print(">>> course:", course)
            #print(">>> assessment:", assessment)
            s = readfile(line1)
            if course != None:
                old = r'\newcommand\COURSE{ciss240}'
                new = r'\newcommand\COURSE{%s}' % course
                s = s.replace(old, new)
            if assessment != None:
                old = r'\newcommand\ASSESSMENT{q0000}'
                new = r'\newcommand\ASSESSMENT{%s}' % assessment
                s = s.replace(old, new)
            writefile(line1, s)
            
if __name__ == '__main__':
    makequiz()
