triad_chord=['major','minor','dim','aug']
seventh_chord=['major_seventh','dominant_seventh','minor_seventh','dim_minor_seventh','diminished_seventh']
sharpe_flat_kind=['','sharpe','double_sharpe','double_flat','flat']
base_note=['c','d','e','f','g','a','b']
class Chords_that_cannot_be_formed:
    def __init__(self,chord_name,root_note,sharpe_flat):
        self.base_note=['c','d','e','f','g','a','b','c1','d1','e1','f1','g1','a1','b1']
        self.base_note_num=[1,3,5,6,8,10,12,13,15,17,18,20,22,24]
        self.sharpe_flat_num=[0,1,2,-2,-1]
        self.root_note=root_note
        self.sharpe_flat=sharpe_flat
        self.chord_name=chord_name
    def convert_note_num(self,root_note,sharpe_flat):
        note_num=self.base_note_num[self.base_note.index(root_note)]
        sharpe_flat_num=self.sharpe_flat_num[sharpe_flat_kind.index(sharpe_flat)]
        note_num_all=note_num+sharpe_flat_num
        return note_num_all
    def create_chord_num(self):
        # 先把根音转换成数字
        note_num=self.convert_note_num(self.root_note,self.sharpe_flat)
        # 罗列不同种类的和弦
        if self.chord_name=='major':
            add_l=[4,3]
        if self.chord_name=='minor':
            add_l=[3,4]
        if self.chord_name=='dim':
            add_l=[3,3]
        if self.chord_name=='aug':
            add_l=[4,4]
        if self.chord_name=='major_seventh':
            add_l=[4,3,4]
        if self.chord_name=='dominant_seventh':
            add_l=[4,3,3]
        if self.chord_name=='minor_seventh':
            add_l=[3,4,3]
        if self.chord_name=='dim_minor_seventh':
            add_l=[3,3,4]
        if self.chord_name=='diminished_seventh':
            add_l=[3,3,3]
        # 形成一个和弦的数字列表
        chord_num_l=[note_num]
        for v1 in add_l:
            note_num+=v1
            chord_num_l.append(note_num)
        return chord_num_l
    def chord_to_base_note_num(self):
        # 根据和弦种类求出还需要哪几个基本音级
        v1=self.base_note.index(self.root_note)
        chord_base_l=[self.root_note]
        if self.chord_name in triad_chord:
            for i in range(2):
                v1+=2
                chord_base_l.append(self.base_note[v1])
        if self.chord_name in seventh_chord:
            for i in range(3):
                v1+=2
                chord_base_l.append(self.base_note[v1])
        # 根据基本音级的列表转换成数字
        chord_base_note_l=[]
        for v2 in chord_base_l:
            chord_base_note_l.append(self.convert_note_num(v2,''))
        return chord_base_note_l
    def compare_list(self):
        l1=self.create_chord_num()
        l2=self.chord_to_base_note_num()
        # 对两个列表进行比较，如果差值超过2，那么就是不能生成的情况。
        error_l=[]
        for v1,v2 in zip(l1,l2):
            if abs(v1-v2)>2:
                error_l.append('fail')
            else:
                error_l.append('normal')
        return error_l
    def result_zh(self):
        # 和弦名称本地化
        triad_chord_name=['大三和弦','小三和弦','减三和弦','增三和弦']
        seventh_chord_name=['大大七和弦','大小七和弦','小小七和弦','减小七和弦','减减七和弦']
        if self.chord_name in triad_chord:
            chord_name=triad_chord_name[triad_chord.index(self.chord_name)]
        else:
            chord_name=seventh_chord_name[seventh_chord.index(self.chord_name)]
        # 音名本地化
        sharpe_flat_name_l=['','#','x','bb','b']
        sharpe_flat_name=sharpe_flat_name_l[sharpe_flat_kind.index(self.sharpe_flat)]
        note=self.root_note.upper()
        
        note_name=sharpe_flat_name+note
        return chord_name,note_name

def __main__():
    for v1 in triad_chord+seventh_chord:
        for v2 in base_note:
            for v3 in sharpe_flat_kind:
                t=Chords_that_cannot_be_formed(v1,v2,v3)
                if 'fail' in t.compare_list():
                    chord_name,note_name=t.result_zh()
                    print('当根音为'+note_name+'时，'+chord_name+'不能构成')

__main__()


