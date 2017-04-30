# -*- mode: python -*-

block_cipher = None


a = Analysis(['TCPServer.py'],
             pathex=['C:\\Users\\陈先生\\Desktop\\1\\python\\TCP简单应用'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='TCPServer',
          debug=False,
          strip=False,
          upx=True,
          console=True )
