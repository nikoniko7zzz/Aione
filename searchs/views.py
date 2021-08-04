from django.contrib.auth.decorators import login_required
from searchs.models import Search
from django.shortcuts import render, redirect, get_object_or_404
from searchs.forms import SearchForm

def top(request):
    searchs = Search.objects.all()
    context = {"searchs": searchs}
    return render(request, "searchs/top.html", context)

@login_required
def search_new(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.created_by = request.user
            search.save()
            return redirect(search_detail, search_id=search.pk)
    else:
        form = SearchForm()
    return render(request, "searchs/searchs_new.html", {'form': form})
    

# @login_required
def search_edit(request, search_id):
    search = get_object_or_404(Search, pk=search_id)
    # if search.created_by_id != request.user.id:
    #     return HttpResponseForbidden("このスニペットの編集は許可されていません。")

    if request.method == "POST":
        form = SearchForm(request.POST, instance=search)
        if form.is_valid():
            form.save()
            return redirect('search_detail', search_id=search_id)
    else:
        form = SearchForm(instance=search)
    return render(request, 'searchs/searchs_edit.html', {'form': form})


def search_detail(request, search_id):
    search = get_object_or_404(Search, pk=search_id)
    return render(request, 'searchs/searchs_detail.html',{'search': search})
    

