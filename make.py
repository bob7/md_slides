#!/usr/bin/env python3

# python make.py -n nankai25.md -o xx.html

from marko.ext.gfm import gfm
import argparse
import re
import sys
import errno

minislides = """
@import url('https://fonts.googleapis.com/css?family=Red+Hat+Text&display=swap');
@import url('https://fonts.googleapis.com/css?family=Overlock&display=swap');

:root {
	--background-light: #fdfdfd;
	--background-dark: #333; 
	--text-dark: #444;
	--box-vlight:#f6f6f6; 
	--box-light:#f0f0f0; 
	--green: #718c00;
    - greenwhite: #A8D2A2;
	--green1:#579C37;
	--green2:#579C50;
	--green3:#16A085;
	--green4:#60A93E;
	--green5: #619E45;
	--red:#D15237;
	--red1:#CD5C5C;
	--red2:#E76662;
	--red3: #b22;
	--red4: #C8472D;
	--red5: #D6644D;
	--red6: #D15237;
	--purple-pink:#CA5D7D;
	--purple-dark:#885DCA;
	--purple2:#AF77DE;
	--blue: #4271ae;
	--blue-fade:#5D93CA;
	--orange: #f5871f; 
	--gray-light: #bbbbbb;
} 

* {box-sizing:border-box; }

body {background: #444;}

@media print {

* {box-sizing:border-box;}

body {
	background: none; 
	margin: 0rem auto 0rem auto !important;
}
.slides {
	margin: auto auto auto auto !important;
}

.slides section {
	box-sizing:content-box; 
	height: 775px !important;
	width: 1040px !important;
	border: 1px solid #eee !important;
	border-radius:15px;
	margin: 0rem auto 0rem auto !important;
	padding-top:0rem !important;
	padding-bottom:0rem !important;
	page-break-after: always;
	page-break-inside: avoid;
}
.slides section:nth-child(1) {margin-top: 0px;} 

.slides section::after {
	position: absolute;
	bottom:1rem !important;
	right:1.5rem !important;
	counter-increment:section;
	content: counter(section) '/20';
	font-size: 1rem;
	color: var(--text-dark);
	opacity: 0.7;
} 

.slides section:nth-child(1)::after {
	counter-increment: none;
	content:'';
}
}

.slides {
	color:#444; 
	font-size:1.7rem;
	position:center;
	margin-top:1rem;
	counter-reset: section;
}

.slides h1, .slides h2,  .slides p, .slides blockquote {
	text-align: left; 
	-webkit-hyphens: auto; 
	-moz-hyphens: auto; 
	-ms-hyphens: auto; 
	hyphens: auto; 
	width: 90%; 
	max-width: 90%; 
}

.slides h1 {
	padding: 4rem 0 1rem 0; 
	font-size:3rem; 
	opacity:0.85;
	box-shadow: inset 0 -3px var(--gray-light);
}

.slides h2 {
	font-size:2.5rem; 
	padding-bottom:0.1rem; 
	position: flex;
	opacity:0.85;
}

.slides ul, .slides ol { 
	-webkit-hyphens:auto; 
	-moz-hyphens:auto; 
	-ms-hyphens:auto;hyphens:auto; 
	width:100%; 
	margin:0.1rem 0; 
	line-height:1.7em;
	padding-top:0.5rem;
	padding-bottom:0.2rem;
}

.slides li {hyphens:none; margin-left: 2rem;}

.slides section {
	position: relative;
	box-sizing:content-box; 
	height: calc(100vh - 6rem);
	width: calc((100vh - 4rem) * 1.284);
	border: 1rem solid #444;
	margin: 1rem auto 1rem auto;
	padding: 2rem 4rem 1rem 4rem; 
	background: var(--background-light);
	font-family:"Overlock";
}

.slides section:nth-child(1) {margin-top: 0px;} 

.slides section::after {
	position: absolute;
	bottom:1rem;
	right:1.5rem;
	counter-increment:section;
	content: counter(section) '/20';
	font-size: 1rem;
	color: var(--text-dark);
	opacity: 0.7;
} 


.slides section:nth-child(1)::after {
	counter-increment: none;
	content: '';
}

.slides .frozen {
}

.slides .frozen::after {
	counter-increment: none;
}

.slides .includehtml {
	background: #fefefe;
	box-sizing:content-box; 
	background:#333;
	display: flex; 
	flex-direction: column; 
}

.slides .includehtml  h3 {
	color:#eee; 
	font-weight:bold; 
	font-size:3.5rem;
    padding-top:4rem;
} 

.slides .includehtml  ul {
	color:#eee; 
	font-size:2rem;
	text-align:left;
} 

.slides .includehtml::after {
	counter-increment: none;
	content: '';
}

.slides .thanks {
	background:#333;
	box-sizing:content-box; 
	height: calc(100vh - 6rem);
	width: calc((100vh - 4rem) * 1.284);
	border: 1rem solid #444;
	margin: 1rem auto 1em auto;
	padding: 2rem 4rem 1rem 4rem; 
	display: flex; 
	flex-direction: column; 
    color:#eee; 
}

.slides .thanks::after {
	counter-increment: none;
	content: '';
}

.slides .thanks  xthanks {
    display:block;
    align-items:center;
	color:#bbb; 
    text-align:center;
    font-size:1.8rem;
    margin-left:auto; margin-right:auto;
    padding-bottom:4rem;
        padding-left:2rem;
} 

.slides .thanks  ul {
    padding-left:1rem;
    padding-bottom:1rem;
    margin-top:0rem;
	color:#bbb; 
    font-size:1.6rem;
} 

.slides .thanks  li {
	color:#bbb; 
} 

.slides .thanks  h2 {
	color:#eee; 
    padding-top:5rem;
    margin-left:auto; margin-right:auto;
	padding-bottom:1rem; 
	font-weight:bold; 
	text-align:center; 
	font-size:3.5rem;
} 

.slides .references {
	background:#333;
	box-sizing:content-box; 
	height: calc(100vh - 6rem);
	width: calc((100vh - 4rem) * 1.284);
	border: 1rem solid #444;
	margin: auto auto auto auto;
	padding: 1rem 4rem 1rem 4rem; 
	display: flex; 
	flex-direction: column; 
    color:#ddd; 
}

.slides .references::after {
	counter-increment: none;
	content: '';
}
    
.slides .references  ul {
    padding-left:1rem;
    padding-bottom:0.6rem;
    margin-top:0rem;
	color:#ddd; 
    font-size:1.4rem;
    padding-top:0;
} 

.slides .references  li {
	color:#ddd; 
} 

.slides .references  h2 {
	color:#eee; 
	font-size:2.4rem;
    font-weight:bold;
} 

.slides .centered {
	background:#333;
	box-sizing:content-box; 
	height: calc(100vh - 6rem);
	width: calc((100vh - 4rem) * 1.284);
	border: 1rem solid #444;
	margin: 1rem auto 1em auto;
	padding: 2rem 4rem 1rem 4rem; 
	display: flex; 
	flex-direction: column; 
    color:#eee; 
}

.slides .centered::after {
	counter-increment: none;
	content: '';
}

.slides .centered  h2 {
	color:#fff; 
	margin:auto;
	padding-bottom:4rem; 
	font-weight:bold; 
	text-align:center; 
	font-size:3.5rem;
} 

.slides .centered  h3 {
	color:#eee; 
	font-weight:bold; 
	font-size:3rem;
    padding-bottom:1rem;
        padding-top:3rem;
} 

.slides .centered  ol {
    display:block;
	color:#eee; 
	font-size:2rem;
	text-align:left;
    padding-left:4rem;
} 

.slides .centered  ul {
	color:#eee; 
	font-size:2rem;
	text-align:left;
} 

.slides.numbered {
	counter-reset: section;
} 

.slides.numbered section::after {
	position: absolute;
	bottom: 1rem;
	right:1.5rem;
	counter-increment:section;
	content:counter(section);
	font-size: 1rem;
	color: var(--text-dark);
	opacity: 0.7;
} 

.slides.numbered section:nth-child(1)::after {
	counter-increment: none;
	content: '';
}

.slides .subtitle {margin: 1rem 0;font-size: 2rem; opacity: 0.7;}
.slides .author {margin: 4rem 0 0 0;font-size: 2rem; opacity: 0.7; font-weight:bold;}
.slides .coauthors {margin: 0.2rem 0 0 0; opacity: 0.6;}
.slides .affiliation {margin: 0.8rem 0; opacity: 0.7; color:rgb(10,90,5);font-weight:bold;}

.slides thm, .slides thmc, 
.slides prop, .slides propc, 
.slides defi, .slides defic, 
.slides fact, .slides factc, 
.slides quest, .slides questc,  
.slides ex, .slides exc, .slides box {
	display:block; 
	background-color:var(--box-vlight); 
	border:0.1em #ddd solid; 
	border-radius:15px; 
	color:#444; 
	text-align:left; 
	margin:2rem 1rem 2rem 1rem; 
	padding:1rem 1.5rem 0.5rem 1.5rem; 
	width:90%; 
	line-height:1.4em; 
	hyphens:none;
	font-family:"Overlock"; 
}

.slides questce {
	display:block; 
	border:0.1em #ddd solid; 
	border-radius:15px; 
	color:#444; text-align:left; 
	margin:1rem; 
	padding:1rem 1.5rem 1rem 1.5rem; 
	width:90%; 
	line-height:1.4em; 
	hyphens:none;
}

.slides thm::after, .slides thmc::after, 
.slides prop::after, .slides propc::after, 
.slides defi::after, .slides defic::after, 
.slides fact::after, .slides factc::after, 
.slides quest::after, .slides questc::after, .slides questce::after,  
.slides ex::after, .slides exc::after, .slides box::after {margin:0.5rem;}

.slides thmc::before,
.slides propc::before,  
.slides defic::before,
.slides factc::before,
.slides exc::before {font-weight:bold; color:var(--green);}

.slides questc::before,
.slides questce::before {font-weight:bold; color:var(--red);}

.slides thm::before, 
.slides prop::before, 
.slides defi::before,
.slides fact::before,
.slides quest::before, 
.slides ex::before {padding-bottom:0.3rem; display:block; font-weight:bold; color:var(--green);}

.slides thm::before{content:"Theorem";}
.slides prop::before{content:"Proposition";}
.slides defi::before{content:"Definition";}
.slides fact::before{content:"Fact";}
.slides quest::before{content:"Question";}
.slides ex::before{content:"Example";}

.slides thmc::before{content:"Theorem. ";}
.slides propc::before{content:"Proposition. ";}
.slides defic::before{content:"Definition. ";}
.slides factc::before{content:"Fact. ";}
.slides questc::before{content:"Question. ";}
.slides questce::before{content:"Question. ";}
.slides exc::before{content:"Example. ";}

.slides thm ul, .slides thmc ul, .slides box ul,
.slides prop ul, .slides propc ul, 
 .slides defi ul, .slides defic ul, 
.slides fact ul, .slides factc ul,
.slides quest ul, .slides questc ul, .slides questce ul, 
.slides ex ul, .slides exc ul {padding-top:0.5rem;}

.slides thm ul li, .slides thmc ul li, 
.slides box ul li, .slides prop ul li, 
.slides propc ul li, .slides defi ul li,
.slides defic ul li, .slides fact ul li, 
.slides factc ul li, .slides quest ul li, 
.slides questc ul li, .slides questce ul li, .slides ex ul li, 
.slides exc ul li {margin-left:0em; line-height:3rem; }

.slides r {color:var(--red); font-weight:normal;}
.slides rb {color:var(--red); font-weight:bold;}
.slides g {color:var(--green);}
.slides gw {color:#8FC680;}
.slides pur {color:#B186C3; font-weight:bold; font-size: 1.6rem;}
.slides ref {color:#E9967A;}
.slides gb {color:var(--green); font-weight:bold;}

.slides p {hyphens:none;  margin:0.2rem 0; line-height:1.3em;}
.slides i, .slides em {color:var(--red); font-style:normal;}
.slides b, .slides strong {color:var(--green);}
.slides code, .slides pre {font-family:'Fira Code', monospace;font-size:1.2rem;background:none; width:80%;}
.slides p code, .slides ul code, .slides ol code {color:var(--blue);}
.slides pre {text-align:left;max-width:100%;}
.slides pre code {margin:1rem 0;overflow-x:scroll;}
.slides a {text-decoration:none;color:var(--blue);}
.slides img {padding-top:2rem; width:95%;}
.slides img.large {max-width:100%;max-height:100%;}
.slides table {margin:1rem 0; overflow:scroll; border-collapse:collapse;}
.slides th, .slides td {padding:0.2rem 0.5rem;}
.slides thead {border-bottom:2px solid var(--text-dark);}
.katex {font-size:1em !important;}
"""

# Minified js for keyboard navigation
navigation = """
var slides=document.getElementsByTagName("section");
var totalSlides=slides.length;
var prev=[37,75,72];
var next=[39,74,76,13];
var start=[48];var end=[57];

function percentageVisible(element){
	const viewHeight=(window.innerHeight||document.documentElement.clientHeight);
	const bounds=element.getBoundingClientRect();
	if(bounds.bottom<0||bounds.top>viewHeight){return 0;}
	if(bounds.top<0&&bounds.bottom>viewHeight){return bounds.height*100/viewHeight;}
	else if(bounds.top<0){return bounds.bottom*100/viewHeight;}
	else if(bounds.bottom>viewHeight){return(viewHeight-bounds.top)*100/viewHeight;}
	return 100;
}

function getCurrentSlide(){
	var index=0;
	var maxPercent=0;
	for(var i=0;i<totalSlides;i++){
		let p=percentageVisible(slides[i]);
		if(p>maxPercent){index=i; maxPercent=p;}
	}
	return index;
}

function navigate(nextSlide){
	let target=nextSlide;if(nextSlide<0){target=0;}
	else if(nextSlide>=totalSlides){target=totalSlides-1;}
	window.scrollTo(0,slides[target].offsetTop-8);
}
document.addEventListener("keydown",event=>{
	let code=event.keyCode;
	let currentSlide=getCurrentSlide();
	if(prev.includes(code)){navigate(currentSlide-1);}
	else if(next.includes(code)){navigate(currentSlide+1);}
	else if(start.includes(code)){navigate(0);}
	else if(end.includes(code)){navigate(totalSlides-1);}
});
"""

# Katex settings
katex = r"""
document.addEventListener("DOMContentLoaded", function() {renderMathInElement(document.body, {
delimiters:[{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}, 
{left: '\\(', right: '\\)', display: false}, {left: '\\[', right: '\\]', display: true}],
macros: {'\\RR': '\\mathbb{R}', 
'\\FF': '\\mathbb{F}',
'\\CC': '\\mathcal{C}', 
'\\twome': '2^{<\\omega}',
'\\omel': '\\omega^{<\\omega}',
'\\ome': '\\omega^{\\omega}',
'\\Pone': '\\mathsf{P1}',
'\\Ptwo': '\\mathsf{P2}',
'\\twomel': '2^{<\\omega}',
'\\Nat': '\\mathbb{N}',
'\\Rat': '\{\mathbb Q}',
'\\ds': '\\textup{\textsf{d}}',
'\\restr': '\\upharpoonright',
'\\un': '\\uparrow',
'\\de': '\\downarrow',
'\\inv': '^{-1}',
'\\pz': '\\Pi^0_1',
'\\pzt': '\\Pi^0_2',
'\\abs': '|{#1}|',
'\\dom': '\\mathsf{dom}',
'\\DNC': '\\mathsf{DNC}',
'\\tuple': '\\langle {#1} \\rangle',
'\\dbra': '\\llbracket {#1} \\rrbracket',
'\\sqbrad': '\\{ {#1} : {#2} \\}',},
throwOnError : false, });
});
"""


# Read the contents of a text file
def readfile(filename):
	try:
		with open(filename, "r") as f:
			text = f.read()
		return text
	except FileNotFoundError:
		print("Cannot find " + filename)
		sys.exit(errno.ENOENT)


# Parse a block of markdown into an HTML section slide
def parse_block(block):
	# If the block starts with the word 'center', add the .centered class to the section
	center = ""
	if block.startswith("center\n"):
		center = " class='centered'"
		block = block.replace("center\n", "", 1)

	if block.startswith("thanks\n"):
		center = " class='thanks'"
		block = block.replace("thanks\n", "", 1)

	if block.startswith("iframe\n"):
		center = " class='includehtml'"
		block = block.replace("iframe\n", "", 1)

	if block.startswith("frozen\n"):
		center = " class='frozen'"
		block = block.replace("frozen\n", "", 1)

	if block.startswith("references\n"):
		center = " class='references'"
		block = block.replace("references\n", "", 1)


	# Convert block from markdown to HTML
	html = gfm.convert(block)
	# Strip out <p></p> surrounding image tags
	html = re.sub(r"<p>(<img[\s\S]*?)</p>", r"\1", html)
	# Wrap in a section tag
	return f"<section{center}>\n" + html + "</section>\n"


def main():
	# Parse command line arguments
	parser = argparse.ArgumentParser(description="Generate html/css slides from a markdown file")
	parser.add_argument("source", help="your markdown source file")
	parser.add_argument("-o" ,"--output", default="", help="destination file for html output")
	parser.add_argument("-c" ,"--centered", default=False, action="store_true", help="center all slide content")
	parser.add_argument("-n" ,"--numbered", default=False, action="store_true", help="show slide numbers")
	parser.add_argument("--notitle", default=False, action="store_true", help="suppress the title slide")
	parser.add_argument("--css", default="", help=".css file for additional styling")
	parser.add_argument("--js", default="", help=".js file for additional functionality")
	args = parser.parse_args()

	# Set css classes for centering and numbering
	centered = "centered" if args.centered else ""
	numbered = "numbered" if args.numbered else ""

	# Read markdown text
	text = readfile(args.source)

	# Split the markdown file into slides
	blocks = text.split("\n---\n")
	
	# Peel off the header
	header = blocks[0]

	# Set default title slide information
	title = ""
	subtitle = ""
	author = ""
	coauthors = ""
	affiliation = ""

	# Read the markdown header information
	for line in header.splitlines():
		line = line.strip()
		if line.startswith("title"):
			title = line.split(":", 1)[1].strip()
		elif line.startswith("subtitle"):
			subtitle = line.split(":", 1)[1].strip()
		elif line.startswith("author"):
			author = line.split(":", 1)[1].strip()
		elif line.startswith("coauthors"):
			coauthors = line.split(":", 1)[1].strip()
		elif line.startswith("affiliation"):
			affiliation = line.split(":", 1)[1].strip()

	# Build title slide
	titlesection = f"""
		<section>
			<h1>{title}</h1>
			<p class="subtitle">{subtitle}</p>
			<p class="author">{author}</p>
			<p class="affiliation">{affiliation}</p>
			<p class="coauthors">{coauthors}</p>
		</section>
	""" if not args.notitle else ""

	# Parse remaining blocks as GitHub flavoured markdown
	sections = ''.join(map(parse_block, blocks[1:]))

	# Add the tile slide to the beginning
	sections = titlesection + sections

	# Get the additional css and js files
	css = readfile(args.css) if args.css else ""
	js = readfile(args.js) if args.js else ""

	# Build complete html document
	html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/tomorrow.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.3/dist/katex.min.css" integrity="sha384-ThssJ7YtjywV52Gj4JE/1SQEDoMEckXyhkFVwaf4nDSm5OBlXeedVYjuuUd0Yua+" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.3/dist/katex.min.js" integrity="sha384-Bi8OWqMXO1ta+a4EPkZv7bYGIes7C3krGSZoTGNTAnAn5eYQc7IIXrJ/7ck1drAi" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.3/dist/contrib/auto-render.min.js" integrity="sha384-vZTG03m+2yp6N6BNi5iM4rW4oIwk5DfcNdFfxkk9ZWpDriOkXX8voJBFrAO7MpVl" crossorigin="anonymous"></script>
<style type="text/css" media="all">
{minislides}	
{css}
</style></head><body>
<div class="slides {centered} {numbered}">
{sections}
</div>
<script type="text/javascript" charset="utf-8">
hljs.highlightAll();
{katex}
{navigation}
{js}
</script></body></html>
"""

	# Dump to the command line unless the --output option is specified
	if not args.output:
		print(html)
	else:
		with open(args.output, "w") as f:
			f.write(html)

if __name__ == '__main__':
	sys.exit(main())
