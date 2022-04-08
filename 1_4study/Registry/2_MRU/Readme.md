forensics-accessing-the-windows-registry-with-python-f32e138691b0
- Shell Item parser(libfwsi project): https://github.com/libyal/libfwsi

### Windows Installer for Python libregf, libfwsi library
- l2timeline: https://github.com/log2timeline/l2tbinaries

### Registry Hive sample files
- dfwinreg: https://github.com/log2timeline/dfwinreg/tree/main/test_data

### Related Documents
- pyfwsi: https://github.com/libyal/libfwsi/wiki/Python-development
- Shell Item List format: https://github.com/libyal/libfwsi/blob/main/documentation/Windows%20Shell%20Item%20format.asciidoc

## Step by Step
### OpenSavePidlMRU
아래는 python 3.10 (64bit) 버전을 기준으로 진행되었음
1. python 3.10 64bit version 설치 (경로 설정하지 않음)
2. l2tbinaries의 libfwsi-python-20210419.1.win-amd64-py3.10.msi 파일 설치
   - 설치시 필히 python 3.10 선택
3. dfwinreg에서 NTUSER.DAT test data download
4. OpenSavePidlMRU_step?.py 실행 실습
