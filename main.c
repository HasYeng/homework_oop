#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>

typedef struct Frog {
  bool hungry;
} Frog;

void day_of_frog(Frog* frog) {
  sleep(3);
  printf("Frog: moving, eating, breathing\n");
  if (frog->hungry) {
    sleep(3);
    printf("Grass: being eaten\n");
  }
  frog->hungry = false;
}

void night_of_frog(Frog* frog) {
  sleep(3);
  printf("Frog: sleeping, sleeping, sleeping\n");
  frog->hungry = true;
}

typedef struct Tree {
  bool oxygen;
  Frog* frog;
} Tree;

void day_of_tree(Tree* tree) {
  tree->oxygen = true;
  sleep(3);
  printf("Tree: creating oxygen\n");
  day_of_frog(tree->frog);
}

void night_of_tree(Tree* tree) {
  tree->oxygen = false;
  sleep(3);
  printf("Tree: doing nothing\n");
  night_of_frog(tree->frog);
}

typedef struct Sun {
  bool light;
  Tree* tree;
} Sun;

void day(Sun* sun) {
  while (true) {
    if (sun->light) {
      sleep(3);
      printf("Sun: shining\n");
      day_of_tree(sun->tree);
      sun->light = false;
    }
    if (!sun->light) {
      sleep(3);
      printf("Sun: not shining\n");
      night_of_tree(sun->tree);
      sun->light = true;
    }
  }
}

int main(int argc, char** argv) {
  Frog frog = { true };
  Tree tree = { false, &frog };
  Sun sun = { true, &tree };
  day(&sun);
  return 0;
}