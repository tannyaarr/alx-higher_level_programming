#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
	 listint_t *temp = list;
	 if (temp == NULL)
		 return 0;
	 while (temp)
	 {
		 if (temp->next == NULL)
			 return 0;
		 if (temp->next == list)
			 return 1;
		 temp = temp->next;
	 }
	 return 0;
}
