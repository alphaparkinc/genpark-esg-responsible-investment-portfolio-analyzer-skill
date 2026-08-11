from client import EsgResponsibleInvestmentPortfolioAnalyzerClient

def main():
    client = EsgResponsibleInvestmentPortfolioAnalyzerClient()
    res = client.analyze_portfolio([{"ticker": "CLEAN", "qty": 100}], "STRICT_SUSTAINABILITY")
    print(f"ESG Rating: {res['esg_rating']}")
    print(f"Carbon Footprint: {res['carbon_footprint_tonnes']} tonnes")
    print("Suggestions:", res["rebalancing_suggestions"])

if __name__ == "__main__":
    main()
