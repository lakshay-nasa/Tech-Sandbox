# import apertium
# import apertium.installer

# apertium.installer.install_apertium()

# apertium.installer.install_module('ita')
# apertium.installer.install_module('en')

# print(apertium.translate("eng","ita","authentication"))

# translation = apertium.translate('en', 'spa', 'cats')
# print(" This is translation --> " + translation)


# import apertium
# g = apertium.Generator('spa')
# print(g.generate('^cat<n><pl>$'))
# print(apertium.append_pair_path('..'))

# print("hello")

import apertium
apertium.installer.install_apertium()

apertium.installer.install_module('eng')
apertium.installer.install_module('spa')
t = apertium.Translator('eng', 'spa')
print(t.translate('cats'))


# ***   Not Working   ***