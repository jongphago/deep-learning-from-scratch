#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int AND(float x1, float x2);
int NAND(float x1, float x2);
int OR(float x1, float x2);
int XOR(float x1, float x2);

	
void main(void) {
	float x1, x2;
	printf("x1값과 x2값을 입력하시오: ");
	scanf("%f %f", &x1, &x2);
	int xorLabel = XOR(x1, x2);
	printf("%d", xorLabel);
}


int AND(float x1, float x2) {
	float w1 = 0.5, w2 = 0.5, theta = 0.7;
	float temp = w1 * x1 + w2 * x2;
	int label;
	if (temp <= theta) label = 0;
	else  label = 1;
	return label;
}

int NAND(float x1, float x2) {
	float w1 = -0.5, w2 = -0.5, theta = -0.7;
	float temp = w1 * x1 + w2 * x2;
	int label;
	if (temp <= theta) label = 0;
	else  label = 1;
	return label;
}

int OR(float x1, float x2) {
	float w1 = 0.5, w2 = 0.5, theta = 0.2;
	float temp = w1 * x1 + w2 * x2;
	int label;
	if (temp <= theta) label = 0;
	else  label = 1;
	return label;
}

int XOR(float x1, float x2) {
	return AND(NAND(x1, x2), OR(x1, x2));
}