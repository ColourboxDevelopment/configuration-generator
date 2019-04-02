# Configuration generator

In order to be GDPR compliant we must store passwords as encrypted strings in parameter store. To make this bearable when writing configuration files, I've made this program to grab keys in parameter store and fill them in.

Let's say you have this configuration template file:
```php
<?php
return [
	'pass' => '{{/DB/Metaeskuel/Jonna/Password}}'
];
```

you can then run `pipenv run python3 render.py config.template.php config.php` which will result in `{{/DB/Metaeskuel/Jonna/Password}}` being filled out with the password stored in parameter store resulting in
```php
<?php
return [
	'pass' => 'ILiekTurtel!'
];
```
