USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[driver_standings]    Script Date: 03/07/2025 19:13:30 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[driver_standings](
	[season] [smallint] NOT NULL,
	[round] [tinyint] NOT NULL,
	[position] [tinyint] NOT NULL,
	[points] [numeric](4, 1) NOT NULL,
	[wins] [smallint] NOT NULL,
	[driverId] [varchar](50) NOT NULL
) ON [PRIMARY]
GO


