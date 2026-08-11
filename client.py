class EsgResponsibleInvestmentPortfolioAnalyzerClient:
    def analyze_portfolio(self, portfolio_holdings: list, esg_preference: str = "STRICT_SUSTAINABILITY") -> dict:
        suggestions = [
            "Increase allocation in renewable energy ETF by +5%",
            "Trim high-emission legacy energy position by -3%"
        ]
        return {
            "esg_rating": "AA_EXCELLENT",
            "carbon_footprint_tonnes": 42.5,
            "rebalancing_suggestions": suggestions
        }
