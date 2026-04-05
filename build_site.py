
# This script writes the improved House Optic site
html = open('/home/user/test/index.html', 'w', encoding='utf-8')
html.write(CONTENT)
html.close()
print("Written", len(CONTENT), "chars")
