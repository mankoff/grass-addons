#ifndef LOCAL_PROTO_H
#define LOCAL_PROTO_H

#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
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
    int neighbors;
} Coords;

typedef struct
{
    int x, y;
    DCELL f, g;
} Path_Coords;

typedef DCELL(*f_statmethod) (DCELL *, int);
typedef int (*f_func) (DCELL *, int, int *, int, f_statmethod);

void writeFrag(int row, int col, int nbr_cnt);

DCELL average(DCELL * vals, int count);
DCELL variance(DCELL * vals, int count);
DCELL std_deviat(DCELL * vals, int count);
DCELL value(DCELL * vals, int count);
DCELL sum(DCELL * vals, int count);

/* heap.c */
void heap_alloc(int size);
void heap_free();
Path_Coords heap_delete(int pos);
void heap_insert(int x, int y, DCELL f, DCELL g);
void upheap(int pos);

int get_dist_matrix(int count);

int get_nearest_indices(int count, int *num_array, int num_count);

int f_dist(DCELL *, int, int *, int, f_statmethod);
int f_area(DCELL *, int, int *, int, f_statmethod);
int f_perim(DCELL *, int, int *, int, f_statmethod);
int f_shapeindex(DCELL *, int, int *, int, f_statmethod);
int f_path_dist(DCELL *, int, int *, int, f_statmethod);

int parseToken(int *res, int pos, char *token);

/* matrix.c */
int writeDistMatrixAndID(char *name, Coords ** frags, int count);
int writeAdjacencyMatrix(char *name, Coords ** frags, int count, int *nns,
			 int nn_count);

/* global variables */
GLOBAL int nrows, ncols;
GLOBAL Coords **fragments;
GLOBAL int *flagbuf;
GLOBAL Coords *actpos;
GLOBAL int verbose;
GLOBAL DCELL *distmatrix;
GLOBAL int *nearest_indices;
GLOBAL int patch_n;

GLOBAL Path_Coords *heap;
GLOBAL int heapsize;
GLOBAL DCELL *costmap;

#endif /* LOCAL_PROTO_H */
