import requests
from bs4 import BeautifulSoup
#LINKS
# https://www.makita.pt/products/l%C3%ADtio-ion.html?fav=&brand_prefix=&overview_config_id=1&search=&svalue=&geo_svalue=&geo_distance=&page_size=&sort=&group_id=21090&extra_field=&sort_tech=&fromfilter=&voucher=&paging_page=1
# https://www.makita.pt/products/l%C3%ADtio-ion.html?fav=&brand_prefix=&overview_config_id=1&search=&svalue=&geo_svalue=&geo_distance=&page_size=&sort=&group_id=21090&extra_field=&sort_tech=&fromfilter=&voucher=&paging_page=2
# https://www.makita.pt/products/carregadores.html
req = requests.get('https://www.makita.pt/products/l%C3%ADtio-ion.html?fav=&brand_prefix=&overview_config_id=1&search=&svalue=&geo_svalue=&geo_distance=&page_size=&sort=&group_id=21090&extra_field=&sort_tech=&fromfilter=&voucher=&paging_page=1')
if req.status_code == 200:
    print('Success!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
prodDivs = soup.findAll("div", {"class" : "product-title"})
f = open("baterias.csv", "a")
for el in prodDivs:
    i = 0
    req = requests.get('https://www.makita.pt/'+el.a['href'])
    if req.status_code == 200:
        content = req.content
    prodSoup = BeautifulSoup(content, 'html.parser')
    prodTitle = prodSoup.find("div", {'class': 'product-title'}).h1.contents[0]
    prodSku = prodSoup.find('span', {'class': 'product-number'}).contents[0]
    prodImg = prodSoup.find('a', {'class': 'fancybox'}).img['src']
    f.write('"","'+prodTitle+'","", "'+prodTitle+'", "", "", "", "", "Makita", "", "Makita", "'+prodImg+'", "NO", "NO", "disabled", "'+prodSku+'", "1.0", "0", "YES", "0.0", "Informação técnica", "<table class=table-striped> <thead> <th scope=col>Especificação</th><th scope=col>Valor</th>  </thead><tr>"')
    prodSpecs = prodSoup.findAll('div', {'class': 'techspecs--row-specification'})
    prodSpecsValues = prodSoup.findAll('div', {'class': 'techspecs--row-value'})
    for spec in prodSpecs:
        try:
          f.write("<td>")
          f.write(spec.contents[0])
          f.write("</td>")
          f.write("<td>")
          f.write(prodSpecsValues[i].contents[0])
          f.write("</td>")
        except TypeError:
          f.write("<td>")
          f.write(spec.contents[0])
          f.write("</td>")
          f.write("<td>")
          f.write("Sim")
          f.write("</td>")
        i+=1
    f.write('</tr></tbody></table>","","","",""')
    print("DONE")
f.close()
