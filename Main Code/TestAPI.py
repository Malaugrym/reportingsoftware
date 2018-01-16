from kayako import KayakoAPI
from kayako import Department


apiurl = 'https://summithosting.kayako.com/api/v1'

apikey = '6f435992-ff82-408e-8ea2-b908c6bf6d0b'

secretkey = 'MjdmNzA0YzQtNGNiMi00M2UyLWJhMmYtYTc1YWI1OWQwN2I3NDc5OWYwMTItOGU3ZC00Y2YzLWJjNzItNzQ3ZjBlMjU0MmQz'

api = KayakoAPI(apiurl,apikey,secretkey)

department = api.create(Department)
department.title = 'Test'
department.type = 'public'
