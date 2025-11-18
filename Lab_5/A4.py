import re

def decode_rle(sequence):
    decoded = []
    i = 0
    while i < len(sequence):
        if sequence[i].isdigit():
            count = int(sequence[i])
            char = sequence[i+1]
            decoded.append(char * count)
            i += 2
        else:
            decoded.append(sequence[i])
            i += 1
    return ''.join(decoded)

def read_sequences(filename):
    sequences = {}
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            parts = line.split('\t')
            if len(parts) >= 3:
                protein_name = parts[0].strip()
                organism = parts[1].strip()
                amino_chain = parts[2].strip()
                
                if any(char.isdigit() for char in amino_chain):
                    amino_chain = decode_rle(amino_chain)
                
                sequences[protein_name] = {
                    'organism': organism,
                    'chain': amino_chain
                }
    
    return sequences

def execute_search(sequences, search_sequence):
    results = []
    
    for protein_name, data in sequences.items():
        if search_sequence in data['chain']:
            results.append({
                'organism': data['organism'],
                'protein': protein_name
            })
    
    return results

def execute_diff(sequences, protein1, protein2):
    missing = []
    if protein1 not in sequences:
        missing.append(protein1)
    if protein2 not in sequences:
        missing.append(protein2)
    
    if missing:
        return {'missing': missing}
    
    chain1 = sequences[protein1]['chain']
    chain2 = sequences[protein2]['chain']
    
    min_len = min(len(chain1), len(chain2))
    differences = 0
    
    for i in range(min_len):
        if chain1[i] != chain2[i]:
            differences += 1
    
    differences += abs(len(chain1) - len(chain2))
    
    return {'differences': differences}

def execute_mode(sequences, protein_name):
    """Выполняет операцию mode"""
    if protein_name not in sequences:
        return {'missing': protein_name}
    
    chain = sequences[protein_name]['chain']
    
    freq = {}
    for amino_acid in chain:
        if amino_acid in freq:
            freq[amino_acid] += 1
        else:
            freq[amino_acid] = 1
    
    max_freq = max(freq.values())
    
    most_common = [aa for aa, count in freq.items() if count == max_freq]
    
    most_common.sort()
    result_aa = most_common[0]
    
    return {'amino_acid': result_aa, 'count': max_freq}

def main():
    sequences = read_sequences('sequences.txt')
    
    output_lines = []
    output_lines.append("Maria Bondarenko")
    output_lines.append("Genetic searching")
    output_lines.append("")
    
    with open('commands.txt', 'r', encoding='utf-8') as f:
        command_number = 1
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split('\t')
            command = parts[0]
            
            cmd_num_str = f"{command_number:03d}"
            
            if command == 'search':
                search_seq = parts[1]
                results = execute_search(sequences, search_seq)
                
                output_lines.append(f"{cmd_num_str} search {search_seq}")
                output_lines.append("organism protein")
                
                if results:
                    for result in results:
                        output_lines.append(f"{result['organism']} {result['protein']}")
                else:
                    output_lines.append("NOT FOUND")
                    
            elif command == 'diff':
                protein1 = parts[1]
                protein2 = parts[2]
                result = execute_diff(sequences, protein1, protein2)
                
                output_lines.append(f"{cmd_num_str} diff {protein1} {protein2}")
                output_lines.append("amino-acids difference:")
                
                if 'missing' in result:
                    missing_str = ", ".join(result['missing'])
                    output_lines.append(f"MISSING: {missing_str}")
                else:
                    output_lines.append(str(result['differences']))
                    
            elif command == 'mode':
                protein_name = parts[1]
                result = execute_mode(sequences, protein_name)
                
                output_lines.append(f"{cmd_num_str} mode {protein_name}")
                output_lines.append("amino-acid occurs:")
                
                if 'missing' in result:
                    output_lines.append(f"MISSING: {result['missing']}")
                else:
                    output_lines.append(f"{result['amino_acid']} {result['count']}")
            
            output_lines.append("-" * 50)
            command_number += 1
    
    if output_lines and output_lines[-1] == "-" * 50:
        output_lines.pop()
    
    with open('genedata.txt', 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')

if name == "main":
    main()
