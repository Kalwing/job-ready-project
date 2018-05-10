# Lesson 7 : Transforms

## About longevity

You should keep the vendor prefix for now:
```css
-webkit-transform: scale(1.5);
   -moz-transform: scale(1.5);
     -o-transform: scale(1.5);
        transform: scale(1.5);
```
 ## 2D

 * `rotate(deg)`
 * `scale(1, [1])`, `scaleX(1)` & `scaleY(1)`
 * `translate(px, px)`, `translateX(px)` & `translateY(px)`
 * `skew(deg, deg)`, `skewX(deg)` & `skewY(deg)`

 Transform can be combined by separating the property with a space.

## Transform origin

Set the origin of the transform; used like this :`transform-origin: % %`

## 3D
### Perspective

Need to be set for the 3D to work : `perspective(200px)`
`perspective-origin: % %` work the same way as `transform-origin`

### 3D Transform

* `rotateX(deg)`, `rotateY(deg)` & `rotateZ(deg)`
* `scaleZ(deg)`
* `translateZ(deg)`

### Transform Style

 `transform-style:` take `preserve-3d` or `flat`.
 It allow the children of a transformed object to keep it's 3d space, or to be
 flattened on the parent.

### Backface Visibility

`backface-visibility` allow us to choose to display or to not display the back
side of an object. Take `hidden` or `visible`(default).
