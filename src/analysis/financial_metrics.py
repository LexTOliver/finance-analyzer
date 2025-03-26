import pandas as pd
from src.utils.logger import get_logger

# -- Get the logger
logger = get_logger()


# -- MARGIN AND PROFITABILITY METRICS
def calculate_gross_margin(df: pd.DataFrame, revenue_col: str, cogs_col: str) -> float:
    """
    Calculate the Gross Margin (%) of a company.

    The Gross Margin indicates the percentage of revenue that exceeds the cost of goods sold (COGS).
    It is calculated as follows:
        Gross Margin = (Revenue - COGS) / Revenue

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        revenue_col - str : Column name for the Revenue.
        cogs_col - str : Column name for the Cost of Goods Sold.

    Returns:
        float : Gross Margin.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if revenue_col not in df.columns or cogs_col not in df.columns:
        missing_cols = [col for col in [revenue_col, cogs_col] if col not in df.columns]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Revenue and COGS
    total_revenue = df[revenue_col].sum(skipna=True)
    total_cogs = df[cogs_col].sum(skipna=True)

    # -- Calculate the Gross Margin
    if total_revenue == 0:
        logger.warning("The total Revenue is zero. The Gross Margin will be zero.")
        gross_margin = 0
    else:
        gross_margin = (total_revenue - total_cogs) / total_revenue

    return gross_margin * 100


def calculate_operating_margin(
    df: pd.DataFrame, revenue_col: str, operating_income_col: str
) -> float:
    """
    Calculate the Operating Margin (%) of a company.

    The Operating Margin indicates the percentage of operating income related to the revenue.
    It is calculated as follows:
        Operating Margin = Operating Income / Revenue

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        revenue_col - str : Column name for the Revenue.
        operating_income_col - str : Column name for the Operating Income.

    Returns:
        float : Operational Margin.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if revenue_col not in df.columns or operating_income_col not in df.columns:
        missing_cols = [
            col for col in [revenue_col, operating_income_col] if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Revenue and Operating Income
    total_revenue = df[revenue_col].sum(skipna=True)
    total_operating_income = df[operating_income_col].sum(skipna=True)

    # -- Calculate the Operational Margin
    if total_revenue == 0:
        logger.warning("The total Revenue is zero. The Operating Margin will be zero.")
        operating_margin = 0
    else:
        operating_margin = total_operating_income / total_revenue

    return operating_margin * 100


def calculate_net_margin(
    df: pd.DataFrame, net_income_col: str, revenue_col: str
) -> float:
    """
    Calculate the Net Margin (%) of a company.

    The Net Margin indicates the percentage of revenue that exceeds the total expenses.
    It is calculated as follows:
        Net Margin = Net Income / Revenue

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        net_income_col - str : Column name for the Net Income.
        revenue_col - str : Column name for the Revenue.

    Returns:
        float : Net Margin.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if net_income_col not in df.columns or revenue_col not in df.columns:
        missing_cols = [
            col for col in [revenue_col, net_income_col] if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Net Income and Revenue
    total_net_income = df[net_income_col].sum(skipna=True)
    total_revenue = df[revenue_col].sum(skipna=True)

    # -- Calculate the Net Margin
    if total_revenue == 0:
        logger.warning("The total Revenue is zero. The Net Margin will be zero.")
        net_margin = 0
    else:
        net_margin = total_net_income / total_revenue

    return net_margin * 100


# -- RETURN ON INVESTMENT METRICS --
def calculate_roi(
    df: pd.DataFrame, net_income_col: str, init_investment_col: str
) -> float:
    """
    Calculate the Return on Investment (ROI) of a company.

    The ROI indicates the return on the initial investment made in the company.
    It is calculated as follows:
        ROI = (Net Income - Initial Investment) / Initial Investment

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        net_income_col - str : Column name for the Net Income.
        init_investment_col - str : Column name for the Initial Investment.

    Returns:
        float : Return on Investment.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if net_income_col not in df.columns or init_investment_col not in df.columns:
        missing_cols = [
            col
            for col in [net_income_col, init_investment_col]
            if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Net Income and Initial Investment
    total_net_income = df[net_income_col].sum(skipna=True)
    total_init_investment = df[init_investment_col].sum(skipna=True)

    # -- Calculate the Return on Investment
    if total_init_investment == 0:
        logger.warning("The total Initial Investment is zero. The ROI will be zero.")
        roi = 0
    else:
        roi = (total_net_income - total_init_investment) / total_init_investment

    return roi * 100


def calculate_roe(df: pd.DataFrame, net_income_col: str, equity_col: str) -> float:
    """
    Calculate the Return on Equity (ROE) of a company.

    The ROE indicates how much profit a company generates from its shareholders' equity.
    It is calculated as follows:
        ROE = Net Income / Equity

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        net_income_col - str : Column name for the Net Income.
        equity_col - str : Column name for the Equity.

    Returns:
        float : Return on Equity.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if net_income_col not in df.columns or equity_col not in df.columns:
        missing_cols = [
            col for col in [equity_col, net_income_col] if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Net Income and Equity
    total_net_income = df[net_income_col].sum(skipna=True)
    total_equity = df[equity_col].sum(skipna=True)

    # -- Calculate the Return on Equity
    if total_equity == 0:
        logger.warning("The total Equity is zero. The ROE will be zero.")
        roe = 0
    else:
        roe = total_net_income / total_equity

    return roe * 100


def calculate_roa(df: pd.DataFrame, net_income_col: str, assets_col: str) -> float:
    """
    Calculate the Return on Assets (ROA) of a company.

    The ROA indicates how much profit a company generates from its assets.
    It is calculated as follows:
        ROA = Net Income / Total Assets

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        net_income_col - str : Column name for the Net Income.
        assets_col - str : Column name with the amount of Assets.

    Returns:
        float : Return on Assets.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if net_income_col not in df.columns or assets_col not in df.columns:
        missing_cols = [
            col for col in [net_income_col, assets_col] if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Net Income and Total Assets
    total_net_income = df[net_income_col].sum(skipna=True)
    total_assets = df[assets_col].sum(skipna=True)

    # -- Calculate the Return on Assets
    if total_assets == 0:
        logger.warning("The total Total Assets is zero. The ROA will be zero.")
        roa = 0
    else:
        roa = total_net_income / total_assets

    return roa * 100


# -- GROWTH INDICATORS --
def calculate_revenue_growth(
    df: pd.DataFrame, revenue_col: str, date_col: str
) -> float:
    """
    Calculate the Revenue Growth of a company.

    The Revenue Growth indicates the percentage increase in revenue from one period to the next.
    It is calculated as follows:
        Revenue Growth = (Revenue(t) - Revenue(t-1)) / Revenue(t-1)

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        revenue_col - str : Column name for the Revenue.
        date_col - str : Column name for the Date.

    Returns:
        float : Revenue Growth.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if revenue_col not in df.columns or date_col not in df.columns:
        missing_cols = [col for col in [revenue_col, date_col] if col not in df.columns]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Sort the DataFrame by the Date
    df = df.sort_values(by=date_col, ascending=True)

    # -- Get the Revenue values
    revenue_values = df[revenue_col].values

    # -- Calculate the Revenue Growth
    if len(revenue_values) < 2:
        logger.warning(
            "There are not enough data points to calculate the Revenue Growth."
        )
        revenue_growth = 0
    else:
        revenue_growth = (revenue_values[-1] - revenue_values[-2]) / revenue_values[-2]

    return revenue_growth * 100


def calculate_net_income_growth(
    df: pd.DataFrame, net_income_col: str, date_col: str
) -> float:
    """
    Calculate the Net Income Growth of a company.

    The Net Income Growth indicates the percentage increase in net income from one period to the next.
    It is calculated as follows:
        Net Income Growth = (Net Income(t) - Net Income(t-1)) / Net Income(t-1)

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        net_income_col - str : Column name for the Net Income.
        date_col - str : Column name for the Date.

    Returns:
        float : Net Income Growth.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if net_income_col not in df.columns or date_col not in df.columns:
        missing_cols = [
            col for col in [net_income_col, date_col] if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Sort the DataFrame by the Date
    df = df.sort_values(date_col)

    # -- Get the Net Income values
    net_income_values = df[net_income_col].values

    # -- Calculate the Net Income Growth
    if len(net_income_values) < 2:
        logger.warning(
            "There are not enough data points to calculate the Net Income Growth."
        )
        net_income_growth = 0
    else:
        net_income_growth = (
            net_income_values[-1] - net_income_values[-2]
        ) / net_income_values[-2]

    return net_income_growth * 100


# -- FINANCIAL HEALTH INDICATORS --
def calculate_ebitda(
    df: pd.DataFrame,
    operating_income_col: str,
    depreciation_col: str,
    amortization_col: str,
) -> float:
    """
    Calculate the Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) of a company.

    The EBITDA indicates the profitability of a company before the financial and accounting deductions.
    It is calculated as follows:
        EBITDA = Operating Income + Depreciation + Amortization

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        operating_income_col - str : Column name for the Operating Income.
        depreciation_col - str : Column name for the Depreciation.
        amortization_col - str : Column name for the Amortization.

    Returns:
        float : EBITDA.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if (
        operating_income_col not in df.columns
        or depreciation_col not in df.columns
        or amortization_col not in df.columns
    ):
        missing_cols = [
            col
            for col in [depreciation_col, operating_income_col, amortization_col]
            if col not in df.columns
        ]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Operating Income, Depreciation, and Amortization
    total_operating_income = df[operating_income_col].sum(skipna=True)
    total_depreciation = df[depreciation_col].sum(skipna=True)
    total_amortization = df[amortization_col].sum(skipna=True)

    # -- Calculate the EBITDA
    ebitda = total_operating_income + total_depreciation + total_amortization

    return ebitda


def calculate_debt_ratio(df: pd.DataFrame, debt_col: str, assets_col: str) -> float:
    """
    Calculate the Debt Ratio of a company.

    The Debt Ratio indicates the percentage of assets financed by debt.
    It is calculated as follows:
        Debt Ratio = Total Debt / Total Assets

    Parameters:
        df - pd.DataFrame : DataFrame containing the data.
        debt_col - str : Column name for the Total Debt.
        assets_col - str : Column name for the Total Assets.

    Returns:
        float : Debt Ratio.

    Raises:
        KeyError : If the indicated columns are not present in the DataFrame.
    """
    # -- Check if the columns exist
    if debt_col not in df.columns or assets_col not in df.columns:
        missing_cols = [col for col in [debt_col, assets_col] if col not in df.columns]
        logger.error(f"Missing columns in DataFrame: {missing_cols}")
        raise KeyError(f"Missing columns in DataFrame: {missing_cols}")

    # -- Get the sum of the Total Debt and Total Assets
    total_debt = df[debt_col].sum(skipna=True)
    total_assets = df[assets_col].sum(skipna=True)

    # -- Calculate the Debt Ratio
    if total_assets == 0:
        logger.warning("The total Total Assets is zero. The Debt Ratio will be zero.")
        debt_ratio = 0
    else:
        debt_ratio = total_debt / total_assets

    return debt_ratio * 100
