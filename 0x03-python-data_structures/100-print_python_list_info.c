#include <python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: pointer to the list
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	long int len = list->ob_size;
	long int i = 0;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %lu\n", list->allocated);

	while(i < len)
	{
		printf("Element %ld: %s\n", i, py_TYPE(list->ob_item[i])->tp_name);
		i++;
	}
}

