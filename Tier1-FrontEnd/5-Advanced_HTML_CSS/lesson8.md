# Lesson 8 : Transitions & Animations
## Disclaimer :
All transition related property should use vendor prefix.

## Transition
Properties :
* `transition-property` : the property on which the transition apply (Example : `background-color`) or `all`
* `transition-duration` : duration in `s` or `ms`.
* `transition-timing-function` : linear, ease-in, ease-out, ease-in-out.
* `transition-delay` : time before the beginning of the transition in `s` or `ms`

Multiple value separated by a "," will be affected to the `transition-property` on the same order.

The shorthand property `transition` take parameter in the order listed here (`transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`).

## Animations
They use the `@keyframe` rule.

Example :
```css
@keyframes slide {
  0% {
    left: 0;
    top: 0;
  }
  50% {
    left: 244px;
    top: 100px;
  }
  100% {
    left: 488px;
    top: 0;
  }
}
```

To work, the element should have its `animation-name` property set to the animation name, and a `animation-duration` set.

`animation-timing-function` & `animation-delay` may also be used.

`animation-iteration-count` make the animation repeat. It takes an integer or `infinite`

`animation-direction` take `normal`, `reverse`, `alternate` & `alternate-reverse`

`animation-play-state` take `running` or `paused`

The shorthand property work like this : `animation-name`, `animation-duration`, `animation-timing-function`, `animation-delay`, `animation-iteration-count`, `animation-direction`, `animation-fill-mode`, and lastly `animation-play-state`.
