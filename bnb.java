/** Node in a state space tree */
private static class Node {
    public int index, level, value, weight;
    public double upperBound;
        
    public Node(int i, int l, int v, int w) {
        index = i; level = l;
        value = v; weight = w;
    }
}

/** Calculates the upper bound on the state space tree nodes */
private static double getUpperBound(int valueSoFar, int remainingCapacity, int weight, int value) {
    if (value == 0 || weight == 0 || remainingCapacity < 0)
        return 0;
    else
        return valueSoFar + remainingCapacity *
          ((double)value /(double)weight);
}

/** Performs a Branch and Bound algorithm to solve the Knapsack problem
  * Referenced from <http://stackoverflow.com/questions/20362196/branch-n-bound-knapsack-0-1-optimization-java>
  */
private static void branchBound(int num, int capacity, int[][] items) {
    Node current, left, right;
    int valueSoFar = 0, remainingCapacity = capacity;
    char[] solution = new char[num];
        
    PriorityQueue<Node> queue = new PriorityQueue<Node>(num, new Comparator<Node>() {
        public int compare (Node a, Node b) {
            return Double.compare(a.upperBound, b.upperBound) * -1;
        }
    });
    double[][] ratios = new double[num][2];
    for (int i = 0; i < num; i++) {
        ratios[i][0] = i + 1;
        ratios[i][1] = (double)items[i + 1][0] / items[i + 1][1];
    }
    Arrays.sort(ratios, new Comparator<double[]>() {
       public int compare(double[] a, double[] b) {
           return Double.compare(a[1], b[1]) * -1;
       }
    });
        
    int item = (int) ratios[0][0];
    current = new Node(0, 0, 0, 0);
    current.upperBound = getUpperBound(0, capacity, items[item][1], items[item][0]);
    queue.add(current);
        
    while (!queue.isEmpty()) {
        current = queue.remove();
        if (current.upperBound > valueSoFar) {
            left = new Node(
                (int) ratios[current.level][0], // index of next best item
                current.level + 1,
                current.value + items[(int)ratios[current.level][0]][0],
                current.weight + items[(int)ratios[current.level][0]][1]);
            left.upperBound = getUpperBound(
                left.value,
                capacity - left.weight,
                items[(int)ratios[current.level][0]][1],
                items[(int)ratios[current.level][0]][0]);
            if (left.weight <= capacity && left.value > valueSoFar) {
                valueSoFar = left.value;
                remainingCapacity = capacity - left.weight;
                solution[left.index - 1] = '1';
            }
            if (left.upperBound > valueSoFar)
                queue.add(left);
                
            // Right node in tree
            right = new Node(
                0, 
                current.level + 1,
                current.value,
                current.weight);
            if (right.level == num)
                right.upperBound = right.value;
            else
                right.upperBound = getUpperBound(
                    current.value,
                    capacity - current.weight,
                    items[(int)ratios[right.level][0]][1],
                    items[(int)ratios[right.level][0]][0]);
            if (right.upperBound > valueSoFar)
                queue.add(right);
        }
    }
        
    System.out.println("BnB: " + valueSoFar + " " + (capacity - remainingCapacity));
    for (int i = 0; i < solution.length; i++)
        System.out.print(solution[i] == '1' ? (i + 1) + " " : "");
    System.out.println();
}