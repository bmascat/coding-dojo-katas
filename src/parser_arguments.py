
class ParserArguments:
    def __init__(self, schema: dict):
        self.schema = schema

    def parse(self, args: str) -> dict:
        args_parsed = {}
        args = args.strip().split("-")
        for arg in args:
            temp_arg = arg.strip()
            
            if temp_arg == '':
                continue
            if len(temp_arg) == 1:
                args_parsed[temp_arg] = True
            else: 
                key, value = temp_arg.split(" ")
                args_parsed[key] = int(value) if self._is_int(value) else value
                
        return args_parsed
    
    def _is_int(self, value: str) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

