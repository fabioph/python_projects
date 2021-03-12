from bs4 import BeautifulSoup

f = open("comments.txt", "r", encoding='utf8')
content = f.read()
soup = BeautifulSoup(content, 'html.parser')
users = {}
for i in range(1,2472):
    user = soup.find("span", {'id': 'username-'+str(i)})
    users[user.contents[0]] = []
for i in range(1,2472):
    user = soup.find("span", {'id': 'username-'+str(i)})
    comment = soup.find('span', {'id': 'caption-'+str(i)})
    for userCommented in comment.contents[0].split(" "):
        if userCommented:
            if userCommented in users[user.contents[0]]:
                print(user.contents[0]+" repetiu um nome!: "+userCommented)
            else:
                users[user.contents[0]].append(userCommented)
print("Total de participantes: "+str(len(users)))
f.close()
exit(1)
