# Lesson 1 : Performance & Organization 
## Strategy & Structure

SH recommends to split the css between differents directories.
For example :

```
# Base
  – normalize.css
  – layout.css
  – typography.css

# Components
  – alerts.css
  – buttons.css
  – forms.css
  – list.css
  – nav.css
  – tables.css

# Modules
  – aside.css
  – footer.css
  – header.css
```
* **Base** : common styles and variables to be used across the entire website
* **Components** : styles for specific user interface elements which are broken down into different component files
* **Modules** : styles for different sections of a page

Influenced by *OOCSS* and *Scalable & Modular Architecture for CSS*

## Performance Driven Selectors

* Keep Selectors Short :

minimize specificity,improve efficiency

* Favor Classes

## Reusable Code :

Cut code that is used by multiple class in his own class (rounded corner for example)

## Minify & Compress Files

* Use gzip Compression on code
* Optimize Images :

   * Compress with PNGGauntlet
   * set the height and width tag on img

## Reduce HTTP Requests :

* Combine link to other files

For example just do a link to style.css, instead of multiple files.
This seems to be incompatible with the structure proposed at the beginning of the article.

I guess it needs to use a program to combine on save/push ?

* Make a Image Spritesheet

And navigate in it with `background-position`
