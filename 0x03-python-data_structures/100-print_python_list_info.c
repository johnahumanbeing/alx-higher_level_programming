#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info on Python lists
 * @p: pointer to python list object
 *
 * Return: zero
 */
void print_python_list_info(PyObject * p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
