# Lesson 3 : Complex Selectors


*** DISCLAIMER :  *** Always check for Browser compatibility when using selectors

## Sibling Selectors



* **General Sibling Selector `~`:**

   *Example : *
   ` h2 ~ p` looks for p elements that follow, and share the same parent, of any h2 elements. The p element must come after any h2 element to be selected.

* **Adjacent Sibling Selector `+`:**

   *Example : *
   ` h2 + p` looks for  p elements that directly follow a h2 elements.

## Attribute Selectors

* **Attribute Present Selector** :

   *Example : *
   `img[alt]` looks for image with an alt

* **Attribute Equals Selector** :

   *Example : *
   `a[href="http://google.com/"]` looks for links pointing to google

* **Attribute Contains Selector**

   *Example : *
   `a[href*="login"]` looks for links containing a login

* **Attribute Begins With Selector**

   *Example : *
   `a[href^="https://"]` looks for links beginning by https

* **Attribute End With Selector**

   *Example : *
   `a[href$=".pdf"]` looks for links to pdf Files

* **Attribute Spaced With Selector**

   *Example : *
   `img[alt~="one"]` looks for image containing the word "one"

* **Attribute Spaced With Selector**

   *Example : *
   `a[lang|="en"]` looks for link where lang contain a en hyphenated. for example `lang="en-US"`

## Pseudo-classes

`:link` link that hasn't been visited

`:visited` otherwise


`:enabled` and `:disabled` select element that has been disabled or not

`:checked` select cheked radio buttons or checkboxes that has been checked, `:indeterminate` select one where the user hasn't done anything yet.

`:first-child`, `:last-child`, & `:only-child`

`:first-of-type`, `:last-of-type`, & `:only-of-type`

`:nth-child(n)`, `:nth-last-child(n)`, `:nth-of-type(n)`, & `:nth-last-of-type(n)` :

   * n in the format `an+b`. That means that `:nth-child(3n)` select every third child.
      * If there's no `a`, it select every element starting with `b` (`li:nth-child(n+5)`)
      * If `a` or `n` < 0, it select from b to 0 according to a. (`:nth-child(-n+9)`)

`:empty` select element containing no child or text

`:not()` select an element that is not what's inside the parenthesis

`:target` will select the element currently targeted. For exemple : `http://a.com#hello` will select the element with an `#hello` ID.

## Pseudo-elements

* **Textual Pseudo-elements :**
   * `:first-letter`

   * `:first-line`

* **Fragment Pseudo-elements**
   * `::selection` slect what's highlighted by the user
