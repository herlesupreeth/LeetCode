/* All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
*/

public class Solution {
	public List<String> findRepeatedDnaSequences(String s) {
		String m = new String(s);
		if (m.length() < 11)
			return new ArrayList<String>();
		
		m = m.replace('A', '1');
		m = m.replace('C', '2');
		m = m.replace('G', '3');
		m = m.replace('T', '4');
		
		ArrayList<Long> al = new ArrayList<Long>();
		for(int i=0;i<m.length()-9;i++){
			al.add(Long.parseLong(m.substring(i, i+10)));
		}
		
		HashSet<Long> dnaSet = new HashSet<Long>(al);        
		if (al.size() == dnaSet.size())
			return new ArrayList<String>();
		
		for (long mn: dnaSet){
			al.remove(al.indexOf(mn));
		}
		
		HashSet<Long> finres = new HashSet<Long>(al);
		al.clear();
		dnaSet.clear();
		ArrayList<String> res = new ArrayList<String>();
		for (long mn: finres){
			String sr = Long.toString(mn);
			sr = sr.replace('1','A');
			sr = sr.replace('2','C');
			sr = sr.replace('3','G');
			sr = sr.replace('4','T');
			res.add(sr);
		}
		return res;
	}
}