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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bf152d6-13da-3c3b-9231-fa76fb27480e | -5.73662 | -43.95417 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e2ea651-fcfe-3f89-ac13-ac7d67e76b06 | -5.75145 | -43.95228 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74af977b-9b4a-31f4-b207-9071db25cd22 | -4.86247 | -47.75206 | 2025-07-28 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dead15d-ccd8-36e1-a03e-aefa5ef5851f | -2.79377 | -49.5942 | 2025-07-28 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1754ef56-f86f-3238-a64d-066cd187530d | -4.16651 | -46.82259 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 2d1098bd-1319-39ed-b382-8f55ed6fe37b | -5.74928 | -43.96735 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66fe9c2c-425a-3ce7-99dd-6c8e5e21423e | -5.85624 | -44.2374 | 2025-07-28 04:38:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 664e2d96-f850-3c82-af74-c9fb449cd4da | -4.11104 | -47.93244 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68cea051-e82b-3098-bfae-75ca8678ebbf | -4.8664 | -47.74898 | 2025-07-28 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 408dc02e-27de-38c5-92a4-eae2a026ffde | -3.21837 | -48.81686 | 2025-07-28 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a2b48a97-4054-3d94-8b55-0c3925681cd4 | -3.22167 | -48.81737 | 2025-07-28 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| effc9d6e-860d-3714-acc0-6bc3bc885f12 | -2.95235 | -41.35835 | 2025-07-28 04:38:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b2be9754-3b54-3522-8354-294b4da5ebd8 | -4.1105 | -47.93597 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cd466f1-d79b-3d2d-a515-a6c5b84c7aab | -4.1671 | -46.81873 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 4f6f10d6-8eb2-3d4b-b949-36fb7895ed54 | -3.39948 | -47.49924 | 2025-07-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da83ba74-fffb-32b5-aea7-294ff9b8432c | -4.30609 | -48.09992 | 2025-07-28 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d12125dc-7396-31e4-a97a-5f11fa3abcae | -5.8737 | -43.25175 | 2025-07-28 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f072ccb-4ae6-3ec9-9be0-cfd27f6d3af9 | -4.15716 | -50.22494 | 2025-07-28 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f963ff2-0089-3182-a989-e5163b99f982 | -5.74565 | -43.96304 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10d13ab3-5dd9-38b7-89af-127dad5fdf00 | -4.30329 | -48.09589 | 2025-07-28 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 016613eb-4b87-3d14-9aa7-72cb8e0c5591 | -3.36429 | -49.16742 | 2025-07-28 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445736aa-81cd-315d-a87e-776ce1907398 | -6.09519 | -42.92293 | 2025-07-28 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 49f64ec5-cb68-3f14-a570-1613274e9430 | -4.15669 | -46.81719 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 281427af-05d7-3cca-b72a-ba1496df0a66 | -3.14092 | -47.01445 | 2025-07-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17e51b27-bd8e-3d24-9de0-af8b40923b67 | -3.36483 | -49.16398 | 2025-07-28 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdc0ed77-6b3c-35f5-ad25-36f4a70d1366 | -4.60392 | -43.31139 | 2025-07-28 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dca038b9-8eb1-3022-8592-6a78102ad6f0 | -4.60025 | -43.3067 | 2025-07-28 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efbbc5b9-8d75-312d-8c63-9dd712265a96 | -5.11074 | -43.78006 | 2025-07-28 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98927772-c27a-34a9-a8f1-207cfc7d4758 | -4.16074 | -46.8139 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1055cc7b-3b96-3a07-8d94-938d12096675 | -3.13751 | -47.01391 | 2025-07-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09bbaa04-b545-3fc3-9c43-72f2faf5be59 | -2.94676 | -48.05015 | 2025-07-28 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0309b59c-5298-3a74-b47d-2ce3751ed12d | -5.74729 | -43.95164 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a72c7c-8f7a-3207-8604-9d39dab9df9a | -4.16133 | -46.81002 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 185f8620-0e41-3343-bef5-cda3af8cf417 | -2.91719 | -48.24083 | 2025-07-28 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1157f08-4488-3ecd-afb4-2a1f55d961d8 | -5.75075 | -43.98667 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eea7e212-1b78-36bf-8da8-d811b13e65e3 | -3.50799 | -49.05247 | 2025-07-28 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13f90bd4-99ba-3156-a926-69502ccc35b9 | -6.09309 | -42.92085 | 2025-07-28 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 958947d4-34a1-3617-9464-5c58af3a9a89 | -4.11156 | -48.1271 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 191c8bd7-94c1-39fb-994d-b1982ddf2264 | -4.16304 | -46.8221 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c6088407-166e-3773-b75b-281378f00f4d | -5.87309 | -43.25603 | 2025-07-28 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77cfea08-294a-3d04-afb9-06358340bc77 | -5.7529 | -43.97168 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4f688db-a555-3165-9520-86f010f35cfc | -5.75344 | -43.96795 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6d13226-77ed-3a91-8255-b452dee980ed | -4.30663 | -48.0964 | 2025-07-28 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 338a9f56-a7b3-3d30-88cb-8769d6c4cd56 | -3.62161 | -49.54359 | 2025-07-28 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cfcb093-796e-3fe4-8e85-131bee4968e5 | -5.74715 | -43.98221 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7a724ee-0465-3dc8-adca-1ffb2a451a7e | -3.13808 | -47.01023 | 2025-07-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a3665e3-9b6d-325a-86d4-90b31b8120b1 | -4.11159 | -47.92889 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac9be958-cfe5-3412-bab2-008b88ccd7c0 | -5.81975 | -43.89285 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6280e08d-b3cb-3517-8ea5-0333dc432175 | -4.16421 | -46.8144 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e8d1d847-14c1-34b8-b7e1-a2d17f7f10fa | -3.82954 | -54.12218 | 2025-07-28 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8280703-7765-36d6-830c-176ef69e3444 | -4.07378 | -47.95193 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfc50f55-3225-39ae-a1f2-09843d8bf8e7 | -1.98538 | -47.97852 | 2025-07-28 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 370b2e8c-8efb-374f-b4a5-b840fa00f71c | -4.19368 | -48.23329 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1181885-ccd3-37ed-affa-7729be5bab95 | -5.87688 | -39.76337 | 2025-07-28 04:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3e73db4-1ec4-3a3a-8541-7f28e3121f81 | -5.74512 | -43.96674 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00319c82-916f-3b09-bec4-eeffaa281ea6 | -5.78903 | -43.6045 | 2025-07-28 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa8c0652-1886-3359-801d-8e3fcc5b2731 | -4.16016 | -46.81774 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 543e536d-b135-3278-ba13-b8eb79333d0d | -5.7415 | -43.96239 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e833294-be0e-3fa4-a7eb-40f2c1fe3695 | -4.15728 | -46.81334 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1119a46a-c9f8-3817-bbd1-69e652d3b0f1 | -3.91055 | -47.82211 | 2025-07-28 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 366bad59-d3ae-325c-9bbb-089b1cad9732 | -4.30275 | -48.0994 | 2025-07-28 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3a5f243d-9f13-31ab-8dd3-6f5353f5c53d | -5.11335 | -43.78068 | 2025-07-28 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7962eb91-5ff4-330d-98d5-5c14eb0c4f77 | -14.3166 | -54.1473 | 2025-07-28 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| bdf7e519-1117-32d4-89cc-21b05db3c10b | -6.5074 | -56.213 | 2025-07-28 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0d4885a3-203a-348c-9b4c-93ce3015e310 | -6.54602 | -56.19797 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69f6fa2a-6831-3557-8b0e-67d9b7602327 | -7.38093 | -44.4816 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d428060-9195-3b39-ac7a-55e783e2d67b | -11.9747 | -46.69843 | 2025-07-28 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37ae6cc0-f9ca-3d97-8345-bbe04a54c9bf | -13.11957 | -47.37352 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13bf6e06-a895-3c82-a773-59f7718d9c90 | -7.11116 | -44.8842 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24ce56e5-8597-3178-8f0c-3facac223386 | -6.49156 | -56.20306 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46ede54b-c332-396d-9047-18e261b83734 | -7.81262 | -44.59552 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfede00b-0488-3b65-b211-5c7c9bcf6ad0 | -8.89166 | -47.34616 | 2025-07-28 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be314e7a-314c-348c-bc6a-511b727b0eb3 | -7.80181 | -44.61286 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 832e98b1-3611-3258-8f82-9b5c132641db | -7.80643 | -44.60976 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20a019bc-b3a2-31cb-94b8-69e1c18ee7cf | -7.17768 | -43.9491 | 2025-07-28 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25899081-f631-3174-b686-626e4e22e00c | -6.49973 | -56.20893 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0ae9293a-ee12-3433-971b-a7cc4ac75c6b | -13.13535 | -47.34296 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae9e144c-70fe-3e27-b724-cba56b3417e3 | -6.38551 | -43.69156 | 2025-07-28 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7aaf7e9-2457-30fb-b32a-c457913d2d8a | -6.25462 | -44.96397 | 2025-07-28 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f8b007b-c54a-35f3-8ff0-3b94c110ec3c | -7.09885 | -44.95283 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aee43f38-06ab-3ad6-93d8-af1b2694c384 | -6.92269 | -44.25219 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e4efe06-852f-3cf0-a9f4-4ce2a8c29459 | -7.81671 | -44.59624 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c68ee8c-7c11-31ae-a4df-13ef180a733f | -7.2152 | -44.16649 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7499a71b-7eb7-3770-82cf-41d0a43b09c4 | -12.72194 | -47.01735 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8be0a7da-cb31-38de-944c-354a24eaabf4 | -10.4555 | -46.5108 | 2025-07-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a63076a3-bae4-3016-9286-316c3b468b66 | -9.02864 | -59.7612 | 2025-07-28 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87648f54-fd14-3895-a142-0200444e72b1 | -6.5379 | -56.19203 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab4c9f98-6da1-31d6-9e8b-628f3b57c70e | -12.73039 | -46.27245 | 2025-07-28 04:40:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b445ac2-50cf-3a74-9022-06cfe36a5600 | -12.74637 | -44.74107 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce5fdca3-6e0f-3e16-a24d-7039a8c0e28f | -7.69535 | -46.04713 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af115101-fccb-3af8-b616-26f5b3ccd5f8 | -7.07244 | -44.91154 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70b2426b-dd21-3d92-b077-bd3ceb8978a0 | -13.07561 | -47.36208 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 706875fd-859c-3a3f-9798-af674f785a61 | -7.08336 | -44.92021 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 973a2f14-7105-3b30-a278-18d9d9116480 | -10.31653 | -54.15891 | 2025-07-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4357fdbb-058b-3ef1-b96b-604f33293856 | -9.02705 | -59.76051 | 2025-07-28 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 287fde6d-7494-38eb-9c78-fc838deb6667 | -6.88903 | -52.8668 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6ec9c5-898b-3eac-8eb5-a564a0226e64 | -6.56971 | -41.51287 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01647320-5840-316a-affa-98b6f1f4a1b7 | -13.1152 | -47.37751 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e123b52-12cf-371f-8b0a-bf7a9d2bb71a | -7.74126 | -51.11651 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39a38e4c-8c3e-3884-a329-478a95543194 | -7.43652 | -44.96426 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
