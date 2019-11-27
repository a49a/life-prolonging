from random import choice


class Choice:

    def __init__(self, pool, args):
        self.pool = pool
        self.args = args

    def choose_all(self):
        choices_results = []
        for category, v in self.args.__dict__.items():
            if v:
                r = self.choose(category)
                choices_results.append(r)
        return choices_results

    def choose(self, name):
        r = choice(self.pool[name])
        return r



