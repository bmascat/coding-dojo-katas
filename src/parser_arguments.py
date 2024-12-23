from dataclasses import dataclass

@dataclass
class ParserArguments:
    schema: dict
            
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
        
        for key, value in self.schema.items():
            if key not in args_parsed:
                if value is bool:
                    args_parsed[key] = False
                elif value is int:
                    args_parsed[key] = 0
                elif value is str:
                    args_parsed[key] = ""
                else:
                    args_parsed[key] = None
        
        self.values = args_parsed
        return args_parsed
    
    def _is_int(self, value: str) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False