# Lesson 2 : Detailed Positioning
## Containing Floats

Various method to clear float :
* `overflow: auto`
* Clearfix :
   ```css
   .group:before,
   .group:after {
     content: "";
     display: table;
   }
   .group:after {
     clear: both;
   }
   .group {
     *zoom: 1;
   }
   ```
   The before and the zoom are mostly here for compatibility with IE7 & 8. Good to know.

   A common name for a clearfix class is **group**.

## Position Property

* Fixed footer
   ```css
   footer {
     bottom: 0;
     left: 0;
     position: fixed;
     right: 0;
   }
   ```
   The left and right property allow the footer to not disturb the box model.
