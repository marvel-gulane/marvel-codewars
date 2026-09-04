import random

class Three(object):	
	def __init__(self, ball01, ball02, ball03): self.ball01, self.ball02, self.ball03 = ball01, ball02, ball03;
	def __str__(self): return "(PCSO)3rtres	:%s %s %s" % (self.ball01, self.ball02, self.ball03);

class Six(object):
	def __init__(self, ball01, ball02, ball03, ball04, ball05, ball06): self.ball01, self.ball02, self.ball03, self.ball04, self.ball05, self.ball06 = ball01, ball02, ball03, ball04, ball05, ball06;
	def __str__(self): return "(PCSO)6/45	:%s %s %s %s %s %s" % (self.ball01, self.ball02, self.ball03, self.ball04, self.ball05, self.ball06);

ball01	= random.randrange(10);
ball02	= random.randrange(19); 
ball03	= random.randrange(10); 
ball04	= random.randrange(10);
ball05	= random.randrange(10);
ball06	= random.randrange(10);

banner = "∫10 ∫101 π2 dxdy = 1 − xy 6"
roll3 	= Three(ball01, ball02, ball03);
roll6	= Six(ball01, ball02, ball03, ball04, ball05, ball06);
print("%s\n\n%s\n%s"%(banner, roll3, roll6))
