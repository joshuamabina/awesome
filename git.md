# Style Guide for Git

## Branches

- Choosen names must be short and descriptive.
	```bash
	# good
	$ git checkout -b laravel-passport-migration

	# bad - too vague
	$ git checkout -b fix-authentication
	```

- Whenever possible, names should include a suffix corresponding to the issue identifier. 
	```bash
	# GitHub issue #10
	$ git checkout -b laravel-passport-migration-10
	```

- Use *dashes* to separate words.

- Branches must be deleted from remotes after being merged.

> **ProTip:** Use `git branch --merged | grep -v "\*"` to list merged branches.

## Commits

- Each commit should be a single logical change. Don't make several logical changes in one commit. For example, if a patch fixes a bug and optimizes the perfomance of a feature, split it into two separate commits.

> **ProTip:** Use `git add -p` to interactively stage specific portions of modified files.

- Don't split a single logical change into to several commits. For example, the implementation of a feature and its tests should be in the same commit.

- Commits should be ordered logically. For example, if commit X depends on changes done in commit Y, then commit Y should come before commit X.

### Messages

- Use the editor, not the terminal, when writing a commit message
	```bash
	# good 
	$ git commit

	# bad
	$ git commit -m "Quick fix"
	```

Committing from the terminal encourages a mindset of having to fit everything in one line, which *almost* always results into a non-informative, ambigous, useless commit messages.

```bash
type: title

body

footer
```

- The first line of the message contains the `type` and `title` summarizing all the changes made. 

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

- The commit title should be followed with a blank line and more thorough description. 

	- It should be wrapped in *72 characters* and explain:

		- **why** the change is needed 
		- **how** it addresses the issue 
		- **what** *side-effects* it might have

	- It should also provide any pointers to related resources.

- The footer is also optional and is used to reference issue tracker IDs.

> **ProTip:** Ultimately, think about what you need to know if you ran across the commit in a year from now.

## Merging

> **ProTip:** Altering published history is a common source of problems for anyone working on the project.

- Never rewrite history of the **master** branch or any other special branches.

- Before you merge your branch, rebase onto the branch its going to be merged to.

	```bash
	[my-branch] $ git fetch
	[my-branch] $ git rebase origin/master
	[my-branch] $ git checkout master

	[master] $ git merge my-branch
	```

- If your branch contains more than one commit, do not merge with a fast-forward.
	```bash
	# good 
	$ git merge --no-ff my-branch 

	# bad
	$ git merge my-branch
	```
