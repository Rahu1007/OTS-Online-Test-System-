from unittest import loader
from django.template import loader # type: ignore
from django.shortcuts import render,redirect # type: ignore
from django.http import HttpResponse ,HttpResponseRedirect # type: ignore
from OTS.models import *
from .models import Candidate  # Ensure the Candidate model is imported
import random
from .models import Question
from .models import Question, Result, Candidate

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())
def candidateRegistrationForm(request):
    res=render(request,'registrationForm.html')
    return res

def candidateRegistration(request):
    if request.method == 'POST':
        # Fetch the username from the POST request
        username = request.POST.get('username', '')  # Safely get the value with a default
        
        # Check if the username already exists
        if Candidate.objects.filter(username=username).exists():
            userStatus = 1  # User already exists
            #Scenario 1: If the username already exists, it should return userStatus = 1.

        else:
            # Create and save a new candidate
            candidate = Candidate()
            candidate.username = username
            candidate.password = request.POST.get('password', '')  # Avoid directly assigning
            candidate.name = request.POST.get('name', '')
            candidate.save()
            userStatus = 2  # User successfully registered
            #Scenario 2: If the user successfully registers, it should return userStatus = 2.
    else:
        userStatus = 3  # Invalid request method
             #Scenario 3: If the request method is not POST (e.g., GET), it should return userStatus = 3.

    # Pass the user status to the template
    context = {
        'userStatus': userStatus
    }
    # Render the response
    return render(request, 'registration.html', context)

            

# def loginView(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         candidate=Candidate.objects.filter(username=username,password=password)
#         if len(candidate)==0:
#                 loginError="Invalid username or Password"
#                 res=render(request, 'login.html',{'loginError':loginError})
#         else:
#             request.session['username']=candidate[0].username
#             request.session['name']=candidate[0].name
#             res=HttpResponseRedirect('home')
#             res = redirect('OTS:home')  # type: ignore # Use Django's `redirect` function with the namespaced URL

#     else:
#         res=render(request, 'login.html')  # Render the login template
#     return res


def loginView(request):
    if request.method == 'POST':
        # Fetch the username and password from the POST data
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Filter candidates with the given username and password
        candidate = Candidate.objects.filter(username=username, password=password).first()

        if not candidate:
            # If no candidate is found, show an error message
            loginError = "Invalid username or password"
            res = render(request, 'login.html', {'loginError': loginError})
        else:
            # If a valid candidate is found, set session data and redirect to 'home'
            request.session['username'] = candidate.username
            request.session['name'] = candidate.name
            res = redirect('OTS:home')  # type: ignore # Use named URL for better maintainability
    else:
        # Render the login template for GET requests
        res = render(request, 'login.html')
    
    return res



def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    else:
        res=render(request,'home.html')
    return res
    


def testPaper(request):
    # Check if the user is logged in
    if 'name' not in request.session.keys():
        return HttpResponseRedirect("login")  # Redirect to login if not logged in

    # Get the number of questions to display
    n = int(request.GET.get('n', 1))  # Default to 1 question if 'n' is not provided

    # Fetch and shuffle questions
    question_pool = list(Question.objects.all())  # Corrected 'objects'
    random.shuffle(question_pool)
    question_list = question_pool[:n]  # Select the required number of questions

    # Prepare the context and render the template
    context = {'questions': question_list}
    return render(request, 'test_paper.html', context)



# def calculateTestResult(request):
#     if 'name' not in request.session.keys():
#         return HttpResponseRedirect("login")
#     total_attempt=0
#     total_right=0
#     total_wrong=0
#     qid_list=[]
#     for k in request.POST:
#         if k.startswith('qno'):
#             qid_list.append(int(request.POST[k]))
#     for n in qid_list:
#         questions=Question.objects.get(qid=n) 
#         try:
#             if questions.ans==request.POST['q'+str(n)]:
#                 total_right+=1
#             else:
#                 total_wrong+=1
#             total_attempt+=1
#         except:
#             pass
#     points=(total_right-total_wrong)/len(qid_list)*10
#     #store  result in Result Table
#     result=Result()
#     result.username=Candidate.objects.get(username=request.session['username'])
#     result.attempt=total_attempt
#     result.right=total_right
#     result.wrong=total_wrong
#     result.points=points
#     result.save()
#     #update
#     candidate=Candidate.objects.get(username=request.session['username'])
#     candidate.test_attempted=+1
#     candidate.points=(candidate.points*(candidate.test_attempted-1)+points)/candidate.test_attempted
#     candidate.save()
#     return HttpResponseRedirect('result')

def calculateTestResult(request):
    # Check if the user is logged in
    if 'name' not in request.session.keys():
        return redirect('OTS:login')  # Redirect to the login page using namespace

    total_attempt = 0
    total_right = 0
    total_wrong = 0
    qid_list = []

    # Extract question IDs from the POST request
    for k in request.POST:
        if k.startswith('qno'):
            try:
                qid_list.append(int(request.POST[k]))
            except ValueError:
                pass  # Handle any non-integer values gracefully

    # Calculate results for each question
    for qid in qid_list:
        try:
            question = Question.objects.get(qid=qid)  # Get the question object
            user_answer = request.POST.get(f'q{qid}', None)  # Fetch user's answer
            if user_answer == question.ans:
                total_right += 1
            else:
                total_wrong += 1
            total_attempt += 1
        except Question.DoesNotExist:
            pass  # Ignore missing questions

    # Avoid division by zero in points calculation
    points = 0
    if qid_list:
        points = ((total_right - total_wrong) / len(qid_list)) * 10

    # Store the result in the Result table
    try:
        result = Result()
        result.username = Candidate.objects.get(username=request.session['username'])
        result.attempt = total_attempt
        result.right = total_right
        result.wrong = total_wrong
        result.points = points
        result.save()
    except Candidate.DoesNotExist:
        return redirect('OTS:login')  # Redirect to login if candidate does not exist

    # Update the Candidate table
    try:
        candidate = Candidate.objects.get(username=request.session['username'])
        candidate.test_attempted += 1  # Increment test_attempted
        candidate.points = (
            (candidate.points * (candidate.test_attempted - 1) + points) 
            / candidate.test_attempted
        )
        candidate.save()
    except Candidate.DoesNotExist:
        return redirect('OTS:login')  # Redirect to login if candidate does not exist

    # Redirect to the result page
    return redirect('OTS:result')






    
def testResultHistory(request):
    # Check if the user is logged in
    if 'username' not in request.session:
        return redirect('OTS:login')  # Redirect to the login page

    try:
        # Get the logged-in candidate
        candidate = Candidate.objects.get(username=request.session['username'])

        # Fetch all test results for the candidate, ordered by resultid (latest first)
        results = Result.objects.filter(username=candidate).order_by('-resultid')

        # Prepare context for rendering
        context = {
            'candidate_name': candidate.name,
            'results': results,
            'candidate':candidate,
        }
        return render(request, 'test_history.html', context)

    except Candidate.DoesNotExist:
        # Redirect to login if candidate does not exist
        return redirect('OTS:login')



def showTestResult(request):
    def showTestResult(request):
    # Check if the user is logged in
        if 'username' not in request.session:
            return redirect('OTS:login')  # Redirect to the login page

    try:
        # Retrieve the candidate's result from the database
        candidate = Candidate.objects.get(username=request.session['username'])
        result = Result.objects.filter(username=candidate).last()  # Fetch the latest result

        if not result:
            # If no result exists, handle the scenario
            context = {'error': "No test results found."}
            return render(request, 'result.html', context)

        # Prepare context for the result page
        context = {
            'attempt': result.attempt,
            'right': result.right,
            'wrong': result.wrong,
            'points': result.points,
            'candidate_name': candidate.name,
        }
        return render(request, 'result.html', context)

    except Candidate.DoesNotExist:
        # Redirect to login if candidate does not exist
        return redirect('OTS:login')






def logoutView(request):
  
    if 'name' in request.session:
        del request.session['username']  # Safely delete 'username' key
        del request.session['name']     # Safely delete 'name' key

    # Redirect to the login page
    return HttpResponseRedirect("/OTS/login/")
