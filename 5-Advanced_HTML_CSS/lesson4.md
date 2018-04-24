# Lesson 4 : Responsive Web Design
## Responsive Overview

**Responsive** : to react quickly and positively to any change

**Adaptive** : to be easily modified for a new purpose or situation, such as change

## Flexible Layouts

`vmin` `vmax` maximum or minimum between viewport height and width

From fixed unit to relative : the target width of an element / width of parent = relative width of target :
```
target/context = result
```
## Media Queries

*Example :* `@media all and (min-width: 320px) and (max-width: 780px)`

Logical Operator :
   * `and`
   * `not`
   * `only` : only for browser capable of handling media queries

### Media Features :
   * `width`, `height` & `max-..`, `min-..`
   * `orientation` : (`landscape` or `portrait`)
   * `aspect-ratio` & `max-..`, `min-..`  : Take a fraction width/height
   * `resolution` & `max-..`, `min-..`  : Take a value in dpi, dpx, dpcm

## Mobile First

This approach include using styles targeted at **smaller viewports** as the **default** styles for a website, then use** media queries **to add styles as the viewport **grows**.

## Viewport

Sometimes browser ignore the size of the viewport on loading (*How ?!*) so we have to use viewport like so :

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
`maximum-scale`,`minimum-scale` & `ìnitial-scale` : determine how the user can scale.

## Flexible Media

Trick to scale an embedded media (as youtube) according to the size of the window :
```css
figure {
  height: 0;
  padding-bottom: 56.25%; /* 16:9 */
  position: relative;
  width: 100%;
}
iframe {
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
}
```
