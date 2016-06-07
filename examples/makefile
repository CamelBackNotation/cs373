FILES :=              \
    Hello             \
    UnitTests3        \
    Coverage1         \
    Coverage2         \
    Coverage3

ifeq ($(CI), true)
    PYLINT := pylint
else
	PYLINT := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	./$<

clean:
	rm -f  *.pyc
	rm -rf __pycache__

pull:
	git pull
	git status

scrub:
	rm -f .pylintrc

test: $(FILES:=.pyx)
