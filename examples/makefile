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

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	./$<

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

clean:
	rm -f  *.pyc
	rm -rf __pycache__

scrub:
	rm -f .pylintrc

test: $(FILES:=.pyx)
