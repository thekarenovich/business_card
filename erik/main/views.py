from django.shortcuts import render, redirect

from .models import Theme


def index(request):

    color_bg = ''
    color_fg = ''
    color_win = ''
    if Theme.objects.filter(user=request.user.username).exists():
        color_bg = Theme.objects.get(user=request.user.username).color
        if color_bg == '#212529':
            color_fg = '#ffffff'
            color_win = '#1E1F1F'

        elif color_bg == '#ffffff':
            color_fg = '#212529'
            color_win = '#EEEEEE'

    return render(request, 'main/index.html', {'color_bg': color_bg, 'color_fg': color_fg,
                                               'color_win': color_win})


def theme(request):
    color = request.GET.get('color')

    if color == 'dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme = Theme.objects.get(user=request.user.username)
            user_theme.user = request.user.username
            user_theme.color = '#212529'
            user_theme.save()
        else:
            user2 = Theme(user=request.user.username, color='black')
            user2.save()

    elif color == 'light':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme1 = Theme.objects.get(user=request.user.username)
            user_theme1.user = request.user.username
            user_theme1.color = '#ffffff'
            user_theme1.save()
        else:
            user4 = Theme(user=request.user.username, color='white')
            user4.save()

    return redirect('/')
