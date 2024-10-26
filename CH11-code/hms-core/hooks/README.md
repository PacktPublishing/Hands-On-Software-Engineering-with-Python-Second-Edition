# How to use these hooks

The first time this repository is checked out or pulled
from SCM, it is important to alter your local Git
configuration so that it will use the hooks in this
directory instead of the default `.git/hooks` directory.

To do this, run the following command from a terminal
session in the project's root directory:

```bash
git config core.hooksPath hooks
```

## `post-checkout` and `post-merge`

(See [post-checkout](https://git-scm.com/docs/githooks/2.2.3#_post_checkout)
and [post-merge](https://git-scm.com/docs/githooks/2.2.3#_post_merge))

> Invoked when a git checkout is run after having updated
> the worktree, including when a `git clone` is executed;
and
> after a `git merge`, which happens when a `git pull` is
> done on a local repository;

respectively.

Both of these hooks update the project's package dependencies
before running the standard security check, [`security-scans.py`](security-scans.py)
against the current package-dependency versions.

## `pre-push`

(See [pre-push](https://git-scm.com/docs/githooks/2.2.3#_pre_push))

> This hook is called by git push and can be used to
> prevent a push from taking place.

- Executes the [`security-scans.py`](security-scans.py)
  script to check for known security issues with packages
  used by the project.
- Runs the unit-test suite (`tests/unit`) with `pytest`
- Runs `flake8` against the code in the `src` directory
- Runs `flake8` against the code in the `tests/unit` directory


## The `security-scans.py` script

(See [`security-scans.py`](security-scans.py))

A script that runs pipenv check with a collection of
vulnerabilities to ignore, each of which is documented
with a reason in the script itself.

As vulnerabilities surface, there are two options:

- The offending package can be updated or replaced.

- The reported vulnerability may be added to the `IGNORE_ITEMS`
  dictionary in the script, ***along with a brief explanation
  of why it can be ignored***.

See [example-scan-results.txt](example-scan-results.txt)
for an example of the output this generates.
