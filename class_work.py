#
# class Squar:
#
#     def __init__(self, system='sm'):
#         self.system = system
#         self._height = 0
#         self._wight = 0
#         self._area = 0
#
#     @property
#     def height(self):
#         if self.system == 'sm':
#             return self._height
#         if self.system == 'm':
#             return self._height/100
#         if self.system == 'mm':
#             return self._height*100
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#
#     @property
#     def wight(self):
#         if self.system == 'sm':
#             return self._wight
#         if self.system == 'm':
#             return self._wight / 100
#         if self.system == 'mm':
#             return self._wight * 100
#
#     @wight.setter
#     def wight(self, value):
#         self._wight = value
#
#     @property
#     def area(self):
#         self._area = self._wight * self._height
#         return self._area
#
# sq = Squar('sm')
#
# sq._height = 10
# sq._wight = 5
# print(sq.area)
#
#
# sq = Squar('m')
#
# sq._height = 10
# sq._wight = 5
# print(sq.area)
#
#
# sq = Squar('mm')
#
# sq._height = 10
# sq._wight = 5
# print(sq.area)


