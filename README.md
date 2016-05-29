This is not an official Google product.

Copy type annotations from a PEP484 stub file into python source.

Sample use:

       python merge_pyi.py --pep484 --diff testdata/simple.py testdata/simple.pyi

#### Regression tests

```
testdata/foo.py  : input we want to annotate
testdata/foo.pyi : type hints we want to add to foo.py (may be intentionally bad)

testdata/foo.comment.py : expected output, inserting types as comments
testdata/foo.pep484.py  : expected output, inserting types in PEP484 style
```
