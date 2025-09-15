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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44501198-7e52-3738-bfbc-ae707ee0b0d6 | -13.75374 | -48.77618 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75dc9118-b68b-3cdb-b43f-9db449c3ba7a | -13.76033 | -48.76938 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 367947a7-3be5-3646-a97f-df8da57ab020 | -15.77895 | -53.47141 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| adaf1ac5-42f6-35e2-ad94-a3fe99e05983 | -18.16306 | -49.20322 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e4c7ca23-e19d-3d15-b934-fbdff355626f | -15.78419 | -53.46442 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c8ef5e23-3b9a-32e2-b9af-ba19e1d23ec8 | -13.75566 | -48.77728 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 777b4c66-cc7f-3a72-a1f0-5fc0b7182a1c | -14.45803 | -55.96227 | 2025-09-15 05:12:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8076373e-9027-37dc-8539-ee3777841f22 | -15.85937 | -59.402 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 218f1313-a605-3cea-bf3c-4396e3c30017 | -15.89536 | -49.98691 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 662f55b0-4ace-3afe-bb86-9edb23808cdd | -12.43701 | -63.89322 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 839331c6-00ad-3333-aaf6-89a66599c821 | -12.04586 | -63.11868 | 2025-09-15 05:12:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fb3cac5-a2d5-37e2-9d76-130a7257d97c | -13.88482 | -48.31074 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a7fa751-bcc2-32d2-b42d-8c45a86eb2cb | -13.87471 | -48.13597 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f18e7d6-d764-3806-addd-fc918cabf50d | -15.10927 | -52.48481 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18a12ab6-d3ab-37cc-b86c-b6593705c3e6 | -15.69473 | -54.34301 | 2025-09-15 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 498f9d91-6525-3c09-9d43-0bee6c4fba27 | -11.77631 | -64.9441 | 2025-09-15 05:12:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93385017-c00e-3a05-8b93-124e326dddc7 | -13.87427 | -48.13995 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 908cdc31-bb23-3b3c-9fb1-4c2c8f5c31a0 | -14.20137 | -48.77944 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87d4e286-2af9-3c75-a2f6-a91a8abdbab2 | -12.79514 | -47.94523 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2969094a-47aa-303e-8381-b535251eebd3 | -14.59497 | -46.59719 | 2025-09-15 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30b0cec4-0a35-3607-9c57-5ff06acddc5f | -15.79176 | -52.21536 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06d35b70-b893-397b-b064-e5410478c923 | -18.15837 | -49.20029 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 343e51f4-51ad-3348-96f8-cbf3d032e67f | -14.43873 | -53.36468 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d07724a-82cf-3fd3-9c55-3f6ee4164fc0 | -12.40825 | -63.88825 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 040346c8-811a-3e3f-a215-5258246e01a3 | -12.43427 | -63.88529 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b7f2a4-3c23-3ab9-8b18-401329a8792f | -14.81859 | -51.63679 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d0dd556c-3dcf-33ad-9156-1409f190953b | -14.92641 | -46.56951 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 488b09c5-8051-3ef9-a0a9-2722fabb1b17 | -14.80202 | -51.61314 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6889dc90-be24-3412-bf17-fd0c0647f63d | -13.76172 | -48.7747 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ab3d1b7-c864-308b-8dea-ea99f02a22e3 | -14.94222 | -46.59383 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13ae1afa-ee23-33ed-a130-bc538e6eb516 | -17.14124 | -48.52595 | 2025-09-15 05:12:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b67f46d-aca4-3bdb-a91e-d0327867413c | -14.93229 | -46.57724 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ef7243a-bed0-3bc3-ab2f-d05f4760ca35 | -15.10021 | -52.48368 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee7f9bd0-9b57-33e1-b78f-a2170cb79abe | -12.43025 | -63.88454 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a118073-f277-3b2b-abf5-7ef657c15704 | -14.81843 | -51.63462 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 11f4abca-f808-36ad-a0c6-6c0daeda0de7 | -17.14171 | -48.52139 | 2025-09-15 05:12:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 428d0d98-5039-33cc-9848-9f536ff59d27 | -13.00973 | -47.97387 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e70404c-083b-3f79-8aa2-d5d0a8888b3a | -13.74813 | -48.77482 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0c15af9-c032-3bd2-8ce8-54ab94c4214b | -16.01159 | -59.42677 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af93df81-1d0a-3b6a-bff3-f88eff4e3099 | -18.79023 | -48.54144 | 2025-09-15 05:12:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c1172e2-8ec3-3faf-82c3-13caa41431d3 | -12.40586 | -63.95084 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cf927aa-57cc-317c-b197-2d8aceae5421 | -15.04433 | -47.96781 | 2025-09-15 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58c00bdd-0c9b-3693-837d-3f00ea46f9ee | -15.76332 | -52.21601 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee1aac81-e38d-3d97-8310-668e2d4b9117 | -10.92417 | -61.96172 | 2025-09-15 05:12:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 91db6a70-139e-3d3c-99d6-e6ef0fdb06bb | -15.69572 | -54.33557 | 2025-09-15 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 377adaf2-ae4a-3915-a081-56e654d0a8a1 | -15.90366 | -49.9619 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ac90b711-b74f-3130-8733-db766515bcf9 | -14.47613 | -55.96496 | 2025-09-15 05:12:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 646e6c5f-90f9-350f-b6bd-4bf6c540f970 | -18.59603 | -47.20586 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4b466c4-4ef3-3515-8139-c8cd6cacfccc | -14.94445 | -46.58891 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ebf5194-ef80-3854-b9d3-489a01da2e78 | -16.66328 | -49.76461 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54df7aa7-3dc4-3a5b-8cf4-49f416c5e48d | -15.08214 | -52.48109 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e55b830c-379e-35f4-ba2c-ac2d1a500d49 | -12.78787 | -47.9768 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec6a99f2-954c-33e6-8ae2-f9e12d751d73 | -13.17992 | -47.29156 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc7e5e6b-5922-3f79-9af6-cf45d1953d8a | -15.79116 | -52.2201 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd15bbf5-9a01-3b39-8fe8-3244d0669deb | -15.85494 | -59.4086 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df387ed3-7b51-3676-8e50-db11af769d51 | -14.81382 | -51.63615 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4d029443-fde6-3291-af0b-ba2ac3246f58 | -15.77945 | -53.46748 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 327d491d-dc75-3e81-aafa-374d977f1c6a | -13.75982 | -48.7736 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b85bb297-2a58-3d66-bb06-e18d3f08f6f1 | -14.93846 | -46.58225 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7a95c74-938a-304b-bec9-3d6ee71f43d6 | -15.76795 | -52.21677 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f08791be-18b9-3545-a0ae-454a128cd837 | -15.8422 | -59.42479 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b20118ea-2351-338e-85be-5d5e63cbc5b6 | -18.58023 | -48.15138 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f168059d-5c4d-3a7a-9a25-63f8def0bd66 | -12.78922 | -47.9444 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a90a46f9-6162-3934-ae65-7078cda9ebe9 | -15.78716 | -52.21436 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ae6a6ef-961e-369b-8b5b-060af9508ed5 | -18.57963 | -48.15754 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe221bef-41f3-3f0b-9bd8-113a294696f6 | -18.15797 | -49.20407 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 91f23d52-a63a-3685-bba0-c1185f887c5a | -14.47251 | -55.96441 | 2025-09-15 05:12:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa6abbda-b2a1-35ca-8a56-e900ae31d5b9 | -11.70656 | -59.30998 | 2025-09-15 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd4c6ebf-7879-3d0a-a2cf-cb9150fc9009 | -16.49784 | -55.16318 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 453c70d6-d43b-30c7-a21e-fd80ca1d38f6 | -15.90033 | -49.99141 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3951f3f-4107-30aa-ad35-10cc72f23ba5 | -15.80207 | -52.19538 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a336ab0-a498-39cc-8fae-7d5038f800ec | -14.28086 | -46.12798 | 2025-09-15 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81d40596-fa87-3d30-a3d0-4f52dabc52b2 | -12.79463 | -47.9498 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fc4854f-4879-3b46-bd9c-538e4e859aa0 | -12.04973 | -63.11937 | 2025-09-15 05:12:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ddcd0f2-3871-3656-b01b-5fb8536a2683 | -14.82878 | -51.63278 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a28b86df-8f2c-32b7-b0cb-15d72df02931 | -15.89455 | -49.99412 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66f91db4-1aac-3fa3-8d47-18bb650f1ee6 | -14.9331 | -46.56952 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6033f8e4-9be3-3da5-8e2e-1c0f9dc8643a | -13.75608 | -48.77355 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cccce16-61dc-3cac-9b44-b7537cebe600 | -16.28347 | -45.6866 | 2025-09-15 05:12:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 507b85e1-b4c9-330b-91af-2cf9db66bb8f | -14.20405 | -48.76859 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54e77b3d-f10c-30bf-bf73-b37b778ab390 | -15.80563 | -53.46696 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84d0b68f-c5c9-3b37-9500-df23e0759c70 | -14.20184 | -48.77552 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1965daab-7b36-388c-96e8-e8f55767ad9c | -15.85606 | -59.40144 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f122110c-19d4-381a-8246-3b044fd26d8e | -14.63799 | -52.01832 | 2025-09-15 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05a08153-c91d-3334-9358-ef1c97344c04 | -17.16824 | -49.386 | 2025-09-15 05:12:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf8dca13-fe2e-3445-a7d6-039964e858f6 | -13.88156 | -48.12867 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1892496e-0c81-3afc-bebe-4161b34018ef | -14.83898 | -51.62877 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 292ea442-f14a-347c-9016-7248d25b59a5 | -13.19234 | -47.29303 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f71dbea2-abd3-3a20-a8c7-b28e105f670f | -16.67329 | -49.77568 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8750e78-51f3-3bdf-906f-fb40337b5166 | -15.79404 | -52.22306 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b68c2e6e-833b-3e25-bb84-cd270fddf829 | -13.7622 | -48.77047 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72cb0e61-7cfc-3fa3-8096-4594a3456f94 | -16.65197 | -49.76534 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b7bfa31-4325-3734-bf5f-ec626637523a | -13.86327 | -48.13059 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 715f721f-19e4-3faa-8a3e-0010548f46e6 | -14.93053 | -46.57669 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8aa0dce8-0fe0-34ec-85f6-0707d97beb5d | -14.46165 | -55.9628 | 2025-09-15 05:12:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8000a9e-946a-3e12-870d-7eb834f94cce | -14.59436 | -46.60294 | 2025-09-15 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e76abc10-cb3a-3dcb-a84c-afbaf4478a85 | -14.80139 | -51.61843 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 20b087a8-6e7c-33d0-a2a5-89dbd5b49b2f | -13.86923 | -48.13122 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 758e759e-d037-3ef2-b1ba-a1671eb2b550 | -13.19288 | -47.28839 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 745f1bec-c3d7-3a23-b787-1c378248d3a2 | -11.70989 | -59.31053 | 2025-09-15 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README63.md)
