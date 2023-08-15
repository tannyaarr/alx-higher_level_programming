#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *mid = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast)
    {
        mid = slow;
        slow = slow->next;
    }

    listint_t *second_half = slow;
    prev_slow->next = NULL;

    listint_t *prev = NULL, *current = second_half, *next;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    second_half = prev;

    listint_t *first_half = *head;
    while (first_half && second_half)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    prev = NULL, current = prev_slow->next;
    prev_slow->next = NULL;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    prev_slow->next = prev;

    if (mid)
    {
        prev_slow->next = mid;
        mid->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return is_palindrome;
}
