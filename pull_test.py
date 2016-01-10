from xml.dom.pulldom import CHARACTERS, START_ELEMENT, parseString, END_ELEMENT


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]

source = """<rdg wit="#ipa">рускаꙗ землѧ <lb/>
                                <add place="margin">и хто в неи почалъ пѣрвѣе кнѧжи<hi rend="sup"
                                        >т</hi></add>·:·</rdg>"""

doc = parseString(source)
output = ""

for event, node in doc:
    if event == START_ELEMENT:
        # skip rdg element
        if node.localName == "rdg":
            continue
        # in case of add deal with overlapping hierarchies
        if node.localName == "add":
            node.setAttribute("type","start")
        # TODO: toxml marks every element as />
        # TODO: use stack of open elements
        output += node.toxml()
        # print(node)
        # print(type(node))
        print(event, node)
    if event == END_ELEMENT:
        # skip rdg element
        if node.localName == "rdg":
            continue
        # in case of add deal with overlapping hierarchies
        if node.localName == "add":
            node.setAttribute("type","end")
        # TODO: toxml marks every element as />
        # TODO: use stack of open elements
        output += node.toxml()
        # print(node)
        # print(type(node))
        print(event, node)

print(output)