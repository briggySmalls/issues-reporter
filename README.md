[![Build Status](https://travis-ci.org/briggySmalls/gisrep.svg?branch=master)](https://travis-ci.org/briggySmalls/gisrep)

# Gisrep

The command line Github issues reporter, powered by [PyGithub](https://github.com/PyGithub/PyGithub).

## Installation

```
pip install 'path/to/package'
```

This installs the `gisrep` script to the command line.

## Usage

### Publishing reports

Publishing reports uses the `report` subcommand:

```
gisrep report simple_report.md "repo:twbs/bootstrap is:open label:feature" clipboard
```

The gisrep report subcommand comprises three components:

- A Template (`simple_report.md`) to format issues
- A Github search query (`"repo:twbs/..."`) to filter issues
- An Output (`clipboard`) used to deliver the report

#### Templates
The template component can be either a tag for a built-in template, or a filepath to a custom template. Read the [templates readme](gisrep/templates/README.md) for creating custom templates.

#### Github search query
The search query is passed to the [Github search API](https://developer.github.com/v3/search/#search-issues) to filter issues and pull requests. Read the Github guide on [searching issues and pull requests](https://help.github.com/articles/searching-issues-and-pull-requests/) for help constructing queries.

#### Outputs
The output is a method of delivering the report. Defaults to printing to the console.

### Listing built-ins

Listing the available built-in templates or outputs uses the `list` subcommand.

To list the tags for built-in templates use the following command:

```
gisrep list templates
```

To list the tags for built-in outputs use the following command:

```
gisrep list outputs
```

### Private repositories

The tool needs to be initialised with Github credentials in order to access private repositories. The tool is initialised with the following command:

```
gisrep init
```

You will be prompted for your Github username and password. The password is stored in your system's password manager using [keyring](https://pypi.python.org/pypi/keyring). To overrwrite an existing configuration use the `--force` argument.
