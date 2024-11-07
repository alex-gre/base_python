
class MatPPR():

  def __init__(self):
      pass

  def topmenuppr (self):

      print('start')
      print("------------------------------------------------------------------------")
      print('Программа расчёта материала для системы отопления из пропиленновых труб.')                   
      print(' n - new   Новый объект')      
      print('------------------------------------------------------------------------')   
  
  def inpmenuppr(self):

      self.objname = input ('Название объекта: ')
      self.s_home = int(input ('Площадь помещения: '))
      self.kotl_w = self.s_home/10
      self.n_radiator = int(input('Введите количество радиаторов...'))
      self.truba_d20 = int(input('Введите метраж трубы диам. 20 мм...'))
      self.truba_d25 = int(input('Введите метраж трубы диам. 25 мм...'))
      self.truba_d32 = int(input('Введите метраж трубы диам. 32 мм...'))
      self.mknr = self.n_radiator*2
      self.ugolok_prjam20 = self.n_radiator*6
      self.ugolok_kosoy20 = self.n_radiator*3
      self.klipsa20 = self.truba_d20*2
      self.klipsa25 = self.truba_d25*2
      self.klipsa32 = self.truba_d32*2
      self.dupel_gvozd = self.klipsa20+self.klipsa25+self.klipsa32
      self.silicon_len = self.n_radiator % 5
      if self.n_radiator < 5 :
          self.silicon_len = 1 
          self.mufta_20 = 2
          self.mufta_25 = None
          self.mufta_32= None
      else:    
          self.mufta_20 = int(self.truba_d20/3)
          self.mufta_25 = int(self.truba_d25/3)
          self.mufta_32 =int(self.truba_d32/3) 
      
      
     
  def outpppr(self):

      print('===================================================\n')
      print(f"Список материала для объекта: {self.objname} сформирован.")
      print(f"Мощьность котла: {self.kotl_w} киловатт")
      print('на объект расчитано... \n')
      print(f"радиаторов: {self.n_radiator} шт.")
      print('для обвязки радиаторов потребуется, след. материал...')
      print(f"кранов запорных: {self.n_radiator} шт.")
      print(f"кранов терморег: {self.n_radiator} шт.")
      print(f'муфта диам. 20 мм. комбин.с наружней резьбой диам 1/2" {self.mknr} шт.')
      print(f'уголок 90 гр. {self.ugolok_prjam20} шт.')
      print(f'уголок 45 гр. {self.ugolok_kosoy20} шт.')
      print('для магистрального трубопровода потребуется... ')
      print('----------------------------------------------------------')
      print(f'труба диам. 20: {self.truba_d20} метров')
      print(f'труба диам. 25: {self.truba_d25} метров')
      print(f'труба диам. 32: {self.truba_d32} метров')
      print(f'клипса диам. 20: {self.klipsa20} шт. ')
      print(f'клипса диам. 25: {self.klipsa25} шт. ')
      print(f'клипса диам. 32: {self.klipsa32} шт. ')
      print(f'дюпель-гвоздь 6/60 мм.: {self.dupel_gvozd} шт.')
      print(f'энергофлекс диам. 22 мм.: {self.truba_d20} метров')
      print(f'энергофлекс диам. 28 мм.: {self.truba_d25} метров')
      print(f'энергофлекс диам. 35 мм.: {self.truba_d32} метров')
      print('предварительный список по материалу сформирован и сохранён в файле raschet.txt')
      
      # контекстный менеджер py3
      with open("otchet.txt", 'w') as fout:

         fout.write('//////////////////////////////////////////////////////////\n')
         fout.write('/         Список материала на систему отопления.         /\n')
         fout.write('//////////////////////////////////////////////////////////\n')
         fout.write(f'Наименование объекта: {self.objname}\n')
         fout.write(f'Мощьность котла: от {str(self.kotl_w)} киловатт\n')
         fout.write('----------------------------------------------------------\n')
         fout.write(f'радиаторов: {str(self.n_radiator)} шт.\n')
         fout.write(f'для обвязки радиаторов потребуется, след. материал...\n')
         fout.write(f'кранов запорных: {str(self.n_radiator)} шт.\n')
         fout.write(f'кранов терморег: {str(self.n_radiator)} шт.\n')
         fout.write(f'муфта диам. 20 мм. комбин.с наружней резьбой диам 1/2" '+str(self.mknr)+' шт.\n')
         fout.write(f'уголок 90 гр. {str(self.ugolok_prjam20)} шт.\n')
         fout.write(f'уголок 45 гр. {str(self.ugolok_kosoy20)} шт.\n')
         fout.write(f'----------------------------------------------------------\n')
         fout.write('для магистрального трубопровода потребуется... \n')
         fout.write(f'труба диам. 20: {str(self.truba_d20)} метров\n')
         fout.write(f'труба диам. 25: {str(self.truba_d25)} метров\n')
         fout.write(f'труба диам. 32: {str(self.truba_d32)} метров\n')
         fout.write(f'клипса диам. 20: {str(self.klipsa20)} шт.\n')
         fout.write(f'клипса диам. 25: {str(self.klipsa25)} шт.\n')
         fout.write(f'клипса диам. 32: {str(self.klipsa32)} шт.\n')
         fout.write(f'муфта диам. 20: {str(self.mufta_20)} шт.\n')
         fout.write(f'муфта диам. 25: {str(self.mufta_25)} шт.\n')
         fout.write(f'муфта диам. 32: {str(self.mufta_32)} шт.\n')
         fout.write(f'дюпель-гвоздь 6/60 мм.: {str(self.dupel_gvozd)} шт.\n')
         fout.write(f'энергофлекс диам. 22 мм.: {str(self.truba_d20)} метров\n')
         fout.write(f'энергофлекс диам. 28 мм.: {str(self.truba_d25)} метров\n')
         fout.write(f'энергофлекс диам. 35 мм.: {str(self.truba_d32)} метров\n')
         fout.write(f'силикон + лён {str(self.silicon_len)} шт.\n')
         fout.write(f'----------------------------------------------------------\n')
         fout.write(f'дополнительный список заполнить по месту\n')
         fout.write('///////////////////////////////////////////////////////////////\n')
         fout.write('/тройник 20 мм                                                /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/тройник 25 мм                                                /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/тройник 32 мм                                                /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/уголок  20 мм                                                /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/уголок  25 мм                                                /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/уголок  32 мм                                                /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/                                                             /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/                                                             /\n')
         fout.write('---------------------------------------------------------------\n')
         fout.write('/                                                             /\n')
