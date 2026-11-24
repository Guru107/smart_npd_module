# Smart NPD Module

New Product Development for automotive suppliers, following APQP under
IATF 16949. Runs on Frappe / ERPNext v15 and v16.

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch main
bench --site your_site install-app smart_npd_module
```

Symlink-based development benches work identically via
`bench get-app --soft-link`; CI proves both modes on pushes to `main` and
every pull request.

## Contributing

This app uses `pre-commit` for code formatting and linting. Please
[install pre-commit](https://pre-commit.com/#installation) and enable it for
this repository:

```bash
cd apps/smart_npd_module
pre-commit install
```

Pre-commit runs ruff (import sort, lint, format), prettier, eslint, gitleaks
(secrets scanning), markdownlint-cli2, actionlint and zizmor (GitHub Actions
checks), codespell, pydoclint (docstring correctness), djLint (jinja lint),
and the generic file-hygiene hooks. Commit messages must follow
Conventional Commits (commitlint is enforced on pull requests).

Keep pull requests small: one self-contained change per PR. ~100 lines is a
reasonable size, ~500 lines (including tests) is the soft ceiling, ~1000 is
too large — size judgment stays with reviewers (an advisory labeler
workflow annotates PRs; it never blocks).

## CI

The following GitHub Actions workflows are configured:

- **CI** (`.github/workflows/ci.yml`, pushes to `main` + PRs): installs the app
  and runs the test suite on Frappe `version-15` (Python 3.13) and
  `version-16` (Python 3.14), Node 24 on both, plus a `bench get-app --soft-link` install
  smoke leg on v16.
- **Linters** (`.github/workflows/linter.yml`, PRs): Frappe semgrep rules +
  `r/python.lang.correctness` + `r/python.lang.best-practice` + `p/bandit`,
  basedmypy type checking, pip-audit, gitleaks, markdownlint, and commitlint.
- **PR Size** (`.github/workflows/pr-size.yml`, PRs): advisory size labels
  only — never blocks.

## License

agpl-3.0
