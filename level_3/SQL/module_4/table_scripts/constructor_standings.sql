USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[constructor_standings]    Script Date: 03/07/2025 17:16:10 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[constructor_standings](
	[season] [smallint] NOT NULL,
	[round] [tinyint] NOT NULL,
	[position] [tinyint] NOT NULL,
	[points] [numeric](4, 1) NOT NULL,
	[wins] [tinyint] NOT NULL,
	[constructorId] [varchar](50) NOT NULL
) ON [PRIMARY]
GO


