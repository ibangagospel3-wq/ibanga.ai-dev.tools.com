import asyncio
from sqlalchemy import select
from app.database import AsyncSessionLocal,engine,Base
from app.models import Lesson,Challenge
LESSONS=[('HTML','Introduction to HTML'),('HTML','HTML structure'),('HTML','Semantic HTML'),('CSS','Introduction to CSS'),('CSS','Flexbox'),('CSS','Responsive design'),('JavaScript','Introduction'),('JavaScript','Variables'),('JavaScript','DOM events'),('JavaScript','LocalStorage')]
async def seed():
    async with engine.begin() as connection:await connection.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as db:
        for index,(category,title) in enumerate(LESSONS,1):
            slug=f'{category.lower()}-{index}'
            if not await db.scalar(select(Lesson).where(Lesson.slug==slug)):db.add(Lesson(title=title,slug=slug,category=category,description=f'Learn {title.lower()} through an example.',content=f'<h2>{title}</h2><p>Practice this concept in the IBANGA playground.</p>',difficulty='Beginner',order_number=index))
        if not await db.scalar(select(Challenge).where(Challenge.title=='Interactive button')):db.add(Challenge(title='Interactive button',description='Change a button background when clicked.',category='JavaScript',difficulty='Beginner',starter_html='<button id="color-button">Change color</button>',starter_css='',starter_javascript='',expected_behavior='color-button addEventListener'))
        await db.commit()
    await engine.dispose()
if __name__=='__main__':asyncio.run(seed())
