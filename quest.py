# coding:utf8
"""任务系统"""

class Quest(object):
	"""任务基类"""
	WAIT 		= 0 # 等待任务请求
	ACCEPTED 	= 1	# 已接受，正在执行任务
	DONE 		= 2	# 已完成任务要求，但尚未交还
	COMPLETED 	= 3	# 已交还任务，彻底完成任务目标
	OUTOFDATE 	= 4	# 任务已过期
	def __init__(self, *args, **kwargs):
		#任务目标对象列表
		self.targets = kwargs.get('targets', [])
		# 任务内容的简要描述（一行）
		self.title = kwargs.get('title', "")
		# 任务内容的详细描述（多行）
		self.description ＝ kwargs.get('description', "")
		# 任务状态
		self.status = Quest.WAIT

	def execute(self, player, target):
		"""执行任务"""
		pass


class TalkQuest(Quest):
	"""对话类任务"""

	def __init__(self, talkto, msg, *args, **kwargs):
		super(TalkQuest, self).__init__(
			targets=[talkto],
			*kargs, **kwargs)
		self.msg = msg

	def execute(self, player, target):
		assert target in self.targets
		MsgBox(self.msg).show()
		self.status = Quest.DONE


class CollectQuest(Quest):
	"""收集类任务"""


class FightQuest(Quest):
	"""战斗类任务"""


class QuestMaster(Npc):
	"""提供任务的NPC"""
	quest_class = Quest

	def __init__(self, *args, **kwargs):
		super(QuestMaster, self).__init__(*args, **kwargs)
		self.quest = self.quest_class()

	def do_collide(self, player):
		if self.quest.status == Quest.WAIT:
			player.quests.append(self.quest)
		elif self.quest.status == Quest.ACCEPTED:
			MsgBox("Please complete your quest!").show()
		elif self.quest.status == Quest.DONE:
			self.commit()

	def commit(self):
		self.quest.status = Quest.COMPLETE


def TestQM(QuestMaster):
	def __init__(self, *args, **kwargs):
		self.quest = TalkQuest(talkto, "asfsdf")