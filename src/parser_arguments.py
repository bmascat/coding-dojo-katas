
class ParserArguments:
    def __init__(self, schema: dict):
        self.schema = schema

    def parse(self, args: str) -> dict:
        args_parsed = {}
        args = args.strip().split("-")
        for arg in args:
            if arg == '':
                continue
            if len(arg) == 1:
                args_parsed[arg] = True
            else: 
                key, value = arg.strip().split(" ")
                args_parsed[key] = value
                
        return args_parsed
