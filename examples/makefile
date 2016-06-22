FILES :=              \
    Hello             \
    UnitTests3        \
    Coverage1         \
    Coverage2         \
    Coverage3         \
    Exceptions        \
    Types             \
    Operators         \
    Variables         \
    Cache             \
    Copy              \
    Iteration         \
    Yield             \
    Comprehensions    \
    Lambdas           \
    Iterables         \
    FunctionKeywords  \
    FunctionDefaults  \
    FunctionUnpacking \
    FunctionTuple     \
    FunctionDict      \
    Callables

ifeq ($(CI), true)
    PYLINT := pylint
else
	PYLINT := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	./$<

clean:
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)
