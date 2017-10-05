import xml.etree.ElementTree as ET

tree = ET.parse('Abarelix_ddi.xml')
root = tree.getroot()


for sentence in root.findall('sentence'):
        rank = sentence.find('pair')
        if rank is  None:
           root.remove(sentence)

tree.write('maniteja.xml')
