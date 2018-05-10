# Lesson 10 : Extending Semantics & Accessibility

## Semantic tagging
* `display: none` Should mostly be replaced by the **hidden attribute**.
* `strong` mean that the text is **important**, while `b` is purely stylistics.
* `em` mean that you put a **stressed emphasis** on the content, while `i` is
for using an **alternate tone** or to mark a text without altering it's meaning.
* `ins` means that the text has been **recently added** to the document, while
`u` is simply an **annotation**.

   **Avoid underline when it can be confused as a link.**
* `del` identify text **deleted or removed** from the document, and `s` element
that are **no longer accurate**.

   ins and del mays use `cite` specifying a resource that explains the change
   and `datetime` identifying when the content was removed from the document.

*  `mark` identify texts, specifically for reference purposes (by highlighting
   them).
* `<abbr title="HyperText Markup Language">HTML</abbr>` design an abbreviation
* Use `sub` and `sup` for subscript and superscript.

* `meter` is used to **measure a fixed value**, one that does not change over time.

   It may be used with the min, max, low(*low part*), high(*high part*),
   optimum(*most favorable part*), and value attributes.

* `progress` element indicates progress. It specifically represents the
completion of a task.

   It may be used with min, max and value.

* `time` element may be used with, or without, the datetime attribute, depending on how the text within the element is formatted. If the content is formatted with the correct time stamp then the datetime attribute may be omitted. Furthermore, if the time is representing the date or time of a publication the pubdate Boolean attribute should be used.
   ```html
   <time datetime="2011-08-24" pubdate>August 24th, 2011</time>
   ```
* `address` is used to hold any and only contact information.
* `code` is used for inline code sample, or in conjunction with pre as such :
   ```html
   <pre><code>body {
      color: #666;
      font: 14px/20px Arial, sans-serif;
   }</code></pre>
   ```
* `wbr` indicate where the word should break;
* `small` identify the text as a side comment (often a copyright information)
* **Quote :**
   * `cite` : Used to reference a creative work, author, or resource
   * `q` : Used for short, inline quotations
   * `blockquote` : Used for longer external quotations
* **Link :**
   * the `download` attribute tell the browser to download whats on the link.
     It can be a Boolean attribute or tell with which name the file should be
     downloaded

## Microdata

They are used to make information more easily readable for search engine and
browser.
The attribute `itemscope` must be placed on the parent of all relevant microdata.`itemtype=""` identify which vocabulary is used by the microdata. Most can be found [here](http://schema.org/docs/schemas.html).

We then can use `itemprop` to identify the property described by the element.

*Example of a **Person** Microdata :*
 ```html
 <section itemscope itemtype="http://schema.org/Person">
  <strong itemprop="name">Shay Howe</strong>
  <img src="shay.jpg" itemprop="image" alt="Shay Howe">
  <div itemprop="jobTitle">Designer and Front-end Developer</div>
  <a href="http://www.shayhowe.com" itemprop="url">shayhowe.com</a>
  <div itemprop="telephone">(555) 123-4567</div>
  <a href="mailto:shay@awesome.com" itemprop="email">shay@awesome.com</a>
  <address itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
    <span itemprop="streetAddress">600 W. Chicago Ave.</span>
    <span itemprop="addressLocality">Chicago</span>,
    <abbr itemprop="addressRegion" title="Illinois">IL</abbr>
    <span itemprop="postalCode">60654</span>
  </address>
</section>
```

*For more info :*
[http://diveintohtml5.info/extensibility.html](http://diveintohtml5.info/extensibility.html)

## WAI-ARIA

WAI-ARIA is used to define role that are not already implied by a tag.
