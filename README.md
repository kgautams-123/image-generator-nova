# AI Image Generator with Amazon Nova Canvas

A Streamlit web application that generates high-quality images using Amazon Nova Canvas through Amazon Bedrock. This application supports text-to-image generation with negative prompting capabilities.

## Features

- Text-to-image generation
- Negative prompt support
- Multiple image generation (up to 4 images)
- Customizable image dimensions (512x512 to 2048x2048)
- Multiple quality settings (draft, standard, premium)
- Image download functionality
- User-friendly interface

## Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS credentials configured
- Basic understanding of Python and Streamlit

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kgautams-123/image-generator-nova.git
cd image-generator-nova
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## AWS Configuration

1. Configure AWS credentials:
```bash
aws configure
```
Enter your:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-east-1)
- Output format (json)

2. Ensure you have access to Amazon Bedrock services

## Usage

1. Start the Streamlit app:
```bash
streamlit run image_generator.py
```

2. Access the web interface at `http://localhost:8501`

3. Enter your prompt in the text area

4. (Optional) Add negative prompts to exclude unwanted elements

5. Adjust settings in the sidebar:
   - Image quality
   - Image dimensions
   - Number of images

6. Click "Generate Image" and wait for the results

7. Download generated images using the download buttons

## Project Structure

```
ai-image-generator/
├── image_generator.py.py              # Main Streamlit application
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── .gitignore                         # Git ignore file
```

## Requirements

```
streamlit==1.28.0
boto3==1.28.44
Pillow==10.0.0
```

## Features in Detail

### Image Generation Options
- Quality levels: draft, standard, premium
- Dimensions: 512x512 to 2048x2048
- Multiple image generation
- Negative prompting

### User Interface
- Clean and intuitive design
- Real-time progress updates
- Image preview
- Download capabilities

### Technical Features
- AWS Bedrock integration
- Error handling
- Progress tracking
- Efficient image processing

## Best Practices

1. Prompt Writing
   - Be specific and descriptive
   - Use artistic terminology
   - Include style references

2. Performance Optimization
   - Start with draft quality for testing
   - Use smaller dimensions for iterations
   - Increase quality for final outputs

3. Resource Management
   - Monitor AWS usage
   - Clean up generated images
   - Handle errors gracefully

## Troubleshooting

Common issues and solutions:

1. AWS Credentials
```bash
aws configure
```
Verify credentials are correctly set up

2. Dependencies
```bash
pip install -r requirements.txt
```
Ensure all dependencies are installed

3. Access Issues
- Check AWS Bedrock access
- Verify region settings
- Confirm IAM permissions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Amazon Bedrock team
- Streamlit community
- Contributors and testers

## Support

For support:
1. Check existing issues
2. Create a new issue
3. Contact project maintainers

## Future Enhancements

- Style preset support
- Batch processing
- Advanced image settings
- Custom model parameters
- Image editing capabilities
