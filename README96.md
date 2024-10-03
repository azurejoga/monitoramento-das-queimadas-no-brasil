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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b54d247-e9db-369b-b74a-1fdfb91cb382 | -8.27828 | -50.86892 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58e79c47-a291-3b7d-99ec-df179ac84cc7 | -8.183 | -50.48502 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b2d623d-5076-3ece-82f1-5fa1d796a312 | -8.18226 | -50.48951 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83efb09d-5a4c-35d0-ae5b-0d7100def509 | -8.17927 | -50.48441 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eec3e214-afd9-317c-836e-66f0378d2a8f | -8.17853 | -50.48891 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6e6263c-5e28-340a-8fac-4ecaadb0bdbc | -8.09164 | -51.12943 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebddf327-3781-38e5-b79d-fca5ef4dad2d | -8.08221 | -51.13823 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f548a8fc-f42c-39da-a583-988b5f5ee0db | -8.07833 | -51.13755 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4539980c-5583-33d2-b919-9f6e142ef7f8 | -8.0777 | -51.11749 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 383b85fb-081b-3641-921a-74d8de328df0 | -8.07751 | -51.1425 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 341809ed-95ce-31cc-ab36-cc09567dcf8b | -8.07667 | -51.14751 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eafafed1-68b6-3b4f-95cd-778ad828da19 | -8.07382 | -51.11689 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dba3c7c8-c7ec-38ac-8e66-39074266e295 | -8.0689 | -51.14626 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71baa83a-c4ce-30dd-91f9-732e039c6414 | -8.0681 | -51.15107 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 876eb957-759c-3cdf-af1d-d08d9f63977a | -8.06728 | -51.15596 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 47785ea9-66c4-3da4-a098-fb7f8f13edfd | -8.06642 | -51.16109 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89682651-70ac-3410-9fa4-75a2fe96f140 | -8.05953 | -51.15456 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72f3e661-87d8-3cb2-9a2b-ae29adf0f9a1 | -9.32668 | -51.13288 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50f2789e-5c4f-3964-8a54-6f656f4b8f3f | -9.2983 | -51.07217 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61009023-9077-3c41-abea-004e147d5a8a | -9.29607 | -51.06215 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 246e4c98-c41e-397f-9c1f-a14fbde45aa0 | -9.29228 | -51.06155 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24b2dd8b-35ad-3b1b-9dfd-a1cd06d98a46 | -9.29071 | -51.0709 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5968b753-4170-3dd0-a923-5b00c69744c1 | -9.11422 | -51.52176 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52a5243c-09c3-3131-b52c-c67cab448921 | -9.11031 | -51.52111 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d99e31c2-a689-3910-a9f4-34bd0f434b82 | -9.10948 | -51.52603 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a46d244d-7556-36f9-b872-5727e98e9f33 | -9.7458 | -50.65955 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ec5df46-aad0-35d4-b753-572b78516cb3 | -9.73325 | -50.6665 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f9aa6d9-37e2-3999-be2e-e5672333360e | -9.73249 | -50.67096 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9362052-ba4b-38a6-882e-f7ca0dac1c9f | -10.63404 | -51.11429 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ec07ed1-123e-3097-a606-43dcc4258363 | -10.63108 | -51.10912 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a3868d8-cc3f-3c20-9cf0-640cb2455555 | -10.54653 | -50.95393 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fabf3156-56bf-349f-a0b8-b50f7c0abcda | -10.54509 | -50.95269 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c43bf1d-d4b0-343c-b079-868b97eda457 | -10.53087 | -51.07985 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f5bc947-e01c-366b-8ee5-56643b3a6910 | -10.52715 | -51.07916 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aea48c54-73a9-398e-9340-4e9454c96ab9 | -10.52565 | -51.07993 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f35b026-702e-3561-9188-7136cb8bf445 | -10.52343 | -51.07847 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5f04efe-26e2-357f-b53a-546fd7f47ef0 | -10.52267 | -51.07481 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb9ecf37-91e7-3378-b1bf-45e62ebde4ad | -10.5197 | -51.07781 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 839ecb15-d8f8-3b6b-8ce7-d645c371fe29 | -10.5182 | -51.07861 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ca807ae-7ac4-33f4-8e37-9948f386674a | -10.51597 | -51.07719 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3df1d326-0a92-3884-82c6-e269458989bf | -10.51521 | -51.0816 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 93d1fe09-86cf-3bb3-8b2b-7d86ac4b7674 | -10.51446 | -51.07798 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ab62fca-502d-3177-ad9b-6dbb39e0aa5a | -10.51372 | -51.08241 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa3f6db9-d6cf-3b58-93bf-2bcef7961d79 | -10.51298 | -51.08687 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af8f7ed6-2395-341a-a37b-a60167ca9b23 | -10.50998 | -51.08185 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd5666c-908d-39d2-b476-a9c2059a2f18 | -10.50923 | -51.08636 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81f83f92-7d5e-3d86-9e0b-9168239fbafc | -10.50846 | -51.09096 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1442384a-2449-3810-86b8-ed0a35d2629c | -10.50769 | -51.09557 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4572d95d-5879-3bcc-bd56-3b9f1309920b | -10.50542 | -51.10921 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b94ab4de-a602-3b45-91c6-faa396077347 | -10.50467 | -51.11365 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04bb3a1e-955d-345c-81a7-862e297225dc | -10.50091 | -51.11316 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fec88c0-2638-3895-8c99-4490fc11d5c4 | -10.50018 | -51.11754 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62ba0beb-b4e9-3cc2-b64b-b91f00a4545a | -10.4964 | -51.11714 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cbd788c-5815-37d2-a46b-d3df0c4bfe40 | -10.49563 | -51.12171 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67b02b54-a328-3b54-b81e-3a2df0d46d3a | -10.49188 | -51.12116 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfeca0f8-6b63-3eb6-992d-6f97eaa43015 | -10.44912 | -50.76994 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c05c9df6-76e5-33c0-99d3-cd72980dd297 | -10.44547 | -50.81472 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1fdfda6-0068-3e78-970e-03303d46d7a6 | -10.43884 | -50.80902 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d1e32d3-3db3-3275-8cd2-264efb14f958 | -10.43811 | -50.81342 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4892e17-5572-3b91-8447-de6ea82f4b23 | -10.43738 | -50.81783 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecfea055-c56f-396f-8aaf-12aadf2d21c2 | -10.43517 | -50.80836 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6a91269-62ae-35c8-bbe7-05c9791cafc3 | -10.43443 | -50.81279 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1d7d0b0-12b7-3589-b2df-ce2da9ecc3e3 | -10.43368 | -50.79462 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8129d9b-0926-3770-9845-44044eb0f2b2 | -10.43295 | -50.79895 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb8ff43b-c290-3c67-9dac-598ad0cd2906 | -10.43224 | -50.80323 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f72c547b-136e-3d74-bf77-346fd8436232 | -10.4315 | -50.80767 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 924f52ac-995b-3208-90df-b8dbb1da2dc3 | -10.43075 | -50.81216 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29931f43-acbb-30b8-9254-7c4f8c7a3c71 | -10.42857 | -50.80255 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 89688389-6d45-331b-a264-8846f2e17b52 | -12.90248 | -51.3278 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9044714c-74e1-3dba-8b06-64638aaa4cec | -12.90172 | -51.33221 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6ed332d-b23c-3e50-8eb2-921375ef1750 | -12.89149 | -51.32588 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac410432-19fa-33b4-87b4-f1d80f76fadc | -12.7228 | -51.9828 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 053f1254-a56d-3439-a8a5-f1ee70732def | -13.25875 | -51.22466 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 85470f04-0449-37c1-bf28-3336b4c1e8ab | -13.25801 | -51.22898 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4b41518-882f-3020-8e3e-b6ab3bea81e4 | -13.25727 | -51.2333 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88c210bd-47a5-348c-8232-ee5ee9ffa1e2 | -13.25653 | -51.23763 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94a0c1b3-e4d8-3b6f-a766-c0438d3ef765 | -13.18958 | -51.20974 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 005ab037-9fff-3de1-8bd9-f96605688e84 | -13.13121 | -51.42002 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65db65b1-4434-3bf1-a478-00cd6a124a27 | -13.80713 | -52.43772 | 2024-10-03 04:27:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77b3a865-6dbf-371d-b792-989811ab0338 | -9.46459 | -52.09837 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920b8f5b-65ce-3836-be77-7c3716191135 | -9.46117 | -52.09404 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96054400-3e54-301f-bd6c-5b80470aaca0 | -9.46056 | -52.09768 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59413e5b-6ebc-3a33-a631-a67c143fa6a9 | -9.01931 | -52.10917 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91d0d4df-1b7e-3848-899e-c3cc20d8a8f1 | -9.01871 | -52.11273 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0b241a4-6365-3735-b254-c788ef228bf7 | -8.96858 | -52.81449 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa733f7e-bf37-3eaa-8c3f-58892384746d | -8.96788 | -52.81855 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7340798-1aa8-34dc-bfa8-f75333407baf | -8.96221 | -52.80071 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd26939-5bd2-3ba1-aeff-44b6864d1817 | -8.9615 | -52.80476 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94fec098-1931-38f6-ad0f-a9a74ebc57e9 | -8.95797 | -52.79987 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 375eb248-1105-3d34-9f7a-96f2b5704f23 | -8.9487 | -52.80274 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19bad8d5-3ba6-3ee4-ac41-937bdf8036eb | -8.93602 | -52.77518 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfcf5ada-cf74-3911-aac6-509e416309f9 | -8.88269 | -53.00139 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba4a2f08-7d77-3a28-8f99-3c91f4d5b074 | -8.88197 | -53.00543 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67d2b774-afd1-3fba-b82a-5bd1c741af53 | -10.91008 | -52.4097 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bfa9d4d-ff8e-3481-ae35-832ad2bc7f5c | -10.90947 | -52.41324 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50a0b55a-29f2-30c3-9ba4-2858c5507948 | -10.90886 | -52.41679 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7377d151-973a-3a11-a68e-219373081c83 | -10.90825 | -52.42034 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e8312019-63ca-35cf-b0c7-c045483046bb | -10.90762 | -52.42393 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0fc6822e-ab71-396e-864a-988b0422bbc4 | -10.907 | -52.42756 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef36d74d-ead3-3ea3-8691-86be7b940e10 | -10.90668 | -52.40543 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README97.md)
