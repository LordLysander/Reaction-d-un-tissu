k=	0			#Coefficient de raideur du ressort
l0=	0			#Longueur a vide
m=	0			#Masse d'une maille
dt=	0.01



class Vec3f:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0


	def dot_product(self, vec):
		return self.x*vec.x + self.y*vec.y + self.z*vec.z


	def cross_product(self, vec):
		ret = Vec3f()
		ret.x = self.y*vec.z-vec.y*self.z
		ret.y = self.z*vec.x-vec.z*self.x
		ret.z = self.x*vec.y-vec.x*self.y
		return ret


	def add(self, vec):
		ret = Vec3f()
		ret.x, ret.y, ret.z = self.x + vec.x, self.y + vec.y, self.z + vec.z
		return ret


 	def mult(self , scal):
		self.x *= scal   # a*=l <=> a = a * l   marche aussi avec | & && || << >> < > ! % + -  / // **
		self.y *= scal
		self.z *= scal



class Node:
	def __init__(self, pos):
		self.pos = pos
		self.velocity = Vec3f();
		self.mass = m
		self.neigbhour = []
		#other vars
		#here are the definitions of local Node parameters aka (mass, velocity, position, and such ...)
	


def iterate(nd_lst): #nd_lst stand for Node[]
	#differential equation
	# ....... good luck
	for i in range(len(nd_lst)):
		for j in range(len(nd_lst[i].neigbhour)):
			nd_lst[i].velocity = nd_lst[i].velocity.add(nd_lst[i].position.mult(-1)).add(nd_list[nd_list[i].neigbhour[j]].position).add(l0*(nd_lst[i].position.mult(-1)).add(nd_list[nd_list[i].neigbhour[j]].position)/((nd_lst[i].position.mult(-1)).add(nd_list[nd_list[i].neigbhour[j]].position).lenght())).mult((dt/m)*k)
		
		nd_lst[i].position = nd_lst[i].position.add(nd_lst[i].velocity.mult(dt))

	return nd_lst



def surfacegrid(length,width,precision):
	nd_lst = []
	for i in range(0, lenght):
		for j in range(0,width):
			nd_lst.append(Node(Vec3f(i*precision, j*precision, 0)) )
	return nd_lst


#a executer pour beaucoup de pt de la liste
def impact(p,force):
	nd_list[p].velocity += dt*force/nd_list[p].mass
	vb += - dt*force/mb
	#modéliser l'impact de la balle sur le maillage et appliquer les modifications que subit le tissu




def finalmod(p,q,vb,mb,length,width,precision,k,l0,m,dt):
	grid=surfacegrid(length,width,precision)
	
	#à partir des conditions initiales, présenter le modèle et ça déformation (si possible intégrer images)
