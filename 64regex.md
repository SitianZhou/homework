Regex Quick Reference
=====================


`a`: the letter a
`[abc]`: a letter of a, b, or c
`[a-c]`: a letter in the range a-c
`[0-9]`: a number in the range 0-9
`(...)`: a group; captures any characters in parentheses
`\s`: any whitespace
`\S`: any non-whitespace
`\w`: any word symbol, including letters, numbers, underscore
`\W`: any non-word symbol
`\d`: any digit
`\D`: any non-digit symbol
`.`: any single character
`\`: escape special characters - eg. `\.` matches an actual dot
`?`: ungreedy quantifier - eg. `\w+?` matches one word symbol
`*`: zero or more - eg. `\s*` matches zero or more whitespaces
`+`: one or more - eg. `\d+` matches one or more numbers
`?`: zero or one - eg. `\w?` matches zero or more word symbol
