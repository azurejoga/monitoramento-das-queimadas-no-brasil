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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c5b7aa3-450c-38ed-ad19-0c217316a6ef | 3.2554 | -60.8004 | 2026-03-06 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 67d40d6d-6759-3d38-9924-5437db415534 | -21.2984 | -49.3193 | 2026-03-06 00:00:00 | GOES-19 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |
| 4f470d23-ee7a-3872-acd9-40cca3f0c8ad | 0.1367 | -60.412 | 2026-03-06 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 979918f6-a7fe-3b52-9464-71c7dd12fad4 | -20.30308 | -49.58637 | 2026-03-06 00:02:00 | TERRA_M-M | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| d6902f14-570f-3553-8610-7c0d9d247dc4 | -20.30461 | -49.59299 | 2026-03-06 00:02:00 | TERRA_M-M | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 02a38153-6f20-3d07-a20e-12c6e3f794f1 | -21.30169 | -49.32248 | 2026-03-06 00:02:00 | TERRA_M-M | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| d3cc1a00-5c36-371d-90eb-aba2ee3fee9a | -22.92879 | -48.61035 | 2026-03-06 00:02:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ba22e819-4ad5-332d-95a5-b9cf08604c63 | -21.85409 | -46.99044 | 2026-03-06 00:02:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 027dae37-cd55-3045-b6a8-659cda2a9bb7 | -20.62155 | -43.20649 | 2026-03-06 00:02:00 | TERRA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 912e9c87-971a-3174-91ac-8f59fb573e18 | -21.70865 | -48.43906 | 2026-03-06 00:02:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ddff7597-16b3-3286-84fc-1b99907fb8f9 | -22.47976 | -46.99467 | 2026-03-06 00:02:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 8879c4f7-e069-3dc6-ad32-4f5e8c4c1c90 | -21.85249 | -46.97586 | 2026-03-06 00:02:00 | TERRA_M-M | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 45c42ea2-4059-38d3-8ecb-ab0590662ab1 | -22.48147 | -47.00966 | 2026-03-06 00:02:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0f5f4376-ba4d-31cc-8648-b0a77ef8a9f4 | -21.19265 | -48.61104 | 2026-03-06 00:02:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| f6183e41-5323-3bea-a9ec-e03ef998160b | -19.66867 | -49.34622 | 2026-03-06 00:02:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b5636539-30c0-30d3-a5ec-2df0e58e55b9 | -21.2888 | -49.32378 | 2026-03-06 00:02:00 | TERRA_M-M | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 7a0cba2d-58d7-3554-b92f-d72333c7f51c | -21.20074 | -48.61575 | 2026-03-06 00:02:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| eb1a0286-50d2-3659-bfca-1d01c6306d3f | -22.4829 | -47.00387 | 2026-03-06 00:02:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 25b8d325-9b5e-3d73-b424-17f5d2d28449 | 3.2554 | -60.8004 | 2026-03-06 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2bb90272-8bf5-3920-806e-d0bbffe6a8df | -10.0845 | -36.2866 | 2026-03-06 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 56.8 |
| 017b3d19-b946-3098-9fe8-a87195d97766 | -10.0651 | -36.29 | 2026-03-06 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 6fc85e8e-dc7e-35c0-952f-90d4067e4df1 | 0.1367 | -60.412 | 2026-03-06 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c87e0342-26bd-35e5-9d76-cb516b77501d | -10.084 | -36.3136 | 2026-03-06 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 5a9d4579-53f1-3cd8-acb9-4afd3a4c36eb | -10.0646 | -36.3171 | 2026-03-06 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 174.2 |
| 15db4f1b-2b0c-32b7-b4fe-e2a9a2ccade4 | 3.2555 | -60.7815 | 2026-03-06 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7200c798-b48b-35f5-b7a3-81dc0c6cda7a | 3.2555 | -60.7815 | 2026-03-06 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 186dd129-dc07-34b6-938d-10e9c4e31fa7 | 3.2554 | -60.8004 | 2026-03-06 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| b92fb174-d3d0-3e03-8b3b-1c7050962670 | 3.2555 | -60.7815 | 2026-03-06 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a8936f03-2f3d-3820-839f-80bdf46558fa | 3.2554 | -60.8004 | 2026-03-06 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e80105e8-e1f8-31a4-9b42-1b1b5bd6f75a | 2.7633 | -60.3531 | 2026-03-06 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c33aad08-f010-3e4f-8f3d-361980a1e9dc | 3.2555 | -60.7625 | 2026-03-06 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 971fcce7-a935-336f-a460-914c002b2ca3 | 3.2555 | -60.7815 | 2026-03-06 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b67929fa-7fda-33a6-a86d-759066103ac7 | 2.7633 | -60.3531 | 2026-03-06 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2a2f8a37-cc76-39be-b63d-63a941eea5a7 | 3.2555 | -60.7625 | 2026-03-06 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6b1f043e-62a4-38a7-b56e-8e3c639b4416 | 2.7633 | -60.3531 | 2026-03-06 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 61d8a8a4-6572-3374-a8d7-55f9319b4ee5 | 3.2555 | -60.7625 | 2026-03-06 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1852f06b-cb4f-3988-9081-8d6260598029 | 3.2555 | -60.7625 | 2026-03-06 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b23af2db-e13c-34f6-9aa8-09a5c56996dd | 3.2555 | -60.7815 | 2026-03-06 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 170a77f9-3fe6-3deb-a904-b3d781e0c22a | 0.1367 | -60.412 | 2026-03-06 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f06ae9a7-2612-3043-a79d-33558ec3ca89 | 0.0455 | -60.9988 | 2026-03-06 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c02d5978-63d1-3043-9173-310b48ecb7d6 | 0.0455 | -60.9799 | 2026-03-06 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6f80b46a-c2d8-3270-9cba-bca117aef0e1 | 3.2555 | -60.7815 | 2026-03-06 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 354225b1-c625-337a-b043-6a2d175457e7 | 3.2555 | -60.7815 | 2026-03-06 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| fa3f0429-b044-31b9-bba7-b2948fa9ef14 | 3.2555 | -60.7625 | 2026-03-06 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f314a445-2821-3b6c-bc2a-50d470c9ba6d | 3.2555 | -60.7815 | 2026-03-06 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9fdc6197-f346-3179-8d30-6f91904360ec | 3.2372 | -60.7818 | 2026-03-06 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 97d02305-5dd3-30a1-8c6a-b3542af85fd3 | 3.2555 | -60.7625 | 2026-03-06 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 22cfbbb5-6667-3def-aaba-5d7ac63f542f | 3.2372 | -60.7628 | 2026-03-06 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 38.9 |
| b5beb31f-7f0a-3977-9d4c-fe6a36d3f0c0 | 3.2555 | -60.7625 | 2026-03-06 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 72f18da2-1af0-3f22-aab1-5e36e3418c96 | 3.2555 | -60.7815 | 2026-03-06 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7ea63737-db5a-3cd8-9de5-c59d726c0b8f | 3.2372 | -60.7818 | 2026-03-06 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3e27d390-0e3b-3fda-9512-cf269f021f1a | 3.2555 | -60.7625 | 2026-03-06 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| eaf4759a-1d1a-380b-99dc-466ab0854494 | 3.2372 | -60.7818 | 2026-03-06 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ac75e07f-3f08-31d2-aa04-b51e60dd90e3 | 3.2555 | -60.7815 | 2026-03-06 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 5ce11ec1-0896-3335-be1b-52b557722234 | -5.12292 | -37.84979 | 2026-03-06 03:06:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 266f57e0-3375-34cd-a86a-24e9ba4a985b | -5.12942 | -37.851 | 2026-03-06 03:06:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 754ebb43-164f-3008-a166-83cc94917128 | -5.12193 | -37.85532 | 2026-03-06 03:06:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b5155635-f40e-3bc4-a230-e89255138c6c | 3.2555 | -60.7625 | 2026-03-06 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6290992d-77f3-3016-ada9-abd48849fd7e | 3.2555 | -60.7815 | 2026-03-06 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0f0b7840-bc44-3e48-b2ea-9a58b3a9b5f2 | 3.2555 | -60.7625 | 2026-03-06 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 5ef42570-9467-3aee-a923-b1eaddf0d7df | 3.2555 | -60.7625 | 2026-03-06 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e080ebd1-31d6-316e-86da-879621a6b00d | 0.0455 | -60.9799 | 2026-03-06 03:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| adfc05b0-8520-39cf-8c41-16bd4819dc9e | -5.12533 | -37.84963 | 2026-03-06 03:55:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ce98550-81b6-3009-b7b2-f577002fcfe9 | -5.12917 | -37.8467 | 2026-03-06 03:55:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5bb6ee2-b430-336e-9e88-133e1180e80b | -5.12863 | -37.85015 | 2026-03-06 03:55:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ac3cc193-e62a-313b-be38-644bfd736efa | -12.96347 | -38.45847 | 2026-03-06 03:57:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4bbcbcc2-a905-3d45-8416-ce2324054fb0 | -20.94321 | -48.71695 | 2026-03-06 03:59:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf4134ff-1592-39e2-85d8-029c0a66998e | -19.95121 | -41.34769 | 2026-03-06 03:59:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2aa919ec-f90b-3658-88fb-a2d53f72390d | -20.20731 | -50.65067 | 2026-03-06 03:59:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f5dd58a2-edb0-3b03-96b4-867c8ea30141 | -21.32867 | -49.00085 | 2026-03-06 03:59:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 205f4fe5-1b06-3e5d-8dcf-cd158a6d222e | -21.28712 | -41.80946 | 2026-03-06 03:59:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34405f3c-9c5f-3003-a296-da7a6678e299 | -19.17373 | -47.36017 | 2026-03-06 03:59:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 168c61c3-4e43-3e49-9a21-59ccb5195695 | -19.14078 | -50.60325 | 2026-03-06 03:59:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ef00785e-9dc7-3ec3-9d6a-ef4884c63056 | -20.94413 | -48.71231 | 2026-03-06 03:59:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 688046ec-e832-3b83-9f76-c10bfe66919e | -21.92981 | -50.66376 | 2026-03-06 03:59:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8cb33bdd-b507-3bd8-83a1-1c7b8f8f9501 | -20.64115 | -51.68085 | 2026-03-06 03:59:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc2c0d69-efbd-35a7-8679-abb0b1146ecc | -19.88468 | -44.76094 | 2026-03-06 03:59:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9aecb0c3-be32-3923-9a90-03dcae138057 | -20.30632 | -49.58192 | 2026-03-06 03:59:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cf800bb-ce53-3ac5-93a6-63b50440a216 | -20.91445 | -50.53206 | 2026-03-06 03:59:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e34006ca-3cdc-3d1e-bece-4591b16683e5 | -19.95188 | -44.70557 | 2026-03-06 03:59:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d353e83-5e9b-3385-947c-cc3d7f563949 | -19.67043 | -49.34054 | 2026-03-06 03:59:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77f2e394-485d-3387-9e14-761ea4c0af5e | -21.29806 | -49.31641 | 2026-03-06 03:59:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dda37e26-cbc6-3c8a-ad23-71fa3e53b949 | -20.63585 | -51.67956 | 2026-03-06 03:59:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2924e27f-69ba-3218-a26b-a361eb3d97b2 | -19.16957 | -47.35933 | 2026-03-06 03:59:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf1cb55c-1c18-325b-b8a3-76173dc03f34 | -23.25666 | -47.47788 | 2026-03-06 03:59:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 59052f4f-5a76-3a0c-b891-20554d06d0af | -20.20161 | -50.6527 | 2026-03-06 03:59:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c2decb13-a456-36fe-8cf3-52e30d344fe3 | -21.71315 | -48.43621 | 2026-03-06 03:59:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b441737e-47dd-3a54-b81b-2aa1710fc652 | -21.29707 | -49.32136 | 2026-03-06 03:59:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 38fa89f2-190b-3325-b1ab-620181e3870f | -21.93106 | -50.65796 | 2026-03-06 03:59:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 94371b56-1a59-34ce-9ca0-1be63d1220ea | -20.20665 | -50.65381 | 2026-03-06 03:59:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 41979b3e-9650-3ef4-b4df-4d83238cc9a5 | -21.92804 | -50.66047 | 2026-03-06 03:59:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 961638e2-59bc-3734-a42b-79ab2179b65c | -22.80203 | -42.94409 | 2026-03-06 03:59:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 827251bd-5e70-320b-893f-0411729c4363 | -21.20038 | -49.18784 | 2026-03-06 03:59:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 028c8133-7415-3e6c-9a3a-2337ab0183fd | -20.20228 | -50.64956 | 2026-03-06 03:59:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c605f646-04ff-333e-af84-0436977afecc | -20.91935 | -50.5333 | 2026-03-06 03:59:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 19378a2f-4cd5-3d06-83f7-ca765ab7fee4 | -21.92497 | -50.66254 | 2026-03-06 03:59:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4dcfd7f-49f1-3a93-a114-1a0aa4fdb7fd | 3.2372 | -60.7818 | 2026-03-06 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 02dbb2a4-378c-3f60-a2e9-966551bac140 | 2.7633 | -60.3531 | 2026-03-06 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 7b503645-3bfd-3da9-ae51-893e9d8ffc5e | -23.85114 | -51.74181 | 2026-03-06 04:01:00 | NOAA-21 | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cb836527-950d-370b-b4d3-bc42a52e45bd | -23.09577 | -52.35873 | 2026-03-06 04:01:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
