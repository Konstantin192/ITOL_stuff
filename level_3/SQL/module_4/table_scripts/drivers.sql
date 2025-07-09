USE [ITOL_SQL]
GO

/****** Object:  Table [dbo].[drivers]    Script Date: 03/07/2025 19:13:45 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[drivers](
	[driverId] [varchar](50) NOT NULL,
	[url] [varchar](255) NOT NULL,
	[GivenName] [varchar](50) NOT NULL,
	[FamilyName] [varchar](50) NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[Nationality] [varchar](50) NOT NULL,
 CONSTRAINT [PK_drivers] PRIMARY KEY CLUSTERED 
(
	[driverId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


