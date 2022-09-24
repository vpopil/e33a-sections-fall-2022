from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import markdown2


class NewCategoryForm(forms.Form):
    category = forms.CharField(label="New Category", required=True)
    allowance = forms.IntegerField(
        label="Allowance",  min_value=1, max_value=1000)


# Create your views here.
def index(request):
    if "categories" not in request.session:
        request.session["categories"] = []

    # Converting md to html
    md_string = "`Hello Section`"  # custom MD
    html_string = markdown2.markdown(md_string)

    return render(request, "budget/index.html", {"categories": request.session["categories"],
                                                 "html_string_abc": html_string
                                                 })

    #    y = function_to_mulitply(5)
    # md_string = "`Hello Section`"


def function_to_mulitply(x):
    x *= 2
    return x


def add(request):
    """ this function does abc... """
    # count = 1

    if request.method == "POST":
        # Fetch the form ...
        form = NewCategoryForm(request.POST)

        # Validation form and saving the budget cate
        if form.is_valid():
            category = form.cleaned_data["category"]

            print(form.cleaned_data["category"])
            print(form.cleaned_data["allowance"])

            request.session["categories"] += [category]
            # count += 1
            # my_greeting = "Hello"

            # return render(request, "budget/index.html", {})# not good

            return HttpResponseRedirect(reverse("budget:index"))

        return render(request, "budget/add.html", {
            "form": form
        })

    return render(request, "budget/add.html", {
        "form": NewCategoryForm()
    })


# Random mention:
# '/wiki/add/<str:title>'
# '/wiki/edit/<str:title>'


# '/wiki/<str:title>'
# '/wiki/<str:title>/edit'

# '/random'

# #No good:
# '/<str:title>'


#
# def entry(request, title):
#     # print(title)
#     # pull file
#     # make into html
#     # render
