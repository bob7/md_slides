# md_slides Documentation

Run the python script on a markdown file produce html slides.

Supports:

- Latex macros and multiple slide types (customizable)
- tags for color, background, fonts, boxes etc. (customizable)
- multiple environments: theorem, lemma, definition, example etc. (customizable)
- javasript for interactive slides
- dynamic html imports
-  export pdf from the browser
  
## Command Options
```bash
python make.py file.md -o out.html
  -c          # center all slides
  -n          # show numbers
  --notitle   # no title slide
  --css file  # extra CSS
  --js file   # extra JS
```

## Slide Types
Start slide with keyword + `\n---\n`

- `center`: Centered dark slide  
  ```markdown
  center
  # Main Title
  Large centered text
  ---
  ```
- `thanks`: Thanks slide  
  ```markdown
  thanks
  # Thank You!
  - Q&A
  ---
  ```
- `iframe`: Include HTML (dark flex)  
  ```markdown
  iframe
  <iframe src="demo.html"></iframe>
  ---
  ```
- `frozen`: No page number  
  ```markdown
  frozen
  Hidden slide content
  ---
  ```
- `references`: References list  
  ```markdown
  references
  # References
  - [1] Author, Title
  ---
  ```

## Environment Blocks

### Theorems & Definitions
- `<thm>`: Theorem block  
  ```markdown
  <thm>
  Pythagoras: \(a^2 + b^2 = c^2\)
  </thm>
  ```
- `<thmc>`: Inline Theorem.  
  Ex: `<thmc> E=mc² </thmc>` → **Theorem.** E=mc²
- `<prop>`, `<propc>`: Proposition
- `<defi>`, `<defic>`: Definition
- `<fact>`, `<factc>`: Fact
- `<ex>`, `<exc>`: Example

### Questions
- `<quest>`: Question block (red label)  
  ```markdown
  <quest>
  Is P=NP?
  </quest>
  ```
- `<questc>`: Inline Question. 
- `<questce>`: Compact question block

### Box
- `<box>`: Light background box  
  ```markdown
  <box>
  Key point here
  </box>
  ```

## Inline Tags

### Color/Style
- `<r>`: red text  
  Ex: `<r>warning</r>` → <span style="color:#D15237">warning</span>
- `<rb>`: bold red  
  Ex: `<rb>ERROR</rb>` → <b style="color:#D15237">ERROR</b>
- `<g>`: green  
  Ex: `<g>success</g>` → <span style="color:#718c00">success</span>
- `<gw>`: light green  
  Ex: `<gw>note</gw>` → <span style="color:#8FC680">note</span>
- `<gb>`: bold green  
  Ex: `<gb>OK</gb>` → <b style="color:#718c00">OK</b>
- `<pur>`: purple bold large  
  Ex: `<pur>Title</pur>` → <b style="color:#B186C3;font-size:1.6rem">Title</b>
- `<ref>`: salmon  
  Ex: `<ref>[1]</ref>` → <span style="color:#E9967A">[1]</span>
- `<i>`, `<em>`: red italic-like  
  Ex: `<i>emphasis</i>` → <span style="color:#D15237">emphasis</span>
- `<b>`, `<strong>`: green bold  
  Ex: `<b>bold</b>` → <b style="color:#718c00">bold</b>

## KaTeX Macros
| Macro | Renders |
|-------|---------|
| `\RR` | \mathbb{R} |
| `\FF` | \mathbb{F} |
| `\CC` | \mathcal{C} |
| `\twome` | 2^{<\omega} |
| `\omel` | \omega^{<\omega} |
| `\ome` | \omega^{\omega} |
| `\Pone` | \mathsf{P1} |
| `\Ptwo` | \mathsf{P2} |
| `\twomel` | 2^{<\omega} |
| `\Nat` | \mathbb{N} |
| `\Rat` | \mathbb{Q} |
| `\ds` | \textup{\textsf{d}} |
| `\restr` | \upharpoonright |
| `\un` | \uparrow |
| `\de` | \downarrow |
| `\inv` | ^{-1} |
| `\pz` | \Pi^0_1 |
| `\pzt` | \Pi^0_2 |
| `\abs{...}` | \|{...}\| |
| `\dom` | \mathsf{dom} |
| `\DNC` | \mathsf{DNC} |
| `\tuple{...}` | \langle {...} \rangle |
| `\dbra{...}` | \llbracket {...} \rrbracket |
| `\sqbrad{...}{...}` | \{ {...} : {...} \} |

