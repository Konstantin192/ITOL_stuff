USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[results_qualy]    Script Date: 03/07/2025 19:14:43 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[results_qualy](
	[Season] [smallint] NOT NULL,
	[Round] [tinyint] NOT NULL,
	[CircuitID] [varchar](50) NOT NULL,
	[DriverID] [varchar](50) NOT NULL,
	[Code] [varchar](50) NULL,
	[PermanentNumber] [tinyint] NOT NULL,
	[GivenName] [varchar](50) NOT NULL,
	[FamilyName] [varchar](50) NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[driver_nationality] [varchar](50) NOT NULL,
	[ConstructorID] [varchar](50) NOT NULL,
	[ConstructorName] [varchar](50) NOT NULL,
	[constructor_nationality] [varchar](50) NOT NULL,
	[Q1] [varchar](50) NOT NULL,
	[Q2] [varchar](50) NOT NULL,
	[Q3] [varchar](50) NOT NULL,
	[avg_Q1_time] [varchar](50) NULL,
	[avg_Q2_time] [varchar](50) NULL,
	[avg_Q3_time] [varchar](50) NULL,
	[driver_avg_position] [numeric](3, 1) NULL,
	[driver_total_races] [float] NULL,
	[avg_constructor_position] [numeric](3, 1) NOT NULL,
	[was_first_last_1] [tinyint] NOT NULL,
	[was_first_last_2] [tinyint] NOT NULL,
	[was_first_last_3] [tinyint] NOT NULL,
	[was_first_last_4] [bit] NOT NULL,
	[was_first_last_5] [bit] NOT NULL,
	[was_top3_last_1] [tinyint] NOT NULL,
	[was_top3_last_2] [bit] NOT NULL,
	[was_top3_last_3] [bit] NOT NULL,
	[was_top3_last_4] [bit] NOT NULL,
	[was_top3_last_5] [bit] NOT NULL,
	[was_top5_last_1] [bit] NOT NULL,
	[was_top5_last_2] [bit] NOT NULL,
	[was_top5_last_3] [bit] NOT NULL,
	[was_top5_last_4] [bit] NOT NULL,
	[was_top5_last_5] [bit] NOT NULL,
	[was_top8_last_1] [bit] NOT NULL,
	[was_top8_last_2] [bit] NOT NULL,
	[was_top8_last_3] [bit] NOT NULL,
	[was_top8_last_4] [bit] NOT NULL,
	[was_top8_last_5] [bit] NOT NULL,
	[was_top10_last_1] [bit] NOT NULL,
	[was_top10_last_2] [bit] NOT NULL,
	[was_top10_last_3] [bit] NOT NULL,
	[was_top10_last_4] [bit] NOT NULL,
	[was_top10_last_5] [bit] NOT NULL,
	[was_top15_last_1] [bit] NOT NULL,
	[was_top15_last_2] [bit] NOT NULL,
	[was_top15_last_3] [bit] NOT NULL,
	[was_top15_last_4] [bit] NOT NULL,
	[was_top15_last_5] [bit] NOT NULL,
	[Position] [tinyint] NOT NULL
) ON [PRIMARY]
GO


