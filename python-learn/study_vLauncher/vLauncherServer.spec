# -*- mode: python -*-

block_cipher = None


a = Analysis(['vLauncherServer.py'],
             pathex=['D:\\Yummy\\A_Python\\python-learn\\study_vLauncher'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='vLauncherServer',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='image\\vLauncher.ico')
