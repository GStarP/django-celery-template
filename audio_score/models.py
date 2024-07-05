from django.db import models


class AudioScore(models.Model):
    # pk
    conf_id = models.CharField(max_length=32, verbose_name='会议ID')
    audio_id = models.CharField(max_length=64, verbose_name='音频ID')
    # for better locating
    user_id = models.CharField(max_length=16, blank=True, null=True, verbose_name='工号')
    # score
    model = models.CharField(max_length=16, default='NISQAv2', verbose_name='模型')
    mos = models.FloatField(blank=True, null=True, verbose_name='主观评分')
    noi = models.FloatField(blank=True, null=True, verbose_name='噪声评分')
    dis = models.FloatField(blank=True, null=True, verbose_name='连续评分')
    col = models.FloatField(blank=True, null=True, verbose_name='失真评分')
    loud = models.FloatField(blank=True, null=True, verbose_name='响度评分')

    def __str__(self):
        return f'{self.conf_id} | {self.audio_id}'

    class Meta:
        verbose_name = verbose_name_plural = '音频评分'
