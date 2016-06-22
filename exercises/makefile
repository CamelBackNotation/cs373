FILES :=           \
    IsPrime1T      \
    IsPrime2T      \
    FactorialT     \
    ReduceT        \
    RMSET          \
    Map

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
	PYLINT   := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

RMSET.pyx: RMSET.py .pylintrc
	-$(PYLINT) $<
	./$<

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	$(COVERAGE) run --branch $<
	$(COVERAGE) report -m

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)
