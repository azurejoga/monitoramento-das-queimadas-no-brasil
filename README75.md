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
| 43b15c92-c58a-3771-aa0a-0d1d27e5bb88 | -5.86977 | -57.77362 | 2026-08-30 07:50:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| f816b880-fe0e-3dab-b9dc-5a416a2e8d39 | -7.51559 | -55.33268 | 2026-08-30 07:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ab469576-4e09-3a64-8f76-f737de4ad131 | -5.87478 | -57.76 | 2026-08-30 07:50:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1849fdd7-c5f1-3336-b212-bdb026cc0864 | -7.29644 | -60.58848 | 2026-08-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 12bf4cda-6a3e-3a38-9eca-c36b1cf6d1e6 | -9.05682 | -65.41742 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3897efe2-eb83-39f9-9c4a-eb04f9698fce | -9.15103 | -59.5054 | 2026-08-30 07:52:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 274b18e0-1109-3a90-aa83-a9fadbb9336a | -9.04799 | -65.41607 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a7e6d00-5e80-36b7-92e8-a149aeae8d84 | -9.88579 | -60.26793 | 2026-08-30 07:52:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e6e5caf4-5e13-30cb-a436-37c2e35aec3e | -10.48112 | -64.50494 | 2026-08-30 07:52:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 14d7e923-81ba-3100-a6e4-b47c99571028 | -9.01086 | -65.40465 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a4173bcb-9fdc-3f48-be58-bb8a166ad825 | -9.04937 | -65.4071 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 15e4099c-0331-37e0-9b14-87dd58c4b197 | -9.93312 | -60.51946 | 2026-08-30 07:52:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ca09aa60-cdb2-36dd-8ed2-9a2173466519 | -9.89672 | -60.26939 | 2026-08-30 07:52:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7031fcf8-de1d-3f74-8f14-f4d2e8c49dd9 | -10.48093 | -59.60958 | 2026-08-30 07:52:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 765017ae-eff4-378a-9f2d-4f81743a9a68 | -8.94688 | -62.37465 | 2026-08-30 07:52:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5863f545-4e61-351a-95b9-3e07b0b91b1b | -8.90914 | -66.95396 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b57285f4-5b6b-3e05-8201-62c30e929109 | -9.01223 | -65.39568 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 15eba326-8f77-3d80-bb8f-d35702cc3204 | -8.57825 | -66.95052 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 21cce4a2-5e47-3370-b560-e0f46240df09 | -8.9281 | -67.36002 | 2026-08-30 07:52:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| dd7dd0b2-972f-3af4-b9de-9e0ef4da7936 | -9.0582 | -65.40845 | 2026-08-30 07:52:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9d39123d-af75-39cc-98b7-abc31663eccc | -10.49033 | -59.6017 | 2026-08-30 07:52:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d7e19a2f-55f1-3e68-a0e0-73bd68746ebd | -9.88387 | -60.28213 | 2026-08-30 07:52:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| b85f74eb-fb88-3eaa-a7e7-3050f9a8187c | -14.4197 | -52.5413 | 2026-08-30 08:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 452377aa-da75-31b2-9dc1-076849939ee2 | -14.4193 | -52.5625 | 2026-08-30 08:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e2d511f4-3c0f-3af6-b70e-7e1ec0a3f196 | -4.9604 | -55.8424 | 2026-08-30 08:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4458be23-9bb9-3d94-8c5a-baea1601dd6d | -9.8927 | -60.2752 | 2026-08-30 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f1390f7b-14a3-366f-b5e1-09d2cfa377a3 | -7.5136 | -55.3251 | 2026-08-30 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 92218bbf-075d-30f1-8784-caa2a814ba8d | -14.4197 | -52.5413 | 2026-08-30 08:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3dd5f840-9339-38ed-8d4b-f6989cfbf596 | -4.9604 | -55.8424 | 2026-08-30 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 91e5289f-72c5-3a9b-a7ff-0409f3384477 | -9.8927 | -60.2752 | 2026-08-30 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 79bc6de6-25b8-37f6-83d3-7e6f08caf2a4 | -9.8927 | -60.2752 | 2026-08-30 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 373621f3-9041-3d93-a249-1d401cc82f4e | -11.1534 | -51.296 | 2026-08-30 08:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2495d012-39f9-3889-a5d4-589c21134cc2 | -4.9604 | -55.8424 | 2026-08-30 08:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4208ef79-d173-3ab8-805a-1fa800ab3241 | -14.4197 | -52.5413 | 2026-08-30 08:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 63a25887-78cc-3d1a-aed1-ac9aac0f1395 | -4.9604 | -55.8424 | 2026-08-30 08:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1464a65b-783e-3322-be17-5d7fdd13886f | -9.8927 | -60.2752 | 2026-08-30 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d36e1915-727c-398c-84e6-8f481071668d | -14.4197 | -52.5413 | 2026-08-30 08:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2c1ec5a3-2939-36e8-a6b0-e721692bd7e3 | -4.9604 | -55.8424 | 2026-08-30 08:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 72376629-4abc-37b0-ab62-38d8e1e67597 | -9.8927 | -60.2752 | 2026-08-30 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bbc23d7d-8078-341b-a438-684a3d768d8e | -9.8927 | -60.2752 | 2026-08-30 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b49df1d0-4597-3ee0-b6e4-0ad08e47cc09 | -4.9604 | -55.8424 | 2026-08-30 08:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| e943c797-af61-32ca-9659-65777aa529c0 | -14.4197 | -52.5413 | 2026-08-30 08:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0ede88ea-fa95-3488-9a2f-dfac47809158 | -4.9604 | -55.8424 | 2026-08-30 09:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 68d4b1e1-410e-3279-aecd-7ff481272874 | -7.9422 | -44.277 | 2026-08-30 10:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| b0b6f174-3ca6-380b-aba2-39cb7e454f75 | -7.9422 | -44.277 | 2026-08-30 10:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| a9d21256-2604-34b2-a1a0-242107848a38 | -7.9422 | -44.277 | 2026-08-30 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 286.4 |
| fd0b1aa8-2956-3624-a12f-0d0931986162 | -8.1537 | -45.4677 | 2026-08-30 10:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 5f11898f-a35e-332f-b2b8-d91160367b15 | -8.1534 | -45.4904 | 2026-08-30 10:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| eb746fd0-151b-352e-a631-9c640cd5c623 | -8.1348 | -45.4696 | 2026-08-30 10:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 538c11c6-ef45-3cb4-a266-9454a6cba0d6 | -7.9422 | -44.277 | 2026-08-30 11:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7c164f85-f5f6-355e-96f5-347814623835 | -8.1348 | -45.4696 | 2026-08-30 11:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 507782a4-b3d3-3003-9dca-d5ac2ee070ab | -7.9422 | -44.277 | 2026-08-30 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 355.2 |
| 2d3166ff-c168-385f-bec4-978a9d2cc9d6 | -7.9425 | -44.2538 | 2026-08-30 11:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 45caae45-9eb0-3ff8-b9fb-cfaa9723ebbd | -10.1538 | -45.6982 | 2026-08-30 11:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4ef1a388-73d8-3e73-98cd-424543686d8f | -7.9422 | -44.277 | 2026-08-30 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 28e55429-89fe-3b79-a445-af6b16e42120 | -14.1649 | -52.8058 | 2026-08-30 11:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 49c57b10-af83-360e-9b98-9e0d3cb5215a | -14.1456 | -52.8082 | 2026-08-30 11:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| a26c3aa4-2ef7-3fb8-9b76-0bb78f626b41 | -7.9425 | -44.2538 | 2026-08-30 11:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 6644f49c-e24f-345b-a609-84d47d0c0545 | -7.9611 | -44.275 | 2026-08-30 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 84ca9a4d-4d89-3680-8d3d-67712c18a7f7 | -14.1456 | -52.8082 | 2026-08-30 11:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 64f5cd04-c837-3545-80b3-432e565a944f | -7.9425 | -44.2538 | 2026-08-30 11:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7820238f-4d9d-371b-a13b-0c190808c895 | -7.9422 | -44.277 | 2026-08-30 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 2f3a6568-30d6-3539-bb63-268c3e78321d | -2.00222 | -44.79357 | 2026-08-30 11:30:00 | TERRA_M-M | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1dc7dfcd-8982-36bd-b442-9cf340241ae3 | -2.95364 | -43.76378 | 2026-08-30 11:30:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 301b6505-36cf-378c-b5c5-6db7ac4d1204 | -3.68886 | -41.78122 | 2026-08-30 11:30:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ea3aa414-640a-37a8-9608-11a237ad41ad | -3.68758 | -41.79028 | 2026-08-30 11:30:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 2da387f7-8364-3fc5-81be-e40cd6633747 | -3.67144 | -42.55721 | 2026-08-30 11:30:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c3aca087-50f4-3fc5-b2a3-f749b6a70427 | -8.8531 | -46.69506 | 2026-08-30 11:32:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b006c49b-d689-3397-ba1a-c3ae6d47287c | -6.24519 | -39.2124 | 2026-08-30 11:32:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 1a68bd0b-44c2-3d4e-94e8-122cfa83ba48 | -10.78851 | -45.32852 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| b481cb56-5ea5-38e2-9429-fbaa891d5559 | -10.15134 | -45.7094 | 2026-08-30 11:32:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 996176a6-cfd1-3179-a963-cc5e06b714dd | -7.944 | -44.27787 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e63b6695-7195-3337-a520-bfed8b84e269 | -11.36608 | -45.16255 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c9c0fc0c-0540-36a2-ba82-ad8ef10c6db7 | -10.75227 | -50.85044 | 2026-08-30 11:32:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| efa0cb5b-7250-3fe1-9b52-d303e1349c8d | -5.52644 | -39.86715 | 2026-08-30 11:32:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 17e985fe-7323-32a5-a339-0a8650dcc132 | -10.82289 | -45.34296 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 0a26a02b-144d-3741-b3fd-2138bfd074cc | -6.86285 | -41.68222 | 2026-08-30 11:32:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| f3f3e317-b860-342b-97dc-76a5a1e95f46 | -7.94271 | -44.28675 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 436e823b-7181-39d7-917c-47554b297b8f | -7.4466 | -43.88949 | 2026-08-30 11:32:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 45818e83-6810-3a00-81d7-84b40fdb7985 | -10.77181 | -50.65271 | 2026-08-30 11:32:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 79aab9a6-95ae-3968-9c65-c9f167c8a4f2 | -7.94658 | -44.26005 | 2026-08-30 11:32:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| aafa5704-41b8-31a6-a7ca-227aff9c6ae0 | -6.86551 | -41.66297 | 2026-08-30 11:32:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 43.1 |
| 21b93929-652c-3582-9cfd-fd00ea434b35 | -11.36477 | -45.1716 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 02f9cd26-11f6-3f22-9fe9-b7daa3462d10 | -6.85375 | -42.87165 | 2026-08-30 11:32:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 15253319-4c79-3ec1-9b7d-254de62b6603 | -10.77824 | -45.33637 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eccb2ad9-f506-337b-afa0-ea47dace1c38 | -10.48273 | -42.41199 | 2026-08-30 11:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 590e7462-e569-3f1a-9c98-fd6e6d4102c0 | -10.82555 | -45.3246 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e9bedf4b-21ae-312f-bff5-bb21cce20b6c | -8.41192 | -44.99019 | 2026-08-30 11:32:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 63b6ba8c-bd4d-3ff5-8a22-f89dcb241c9b | -10.76358 | -44.86555 | 2026-08-30 11:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d491be3c-b773-3148-8817-6ef9b338e7e3 | -10.78984 | -45.31937 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 44409ab6-6138-32f7-9fa5-0dde8968f767 | -7.95414 | -44.27022 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 36e7f6aa-d864-30f3-997f-2fe68e988259 | -10.78717 | -45.33769 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 867c812a-0fe9-3666-b92a-9514f8b8b5db | -7.95285 | -44.27912 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b17279d7-3f00-3bc7-9239-fa8ddc981ad2 | -7.98552 | -45.50646 | 2026-08-30 11:32:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28bfadaa-13a6-3dce-b030-c9de702214c2 | -6.87913 | -42.88424 | 2026-08-30 11:32:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 815dc602-da66-359f-9179-29501d0f026d | -11.34833 | -45.15996 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bc6d7c27-af8a-3395-ab47-33571b416692 | -9.45064 | -45.64436 | 2026-08-30 11:32:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d6024d08-79ba-3b79-98cc-0d66c7a2c745 | -6.86419 | -41.67257 | 2026-08-30 11:32:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| ed37d9b8-a8b8-3f31-a4f1-0c84a549c00f | -7.04899 | -42.19958 | 2026-08-30 11:32:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5c999249-2d4a-3f09-85cf-52a10054820f | -10.80916 | -50.50323 | 2026-08-30 11:32:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |


[Clique aqui para ver as próximas entradas](README76.md)
