USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[results]    Script Date: 03/07/2025 19:14:15 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[results](
	[Season] [smallint] NOT NULL,
	[Round] [tinyint] NOT NULL,
	[CircuitID] [varchar](50) NOT NULL,
	[Position] [tinyint] NOT NULL,
	[Points] [numeric](5, 3) NOT NULL,
	[DriverID] [varchar](50) NOT NULL,
	[Code] [varchar](50) NULL,
	[PermanentNumber] [tinyint] NOT NULL,
	[GivenName] [varchar](50) NOT NULL,
	[FamilyName] [varchar](50) NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[Nationality] [varchar](50) NOT NULL,
	[ConstructorName] [varchar](50) NOT NULL,
	[ConstructorNationality] [varchar](50) NOT NULL,
	[Grid] [tinyint] NOT NULL,
	[Laps] [tinyint] NOT NULL,
	[Status] [varchar](50) NOT NULL,
	[Time] [varchar](50) NOT NULL,
	[FastestLapTime] [varchar](50) NOT NULL,
	[FastestLap] [tinyint] NOT NULL,
	[AverageSpeed] [numeric](6, 3) NOT NULL
) ON [PRIMARY]
GO


