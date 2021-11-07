#http://elib.shpl.ru/pages/3131833/zooms/8 832
import requests
hd = {
        'User-Agent': 'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)'
      }
def save_from_www(link):
    filename = link.split('/')[-3] + ".jpg"
    print(filename)
    r = requests.get(link, headers=hd, allow_redirects=True)
    open(filename, "wb").write(r.content)



n=3131457
while n <= 3131459:
    n += 1
    link3 = 'http://elib.shpl.ru/pages/' + str(n) + '/zooms/8'
    print (n)
    print (link3)
    save_from_www(link3)



# link3 = 'http://elib.shpl.ru/pages/3131459/zooms/8'
# save_rom_www(link3)


