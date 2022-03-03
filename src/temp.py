
from resource_identifier.config import ZamResourceIdentifierConfig
from resource_identifier.cursor import create_cursor
from resource_identifier.unique_identifier import ZamResourceIdenrtifier, ZamResourceIdentifierBase
import time


if __name__ == '__main__':
    
    # a = ZamResourceIdentifierBase('sdf')
    # print(a)
    # b = ZamResourceIdentifierBase(a)
    # print(b)
    # c = ZamResourceIdentifierBase(b)
    
    # print(id(a) == id(b))
    # print(a == c)
    
    # print(type(a))
    # print(type(b))
    
    # print(a.cursors)
    
    config = ZamResourceIdentifierConfig()
    
    # res = ZamResourceIdenrtifier('apiv1://[beijs--ing]starwar_ep03_sc_0020:anim:andy@v0.2.3/1/2/3/4/5#1#2#4')
    # print(res.parse)
    # res = ZamResourceIdenrtifier('starwar_chr_amy:anim:andy@v0.2.3/1/2/3/4/5#1#2#4')
    # print(res.parse)
with create_cursor(r'apiv1://[beijs--ing]starwar_ep03_sc_0020:safd@v1.2.3/1/2/3/4/5#1#2#4') as c:
    print(c.resource)
    print(c.resource.parse)
    print(c.resource.cursors)
    

