from pydantic import BaseModel
from typing import Optional
from app.models import MaritalStatus, Gender, LawyerPosition, EducationDegree, RequestType
from enum import Enum


# User
class ISecureUser(BaseModel):
    id: Optional[int] = None
    isLawyer: Optional[bool] = None
    username: str
    fullname: str
    phoneNumber: str
    email: str


class ICreateUserBody(ISecureUser):
    password: str


class ICreateUserController(ISecureUser):
    hashedPassword: str


class IUpdateUserBody(BaseModel):
    username: Optional[str] = None
    fullname: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None


class IUpdateUserController(BaseModel):
    username: Optional[str] = None
    fullname: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None


class IUpdateUserPasswordBody(BaseModel):
    currentPassword: str
    newPassword: str


# Lawyer
class ISecureLawyer(BaseModel):
    id: Optional[int] = None
    gender: Gender
    age: int
    maritalStatus: MaritalStatus
    provinceId: int
    cityId: int
    eduDegree: EducationDegree
    studyField: str
    profilePic: Optional[str] = None
    licenseCode: str
    position: LawyerPosition
    experienceYears: int
    biography: str
    officePhoneNumber: Optional[str] = None
    officeAddress: Optional[str] = None
    specialtyId: int


class ICreateLawyerBody(ISecureLawyer):
    username: str
    fullname: str
    phoneNumber: str
    email: str
    password: str


class ICreateLawyerController(ISecureLawyer, ICreateUserController):
    pass


# Question
class ICreateQuestionBody(BaseModel):
    questionCategoryId: int
    description: str
    isPrivate: bool


class ICreateQuestionController(ICreateQuestionBody):
    userId: int


# Answer
class ICreateAnswerBody(BaseModel):
    questionId: int
    description: str


class ICreateAnswerController(ICreateAnswerBody):
    lawyerId: int
