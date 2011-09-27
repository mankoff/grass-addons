#ifndef LOCAL_PROTO_H
#define LOCAL_PROTO_H

#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <time.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include <grass/stats.h>

#ifdef MAIN
#define GLOBAL
#else
#define GLOBAL extern
#endif

#define MAX_DOUBLE 1000000.0

typedef struct
{
    int x, y;
} Position;

typedef int (*f_method) (Position *, int, int);

/* func.c */
int f_circular(Position * list, int count, int neighbors);
int f_random(Position * list, int count, int neighbors);
int f_costbased(Position * list, int count, int neighbors);

/* global variables */
GLOBAL int nrows, ncols;
GLOBAL int *flagbuf;
GLOBAL DCELL *costmap;

#endif /* LOCAL_PROTO_H */
