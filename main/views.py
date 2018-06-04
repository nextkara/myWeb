from django.shortcuts import render

# Create your views here.
def testWeb(Request):
    return render(Request,'index.html')


def testHelp(Request):
    return render(Request, 'help.html')

def testWorklist(Request):
    return render(Request, 'worklist.html')

def testUpload(Request):
    return render(Request, 'upload.html')

def testDownload(Request):
    return render(Request, 'download.html')