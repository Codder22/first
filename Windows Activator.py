from pywebio import start_server
from pywebio.input import input, textarea
from pywebio.output import put_text
import time

def win():
    while True:
        type = input('Какой Windows вы желаете активировать?',type='text')
        if type == 'Windows 10' or 'виндувс 10' or 'Виндувс 10' or 'windows 10' :
            type2 = input('Введите класс вашей Windows:')
            if type2 == 'pro' or 'Pro':
                put_text('Подготавливаем инструкцию по ативации вашей windows...')
                time.sleep(2)
                put_text('Пожалуйста откройте командную строку (ВНИМАНИЕ - ВАЖНО ОТКРЫТЬ ЕЁ С ПРАВАМИ АДМИНИСТРАТОРА) ')
                time.sleep(3)
                put_text('Введите данную команду - slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX  и нажмите enter. ')
                time.sleep(2)
                put_text('Введите введите следующую команду - slmgr /skms kms.digiboy.ir  и нажмите. ')
                time.sleep(2)
                put_text('Введите еще одну команду - slmgr /ato и нажмите enter.')
                time.sleep(2)
                put_text('если активация не прошла попробуйте заменить вторую команду на одну из этих - 1) slmgr /skms zh.us.to  2) slmgr /skms kms.xspace.in')
                time.sleep(1)
                put_text('Поздравляем вы активировали виндувс совершенно бесплатно! Если же что то не получилось внимательно пересмотриет инструкцию и попробуйте снова.')
                time.sleep(40)
if __name__ == '__main__':
        win()