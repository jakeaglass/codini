import sublime, sublime_plugin
import json
import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 8888
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

class Codini(sublime_plugin.EventListener):
	def find_possible_matches(self, view, point, string):
		syntax = view.scope_name(point)
		print(syntax)
		#if (syntax == "")
		HTMLelements = [ "<title>", "<a>", "<abbr>", "<acronym>", "<address>", "<applet>", "<area>", "<article>", "<aside>", "<audio>", "<b>", "<base>", "<basefont>", "<bdi>", "<bdo>", "<bgsound>", "<big>", "<blink>", "<blockquote>", "<body>", "<br>", "<button>", "<canvas>", "<caption>", "<center>", "<cite>", "<code>", "<col>", "<colgroup>", "<content>", "<data>", "<datalist>", "<dd>", "<decorator>", "<del>", "<details>", "<dfn>", "<dialog>", "<dir>", "<div>", "<dl>", "<dt>", "<element>", "<em>", "<embed>", "<fieldset>", "<figcaption>", "<figure>", "<font>", "<footer>", "<form>", "<frame>", "<frameset>", "<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>", "<head>", "<header>", "<hgroup>", "<hr>", "<html>", "<i>", "<iframe>", "<img>", "<input>", "<ins>", "<isindex>", "<kbd>", "<keygen>", "<label>", "<legend>", "<li>", "<link>", "<listing>", "<main>", "<map>", "<mark>", "<marquee>", "<menu>", "<menuitem>", "<meta>", "<meter>", "<nav>", "<nobr>", "<noframes>", "<noscript>", "<object>", "<ol>", "<optgroup>", "<option>", "<output>", "<p>", "<param>", "<picture>", "<plaintext>", "<pre>", "<progress>", "<q>", "<rp>", "<rt>", "<ruby>", "<s>", "<samp>", "<script>", "<section>", "<select>", "<shadow>", "<small>", "<source>", "<spacer>", "<span>", "<strike>", "<strong>", "<style>", "<sub>", "<summary>", "<sup>", "<table>", "<tbody>", "<td>", "<template>", "<textarea>", "<tfoot>", "<th>", "<thead>", "<time>", "<title>", "<tr>", "<track>", "<tt>", "<u>", "<ul>", "<var>", "<video>", "<wbr>", "<xmp>" ]
		CSSelements =['color', 'opacity', 'background', 'background-attachment', 'background-color', 'background-image', 'background-position', 'background-repeat', 'background-clip', 'background-origin', 'background-size', 'border', 'border-bottom', 'border-bottom-color', 'border-bottom-left-radius', 'border-bottom-right-radius', 'border-bottom-style', 'border-bottom-width', 'border-color', 'border-image', 'border-image-outset', 'border-image-repeat', 'border-image-slice', 'border-image-source', 'border-image-width', 'border-left', 'border-left-color', 'border-left-style', 'border-left-width', 'border-radius', 'border-right', 'border-right-color', 'border-right-style', 'border-right-width', 'border-style', 'border-top', 'border-top-color', 'border-top-left-radius', 'border-top-right-radius', 'border-top-style', 'border-top-width', 'border-width', 'box-decoration-break', 'box-shadow', 'bottom', 'clear', 'clip', 'display', 'float', 'height', 'left', "Specifies what happens if content overflows an element's box", 'overflow-x', 'overflow-y', 'padding', 'padding-bottom', 'padding-left', 'padding-right', 'padding-top', 'position', 'right', 'top', 'visibility', 'width', 'vertical-align', 'z-index', 'align-content', 'align-items', 'align-self', 'display', 'flex', 'flex-basis', 'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap', 'justify-content', 'margin', 'margin-bottom', 'margin-left', 'margin-right', 'margin-top', 'max-height', 'max-width', 'min-height', 'min-width', 'order', 'hanging-punctuation', 'hyphens', 'letter-spacing', 'line-break', 'line-height', 'overflow-wrap', 'tab-size', 'text-align', 'text-align-last', 'text-indent', 'text-justify', 'text-transform', 'white-space', 'word-break', 'word-spacing', 'word-wrap', 'text-decoration', 'text-decoration-color', 'text-decoration-line', 'text-decoration-style', 'text-shadow', 'text-underline-position', 'font', 'font-family', 'font-feature-setting', '@font-feature-values', 'font-kerning', 'font-language-override', 'font-synthesis', 'font-variant-alternates', 'font-variant-caps', 'font-variant-east-asian', 'font-variant-ligatures', 'font-variant-numeric', 'font-variant-position', 'font-size', 'font-style', 'font-variant', 'font-weight', '@font-face', 'font-size-adjust', 'font-stretch', 'direction', 'text-orientation', 'text-combine-horizontal', 'unicode-bidi', 'writing-mode', 'border-collapse', 'border-spacing', 'caption-side', 'empty-cells', 'table-layout', 'counter-increment', 'counter-reset', 'list-style', 'list-style-image', 'list-style-position', 'list-style-type', '@keyframes', 'animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-timing-function', 'animation-play-state', 'backface-visibility', 'perspective', 'perspective-origin', 'transform', 'transform-origin', 'transform-style', 'transition', 'transition-property', 'transition-duration', 'transition-timing-function', 'transition-delay', 'box-sizing', 'content', 'cursor', 'icon', 'ime-mode', 'nav-down', 'nav-index', 'nav-left', 'nav-right', 'nav-up', 'outline', 'outline-color', 'outline-offset', 'outline-style', 'outline-width', 'resize', 'text-overflow', 'break-after', 'break-before', 'break-inside', 'column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color', 'column-rule-style', 'column-rule-width', 'column-span', 'column-width', 'columns', 'widows', 'orphans', 'page-break-after', 'page-break-before', 'page-break-inside', 'marks', 'quotes', 'filter', 'image-orientation', 'image-rendering', 'image-resolution', 'object-fit', 'object-position', 'mask', 'mask-type', 'mark', 'mark-after', 'mark-before', 'phonemes', 'rest', 'rest-after', 'rest-before', 'voice-balance', 'voice-duration', 'voice-pitch', 'voice-pitch-range', 'voice-rate', 'voice-stress', 'voice-volume', 'marquee-direction', 'marquee-play-count', 'marquee-speed', 'marquee-style']
		JSelements = [""]
		possible_HTMLelements = []
		possible_CSSelements = []
		possible_JSelements=[]

		for element in HTMLelements:
			if(element.startswith("<"+string)):
				possible_HTMLelements.append(element)\

		for element in CSSelements:
			if(element.startswith(string)):
				possible_CSSelements.append(element)

		for element in CSSelements:
			if(element.startswith(string)):
				possible_JSelements.append(element)

		possibleElements = [possible_JSelements, possible_HTMLelements, possible_CSSelements]
		print (possibleElements)
		return possibleElements


	def on_modified_async(self, view):  
		point = view.sel()[0].begin()
		region = view.word(point)
		word = view.substr(region)
		possible_matches = self.find_possible_matches(view, point, word)
		print (region)
		background-i
		jsonData = {}
		jsonData['action'] = 'suggested'
		jsonData['data'] = {}
		jsonData['data']['suggestions'] = possible_matches
		sock.sendto(str.encode(json.dumps(jsonData)), (UDP_IP, UDP_PORT))
		print (word)
		print(jsonData)