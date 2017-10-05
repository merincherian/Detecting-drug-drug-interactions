import xml.etree.ElementTree as ET
tree = ET.parse('Edited/Acitretin_ddi.xml')
root = tree.getroot()



for entity in root.iter('entity'):
     text=entity.get('text')
     list1 = text.lower()
     print list1
