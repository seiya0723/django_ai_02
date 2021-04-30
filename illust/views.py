from django.shortcuts import render,redirect

## Create your views here.
#from django.shortcuts import render
from django.views import View

from .models import Design
from .forms import DesignForm

class illustView(View):

    def get(self, request, *args, **kwargs):

        #Designクラスを使用し、DBへアクセス、データ全件閲覧
        designs = Design.objects.all()

        button1     = "Prev"
        data        = "データのプレビュー"
        category    = "カテゴリ−１"
        category2   = "カテゴリ−2"
        category3   = "カテゴリ−3"

        context = {
                   "button1":button1,
                   "data":data,
                   "category1":category,
                   "category2": category2,
                   "category3": category3,

                   "designs":designs,

                   }

        return render(request,"illust/index.html",context)

    def post(self, request, *args, **kwargs):

        """
        if "title" in request.POST:
            posted  = Design( title = request.POST["title"] )
            posted.save()
        """

        form    = DesignForm(request.POST)
        
        if form.is_valid():
            print("バリデーションOK ")
            form.save()
        else:
            print("バリデーションNG")
        

        return redirect("illust:index")

index   = illustView.as_view()


#削除を行うビュークラス
class illustDeleteView(View):

    def post(self, request, pk, *args, **kwargs):

        design  = Design.objects.filter(id=pk).first()
        design.delete()

        return redirect("illust:index")

delete  = illustDeleteView.as_view()


#編集を行うビュークラス
class illustEditView(View):

    def get(self, request, pk, *args, **kwargs):

        design  = Design.objects.filter(id=pk).first()

        context = { "design":design }

        return render(request,"illust/edit.html",context)

    def post(self, request, pk, *args, **kwargs):

        
        #編集対象のレコードを特定する
        instance    = Design.objects.filter(id=pk).first()

        #キーワード引数instanceに編集対象のレコードを指定
        form        = DesignForm(request.POST, instance=instance)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")


        return redirect("illust:index")

edit    = illustEditView.as_view()
