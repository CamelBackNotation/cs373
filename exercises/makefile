FILES :=           \
    IsPrime1T

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
	PYLINT   := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

RMSET.pyx: RMSET.py
	-$(PYLINT) $<
	./$<

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	$(COVERAGE) run --branch $<
	$(COVERAGE) report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

pull:
	git pull
	git status

scrub:
	rm -f .pylintrc

test: $(FILES:=.pyx)
