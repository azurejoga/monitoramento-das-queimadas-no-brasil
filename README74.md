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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8f8112e-ac5a-3dcc-9ea7-dbcf3d613be9 | -16.05874 | -49.96742 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1f5348a-d9f3-3413-85d1-0cf067e8adf4 | -12.0131 | -50.99358 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8f127586-6d5b-37cc-bee6-e73f9b2d21d2 | -15.47649 | -49.36832 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 751842a8-0c97-397f-82c8-31e69f7e3977 | -15.52506 | -48.38008 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e42d6d8b-f049-34e3-aad3-507e679c500b | -14.59886 | -43.93238 | 2025-09-10 04:44:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc837bf4-13ce-31fa-afec-67ba1676c30d | -20.16011 | -43.66019 | 2025-09-10 04:44:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99546188-e25f-34d9-9053-55e35f745781 | -12.96345 | -54.75765 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74bee55d-1d1f-3351-9224-9be1bbe4344e | -13.00515 | -45.21029 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff9d3c70-9a11-3764-8f29-6e7852a2fd3e | -17.15959 | -50.152 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c04f4ac-4453-39dc-87cc-c19f9921e21b | -13.75702 | -47.17101 | 2025-09-10 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03798e60-6741-367f-b8ce-44677a2eed36 | -16.46492 | -50.66772 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a79530d7-a075-338d-9fbb-a5cea67c0069 | -14.60639 | -52.10061 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a64d8fbd-5c7e-33cf-9251-dbf13c62d4ff | -14.56326 | -48.762 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b6e3481-6de0-3772-93af-a3bb5181199a | -17.90427 | -43.40521 | 2025-09-10 04:44:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0418dd98-31c7-38b1-9ac1-b6da4e50f594 | -13.64609 | -46.97494 | 2025-09-10 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c77c69bc-5dd7-321d-9ee2-e0322610382c | -15.1667 | -47.95599 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa9b6590-d1d9-3278-ad6d-516589714296 | -15.27981 | -53.78105 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8c00834-954c-3c80-9e80-8e9afa43d8fc | -13.97828 | -48.23671 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8203813a-828d-300a-a55f-5f6be2a6a585 | -14.92904 | -55.93453 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78c2db57-6c6b-3dcb-b8d0-0eb023517d3a | -12.90573 | -47.98449 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbd3921a-3807-3d66-b430-764a0ccc9df7 | -15.10784 | -50.08257 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8909145e-b0f1-3ace-b381-fde14022afe7 | -14.43931 | -52.95308 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56c73c2f-5d2d-34b3-a470-526e3d0d1f5a | -15.83387 | -48.97049 | 2025-09-10 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cb60499-8639-3edd-9d88-b3864b24b689 | -12.99146 | -48.03692 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c5305a4-0416-370d-8b0d-90734f104d3c | -13.1231 | -54.92994 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f454382-930b-3069-b384-70dce96db972 | -14.5991 | -52.10311 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebd98414-9948-3143-abef-db001df97c9c | -15.83032 | -48.97013 | 2025-09-10 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5374eab6-8f3c-3595-b3db-476734a8f2cf | -12.00479 | -50.98133 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7cdcc166-a6b7-36d1-bbc8-4b7c2be5cf50 | -14.39182 | -43.65157 | 2025-09-10 04:44:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 420e63bf-bfe8-3fde-beef-df64e908e66b | -13.50955 | -50.80856 | 2025-09-10 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b859b1ff-e61d-30c5-b231-9d8cc861cdbf | -16.14852 | -47.8917 | 2025-09-10 04:44:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e31cfb1c-c2c6-37a4-985c-32def9101740 | -12.85059 | -52.94587 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e4ffbc-80b4-328b-8732-123c95749554 | -16.48807 | -51.97285 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ab5de3-3b5b-3d62-9b94-ada1c6f6ada4 | -15.84085 | -52.26802 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afabe6e6-28ad-38fb-a332-cfffd9c93ce5 | -16.34151 | -52.9474 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c266378c-6ba6-3ede-bad0-4949f6f58b19 | -12.54903 | -45.28732 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15af1e4e-a7c7-3533-a02a-156e702bf75e | -14.92786 | -55.91859 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afd45b24-3c97-33e8-8d77-85b806b5ac76 | -14.89891 | -55.85626 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b8608e0-090b-3712-8ce1-6284bf29949d | -15.11401 | -52.35386 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45ea32f4-4251-32e8-b284-2f1dd155bf87 | -13.7921 | -46.29446 | 2025-09-10 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 12365f79-c53a-341d-90e6-552cfc7d90d8 | -15.95965 | -50.23146 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95765bb7-d4e5-300c-8db1-94da96950dcb | -18.36986 | -49.27025 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad04eef7-e489-304b-baf3-2e3fa288ff19 | -19.29782 | -47.98963 | 2025-09-10 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d69c461-820e-3b06-999b-3260dfbe825d | -11.94071 | -51.08335 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6afdf7dd-724f-302a-819d-db9d5cccc96f | -16.57327 | -49.73894 | 2025-09-10 04:44:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 901caedb-e638-3a45-91da-6737713d47a2 | -19.48904 | -45.30536 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 186910af-289c-3b7e-8ab2-d80622fe668c | -19.64395 | -45.03974 | 2025-09-10 04:44:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73f21cb0-5a45-3777-91b6-697001ae612e | -14.55386 | -48.75248 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d099c4f2-05ff-38e2-a1c4-a77fa3dee612 | -18.00882 | -47.12784 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fad5a38-e55c-3036-ab7b-424e8155e7c1 | -13.94673 | -48.26313 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e192b966-0300-3ada-994f-508533f8bddb | -14.32946 | -47.3075 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 002f804b-1c4c-3e88-b2ab-2c86aff5d2a4 | -14.53403 | -42.48181 | 2025-09-10 04:44:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e32ef4e2-107e-343c-92ed-51c66929f2f5 | -11.20957 | -54.99372 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c4629ce-91d6-3f00-927d-350eecc359ec | -16.68818 | -48.52945 | 2025-09-10 04:44:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd7def3d-4034-3ab4-af28-3a7c08a494ba | -18.71157 | -52.59747 | 2025-09-10 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3917e453-e3ba-3343-a15a-4a8af3ec1446 | -14.89113 | -55.85495 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 637cfacc-a455-3172-aed4-c2c646da369b | -14.3589 | -47.31701 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11cb5fe5-bf64-3fb0-be7d-4d7601b44554 | -14.92101 | -50.11788 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f85f463-541c-3106-9bec-247a7fccc823 | -14.30787 | -44.8752 | 2025-09-10 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f0244b3-774d-332b-80c1-5a7aca430f14 | -15.47292 | -53.04416 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c36030a1-ea3e-34ce-b184-716cc084d27e | -15.14227 | -52.39226 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d152629-bcaf-39e6-9331-8c48ce65d024 | -14.88543 | -55.86432 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6e02bd0-0ccb-30d2-9ca4-6676452a7460 | -19.51638 | -45.02007 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e42ec26-ab36-3908-bbf5-09440374759c | -12.9605 | -54.75239 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50461616-6fd3-3341-867f-885b3320c310 | -13.19327 | -45.27864 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b567d6a-9c22-34c2-bc9c-bd611f51e0d5 | -15.90016 | -50.18802 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3795a79-361c-3f81-a2f4-2854a45b5515 | -15.77552 | -53.64458 | 2025-09-10 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bcd4281-1358-37f2-b400-ab57e0114b01 | -14.44273 | -52.95367 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be4df013-ce89-39c0-9f77-1b997111c724 | -14.89981 | -55.85126 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| accfcf82-0548-38ff-baf6-72fa965d0262 | -19.63928 | -45.03905 | 2025-09-10 04:44:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 615f5cd8-d442-3aa0-a5c4-d72c58ba0034 | -19.85089 | -48.10452 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24e8d66b-7593-36fe-80fa-7b63011958fb | -13.92942 | -48.25666 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 638b001a-9696-393b-a047-4aa6fb9120fe | -19.81248 | -47.7903 | 2025-09-10 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 569eebd0-1e7c-31c1-8b67-e408d3530e84 | -11.21262 | -54.99932 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeb01c33-acb5-3845-9d02-fd8b1f3369b2 | -13.12687 | -54.9306 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b06ed0d0-2691-3047-bbc8-95cf7869b311 | -14.5569 | -52.21503 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a39252f6-6c41-3be2-aabd-b23391d4fff8 | -13.02189 | -48.03932 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76890406-4875-3af1-bd7c-2943601513f4 | -18.35543 | -49.3462 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92fdd63d-f42d-3838-a8a6-25f539864f82 | -17.55773 | -44.53559 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cafc3207-2a67-3af2-ae62-aa65f30bd8a2 | -15.22044 | -44.04187 | 2025-09-10 04:44:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0785a88f-aabd-36c3-8713-6f9ae1006870 | -16.58088 | -49.21857 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 293c4f7c-33cd-369e-8fa3-23055a8012ed | -14.78107 | -48.23063 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55f315d5-7643-3c74-aebc-7841cbd5e04e | -17.30707 | -46.7545 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c198c6-d3ca-3a9c-994e-20629d6ac211 | -16.54342 | -55.15157 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c6cbf904-bf8f-3d5f-8fbb-89112dc19c0a | -12.04268 | -51.03817 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79ed9edf-3f0e-33fa-9da9-4da5e58d57f1 | -12.93676 | -54.80016 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b0034a5-da58-385a-902b-d83edd285439 | -13.29785 | -51.72013 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c8a6efe9-fa68-309b-9c73-fd3a389b0329 | -17.74294 | -44.48969 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4519117-13d0-3a3d-be03-cc3af10d2305 | -15.02249 | -49.2562 | 2025-09-10 04:44:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d5329c3-0598-359b-9155-c8c418baa71c | -14.43869 | -52.95687 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6775fa8b-320a-3298-8065-909cffc286b7 | -15.13381 | -52.40191 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0e8a8b88-0358-3855-9f98-ea260bda6d30 | -15.60405 | -52.75326 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63f92470-a696-3652-b044-95e7458b7ba7 | -16.44914 | -51.98106 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 590c8cd1-f2ac-3426-8e59-252e7885ede0 | -15.02057 | -50.0842 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cb4db1d8-9b20-38a9-a29b-f002b62d2bca | -13.02542 | -48.01494 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a96588-fb4c-3dfd-b54f-7b6718dbcd24 | -15.9399 | -50.22438 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c72aa1dd-ee08-3fde-840c-fa1e9b915064 | -12.99505 | -48.03733 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7c3b97d-fd44-3876-bedb-add5ce393d07 | -14.37848 | -47.31456 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69e1d948-3378-3dc5-bcb7-cd497b82eae0 | -12.00812 | -50.98188 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d639a57c-71b0-3e93-bc60-8ea0566b7914 | -18.95811 | -42.3921 | 2025-09-10 04:44:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README75.md)
