# coding=utf-8
import unittest,ddt,time,warnings,os,sys
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from case.Scene.scene import CJ
from case.Bussiness.bussiness import ye_wu
from case.NetworkTenants.networktenants import zu_hu
from case.EndUser.enduser import z_d
from case.SliceTemplate.slicetemplate import qie_pian
from case.MEC.mec import M_ec
from case.NetworkLevel.networklevel import z_w
from case.SystemManger.systemmanger import system
from case.SystemManger.logout import quit
from case.SituationAwareness.situationawareness import taishi
from BeautifulReport import BeautifulReport
from util.Excelread import ExcelUtil
from util.log.mylog import Log
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from config import globalparam
#取消警告提醒
warnings.filterwarnings("ignore")
report_path=globalparam.report_path
epath=globalparam.data_path

#场景用例--5 

@ddt.ddt
class Testcase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Log().info('******************** 场景测试开始 ********************')
        # Conn().__init__()

    @classmethod
    def tearDownClass(cls):
        # Conn().drop("user")
        Log().info('********************  场景测试结束  ********************')

    excel = ExcelUtil()
    @ddt.data(*excel.next(epath, '场景'))
    @ddt.unpack
    def testcase01(self,name,beizhu):
        '''创建场景'''
        result = CJ().add(name,beizhu)
        self.assertIn(result,"添加场景成功","测试失败")
        Log().info(result)

    def testcase02(self):
        '''对场景进行编辑'''
        result=CJ().alter("自动化")
        self.assertIn(result,"编辑场景成功","测试失败")

    def testcase03(self):
        '''根据场景名称进行查询'''
        result=CJ().select_cj('test')
        self.assertIn(result, "编辑", "测试失败")

    def testcase04(self):
        '''根据行业进行查询'''
        result = CJ().select_hy()
        self.assertIn(result, "编辑", "测试失败")

    def testcase05(self):
        '''对场景进行删除'''
        result=CJ().delete()
        self.assertEqual(result,"删除成功","测试失败")


#业务用例----4
# @ddt.ddt
# class Testcase02(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):

#         Log().info('******************** 业务测试开始 ********************')

#     @classmethod
#     def tearDownClass(cls):
#         Log().info('********************  业务测试结束  ********************')

#     excel = ExcelUtil()
#     @ddt.data(*excel.next(epath, '业务'))
#     @ddt.unpack
#     def testcase1(self,name,beizhu):
#         '''创建业务'''
#         r = ye_wu().add(name,beizhu)
#         self.assertEqual( "业务保存成功",r,"测试失败")
#         Log().info(r)

#     def testcase2(self):
#         '''对业务进行编辑'''
#         r=ye_wu().alter("自动化")
#         self.assertEqual(r,"业务编辑成功","测试失败")

#     def testcase3(self):
#         '''查询业务'''
#         r=ye_wu().select()
#         self.assertIn(r,'1',"测试失败")

#     def testcase4(self):
#         '''对业务进行删除'''
#         r=ye_wu().delete()
#         self.assertEqual(r,"删除成功","测试失败")


# #租户用例---8
# @ddt.ddt
# class Testcase03(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         Log().info('******************** 专网租户测试开始 ********************')

#     @classmethod
#     def tearDownClass(cls):
#         Log().info('******************** 专网租户测试结束********************')

#     excel = ExcelUtil()
#     @ddt.data(*excel.next(epath, '专网租户'))
#     @ddt.unpack
#     def testcase001(self,name,xm,phone,beizhu):
#         '''新建专网租户成功'''
#         r=zu_hu().add(name,xm,phone,beizhu)
#         self.assertEqual(r,"专网租户添加成功","测试失败")
#         Log().info(r)

#     def testcaose002(self):
#         '''对专网租户信息进行编辑'''
#         r=zu_hu().alter("修改名称", "李", "13150600101","11")
#         self.assertIn(r,"专网租户编辑成功","测试失败")

#     def testcase003(self):
#         '''专网详情页页面跳转'''
#         r=zu_hu().swith()
#         self.assertIn(r, "专网配置", "测试失败")

#     def testcase004(self):
#         '''租户专网配置[引用专网等级模版]'''
#         r=zu_hu().peizhi_1()
#         self.assertIn(r, "配置成功", "测试失败")
#         Log().info("租户专网引用专网等级模版配置成功")

#     def testcase005(self):
#         '''租户专网配置[引用模版]'''
#         r = zu_hu().peizhi_2()
#         self.assertIn(r, "配置成功", "测试失败")
#         Log().info("租户专网引用模版配置成功")

#     def testcase006(self):
#         '''专网租户登录'''
#         r=zu_hu().zuhu_login("测试租户001","18966453111")
#         self.assertEqual(r,"态势感知","测试失败")

#     def testcase007(self):
#         '''删除租户'''
#         r=zu_hu().delete()
#         self.assertIn(r,"删除成功",'测试失败')

#     def testcase008(self):
#         '''修改配置单状态'''
#         r=zu_hu().state()
#         self.assertEqual(r,'配置成功','测试失败')

# #终端用户用例---7
# @ddt.ddt
# class Testcase04(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         Log().info("********************终端用户测试开始********************")

#     @classmethod
#     def tearDownClass(cls):
#         Log().info("********************终端用户测试结束********************")

#     #采用ddt进行数据的多个添加
#     excel = ExcelUtil()
#     @ddt.data(*excel.next(epath, '终端用户'))
#     @ddt.unpack
#     def testcase01(self,phone,im,beizhu):
#         '''新建单个终端用户'''
#         r=z_d().add(phone,im,beizhu)
#         self.assertIn(r,"添加用户成功","测试失败")
#         Log().info("添加用户成功")

#     def testcase02(self):
#         '''对终端用户信息进行编辑'''
#         r=z_d().alter()
#         self.assertIn(r,"编辑用户成功","测试失败")

#     def testcase03(self):
#         '''查找终端用户存在'''
#         r=z_d().select('13512311316')
#         self.assertIn(r,"1","测试失败")

#     def testcase04(self):
#         '''终端用户模版下载'''
#         r=z_d().pladd()
#         self.assertEqual(r, "下载模板", "测试失败")

#     def testcase05(self):
#         '''批量创建终端用户'''
#         r=z_d().pldaoru(globalparam.impo_path)
#         self.assertIn("导入成功！",r,"测试失败")
#         Log().info(r)

#     def testcase06(self):
#         '''删除终端用户'''
#         r=z_d().delete()
#         self.assertIn(r,'删除成功','测试失败')

#     def testcase07(self):
#         '''批量删除终端用户'''
#         r=z_d().betch_delete()
#         self.assertEqual(r,'批量删除成功',"测试失败")

# #切片模版用例---5
# @ddt.ddt
# class Testcase05(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         Log().info("********************切片模版测试开始********************")

#     @classmethod
#     def tearDownClass(cls):
#         Log().info("********************切片模版测试结束********************")

#     excel = ExcelUtil()
#     @ddt.data(*excel.next(epath,'切片模版'))
#     @ddt.unpack

#     def testcase01(self,name,ip,port):
#         '''创建切片模版'''
#         r=qie_pian().add(name,ip,port)
#         self.assertEqual(r,"模板保存成功","测试失败")

#     def testcase02(self):
#         '''对切片模板信息进行编辑'''
#         r=qie_pian().alter()
#         self.assertIn(r,"模板保存成功","测试失败")

#     def testcase03(self):
#         '''切片模版根据模版名称进行查询'''
#         r=qie_pian().select1("医疗切片")
#         self.assertIn(r, "编辑", "测试失败")

#     def testcase04(self):
#         '''根据场景/业务条件进行查询'''
#         r=qie_pian().select2()
#         self.assertIn(r, "编辑", "测试失败")

#     def testcase05(self):
#         '''删除切片'''
#         r=qie_pian().delete()
#         self.assertIn(r,'删除成功','测试失败')

# #MEC--4   一个租户只能绑定一个mec
# @ddt.ddt
# class Testcase06(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         Log().info("********************MEC测试开始********************")

#     @classmethod
#     def tearDownClass(cls):
#         Log().info("********************MEC测试结束********************")

#     def testcase01(self,url):
#         '''添加mec'''
#         self.add=M_ec().add(url)
#         self.assertIn(self.add, "添加MEC成功", "测试失败")
#         r=M_ec().add("10.1.3.2")
#         self.assertIn(r, "添加MEC成功", "测试失败")
#         Log().info(r)

#     def testcase02(self):
#         '''对mec信息进行编辑'''
#         r=M_ec().alter()
#         self.assertIn(r,"编辑MEC成功","测试失败")

#     def testcase03(self):
#         '''对mec进行查询'''
#         r= M_ec().select()
#         self.assertIn(r,"编辑",'测试失败')

#     def testcase04(self):
#         '''对mec进行删除'''
#         r = M_ec().delete()
#         self.assertIn(r, "删除成功", "测试失败")


# # #专网等级---5
# @ddt.ddt
# class Testcase07(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         Log().info("********************专网等级测试开始********************")

#     @classmethod
#     def tearDownClass(cls):
#         Log().info("********************专网等级测试结束********************")

#     excel = ExcelUtil()
#     @ddt.data(*excel.next(epath, '专网等级'))
#     @ddt.unpack
#     def testcase01(self,name,ip,port):
#         '''手动输入创建专网等级模板'''
#         r=z_w().add01(name,ip,port)
#         self.assertIn(r,"配置成功", "测试失败")
#         Log().info('手动输入创建专网等级模板配置成功')

#     def testcase02(self):
#         '''引用模版创建专网等级模板'''
#         r = z_w().add02("引用模版01")
#         self.assertIn(r,"配置成功", "测试失败")

#     def testcase03(self):
#         '''对专网等级模版进行查询[通过模版名]'''
#         r=z_w().select_1("回归")
#         self.assertEqual(r,"详情","测试失败")

#     def testcase04(self):
#         '''对专网等级模版进行查询[通过行业与等级]'''
#         r=z_w().select_2()
#         self.assertIn(r, "暂无数据", "测试失败")

#     def testcase05(self):
#         '''对专网等级模版进行删除'''
#         r=z_w().delete()
#         self.assertIn(r, "删除成功", "测试失败")

# # #系统用户管理用例----8
# @ddt.ddt
# class Testcase08(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         Log().info("********************系统用户管理测试开始********************")

#     @classmethod
#     def tearDownClass(cls):
#         Log().info("********************系统用户管理测试结束********************")

#     excel = ExcelUtil()
#     @ddt.data(*excel.next(epath, '系统用户'))
#     @ddt.unpack
#     def testcase01(self,name,beizhu):
#         '''新建系统用户成功[运维](冒烟)'''
#         r=system().add(name,beizhu)
#         self.assertIn(r,"添加用户成功", "测试失败")
#         Log().info(r)

#     def testcase02(self):
#         '''对用户列表数据进行编辑[修改用户名,角色和备注]'''
#         r=system().alter("usermame", "1")
#         self.assertIn(r,"编辑用户成功", "测试失败")

#     def testcase03(self):
#         '''验证用户创建后登陆成功[运维人员]'''
#         r = system().login_yw("ubgoill3fbb")
#         self.assertIn(r, "运维管理", "测试失败")

#     def testcase04(self):
#         '''验证用户创建后登陆成功[运营人员]'''
#         r = system().login_yy("ub79HUIHI7b")
#         self.assertEqual(r, "运营概览", "测试失败")

#     def testcase05(self):
#         '''对用户列表数据进行查询[通过角色名]'''
#         r =system().select_juese("运营人员")
#         self.assertIn(r, "编辑", "测试失败")

#     def testcase06(self):
#         '''对用户列表数据进行查询[通过用户名称]'''
#         r = system().select_name("username")
#         self.assertIn(r, "编辑", "测试失败")

#     def testcase07(self):
#         '''删除用户'''
#         r=system().delete()
#         self.assertIn(r,'删除成功',"测试失败")

#     def testcase08(self):
#         '''运维运营登录退出'''
#         r=quit().Logout_('username')
#         self.assertEqual(r,'登录Login','测试失败')


#综合态势感知用例----3条
class Testcase09(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Log().info("********************综合态势感知测试开始********************")

    @classmethod
    def tearDownClass(cls):
        Log().info("********************综合态势感知测试结束********************")

    def testcase01(self):
        '''专网等级分布'''
        r=taishi().zwdj()
        self.assertIn(r,"专网等级分布", "测试失败")

    def testcase02(self):
        '''专网行业分布'''
        r=taishi().zwhy()
        self.assertIn(r, "专网行业分布", "测试失败")

    def testcase03(self):
        '''专网运行状况'''
        r = taishi().zwzt()
        self.assertIn(r, "专网运行状况", "测试失败")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    report_title = '专网管理测试报告' + now + ".html"
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    Name = ['场景测试', '业务测试', '专网租户测试', '终端用户测试', '切片模块测试', 'MEC模块测试', '专网等级模块测试', '系统用户管理测试', '综合态势感知测试']

    testcases = unittest.TestLoader().loadTestsFromTestCase(Testcase01)
    suite.addTest(testcases)
    BeautifulReport(testcases).report(filename=report_title,   description=Name[0],report_dir=report_path,theme="theme_cyan")

