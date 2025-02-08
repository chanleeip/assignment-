from dataclasses import dataclass,asdict
from typing import List
import json
HEADERS={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

@dataclass
class OutputFormatData:
    url:str
    title:str
    author_name:str
    author_page_link:str
    date:str
    categories:List[str]
    summary:str
    content:str

    def to_json_str(self):
        '''
            Return as a json string
        '''
        return json.dumps(asdict(self),indent=4)
    
    def to_dict(self):
        '''
            Return as a dict
        '''
        return asdict(self)