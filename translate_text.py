from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='fr', target='en').translate_file('./Downloads/se braquer_m.txt')
f = open("./Downloads/se braquer_t.txt", "w")
f.write("Text:"+translated)
f.close()
