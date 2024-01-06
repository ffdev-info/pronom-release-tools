.DEFAULT_GOAL := help

.PHONY: clean package package-deps package-source package-upload package-wheel tar-source

tar-source: package-deps                                    ## Package repository as tar for easy distribution
	rm -rf tar-src/
	mkdir tar-src/
	git-archive-all --prefix template/ tar-src/template-v0.0.0.tar.gz

package-deps:                                               ## Upgrade dependencies for packaging
	python3 -m pip install -U twine wheel build git-archive-all

package-source: package-deps clean                          ## Package the source code
	python -m build .

package-check: clean package-source                         ## Check the distribution is valid
	twine check dist/*

package-upload-test: clean package-deps package-check       ## Upload package to test.pypi
	twine upload dist/* --repository testpypi --verbose

package-upload: clean package-deps package-check            ## Upload package to pypi
	twine upload dist/* --repository pypi --verbose

package: package-upload

pre-commit:     											## Run all pre-commit checks
	pre-commit run --all-files

docs:                                                       ## Generate documentation
	pdoc3 --force --html -o docs src/
	mv docs/src/* docs/.
	rm -r docs/src

serve-docs:                                                 ## Serve the documentation
	python3 -m http.server --directory html/src/

clean:                                                      ## Clean the package directory
	rm -rf src/*.egg-info/
	rm -rf build/
	rm -rf dist/
	rm -rf tar-src/

help:                                                       ## Print this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
