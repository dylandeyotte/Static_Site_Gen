from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(block):
    split_blocks = block.split('\n')
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    elif len(split_blocks) > 1 and split_blocks[0].startswith('```') and split_blocks[-1].endswith('```'):
        return BlockType.CODE
    elif all(line.startswith('>') for line in split_blocks):
        return BlockType.QUOTE
    elif all(line.startswith('- ') for line in split_blocks):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f'{i}. ') for i, line in enumerate(split_blocks, start = 1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
