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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75cb68cb-afbf-3a99-9517-aec783588f7a | -11.0331 | -57.216 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a58d02c-e914-36a9-802d-7d176a6d5148 | -9.6752 | -55.072498 | 2026-08-30 00:55:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05b3ff0f-f118-3053-a773-da89809d8a34 | -5.2567 | -55.908001 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae7a2702-3ed2-3f40-8476-871c8b20b179 | -6.1623 | -53.4804 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcef5d06-fd21-3730-8435-76ebfbc04481 | -14.7714 | -48.732201 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bdc27425-1abe-3634-a989-1ab284207551 | -6.6138 | -55.445702 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58b71cf1-e585-3a20-8d10-f1e46bfd1a94 | -9.1037 | -50.6045 | 2026-08-30 00:55:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e26e8421-2257-38c8-97eb-5ffcfc73865e | -8.613 | -54.7719 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90880f9-ed79-36f0-b06a-360798a392c5 | -7.4157 | -49.739498 | 2026-08-30 00:55:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b43c5c8d-729a-3a91-85df-1141287f74c7 | -10.7567 | -54.052502 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a165c39f-1275-3cee-a8d1-f80c6670f672 | -3.6259 | -60.566601 | 2026-08-30 00:55:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b58e9e3-c3d4-3bc2-a39d-056ee46ba1de | -11.437 | -61.488998 | 2026-08-30 00:55:00 | METOP-C | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb31eead-2992-3421-a87c-8a4b47198551 | -6.1647 | -57.783901 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76440a6-7375-3d18-bd9d-17cfd5c1e109 | -7.5217 | -55.321899 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d13c50-b23e-3d80-839e-bee6d42ef17e | -10.947 | -43.010502 | 2026-08-30 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2fbdca9-441b-3f5f-a2c5-7fcfe7598445 | -16.3482 | -50.992401 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f2d64ac4-35cf-310b-813a-c8aadad20aab | -6.7142 | -58.568699 | 2026-08-30 00:55:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3b1f42d-0058-35b4-a56e-2440d12ac67d | -14.7519 | -48.7369 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd5b025b-7766-30c1-b55b-2b4dcc15b9a6 | -9.9319 | -60.517799 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b29d669-ea9e-3416-81e2-f183a3a27c4f | -8.6223 | -54.721298 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55f566ab-88fe-3872-8fcb-a4b58e12dc59 | -10.7436 | -54.039398 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec9c675b-7c7c-36a4-a754-aafff2690e00 | -6.9413 | -55.717999 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 957ff3a9-a03a-3cbf-9f52-dd6070a3aced | -13.8603 | -54.119499 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96f44609-05b3-3ca6-a7e9-c8ff69632aaa | -10.7549 | -53.9972 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78d3f3a5-d00c-3fd1-8509-676d7cbab075 | -7.0059 | -59.6404 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a368c38-e7df-3e86-a720-4427f5af523d | -3.7693 | -59.3232 | 2026-08-30 00:55:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38bf3fac-9479-397a-9284-0c34d930e664 | -5.4877 | -57.131199 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b37203-e7b5-3478-a0e4-faa3fbb4e8e7 | -5.5092 | -44.007999 | 2026-08-30 00:55:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8f9ebd8-4e6f-35c4-bc85-47853558de76 | -6.3445 | -44.106201 | 2026-08-30 00:55:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2a63c23-bc69-3f57-a189-384016c1de68 | -6.7514 | -55.648998 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a57f88df-400c-380d-84ab-60661efff8b1 | -19.4765 | -57.5499 | 2026-08-30 00:55:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 59205d56-6a21-3782-8f59-5e58abf6890a | -5.4995 | -44.010399 | 2026-08-30 00:55:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b617e5a5-5e15-3387-901c-84c8c42aba09 | 0.2188 | -51.457001 | 2026-08-30 00:55:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8b0a0007-fc9c-3c3b-85e8-9d8ea39edb46 | -8.5541 | -54.784698 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e54326a9-4206-32ad-8171-d6717988ee49 | -6.771 | -55.644699 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5dbfe36-67e2-32b9-8df5-dd8bbde00555 | -10.7525 | -50.8629 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce41c26c-0349-3f5f-817f-c9a9d83c213f | -4.9521 | -55.833698 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b82ef47d-98ba-37cf-ae2e-7d86474984dd | -14.5916 | -53.076801 | 2026-08-30 00:55:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 144cd72b-a1b1-3a08-b63a-a9640e59b5c9 | -10.7477 | -50.841702 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c7210c3-3619-3978-83e9-e4cacffe8f47 | -6.9494 | -55.707699 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90db4f20-e07f-31dc-80ad-06162477d8f3 | -9.6486 | -48.2649 | 2026-08-30 00:55:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c98100c6-350a-359f-bda7-a47913cbb5c0 | -14.3996 | -52.568401 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43b1be2f-c763-390e-97e1-bc8ddd53155b | -23.214199 | -46.978001 | 2026-08-30 00:55:00 | METOP-C | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b03108c-9688-3b2e-8c3e-a5aa147d49ef | -8.6271 | -54.696098 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccceb2cb-3c7f-3b66-b392-f42ddf833607 | -11.4424 | -61.464901 | 2026-08-30 00:55:00 | METOP-C | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd7f6354-c86c-31a1-b717-6404ac894be5 | -23.216 | -46.985901 | 2026-08-30 00:55:00 | METOP-C | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cef39ff-4f35-328a-8c63-5895cfcf309a | -11.2997 | -54.045502 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e74aa4b-a772-39e8-b380-77cd94d57a29 | -15.4568 | -52.803501 | 2026-08-30 00:55:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d12f593-9ff9-3180-97e7-f32e79714dcd | -19.574301 | -48.821701 | 2026-08-30 00:55:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3394e27c-5a56-3b58-bd3a-b9c47a4056bc | -8.7624 | -50.467999 | 2026-08-30 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bff2168-4254-3482-bcd6-8cd5098d77d1 | -10.7574 | -50.883999 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 032be0d5-73a5-30b0-bd6f-9e7e84e9a31c | -8.9428 | -50.801399 | 2026-08-30 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 867ca9d9-01e5-300a-b129-a69e2d03452a | -8.6254 | -54.6884 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee6e1e98-0142-3b53-b0e0-aaec250aea51 | -11.1617 | -51.299599 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f67bcd53-ab4a-31d6-9962-712ace1cea89 | -9.1995 | -51.558998 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f6fccd-6b77-3742-975f-7dd9cbdb36a4 | -10.7747 | -54.0406 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b394c60-8f19-3706-9562-0954878b99d4 | -7.5514 | -61.306801 | 2026-08-30 00:55:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 299e4cbe-d356-35eb-a225-7d7ebfdd01fb | -13.8568 | -54.103001 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f81b22a-6d04-326e-b400-7163cfcd0c91 | -8.6113 | -54.764198 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85a367e-5a73-39db-80c9-84e1d2a6e7ae | -12.2316 | -50.518902 | 2026-08-30 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfcfa2b9-13a6-308c-86ea-d9a3543bfdb6 | -4.6974 | -55.661499 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4b19fe-49ed-3230-94aa-af03e72c7046 | -14.8993 | -47.741402 | 2026-08-30 00:55:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a523ef8-fd06-3d19-8f1c-50858dded93b | -13.841 | -54.0289 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e05e845b-954e-398e-9dc0-e3740b87de9b | -11.0355 | -57.2272 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6273ace2-449c-3646-8667-2784f6ed3bf7 | -10.1404 | -45.698101 | 2026-08-30 00:55:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6f96a60-dfab-3d97-a4db-f96c38e01843 | -6.7808 | -55.642601 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 932a7fe4-7c59-3e17-bf4c-4d58e669a4c1 | -4.6894 | -55.671299 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3aded28-17c7-35a7-9f2f-4a41d85b3f9e | -11.827 | -51.050598 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 540448a6-ad4b-3d22-a368-0acc24523874 | -8.22 | -54.947201 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 452d8b68-d841-32ed-a26e-26933753c5e5 | -5.8754 | -52.087002 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16aebfcf-6264-3e38-a2fc-a7137ba3d5bf | -14.4403 | -52.567001 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86cd34f6-b805-36a4-adaa-53bfa5d6c449 | -6.3748 | -51.746601 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 149b90a8-22c0-3ce8-a730-b1ad875b34c0 | -11.1649 | -51.313499 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bbc9509-3a1c-323d-b006-0d51b0722fbc | -7.5004 | -55.318298 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ace576d9-225d-32c7-8ae1-736c2a1762c7 | -5.9647 | -57.666302 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38128512-7e0d-3396-b862-1b712702e82a | -9.1642 | -59.496101 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c80b71b-2fb6-39fa-be89-1f7652d27b1c | -9.6707 | -55.099201 | 2026-08-30 00:55:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16b75fe3-4dad-31ea-bd83-c19a3b49376d | -11.8302 | -51.064602 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a54d0f5-2d0c-35da-a845-288a738350fe | -4.0873 | -54.100899 | 2026-08-30 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d5b6c77-2d7b-3ac9-bc16-69b5597e8e38 | -5.8749 | -57.770802 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19aa2e2c-a157-3b7a-9575-753eafea76f3 | -9.2062 | -51.542801 | 2026-08-30 00:55:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93875b44-41d5-3c06-ab5c-ac11ff55f67e | -14.2491 | -54.6525 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbebc623-329c-3b1b-a25d-3c523968a80e | -5.8771 | -57.780998 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841ec21c-bfa8-3bf4-ad69-948ba9708fe1 | -5.6102 | -44.126598 | 2026-08-30 00:55:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f39048f-3a64-3b1e-8c4e-92704e8a2568 | -6.755 | -55.665199 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bccb502-cb29-3031-8bb0-1e172564960d | -10.7503 | -54.069901 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd66599-f912-3ecb-b994-a2f2194e2258 | -6.9476 | -55.6996 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4228a085-abe4-3594-ad49-6c4d16a7df6e | -11.1879 | -55.094299 | 2026-08-30 00:55:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad199604-779a-3aaf-a558-da8f01782545 | -3.7621 | -59.337299 | 2026-08-30 00:55:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36a382b8-91b8-3b12-882c-7d3af4722068 | -6.747 | -55.675301 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f02f92d-f5d5-3a8a-b8da-a328b7e8f9bd | -6.7782 | -55.676998 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f81efae2-c107-31cf-949b-00e4aa20399e | -7.9491 | -52.452099 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0aec4dc-0930-3787-a626-2ddc934fbcb0 | -4.9619 | -55.831501 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1408e94-0cbe-3b54-b2ce-a944c397ea6c | -10.7565 | -54.004799 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 973346ae-749a-371f-a4ad-134097b5d669 | -6.365 | -51.748798 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2689d124-b1a9-38a7-ad4c-1c5c63085186 | -3.4919 | -54.6558 | 2026-08-30 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eaa7181-c22b-38b1-bb2d-41eb948ccbee | -7.4968 | -55.302502 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec47b691-f106-3e9f-a26e-a113528556fc | -6.7116 | -58.5569 | 2026-08-30 00:55:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5f14454-a4bc-3f02-95b0-0e6f7d87a80c | -6.9574 | -55.697399 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637e3262-3f2c-36ac-9922-13061277989d | -7.487 | -55.3046 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
