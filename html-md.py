import html2text
import os
import re

def get_filelist(dir):
    for home, dirs, files in os.walk(dir):
        for dir in dirs:
            print(dir)
        for filename in files:

            fullname = os.path.join(home, filename)
            if fullname.endswith('html'):
                with open(fullname, 'r', encoding='utf8') as f:
                    md = html2text.html2text(f.read())
                    pattern = r'-\n'
                    md_text = re.sub(pattern, '-', md)
                    with open(re.sub('html', 'md', fullname), 'w', encoding='utf8') as nf:
                        nf.write(md_text)
            
if __name__ == "__main__":
    get_filelist('c:/Users/42210/Desktop/Django课件V3.1/Django新课件')
