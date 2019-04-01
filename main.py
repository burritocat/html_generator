#import needed libraries (sys; random; re; time)
#Create html escape table dictionary
#Create html syntax dictionary
#Create css syntax dictionary 
#Create dictionary for webpage headers and for webpage paragraphs 
#Create dictionary for selected colors of headers and paragraphs
#Create list of color options for css formatting

#function - titlecase function that deals with apostrophes 
          # to be called within other functions 
#function - intro user to program
#function - ask user for webpage title 
          #call titlecase function
          #return webpage title
#function - ask user for webpage headers
          #loop through input until user finishes
          #call titlecase function
          #add webpage headers to dictionary as keys w/ values of None
#function - ask user for webpage paragraphs
          #loop through input until 1 paragr per header
          #add webpage paragraphs as updated values to the associated keys w/i dictionary
#function - ask user if they would like to have css for coloring text
          #if yes, display options
#function - color preference function
          #to be called if answer to previous function was yes
          #ask color preference
          #return answer
#function - print webpage html
          #print content with html syntax 
#function - print webpage css 
          #print css color formatting
#function - program outro
          #end program and remind user to copy and save html formatted text/css 
#function to call all main program functions
          #call css generation function only if user selected to have css
#call main program function


"""import libraries"""
import sys
import random
import re
import time

"""html escapes dictionary to reformat user input that matches a type of html syntax, but is not intended to be interpreted in html"""
html_escape_table = {
  "&": "&amp;",
  '"': "&quot;",
  "'": "&apos;",
  ">": "&gt;",
  "<": "&lt;",
  }

"""html syntax dictionary"""
HTML_DICT = {
  "html_start": "<html>",    
  "html_end": "</html>",
  "head_start": "  <head>",
  "head_end": "  </head>",
  "title_start": "    <title>",
  "title_end": "</title>",
  "body_start": "      <body>",
  "body_end": "      </body>",
  "h1_start": "        <h1>",
  "h1_end": "</h1>",
  "p_start": "          <p>",
  "p_end": "</p>"
  }

"""css syntax dictionary"""
CSS_DICT = {
  "h1_ft1": "h1 {",
  "h1_ft2": "  color:",
  "h1_ft3": "}",
  "p_ft1": "p {",
  "p_ft2": "  color:",
  "p_ft3": "}"
  }

"""dictionary for storage of headers and corresponding paragraphs"""
h1_p_dict = {}

"""dictionary for css color choices"""
color_choices_dict = {
  "header": None, 
  "paragraph": None
  }
"""list of css color options"""
COLOR_LIST = ["blue", "purple", "red", "pink", "green", "brown", "orange", "black"]

def html_escape(text):
  """Produce html escapes within text"""
  return "".join(html_escape_table.get(c,c) for c in text)

def titlecase(s):
  """function to avoid the capitalization after apostrophes that ".title()" causes"""
  return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                lambda mo: mo.group(0)[0].upper() +
                            mo.group(0)[1:].lower(),
                s)

def program_intro():
  """intro user to program. no need to return anything"""
  print("\nHi! Welcome to the Basic html + css Generator...where we wrap your header and paragraph webpage content into proper html formatting + give your text a splash of color!")
  print("\n~~Let's get started!~~")
  time.sleep(1)

def create_webpage_title():
  """ask user for webpage title. return title name for use in html generation"""
  title = input("\nWhat is the title of your page? Hit ENTER once finished. \n(Note: This will not appear in the text of your published webpage)\n> ")
  title = titlecase(title)
  return title

def create_webpage_headers():
  """create loop to ask user for webage headers until user is finished. return each header and append onto h1_list"""
  print ("\nLet's list out the main headers of your page. Add a main header, and then hit ENTER. When finished adding headers, leave blank and hit ENTER.")
  while True:
    h1_add = input("> ")
    if h1_add != "":
      h1_add = titlecase(h1_add)
      h1_p_dict[h1_add] = None
    else:
      break
  print()

def create_header_paragraphs():
  """create loop that prompts user to input a paragraph for each header in the header list. append paragraphs onto parag_list"""
  print("Now let's add the main content of the page-- type in a paragraph of text to coincide with each of your main headers.")
  for key in h1_p_dict:
    print ("\nThe header we're working on now is - *{}*".format(key))
    parag_content = input("> ")
    if parag_content != "":
      print ("\nGreat, we'll add that in.")
      h1_p_dict[key]= parag_content
      time.sleep(1)
    else:
      print("\n¯\_(ツ)_/¯ Ok, we'll skip adding content under this header.\n")
      parag_content = "[N/A - you can erase this section.]"
      h1_p_dict[key]= parag_content

def find_css_preference():
  """ask user if they want to change color of their text."""
  print ("\nWould you like to generate some CSS code to edit the color of your html title and paragraph text?\nEnter 'yes' or 'no'.")
  while True:
    wantCSS = input("> ")
    wantCSS = wantCSS.lower()
    if (wantCSS != "yes") and (wantCSS != "no"): 
      print("Please enter 'yes' or 'no'.\n")
    else:
      while True:
        if wantCSS == "no":
          print ("¯\_(ツ)_/¯ Okay. Let's get to your html.")
          break
        elif wantCSS == "yes":
          print ("\nHere are your color options:")
          for color in COLOR_LIST:
            print ("-",color)
          print ("- random color")
          return wantCSS
          
def css_color_selection():
  """ask user which color they would like for the sections of their CSS, until they answer one of the available color options. records their color preference"""
  for key in color_choices_dict:
    while True:
      color_choice = input("\nWhich color option would you like for *{}* text?\n> ".format(key))
      color_choice = color_choice.lower()
      if (color_choice == "random color") or (color_choice == "random"):
        time.sleep(1)
        print ("\nGreat! We'll use", color_choice)
        random_color = random.choice(COLOR_LIST)
        color_choice = random_color
        color_choices_dict[key] = color_choice
        break
      elif color_choice in COLOR_LIST:
        time.sleep(1)
        print ("\nGreat! We'll use", color_choice)
        color_choices_dict[key] = color_choice
        break
      else:
        time.sleep(1)
        print("\n¯\_(ツ)_/¯ I didn't understand your color choice for {}. Please choose one of the options from the list.\n".format(key))
  return color_choices_dict

def html_generator(title):
  """print input content wrapped in html syntax"""
  print ()
  print ("This page content really shaped up nicely!")
  time.sleep(1)
  print ("Here's your HTML code!--Please copy and save the code below this line.")
  print ("-------------------------------\n")
  time.sleep(2)
  print (HTML_DICT["html_start"])
  print (HTML_DICT["head_start"])
  print (HTML_DICT["title_start"], html_escape(title), HTML_DICT["title_end"])
  print (HTML_DICT["head_end"])
  print (HTML_DICT["body_start"])
  for key, value in h1_p_dict.items():
    print (HTML_DICT["h1_start"], html_escape(key), HTML_DICT["h1_end"])
    print (HTML_DICT["p_start"], html_escape(value), HTML_DICT["p_end"])
    print ()
  print (HTML_DICT["body_end"])
  print (HTML_DICT["html_end"])
  print ("\n-------------------------------")

def css_generator():
  """print input css formatting requests in css code"""
  time.sleep(1)
  print ("\nHere's your CSS code!--Please copy and save the code below this line.")
  print("-------------------------------\n")
  time.sleep(2)
  print(CSS_DICT["h1_ft1"])
  print(CSS_DICT["h1_ft2"], color_choices_dict["header"])
  print(CSS_DICT["h1_ft3"])
  print()
  print(CSS_DICT["p_ft1"])
  print(CSS_DICT["p_ft2"], color_choices_dict["paragraph"])
  print(CSS_DICT["p_ft3"])
  print("\n-------------------------------\n")

def program_outro():
  time.sleep(2)
  sys.exit("Thanks! Have a great day! Don't forget to save your new code, printed in between the lines above. If you're just testing out this generator, its creator suggests trying out the code at https://codepen.io/")

def run_program():
  program_intro()
  title = ""
  while title == "":
    title = create_webpage_title()
    if title == "":
      print ("Please input a title.")
  while h1_p_dict == {}:
    create_webpage_headers()
    if h1_p_dict == {}:
      print ("Please create some headers.")
  create_header_paragraphs()
  wantCSS = find_css_preference()
  if wantCSS == "yes":
    css_color_selection()
  html_generator(title)
  ##html printing and file writing -- NEEDS WORK
  #html = html_generator(title)
  #fo1 = open("webpagecontent.html", "wb")
  #fo1.write(html)
  if (color_choices_dict["header"] != None) or (color_choices_dict["paragraph"] != None):
    css_generator()
    ##css printing and file writing -- NEEDS WORK
    #css = css_generator()
    #fo2 = open("webpagestyle.css", "wb")
    #fo2.write(css)
  program_outro()

run_program()
