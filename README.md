Codini
======

Code Completion, Documentation, and Programming Teaching App; a plugin for Sublime Text 2/3 with companion web app for live code suggestions and docs, like MAGIC!

Features:
- Automatic code completion and documentation 
- Provides documentation with HTML, CSS, JavaScript
- Provides documentation for language defined words
- Comment pseudocode
- Finds all your current comments; click on it and your cursor will jump to the comment.
	- Expandable text -- see your code between two comments

##Getting Codini

###Now Available as an easy Installer Package for OS X and Sublime Text 3!

There are two components to a Condini setup: the server or host computer and the client. The server is where you're writing your code, so it's probably a PC. The latter device, the client, can be any computer that can access the web and will display your code completion suggestions and help you instantly navigate documentation, instantaneously updating as you code away on the host computer.

###Install Dependencies
A dependency of Codini is Node.js on the host computer. You can [download a prebuilt installer from Node.js](http://nodejs.org/download/) or use your favourite package manager for the installation if you don't already have it.

You'll also need to have [Sublime Text 2 or 3](http://www.sublimetext.com/) installed (3 is recommended). 

###Clone Git into Plugins
You'll need to add the files in this folder to your plugins directory in order for sublime to access them; the easiest way is to `cd` into your plugins directory and:

`git clone https://github.com/jakeaglass/codini.git`

On a Mac, the Sublime Text plugins directory is located under `~/Library/Application Support/Sublime Text 3/Packages/`. On Windows the path is `%APPDATA%\Sublime Text 3`, and Linux has it under ` ~/.Sublime Text 3`. 

###Start Local Server
The plugin should start on its own when you open Sublime, and you will be notified as such. However, if it doesn't work the first time, try to `cd` into the directory where the plugin is installed and run

`./start`

###Access WebApp on Companion Device
Go to [http://macpie.net/codini](http://macpie.net/codini) on your secondary device and you'll be met with a dialogue requesting the IP of your host machine. Find the local IP in your host computer's network configuration and enter it into the webpage on the secondary device, then hit "Get Started." Magicalness should now occur!

##More Resources, Languages, and Docsets, Oh My!
The folder `codini/broadcastServer/docsets/` contins `.json` array files of the languages currently supported for documentation.

- Sublime Text's backend will determine what language the user is writing, and Codini's python on the main computer will use that information to pick a language index file.
- Currently, Codini ONLY supports Python, CSS, HTML, and Javascript, but you can add languages.
- The way Codini's implementation of reference file parsing works is by the host PC passing the client device an array of possible matches for the word you're typing, which are each linked to reference files stored on a remote server; these open in an Iframe on the right half of the secondary device, while the suggestions appear on the left.
