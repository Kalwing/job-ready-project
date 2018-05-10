# Lesson 5 : Preprocessors

## Haml (*HTML abstraction markup language*)

A html generator in Ruby.

doctype HTML5 :
```haml
!!! 5
```
Haml define block by indentation :
```haml
%body
   %header
      %h1 Hello !
   %section
      %p
         I'm here.
```
Attributes are between `()` :
```haml
%img(src="shay.jpg" alt="Shay Howe")
```
Classe & ID may also be added like this :
```haml
%section#hello.feature(role="region")
```
if a class or an ID is used on a `%div`, the div can be omitted
The text can be escaped by adding a `\`, otherwise it may be executed as Ruby
```haml
.author
  = @author
  \= @author
```
```html
<div class="author">
  Shay Howe
  = @author
</div>
```

## SCSS & SASS

Pour generer css a chaque sauvegarde :
```
sass --watch styles.sass:styles.css
```
or for a whole folder :
```
sass --watch assets/sass:public/css
```

### Basic syntax

```scss
.new {
  color: #ff7b29;
  font-weight: bold;
  span {
    text-transform: uppercase;
  }
}
```
```sass
.new
  color: #ff7b29
  font-weight: bold
  span
    text-transform: uppercase
```

They use nesting for selectors but also for properties :
```sass
div
  font:
    family: Baskerville, Palatino, serif
    style: italic
    weight: normal
```

`&` refer to the parent selector :
```sass
a
   color: #0087cc
   &:hover
      color: #ff7b29
```

Variable are prefixed by a `$` as such `$fontSize: 1em`

An **hex color** can be used in **rgba** and math can be used on a color.

### OOP like :
A selector can be an extension of another :
```sass
h2
  color: #9c6
  span
    text-decoration: underline

.sub-heading
  @extend h2
```
Constructor with mixin :
```sass
@mixin btn($color, $color-hover)
  color: $color
  &:hover
    color: $color-hover

.btn
  +btn($color: #fff, $color-hover: #9799a7)
```
(in SCSS the + is remplaced by `@include`)
```css
.btn {
  color: #fff;
}
.btn:hover {
  color: #9799a7;
}
```
We can also specify default argument as in Python.

### Fix the folder issue

To compile multiple files in one, we can use `@import "other.css"` at the top of the main one.

### Conditional, iterative..

**If :**
```sass
$shay: awesome

.shay
  @if $shay == awesome
    background: #ff7b29
  @else if $shay == cool
    background: #0087cc
  @else
    background: #333
```
```css
.shay {
  background: #ff7b29;
}
```
**For :**

`through` include the last one, `to` doesn't
```sass
@for $col from 1 to 3
    .col-#{$col}
    width: 40px * $col
```
```css
.col-1 {
  width: 40px;
}
.col-2 {
  width: 80px;
}
```
**Each :**

```sass
@each $class in uxd, rails, html, css
   .#{$class}-logo
   background: url("/img/#{$class}.jpg")
```
**While :**
```sass
$heading: 1
@while $heading <= 6
  h#{$heading}
    font-size: 2em - ($heading * .25em)
  $heading: $heading + 1
```
