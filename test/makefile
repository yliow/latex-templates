pdf:
	-python /home/student/.alex/alexrunner.py replaceemail
	#pdflatex --shell-escape main.tex
	pdflatex --shell-escape main.tex
	xdg-open main.pdf

b:
	cp main.tex "main-$$(date +"%Y-%m-%-d-%H-%M-%S").tex"

v:
	xdg-open main.pdf

c:
	rm -f main.aux main.idx main.log main.out makefile.old main.py main.py.err main.py.out latex.py

s:
	rm -f main.aux main.idx main.log main.out makefile.old main.py main.py.err main.py.out latex.py
	rm -rf submit; rm -f submit.tar.gz; mkdir submit; rsync -av . submit --exclude submit; tar -cvf submit.tar submit; gzip submit.tar || true
	@echo ""
	@echo "done ... submit.tar.gz is created:"
	@ls -la submit.tar.gz
	@echo ""
