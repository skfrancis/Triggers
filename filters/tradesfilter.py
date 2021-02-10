import regex


class TradesFilter:
    def __init__(self):
        self.regexes = [
            regex.compile(r"^(.+?) (have fashioned the items together to create [^:]+:) ([^.]+)\.$"),
            regex.compile(r"^(.+?) (lacked the skills to fashion) ([^.]+)\.$"),
            regex.compile(r"^(.+?) (has fashioned) ([^.]+)\.$"),
            regex.compile(r"^(.+?) (was not successful in making) ([^.]+)\.$")
        ]

    def parse(self, log_line):
        def process_data(timestamp, result_data):
            created = False
            if 'fashioned' in result_data.group(2):
                created = True
            return {
                'timestamp': timestamp,
                'source': result_data.group(1),
                'created': created,
                'item': result_data.group(3),
                'type': 'tradeskill',
                'debug': result_data.string

            }

        for expression in self.regexes:
            result = regex.search(expression, log_line.get('text'))
            if result:
                return process_data(log_line.get('timestamp'), result)

        return None
