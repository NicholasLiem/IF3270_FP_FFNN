from Utils.JsonModelParser import JsonModelParser

def main():
    json_path = "Tests/" + input("Input json file name (*.json in Tests folder): ")
    parser = JsonModelParser(json_path)
    if parser.data:
        print("Model Information:")
        print("Input_Size:", parser.input_size)
        print("Layers:", parser.layers)

        print("Input Data:", parser.input_data)
        print("Weights:", parser.weights)
        print("Expected Output:", parser.output)
        print("Maximum SSE:", parser.max_sse)
    else:
        print("Failed to load or parse the JSON data.")

if __name__ == '__main__':
    main()
