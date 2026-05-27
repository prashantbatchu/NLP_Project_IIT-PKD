import re

def clean_vtt_to_txt(vtt_file_path, output_txt_path=None):
    if output_txt_path is None:
        output_txt_path = vtt_file_path.replace('.vtt', '.txt')
    
    with open(vtt_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    text_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('WEBVTT') or '-->' in line:
            continue
        
        line = re.sub(r'<[^>]+>', '', line)
        
        if line:
            text_lines.append(line)
    
    full_text = '\n'.join(text_lines)
    full_text = re.sub(r'\n\s*\n', '\n\n', full_text)
    
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Input:  {vtt_file_path}")
    print(f"Output: {output_txt_path}")
    return output_txt_path

if __name__ == "__main__":
    
    input_vtt1 = "data/cleaned_transripts/MGB/RahulGandhi&TejashwiYadavMuzaffarpur.vtt"
    input_vtt2 = "data/cleaned_transripts/MGB/TejashwiYadavkarakat.vtt"
    input_vtt3 = "data/cleaned_transripts/NDA/modiinchappra_trimmed.vtt"
    input_vtt4 = "data/cleaned_transripts/NDA/AmitShahLakhisarai.vtt"
    
    clean_vtt_to_txt(input_vtt1)
    clean_vtt_to_txt(input_vtt2)
    clean_vtt_to_txt(input_vtt3)
    clean_vtt_to_txt(input_vtt4)