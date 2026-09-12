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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ed762a9-a1ff-3219-a93c-21143348d37a | -4.52502 | -37.73261 | 2026-09-12 03:49:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 29a76f2c-ab4e-33c4-90c1-29bb025f0f4c | -13.45535 | -48.51139 | 2026-09-12 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b891fa1c-835a-3345-ace4-88d0b72d2fd3 | -11.369 | -46.80035 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52974881-fe69-3773-a97c-66fc1c18de0f | -14.58763 | -48.84403 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 722326e1-e682-3d38-93a0-ff5d8e144944 | -9.93194 | -48.52414 | 2026-09-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 915f0334-5011-3e4e-93c7-09d7d9cd7e32 | -3.51261 | -40.35989 | 2026-09-12 03:49:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| da172307-7ec5-330f-95bf-234d33da5912 | -10.21989 | -45.19225 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5eb8048e-5ae2-34ef-8b9e-df24e9da152b | -9.31744 | -45.64451 | 2026-09-12 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d43c0a2-ecc4-3110-8d88-adf5e22a3ae0 | -10.36685 | -45.12803 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46d250c6-c5af-379f-9271-315bdb9bbf42 | -8.38778 | -46.30559 | 2026-09-12 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0245d52-1727-30d6-91d2-56ad340ab56b | -9.51766 | -40.33256 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| c548561f-8e61-3765-8fac-70e105c5ae1c | -11.40663 | -43.9432 | 2026-09-12 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df39c728-54a5-3f1e-9f4f-4db224c3d7be | -12.64309 | -47.0974 | 2026-09-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52aff647-57a4-3e41-abfb-7cc3498e2e23 | -3.23223 | -46.95497 | 2026-09-12 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 87fd639d-18d0-3e50-bcdb-6d27eb402322 | -10.55805 | -45.69645 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19793597-8534-355a-8be8-f96207a8ee91 | -10.21744 | -50.36937 | 2026-09-12 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f94b818f-f8d3-3880-8dc6-b9e8c6d9e795 | -9.36815 | -48.42295 | 2026-09-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edb70292-3602-37e8-a5bc-a7651338a6da | -9.4614 | -50.32202 | 2026-09-12 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc5101e8-00ef-3eb8-8ef2-a77da1d789bf | -12.7378 | -44.74305 | 2026-09-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b110a4-0e64-3545-9b98-47f377b634d6 | -9.31071 | -44.36496 | 2026-09-12 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55c86fa6-280a-39ec-bbf7-4d2d4f58f402 | -10.05091 | -46.26713 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ecfe8e5-026f-3bcc-b1cb-338a035484f3 | -11.37184 | -46.83486 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c867f419-916b-3d2a-99b1-2592554ef698 | -11.35147 | -45.79599 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cca45c2-1d1d-3392-bc1c-50e5efefa859 | -10.54931 | -45.22424 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 67994493-aef5-32f7-a851-c2e2d7cd5014 | -13.412 | -42.48812 | 2026-09-12 03:49:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ff3c9bb-c68f-38a9-a609-e9ec162e51fc | -9.79981 | -43.47584 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 119c4f1a-59dc-33d7-8efb-66c789432102 | -10.2136 | -50.373 | 2026-09-12 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86d4a59e-03a5-3cb5-a9d9-9efef69524e2 | -10.2814 | -45.26929 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2ff07d9-17d3-3f7b-95d8-b6cff24fadd7 | -11.79818 | -46.38712 | 2026-09-12 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6995d6d4-52fd-30bb-a4f3-e59d78416191 | -13.46371 | -48.50144 | 2026-09-12 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8459561-e5c5-3e7a-91ec-1f8d5ce82826 | -11.38602 | -43.97582 | 2026-09-12 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73489fcf-94cd-3655-8225-f9d44396b5d7 | -11.35671 | -46.28382 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d80911a-aae5-32f8-84ea-2382d27c539d | -13.41274 | -42.48406 | 2026-09-12 03:49:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2812fa1-b4eb-30d5-8040-3a5482e3a0aa | -10.90665 | -47.84134 | 2026-09-12 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bfb393b-5dbf-300d-ba32-0b92400b22d7 | -3.73565 | -40.42998 | 2026-09-12 03:49:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d7b3268-8d76-3989-ac8d-4678b5959e86 | -10.55803 | -45.20613 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3122c3-eff8-311f-96f3-132229214f4c | -14.11789 | -44.21928 | 2026-09-12 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16578193-91d0-3548-92c2-50c5f65f4cc3 | -10.55225 | -45.20844 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b188619c-64a2-3c8f-b2b6-321925e540e0 | -4.29688 | -38.53022 | 2026-09-12 03:49:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 423fe0e5-97d1-3619-b770-d5d2e6f6c9cf | -11.37331 | -46.83791 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 537351dd-ba44-3df3-bc56-58605579730c | -10.43555 | -42.74276 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06c8ee3e-11fb-31fa-a3f0-67ada7328626 | -9.59934 | -40.36156 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ce87ab4-01f9-384f-b6d7-b23940792694 | -11.3741 | -46.83393 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 85ac9ee8-4a11-35d9-87c5-4278629476d6 | -7.9645 | -44.00291 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c72abc4-3aec-3adf-bc01-376790338516 | -3.22573 | -46.95372 | 2026-09-12 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| bd18fc48-d754-3aff-a6c9-653f3c2e5ce1 | -9.67446 | -46.01295 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b74726c-d4ed-368c-b1f0-f67e2fa03d03 | -14.90372 | -47.75535 | 2026-09-12 03:49:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96f49fa5-7fa3-3055-80ff-5ecbd2a914cf | -11.35701 | -46.28446 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 716fcc4b-3aa1-3a4c-b521-3879c63061d4 | -9.53409 | -45.45192 | 2026-09-12 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b87619d6-358e-3b93-a1f7-9ad4aff23daf | -9.70037 | -43.39813 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0f4db72-0fff-35e5-8833-881c307d18d8 | -9.74251 | -41.87398 | 2026-09-12 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0428def1-323a-3d4f-b3a7-c26aa804e53d | -12.13159 | -48.97768 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69d3d686-203f-3a6d-92ea-1afa095aa4ea | -10.63033 | -46.12644 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25c99130-3877-3c1c-b8d8-671021404e83 | -11.36975 | -46.79655 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45cdf220-eba7-3885-b58f-805d511d67a2 | -12.85177 | -44.3964 | 2026-09-12 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4819395f-e4f3-34cc-a319-efda18387821 | -7.60732 | -46.1266 | 2026-09-12 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5146eda1-34b5-314e-ad25-4b4df9160a3f | -11.3504 | -45.79228 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c234de4c-5e5d-3e7b-8f7e-1871f73e9d97 | -14.91274 | -44.66869 | 2026-09-12 03:49:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87d8b15e-f503-3e54-9c17-62e9b841fa02 | -12.12896 | -48.95779 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b90908d-5425-3f0b-8fca-a65b4f6da610 | -11.3726 | -46.83086 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 444fe83c-5871-3158-ac1a-f640766211b5 | -7.97106 | -43.99498 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f9825a2-c345-3f3f-b4bf-19a1b9ffeef7 | -2.7148 | -57.6274 | 2026-09-12 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f36a184b-6570-32d5-ad09-705685a599a6 | -2.9395 | -50.3994 | 2026-09-12 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 78c10c2f-3308-3b23-bc87-889632185c39 | -2.7331 | -57.6465 | 2026-09-12 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| f2e1237c-9d8a-311e-a893-2787a16e8d3d | -2.9394 | -50.4203 | 2026-09-12 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 66bb42df-af62-3af4-8bc2-90b610220628 | -2.7148 | -57.6469 | 2026-09-12 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 590431fd-7974-35fa-a054-fc1f78a05a76 | -2.7331 | -57.6271 | 2026-09-12 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e8e44b9a-3e71-387e-afbf-2ffb0dd32bfc | -10.7015 | -54.1663 | 2026-09-12 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f0305db9-6140-3f39-93c8-22c9eefaac55 | -10.6827 | -54.1679 | 2026-09-12 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c990dbe7-2daf-3ef4-a0a5-c78e2761dc5b | -18.93572 | -46.82884 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82bc7b90-42f5-31e7-8618-f66403dc175e | -16.03119 | -47.90436 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66f7a84b-0dd0-3100-9829-d960dcb99c49 | -18.64187 | -47.2906 | 2026-09-12 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c8d647d-54b7-334a-a8ff-a515151b5f71 | -19.58001 | -42.91453 | 2026-09-12 03:51:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d818daa-f754-3fb0-a88d-a5fce7bc604b | -19.87152 | -42.63728 | 2026-09-12 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 597dd60c-c749-3f91-b272-774e3d5f3f68 | -18.40815 | -46.05527 | 2026-09-12 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7169b484-dd47-3fec-af2f-c2bcbc772790 | -15.01901 | -48.50882 | 2026-09-12 03:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdd76044-a9ed-3284-ba1e-de33667ef287 | -20.27597 | -44.70209 | 2026-09-12 03:51:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dac5f718-9bd3-388b-a6e2-3ffdd3b21815 | -16.54216 | -41.04055 | 2026-09-12 03:51:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9e363235-0c8c-34b5-bcdc-1b881efdeda9 | -18.03576 | -42.54561 | 2026-09-12 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c5a159cd-5ca0-3317-9821-0a22822ec91c | -18.64716 | -42.83157 | 2026-09-12 03:51:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f236222f-ab3d-37c6-a779-26c47ed34173 | -16.35102 | -47.34887 | 2026-09-12 03:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f334e8b-b50b-3704-a145-86d193254134 | -16.03524 | -47.9127 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 944cbd89-dccf-3367-80eb-05985a22c6c8 | -18.66805 | -42.00758 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| e2b50358-75ee-3171-9e02-fdd3c217dbfa | -15.01716 | -48.50729 | 2026-09-12 03:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1fbaa341-8147-3fc9-8ab3-7e934b5593d0 | -16.62506 | -41.92206 | 2026-09-12 03:51:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c02ced20-f42d-3759-a8c9-20e113331910 | -18.93692 | -46.82295 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a3848da-1c92-327e-b6b7-c5d2814d7c61 | -18.65857 | -41.99651 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c945513f-bdb9-307b-8335-423c9f7feeb6 | -16.02627 | -47.90846 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f6df714-0647-3736-b05e-9ab71b870d8c | -18.66514 | -42.00246 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 7505ff21-7644-3d03-8765-60b83959295a | -15.01418 | -48.50242 | 2026-09-12 03:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18240316-d2d6-36aa-9006-ca500ae13d19 | -18.66593 | -41.99799 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 61a5419f-81dc-3353-9c15-e6aa02bf5e52 | -18.86694 | -40.23895 | 2026-09-12 03:51:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7dbf8fd-7e48-3011-9eec-9457bfacca51 | -18.70207 | -42.62052 | 2026-09-12 03:51:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4a5a3d5c-d589-31e5-ba61-b467a7c3213d | -18.6462 | -47.29532 | 2026-09-12 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55b25c01-10fc-3765-8544-89d307bdc4b1 | -18.7297 | -45.02686 | 2026-09-12 03:51:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0277fbe-04ce-35b3-92b5-08d0bbb89403 | -20.37665 | -40.59521 | 2026-09-12 03:51:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 370a345e-8ce1-31e5-a844-6bd17c96fa8f | -18.41288 | -46.05627 | 2026-09-12 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1af63874-17a6-3ea7-85c1-98108db68231 | -18.87891 | -46.98039 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f09a5923-3d05-3442-9b63-1eb4531ce263 | -17.10365 | -51.26136 | 2026-09-12 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0db2f121-aa18-36f4-8fe9-b45583d25005 | -18.41653 | -46.06269 | 2026-09-12 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
