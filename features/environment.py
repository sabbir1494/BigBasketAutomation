from utils.driver_factory import DriverFactory
from utils.screenshot_utils import ScreenshotUtils
from utils.logger import Logger

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


logger = Logger.get_logger(__name__)


def before_all(context):
    logger.info("===================================")
    logger.info("BigBasket BDD Test Execution Started")
    logger.info("===================================")


def before_scenario(context, scenario):

    logger.info("-----------------------------------")
    logger.info(f"Starting Scenario: {scenario.name}")

    try:
        context.driver = DriverFactory.get_driver()

        # Page Objects
        context.home = HomePage(context.driver)
        context.search = SearchPage(context.driver)
        context.product = ProductPage(context.driver)
        context.cart = CartPage(context.driver)

        logger.info("Chrome WebDriver initialized successfully")

    except Exception as error:
        logger.error(
            f"Failed to initialize WebDriver: {error}",
            exc_info=True
        )
        raise


def after_scenario(context, scenario):

    try:

        if scenario.status == "failed":

            logger.error(
                f"Scenario FAILED: {scenario.name}"
            )

            if hasattr(context, "driver") and context.driver:

                ScreenshotUtils.capture(
                    context.driver,
                    scenario.name.replace(" ", "_")
                )

                logger.info(
                    f"Failure screenshot captured for: {scenario.name}"
                )

        else:

            logger.info(
                f"Scenario PASSED: {scenario.name}"
            )

    except Exception as error:

        logger.error(
            f"Error during after_scenario: {error}",
            exc_info=True
        )

    finally:

        if hasattr(context, "driver") and context.driver:

            try:
                context.driver.quit()

                logger.info(
                    f"Browser closed: {scenario.name}"
                )

            except Exception as error:

                logger.error(
                    f"Error while closing browser: {error}",
                    exc_info=True
                )


def after_all(context):

    logger.info("===================================")
    logger.info("BigBasket BDD Test Execution Finished")
    logger.info("===================================")