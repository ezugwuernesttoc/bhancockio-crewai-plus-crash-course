from pydantic import BaseModel, Field


class EmailContent(BaseModel):
    name: str = Field(..., description="The recipient's full name")
    email: str = Field(..., description="The recipient's email address")
    subject: str = Field(..., description="The subject line of the email")
    content: str = Field(..., description="The body content of the email")
