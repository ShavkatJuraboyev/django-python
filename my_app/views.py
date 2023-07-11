from django.http import HttpResponse
from django.shortcuts import render
from .models import University, Yonalishlar, Fanyonalishlar

# Create your views here.
def my_site(request):
    posts = University.objects.all()
    print(posts)
    post_list = """
    <h1 style="text-align: center; color: blue;">Asosiy saxifa</h1>
    <h2 style="text-align: center; ">Unversitetlar ro'yxati</h2>
    
    """
    for post in posts:
        post_list += f"""<li><a style="text-decoration: none; font-size: 20px;" href="tatusf/">{post}</li><hr><hr>"""
        print(post)

    post_list += """<br><li><a style="text-decoration: none; font-size: 20px;" href="admin/">Users</a></li><hr>"""
    return HttpResponse(f"""<ul style="list-style-type: none;">{post_list}</ul>""")


def first_site(request):
    yonalish = Yonalishlar.objects.all()
    http = """<h1 style="text-align: center; color: blue;">Toshkent axborot texnologiyalari universiteti Samarqanddagi filiali</h1>
            <h2 style="text-align: center; ">Bakalavriatura:</h2>"""
    for i in yonalish:
        http += f"""
        <li><a style="text-decoration: none; font-size: 20px;" href="ax/">{i}</a></li><hr><br>
    """
    http += """<li><a style="text-decoration: none; font-size: 20px; color:blue;" href="../">Unversitetlar ro'yxati</a></li><hr>"""

    return HttpResponse(f"""<ul style="list-style-type: none;">{http}</ul>""")


def fanlar(request):
    fan = Fanyonalishlar.objects.all()
    http = """
       <h1 style="text-align: center; color: blue;">Toshkent axborot texnologiyalari universiteti Samarqanddagi filiali</h1>
       <h2 style="text-align: center; ">Axborot xavfsizligi </h2>
       <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>"""
    for i in fan:
        http += f"""
               <li style="color: rgb(79, 2, 2); font-size: 20px;">{i}</li>
           """

    http += """
        <ul style="list-style-type: none;">
           <li><a style="text-decoration: none; font-size: 20px;" href="../">Bakalavr ro'yxatlari</a></li><hr>
           <li><a style="text-decoration: none; font-size: 20px;" href="../../">Unversitetlar ro'yxati</a></li><hr>
         </ul>
       """
    return HttpResponse(f"""<ul style="list-style-type: none;">{http} </ul>""")