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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56527900-98c8-3c67-be71-4e0dbe6211f4 | -10.47614 | -47.58297 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85709f19-1967-3df4-8536-68f76e1e7786 | -14.60934 | -48.21607 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6dea82d-9b79-3938-ab0d-3075f54e50cc | -11.38134 | -45.0587 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e12ef4da-227e-33e9-95d0-8d098a4742f1 | -11.76733 | -46.85262 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ab2afa00-2c96-3eda-8c15-b9d3ae5a7a15 | -10.72985 | -48.17976 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77b63d57-3443-3ec2-a95e-cf2653f7b2fa | -10.91791 | -44.30667 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 696c8a34-a1e9-33a5-ad94-eb7eb832891e | -13.2899 | -47.23223 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f931394a-8236-33e4-8501-33b43830d131 | -16.3724 | -47.0462 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 541b96e5-763a-38d5-98bd-98e4cc051514 | -10.36448 | -48.78259 | 2025-10-01 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cb1e8cf-ab40-3a9c-8001-04aa3bbf0a6c | -14.59921 | -48.21451 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86b33569-03be-369e-b914-61c4b2aff41e | -14.36414 | -47.13396 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e4f0f79-7471-3b72-ba0d-2b9b7ed76c35 | -11.91992 | -47.89306 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6f9ac77-6d15-3b31-8c73-cb3993e4cea5 | -12.84816 | -47.03466 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 340fc450-e183-30d3-aa9d-cffa8bd60499 | -15.77657 | -43.70925 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 806e45fb-8bd5-32a5-869b-0cae670dd924 | -11.64322 | -47.49744 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc25cd3-e5b4-3919-8578-4f2da5b33157 | -15.27007 | -49.28416 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84e1e626-26c5-370d-953a-09ff4c4dd878 | -13.33413 | -47.33936 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac28447f-a118-30d4-8890-286cfd96ce47 | -15.62871 | -46.24871 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6c98bd5-f945-3feb-9ae7-4907bf4b9147 | -21.66943 | -45.34006 | 2025-10-01 04:23:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed67f0d6-8968-37b4-956e-89f53a331e58 | -22.63055 | -49.05071 | 2025-10-01 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3c694b75-0200-3499-9022-db04a7a9d4a5 | -18.69991 | -44.3329 | 2025-10-01 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e5f3dcd-29eb-375c-a30c-151970fb4a5a | -19.86455 | -43.81805 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9d95991c-5429-3e55-980e-11a77533332d | -20.63011 | -46.20431 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a56efdf6-808c-3d53-aeb3-57c0d2530d63 | -19.93112 | -43.89189 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 510f1ca0-18fc-3d8e-bd19-d6735bf7b607 | -21.81422 | -48.13927 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72bd7199-26b2-336b-8d63-09c326fdbe57 | -23.3313 | -46.86555 | 2025-10-01 04:23:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0940b01c-c928-364f-bd74-74674b7a4e92 | -19.85891 | -42.5825 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1ce1e3c9-aab2-3f3f-bed3-04937324239f | -20.62839 | -46.21629 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a34471e1-4d5a-3de6-a97e-47cc2ebfd364 | -20.02829 | -44.54736 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9a199d7c-1d30-35b4-9d22-0ab9cd567617 | -20.48749 | -43.94437 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 43f8c831-fadb-3efc-aa47-09a63a6c3d35 | -22.44339 | -48.3143 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cc21097-c5c4-3596-9855-a3f71699d3b0 | -20.61367 | -46.22179 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05fe8e6e-e3b4-3507-9803-66bd25c3b974 | -22.24128 | -43.40848 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 238a8857-a526-35e5-aa2e-a7c15303bc01 | -18.67172 | -43.70706 | 2025-10-01 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b6017b1-d9ba-3b33-96bc-7e9257c91d49 | -20.6267 | -46.20382 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20f00aa7-a622-3c23-962f-9672a0edb8af | -17.67613 | -47.25783 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3188d104-eeaf-3b19-a5f1-b4794a11f277 | -17.79424 | -48.63147 | 2025-10-01 04:23:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3848743c-d10c-300f-b1d2-1060bd6bc528 | -22.43678 | -48.31314 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfa5c4d4-ea70-3bba-8027-4feae7eabf25 | -20.63463 | -46.22124 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8631bd39-39f2-3b90-96c9-850b0b0f502f | -20.02526 | -44.54251 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 9d43a15f-7f4d-388b-b48f-23dc4bab0441 | -19.77382 | -45.43972 | 2025-10-01 04:23:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 42193804-d039-39b4-870d-6fda9024c377 | -19.85698 | -47.49296 | 2025-10-01 04:23:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96b32768-4323-3c45-87f1-a709dd0c2995 | -20.46956 | -47.37819 | 2025-10-01 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b8a98e9-9263-3f24-9a48-71db3ca9be99 | -20.11157 | -51.80273 | 2025-10-01 04:23:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 804c1c45-c4bb-3f7b-9829-ca0ec098c8d8 | -23.27014 | -46.65525 | 2025-10-01 04:23:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 32ec6c08-f5a8-354b-9768-dbcedd12f943 | -20.61818 | -46.21469 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a8f79b2-0e74-3b61-b897-3becc2b8c80c | -18.3117 | -44.02745 | 2025-10-01 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d6e8cff-e85a-32da-8b10-a31ef037555f | -23.21173 | -45.11259 | 2025-10-01 04:23:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 569ae2d3-67b7-3170-ba18-53c0a98fb671 | -22.11897 | -44.69514 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e06d87c7-aa06-3976-8af7-4b6a13eab062 | -22.29505 | -47.7533 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bcdc0662-551b-35b8-988a-9f1b93c70f7c | -21.3345 | -45.87759 | 2025-10-01 04:23:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a4471995-97ef-3c1a-9d7b-f1bce1ee8683 | -22.6552 | -46.7457 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ecac956d-2d41-3cac-b7a4-719b72941933 | -20.02889 | -44.54304 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ad2cf9c7-1c77-3eb9-80e0-b3345dfdd937 | -20.22071 | -43.44514 | 2025-10-01 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2a525973-5e0b-3f1d-a54a-d5f130569a25 | -20.64202 | -46.21827 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f9eab60-040a-322c-afc9-034c308058c6 | -17.97237 | -45.02101 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc82e00-1cd9-3d45-adf3-95d02f6f1440 | -19.63972 | -46.5516 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31836f8b-4114-317e-a3a4-332cbc40640f | -23.35947 | -47.03214 | 2025-10-01 04:23:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e97adbb7-6879-3dbb-a7ca-897de9f714dd | -21.59567 | -43.49363 | 2025-10-01 04:23:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57f26174-594e-3926-b9ec-f99cf11f710e | -20.83638 | -43.02295 | 2025-10-01 04:23:00 | NOAA-21 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0f027df0-dc61-3286-b73e-3ccb770fd47b | -19.93728 | -43.90269 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3c2e3626-7127-3582-b30b-b50a4e394de6 | -22.58453 | -46.77757 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 8af87ba5-761e-3a3f-91e6-2f133fac9356 | -21.62762 | -41.39762 | 2025-10-01 04:23:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c8f4d9e5-3873-3752-82cb-c5f84f85ab96 | -18.90689 | -48.06536 | 2025-10-01 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2604ab07-20fe-30a9-bede-e6b8e408ae9a | -19.69406 | -43.98927 | 2025-10-01 04:23:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd64d6f-ca91-3eda-8bb9-f19a72377a8c | -22.37083 | -48.64842 | 2025-10-01 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b6fe0cf0-62d0-3795-9c65-3786823f50dc | -21.88169 | -48.14368 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9fd27bd-cc35-3095-a095-a7fca508435d | -22.06347 | -48.33097 | 2025-10-01 04:23:00 | NOAA-21 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef1696b5-469c-32fc-bc88-16f22268b56a | -22.1032 | -47.80793 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd8a118d-2b11-3810-b8ee-1a7520713263 | -22.11645 | -44.68568 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cae3abd4-9c62-3dd2-9a0a-5a578293cd9c | -18.42362 | -43.81384 | 2025-10-01 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 994fb2ef-2cde-33e6-85da-363bb0113446 | -18.43353 | -43.79663 | 2025-10-01 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bf9c68e-4069-3d75-8db2-a8375513f29a | -20.12593 | -44.02261 | 2025-10-01 04:23:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 47587a97-22f4-3b2e-aa6f-13ef6a1deb53 | -22.93066 | -45.50939 | 2025-10-01 04:23:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7e931fb6-1f86-355c-b8f4-51eead544317 | -19.8683 | -43.81862 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf0ac43e-26db-3c34-ba3e-64823e97e52f | -22.41292 | -43.16773 | 2025-10-01 04:23:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 106ce278-6e53-39c4-b849-daab15eb903f | -18.25577 | -43.14459 | 2025-10-01 04:23:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4515c01d-c492-3cfe-b84f-8b5703a67496 | -18.36139 | -42.3957 | 2025-10-01 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 24d41b55-02b0-39e6-9773-dfd6e8c6fcb6 | -20.44623 | -43.11332 | 2025-10-01 04:23:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 569934ca-341e-3964-8920-e15f36574b1d | -17.96084 | -45.02725 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 345fe72a-79ec-38b4-bcc2-fd1674ed85cd | -18.70892 | -49.16565 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c7ddae3-87ef-35f6-b7ca-0dbbd462db92 | -20.23241 | -43.8921 | 2025-10-01 04:23:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fd01532b-279f-30e7-9b3f-3d16cadaaa9b | -22.10983 | -47.80906 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69de68ae-63ae-3294-a4c7-17624f6e7462 | -22.10595 | -47.81221 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e71ecaa0-8243-3bae-8aa3-f32db5024271 | -19.80973 | -44.07217 | 2025-10-01 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45fd0ba7-c8c6-3716-b47e-5501f3eba635 | -20.62386 | -46.19943 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed5b3059-dbd9-3b5e-af0c-1c62d73d24b6 | -23.06209 | -47.0282 | 2025-10-01 04:23:00 | NOAA-21 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b7c81833-33ae-37a3-8df7-e7bdeebdf136 | -23.24424 | -45.45536 | 2025-10-01 04:23:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7c50e8e-24ab-3c8b-9a8a-6a0801fae97b | -19.86274 | -43.83181 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7785c6ca-d4af-3722-9d7c-4ea7cdab4a13 | -19.46364 | -44.28401 | 2025-10-01 04:23:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43f96fc2-f38c-3b1a-8623-830e9de56a17 | -23.19366 | -45.10849 | 2025-10-01 04:23:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f99f712b-1bfc-3aea-8e9a-d29018922037 | -22.11163 | -44.69389 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 48202354-0dc0-3e68-b710-c0699ae10c8c | -21.80015 | -48.18614 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c681ec18-cb7c-3546-a027-aa855d576c09 | -22.24522 | -43.40921 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| ae00d61c-bb77-3345-a66d-75dabafc3a45 | -20.58909 | -45.88085 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c8d91d17-387b-3d99-bede-75a709b1c6ad | -17.95504 | -45.01813 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7fc8d05-277b-3fd7-8e42-556b534fa672 | -18.96733 | -43.70959 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 443180ad-5f27-3d99-834e-664225e10d2e | -17.67501 | -47.26502 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 240c5471-b744-3d89-a544-5b610255a1e5 | -22.27663 | -46.72842 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 076601c7-32c3-3ecc-b2eb-aa2dd00f8bef | -22.11471 | -44.69902 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |


[Clique aqui para ver as próximas entradas](README76.md)
