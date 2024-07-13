package sort;

import java.util.Arrays;

public class InsertSort {
    public static void main(String[] args) {
        int[] arr = {4, 2, 7, 1, 3};
        System.out.println(Arrays.toString(insertSort(arr)));
    }

    static int[] insertSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int position = i - 1;

            while (position >= 0 && arr[position] > key) {
                arr[position + 1] = arr[position];
                position -= 1;
            }
            arr[position + 1] = key;
        }

        return arr;
    }
}
