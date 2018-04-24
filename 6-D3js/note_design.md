# Note on design :
## How to choose a Chart :

Think about the number of dimension I have in my data, and of which type is
   each data (continuous/categorical)

### Line plot or Scatter plot ?
 * Line plot if each data is an evolution of the precedent (evolution of money, sound..)
 * Scatter otherwise

### The primordial charts :
"Signal vs Noise"'s *Noah Lorang* 3 charts:
* **Line chart** : To show how much something changed over a variable
* **Histogram** : To show something is distributed
* **Table** : to display summary information

Udacity's Course teacher 3 charts :
* **Scatter Plot** : To represent relationship between variable
* **Grouped bar Chart / Stack Bar Plot** : To represent comparison / the total of subgroup of a category
* **Line Chart** : To show a trend

### Fun one to think about :
 * **Bullet Graph** (*meter with a target or other information in the form of a background*)
 * **Sparkline**   (*Line plot on a single line of data*)
 * **Cycle Plots** (*Fractioned line plot*)
 * **Connected scatter plot** (*scatter plot with a third variable as an anotation*).
   See this [link](http://www.thefunctionalart.com/2012/09/in-praise-of-connected-scatter-plots.html) for an exemple. I really **love** them.

## Good design practices
### Pre-attentive Attributes
They are attributes that immediately distinguish a data from the rest.

Four type :
   * Color (hue/intensity)
   * Movement
   * Form
   * Spacial Position

### Use Negative Space
### Be careful with redundant encoding

First see if your graphic needs color by viewing it in black and white.

If you need color use pastel or medium color.

Color should Highlight what you want.

### Rules about colors :
1. If you want** different objects** of the **same color** in a table or graph
to look the same, make sure that the **background**—the color that surrounds
them—is **consistent. **
2. If you want objects **in a table or graph** to be easily seen, **use a
background color that contrasts** sufficiently with the object.
3. Use color **only** when needed to serve a particular communication **goal**
4. Use** different colors** only when they correspond to **differences of
meaning** in the data.
5. Use soft,**natural** colors to display **most** information and **bright
and/or dark** colors to **highlight** information that requires greater
attention
6. When using color to encode a **sequential** range of *quantitative* values,
stick with a **single hue** (or a small set of closely related hues) and **vary
intensity** from pale colors for low values to increasingly darker and brighter
colors for high values

   i.e. : **AVOID RAINBOW PALETTE**
7. **Non-data** components of tables and graphs should be displayed **just
visibly enough** to perform their role, but no more so, for excessive salience
could cause them to distract attention from the data

Components | Colors |
       --- | ---
Axis lines | Use thin gray lines of medium intensity.
Borders    | Whether around the graph as a whole, its plot area, or a legend, when borders are needed (and usually they are not), use thin gray lines of medium intensity.
Background | Use white (or in Excel select “None” for color)
Bars       | Use a distinct hue of medium intensity for each data series.
Lines      | For thin lines, use a distinct hue of fairly high intensity for each; otherwise, use distinct hues of medium intensity.
Data Points| For small points, use a distinct hue of fairly high intensity for each; otherwise, use distinct hues of medium intensity

8. To guarantee that most people who are colorblind can distinguish groups
of data that are color coded, **avoid** using a combination of **red and green** in
the same display
9. **Avoid using visual effects** in graphs.

[Source : Stephen Few](http://www.perceptualedge.com/articles/visual_business_intelligence/rules_for_using_color.pdf)

## Strive for a minimalistic graph (low data to ink ratio)

## Do not lie (keep a low lie factor)
