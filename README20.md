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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a2ae3b6-4b10-345f-9eb3-6a3e201aaf64 | -8.84612 | -49.85668 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e9cb620-3018-3c65-97f5-18b5cea98ba7 | -11.57393 | -52.10854 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8fe27e77-50fe-3c48-8742-b11d681a1d77 | -9.23767 | -50.03283 | 2025-06-27 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07db60d3-52d3-3b94-8bcc-bdaa0df6ddd2 | -9.07596 | -49.4281 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e84dfd3-0fe3-337c-977b-e2a58a10de26 | -12.0321 | -48.75216 | 2025-06-27 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa8fb024-d344-3fb1-89e2-dd6094bcabfc | -12.42612 | -43.72506 | 2025-06-27 04:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7be81871-11c0-31cd-91ee-edc9b0194cbb | -9.06842 | -49.43088 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1edffa8f-b364-3b96-b054-e625a8791ec9 | -9.78685 | -48.57356 | 2025-06-27 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6793bb6c-20e0-3852-aa0f-80386331a0c4 | -11.99934 | -47.16187 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2cb858e-1cc0-3c40-a2ab-1de4b5edca19 | -10.06859 | -55.55304 | 2025-06-27 04:49:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 663579fe-7e9a-302d-8865-2823a5ae6969 | -10.82232 | -53.75012 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5557369f-a9af-3183-8463-89ba63102cd6 | -11.57227 | -52.1191 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b427b7f5-17a5-38dd-867a-3911b0493944 | -11.68386 | -46.72847 | 2025-06-27 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67f33eab-9458-3b86-8263-293fa5d7e771 | -14.21141 | -42.78177 | 2025-06-27 04:49:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 34f689a9-34ab-3b61-8cce-48221501fe14 | -10.41916 | -47.51096 | 2025-06-27 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de0a9afa-52c8-35dd-a841-f7f485e0b403 | -11.91806 | -54.81262 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e019204e-8f93-35ed-a57b-f023b93a2250 | -12.00847 | -47.15581 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d3b9b63-6707-328d-80ad-bfd274c50802 | -10.52435 | -53.62607 | 2025-06-27 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2101de09-6c53-3c90-a202-4351d50383d9 | -11.18634 | -55.91868 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0f2d015-e2ec-3bf8-b482-e481fdefe80d | -12.5212 | -57.23619 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53819a26-5e98-3a39-bc83-99e8ec140ce7 | -9.09039 | -47.96933 | 2025-06-27 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d72007e9-92f4-35ce-a842-9b84d1860737 | -12.02207 | -57.08809 | 2025-06-27 04:49:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63f610b1-d2f9-33ea-88bb-668406f0c69f | -10.29494 | -57.12891 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd22e844-bd02-3b9e-8653-fd72e9893e13 | -12.00748 | -47.16311 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01ca57b9-290c-3a62-b24b-57ad6682472b | -12.10823 | -54.66652 | 2025-06-27 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3caa4ff-6770-357b-a2b5-e923272567fa | -10.64245 | -46.70781 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11b08e49-0280-3b7c-9ad8-88b33337662c | -8.48337 | -48.25922 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbc34f50-9a94-3396-8bde-7dc3e0fee8f8 | -11.06996 | -55.37925 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4df1673f-85d3-361f-aed7-9ee036db2da9 | -10.42021 | -48.61484 | 2025-06-27 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 575a2fdd-8654-350b-838f-c70e03c8735f | -9.87425 | -48.05347 | 2025-06-27 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13bb0ec4-c31b-32f7-82d0-0bf2e41848e0 | -10.81367 | -57.75628 | 2025-06-27 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e2b5569-f8d3-3393-9740-7b3cb9cf263b | -8.12475 | -49.4854 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f28b6018-de55-3cfa-a591-029ac20854b9 | -14.20533 | -42.78487 | 2025-06-27 04:49:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 48450824-1eea-3576-b27e-8cf1abacc290 | -8.3735 | -51.0772 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f47bc43-038d-3f89-aea3-fa3f5c63c666 | -11.57948 | -52.11666 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| cd78b55b-4e62-31e8-9eac-915f655156f6 | -11.67968 | -46.72798 | 2025-06-27 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eebed135-c3b7-314b-ab4c-0e57d26dd0c9 | -10.43085 | -51.8275 | 2025-06-27 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8398a2-8bdb-35bc-8f1a-ac3746d31310 | -10.65381 | -44.48734 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed57a2ee-806b-304a-92c6-cdb84c59dbcb | -12.75435 | -44.41291 | 2025-06-27 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0e002ccf-4bf2-31d1-80d5-7840fc2a564d | -12.00363 | -47.16327 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e609d1c-394a-325f-9678-fe8d29d382a3 | -9.35622 | -58.84972 | 2025-06-27 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb36141-e5e2-3fd3-a47a-9d6dc5923ccf | -8.54634 | -55.03458 | 2025-06-27 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d33331c0-8cb4-3234-9759-ef77a16d271a | -8.6208 | -51.57077 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d95c4949-4ee1-378b-8b06-71abcdfa6ff3 | -10.71441 | -59.1305 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3af89504-2268-35ff-a044-72b04846b2a8 | -10.27335 | -47.61198 | 2025-06-27 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20b25e4b-1bea-38b3-ae7b-f885ae1c58f2 | -11.77453 | -55.04006 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5281ce53-b142-3163-a368-098e8d493ac4 | -9.49735 | -56.09411 | 2025-06-27 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5512a510-063c-314c-b292-abcc234e3607 | -10.43141 | -51.82399 | 2025-06-27 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ae7f57-57e3-3f2b-ac3c-4bc2cff6b338 | -11.3847 | -56.54735 | 2025-06-27 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdc294f7-baf5-3278-9f0b-2aeef74a4b57 | -11.06633 | -55.37861 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52db2a0d-93d7-3806-98e4-77b87a1f1c43 | -10.42378 | -47.50653 | 2025-06-27 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 343913fe-8a40-3c32-bda3-d0f0e5bf034b | -8.49002 | -48.26455 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 572c368d-bcaa-3125-89ce-fd2c4a9d474d | -10.27475 | -47.60224 | 2025-06-27 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fedf8f5-47d8-336c-872e-31a323ea859e | -7.30563 | -55.3059 | 2025-06-27 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9d2fa4e-936b-3189-8d8f-bdc0136621b7 | -11.5767 | -52.1126 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e58c4fb3-5d44-31d2-b903-3b73ab72e903 | -9.74504 | -48.045 | 2025-06-27 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b6472c3-b34b-36b0-91d8-fb94230e681c | -9.12159 | -49.44277 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b8dbb23-2da1-3cb6-a113-84fb7a7efd13 | -13.05242 | -48.82114 | 2025-06-27 04:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3b18282-b32a-376e-9ad4-4faefe2ecd62 | -10.30589 | -57.13833 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0560f4ef-69a1-37a6-b83e-ea183a7e06f1 | -11.74613 | -54.23304 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ad5b3d-618a-35ff-880a-73ff69bc252b | -9.7881 | -48.56503 | 2025-06-27 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c2d3a39-43a0-3dc7-8e01-11d239479e21 | -11.77374 | -55.02325 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeaaee64-e33c-3097-80bb-c50add6eab47 | -10.83095 | -53.74017 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e56c6a6-5b08-30d5-ab02-5b71406014e7 | -9.23141 | -50.02808 | 2025-06-27 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66868e3c-3e82-3e6d-af30-d809166e5a11 | -11.99904 | -47.16632 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1ad7a0f-64ab-3036-a517-d75dd8b53517 | -11.44122 | -54.46555 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 446b4ff2-ef12-33f7-b4d7-e713cc52f244 | -8.22411 | -47.21672 | 2025-06-27 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f843f35-0f6b-38a8-a5b4-a177acd9f7df | -9.0696 | -49.42318 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87625538-a442-3951-a09e-e1a9f4acb97b | -8.61251 | -51.58017 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33f8beda-6ebb-363c-ab7c-3e14089db61a | -9.50507 | -56.09541 | 2025-06-27 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cb10180-dc23-3121-bbef-c13ba123829a | -12.43169 | -43.72258 | 2025-06-27 04:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52bc1ee4-4859-3ba9-82c2-dc1027a32838 | -10.85235 | -54.03198 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7418831f-ee93-3def-a4f3-a84afeec4a01 | -12.11106 | -54.67102 | 2025-06-27 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c3b4838-9ea6-3679-988a-53eae66b9650 | -9.35159 | -58.84887 | 2025-06-27 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c3afa07-4e78-3856-916b-cfae41e26183 | -9.43093 | -49.39637 | 2025-06-27 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7806e0d-1b83-3baf-8f6a-7cf49267242d | -10.88017 | -49.54993 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 823fd986-e8af-39f5-b305-4811da12eb01 | -12.11171 | -54.66712 | 2025-06-27 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd445548-28a8-3c7d-88da-68c4b81a454a | -11.4371 | -54.46881 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 529673f9-17c2-3986-9afd-e3be45297193 | -11.78162 | -55.04129 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9247ef5-9e7d-3c2f-bbf7-adf95af94329 | -8.37738 | -51.07423 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba51506b-aa04-315f-8b75-37298ec4b617 | -9.82324 | -48.37656 | 2025-06-27 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a6fb91c-18bb-33e1-8158-c36c12a6cddf | -12.02729 | -47.77228 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 052324c5-2d1f-38c5-89d9-f644f946c534 | -11.67082 | -46.73056 | 2025-06-27 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdcc6b82-a792-3edb-9061-63251719d5dc | -8.61693 | -51.57372 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1da266eb-ee40-37b3-9a36-000ecd0b520a | -11.43993 | -54.47326 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16bf717a-76a9-3ae5-a83c-20c83d89eeac | -12.02691 | -57.08364 | 2025-06-27 04:49:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b5fd66c-3852-3cd1-ad70-33f61f79b13a | -9.81892 | -48.38033 | 2025-06-27 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cce5b529-d8c6-39e4-89fa-01a5d7bd52e9 | -8.61528 | -51.58418 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48a29f8b-6e1c-3dc6-a0fa-f0dab2b78ef7 | -11.60222 | -55.54733 | 2025-06-27 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a8dedfa-8a59-3d40-be03-4b032c675565 | -10.83034 | -53.74388 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6adae9ca-87ed-3855-a817-288d8080b3f1 | -11.60295 | -55.54304 | 2025-06-27 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a671bf3-7797-34ea-8856-9524e891c225 | -13.06402 | -51.63989 | 2025-06-27 04:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c921308a-19b4-366a-9483-84e7d9654d39 | -11.18092 | -55.92479 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f78e6bc-85d1-3ad1-a8ee-2f33b3b065f7 | -10.24435 | -47.67663 | 2025-06-27 04:49:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbd18b85-0db7-3cba-b192-aa6a78ef6ee7 | -9.34148 | -58.85206 | 2025-06-27 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60d8377b-8168-345e-b4a6-272ea584fdd1 | -8.12419 | -49.48915 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80528df3-06f4-340e-a372-17795e6e8961 | -9.11522 | -49.43785 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2646028c-ead3-3cae-aa2f-f9b88e37b459 | -10.8738 | -53.77792 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4646214-6888-31b7-b3a6-ef0c5b97ea43 | -7.98359 | -49.6815 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 888ac216-412d-3ef7-9a53-b511fcc87f51 | -12.03139 | -47.77629 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README21.md)
