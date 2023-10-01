from . import router_awesome as router


router.tags = ["Awesome"]


@router.get("/caller")
async def get_who_you_are(message: str):
    return f"You're {message}"
