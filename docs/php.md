# Style Guide for PHP

## Overview

The guide follows the PSR-2 coding standard and the PSR-4 autoloading standard.

## Contents

1. [General](#general)
2. [Indentation and whitespace](#indentation-whitespace)
3. [Brackets and braces](#brackets-braces)
4. [Spaces](#spaces)
5. [Directories, files and namespaces](#directories-files-namespaces)
6. [Classes](#classes)
7. [Commenting](#commenting)
8. [Data structures](#data-structures)
9. [PHP Coding Standards Fixer](#php-cs-fixer)


<div id="general"></div>

### General

#### PHP Tags

The first line of all `.php` files should be exactly "`<?php`".

Never use the closing PHP tag (`?>`).

Never use PHP short tags.

```php
#bad
<?= //...

#good
<?php //...
```

#### Character Encoding

All files must only use `UTF-8`, without `BOM`.

#### Date and Time

> **Coordinate Universal Time** (French: *Temps universel coordonne*), abbreviated to **UTC**,
is the primary time standard by which the world regulates clocks and time. [Read more](3)

Always use UTC timezone to store date and time.

#### Files

> Every `.php` file should be side effect free.

**A file should declare new symbols** (classes, functions, constants, etc.) and cause no side effects,
**or should execute logic with side effects**, but **should not do both**.

> Every `.php` php file should only contain one class declaration.

The following is an example of what to avoid.

```php

//side effects; changes ini settings
ini_set('display_errors', '1');

//declaration
function getCurrentTime()
{
	//
}

//class declaration
class Product
{
	//
}

//another class declaration
class ProductCategory
{
	//
}

//side effects; includes a file
include "helpers.php";
```

The following is an example of what to emulate.

```php
//conditional declaration is *not* a side effect
if (function_exists('getCurrentTime')) {

	function getCurrentTime()
	{
		//
	}
}
```


- Never use global variables, except for superglobals.
- Properties should always be declared.
- Variables SHOULD always be declared at the top of the block they are used in.

<div id="indentation-whitespace"></div>

### Indentation and whitespace

- Use the tab character for indentation, set to 4 columns wide.
- Avoid "double-indenting" blocks of code where no indentation is necessary for readability.
- Do not leave whitespace at the end of lines.
- Be as strict as is sensible to enforce 80 character lines.
- Limit to four levels of indentation.

<div id="brackets-and-braces"></div>

### Brackets and braces

- Opening and closing braces should always be placed at the start of their own line.
- One level of indentation should be applied within, and only within, the braces.
- Conditionals within brackets should not gain extra indentation when breaking onto separate lines.
- Never leave conditional statements unbraced or unindented.

<div id="spaces"></div>

### Spaces

- No extra space should be placed after a control structure keyword or function name.
- Opening brackets should not have a space after, closing brackets should not have a space before.
- Commas separating variable lists should have a space or newline after, no whitespace before.
- A space should surround binary and ternary, but not unary operators.

<div id="directories-files-namespaces"></div>

## Directories, files and namespaces

- Directories and file must be namespaced-mapped.
- Namespaces must map to file paths as per PSR-4.
- Namespace-mapped files and directories must use `UpperCamelCase`.
- There must be one blank line after the `namespace` declaration.
- When present, `use` declarations go after the `namespace` declaration.
- There must be one `use` keyword per declaration.
- There must be one blank line after `use` declarations.

<div id="classes"></div>

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

<div id="commenting"></div>

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

<div id="php-cs-fixer"></div>

### PHP Coding Standards Fixer

> A tool to automatically fix PHP coding standards issues. - [sensiolabs](1)

To use PHP-CS-Fixer:

- Installation (via composer)

	```bash
	$ composer global require friendsofphp/php-cs-fixer
	```
- Make sure you have the global composer binaries in your `PATH`.

	```bash
	$ export PATH="$PATH:$HOME/.composer/vendor/bin"
	```

- Run the fixer against the file or directory.

	```bash
	$ php php-cs-fixer.phar fix /path/to/file
	$ php php-cs-fixer.phar fix /path/to/dir
	```

- If you want to pair it with your favorite text editor, [dedicated plugins](2) exist for just this.

[1]: http://cs.sensiolabs.org
[2]: http://cs.sensiolabs.org/#helpers
[3]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time
