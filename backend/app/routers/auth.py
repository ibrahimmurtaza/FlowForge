"""Auth routes — registration, login, logout, and current-user retrieval."""

from fastapi import APIRouter, Depends, HTTPException, status
from supabase import AuthApiError, Client

from app.auth import get_current_user
from app.schemas.auth import (
    AuthResponse,
    LoginRequest,
    MeResponse,
    RegisterRequest,
    UserInfo,
)
from app.supabase_client import get_supabase_client


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
def register(
    body: RegisterRequest,
    client: Client = Depends(get_supabase_client)
):
    """Register a new user via Supabase Auth."""
    try:
        response = client.auth.sign_up({"email": body.email, "password": body.password})
    except AuthApiError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    session = response.session
    user = response.user
    if not session or not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Registration failed — no session returned",
        )

    return AuthResponse(
        access_token=session.access_token,
        refresh_token=session.refresh_token,
        user=UserInfo(id=user.id, email=user.email or ""),
    )


@router.post("/login", response_model=AuthResponse)
def login(
    body: LoginRequest,
    client: Client = Depends(get_supabase_client)
):
    """Log in an existing user via Supabase Auth."""
    try:
        response = client.auth.sign_in_with_password(
            {"email": body.email, "password": body.password}
        )
    except AuthApiError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc))

    session = response.session
    user = response.user
    if not session or not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login failed — invalid credentials",
        )

    return AuthResponse(
        access_token=session.access_token,
        refresh_token=session.refresh_token,
        user=UserInfo(id=user.id, email=user.email or ""),
    )


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout():
    """Log out the current user.

    Supabase JWT tokens are stateless — the client discards the token.
    This endpoint exists so frontends have a conventional POST to call.
    """
    return None


@router.get("/me", response_model=MeResponse)
def me(current_user: dict = Depends(get_current_user)):
    """Return the currently authenticated user's info."""
    return MeResponse(id=current_user["id"], email=current_user["email"])
