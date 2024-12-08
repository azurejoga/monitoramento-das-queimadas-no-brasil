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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89877338-c670-324b-b0f0-c700f926a447 | -13.11408 | -43.3767 | 2024-12-08 04:16:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b9187f9-b17e-3004-a7ac-954c448ee13a | -12.00158 | -52.50469 | 2024-12-08 04:16:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce866ee-fb24-3840-a6d0-1b768b769986 | -17.75852 | -46.99757 | 2024-12-08 04:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 746bb6d7-9418-309b-a886-423ca72295a1 | -18.95981 | -53.69407 | 2024-12-08 04:16:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a7101025-a792-37b3-8171-96f09cad2b65 | -11.20463 | -53.81921 | 2024-12-08 04:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce072778-ad80-355a-921f-4434a37fdad9 | -12.9521 | -45.01186 | 2024-12-08 04:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28532bbc-5fa7-3673-9362-eeba3b455ed9 | -15.95305 | -43.40292 | 2024-12-08 04:16:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b127beca-26a9-3cfa-826b-ba439a73bc1a | -11.72398 | -57.44191 | 2024-12-08 04:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eddf5344-7831-3f90-98d6-ce3d7c8841c2 | -15.25654 | -53.57744 | 2024-12-08 04:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95a19fff-9e15-384b-b44b-2df6a345969e | -17.46405 | -47.86722 | 2024-12-08 04:16:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b856450c-8f55-320c-a6d7-64f0dc984908 | -15.36146 | -53.12164 | 2024-12-08 04:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86d607c4-d21c-3fea-aa7b-2fdfb558d6ff | -20.20464 | -41.78971 | 2024-12-08 04:16:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20758ae7-6f0d-3678-9bc5-aeb918ffc954 | -17.12924 | -42.41119 | 2024-12-08 04:16:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1e76f73-3a89-340b-b237-64bff9d76c84 | -12.85865 | -51.93036 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28321503-7ca4-33f7-bf13-f90d588b8d83 | -19.71677 | -40.35446 | 2024-12-08 04:16:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f1d977a-4657-3125-b994-c3ea3a13ea64 | -12.86021 | -51.93941 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22ba0b60-20c0-38bc-a8f9-c7f1ee6caac9 | -12.854 | -51.92942 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cfd59cc-08f2-3d4b-a5eb-306aee395f7c | -12.32073 | -48.00707 | 2024-12-08 04:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db073172-6e89-3bb0-a3b8-b67cd0abcae9 | -13.62477 | -44.51835 | 2024-12-08 04:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db686ce6-1f41-361a-954d-65517a7f6f37 | -15.97571 | -57.17187 | 2024-12-08 04:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b90db96-23ce-31d7-8086-38d9d8ffb459 | -13.88425 | -47.38836 | 2024-12-08 04:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acc2872a-a059-304e-a08e-32cee62efb1a | -23.59499 | -47.44011 | 2024-12-08 04:18:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd5cf3fe-e3d0-3efe-96ef-27eb651511a9 | -18.94598 | -54.92421 | 2024-12-08 04:18:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1ba9423-98c3-3a52-98b4-b224b7247e9a | -18.94534 | -54.92736 | 2024-12-08 04:18:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8127daf-8d4b-36ac-9e65-977437892923 | -20.87972 | -43.85226 | 2024-12-08 04:18:00 | NPP-375D | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc826356-e337-33c4-8d76-fb49b5180aa4 | -30.15101 | -52.02585 | 2024-12-08 04:21:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 25e1ca7a-4703-3c46-98b8-dc60dc70e04f | -1.64837 | -45.90314 | 2024-12-08 04:33:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7598ceec-50c1-3bbe-9d34-8ce2287d7415 | 2.00184 | -61.14997 | 2024-12-08 04:33:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 386e8d9b-2a85-33e4-9760-03353b7d4d00 | -1.64777 | -45.90696 | 2024-12-08 04:33:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5656fe50-9bb5-30a3-9421-5ea95a066702 | -1.64718 | -45.91078 | 2024-12-08 04:33:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 172465f5-613d-30d7-92af-f0b9dd7d9a68 | 1.99466 | -61.15073 | 2024-12-08 04:33:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e9fa859-3cec-3751-b406-843da28f34f8 | -1.47891 | -46.13648 | 2024-12-08 04:33:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13471f5e-54ce-3682-bfba-8a4149455f28 | -1.77751 | -46.49098 | 2024-12-08 04:33:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc60e5e3-9f96-3003-8890-7fd1e1754261 | -5.92463 | -48.028 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a361c4f-6dcb-39d7-8ded-a91ce9226e05 | -6.98688 | -47.08859 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6186faa6-d849-3816-bd84-4c58c683d941 | -7.80297 | -46.22812 | 2024-12-08 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51fa3489-b36b-3911-be6d-34ea132a4f48 | -4.5696 | -48.02834 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9e257f4-f8b3-31c6-8e20-f4eafdb313f8 | -5.47597 | -39.41944 | 2024-12-08 04:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c290ce6-6e74-3dc8-8450-83c9eca5b5a0 | -6.90549 | -46.21061 | 2024-12-08 04:36:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5e3e629-104a-333d-9574-f136f01def55 | -6.05031 | -44.05002 | 2024-12-08 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6309e5eb-1f58-3784-af54-1d2174647e5c | -1.70383 | -52.60606 | 2024-12-08 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8de85213-9d0a-3cea-97ba-da10a4b17abc | -6.95282 | -47.79169 | 2024-12-08 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ef1984-23da-3ed2-80a5-2cd2f55324e2 | -4.56681 | -48.02433 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b192b16-7dfd-3965-bfad-60634a9f5464 | -5.19849 | -47.74244 | 2024-12-08 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ccd1b86-0c38-3f66-8616-1e2e960f52ad | -2.79376 | -52.87139 | 2024-12-08 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d53643be-cfe3-35ce-803e-ef6bc9226978 | -4.58454 | -48.01994 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 263e3319-6bf2-30f3-b773-0c3161adef64 | -5.90734 | -48.02891 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3f9e59b-0a69-3989-b41f-d79c25053262 | -6.05137 | -44.04278 | 2024-12-08 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b1aa723-0a22-3537-b789-636f1d9cc1f1 | -4.07383 | -46.70755 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a6235ce-6a91-3c62-8014-0aea3fc6387e | -6.98341 | -47.08805 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea1a6b3c-5d01-3ce6-bc80-d0932f338cfc | -4.56627 | -48.02782 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28a0be7c-8358-3a1e-980e-4b587b89d7aa | -5.13447 | -48.58612 | 2024-12-08 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84d02fb3-db47-32bb-8cab-f892acbac2ac | -6.20545 | -46.06667 | 2024-12-08 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e56f00a-20a4-3578-af83-fe72709587a4 | -6.68625 | -47.66167 | 2024-12-08 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c400800-f3b7-3cfb-93d9-9d2eab82bec8 | -6.28684 | -43.85195 | 2024-12-08 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ee4208f-f0f7-3463-a78d-ebc0a29bca5c | -5.13116 | -48.58561 | 2024-12-08 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5ea1405-a664-31ec-a8b6-4ccfc9755f95 | -5.57987 | -45.21553 | 2024-12-08 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14dc87f6-197c-3f3b-a1b1-7823ad495165 | -6.65723 | -47.52924 | 2024-12-08 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1ec9a66-b7c1-346a-a956-d2d277a072ee | -7.52605 | -47.29631 | 2024-12-08 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95250f99-5087-3fa8-a96a-7b4893945d2e | -5.50157 | -46.24926 | 2024-12-08 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 430f7dcf-e53f-30f9-81ac-c56e8422fb44 | -4.04917 | -46.70765 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f0a12db-8491-3ad3-a45b-9402a9b447b2 | -4.08012 | -46.71237 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 857f1a83-16ec-3c79-b7ec-f23ffca5f88a | -1.53952 | -52.68232 | 2024-12-08 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35a6f4a3-cf3e-33cc-9c81-d86e877921c6 | -5.24756 | -37.50502 | 2024-12-08 04:36:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5fecb05e-101f-3e64-a045-3e7fcca74357 | -7.99094 | -45.79533 | 2024-12-08 04:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6885b893-bc15-3cf5-af52-a77f05ad194a | -6.05552 | -52.33924 | 2024-12-08 04:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b605bf2c-5440-3754-a0d4-f1cb9aad1409 | -4.0761 | -46.71555 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5daa9817-b9b5-3848-bda3-532d2dc8f4bd | -5.58055 | -45.21099 | 2024-12-08 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9603caf8-3de8-3054-a8d8-2174eae3cb09 | -3.85878 | -40.44832 | 2024-12-08 04:36:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5038db8-a830-3081-877a-e3877ab943f8 | -5.90678 | -48.03246 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d582dd66-ee76-340b-a659-89d827c466c1 | -4.07039 | -46.707 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5871efe2-6b30-3459-9146-a076d177ac44 | -5.52583 | -46.96436 | 2024-12-08 04:36:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50e5ff8a-9824-3fdd-ab98-e77e23baa622 | -7.80233 | -46.23237 | 2024-12-08 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea1b812b-701e-36af-91b7-a0df8796008b | -6.68761 | -47.40092 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5238edf6-311e-3898-b819-f3bc602c4c3b | -3.22232 | -45.64526 | 2024-12-08 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef99cf58-611b-37e7-a39e-c722c5b92334 | -6.87245 | -47.24402 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7168a65e-d087-3879-b8b7-fc79b10cc530 | -1.5403 | -52.67745 | 2024-12-08 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aca167ba-2697-353c-8f26-cd80f4ce894b | -3.92004 | -46.72622 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e534e828-efd0-35e2-be4b-59d1572acc90 | -5.91013 | -48.03299 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44f29d36-0f7b-32c0-873b-817409a09a9d | -5.49485 | -46.77295 | 2024-12-08 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a665231-a2ae-34db-8c71-5d7c4992d29e | -5.50152 | -47.16737 | 2024-12-08 04:36:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6db701fd-a7ed-38cf-897c-3275421270b7 | -5.92128 | -48.02748 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 473fbbb0-810a-3371-a3ac-97187359b310 | -5.58124 | -45.20645 | 2024-12-08 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab08e131-3034-3684-ab15-2d34628d668b | -6.95388 | -46.35398 | 2024-12-08 04:36:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9280f456-3daa-36e8-a204-501fd75da3f0 | -1.43264 | -52.59774 | 2024-12-08 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0814a1fc-8660-3c6c-b536-9e7a7fdd6b01 | -6.46318 | -47.54149 | 2024-12-08 04:36:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c476050-ed35-3c97-853c-497b15a3eca5 | -6.55546 | -44.2047 | 2024-12-08 04:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74e64867-e60c-3714-8527-891aa3de28c6 | -5.14092 | -47.50269 | 2024-12-08 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80c73fc8-354c-3b55-8d54-840c058a379b | -4.07726 | -46.7081 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6e3c7d8-4ef2-34c3-8d84-d36b95c36337 | -6.68476 | -47.39667 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc58c48f-be91-32a6-922b-1a6aa73e7a52 | -4.04724 | -46.81036 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb7aa600-e4be-3998-bdda-c102d0031c24 | -7.79582 | -46.20089 | 2024-12-08 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d095bcd8-447c-398b-8d48-081a3e8220f2 | -5.52297 | -46.96003 | 2024-12-08 04:36:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d38b2273-af99-37ab-b7be-993b60ddadd8 | -3.73338 | -49.9305 | 2024-12-08 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a17846-d711-3e9b-9ca3-210abc5a7411 | -4.03982 | -46.81298 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fad23401-6f1d-3f0d-a247-3b7497acc051 | -3.66192 | -49.95543 | 2024-12-08 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84dc06dc-d887-38dc-a417-3e09b4e30282 | -4.07668 | -46.71182 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54e0e533-2615-3b7a-885b-261877359c0f | -5.4765 | -39.41577 | 2024-12-08 04:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0eb64ed4-0a80-32c1-a64c-06218eadce71 | -6.76928 | -44.85148 | 2024-12-08 04:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5255c4c4-6c6a-3606-99e6-50a5c2d31dcb | -5.42804 | -44.70909 | 2024-12-08 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README9.md)
