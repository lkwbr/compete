import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

class MyClass
{
    public static void main (String[] args) throws java.lang.Exception {
        int[] documents = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
        int[][] documentWords = new int[][] {
            new int[] {5, 4, 2, 10},
            new int[] {5, 1},
            new int[] {2, 7, 8, 9, 10, 14, 22, 44, 100, 200, 23, 44, 4, 9111, 33243, 2346234, 3421},
            new int[] {5, 1},
            new int[] {5, 1},
            new int[] {6, 2, 3, 56},
            new int[] {5, 1},
            new int[] {66, 1},
            new int[] {5},
            new int[] {5, 1},
            new int[] {5, 1, 234, 2341235, 22, 6613, 234, 33333},
        };
        sparseSimilarity(documents, documentWords);
    }

    public static void sparseSimilarity(int[] documents, int[][] documentWords) {
        // Create HashMap
        HashMap<Integer, HashSet> documentMap = new HashMap();
        for (int i = 0; i < documents.length; i++) {
          int document = documents[i];
          int[] words = documentWords[i];
          HashSet hashedWords = new HashSet<Integer>();
          for (int word : words) hashedWords.add(word);
          documentMap.put(document, hashedWords);
        }
        // Compare HashSets
        for (int i = 0; i < documents.length - 1; i++) {
          int documentA = documents[i];
          HashSet documentASet = documentMap.get(documentA);
          for (int j = i + 1; j < documents.length; j++) {
            int documentB = documents[j];
            HashSet documentBSet = documentMap.get(documentB);
            HashSet documentIntersectionSet = new HashSet(documentASet);
            HashSet documentUnionSet = new HashSet(documentASet);
            documentIntersectionSet.retainAll(documentBSet);
            documentUnionSet.addAll(documentBSet);
            int unionCount = documentUnionSet.size();
            int intersectionCount = documentIntersectionSet.size();
            float similarity = intersectionCount / (float) unionCount;
            System.out.println(String.format("%d, %d\t:\t%.2f", documentA, documentB, similarity));
          }
        }
    }
}
