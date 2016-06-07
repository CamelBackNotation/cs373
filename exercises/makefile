FILES :=           \
    IsPrime1T

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
	PYLINT   := pylint3
endif

%.pyx: %.py
	-$(PYLINT) $<
	$(COVERAGE) run --branch $<
	$(COVERAGE) report -m

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

RMSET.pyx: RMSET.py
	-$(PYLINT) $<
	./$<

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

scrub:
	rm -f .pylintrc

test: .pylintrc $(FILES:=.pyx)
