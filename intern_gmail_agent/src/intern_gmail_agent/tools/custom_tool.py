# src/my_project/tools/custom_tool.py
import PyPDF2
from crewai.tools import BaseTool

class ResumeExtractorTool(BaseTool):
    name = "resume_extractor"
    description = str("Extract text content from a PDF resume file.")

    def run(self, file_path: str) -> str:
        reader = PyPDF2.PdfReader(file_path)
        return "\n".join([page.extract_text() for page in reader.pages])

class CompanyRequirementsTool(BaseTool):
    name = "company_requirements"
    description = str("Returns the input company requirements text.")

    def run(self, text: str) -> str:
        return text
