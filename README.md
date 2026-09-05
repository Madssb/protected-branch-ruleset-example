# protected-branch-ruleset-example

Example repository for protecting the main branch, requiring PRs to pass pytest checks and ruff linting and format checking.

## setup

1. In "Branch targeting criteria", click Add target, then click "Include by pattern". Add the inclusion pattern with "main" as the "Branch naming pattern".

2. In "Branch rules", add the following:
   1. "Restrict deletions".
   2. "Require a pull request before merging".
   3. "Require status checks to pass" with the `pytest-ruff.yml` Github Action as the status check that is required.
   4. "Block force pushes".
