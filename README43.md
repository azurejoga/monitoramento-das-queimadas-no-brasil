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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dc71ef3-3c31-342b-884d-6e168b6bc70b | -8.57508 | -54.73352 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db5a317a-299c-3022-8e25-3d9eb9a3dc2f | -9.46303 | -51.60288 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 374f17b6-7671-37af-a68a-247053e02d60 | -12.36984 | -46.44102 | 2026-08-19 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e839699-2471-3197-89d3-eec244cdf5bf | -11.22925 | -55.07935 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47f7aae4-53a2-386f-825f-1e23ce9b62b9 | -11.22998 | -55.0753 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34048d8e-958f-3669-bda8-5ab31bf95ea0 | -9.3937 | -60.55847 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35442df1-0728-32f5-bac2-cd5ac27debbb | -8.54261 | -54.73352 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a593b8f-3133-3ee9-a78f-f7a4bd9eca18 | -11.41038 | -47.23496 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f154b2d9-e0c6-33b0-bf78-018cfd8654f2 | -9.07811 | -50.80952 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a2451b1-f376-36a8-a0df-c84c935eed3b | -8.56341 | -54.77451 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc4264d2-b668-3b09-9edf-7f43d351a83b | -9.45389 | -51.61404 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a6e68cd-0b31-37d0-8e50-835aa22a8df4 | -11.20102 | -54.01234 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38ad4bb2-d9b1-39b4-aacc-cb496edd9b95 | -8.57726 | -54.7466 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc277f1b-50a1-3ced-b651-3ed83f0e3a6f | -9.08277 | -50.80263 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2fb0ab5-2bed-36b3-b408-cba888caf4e5 | -10.67637 | -49.00223 | 2026-08-19 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e60541d-0164-3948-bf6d-1e4e85828549 | -8.54123 | -54.72298 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a120d66-8296-3231-b7be-d814ffd70a7d | -8.53464 | -54.73489 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f76acc16-29ae-3525-b393-4fecdba23275 | -8.539 | -54.72851 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ee16ab0-9aeb-3c26-bb39-559bbc92fa87 | -12.75903 | -48.44806 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 733db228-349d-3bd9-abe2-bec8519fb789 | -10.12612 | -52.10337 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd834c10-a81f-308e-95cc-7ab7b73b0f29 | -10.4227 | -46.34363 | 2026-08-19 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59abd078-8df0-3905-a183-f32661007bd0 | -8.58299 | -54.76496 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83f92548-d595-363d-84d1-196ae41eada5 | -9.73893 | -46.83474 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 757ca3c5-f751-3c9b-8001-5ab8412af375 | -8.57076 | -54.7327 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7c819b9-6c5b-37f0-b557-6979e56b0923 | -8.55547 | -54.76877 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f70ba8a-38d7-3a47-a3c4-b9bc136e7db2 | -8.49848 | -54.86054 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1505decb-c404-3838-9fe6-cc7788dcb36d | -8.58593 | -54.72254 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c767f556-9f11-3d7a-9117-d98a342d9024 | -9.55413 | -48.66748 | 2026-08-19 04:40:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ffec67b-a4e9-3bf0-97fa-ab506385a63d | -11.07724 | -47.60618 | 2026-08-19 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d113ecb-44de-3fa9-a06b-fa7f784cdc16 | -14.4582 | -45.62794 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c5b1dec7-508c-321b-b882-ad29629ffc49 | -11.225 | -55.07864 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c049bc90-066d-39fe-ba4c-653d23dd401d | -8.53322 | -54.73621 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fc127a4-9039-3aa7-9c78-b915fdc80ae8 | -9.39167 | -60.55439 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ffd13e17-53b1-3b02-a848-0b55e8a27d96 | -13.45219 | -51.79829 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c629e6ae-3a2b-35a7-9109-82c34be51fbe | -8.58234 | -54.71757 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f70a3fa1-79d9-3c73-be80-aed6f03ffdfd | -9.08683 | -50.79942 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbf3f8de-082e-3978-a868-51f35ec71832 | -11.22222 | -55.06976 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d0c31ea-00c7-30cc-a13d-8ebf5fae6169 | -8.53961 | -54.75719 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a62a4664-3355-34a1-9a90-f84cdd5f20fb | -13.26417 | -51.6413 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dea55c1-16ad-3450-8d54-764ee83ffddb | -10.93671 | -57.10703 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2060e588-d882-3ecb-9abc-797ad8946ab9 | -8.53539 | -54.73066 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cb12d16-4d9f-3dae-a3e9-5bc18d7f66f0 | -8.50696 | -54.86473 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5ca7928-20c9-361b-af22-499d60451c5a | -12.50987 | -47.8556 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 808617e8-5941-3f84-a2d7-0808dbc0d522 | -8.54189 | -54.73774 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87d0e277-9945-3700-a027-9ada16d3ae48 | -14.46518 | -45.63392 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 169d0ff8-03d4-3ef5-9e67-925c42668a65 | -8.57659 | -54.69952 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a99fd4-9db6-395b-b963-fa791a45deec | -9.16393 | -59.71194 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8641bf2e-0930-3f67-842b-3500d5640db1 | -8.50723 | -54.8621 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c21279a-3ce4-3224-96a5-4ec630d9af2f | -8.53181 | -54.72567 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d3068cf-5f00-31a1-8c0e-aa6a9669f8a3 | -10.02806 | -48.18032 | 2026-08-19 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349b4978-33c0-386e-819b-3a614660b7fc | -8.56859 | -54.74507 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 889769ba-e0c3-3329-af71-3b8acd8f546e | -8.57292 | -54.74585 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 055d9230-549b-3057-bbdb-3a80ef47abfc | -15.77977 | -55.55709 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d11918d-745e-3e69-8c5b-c3b4960f030b | -8.53614 | -54.74531 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5299efe-00ad-38b0-a7b2-5fe74815d196 | -15.77501 | -55.56025 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f5f14ce-50db-31e0-b33e-e7d9cb62d48b | -11.22087 | -55.05298 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8ec80e7-ea54-354e-9b24-661064499f49 | -11.20984 | -54.00863 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cacc26c-e762-38bf-bb32-ae22929c0677 | -12.78969 | -48.42696 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71f9db61-709d-35e6-8989-b5f814ac0d2c | -8.53394 | -54.73198 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed4f23e3-0c77-3727-bba3-f5aeb2f67a82 | -9.01531 | -60.51166 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61addf33-37ac-3d45-8ae0-a743d165a612 | -12.47647 | -54.18311 | 2026-08-19 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4760ff6f-a827-3e26-bb36-12b28c184455 | -8.53166 | -54.75156 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26fe61d4-1b64-3a08-bf40-009496163ea6 | -8.56354 | -54.74834 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f8bf8fc-bc0b-359c-8434-2cbd3c3e02a8 | -15.77279 | -55.57272 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 058e57e0-66f2-3ada-a48d-7b25fd1ec9ee | -12.94603 | -56.6462 | 2026-08-19 04:40:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2721540e-01a0-3f31-8ed4-384a2ea7e44a | -11.69058 | -54.55689 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 422b0708-9f6f-3334-8c0b-4974791bf7a9 | -11.12473 | -47.29549 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28ad2a3e-ef9a-32b9-be9b-81c0be9ccee2 | -14.46968 | -45.62961 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ca9e24f-27a6-3546-a8c0-873b3203472c | -8.53037 | -54.75293 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3d4e857-1a0a-3792-946b-1915a384ec30 | -9.42214 | -60.40981 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0123899a-bbf1-3f02-8b35-ef8bd3443dfa | -8.57432 | -54.76339 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f89b69b-7555-35c4-a8c8-e0158f79d64a | -8.56432 | -54.71859 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3ae142e-05f1-314b-8688-9df113541208 | -11.11961 | -47.28327 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0275593-0c2c-3f54-b812-0c982a9baf98 | -8.57948 | -54.68305 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 704fc0df-7728-32f1-bdeb-b6143cc55663 | -8.52965 | -54.75712 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a56925ef-a048-3adc-9783-78c8cc293f0c | -11.11108 | -47.29341 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a59fc515-d8ac-35c8-b122-9d195dd0fc80 | -8.56425 | -54.7443 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e68b941c-a9ae-35e8-8d9b-d11b60be797d | -15.63856 | -54.81173 | 2026-08-19 04:40:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bc1383a-795d-3240-88ef-77c27e69c6e9 | -8.56224 | -54.6799 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d055380e-72b8-3465-9054-0a7be11e6314 | -10.51938 | -50.79226 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83ab065f-51ae-3d71-a4ef-9b4a9b1a45c8 | -16.50406 | -48.83785 | 2026-08-19 04:40:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1442c606-4f17-3ba9-85dc-b3ac790a917b | -8.53539 | -54.72349 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba1c4949-bd46-3f3d-a2b5-145fb9d40319 | -9.16468 | -59.67607 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ff40538-e850-3f33-bf09-972ab69cacdc | -11.11506 | -47.29018 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc2b5f42-2760-35a0-a036-7bc75658a603 | -8.56511 | -54.68885 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8b1908-974a-3a33-b267-2ed6ffdb3244 | -10.2436 | -46.99053 | 2026-08-19 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b28598e3-a88c-34a5-b331-f0b6179d27ec | -13.45156 | -51.80213 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c2c44c8-1626-3792-9372-c2adc93bb8bc | -15.31096 | -56.44933 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87e987bf-200e-3ae9-b2ef-351a5b9011a4 | -8.54828 | -54.75876 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b889362-a60f-32b2-97c8-69eee0f78885 | -9.28271 | -56.89358 | 2026-08-19 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 71ae286f-e713-3d81-83e2-61b72e6b5481 | -12.79247 | -48.43116 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7340b2c-7436-30f1-8454-8afb01e85a33 | -8.53533 | -54.88277 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66392d10-8b1d-3f9f-a6b7-7d8c40119eb8 | -9.05941 | -50.83728 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f27822ec-e915-3ce9-ae30-183438b58f28 | -8.58013 | -54.75574 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 32828cd0-24e0-3beb-ad27-4a12818d92b5 | -9.47077 | -51.60022 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b5a502-9680-3edc-8bda-51817611941b | -9.90423 | -47.73532 | 2026-08-19 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 845ea891-8a47-30e1-b01c-5164b7fa4d8c | -8.52658 | -54.75501 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0d1ce15-1f68-345a-8e5f-a51961fcda28 | -14.46203 | -45.6285 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87fe158a-856b-34d6-9167-076994c5f179 | -11.23891 | -54.83288 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdd18b29-215b-3b73-b374-5536861c82b5 | -14.14846 | -52.92116 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
