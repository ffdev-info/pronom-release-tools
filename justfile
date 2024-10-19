# CLI helpers.

# Help
help:
	@just -l

# Package repository as tar for easy distribution
tar-source: package-deps
	rm -rf tar-src/
	mkdir tar-src/
	git-archive-all --prefix template/ tar-src/template-v0.0.0.tar.gz

# Upgrade dependencies for packaging
package-deps:
	python3 -m pip install -U twine wheel build git-archive-all

# Package the source code
package-source: package-deps clean
	python -m build .

# Check the distribution is valid
package-check: clean package-source
	twine check dist/*

# Upload package to test.pypi
package-upload-test: clean package-deps package-check
	twine upload dist/* --repository testpypi --verbose

# Upload package to pypi
package-upload: clean package-deps package-check
	twine upload dist/* --repository pypi --verbose

# Run all pre-commit checks
pre-commit:
	pre-commit run --all-files

# Generate documentation
docs:
	pdoc3 --force --html -o docs src/
	mv docs/src/* docs/.
	rm -r docs/src

# Serve the documentation
serve-docs:
	python -m http.server --directory html/src/

# Upgrade project dependencies
upgrade:
	python -m pip-upgrade

# Clean the package directory
clean:
	rm -rf src/*.egg-info/
	rm -rf build/
	rm -rf dist/
	rm -rf tar-src/

# Pronom tools
pronom-tools args:
	python -m src.pronom_tools.pronom_tools {{args}}

# Pronom stats
pronom-stats args:
	python -m src.pronom_stats.pronom_stats {{args}}

# Pronom cron
pronom-cron args:
	python -m src.pronom_cron.pronom_cron {{args}}

# Pronom export
pronom-export args:
	python -m src.pronom_export.pronom_xml_export {{args}}
