# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9056e94c-1062-3b5d-9c26-d65765eb3b60 | -11.96182 | -51.47537 | 2025-10-04 05:33:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34499f40-5e7a-3072-a6dd-ea8445ec9450 | -9.31937 | -54.53244 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1a10068-47ba-39da-819d-3bb27721e16d | -9.52242 | -62.59435 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50026af3-3afb-3076-97c0-501437293f08 | -11.78696 | -62.03166 | 2025-10-04 05:33:00 | NPP-375D | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d13dde32-6356-34c5-a3cc-f3ecad1f5421 | -8.62631 | -54.98109 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a7766a6-350d-3c8f-acf0-8a09b520e6c9 | -9.31978 | -54.5294 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2521c25-9b8e-3329-8a6f-520d7da5995a | -9.33033 | -54.52766 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccaa95c0-e612-3a0b-9e8d-3d1c6caa9b6d | -8.62895 | -54.99757 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a78d592d-0986-3bc8-83fd-03cb7bd75fdd | -13.17329 | -50.88842 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5690c00-31f0-3598-8dbd-7bdb8fe75c0b | -10.88996 | -53.75796 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60dacae4-471b-3e1b-b880-a0990298674a | -15.00259 | -56.02252 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1eaeb73-cd9b-33cd-8d04-62070499ca12 | -12.39045 | -54.45827 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc6e8ae5-4966-3cda-8b46-669deb66f37c | -14.7471 | -54.64521 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbae5ea3-e592-3ef8-8371-8dbcbaca9d83 | -11.9936 | -61.02401 | 2025-10-04 05:33:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a82bcd-a1ad-3933-9bef-747b1478b00b | -10.06168 | -59.3555 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a1fbd2b-c380-3af9-a117-643eb0c537cd | -8.6623 | -62.86201 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f387b995-820c-3977-87a6-f07436675dea | -9.29175 | -62.44584 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdd3e3de-474b-3c53-b3a9-6ef77b8cadf7 | -9.34127 | -54.52309 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7fef8f9d-f4c5-3eda-b0c8-4f9c6d300884 | -12.93057 | -54.72587 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee537e7b-ad50-3c4d-b7f8-809d2911b8b3 | -12.21732 | -56.94223 | 2025-10-04 05:33:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1683e95e-d706-3d1f-8dbe-15ad71f7da3e | -14.57704 | -52.49281 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 914740dc-211c-3eab-aeb9-085a9501e369 | -9.33539 | -54.52838 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9448753-12c2-3dc0-a335-c6a51ce73da7 | -9.14546 | -62.36882 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed9f4643-5c00-355b-9871-67ad7b20a3c3 | -16.00846 | -50.93159 | 2025-10-04 05:33:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b197e14-980b-37f6-9b93-d9786d709ec5 | -9.32485 | -54.53003 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e3e25ad-f0e2-3779-9414-55736ec242b0 | -10.33213 | -50.32888 | 2025-10-04 05:36:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 69636f15-4d75-3d70-af65-0defb1f9e71d | -11.88087 | -44.97783 | 2025-10-04 05:36:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 275bb10a-d35f-3a01-994a-827dc286e02b | -12.53081 | -45.97496 | 2025-10-04 05:36:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 6b4270e1-0549-34c6-a8f5-8385dd28281a | -13.93558 | -48.1745 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bb9713f1-d13e-3481-af8c-82db85350be5 | -12.02989 | -45.1961 | 2025-10-04 05:36:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fd0c44c3-76ef-3b4c-a38a-d40c584ab290 | -13.12026 | -47.83553 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 55454dfb-b43b-3622-a015-e227374fc64f | -11.9243 | -46.37983 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 3aa599b6-c607-3434-89cb-3a7df702834e | -11.49344 | -46.73795 | 2025-10-04 05:36:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b62cc3fa-6b52-3aff-b832-c2a0475a9057 | -11.12847 | -47.16674 | 2025-10-04 05:36:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b0fd953c-1b49-356b-a280-dfad43b88979 | -12.81418 | -46.85556 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5412be1c-edfe-3f6c-b8a4-e413e57e197e | -13.47332 | -47.2603 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3f4de543-8310-3269-a9c1-42ea3cb8d2bb | -11.13296 | -47.17781 | 2025-10-04 05:36:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5af2c0c0-5797-31f7-b3f3-5898795e50c2 | -13.92641 | -48.15562 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e3a9a64f-37dc-304c-96ca-3a4c93199f9a | -11.69935 | -47.50158 | 2025-10-04 05:36:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7bc30e95-dcef-3dda-b0ba-1e24568c548c | -13.16858 | -50.9367 | 2025-10-04 05:36:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f1eb919b-8c26-36f4-963d-2479bd9c2d63 | -12.70434 | -48.56614 | 2025-10-04 05:36:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1c67f408-4b46-36cb-8f2c-9039cdec4cae | -13.51914 | -47.2676 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ba9fa543-68da-32f8-98e2-bf4f04036cc5 | -12.30828 | -45.38484 | 2025-10-04 05:36:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6af307fc-1a65-3053-b87d-8d7559c524b1 | -13.70286 | -47.34406 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c8dbed7b-4dae-32df-92b6-fb7e0936ce04 | -11.44558 | -43.50011 | 2025-10-04 05:36:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bac3f086-9bc4-34a2-ace0-1e20bc9625fe | -13.32482 | -47.2541 | 2025-10-04 05:36:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d334c455-02bc-342e-8663-44cc82e04237 | -11.24223 | -47.79187 | 2025-10-04 05:36:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 375c8e9d-f901-323a-bc58-c8bfe46783e5 | -11.17063 | -47.75166 | 2025-10-04 05:36:00 | AQUA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d7cdcf78-44f9-3857-83d1-c903597da844 | -13.9388 | -48.15644 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 01650b7c-4fa5-3734-973d-cbd2f0a24b70 | -13.50778 | -47.26516 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 046b0ce8-dd20-3666-9c11-ac54f2fd0191 | -13.29278 | -47.58625 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ce554356-d53d-3927-b74c-be40213e436c | -13.28985 | -47.60366 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2a312d36-bf81-3eb2-ab75-8b217de6f863 | -12.88879 | -47.16442 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d23d7fe4-e13f-37f6-b1b5-07903cc3bc9b | -13.13814 | -47.80355 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5ff4ac7b-1c0f-3f43-bae6-e1c5da500d5e | -13.12234 | -47.93033 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| e7493a6c-e504-34de-b0fe-330928ba5115 | -12.87472 | -44.62087 | 2025-10-04 05:36:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4e2da5e2-4215-32bf-8eae-8648c56593b9 | -12.88953 | -47.1536 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ab2d6282-0250-31fc-a133-6ec5199fbe8b | -11.49086 | -46.75372 | 2025-10-04 05:36:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 240affe2-87f2-3603-910c-1ab9bb073256 | -13.10828 | -47.83302 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 67f3e658-2e72-3380-9c54-a10a488ba8e8 | -11.92906 | -46.3519 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7aa8b35a-1950-32ca-b801-cb51c796f9a2 | -13.5154 | -47.27439 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bae53e89-5383-3284-bdef-8983d70b5d59 | -11.78896 | -46.83031 | 2025-10-04 05:36:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c6164fc7-5359-319b-8c87-612e90279c41 | -11.91762 | -46.4031 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 042599ec-95c7-3906-9594-e3d372fe4b66 | -12.64157 | -46.9786 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6509be44-c6e5-369d-8c77-d00f0df5f81c | -13.74374 | -48.04916 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 157d4a02-6c94-355f-adf1-5c67d3b7418c | -13.17189 | -50.91039 | 2025-10-04 05:36:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 4102375a-4ad4-389a-8a42-c527aacdd0e6 | -11.56586 | -47.67527 | 2025-10-04 05:36:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2c699e9f-f442-3635-8330-920388d3fa22 | -13.93339 | -48.16626 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1c556319-de17-3be7-ad33-e25e5b60dff2 | -11.55369 | -47.67263 | 2025-10-04 05:36:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| b0dd737c-0035-375b-8b96-f66b5d0e91e9 | -13.24056 | -47.82275 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1544f058-2ab9-3e61-9060-705defeea935 | -14.24722 | -46.09575 | 2025-10-04 05:36:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8fb1ebda-83b7-3cd3-9fe8-48963838c389 | -13.34653 | -48.06357 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 24c7f116-04e8-3ac3-9b07-5a9ab51f2de4 | -13.17413 | -50.90603 | 2025-10-04 05:36:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2484bd08-3517-328a-b96a-ee65e49c9ad9 | -13.12317 | -47.81861 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3f521cc8-2534-3416-a8f1-745e96289bb0 | -11.92185 | -46.39421 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| dc81fe8d-a8fc-346d-ac53-7cb5329c25ad | -11.12548 | -47.18391 | 2025-10-04 05:36:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| bb1227b3-dffd-36f9-97df-b3a27a80a21e | -13.88953 | -46.50632 | 2025-10-04 05:36:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8454c5da-6696-3da6-942c-b4082f792986 | -11.864 | -44.95611 | 2025-10-04 05:36:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a525daa9-3cec-310c-aa41-1687c98840eb | -10.83937 | -47.19876 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 27d6c92c-088e-3734-b536-4d3e87dab766 | -13.18714 | -50.91338 | 2025-10-04 05:36:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| f52a874d-cf20-3cd6-9689-099a05d2b4fa | -13.32464 | -48.11665 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cde621e5-c67f-378d-9b5e-57c2543ac06f | -11.927 | -46.34561 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82a48a2c-6504-3d9b-8fb5-6d0bf5dfff42 | -13.29209 | -47.8392 | 2025-10-04 05:36:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 15c2ef07-d93f-3c2e-ad74-beb984befe04 | -13.33436 | -48.06116 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a3dbd637-5a9e-38b1-92b6-bc7376246a99 | -13.75594 | -48.05069 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2ba1e1b8-f23d-3ed5-8806-9c16786c44d3 | -12.02793 | -45.20797 | 2025-10-04 05:36:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 04639ff6-c665-3d0b-bbef-57e04a7a9a95 | -13.29812 | -47.5938 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| d5eb04f4-57af-3694-9df2-eb444fdd01c9 | -12.69482 | -48.54487 | 2025-10-04 05:36:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| ed6a12ba-57ad-382c-880b-bb4391824682 | -12.03996 | -45.19773 | 2025-10-04 05:36:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ed477334-9b98-39ab-bf96-c8c458d4e3d9 | -11.92465 | -46.36001 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| b597f38d-0826-3098-8f21-a17799e2ec1b | -11.92667 | -46.36592 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 17898106-4f73-3175-a8a3-ad58271afaf6 | -13.3305 | -47.61695 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b043bc9c-ce3e-3a2c-95c7-8d11f54c43c3 | -12.91075 | -46.89428 | 2025-10-04 05:36:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4c36f20c-69fa-3755-9c7c-dae5734d674a | -13.99595 | -48.18808 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ee64e18b-e67a-338c-b397-3739df60c7f6 | -11.9157 | -46.36404 | 2025-10-04 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0babb277-4a10-33ef-9401-b758c76fc0c8 | -10.87278 | -46.64285 | 2025-10-04 05:36:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| a05214a3-c485-33ee-93aa-14782996112a | -13.74661 | -48.05645 | 2025-10-04 05:36:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ddd869f8-9a08-3313-a1e1-f82d387807c8 | -12.31026 | -45.37274 | 2025-10-04 05:36:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 22be8990-9f6f-3f9d-b818-3603a8a4e967 | -13.28631 | -47.59193 | 2025-10-04 05:36:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 548c440a-2473-3a70-bee2-28c38c4fc292 | -11.88887 | -44.99124 | 2025-10-04 05:36:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |


[Clique aqui para ver as próximas entradas](README132.md)
