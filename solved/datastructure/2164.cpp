#include <iostream>

using namespace std;

class Node
{
public:
	int data;
	Node* next;
	Node* prev;

	Node(int _data)
	{
		this->next = NULL;
		this->prev = NULL;
		this->data = _data;
	}

};

class Queue
{
public:
	int size;
	Node* head;
	Node* tail;

	Queue()
	{
		this->size = 0;
		this->head = NULL;
		this->tail = NULL;
	}


	void enQueue(Node* _n)
	{
		if (this->head == NULL)
		{
			this->head = _n;
			this->tail = _n;
		}
		else 
		{
			this->tail->next = _n;
			_n->prev = this->tail;
			this->tail = _n;
		}
		this->size++;
	}

	int deQueue()
	{
		int output = this->head->data;

		Node* temp = this->head;
		this->head = this->head->next;
		this->head->prev = NULL;
		delete(temp);
		this->size--;

		return output;
	}

	void printHead()
	{
		cout << this->head->data << "\n";
	}


};

int main(void)
{
	int n;
	Queue* q = new Queue();
	cin >> n;
	for (int i = 1; i < n + 1; i++) q->enQueue(new Node(i));

	while (q->size != 1)
	{
		q->deQueue();
		q->enQueue(new Node(q->head->data));
		q->deQueue();
	}

	q->printHead();


}
