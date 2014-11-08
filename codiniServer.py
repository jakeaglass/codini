import sublime, sublime_plugin

class Codini(sublime_plugin.EventListener):
	def find_possible_matches(self, view, point, string):
		syntax = view.scope_name(point)
		print(syntax)
		#if (syntax == "")
		HTMLelements = [ "<title>", "<a>", "<abbr>", "<acronym>", "<address>", "<applet>", "<area>", "<article>", "<aside>", "<audio>", "<b>", "<base>", "<basefont>", "<bdi>", "<bdo>", "<bgsound>", "<big>", "<blink>", "<blockquote>", "<body>", "<br>", "<button>", "<canvas>", "<caption>", "<center>", "<cite>", "<code>", "<col>", "<colgroup>", "<content>", "<data>", "<datalist>", "<dd>", "<decorator>", "<del>", "<details>", "<dfn>", "<dialog>", "<dir>", "<div>", "<dl>", "<dt>", "<element>", "<em>", "<embed>", "<fieldset>", "<figcaption>", "<figure>", "<font>", "<footer>", "<form>", "<frame>", "<frameset>", "<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>", "<head>", "<header>", "<hgroup>", "<hr>", "<html>", "<i>", "<iframe>", "<img>", "<input>", "<ins>", "<isindex>", "<kbd>", "<keygen>", "<label>", "<legend>", "<li>", "<link>", "<listing>", "<main>", "<map>", "<mark>", "<marquee>", "<menu>", "<menuitem>", "<meta>", "<meter>", "<nav>", "<nobr>", "<noframes>", "<noscript>", "<object>", "<ol>", "<optgroup>", "<option>", "<output>", "<p>", "<param>", "<picture>", "<plaintext>", "<pre>", "<progress>", "<q>", "<rp>", "<rt>", "<ruby>", "<s>", "<samp>", "<script>", "<section>", "<select>", "<shadow>", "<small>", "<source>", "<spacer>", "<span>", "<strike>", "<strong>", "<style>", "<sub>", "<summary>", "<sup>", "<table>", "<tbody>", "<td>", "<template>", "<textarea>", "<tfoot>", "<th>", "<thead>", "<time>", "<title>", "<tr>", "<track>", "<tt>", "<u>", "<ul>", "<var>", "<video>", "<wbr>", "<xmp>" ]
		CSSelements =[""]
		JSelements = [""]
		possible_HTMLelements = []
		possible_CSSelements = []
		possible_JSelements=[]

		for element in HTMLelements:
			if(element.startswith("<"+string)):
				possible_HTMLelements.append(element)


		for element in CSSelements:
			if(element.startswith(string)):
				possible_CSSelements.append(element)

		for element in CSSelements:
			if(element.startswith(string)):
				possible_JSelements.append(element)

		possibleElements = [possible_JSelements, possible_HTMLelements, possible_CSSelements]
		return possibleElements



	def on_modified_async(self, view):  
		point = view.sel()[0].begin()
		region = view.word(point)
		word = view.substr(region)
		possible_matches = self.find_possible_matches(view, point, word)
		print(possible_matches)