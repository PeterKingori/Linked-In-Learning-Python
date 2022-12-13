#
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphs = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment:", data)
        position = self.getpos()
        print("At line", position[0], " position", position[1])

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        position = self.getpos()
        print("At line", position[0], " position", position[1])

        global paragraphs
        if tag == "p":
            paragraphs += 1

        if len(attrs) > 0:
            print("Attributes:")
            for attr in attrs:
                print("\t", attr[0], "=", attr[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered text data:", data)
        position = self.getpos()
        print("At line", position[0], " position", position[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    html_file = open("samplehtml.html")
    if html_file.mode == "r":
        contents = html_file.read() # read the entire file
        parser.feed(contents)

    print("Paragraph tags:", paragraphs)

if __name__ == "__main__":
    main()
  