from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Project,Idea,Conclusion
from django.shortcuts import render, get_object_or_404
from .forms import IdeaForm,ConclusionForm
from django.db.models import Q



# index

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Idea
    ordering = ['-created_at']
    template_name = 'box/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["projects"] = Project.objects.all()
        return context



# Project

class CreateProject(LoginRequiredMixin, generic.edit.CreateView):
    model = Project
    fields = ['name', 'goal', 'limit']
    template_name = 'box/project_create.html'

    def form_valid(self, form):
        return super(CreateProject, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["projects"] = Project.objects.all()
        return context

class ProjectList(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'box/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class DetailProject(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'box/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class UpdateProject(LoginRequiredMixin, generic.edit.UpdateView):
    model = Project
    fields = ['name', 'goal', 'limit']

    template_name = 'box/project_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class DeleteProject(LoginRequiredMixin, generic.edit.DeleteView):
    model = Project
    success_url = reverse_lazy('index')

    template_name = 'box/project_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context


# Idea

@login_required
def post_idea(request, pk):
    project = get_object_or_404(Project, pk=pk)
    projects = Project.objects.all()
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.project = project
            idea.save()
            return redirect('project_list', pk=project.pk)
    else:
        form = IdeaForm()
    return render(request, 'box/idea_form.html', {'form': form, 'projects': projects})

class DetailIdea(LoginRequiredMixin, generic.DetailView):
    model = Idea
    template_name = 'box/idea_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class UpdateIdea(LoginRequiredMixin, generic.edit.UpdateView):
    model = Idea
    fields = ['idea', 'description', 'image', 'file']  # '__all__'

    template_name = 'box/idea_form.html'

    def dispatch(self, request, *args, **kwargs):
        # ownership validation
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')

        return super(UpdateIdea, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

@login_required
def delete_confirm_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'box/idea_delete.html', {'idea': idea, 'projects': Project.objects.all()})

@login_required
def delete_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('project_list', pk=idea.project.pk)



# Conclusion

@login_required
def conclusion(request, pk):
    project = get_object_or_404(Project, pk=pk)
    projects = Project.objects.all()
    if request.method == "POST":
        form = ConclusionForm(request.POST, request.FILES)
        if form.is_valid():
            conc = form.save(commit=False)
            conc.project = project
            conc.save()
            # project.finish()
            return redirect('project_list', pk=project.pk)
    else:
        form = ConclusionForm()
    return render(request, 'box/conc_form.html', {'form': form, 'projects': projects})

class DetailConclusion(LoginRequiredMixin, generic.DetailView):
    model = Conclusion
    template_name = 'box/conc_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class UpdateConclusion(LoginRequiredMixin, generic.edit.UpdateView):
    model = Conclusion
    fields = ['conclusion', 'description', 'image', 'file']

    template_name = 'box/conc_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class DeleteConclusion(LoginRequiredMixin, generic.edit.DeleteView):
    model = Conclusion
    template_name = 'box/conc_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context



# Board

class CreateBoard(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'box/board.html'


# Archive

class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Project
    ordering = ['-created_at']
    template_name = 'box/archive.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["projects"] = Project.objects.all()
        return context
