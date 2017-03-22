# Style Guide for PHP

## Overview

The guide follows the PSR-2 coding standard and the PSR-4 autoloading standard.

### PHP-CS-Fixer

> The [PHP-CS-Fixer](https://github.com/FriendsOfPhp/PHP-CS-Fixer) fixes *most* issues in your code. 

This tool detects and fixes PHP code style issues.

To use PHP-CS-Fixer:

- Install via composer
- Run the fixer against the directory. 

To tailor it to your personal experience, consider a plugin:

- [Atom](https://github.com/Glavin001/atom-beautify)
- [Sublime Text](https://github.com/benmatselby/sublime-phpcs)
- [Vim](https://github.com/stephpy/vim-php-cs-fixer)

## Concepts of this styleguide

### General concepts

- The first line of all `.php` files should be exactly "`<?php`".
- Never use the closing PHP tag (`?>`).
- Never use PHP short tags.
- All files must only use `UTF-8`, without `BOM`.
- Always use UTC timezone to store date and time.
- Every `.php` library file should contain one class exactly.
- Every `.php` library file should be side effect free.
- Singular words (e.g. item, stylesheet, user) should be used throughout files and code instead of plurals.
- Avoid Hungarian Notation, where file/variable names that indicate their type.
- Never use global variables, except for superglobals.
- Properties should always be declared.
- Variables should always be declared at the top of the block they are used in.

### Indentation and whitespace

- Use the tab character for indentation, set to 4 columns wide.
- Avoid "double-indenting" blocks of code where no indentation is necessary for readability.
- Do not leave whitespace at the end of lines.
- Be as strict as is sensible to enforce 80 character lines.
- Limit to four levels of indentation.

### Brackets and braces

- Opening braces should always be placed at the start of a new line.
- Closing braces should always be placed at the start of their own line.
- One level of indentation should be applied within, and only within, the braces.
- Conditionals within brackets should not gain extra indentation when breaking onto separate lines.
- Never leave conditional statements unbraced or unindented.

### Spaces

- No extra space should be placed after a control structure keyword or function name.
- Opening brackets should not have a space after, closing brackets should not have a space before.
- Commas separating variable lists should have a space or newline after, no whitespace before.
- A space should surround binary and ternary, but not unary operators.

## Directories, files and namespaces

- Directories and file must be namespaced-mapped.
- Namespaces must map to file paths as per PSR-4.
- Namespace-mapped files and directories must use `UpperCamelCase`.
- There must be one blank line after the `namespace` declaration.
- When present, `use` declarations go after the `namespace` declaration.
- There must be one `use` keyword per declaration.
- There must be one blank line after `use` declarations.

### Classes

- The term "class" refers to all; classes, interfaces and traits.
- Class names should be declared in `PascalCase`.
- A class should only be autoloaded - never use `require` or `include`.
- Constants should only be declared on a class.
- Constants should use `UPPERCASE_UNDERSCORED`.
- Properties should use `$camelCase`.
- Methods should use `camelCase()`.
- All parameters should define their type where possible.
- Methods should avoid becoming longer than 20-50 lines.
- Classes should have all or no static methods.
- Visibility must be declared on all properties and methods.
	- `abstract` and `final` should be declared before the visibility.
	- `static` should be declared after the visibility.

### Commenting

- For inline comments, double-slash comments (`//`) should be used.
- Inline comments should have no indentation, starting from column 1.
- Inline comments can span multiple lines, prefixed with the double-slash.
- Block comments should only be used to provide class and method documentation in the form of doc blocks.
- Comments, along with docblocks, should be sparse and punchy to avoid stale documentation.

### Data structures

- Associative arrays should only be used for simple key-value-pairs.
- Move associative arrays to an object's getter/setter storage where possible.
- Static classes should only be used when truly stateless.
- Private functions should be preferred over anonymous functions where appropriate.
- Anonymous functions should never exceed 5 lines.

## Credits

- [PhpGt styleguide](https://github.com/PhpGt/StyleGuide)
- [CodeGuide by PixelUnion](https://github.com/PixelUnion/code-guide)
