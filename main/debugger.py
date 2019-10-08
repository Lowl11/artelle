class Debugger:

    @staticmethod
    def WriteLine(msg, pre = '0'):
        print('\n--------------------------------------------–')
        if pre != '0':
            print(pre + ':')
        print(msg)
        print('--------------------------------------------–\n')

    def __str__(self):
        return 'Static class debugger'
