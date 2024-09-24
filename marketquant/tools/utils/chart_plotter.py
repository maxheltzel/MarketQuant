import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
from typing import Optional, Dict, Any


class LinearChart:
    def __init__(self,
                 dataframe: pd.DataFrame,
                 plot_type: str,
                 figure_size=(12, 8),
                 dpi=100,
                 font_size=12,
                 grid: bool = True,
                 grid_color: str = 'grey',
                 grid_line_style: str = "--",
                 grid_line_width: float = 0.5,
                 axis_color: str = 'black',
                 tick_color: str = 'black',
                 axis_line_width: float = 1.0,
                 x_rotation: int = 45,
                 legend: bool = True,
                 title: str = "Chart",
                 title_font_size: int = 16,
                 title_font_color: str = "navy",
                 xlabel: str = "",
                 ylabel: str = "",
                 xlabel_font_size: int = 14,
                 ylabel_font_size: int = 14,
                 label_color: str = "purple",
                 background_color: str = "white",
                 logo_path: str = 'marketquant/MarketQuant_Logo.png'):
        """
        Initialize the LinearChart with the given DataFrame and customization options.

        :param dataframe: A pandas DataFrame containing the data.
        :param plot_type: Type of chart to plot ('line' or 'candlestick').
        :param figure_size: Tuple for figure size (width, height).
        :param dpi: DPI for the figure.
        :param font_size: Font size for x and y labels.
        :param grid: Enable or disable grid.
        :param grid_color: Color of the grid lines.
        :param grid_line_style: Style of the grid lines (e.g., '--', '-').
        :param grid_line_width: Thickness of the grid lines.
        :param axis_color: Color of the axes.
        :param tick_color: Color of the tick marks.
        :param axis_line_width: Width of the axis lines.
        :param x_rotation: Rotation of the x-axis labels.
        :param legend: Whether to show the legend.
        :param title: Title of the chart.
        :param title_font_size: Font size of the chart title.
        :param title_font_color: Color of the chart title.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param xlabel_font_size: Font size for the x-axis label.
        :param ylabel_font_size: Font size for the y-axis label.
        :param label_color: Color for both x and y labels.
        :param background_color: Background color of the chart.
        :param logo_path: File path to the MarketQuant logo image.
        """
        self.dataframe = dataframe
        self.plot_type = plot_type.lower()
        self.figure_size = figure_size
        self.dpi = dpi
        self.font_size = font_size
        self.grid = grid
        self.grid_color = grid_color
        self.grid_line_style = grid_line_style
        self.grid_line_width = grid_line_width
        self.axis_color = axis_color
        self.tick_color = tick_color
        self.axis_line_width = axis_line_width
        self.x_rotation = x_rotation
        self.legend = legend
        self.title = title
        self.title_font_size = title_font_size
        self.title_font_color = title_font_color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlabel_font_size = xlabel_font_size
        self.ylabel_font_size = ylabel_font_size
        self.label_color = label_color
        self.background_color = background_color
        self.logo_path = logo_path

        self.supported_plot_types = ['line', 'candlestick']

        if self.plot_type not in self.supported_plot_types:
            raise ValueError(f"Unsupported plot type '{self.plot_type}'. "
                             f"Supported types: {self.supported_plot_types}")

    def validate_data(self) -> bool:
        """
        Validate if the DataFrame contains the required columns based on the plot type.

        :return: True if valid, False otherwise.
        """
        if self.plot_type == 'line':
            required_columns = {'x', 'y'}
        elif self.plot_type == 'candlestick':
            required_columns = {'Date', 'Open', 'High', 'Low', 'Close'}
        else:
            required_columns = set()

        if required_columns.issubset(self.dataframe.columns):
            print("Data validation successful. The DataFrame contains the required columns.")
            return True
        else:
            missing_columns = required_columns - set(self.dataframe.columns)
            print(f"Data validation failed. Missing columns: {missing_columns}")
            return False

    def add_logo(self, ax):
        """
        Add the MarketQuant logo to the bottom left of the chart.

        :param ax: The axis to add the logo to.
        """
        if os.path.exists(self.logo_path):
            img = plt.imread(self.logo_path)
            imagebox = OffsetImage(img, zoom=0.1, alpha=0.8)
            ab = AnnotationBbox(imagebox, (0, 0), frameon=False, xycoords='axes fraction',
                                boxcoords="offset points", pad=0.5, xybox=(50, 50))
            ax.add_artist(ab)
        else:
            print(f"Logo image not found at {self.logo_path}")

    def plot_chart(self,
                   line_color: str = 'green',
                   candlestick_style: str = 'classic',
                   candlestick_type: str = 'ohlc',
                   **kwargs):
        """
        Plot the specified chart type with customizable options.

        :param line_color: Color of the line chart.
        :param candlestick_style: Style of the candlestick chart (default: 'classic').
        :param candlestick_type: Type of candlestick chart ('ohlc' or 'candle').
        :param kwargs: Additional keyword arguments for customization.
        """
        if not self.validate_data():
            return

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=self.figure_size, dpi=self.dpi)

        # Set background color
        fig.patch.set_facecolor(self.background_color)
        ax.set_facecolor(self.background_color)

        if self.plot_type == 'line':
            # Plot line chart
            ax.plot(self.dataframe['x'], self.dataframe['y'], color=line_color, label='Line')

        elif self.plot_type == 'candlestick':
            # Ensure 'Date' column is datetime
            if not pd.api.types.is_datetime64_any_dtype(self.dataframe['Date']):
                self.dataframe['Date'] = pd.to_datetime(self.dataframe['Date'])

            self.dataframe.set_index('Date', inplace=True)

            # Plot candlestick chart using mplfinance
            mpf.plot(self.dataframe,
                     type='candle' if candlestick_type == 'candle' else 'ohlc',
                     style=candlestick_style,
                     ax=ax,
                     show_nontrading=False,
                     **kwargs)

        # Customize grid
        if self.grid:
            ax.grid(True, color=self.grid_color, linestyle=self.grid_line_style, linewidth=self.grid_line_width)

        # Customize axes
        ax.spines['top'].set_color(self.axis_color)
        ax.spines['bottom'].set_color(self.axis_color)
        ax.spines['left'].set_color(self.axis_color)
        ax.spines['right'].set_color(self.axis_color)
        ax.tick_params(axis='x', colors=self.tick_color)
        ax.tick_params(axis='y', colors=self.tick_color)

        # Set labels and title
        ax.set_title(self.title, fontsize=self.title_font_size, color=self.title_font_color)
        ax.set_xlabel(self.xlabel, fontsize=self.xlabel_font_size, color=self.label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.ylabel_font_size, color=self.label_color)

        # Rotate x-axis labels
        plt.xticks(rotation=self.x_rotation)

        # Add legend if enabled and plot_type is line
        if self.legend and self.plot_type == 'line':
            ax.legend()

        # Add the MarketQuant logo
        self.add_logo(ax)

        # Adjust layout and display
        plt.tight_layout()
        plt.show()

    def confirm_valid_data(self) -> bool:
        """
        Confirms that the data is in the correct format for plotting.

        :return: True if data is valid, False otherwise.
        """
        return self.validate_data()
