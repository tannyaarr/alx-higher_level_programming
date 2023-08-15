#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
    listint_t *new_node, *tmp = *head;
    listint_t *tmp2, *rev_head = malloc(sizeof(listint_t));

    if (!rev_head)
        return (-1);
 
    rev_head->n = tmp->n;
    rev_head->next = NULL;
    tmp = tmp->next;

    while (tmp != NULL)
    {
        new_node = malloc(sizeof(listint_t));
        new_node->n = tmp->n;
        new_node->next = rev_head;
        rev_head = new_node;
        tmp = tmp->next;
    }

    tmp = *head;
    tmp2 = rev_head;

    while(tmp != NULL)
    {
        if (tmp->n != tmp2->n)
            return (0);
        tmp = tmp->next;
        tmp2 = tmp2->next;
    }
    return (1);
}
