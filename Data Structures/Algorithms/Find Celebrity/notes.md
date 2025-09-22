# 277. Find the Celebrity

**Difficulty:** Medium  
**Tags:** Graph, Two Pointers, Interactive  
**Leetcode Link:** [277. Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/)

---

## Problem Description

You're at a party with `n` people labeled from `0` to `n - 1`. Among these people, there might be **exactly one celebrity**. A celebrity is defined as someone who:

- Is known by all other `n - 1` people at the party
- Does **not** know any of the other people

Your task is to identify who the celebrity is, or determine that **no celebrity exists** at the party.

You can only gather information by asking questions in the form:  
**"Does person A know person B?"**  
This is done through a helper function `knows(a, b)` which returns `true` if person `a` knows person `b`, and `false` otherwise.

The goal is to **minimize the number of questions asked** (in terms of asymptotic complexity) while finding the celebrity.

---

## Function Signature

The function should return:

- The celebrity's label (a number from `0` to `n - 1`) if a celebrity exists
- `-1` if there is **no celebrity** at the party

> **Note:**  
> You don't have direct access to the underlying relationship graph.  
> You can only use the `knows(a, b)` function to query relationships between people.