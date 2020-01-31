class Polyline(object):
    """
    def __init__(self, pt_lst):
        self.start_pt = pt_lst[0]
        self.pt_lst = pt_lst
        self.vec_lst = getVectorListFromPts()
        self.cornerYinYangProperty_lst = getYinYangProperty()
    """
    def __init__(self, start_pt, vec_lst):
        self.start_pt = start_pt
        self.vec_lst = vec_lst
        self.pt_lst = self.getPointListFromVecs()
        self.length = self.getLength()
        self.cornerYinYangProperty_lst = self.getYinYangProperty()

    def getLength(self):
        # 返回polyline的每段向量长度和
        length = 0.0
        for vec in vec_lst:
            length += vec.length()
        return length

    def getPointListFromVecs(self):
        # 根据向量序得到点
        return

    def getVectorListFromPts(self):
        # 根据顺序点得到向量
        vec_lst = []
        for i in range(len(self.pt_lst)-1):
            vec = Vector(self.pt_lst[i], self.pt_lst[i+1])
            vec_lst.append(vec)
        vec = Vector(self.pt_lst[-1], self.pt_lst[0])
        vec_lst.append(vec)
        return vec_lst

    def getYinYangProperty(self):
        # 得到多边形的端点阴阳角性质
        cornerYinYangProperty_lst = []
        return cornerYinYangProperty_lst

    def addPolylines(self, polys):
        # polys: 与之合并的其他顺序多段线list
        new_polyline.start_pt = self.start_pt
        new_polyline.vec_lst = self.vec_lst
        #new_polyline.pt_lst = self.pt_lst
        #new_polyline.length = self.length
        #new_polyline.cornerYinYangProperty_lst = self.cornerYinYangProperty_lst
        i = 0
        for i in range(len(polys)):
            new_polyline.vec_lst.append(polys[i].vec_lst)
            #if i < len(polys):
            #   new_polyline.pt_lst.append(polys[i+1].pt_lst)
            #new_polyline.length.append(polys[i].length)
            #new_polyline.cornerYinYangProperty_lst.append(polys[i].cornerYinYangProperty_lst)
        new_polyline = Polyline(new_polyline.start_pt, new_polyline.vec_lst)
        return new_polyline

    def addPolylines(self, polys):
        # polys: 与之合并的其他顺序多段线list
        new_start_pt = self.start_pt[:]
        new_vec_lst = self.vec_lst[:]
        for i in range(len(polys)):
            new_vec_lst += polys[i].vec_lst
        new_polyline = Polyline(new_start_pt, new_vec_lst)
        return new_polyline        