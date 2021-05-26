# scala hello world -- 20210526
在ubuntu20.04 server上试了下scala的hello world.
## 环境准备
在aws ec2里基于ubuntu20.04 server建一个ec2 instance，内存2G以上不然sbt可能跑不起来。

如果是amazon linux那可能就没有scala/sbt包，要自己上官网下载tar.gz解压即可。
## 安装scala
```
sudo apt-get update
sudo apt-get install scala
```
会把所需要的java runtime也装好而不是jdk。进入scala console: scala
```
Welcome to Scala 2.11.12 (OpenJDK 64-Bit Server VM, Java 11.0.11)
scala> 
```
敲入指令：`println("hw")`回车，得到输出：hw。这就是我们的hellow world程序。

注意这里如果是自己安装的低于java9的版本，回显可能有问题。据说是因为scala是在jdk1.9下编译的，在java1.8下用，就会出问题。这里再一次对java的“一次编写到处运行”和向前兼容失望。也对scala初印象打折。

以上是所谓解释执行方式。要编译的话需要定义个object并定义main函数（见文末）。然后scalac hw.scala得到HW.class，再scala HW即可运行。注意虽然HW.class是标准的java class文件但是用java -cp . HW跑不起来，需要把scala.jar加入到classpath，因为object HW extends scala.AnyRef，可以用javap HW或scalap HW反编译查看。

### 在geany中运行
如果是在自己个人的ubuntu桌面平台也可以用geany来作为它的代码编辑器，我用它来即写代码也写日记。把以上的println("hw");存成hw.scala后，build菜单里添加Compile对应命令scala "%f"即可按F8运行。
感觉运行速度比较慢。

### 安装sbt
sbt(scala build tool)把scala封装了一层便于scala项目的管理。ubuntu里安装需要额外添加它的apt源，也可以自己下载tar.gz解压即可。这里略。

安装完成输入sbt即进入交互式console. 总内存小于2G可能跑不起来。

第一次启动可以看到它从maven repo下载依赖包。整个使用感觉像交互式的maven.

这里先退出sbt(用命令exit)，然后建立第一个项目（建个文件夹里面放一个源文件即可）。
```
mkdir hw
cd hw
vim hw.scala
(edit hw.scala and exit vim)
sbt
run
```
得到输出hw，完成。

注意要编译的源文件不能只是一行println，需要定义个object和一个main入口在里面。源文件内容如下：
```
object HW{
  def main(args: Array[String]) = println("hw")
}
```
