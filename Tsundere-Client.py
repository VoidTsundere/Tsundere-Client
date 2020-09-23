import os
import wget
import shutil
import requests

def console(one):
	if one == 1:
		os.system('cls')
	print('Tsundere-Client 0.0.1\n\nUse /install para ver a lista de apps')
	cl= input('')
	if '1' in cl:
		dereRPG()
	if '/install' in cl:
		os.system('cls')
		print('Use 1 para instalar ou atualizar o DereRPG\n')
		confirm = input('')
		if confirm == '1':
			dereRPG()
		else:
			os.system('cls')
			console(0)

def getVersion():
	wget.download(versionUrl)
	if os.path.exists('DereRPG/Version.txt') == True:
		os.remove('DereRPG/Version.txt')
		shutil.move('Version.txt','DereRPG')

def dereRPG():
	global versionUrl
	versionUrl = 'https://raw.githubusercontent.com/PG-MASTER/Dere-RPG/master/Version.txt'
	Main_py = 'https://raw.githubusercontent.com/PG-MASTER/Dere-RPG/master/Main.py'
	Engine_py = 'https://raw.githubusercontent.com/PG-MASTER/Dere-RPG/master/Data/Engine.py'
	print('a')


	if os.path.exists('DereRPG/Version.txt'):
		print('a')
		with open('DereRPG/Version.txt') as VersionFile:
			LocalVer = VersionFile.readline()
			ServerVer = requests.get(versionUrl)
			VersionFile.close()
			os.system('cls')
			print('Você está com a versão',LocalVer,'a versão do servidor é atualmente',ServerVer.text)
			print('\n1 Para atualizar para a versão do servidor\n0 para cancelar\n')
			check = input()
			if check == '0':
				os.system('cls')
				console(0)
			if check == '1':
				print('Downloading')

				if os.path.exists('DereRPG/Main.py') == True:
					os.remove('DereRPG/Main.py')
				if os.path.exists('DereRPG/Data/Engine.py') == True:
					os.remove('DereRPG/Data/Engine.py')

				wget.download(Main_py)
				wget.download(Engine_py)
				getVersion()

				if os.path.exists('DereRPG') == True:
					shutil.move('Main.py','DereRPG')
					if os.path.exists('DereRPG/Data') == True:
						shutil.move('Engine.py','DereRPG/Data')
					else:
						os.mkdir('Data')
						shutil.move('Engine.py','Data')
						shutil.move('Data','DereRPG')

					if os.path.exists('DereRPG/Saves') == False:
						os.mkdir('Saves')
						shutil.move('Saves','DereRPG')

				else:
					os.mkdir('DereRPG')
					os.mkdir('Data')
					shutil.move('Engine.py','Data')
					shutil.move('Data','DereRPG')
					shutil.move('Main.py','DereRPG')
					shutil.move('Version.txt','DereRPG')
					os.mkdir('Version')
					shutil.move('Version','DereRPG')
	else:
		if os.path.exists('DereRPG/Data') == False:
			os.mkdir('Saves')
			os.mkdir('Data')
			wget.download(Main_py)
			wget.download(Engine_py)
			wget.download(versionUrl)
			shutil.move('Engine.py','Data')
			os.mkdir('DereRPG')
			shutil.move('Data', 'DereRPG')
			shutil.move('Saves','DereRPG')
			shutil.move('Main.py','DereRPG')
			shutil.move('Version.txt','DereRPG')
		else:
			wget.download(Main_py)
			wget.download(Engine_py)
			wget.download(versionUrl)
			if os.path.exists('DereRPG/Saves') == False:
				os.mkdir('Saves')
				shutil.move('Saves','DereRPG')
			shutil.move('Main.py','dereRPG')
			shutil.move('Engine.py','DereRPG/Data')
			shutil.move('Version.txt','DereRPG')

console(0)