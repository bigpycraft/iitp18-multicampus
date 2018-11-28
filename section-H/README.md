
# ML/DL Based Core Industry Big Data Analysis Expert Course

<div align='right'><font size=2 color='gray'>Python For BigData @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## IITP 2018, Innovation Growth Intensive Training in MultiCampus
>  
- [Section-A][link-A] : Python Programming Basics 
- [Section-B][link-B] : Python Modules for Data Analysis
- ♣ [Midterm Test][test10] : Python Core Programming <br/><br/>
- [Section-C][link-C] : Data Analysis Practice for BigData
- [Section-D][link-D] : Web Crawling and Scraping
- ♣ [Team Project][test11] : Keyword Data Analysis by Topic <br/><br/>
- <b>[Section-E][link-E] : Machine Learning</b>
- [Section-F][link-F] : Deep Learning
- ♣ [Team Project][test12] : Challenge Kaggle for Machine Learning <br/><br/>

[link-A]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/section-A "Go Section-A"
[link-B]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/section-B "Go Section-B"
[link-C]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/section-C "Go Section-C"
[link-D]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/section-D "Go Section-D"
[link-E]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/section-E "Go Section-E"
[link-F]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/section-F "Go Section-F"
[test10]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/test-py10 "Go Test-10"
[test11]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/test-py11 "Go Test-11"
[test12]: https://github.com/bigpycraft/iitp18-multicampus/tree/master/test-py12 "Go Test-12"


<img src="../images/img_front_readme_iitp.png">

## Virtual Machine for BigData Environment
- <a href="https://htmlpreview.github.io/?https://github.com/bigpycraft/iitp18-multicampus/blob/master/section-H/html/BDA-VM101-Tutorials.html                 "> 1. Tutorial for Virtual Machine    </a>
<br/><br/>


<hr>

## 팀별 빅데이터 분산처리장치

<table border=1 bgcolor="#EEEEEE">
	<tr bgcolor="#CC0000">
		<td width="100"><div align="center"><font color="#FFFFFF"><b>팀별장비 </b></font></div></td>
		<td width="150"><div align="center"><font color="#FFFFFF"><b>IP       </b></font></div></td>
		<td width="200"><div align="center"><font color="#FFFFFF"><b>로그인ID </b></font></div></td>
		<td width="200"><div align="center"><font color="#FFFFFF"><b>로그인PW </b></font></div></td>
		<td width="150"><div align="center"><font color="#FFFFFF"><b>ROOT PW  </b></font></div></td>
	</tr>
	<tr>
		<td><div align="center">A팀             </div></td>
		<td><div align="center">70.12.115.60    </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
		<td rowspan="5"><div align="center">global</div></td>
	</tr>
	<tr>
		<td><div align="center">B팀             </div></td>
		<td><div align="center">70.12.115.72    </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
	</tr>
	<tr>
		<td><div align="center">C팀             </div></td>
		<td><div align="center">70.12.115.75    </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
	</tr>
	<tr>
		<td><div align="center">D팀             </div></td>
		<td><div align="center">70.12.115.77    </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
	</tr>
	<tr>
		<td><div align="center">E팀             </div></td>
		<td><div align="center">70.12.115.80    </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
		<td><div align="center">user01 ~ user05 </div></td>
	</tr>
</table>


<hr>

###  ▶ VM Basic Information
- <b> 장비이름, Name  </b> : VM-C-LAB01~05
- <b> 운영체제, OS    </b> : Ubuntu 16.04 LTS(64bit)
- <b> 하드웨어, HW    </b> : rCore.S3(Memory 24GB, 8rCore CPU, SSD 25GB[disk], 10GB Traffic/day)
- <b> 스토리지, Block Storage </b> : SATA Block X4 Hard Raid 1TB
<br/><br/>


<hr>

###  ▶ VM User Guide
- <b> 사용기간 </b> : 교육기간에만 사용가능한 임시서버 (~2018.12.01)
- <b> 팀별할당 </b> : 5명 사용제한
- <b> 서버접속 </b> : 원격 콘솔프로그램 PuTTY 통해 VM-LAB에 접속
<br> - PuTTY Download : https://www.putty.org/
<br> - 프로그램 설치 후, VM-LAB의 IP주소 등록
<br> - Category>Connection>SSH>Tunnels
<br> &nbsp;&nbsp;&nbsp;&nbsp; √ Soruce port : 8888
<br> &nbsp;&nbsp;&nbsp;&nbsp; √ Destination : 127.0.0.1:8888
<br> &nbsp;&nbsp;&nbsp;&nbsp; √ Local, Auto Selected
<br> &nbsp;&nbsp;&nbsp;&nbsp; [Add] 클릭
<br> &nbsp;&nbsp;&nbsp;&nbsp; 
<br> &nbsp;&nbsp; cf. Tip> 포트중복막기위해 8888~8892까지, forwarded port 미리 설정
<br> &nbsp;&nbsp;  
<br> &nbsp;&nbsp;  [Open] 클릭
<br/><br/>


<hr>

###  ▶ Anaconda Settings for Deep Learning
- sudo user 를 통해 미리 설정해 놓은 환경변수 경로(/home/ubuntu/.bashrc)를 통해 접근
- 환경변수 경로 설정
<br/> ＄ source /home/ubuntu/.bashrc
- Anaconda 실습용 작업 환경 실행
<br/> ＄ conda activate IITP_BPC
<br/> (IITP_BPC) ＄ pwd
- Jupyter-Notebook 실행
<br/> (IITP_BPC) ＄ jupyter-notebook --ip=0.0.0.0 --no-browser
<br/> (IITP_BPC) ＄ ...
<br/> (IITP_BPC) ＄ ...
<br/> (IITP_BPC) ＄ ...
<br/> (IITP_BPC) ＄ http://(LAB or 127.0.0.1):8889/?token=token_value



<hr>

### TensorFlow

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.tensorflow.org/">
            <img src="../images/TensorFlow_logo2.png" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
    <b> - TensorFlow.org </b> : https://www.tensorflow.org/
    <br/><br/> - An open source machine learning library for research and production.
    <br/><br/>
    <b> 1. TenforFlow Install  : <a href='https://www.tensorflow.org/install/'>[설치가이드]</a>
    <br/><br/>
    <b> 2. TenforFlow Develop : <a href='https://www.tensorflow.org/tutorials/'>[튜토리얼]</a>
    <br/><br/>
    <b> 3. TensorFlow Community </b> : <a href='https://www.tensorflow.org/community/'>[커뮤니티]</a>
    <br/><br/>
    <b> cf. Environment : Install a Python 3.5.x or Python 3.6.x 64-bit release for Windows </b>
</div>
        </td>
    </tr>
</table>
<br/>


<hr>

<h3> Jupyter Notebook </h3>

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://www.seleniumhq.org/projects/webdriver/">
            <img src="../images/jupyter.jpg" width="150" />
            </a>
        </td>
        <td width="800">
<div align="left">
<b> Latest : Version 5.3 | Release Date: September 28, 2018 </b>
<br/>
- Filename : Anaconda3-5.3.0-Windows-x86_64.exe 
<br/>
- Download : https://www.anaconda.com/download/
<br/>
- Check the OS version & bit (32bit / 64bit)
</div>
<br/>
<div align="left">
<b> Recommand : Version 5.2 | Release Date: May 30, 2018 </b>
<br/>
- Filename : Anaconda3-5.2.0-Windows-x86_64.exe
<br/>
- Download : https://repo.continuum.io/archive/ 
<br/>
- Reason : TF Requires Python 3.4, 3.5, or 3.6 
<br/>
- TensorFlow : https://www.tensorflow.org/install/pip
</div></td>
    </tr>
</table>
<br/>


<hr>

### Microsoft Azuer Notebooks

<table align="left">
    <tr align="left">
        <td width="200">
            <a href="https://notebooks.azure.com/">
            <img src="../images/microsoft.jpg" width="100" />
            </a>
        </td>
        <td width="800">
<div align="left">
- <b> Microsoft Azure Notebooks </b> : https://notebooks.azure.com/
<br/><br/>
- Interactive coding in my browser
<br/><br/>
- Free, in the cloud, powered by jupyter
</div></td>
    </tr>
</table>
<br/>


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
