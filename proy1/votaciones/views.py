from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Pregunta, Respuesta
from django.views import generic

# Create your views here.
class IndexViews(generic.ListView):
    template_name = "votaciones/index.html"
    context_object_name = "lista_preguntas_recientes"

    def get_queryset(self):
        return Pregunta.objects.order_by("fecha_publicacion")

# def index(request):
#     lista_preguntas_recientes = Pregunta.objects.order_by("-fecha_publicacion")[:3]
#     # template = loader.get_template("votaciones/index.html")
#     context = {
#         "lista_preguntas_recientes": lista_preguntas_recientes,
#     }
#     return render(request, "votaciones/index.html", context)
#     # return HttpResponse(template.render(context, request))

class DetailView(generic.DateDetailView):
    model = Pregunta
    template_name = "votaciones/detail.html"

# def detail(request, pregunta_id):
#     # try:
#     #     pregunta = Pregunta.objects.get(pk = pregunta_id)
#     # except Pregunta.DoesNotExist:
#     #     raise Http404("Pregunta no encontrada")
#     pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
#     return render(request, "votaciones/detail.html", {"pregunta": pregunta})
#     # return HttpResponse("Estas en la pregunta %s" %pregunta_id)

class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = "votaciones/resultados.html"

# def results(request, pregunta_id):
#     # response = "Estas viendo el resultado de la pregunta %s"
#     # return HttpResponse(response % pregunta_id)
#     pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
#     return render(request, "votaciones/resultados.html", {"pregunta": pregunta})

def vote(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        respuesta_seleccionada = pregunta.respuesta_set.get(pk=request.POST['respuesta'])
    except (KeyError, Respuesta.DoesNotExist):
        return render(
            request,
            "votaciones/detail.html",
            {
                "pregunta": pregunta,
                "error_message": "No existe la opción seleccionada.",
            },
        )
    else:
        respuesta_seleccionada.votos = F("votos") + 1
        respuesta_seleccionada.save()
    # pregunta = pregunta.objects.get(pk = pregunta_id)
    # return HttpResponse("Estas votando en la pregunta %s" %pregunta_id)
    return HttpResponseRedirect(reverse("votaciones:results", args=[pregunta.id]))