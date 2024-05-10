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
def mark_completed(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    user = request.user
    if request.method == 'POST':
        # تحديث حالة الدرس إلى مكتمل للمستخدم الحالي
        UserLessonCompletion.objects.create(user=user, lesson=lesson, completed=True)
        # قم بتحديث البيانات أو إعادة التوجيه حسب احتياجاتك (هنا نعيد توجيه المستخدم إلى الدرس التالي)
        next_lesson = Lesson.objects.filter(id__gt=lesson_id).first()
        if next_lesson:
            return redirect('lesson_details', lesson_id=next_lesson.id)
        else:
            return redirect('home')  # توجيه إلى الصفحة الرئيسية أو أي صفحة تحددها
    return render(request, 'lessons/mark_completed.html', {'lesson': lesson})
