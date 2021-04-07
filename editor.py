class Markdown:
    text = None

    def __init__(self):
        self.text = ''

    def help(self):
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')

    def plain(self):
        self.text += input("- Text: ")

    def bold(self):
        self.text += '**' + input("- Text: ") + '**'

    def italic(self):
        self.text += '*' + input("- Text: ") + '*'

    def header(self):
        level = input("- Level: ")
        if level.isdigit():
            level = int(level)
            if 1 <= level <= 6:
                self.text += '#' * level + ' ' + input("- Text: ") + '\n'
        else:
            print("The level should be within the range of 1 to 6")

    def link(self):
        label = input("- Label: ")
        url = input("- URL: ")
        self.text += '' + '[' + label + '](' + url + ')'

    def inline_code(self):
        self.text += '`' + input('- Text: ') + '`'

    def new_line(self):
        self.text += '\n'

    def un_ordered_list(self, value):
        num_rows = 0
        while num_rows < 1:
            num_rows = int(input("- Number of rows: "))
            if num_rows < 1:
                print("The number of rows should be greater than zero")
        for i in range(num_rows):
            if value == "ordered-list":
                self.text += f"{str(i + 1)}. {input(f'- Row #{i + 1}: ')}\n"
            elif value == "unordered-list":
                self.text += f"* {input(f'- Row #{i + 1}: ')}\n"

    def record_close(self):
        file = open('output.md', 'w', encoding='utf-8')
        file.write(self.text.rstrip('\n'))
        file.close()
        exit()

    def work(self):
        print("$ python markdown-editor.py")
        formatting_commands = ("plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line", 'line-break')
        special_commands = ('!help', '!done')
        choice = ''
        while True:
            choice = input("- Choose a formatter: ")
            if choice == special_commands[0]:
                self.help()
            elif choice == special_commands[1]:
                self.record_close()
            elif choice in formatting_commands:
                if choice == 'plain':
                    self.plain()
                elif choice == 'bold':
                    self.bold()
                elif choice == 'italic':
                    self.italic()
                elif choice == 'header':
                    self.header()
                elif choice == 'link':
                    self.link()
                elif choice == 'inline-code':
                    self.inline_code()
                elif choice == 'ordered-list':
                    self.un_ordered_list('ordered-list')
                elif choice == 'unordered-list':
                    self.un_ordered_list('unordered-list')
                else:
                    self.new_line()  # new-line
                print(self.text)


markdown = Markdown()
markdown.work()
