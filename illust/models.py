from django.db import models
from django.utils import timezone
# Create your models here.
class Design(models.Model):
    # テーブル名の定義
    class Meta:
        db_table = "design"

    # カラム(フィールド)の定義
    title = models.CharField(verbose_name="タイトル", max_length=100)
    date = models.DateTimeField(verbose_name="時間",default=timezone.now)

    # TODO:後々ここにAI,PSを判定するMIMEの値、FileField、投稿者のユーザーIDなどのカラム(フィールド)を定義する。

    def __str__(self):
        return self.title
