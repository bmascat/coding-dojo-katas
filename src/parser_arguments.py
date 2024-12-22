
class ParserArguments:
    def __init__(self, schema: dict):
        self.schema = schema

    def parse(self, args: str) -> dict:
        args_parsed = {}
        args = args.split("-")
        for arg in args:
            if arg == '':
                continue
            if len(arg) > 0:
                key, value = arg.split(" ")
                args_parsed[key] = value
            else: 
                args_parsed[arg] = True
        return args_parsed
