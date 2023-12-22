# PRONOM Release Tools

Tools for working with PRONOM releases.

## Tooling

A summary of the tooling included.

### PRONOM Summary

Summarize a PRONOM by comparing the PRONOM dataset with its corresponding
signature files. The output for a single file format looks as follows:

```json
  {
    "name": "yEnc Encoded File",
    "description": "complete",
    "signature": true,
    "identifier": "fmt/1100"
  }
```

To run:

```sh
python -m src.pronom_summary.pronom_summary
```

### PRONOM Tools

Coordinate PRONOM release output to produce a summary about the dataset and
provide links to latest release information, including links to the latest
PRONOM signature files.

To run:

```sh
python -m src.pronom_tools.pronom_tools
```

#### Check existing

```json
{
  "date": "2023-11-23",
  "latest_puid": "fmt/1924",
  "version": "V116",
  "sig_file": "https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V116.xml",
  "container_sig": "https://cdn.nationalarchives.gov.uk/documents/container-signature-20231127.xml",
  "xpuid_const": "x-fmt/455"
}
```

#### Release stats

```json
{
  "date": "2023-11-23",
  "latest_puid": "fmt/1924",
  "version": "V116",
  "sig_file": "https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V116.xml",
  "container_sig": "https://cdn.nationalarchives.gov.uk/documents/container-signature-20231127.xml",
  "xpuid_const": "x-fmt/455",
  "pronom_data": [
    {
      "name": "Broadcast WAVE 0 Generic",
      "description": "complete",
      "signature": true,
      "identifier": "fmt/1"
    },
    {
      "name": "Microsoft Word for Macintosh Document 3.0",
      "description": "complete",
      "signature": true,
      "identifier": "x-fmt/1"
    }
  ]
}
```

### PRONOM Stats

Provides a HTTP server to store stats about a PRONOM release based on the
different scripts above.

To run:

```sh
python -m src.pronom_stats.pronom_stats
```

#### Environment

A `pronom.emv` file is needed that looks as follows:

```env
# Config for PRONOM tools.
SERVER_AUTH=badf00d
SERVER_ADDR=http://127.0.0.1:26000
```

#### Ports

Ports that are used by this application:

```text
pronom api: 26000
pronom summary site: 26001
```

### PRONOM Cron

PRONOM Cron can be run as a cron task to update the pronom summary database
on a regular basis. Run with `-i` to initialize, and from there, run it `n-`
times a day to look for a new PRONOM release.

To run:

```sh
python -m src.pronom_cron.pronom_cron
```

#### Example cron

> NB. the following example requires that cron-stats is setup and running so
that the stats downloaded during the cron job can be stored.

To test for a new PRONOM release every four hours run:

```sh
crontab -e
```

And then add a task to run every four hours.

```cron
0 */4 * * * pronom-cron
```

For more cron examples see [cron guru][cron-1],

[cron-1]: https://crontab.guru/examples.html

## Developer install

### pip

Setup a virtual environment `venv` and install the local development
requirements as follows:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements/local.txt
```

### tox

#### Run tests (all)

```bash
python -m tox
```

#### Run tests-only

```bash
python -m tox -e py3
```

#### Run linting-only

```bash
python -m tox -e linting
```

### pre-commit

Pre-commit can be used to provide more feedback before committing code. This
reduces reduces the number of commits you might want to make when working on
code, it's also an alternative to running tox manually.

To set up pre-commit, providing `pip install` has been run above:

* `pre-commit install`

This repository contains a default number of pre-commit hooks, but there may
be others suited to different projects. A list of other pre-commit hooks can be
found [here][pre-commit-1].

[pre-commit-1]: https://pre-commit.com/hooks.html

## Packaging

The `Makefile` contains helper functions for packaging and release.

Makefile functions can be reviewed by calling `make`  from the root of this
repository:

```make
clean                          Clean the package directory
docs                           Generate documentation
help                           Print this help message
package-check                  Check the distribution is valid
package-deps                   Upgrade dependencies for packaging
package-source                 Package the source code
package-upload                 Upload package to pypi
package-upload-test            Upload package to test.pypi
pre-commit                     Run all pre-commit checks
serve-docs                     Serve the documentation
tar-source                     Package repository as tar for easy distribution
```

### pyproject.toml

Packaging consumes the metadata in `pyproject.toml` which helps to describe
the project on the official [pypi.org][pypi-2] repository. Have a look at the
documentation and comments there to help you create a suitably descriptive
metadata file.

### Local packaging

To create a python wheel for testing locally, or distributing to colleagues
run:

* `make package-source`

A `tar` and `whl` file will be stored in a `dist/` directory. The `whl` file
can be installed as follows:

* `pip install <your-package>.whl`

### Publishing

Publishing for public use can be achieved with:

* `make package-upload-test` or `make package-upload`

`make-package-upload-test` will upload the package to [test.pypi.org][pypi-1]
which provides a way to look at package metadata and documentation and ensure
that it is correct before uploading to the official [pypi.org][pypi-2]
repository using `make package-upload`.

[pypi-1]: https://test.pypi.org
[pypi-2]: https://pypi.org
