# 🔍 Binary Search (C#)

Binary Search is a fundamental algorithm used to efficiently search for a target value in a **sorted array**. It repeatedly divides the search interval in half, drastically reducing the number of comparisons needed.

This implementation is written in C# and serves as both a reference and learning tool while preparing for technical interviews and coding assessments.

---

## 📌 How It Works

1. Start with two pointers: `left` at the beginning, `right` at the end of the array.
2. Calculate the middle index.
3. Compare the middle element with the target:
   - ✅ If equal → Target found.
   - 🔽 If target is smaller → Search the left half.
   - 🔼 If target is larger → Search the right half.
4. Repeat until the target is found or the search interval is empty.

---

## 💻 Example Code (C#)

```csharp
int[] data = {1, 3, 4, 6, 8, 10, 13};
int target = 8;

int left = 0;
int right = data.Length - 1;

while (left <= right)
{
    int mid = left + (right - left) / 2;

    if (data[mid] == target)
    {
        Console.WriteLine($"Target found at index {mid}: {data[mid]}");
        return;
    }
    else if (data[mid] < target)
    {
        left = mid + 1;
    }
    else
    {
        right = mid - 1;
    }
}

Console.WriteLine("Target Not Found.");
