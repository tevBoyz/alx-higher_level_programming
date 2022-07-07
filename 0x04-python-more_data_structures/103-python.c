#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_bytes - prints info abt python lists
 * @p: address of pyobject
 */

void print_python_bytes(PyObject *p)
{
size_t i, len, size;
char *str;

printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes"))
{
printf(" [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
str = ((PyBytesObject *)p)->ob_sval;
len = size + 1 > 10 ? 10 : size + 1;
printf(" size: %lu\n", size);
printf(" trying string: %s\n", str);
printf(" first %lu bytes: ", len);
for (i = 0; i < len; i++)
printf("%02hhx%s", str[i], i + 1 < len ? " " : "");

printf("\n");
}

/**
 * print_python_list - prints info abt python lists
 * @p: address of Pyobject
 */

void print_python_list(PyObject *p)
{
int i;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
{
printf("Element %d: %s\n", i,
		((PyList *)p)->ob_item[i]->ob_type->tp_name);
if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
print_python_bytes(((PyListObject *)p)->ob_item[i]);
}
}
