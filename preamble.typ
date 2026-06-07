#import "@preview/codly:1.3.0": *


#let template(
  body,
  title: [Labb],
  logo: none,
) = {
  set page(
    paper: "a4",
    margin: (x: 22mm, top: 22mm, bottom: 20mm),
  )
  show heading.where(depth: 1): set text(
    font: "Exo",
    weight: 700,
    size: 23pt,
  )

  show heading.where(depth: 2): set heading(numbering: (..) => h(-.3em))
  show heading.where(depth: 2): set text(font: ("Open Sans", "Liberation Sans"), weight: 700, size: 14pt)

  show heading.where(depth: 3): set text(font: ("Open Sans", "Liberation Sans"), weight: 700, size: 11pt)
  show heading.where(depth: 3): set heading(numbering: (.., level, last) => str(level) + "." + str(last))

  set text(font: ("Open Sans", "Liberation Sans"), size: 10.5pt, weight: 300)

  show: codly-init.with()
  codly(fill: luma(98%))

  show raw.where(block: false): it => box(fill: luma(96%), inset: (x: 3pt, y: 0pt), outset: (x: 0pt, y: 3pt), text(
    fill: purple.darken(30%),
    it,
  ))

  set list(indent: .7em, body-indent: .5em, spacing: .8em)

  box(
    stroke: 3pt + color.rgb("#ffc600"),
    inset: 10pt,
    outset: (x: 30pt),
    radius: 10pt,
    fill: color.rgb("#02005b"),
    table(
      columns: (1fr, auto),
      stroke: none,
      align(heading(depth: 1, text(fill: white, title)), horizon), image(logo, height: 5em),
    ),
  )
  v(1em)
  body
}
