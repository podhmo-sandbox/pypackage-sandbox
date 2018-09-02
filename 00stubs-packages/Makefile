foo-install:
	pip install -e foo
foo-run:
	python examples/ok.py
	python examples/ng.py
foo-mypy:
	mypy --strict examples/ok.py
	mypy --strict examples/ng.py
foo-uninstall:
	pip uninstall foo
foo:
	$(MAKE) foo-install
	$(MAKE) foo-run
	$(MAKE) foo-mypy
	$(MAKE) foo-uninstall
.PHONY: foo

foo2-install:
	cd foo && pip install -e .
	cd foo-stubs && pip install -e .
foo2-run:
	python examples/ok.py
	python examples/ng.py
foo2-mypy:
	mypy --strict examples/ok.py
	mypy --strict examples/ng.py
foo2-uninstall:
	pip uninstall foo foo-stubs
foo2:
	$(MAKE) foo2-install
	$(MAKE) foo2-run
	$(MAKE) foo2-mypy
	$(MAKE) foo2-uninstall
.PHONY: foo2

