The directory organization should be

    ciss101/
        q/
            q0101/
                makefile -- "make" will create q0101.tar.gz
                         -- "make a" will create answers/ from questions/, answers.py, parser.py
                questions/
                        makefile -- "make s" creates submit.tar.gz (but alex can do this)
                answers.py -- contains answers, a list of strings of answers
                parser.py -- used by makefile
                answers
                                        
    project/latex-templates/
        makequiz.py
        quiz/ -- template for quiz directories of courses
        makefile
        questions/ -- template for questions/ 
        answers.py
        parser.py
