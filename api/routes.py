from fastapi import APIRouter, Depends
from scraper.tiktok_scraper import TikTokScraper
from ai_analysis.trend_analyzer import TrendAnalyzer
from ai_analysis.content_generator import ContentGenerator
from database.db_manager import DBManager

router = APIRouter()

def get_scraper():
    return TikTokScraper()

def get_trend_analyzer():
    return TrendAnalyzer()

def get_content_generator():
    return ContentGenerator("your-openai-api-key")

def get_db_manager():
    return DBManager()

@router.get("/trends")
async def get_trends(
    scraper: TikTokScraper = Depends(get_scraper),
    analyzer: TrendAnalyzer = Depends(get_trend_analyzer),
    db: DBManager = Depends(get_db_manager)
):
    trending_data = await scraper.scrape_trending_data()
    descriptions = [item['description'] for item in trending_data]
    trends = analyzer.analyze_trends(descriptions)
    db.save_trends(trends)
    return {"trends": trends}

@router.post("/generate-content")
async def generate_content(
    trend: str,
    generator: ContentGenerator = Depends(get_content_generator)
):
    content_idea = generator.generate_content_idea(trend)
    hashtags = generator.suggest_hashtags(content_idea)
    return {"content_idea": content_idea, "hashtags": hashtags}
