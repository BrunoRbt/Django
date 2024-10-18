from django.shortcuts import render
from django.http import HttpResponse  # Opcional, caso queira retornar respostas de teste

def index(request):
    # Renderiza o template 'index.html'
    return render(request, 'index.html')

def post_detail(request, id):
    # Aqui você renderiza o template 'post_detail.html', passando um objeto "post"
    # Supondo que você tenha um modelo "Post" no seu banco de dados
    # post = get_object_or_404(Post, id=id)
    # return render(request, 'post_detail.html', {'post': post})
    return render(request, 'post_detail.html')  # Simples, sem dados

# Se você precisar de mais views, como para o sidebar, você pode adicionar algo como:
def about(request):
    # Renderiza o template 'sidebar.html'
    return render(request, 'sidebar.html')
