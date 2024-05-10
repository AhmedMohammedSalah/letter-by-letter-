from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import Lesson, UserLessonCompletion
from django.contrib.auth.decorators import login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'lessons/lesson_detail.html', context)
@login_required
def reading_lessons(request):
    reading_lessons = Lesson.objects.filter(lesson_type='reading')
    context = {'lessons': reading_lessons}
    return render(request, 'lessons/reading_lessons.html', context)

@login_required
def listening_lessons(request):
    listening_lessons = Lesson.objects.filter(lesson_type='استماع')
    context = {'lessons': listening_lessons}
    return render(request, 'lessons/listening_lessons.html', context)
@login_required
def writing_lessons(request):
    listening_lessons = Lesson.objects.filter(lesson_type='كتابة')
    context = {'lessons': writing_lessons}
    return render(request, 'lessons/listening_lessons.html', context)

@login_required

def mark_lesson_completed(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user = request.user  # Assuming you have a logged-in user
    
    # Check if there's an existing completion record
    completion_record, created = UserLessonCompletion.objects.get_or_create(user=user, lesson=lesson)
    
    if not completion_record.completed:
        completion_record.completed = True
        completion_record.save()
    
    # Find the next lesson of the same type
    next_lesson = Lesson.objects.filter(lesson_type=lesson.lesson_type, id__gt=lesson_id).first()
    
    if next_lesson:
        return redirect('lesson_detail', lesson_id=next_lesson.id)
    else:
        # Redirect to a suitable page if no next lesson is found
        return redirect('home')  # Replace 'home' with the desired URL name