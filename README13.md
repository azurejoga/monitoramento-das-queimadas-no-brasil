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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d88782b-30f0-38e3-b8ff-238b5c437c00 | -10.86345 | -53.7611 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a74165a4-adb8-3c84-b007-7f55bf4c41c3 | -10.92732 | -57.11961 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1c87f60-4135-36db-9336-78d46d093777 | -11.94942 | -58.75804 | 2025-06-22 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 072952dd-9c9e-33f5-9ff2-268babeff4c0 | -9.14865 | -47.15565 | 2025-06-22 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ca4bd8a-996b-369d-b60b-4fa1e9655bdb | -7.87886 | -47.88936 | 2025-06-22 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b004f00-e6d4-39ae-a34a-efb0dcbb3568 | -8.59939 | -51.58373 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c9156ad0-4678-3969-bfe0-b671af4c9fb2 | -13.79196 | -54.29149 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecb0bb5a-432f-31e9-b8d7-d2ac40377803 | -11.61956 | -58.28917 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e169252b-f68c-30af-b2b0-fff45008b5c2 | -8.41406 | -48.29778 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a37db1bc-dc66-31c9-b588-d71ab9556d75 | -11.83406 | -57.76262 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b230794b-c444-3b5b-a243-42f4c6acabf3 | -11.87693 | -54.67231 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0dd92b-d621-3213-81bf-f67d0f88b130 | -12.12936 | -58.18875 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8caaa3a2-2a41-33dd-90a8-f2274546dd04 | -12.5807 | -56.97421 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce70baa4-ff64-30c3-9b00-2ae232649810 | -9.6351 | -62.19744 | 2025-06-22 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79e1d22c-41e1-30f6-b5d9-048d059d0e56 | -8.60346 | -51.58737 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da1d0217-0686-3c56-8886-bd25d93dc3f4 | -9.4596 | -56.0647 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed1d1e56-d21d-3f83-bf64-eed596e44bb9 | -13.80154 | -54.30168 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4c5a724-935c-3632-8715-76722b615aac | -7.16057 | -55.45572 | 2025-06-22 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fd0b555-b63b-351e-9f6a-07204d7bf2d3 | -10.12788 | -51.66314 | 2025-06-22 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7fd6bf0-92f0-32cc-a973-846b4edfd52c | -13.03625 | -53.71215 | 2025-06-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f63b54e9-2ddf-38ad-819e-189f3d6e7d14 | -10.23015 | -54.29784 | 2025-06-22 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c62ed68-a42f-3c71-a9af-437329f7967e | -12.58125 | -56.97069 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f3dcf71-313e-3f0c-ab01-4b47d04dcdc8 | -14.25875 | -45.50407 | 2025-06-22 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52975fb4-0845-3bd8-aabe-7e1363702371 | -9.258 | -57.52836 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cc95b82-411a-379f-a14b-cf11bc96e6a9 | -11.87751 | -54.66841 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1da07880-469e-377d-8011-cfca58a64841 | -11.62292 | -58.28972 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fa234126-3ebf-37e4-818d-1c8fc9618876 | -11.83681 | -57.76672 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca786ff-88d0-3536-9454-47b472d8ec5f | -8.42086 | -48.30071 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 02a09609-f035-350e-9add-aff8a3bdd595 | -9.46912 | -57.84606 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a84e91f6-3099-3841-8911-b3f6fce3f653 | -9.32697 | -47.82371 | 2025-06-22 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d551485-144c-379c-a1ec-c0b9c442131d | -10.93338 | -57.12418 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94c8ccdf-37ec-38f2-bde9-fc8b0a1ed234 | -11.36127 | -55.12595 | 2025-06-22 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25c36484-f851-3d9c-8ebb-6afb348a80a7 | -13.04362 | -53.71324 | 2025-06-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe980b1f-e91b-3f3b-a534-7ae2e050efb4 | -10.06854 | -49.66337 | 2025-06-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37cadfca-1556-3223-b7fd-47d16f8f7535 | -8.36476 | -55.09287 | 2025-06-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e6426b7-9dcd-395e-9566-3f62ab700011 | -9.4675 | -57.83467 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad871cc7-588c-3947-8584-3a1fc37f6d0f | -13.03994 | -53.71269 | 2025-06-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 931368c5-3124-37f7-9b49-29ccd5974b90 | -12.50671 | -58.35464 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a500bde-c3d3-354b-aff6-67185b560953 | -10.74482 | -52.51104 | 2025-06-22 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6913156b-a995-3db8-8fac-9e71ed212e07 | -9.91726 | -59.90674 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13d3d1f6-d047-3fb8-8271-48154104ae19 | -11.10464 | -46.67475 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a90c4d0-df0b-3477-97cb-3772884b4e60 | -13.79433 | -54.30059 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40d3ba1c-00fb-3893-9044-1b7cf30505bb | -10.06878 | -49.66072 | 2025-06-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38325e2-d87f-36b5-9d8f-d7db00c122bd | -9.46291 | -56.06524 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3744389b-6a60-3174-b52b-e8a0e7331d99 | -11.74418 | -54.71611 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae57757f-4b3a-38b1-8c3a-c21b11e582ad | -11.36468 | -55.12648 | 2025-06-22 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace40f84-3674-341e-b0a2-64e73648d98b | -11.87403 | -54.66788 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a8e8e45-2e60-3d52-8d5d-882e43276f92 | -11.79125 | -57.24193 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84a9df89-5aa4-3872-9667-b18776d704ed | -9.47364 | -57.83939 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca8ca887-5828-37b8-8353-ebef58f07f60 | -9.46677 | -56.06227 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0842934-d593-3197-b4f6-75e98f133a86 | -9.92015 | -59.91165 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| af0c4fdd-3da2-3b8f-80bc-6c0c9470d2cb | -12.52198 | -57.23868 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697d72c5-15d9-3bec-af06-eecd89d5864b | -9.25743 | -57.53191 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3781b44a-c423-3e42-9068-2010602db98e | -8.4182 | -48.30398 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45c42404-a555-3610-8b9b-eb57b773177b | -9.45683 | -56.06069 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5e21574-f743-3fd8-a1a5-f16d5401ca41 | -14.25934 | -45.49865 | 2025-06-22 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 808adf94-b5e4-3394-b813-0a4ea2d7c57e | -9.92088 | -59.90737 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 40143817-242e-32c3-a44d-d6aa5abe8594 | -9.39551 | -63.2644 | 2025-06-22 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dce5e00-4c5e-3a4e-91e5-1b0f6be705ee | -12.51123 | -58.34796 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb1b569b-3b60-3285-aa79-0cdc6e9c92b8 | -13.65637 | -53.93852 | 2025-06-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9817add8-b92c-3997-b303-238a70059a5a | -10.52503 | -53.6294 | 2025-06-22 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ece5a60-ba95-308e-8ad9-6b8fac4595b6 | -12.60772 | -48.37784 | 2025-06-22 05:04:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ab9e6e8-521b-30b4-b214-60136364c0f3 | -10.45129 | -47.02382 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57842d3f-5181-3dce-9a62-c2b90198097c | -10.43235 | -51.82921 | 2025-06-22 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d622ece-47f6-3645-980f-b111f4214875 | -10.29276 | -60.54758 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7238aa56-4cb6-3132-b5c0-12f6230d4f52 | -10.93227 | -57.13119 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b6a8850-4566-38e4-9f7b-18f28482e701 | -13.24022 | -56.57517 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c9e3483-3813-3ef0-bfd2-bd4d6be9f331 | -9.46014 | -56.06121 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b647c309-ab13-36ae-b1d4-a890a78990ed | -13.80515 | -54.30222 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a53f9930-7890-37f9-9331-09dc0f3cab4e | -8.42312 | -48.30466 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d67f30fe-ba1c-3874-8ac3-4ed692d28048 | -9.63442 | -62.20127 | 2025-06-22 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e1fb560-1772-3446-8cf2-5c8738ff8376 | -11.78794 | -57.24139 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4d68522-07ef-3c65-873d-16eb22f98b84 | -11.79152 | -54.77872 | 2025-06-22 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6640daf-b004-3a40-88b3-5bef46376644 | -10.50931 | -47.57762 | 2025-06-22 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b73bce8-33be-3fce-83a9-dc54644027f2 | -10.50889 | -47.58088 | 2025-06-22 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4183b66-e257-3857-8bc0-a4ec3b75ddf7 | -10.37359 | -56.29996 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fce137b0-5f51-3372-9953-e68c90a8d393 | -9.4602 | -57.83717 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5082488e-0fb7-3c11-9538-ac389c91a421 | -11.79069 | -57.24545 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7f94d35-6fcc-35ce-abef-e0d5d161a5bd | -11.87345 | -54.67178 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a4b2eb0-5343-3725-b06f-7e07f5d08947 | -11.11741 | -46.66492 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bce7ccbe-0a80-3fb8-bb01-4b9690349402 | -10.28066 | -47.61054 | 2025-06-22 05:04:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c03c0795-0f8f-3386-8888-a7c19bea658e | -12.13052 | -58.18157 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d71ff670-62cb-3fb7-8a12-9573352194d8 | -10.66975 | -56.55483 | 2025-06-22 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c7c55d6-cdea-3db1-b0c1-2eeba835af74 | -8.42578 | -48.30141 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 020e716f-333c-3d63-b850-eec2bc65cb98 | -9.46345 | -56.06174 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4eaf6379-53be-3263-b295-5fe084c7ec80 | -8.59636 | -51.58091 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 52e43f8c-d7e9-3047-b0f1-087a43adf0af | -12.02592 | -57.08958 | 2025-06-22 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c042c594-2e1a-3ed8-90df-a411391075e4 | -11.53028 | -56.98056 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd02ee1a-8a3a-32e0-8fc9-74b3f71ec79a | -9.63342 | -62.20198 | 2025-06-22 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beb8d42f-30bd-3e37-a8ef-d08611d21b40 | -11.87287 | -54.67569 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24609c96-8de1-3575-8763-5fa353439d9e | -11.9556 | -58.76294 | 2025-06-22 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e0ab263-b14b-3392-9b0d-42f532fb9af6 | -12.36468 | -54.47537 | 2025-06-22 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20b883eb-c750-37fe-8490-e1e5fa8fb51b | -10.50847 | -47.58418 | 2025-06-22 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8efa316-9914-3fff-a308-a6580be9a40c | -12.57739 | -56.97367 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44b0e553-b750-3bba-b45c-0ada4ce44e66 | -8.6003 | -51.58152 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b22d2d82-b0d4-38c8-8cb7-7ee5aede3e9b | -9.47029 | -57.83883 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b80302c-c83e-3806-9ed5-d387ddc239e7 | -11.84459 | -57.76072 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11636420-f78e-3ab8-99a6-1a86ebd0ef6c | -8.45341 | -47.00816 | 2025-06-22 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f998522f-0cb3-3360-945f-f16f4125da5a | -10.43981 | -47.02593 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a393d40e-b963-3d9e-9a9a-4c69cc97b06f | -7.87383 | -47.88871 | 2025-06-22 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
