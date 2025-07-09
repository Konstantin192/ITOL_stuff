USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[constructors]    Script Date: 03/07/2025 19:13:07 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[constructors](
	[year] [smallint] NOT NULL,
	[constructorId] [varchar](50) NOT NULL,
	[url] [varchar](255) NOT NULL,
	[Name] [varchar](50) NOT NULL,
	[Nationality] [varchar](50) NOT NULL
) ON [PRIMARY]
GO


