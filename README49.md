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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3258437-864d-3510-a23b-ad8b73b7109e | -17.9879 | -45.62391 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61cddde6-f2fe-392f-bfd8-cf09b658bb02 | -15.29671 | -46.18484 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3b75aa0-bec4-3e47-882d-dad9d863acfb | -15.31756 | -43.8503 | 2025-10-09 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fa64003-f0c9-3777-98be-23ecbcbdf1d7 | -16.10324 | -47.31317 | 2025-10-09 04:21:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 710808a9-2039-3253-9052-d4daf6d0077b | -18.05683 | -44.96936 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4664c1f5-d652-305c-a84e-1dcd3eef902d | -15.56306 | -45.29563 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d368fed9-4998-3b06-a87d-49501adbab16 | -18.06386 | -44.42069 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72d08f21-9387-3aba-98c1-2fa0c1904a28 | -14.94481 | -46.78027 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9828d81e-8d6a-3dbf-af0e-e0bb0614f03c | -15.29012 | -46.16176 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aeb4382f-4603-3945-8d4b-e218756f2cdb | -18.09168 | -44.45308 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f23c33b7-ec8e-30c8-b705-1824a10c67aa | -17.3762 | -45.08223 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdfcb6fe-1f6f-389d-9f11-ca9d77550fdf | -17.96992 | -57.50237 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| be054c28-adc9-3338-b462-4757152cade7 | -15.47675 | -47.96443 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 430f7f27-7b9c-3c07-be4d-ecb6d65a956e | -19.50613 | -44.08787 | 2025-10-09 04:21:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c2efbeb-1bcc-3623-b907-a2bd164a1539 | -16.37569 | -46.38438 | 2025-10-09 04:21:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12d2dee1-48af-3f42-a928-6eb7e99353ee | -15.75523 | -48.69629 | 2025-10-09 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88549513-0c46-3698-8dc0-b2c22172cd0a | -15.81095 | -43.78098 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7df86b7c-51e9-3be0-bf91-5dff2a8982b2 | -16.6983 | -45.00945 | 2025-10-09 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a25b01e-228e-3053-8031-3627966233f0 | -15.474 | -47.96016 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a89eccb1-ceff-39d5-aa9e-32ef2bfebbb4 | -14.84874 | -48.44696 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 004555bd-6d89-3b9b-9685-cc80d7ebca70 | -17.87908 | -57.6633 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a437b114-6c4f-38ca-a606-6ba726321804 | -17.99129 | -45.62444 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1df699b0-f8b0-37ba-ab03-832aa6d24663 | -17.53814 | -46.05902 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dd26e43-773b-3c63-8357-b25f63aa720f | -20.7219 | -48.41022 | 2025-10-09 04:21:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42377ffa-c8d3-363f-82bc-8d4a1c1d0dd6 | -15.9974 | -59.54491 | 2025-10-09 04:21:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a43d4c8-6d0f-38c0-b037-0a43ed2da882 | -16.06296 | -47.77099 | 2025-10-09 04:21:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a681d9-91a3-38db-a1de-b7ad119c63c2 | -16.60528 | -58.15815 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 97eb6dd0-29de-3591-843e-fbc8ebfd4676 | -15.48197 | -46.86267 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83c707c4-d834-3bfc-882f-59339d424511 | -16.70057 | -47.59267 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82590204-61a7-3592-a419-fe1ae486b163 | -18.24562 | -46.99514 | 2025-10-09 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f304bace-47d0-3690-a7ac-f4a93a69645e | -17.38934 | -46.89156 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a60427b-5492-3e60-bbd9-de7188d40797 | -15.24012 | -46.35115 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eada3dd0-5621-3533-a660-39712c11dfaf | -15.36919 | -47.33278 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe3e5058-c7bf-347b-b5ea-c3534c32e627 | -18.0394 | -57.5286 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 120ca980-bf29-35c5-87ba-d6bfae9cdc24 | -18.01058 | -57.52835 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 24d113a0-7857-3d67-9094-264442d8b13b | -15.23183 | -46.36074 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d53d89-3d10-3083-9608-ffc2e5ea7241 | -16.75276 | -43.97791 | 2025-10-09 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 806c6d98-6b90-3a50-93b1-613a283e4a9f | -18.04184 | -44.95074 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29baeded-8f19-3140-bb04-bc5eb7006b67 | -17.97383 | -44.96488 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f4b040-26f8-30ff-a2f8-966d239f40c8 | -18.05794 | -44.43665 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f6b968b-1c46-3a63-830b-6084ddf1f706 | -17.21388 | -47.65496 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 527e3c78-da89-301c-93f5-668870d3fe5d | -15.24726 | -46.37059 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 885fc4f4-67fe-3ea5-976f-6455d9234ca8 | -20.29994 | -49.70042 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e21c6e4f-8744-3bf8-80f1-fc792cae6d77 | -14.8481 | -48.4508 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 293ce7e9-7eed-3660-a0c5-dd4f52ad0743 | -17.38361 | -45.05566 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24d74a7a-ac2a-38b7-ab84-c1ba3a4044d9 | -15.78819 | -46.25426 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc3080c1-82b2-30be-8e79-d5e37d6aafc3 | -18.03974 | -44.70961 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88bc5a72-bdce-31b6-bd6a-552d6c7e5e37 | -17.37614 | -46.89023 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e96c3e2-683a-384f-a5d8-b6ce3978ea46 | -15.20494 | -44.4934 | 2025-10-09 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c17d0d71-4a25-35f4-85fc-2657d183ca9d | -14.96506 | -46.82384 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4c579d1-1018-3d8f-ac3b-19356bb4aac6 | -17.63626 | -47.20004 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd9e5a13-5ee6-3d65-b463-665ac5411e75 | -17.88905 | -57.66135 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5fa7c476-3ece-3868-9387-f49050c91e0e | -15.7991 | -43.78766 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec5babd7-fc83-399d-ad60-49a889607b95 | -17.37526 | -46.65673 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fce6353-2a8c-3923-9f38-a0b47d0cb1bd | -18.04301 | -44.99138 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dac4ca73-cfc4-3813-b7c0-061dd68ec82f | -17.38772 | -46.8802 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 071c907e-8f96-31b5-867b-6ae8f140f42f | -17.8216 | -57.63173 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0c90674c-b895-3dbf-8690-8af1cf018c50 | -19.33867 | -43.90062 | 2025-10-09 04:21:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9de8dbb0-3321-3d3d-869d-57a34ba22c9f | -16.29217 | -45.24597 | 2025-10-09 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26c53e59-426c-312e-b5ab-b60864c0bfd0 | -15.22959 | -46.375 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1096ebd8-4b2d-3fee-8372-7134954b5217 | -16.60331 | -58.15523 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2abeefd4-f1b1-38a4-8cdb-7f2598440fab | -14.88238 | -48.24561 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa7f5bbd-bd56-3572-9cd1-29ae1bf19740 | -15.29454 | -46.1552 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9668b223-e0ba-326a-95b5-3db309b04305 | -17.95194 | -44.99366 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d1973a68-513a-3337-bb51-c68feeed37e2 | -15.40144 | -46.27465 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 234af5d1-8b67-3675-b9a2-b063ddb91032 | -15.7965 | -46.24453 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8137299-af4f-37f4-b880-badf536a2c1e | -16.28419 | -47.13684 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 050daf5f-2dcf-319f-8173-5a4214e19216 | -18.01843 | -57.56677 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 63b98724-4711-38c8-a4f5-413237d1864b | -16.71242 | -49.75537 | 2025-10-09 04:21:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e4b855f-fb43-3db3-bf7d-c52eae475209 | -16.82827 | -49.37389 | 2025-10-09 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 157280f7-a08d-36fc-b94a-fd77c1ad8cb5 | -14.92986 | -46.7888 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1369b9d-30f7-3f2d-82e4-3612b8450a73 | -18.04127 | -44.97902 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3cc7197-5388-3c6b-800f-e9189ced0078 | -15.28957 | -46.16533 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 766477e9-3f81-3334-94bc-44a1fe950ce3 | -15.31716 | -46.18452 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1492d3f8-ffd2-3674-8a9d-70c9efae1112 | -15.99177 | -46.90423 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7e7617f-b462-32d8-89f2-644860a426e0 | -15.23677 | -46.37253 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c881d5-d07b-3d15-8435-d42d20f088d0 | -20.12007 | -49.53848 | 2025-10-09 04:21:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 93f14b8a-318e-308e-a5c2-cdd062b43747 | -16.60143 | -46.54628 | 2025-10-09 04:21:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82c10953-bdff-3815-87a3-675a545c7a73 | -18.24392 | -55.38265 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 45dccee7-d07e-307e-b4fe-613dd2ce8747 | -15.38814 | -47.32118 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e4a7856-07a7-3a8d-adda-38d8eefbdbf5 | -14.99253 | -46.28449 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 778a5407-e8ca-3180-b67c-33a22cdcfdd2 | -16.19652 | -43.65988 | 2025-10-09 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3477a8c1-67b2-3e02-ba74-47757829db1c | -18.04127 | -44.95469 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3f214dd-b9ad-3130-a462-5916d4fcaea8 | -14.99584 | -46.28504 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9f7153e-b269-3325-ab41-b56eb852baf3 | -15.54625 | -45.2929 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 861165ec-376e-3d50-b25c-81c612af437e | -15.49017 | -47.96683 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 373bbb1e-8fe5-3b6a-bd0e-1448948fceb9 | -17.83532 | -57.64935 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 70817896-01ba-3d9e-9839-0502d4395deb | -17.90302 | -57.66051 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 74fc0fa6-0f9e-3e30-a596-aaf67b077840 | -17.8273 | -57.63237 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 40126ea3-a1c5-3f8b-8e40-ca66672086a4 | -16.29057 | -47.07538 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a67150b1-5b50-39ca-8f30-c90e58191880 | -15.30116 | -46.15631 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d5a2037-7357-3840-a4c0-6ad2a5aa97c3 | -17.243 | -46.91562 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c247fcf-a8b4-3e16-87fd-ecfd305907ad | -17.52335 | -46.7513 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 562984b9-ccbd-3bab-a2e4-5eb108ffb244 | -16.17823 | -45.1433 | 2025-10-09 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7672e98-3d6e-38f5-afa4-4a7c5fc0aa12 | -15.47736 | -47.96073 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 376fcbaf-4b03-3e66-b276-c52e3da3e80b | -16.70447 | -47.58961 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e20e2a1c-d9d5-3ad4-8b92-1c5b511675a6 | -15.06505 | -46.6213 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7529feb6-e73a-3705-8d22-abd5a37435e0 | -16.59551 | -58.16268 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea16ce00-0439-3932-b169-7f1613ad7960 | -18.06975 | -44.42992 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b004aa49-a157-37ce-9b83-e9216101f41e | -16.72671 | -47.61882 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
