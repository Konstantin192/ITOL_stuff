USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[results_history]    Script Date: 03/07/2025 19:14:29 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[results_history](
	[Season] [smallint] NOT NULL,
	[Round] [tinyint] NOT NULL,
	[CircuitID] [varchar](50) NOT NULL,
	[country] [varchar](50) NOT NULL,
	[ConstructorName] [varchar](50) NOT NULL,
	[constructorId] [varchar](50) NOT NULL,
	[ConstructorNationality] [varchar](50) NOT NULL,
	[DriverID] [varchar](50) NOT NULL,
	[DriverName] [varchar](50) NOT NULL,
	[DriverNationality] [varchar](50) NOT NULL,
	[Nationality] [varchar](50) NOT NULL,
	[Position] [tinyint] NOT NULL,
	[Points] [numeric](5, 3) NOT NULL,
	[Grid] [tinyint] NOT NULL,
	[Status] [varchar](50) NOT NULL,
	[AverageSpeed] [numeric](6, 3) NOT NULL,
	[DifferenceGridPosition] [smallint] NOT NULL,
	[WonLastRace] [bit] NOT NULL,
	[WonLast2Races] [bit] NOT NULL,
	[WonLast3Races] [bit] NOT NULL,
	[WonLast4Races] [bit] NOT NULL,
	[WonLast5Races] [bit] NOT NULL,
	[WonLast6Races] [tinyint] NOT NULL,
	[WonLast7Races] [tinyint] NOT NULL,
	[WonLast10Races] [tinyint] NOT NULL,
	[Top3Last5Races] [bit] NOT NULL,
	[Top5Last10Races] [tinyint] NOT NULL
) ON [PRIMARY]
GO


