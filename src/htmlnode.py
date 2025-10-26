class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

    def to_html(self):
        raise NotImplementedError('Not Implemented')
    
    def props_to_html(self):
        if self.props is None:
            return ''
        string = ''
        for entry in self.props:
            string += f' {entry}="{self.props[entry]}"'
        return string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError('No value provided')
        if self.tag is None:
            return self.value
        props_string = f'{self.props_to_html()}'
        return f'<{self.tag}{props_string}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('No tag')
        if self.children is None:
            raise ValueError('No children')
          
        child_string = ''
        for child in self.children:
            child_string += ''.join(child.to_html())
        
        props_string = f'{self.props_to_html()}'
        return f'<{self.tag}{props_string}>{child_string}</{self.tag}>'
        

