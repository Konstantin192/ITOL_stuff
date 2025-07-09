USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[pitstops]    Script Date: 03/07/2025 19:13:58 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[pitstops](
	[season] [smallint] NOT NULL,
	[round] [tinyint] NOT NULL,
	[circuitId] [varchar](50) NOT NULL,
	[driverId] [varchar](50) NOT NULL,
	[stop] [tinyint] NOT NULL,
	[lap] [tinyint] NOT NULL,
	[duration] [varchar](50) NOT NULL
) ON [PRIMARY]
GO


