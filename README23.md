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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa87deb9-2cac-37a9-a4f8-885b09a807cb | -2.50414 | -48.55958 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf3843f-4457-37d0-8155-b7a12bb87819 | -2.50045 | -48.54816 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 675e2415-d893-347b-8af9-5c5a09672e97 | -2.49985 | -48.5517 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dafe811d-8ad5-3026-b00b-f6145132db0f | -2.49926 | -48.5552 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51152774-fba7-396c-97e5-c79a631ee288 | -2.46181 | -47.81213 | 2024-10-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff7900a8-9df2-3cd8-95f7-32ebae512a43 | -2.4504 | -48.67602 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed874c3e-f6e8-398c-87bf-09d5d53a54d0 | -2.44981 | -48.67964 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26b38913-e266-338f-9f13-caed67a64feb | -2.32443 | -48.58188 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a8a51b8-3ca3-3127-bc3b-63d9cc4eb94c | -2.32383 | -48.58552 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4465424-75f1-313b-a4f0-bf337a990dd0 | -2.2398 | -48.01722 | 2024-10-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15643d9a-aac8-3b25-8f40-0bd3e81d1e1d | -2.23397 | -48.01968 | 2024-10-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef8f4df6-8636-31f5-ba86-435439030331 | -2.19803 | -48.35727 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 778cb5c8-cf3e-30e1-8874-7b31ae95a304 | -1.15322 | -49.17053 | 2024-10-15 04:00:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80294f50-78ed-305b-93d3-664409c38e80 | -0.87166 | -48.70303 | 2024-10-15 04:00:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d15aa2b2-8759-3e8b-8d44-2c1ed66ce126 | -2.49943 | -49.0704 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2d040e72-4722-3f5a-ada2-3fe3e0c43cb8 | -2.49881 | -49.07424 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 89a1296f-66fd-3a8a-9b48-f8cb989de365 | -2.47688 | -49.03116 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99477774-22ba-3798-a477-7541020d05d7 | -2.39227 | -49.18895 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 750a0ffc-511d-3e97-a4d8-24aa73c344f4 | -2.3901 | -49.18955 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e19790a9-a1e8-3166-bb86-378b1dacf8d1 | -2.3876 | -49.13278 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fa84ea6-b12e-3ddb-a464-f0780445bf7f | -2.38657 | -49.18799 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91da7b83-bba1-3c82-abd9-b2536c0c26bc | -2.38448 | -49.13142 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 860b33b8-40b9-351e-ac18-5dd58355acdf | -2.38192 | -49.13182 | 2024-10-15 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d5defd4-7d91-3a1c-87e2-e5f94b4edd18 | -7.72612 | -43.19413 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3f64efa0-1921-3c2c-a9d4-b3486fbad274 | -8.98298 | -54.5848 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a77b668f-d9ac-3ef7-830f-ea29d6613da3 | -8.98154 | -54.59183 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4dabf2c2-16cf-35a7-83d9-cee1a32cec9b | -8.97896 | -54.58731 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a0695b2d-7bf9-398d-bb50-f89f130ee895 | -8.97758 | -54.59426 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a9eb0a16-19fe-34a7-ab81-7aac2fa6083b | -4.098 | -42.29057 | 2024-10-15 04:02:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58810308-41a0-3148-873b-08d713d3e040 | -7.18324 | -42.63143 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1b3c9de-fe01-3646-8e62-a6fdda6b41e5 | -7.18038 | -42.62696 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 49922e7b-dab9-3e99-866c-7784790b85f1 | -7.17846 | -42.63869 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 55b7c76f-ce52-35e4-827a-903ea7509b6d | -7.17782 | -42.64258 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2fbdad32-d290-3df9-90bd-326b33465bc2 | -7.17753 | -42.62248 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ad3e521e-0539-3187-8b6a-a1934bf84b52 | -7.17724 | -42.60246 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7808feac-a305-391c-b1af-ee6ebc5d93b5 | -7.17718 | -42.64648 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 51bdd9c6-9257-3aa5-8a4d-bc3f83fe9100 | -6.33044 | -41.91076 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d02f034b-28d4-32e3-8781-504059e82b94 | -6.16904 | -41.84328 | 2024-10-15 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 35a216b7-8860-3485-8422-89683f04a57c | -6.16372 | -41.78893 | 2024-10-15 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6f9717bf-0d79-3849-8fe1-2542c9b5bf30 | -9.25792 | -45.68727 | 2024-10-15 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f9deaf9-17c4-322f-abbd-5534272bf6b4 | -9.25674 | -45.68716 | 2024-10-15 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7a6fc0d-12b6-3bcb-be33-71b18b94c55b | -9.231 | -45.66793 | 2024-10-15 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9d52626-7e61-38fc-bf37-db905baec5dd | -7.94995 | -44.52224 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 560e9287-b224-3623-8848-931b5215300f | -7.47358 | -44.83373 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08c883e8-24a3-330a-bbcf-7f6ea7c7911f | -10.91689 | -44.71307 | 2024-10-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e8f354e-9e4e-3699-a172-01be17d48163 | -10.75739 | -44.83109 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec934a2f-8d3b-3a03-b46a-40633a795bba | -10.7566 | -44.83571 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98e8daa4-5037-3d33-a7ba-f36b7eb9807c | -10.73832 | -44.69648 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f88b241b-ff50-3f3b-aef5-5a9eb921c721 | -10.65554 | -45.17402 | 2024-10-15 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a2aa6d7-274c-3dff-8a7a-46d31820d912 | -10.39307 | -44.81918 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24243c71-ddd4-324c-b023-46c24d2be139 | -7.12883 | -43.91924 | 2024-10-15 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69681838-9831-39f0-92d2-8a3270f3ca66 | -7.12146 | -43.96408 | 2024-10-15 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb94804f-eb0b-3b00-bb28-03254f9f9ba7 | -4.03178 | -43.02875 | 2024-10-15 04:02:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c156976-6d91-35b0-9072-ebe5c0c6ab9c | -4.03108 | -43.03316 | 2024-10-15 04:02:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92846c03-c3e8-36b4-a07e-d5f0e06415a5 | -3.7059 | -42.9319 | 2024-10-15 04:02:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1050a472-59de-3fa1-b52b-5c95953e1b86 | -5.24185 | -42.87484 | 2024-10-15 04:02:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11e58fdf-3f0d-30a9-8586-fc8c848acfca | -5.17677 | -42.77499 | 2024-10-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aba91354-145e-3305-9383-28c37de2bc04 | -6.70028 | -43.05291 | 2024-10-15 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec08e692-c82e-354a-b761-98a1ec348d5e | -6.69312 | -43.05173 | 2024-10-15 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b85ca8a-0f73-3d44-bfd7-12146f061587 | -3.42526 | -43.35247 | 2024-10-15 04:02:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 209cb050-6ca6-3131-a04c-83578cf0e026 | -6.44987 | -43.11666 | 2024-10-15 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04b16e21-55fb-36fe-8bef-87fba255510c | -6.44627 | -43.11607 | 2024-10-15 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4bcf029-7d88-3952-9ba8-e23b679bd9dd | -6.333 | -42.97194 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d82be9b-b93c-3926-80e0-7118c61439be | -6.33234 | -42.97604 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e7d921a-35df-3b0f-9277-c12433d68a91 | -6.31277 | -43.37787 | 2024-10-15 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 97e7544b-27a9-3de7-9efb-49f612d360b8 | -6.29208 | -43.32152 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1f5b20e-399c-3b2a-973a-8b8d75ea4021 | -6.29141 | -42.95643 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d2eecf8-afd4-355a-b282-c77ea3e03b95 | -6.46896 | -43.31802 | 2024-10-15 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8ad5a72-1573-3bf8-b60d-7f0d219f474f | -6.46462 | -43.32175 | 2024-10-15 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 356d1482-c1b2-38fc-89ac-42f602edec2c | -6.43638 | -43.99461 | 2024-10-15 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ff553203-4181-3c6c-8f9c-d58d9371d50f | -6.27306 | -43.89998 | 2024-10-15 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32f96232-5d4a-3e3c-8f6a-a1197e7b62f2 | -6.27231 | -43.90459 | 2024-10-15 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 691d2aad-548f-3d17-9de9-f7f4889d7147 | -6.61805 | -43.66935 | 2024-10-15 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a0b4103-70db-3522-b594-1b2f8d5bec7f | -6.58671 | -43.95478 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12d292d2-1b10-3589-b584-a6946fa6bb7e | -10.84145 | -44.44665 | 2024-10-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76311b73-0175-356e-b94d-4a87404ffbb8 | -10.47349 | -44.06309 | 2024-10-15 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efd5602e-9469-3b26-acb5-dba0a7d1c623 | -10.47279 | -44.0673 | 2024-10-15 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ace3352d-419e-3c96-82e5-403c35154631 | -10.74998 | -44.61304 | 2024-10-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dba1ae4-18eb-37f0-a647-d9015afda2a2 | -10.74049 | -44.70608 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3e4f671-aa7a-3eae-ad2a-ba246d169139 | -10.38959 | -44.82125 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b18873ec-fb82-3e30-970c-002a002f5da0 | -10.38857 | -44.82306 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 373689cd-0465-3374-ac8f-7a94fef3b1fb | -10.76034 | -44.83633 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b6a5abd-a671-36ef-a9c3-79f3f484a52e | -10.75292 | -44.6117 | 2024-10-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73c3d00b-66f8-30bf-b668-54599a8d446e | -10.73461 | -44.69585 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95d364e3-4e69-3015-84a6-200e89293ce5 | -10.72474 | -44.69614 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3eae1e27-0ec4-3e23-ae9b-72234e5c378b | -10.70586 | -44.9739 | 2024-10-15 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8811c5b7-e4c0-398f-9fb5-7808eebe50f7 | -10.70507 | -44.9785 | 2024-10-15 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 192c3e43-53a9-3e36-9099-e2969924f9a9 | -10.5156 | -45.15475 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a260278a-f443-365d-b9cb-51e26966b4a3 | -10.39333 | -44.82196 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6f2e3d25-235e-37e2-8f02-707b33541c27 | -9.45902 | -44.17624 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac28ca85-e352-310d-a33c-8234ee0329fc | -9.45829 | -44.1806 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5f4f7596-729d-35eb-b3dd-9d5d95ae499e | -9.45755 | -44.18501 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 14a18e6f-7874-3bac-8a82-6c106ef7d007 | -9.45678 | -44.14466 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af10b96a-8637-3f5c-a152-db8a3c3e4570 | -9.45536 | -44.17562 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f09db477-bd87-3e5e-80b7-d1a7c65c42f5 | -9.45532 | -44.15337 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 666ade3e-09aa-3712-8225-4487317581ee | -9.45463 | -44.17995 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 730f37cb-2d05-3647-b9ce-26a85ad29a27 | -9.64961 | -36.36405 | 2024-10-15 04:02:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ddcb2c9d-d2d9-3bc9-a7ea-0dfa4bcb5378 | -9.6473 | -36.36207 | 2024-10-15 04:02:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a0aa4df-6ff6-3c38-b287-09716f2ebfab | -9.56391 | -35.69201 | 2024-10-15 04:02:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1552f21e-11c7-38de-aa3f-2c2ab7515b3c | -7.6136 | -44.69647 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README24.md)
