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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1551d462-d949-3f69-90eb-cfd997526dff | -22.17728 | -46.61502 | 2025-09-02 04:19:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f5fe871f-cecb-3c63-b73c-2db759984270 | -23.32064 | -46.034 | 2025-09-02 04:19:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fac61a6f-482e-315a-807d-69e0b44c26fc | -22.10463 | -46.96881 | 2025-09-02 04:19:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49fd31e6-3852-380e-bdbc-d34774c1b66f | -22.67716 | -47.2975 | 2025-09-02 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2af14712-53b0-3b0d-a33b-92b746650fcf | -22.5216 | -46.80151 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03174251-81de-30f7-ba0a-7bb4dfa36dfb | -23.24856 | -45.97442 | 2025-09-02 04:19:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5d514f37-a6de-314f-a306-42430ed658a3 | -23.71774 | -46.36859 | 2025-09-02 04:19:00 | NOAA-20 | RIO GRANDE DA SERRA | SÃO PAULO | Brasil | 3544103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 83fe733e-e065-3d76-925a-3444e1270f46 | -21.8585 | -46.89436 | 2025-09-02 04:19:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6125fabe-1e16-3567-8256-c48a728dd92a | -22.52315 | -46.8133 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baaccdcd-eb69-349c-b386-e1089a476bba | -23.04831 | -49.87618 | 2025-09-02 04:19:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 100b147f-7795-36ac-bbaa-9268cd6e7ded | -23.38446 | -47.2938 | 2025-09-02 04:19:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 910b662f-be65-341b-b29b-0f1cdd9bf878 | -22.52218 | -46.79778 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 25524dd7-914a-3a9c-a100-e69b0459954f | -22.1734 | -46.61811 | 2025-09-02 04:19:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 165ef3dc-b5a1-3d34-8ee5-f89bb3620614 | -23.24914 | -45.97057 | 2025-09-02 04:19:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5367afa9-a846-3e6b-abdb-d440de27a3e8 | -22.10853 | -46.9657 | 2025-09-02 04:19:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ef94725-3082-3660-a532-39a646b1b6e2 | -21.59932 | -48.28011 | 2025-09-02 04:19:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a38ef94-7196-3f37-bc62-b0351a968225 | -23.03593 | -47.17701 | 2025-09-02 04:19:00 | NOAA-20 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 90470ebb-0f70-3508-bef7-0fbcde7ef927 | -23.71369 | -46.39526 | 2025-09-02 04:19:00 | NOAA-20 | RIBEIRÃO PIRES | SÃO PAULO | Brasil | 3543303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| db256f14-7960-36b0-9c23-5e2378e8f8bf | -22.52549 | -46.79838 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9da92b7c-1d56-34aa-b5dd-82a588f98c1e | -22.39623 | -47.18503 | 2025-09-02 04:19:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 53e8e61e-2940-3c9b-a2f7-559c3180a961 | -23.23471 | -51.28673 | 2025-09-02 04:19:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c89d837-f48e-3888-be13-6bd3395f5b12 | -23.22718 | -48.16265 | 2025-09-02 04:19:00 | NOAA-20 | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ca7df3d6-e40a-383d-a796-2e772dc60304 | -23.26908 | -46.88429 | 2025-09-02 04:19:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8c37d3c-b2c5-3e8f-83e2-9d07d7f31762 | -21.6027 | -48.28075 | 2025-09-02 04:19:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3f06fbf-e8d2-34c8-8c42-5a55b16cc909 | -22.9566 | -49.73653 | 2025-09-02 04:19:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f40387ac-8f8b-308b-a114-decb9f042ec3 | -22.52432 | -46.80584 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f6393998-fefc-33df-8e46-3ebc3139ef6d | -22.53004 | -46.81052 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6a872f09-15fe-37e5-92bc-f72dd198d234 | -22.52731 | -46.80619 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 70a35c26-ff53-384c-8658-8a0ca174776e | -22.31647 | -47.80682 | 2025-09-02 04:19:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e8b6a93-b1a1-3aa7-a000-95e7a3013f0f | -23.65468 | -47.4084 | 2025-09-02 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 867ed466-ac3b-3e15-9577-86262fcbe0c7 | -22.78655 | -46.3174 | 2025-09-02 04:19:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 11668cff-2686-3996-ae75-7a7765851301 | -22.54851 | -46.97499 | 2025-09-02 04:19:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f472e764-b317-3683-b4cc-9f2af8521c23 | -23.1277 | -48.16825 | 2025-09-02 04:19:00 | NOAA-20 | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dcede6f6-4a46-39db-99ad-01b646d177f5 | -23.39894 | -47.00687 | 2025-09-02 04:19:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dfd6641b-81d3-3ce9-a104-e3347889975b | -22.52491 | -46.80211 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00a74272-b666-3d76-b8ae-8747df284772 | -22.17397 | -46.6144 | 2025-09-02 04:19:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d36961a-f91a-3b0a-9809-51002e148682 | -23.65136 | -47.40778 | 2025-09-02 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9dbc515f-3795-39b6-afc8-265bbce265d5 | -23.34942 | -47.14833 | 2025-09-02 04:19:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4dcc7bfa-6316-32c6-ae51-6adc8ac33f58 | -22.78988 | -46.318 | 2025-09-02 04:19:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 35f21606-e06a-3ef0-9b43-4af43f9872e6 | -8.9664 | -65.9796 | 2025-09-02 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 0789a67d-ffb5-3fba-a9c7-03b43d7d9db2 | -7.5477 | -61.3247 | 2025-09-02 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 56ecfc50-1254-3c97-9b14-002ed000678c | -3.2305 | -47.135 | 2025-09-02 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5fc7a07e-86c4-332a-b6da-a65b2d7450c1 | -6.7909 | -52.8165 | 2025-09-02 04:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a1d915fa-ceb6-3d84-936e-bf400629a4d0 | -7.5476 | -61.3437 | 2025-09-02 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 951102fb-2e95-39e0-ba42-34642add564e | -7.5476 | -61.3437 | 2025-09-02 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b65aece9-1f2f-3fed-8932-df4eaf3f546e | -6.7909 | -52.8165 | 2025-09-02 04:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d79983c0-88e2-33d7-b614-97f5c29be3a6 | -9.1207 | -61.4864 | 2025-09-02 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 878bcc15-97ac-3964-b4b5-c4b064ebad07 | -7.5477 | -61.3247 | 2025-09-02 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 288ff4fb-2f0a-3d93-80a6-6796707a39d9 | -9.1207 | -61.4864 | 2025-09-02 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 40e63157-f1bf-363f-b4d4-0e8195b6a584 | -7.5477 | -61.3247 | 2025-09-02 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4da16813-07ac-31ce-98e8-6a5946c42dd7 | -3.2305 | -47.135 | 2025-09-02 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 80763770-422a-3d3e-947f-11c16ebabe41 | -6.7909 | -52.8165 | 2025-09-02 04:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e276ef3a-60a6-3032-ac04-448685b2e491 | -7.5476 | -61.3437 | 2025-09-02 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 99e5fa53-19d8-35b1-be0e-4393a0497a1f | -7.5476 | -61.3437 | 2025-09-02 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ad3b6911-91d6-3967-8e07-30e70b964f2a | -9.7294 | -48.9834 | 2025-09-02 05:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 4bc25d3a-6cb6-3e99-ba9a-2e8e4f31d1f2 | -7.5477 | -61.3247 | 2025-09-02 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 46004344-c0aa-3aee-ba6e-3c50649e7996 | 0.47914 | -52.3299 | 2025-09-02 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e0faf84-3cc7-30d4-86d6-a280fa2c12aa | 2.89612 | -60.26414 | 2025-09-02 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 671e007e-e948-3b8a-be7f-8a5344841e58 | -0.75532 | -47.75269 | 2025-09-02 05:01:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f015fe1-be33-3eb6-bdda-d3f704a5a6e3 | -1.97777 | -44.50763 | 2025-09-02 05:01:00 | NOAA-21 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d8ed35a-7226-3947-9b51-35aa7b682cb3 | -6.85906 | -52.81495 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b2c1673-cdc1-3fed-a853-83becbee5a8a | -6.82149 | -52.811 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c26b87-0695-31ef-b0a7-8f8e1dd6c4f5 | -8.05884 | -52.35959 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87d27975-d866-35d4-b340-d24684760fa5 | -6.83769 | -52.8262 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8379ca6-8b32-39f0-800e-69ad2b366eab | -8.05577 | -52.35426 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d53a1668-b04d-332b-bdc9-2c47fb4369e6 | -4.22724 | -47.20811 | 2025-09-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c98c10ce-c19c-3045-b866-2cb200d873bd | -4.48273 | -48.12251 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa1a4ef-5387-3fbd-a592-0caeba12102c | -6.7973 | -52.82438 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d92643d8-eb79-30ab-9fd4-e2a5c230b1e1 | -6.24616 | -60.01573 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73f7e13d-f08f-3fbb-80d1-9e6b267fa90f | -6.85765 | -52.81649 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87d59926-c726-38a8-a196-3cbab0e24e00 | -7.48927 | -47.87775 | 2025-09-02 05:04:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b98462c7-b462-311a-9ce1-851e5e948fe1 | -9.21884 | -47.10951 | 2025-09-02 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a52e4138-3fb9-3363-a701-40dba8d76683 | -9.11813 | -46.04826 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 576a6c73-ef31-3982-8e0d-bc742c14057e | -7.87522 | -47.97023 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d2dcd62-80cb-3d82-af9c-b3e3f2758c8c | -5.7868 | -42.59288 | 2025-09-02 05:04:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3f97c629-67eb-33e7-975d-67a8ea60edf8 | -6.87858 | -45.86206 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6a039c8-1405-3938-bc6f-fb07b46cefd2 | -6.43324 | -55.61303 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4db64cae-55c6-32e2-9352-231cb360def0 | -6.43547 | -55.62045 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd68e8d-22d5-374e-beba-4c60119c5919 | -8.67111 | -49.98646 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20e122f1-c164-3433-ba24-7b3e4fd38f75 | -7.94176 | -46.43153 | 2025-09-02 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c826332e-32e7-39be-bdb8-9eeef90c7602 | -6.85183 | -52.81384 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b0572ed-fc35-3c11-b15e-b4dbdb804480 | -6.86745 | -45.5569 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 28b51bdc-62a5-352d-b049-ceea4db0c4c9 | -6.86213 | -52.78712 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97bae17a-0ed9-30ff-b1dd-5eb0429663fb | -7.48381 | -47.88017 | 2025-09-02 05:04:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03d460cd-3620-3c27-9b61-edbbb5af16a2 | -6.98438 | -44.32003 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5adcce9f-94d8-3f72-bfcd-d5e3145a9044 | -6.22493 | -53.57612 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 849a4779-1dea-32bb-83f7-73ca803583fe | -7.92158 | -46.4549 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34b1d688-a48f-3931-8613-74bee0a5d99b | -6.22574 | -43.36296 | 2025-09-02 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13f12de5-2762-3291-b868-571b549e77ae | -7.06582 | -44.33718 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ead380aa-6e54-3ee9-9492-3fd0844fbae4 | -5.78076 | -42.58558 | 2025-09-02 05:04:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ef65c97a-cd5d-3e30-919e-63d7311a99a4 | -6.43716 | -55.63133 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2282eb88-400c-335c-8466-80064660eb7c | -7.47814 | -45.22102 | 2025-09-02 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c56d5c11-367c-340a-84a9-fa5b40721562 | -6.84618 | -52.81895 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f832f96b-a199-3c34-9dbf-a5e4af7c52e7 | -7.87131 | -47.96382 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff1ca57-04b1-3c1b-86c8-498f5af7e530 | -7.77501 | -45.44491 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4f90917-9990-30b7-a8d3-730c14b3f440 | -8.34321 | -52.53424 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8c17251-92a9-3668-b9d4-497334de74a6 | -6.82811 | -52.81618 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bba5bdb-5be4-37f6-9a28-9f277744b1ba | -7.49862 | -45.34623 | 2025-09-02 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86f58400-d0df-3d93-bd65-952af7301b8b | -6.85544 | -52.81441 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f53209b-6577-3401-8e1d-1c1094ad293a | -6.79917 | -52.81186 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README53.md)
