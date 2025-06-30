# https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

# https://regexr.com/  ---> cheet sheet bana do isski 
# these are two website two master regular expression 






import re
patter="was"
text='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Suspendisse potenti. Proin consectetur, nunc vel fermentum hendrerit, neque erat bibendum turpis, vel interdum libero turpis sit amet turpis. Curabitur ac libero eros. Nam quis ligula eu magna varius vehicula nec vel eros. Vestibulum aliquam magna in tortor fermentum, eget luctus tortor interdum. Aenean aliquet, nunc ut vehicula tempor, tortor lorem interdum risus, a rhoncus odio felis ut magna. 
Donec egestas, purus eu varius vestibulum, ex est blandit felis, id eleifend mauris odio sit amet justo. Nullam malesuada, eros sed aliquet dictum, neque justo sodales augue, sit amet tincidunt felis lacus eu arcu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce volutpat, risus ut elementum feugiat, metus magna fringilla elit, eget dapibus ex mi ut lorem. Nam laoreet lorem et sapien posuere, sed cursus metus dictum. 
Mauris euismod dui ac eros eleifend, id bibendum lacus vulputate. Suspendisse et justo vel ligula pellentesque volutpat. Nunc nec libero id libero feugiat gravida ac nec mi. Duis sodales justo ac justo accumsan, nec consectetur libero fermentum. Vivamus tincidunt lorem sit amet sapien tempor, et molestie elit feugiat. Ut facilisis, tortor at sagittis tincidunt, nisl purus viverra lacus, ac ultricies nulla odio nec odio. Duis fringilla orci et justo condimentum laoreet. Phasellus lacinia, lacus vel dapibus consectetur, augue odio volutpat lectus, non egestas erat nisi ut lorem. Integer volutpat tristique metus at bibendum. 
Curabitur nec turpis at mi dictum cursus. Ut id dolor sit amet mauris gravida aliquet. Integer pharetra orci nec dolor pellentesque, sit amet malesuada odio accumsan. Ut et nunc eu urna bibendum malesuada sed sed orci. Morbi nec leo id magna pellentesque scelerisque vel id tortor. Nam dapibus suscipit turpis, non dictum libero viverra id. Suspendisse in suscipit tortor, non ullamcorper libero. Cras mollis, augue sed tempus ultricies, mi libero bibendum magna, vel aliquet est odio at ligula. Vivamus eget odio non nunc tincidunt facilisis. 
Sed dapibus malesuada risus, ut elementum risus malesuada nec. Aenean laoreet ligula ac turpis"
'''
match =re.search(patter,text)     # 3 keval 1st occurance hi dega  
print(match)

matches =re.finditer(patter,text)  # ye saari occurances de dega unki location bhi 
for match in matches:
    print(match)
# jaha pe bhi was hoga wo la ke de dega auto matically 
# issko "in" keyword ki help se bhi kiya ja ksta tha easily 














patter=r"[A-Z]+yclone"  # A se Z tk start hone wale koi bhi charecter jo ylone se juda kho (Cuyclone + Dyclone) 
text='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Suspendisse potenti. Proin consectetur, nunc vel fermentum hendrerit, neque erat bibendum turpis, vel interdum libero turpis sit amet turpis. Curabitur ac libero eros. Nam quis ligula eu magna varius vehicula nec vel eros. Vestibulum aliquam magna in tortor fermentum, eget luctus tortor interdum. Aenean aliquet, nunc ut vehicula tempor, tortor lorem interdum risus, a rhoncus odio felis ut magna. 
Donec egestas, purus eu varius vestibulum, ex est blandit felis, id eleifend mauris odio sit amet justo. Nullam malesuada, eros sed aliquet dictum, neque justo sodales augue, sit amet tincidunt felis lacus eu arcu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce volutpat, risus ut elementum feugiat, metus magna fringilla elit, eget dapibus ex mi ut lorem. Nam laoreet lorem et sapien posuere, sed cursus metus dictum. 
Mauris euismod dui ac eros eleifend, id bibendum lacus vulputate. Suspendisse et justo vel ligula pellentesque volutpat. Nunc nec libero id libero feugiat gravida ac nec mi. Duis sodales justo ac justo accumsan, nec consectetur libero fermentum. Vivamus tincidunt lorem sit amet sapien tempor, et molestie elit feugiat. Ut facilisis, tortor at sagittis tincidunt, nisl purus viverra lacus, ac ultricies nulla odio nec odio. Duis fringilla orci et justo condimentum laoreet. Phasellus lacinia, lacus vel dapibus consectetur, augue odio volutpat lectus, non egestas erat nisi ut lorem. Integer volutpat tristique metus at bibendum. 
Curabitur nec turpis at mi dictum cursus. Ut id dolor sit amet mauris gravida aliquet. Integer pharetra orci nec dolor pellentesque, sit amet malesuada odio accumsan. Ut et nunc eu urna bibendum malesuada sed sed orci. Morbi nec leo id magna pellentesque scelerisque vel id tortor. Nam dapibus suscipit turpis, non dictum libero viverra id. Suspendisse in suscipit tortor, non ullamcorper libero. Cras mollis, augue sed tempus ultricies, mi libero bibendum magna, vel aliquet est odio at ligula. Vivamus eget odio non nunc tincidunt facilisis. 
Sed dapibus malesuada risus, ut elementum risus malesuada nec. Aenean laoreet ligula ac turpis"
'''
match =re.search(patter,text)     # ye keval 1st occurance hi dega  
print(match)

matches =re.finditer(patter,text)  # ye saari occurances de dega unki location bhi 
for match in matches:
    print(match)
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])
# jaha pe bhi was hoga wo la ke de dega auto matically 
# issko "in" keyword ki help se bhi kiya ja ksta tha easily 



