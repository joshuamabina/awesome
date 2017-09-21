# Style Guide for Git

## Contents

1. [Branches](#branches)
2. [Commits](#commits)
	1. [Basics](#commits-basics)
	2. [Messages](#commits-messages)
3. [Merging](#merging)

<div id="branches"></div>

## Branches

- Choosen names must be short and descriptive.
	```bash
	#good
	$ git checkout -b laravel-passport-migration

	#bad - too vague
	$ git checkout -b fix-authentication
	```

- Whenever possible, names should include a suffix corresponding to the issue identifier.
	```bash
	#GitHub issue #10
	$ git checkout -b laravel-passport-migration-10
	```

- Use *dashes* to separate words.

- Branches must be deleted from remotes after being merged.

> **ProTip:** Use `git branch --merged | grep -v "\*"` to list merged branches.

<div id="commits"></div>

## Commits

<div id="commits-basics"></div>

### Basics

- Each commit should be a single logical change. Don't make several logical changes in one commit. For example, if a patch fixes a bug and optimizes the perfomance of a feature, split it into two separate commits.

> **ProTip:** Use `git add -p` to interactively stage specific portions of modified files.

- Don't split a single logical change into to several commits. For example, the implementation of a feature and its tests should be in the same commit.

- Commits should be ordered logically. For example, if commit X depends on changes done in commit Y, then commit Y should come before commit X.

<div id="commits-messages"></div>

### Messages

> **ProTip:** Ultimately, think about what you need to know if you ran across the commit in a year from now.

- Use the editor, not the terminal, when writing a commit message.

	```bash
	#good
	$ git commit

	#bad
	$ git commit -m "Quick fix"
	```
> **ProTip** Committing from the terminal encourages a mindset of having to fit everything in one line,
> which *almost* always results into a non-informative, ambigous, useless commit messages.

- The first line of the message contains the `type` and `title` summarizing all the changes made.

	```bash
	type: This is a descriptive yet succint title
	```

	- It must be **descriptive** yet **succint**.

	- It should not end with a period.

	- It should be no longer than 50 characters.

	- The title must be capitalized and written in imperative present tense.

	- The type can be one of these:

		- **fix:** fix bug issue
		- **feat:** add a new feature
		- **docs:** change documentation
		- **style:** format code; no code change
		- **refactor:** refactor production code
		- **test:** refactor tests; no code change
		- **chore:** update build tasks, configs, etc; no code change
		- **wip:** work in progress

- The commit title should be followed with a blank line and more thorough description.

	```bash
	feat: Add a git commit message body

	Now the body, contains a more thorough description of the changes made wrapped in 72
	characters. See https://github.com/joshuamabina/styleguide
	```
	- It should be wrapped in *72 characters* and explain:

		- **why** the change is needed
		- **how** it addresses the issue
		- **what** *side-effects* it might have

	- It should also provide any pointers to related resources.

- The footer is also optional and is used to reference issue tracker IDs.

	```bash
	feat: Add footer to git commit message

	The footer is optional; it is used to reference issue tracker IDs.

	Closes #10
	```

<div id="merging"></div>

## Merging

> **ProTip:** Beware, altering published history is a common source of problems for anyone working on the project.

- Never rewrite history of the **master** branch or any other special branches.

- Before you merge your branch, rebase onto the branch its going to be merged to.

	```bash
	[laravel-passport-migration] $ git fetch
	[laravel-passport-migration] $ git rebase origin/master
	[laravel-passport-migration] $ git checkout master

	[master] $ git merge laravel-passport-migration
	```

- If your branch contains more than one commit, do not merge with a fast-forward.
	```bash
	#good
	$ git merge --no-ff laravel-passport-migration

	#bad
	$ git merge laravel-passport-migration
	```
