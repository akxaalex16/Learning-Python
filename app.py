# import entire module
# we have to prefix it with the name of package
import package.shipping

package.shipping.calc_shipping()

# use this instead to get specific method
from package.shipping import calc_shipping

calc_shipping()
calc_shipping()
calc_shipping()

# now we can use this method without typing the package/folder/dirctory name and the file/module name

# or do this to get all methods from shipping.py
from package import shipping

shipping.calc_shipping()