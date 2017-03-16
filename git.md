# Style Guide for Git

## Commits

- Each commit should be a single logical change. Don't make several logical changes in one commit. For example, if a patch fixes a bug and optimizes the perfomance of a feature, split it into two separate commits.

> **ProTip:** Use `git add -p` to interactively stage specific portions of modified files.

- Don't split a single logical change into to several commits. For example, the implementation of a feature and its tests should be in the same commit.

- Commits should be ordered logically. For example, if commit X depends on changes done in commit Y, then commit Y should come before commit X.
