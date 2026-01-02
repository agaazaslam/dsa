
#### Date: 5th Nov 2025 

##### Intuition
- Iterate over String Array.
- for each string create an character occurrence array. 
- make this array a key for dict and add current string.
- strings with similar occurrences will be grouped together 
- return required list  

**Important**   
keys cannot be mutable so convert array to tuple 
before returning convert dict to list and send only dict values.



