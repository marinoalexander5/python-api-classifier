import os, argparse, urllib, requests


class Unsplash():
    def __init__(self):
        self.website = 'www.unsplash.com'
        self.session = requests.Session()
        
    def __call__(self, search, pages=None):
        base_url = self.website + f'/napi/search/photos?query={search}&xp=&per_page=20&'
        if not pages:
            pages = self.session.get(base_url).json()['total_pages']
        urls = []
        for page in trange(1, pages, desc = "Downloading image URLs"):
            search_url = self.website + f'/napi/search/photos?query={search}&xp=&per_page=20&page={page}'
            response = self.session.get(search_url)
            
            if response.status_code == 200:
                results = response.json()['results']
                urls = urls + [(url['id'], url['urls']['regular']) for url in results]
            
        return list(set(urls))

unsplash = _Unsplash()

class _download_images(object):
    def __init__(self, output_dir, query):
        self.query = query
        self.directory = output_dir + '/' + query
        if not os.path.isdir(self.directory): os.makedirs(self.directory)

    def __call__(self, urls):
        with ProcessPoolsExecutor() as pool:
            downloads = [pool.submit(urllib.request.urlretrieve, url[1]), self.directory + '/' + url[0] + '.jpg') for url in urls]
            for download in tqdm(as_completed(downloads, total=len(downloads), desc='Downloading ' + self.query + 'images...' ):
                pass
            
class _scrape(object):
    def __call__(self, args):
        if args.w.lower() == 'unsplash': 
            urls = unsplash.args.q.lower(), args.p)
            download_imgs = _download_images(args.o, args.q.lower())
            download_imgs(urls)

scrape = _scrape()

if name in __main__:
    parser = argsparse.ArgumentParser(description='Web Scraping')
    parser.add_argument(-w, default='unsplash', choices=['unsplash'], metavar='website', required=False, type=str, 
    help='nombre de la página web de la cual quieres colectar datos, ejemplo: unsplash')
    parser.add_argument(-q, metavar='query', required=True, type=str, 
    help='palabra clave a buscar (se recomienda que la misma sea en inglés), ejemplo: sunset')
    parser.add_argument(-o, default='./scraping-output' metavar='output directory', required=True, type=str, 
    help='path del directorio en el cual deseas guardar los datos colectados, si la carpeta no existe se creará automáticamente ')
    parser.add_argument(-p, metavar='no of pages', type=int, 
    help='número de páginas de la cual quieres colectar datos')

args = parser.pase_args()
scrape(args)