from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt

class AskOptions:
    def __init__(self, message, choices, name):
        self.message = message
        self.choices = choices
        self.name = name
        self.style = style_from_dict({
            Token.Separator: '#cc5454',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#f44336 bold',
            Token.Question: '',
        })

    def ask_multiple_select (self):
        questions = [{
                'type': 'checkbox',
                'message': self.message,
                'name': self.name,
                'choices': self.choices,
                'validate': lambda answer: 'You must choose at least one option.' \
                    if len(answer) == 0 else True
            }]
        answers = prompt(questions, style=self.style)
        return answers


