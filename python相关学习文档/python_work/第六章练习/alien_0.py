# coding:utf-8
# һ���򵥵��ֵ䣬ע���ֵ�ĸ�ʽ��-ֵ�ԣ��ֵ�={�ֵ�����ֵ�ֵ���ֵ�����ֵ�ֵ}
# ��Ҫ�����ֵ��е�ֵ�ͱ����Ȼ�ȡ�������ã��ֵ�[��Ҫ���ʵ�ֵ����Ӧ�ļ�]
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
# pythonѧϰ�иУ���Ȼ��python�д�����������ָ�������������ͣ���ͬʱҲĬ���˱���������������������ֵ����������һ�£��������a=5����ô����a��������
new_points=alien_0['points']
print("points:"+str(new_points))
# ��Ӽ�-ֵ�Եķ������ֵ�['����']=������ֵ
# ע�⣺��-ֵ�Ե�����˳�������˳��ͬ��python�����ļ�-ֵ�Ե����˳��
alien_0['x_position']=0
alien_0['y_position']=25
# �޸��ֵ��е�ֵ���ֵ�['ԭ��']=��������ֵ��
alien_0['color']='blue'
print(alien_0)
# �����ȴ���һ�����ֵ�:�ֵ�={}������������Ӽ�-ֵ�ԣ��ֵ�['����']=������ֵ
singer={}
singer['name']='xr'
singer['sex']='man'
print(singer)


