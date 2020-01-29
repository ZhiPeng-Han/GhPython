__author__ = "billpower"
__version__ = "2019.12.25"

#import rhinoscriptsyntax as rs

lst = list(range(10))
print(lst)

lst[5] = 99

lstnone = lst + [None]*6    #��Ҫ�����������ݵ�����ֵʱ��ͨ������none��ֵ
print(lstnone)

lstnone[-6:-2] = list(range(100,106,2)) #��Ƭ��ֵ������ͬʱ�滻�����ֵ

lstnone[:3] = []    #��ֵ�б�Ϊ�գ�����ɾ��ָ������ֵ
print(lstnone)

lstnone[1:1] = [0,0,-3,-4]  #ָ����ʼ�������ͬʱ���൱�ڲ�����ֵ
print(lstnone)

del lstnone[-2:]    #delɾ��ָ��ֵ
print(lstnone)
