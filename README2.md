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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb984fda-7f5d-3e2c-9573-584289fe808f | -7.6327 | -67.1644 | 2026-09-16 00:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bb839c0c-d48a-37fa-ac1b-31eb8b83c11a | -10.4695 | -44.9491 | 2026-09-16 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9db4c277-7f66-3354-a6e1-6f6890d18b7d | -12.6054 | -50.8334 | 2026-09-16 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 32435921-cc69-30cc-88e9-0b59360579f4 | -3.1265 | -61.2566 | 2026-09-16 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 146302fd-4759-369a-8bc0-b18998125a2f | -11.5033 | -45.8396 | 2026-09-16 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 575ff973-b2f9-3f41-85df-4b77edd4ecb2 | -12.733 | -51.2236 | 2026-09-16 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c28d7b30-74c9-314e-9a04-af39024251c2 | -9.3892 | -60.3215 | 2026-09-16 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| bc9206e6-5692-36f3-b012-6140e9ddbd52 | -8.3319 | -51.3022 | 2026-09-16 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 976a6e12-aa34-3a71-88d5-3659cdf47aa4 | -3.1634 | -61.1048 | 2026-09-16 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5e58340b-b28d-3efc-85a1-b53230bb97ad | -12.6239 | -50.8739 | 2026-09-16 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 74628062-51d5-38c0-b198-ac7ef6e4f892 | -9.7136 | -64.9074 | 2026-09-16 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 30b3ded2-f4a1-3691-b169-214e5370a648 | -3.1816 | -61.1235 | 2026-09-16 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 6ac66ff0-70dd-3539-8ac2-bb13e65a35f8 | -5.144 | -55.9345 | 2026-09-16 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| def14086-e9e1-3506-b12e-f44615d4a688 | -2.1052 | -52.037 | 2026-09-16 00:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| e75d81dd-0f38-38fe-90e8-3aa47ad8af0c | -7.651 | -67.1824 | 2026-09-16 00:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 239b4bb1-b474-312e-aaca-6b985610e96a | -2.1051 | -52.0575 | 2026-09-16 00:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b231702c-3b35-369f-b989-0eb74c20d0d1 | -5.7754 | -45.1053 | 2026-09-16 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1f973937-efd0-3488-8ba4-792fc8d37165 | -9.4102 | -62.7113 | 2026-09-16 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b63ada58-59f6-30cd-ae1d-9bda6a037b5e | -12.6051 | -50.8548 | 2026-09-16 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0a2d19f4-3703-3bea-ad2c-d5520ad27cf7 | -3.1816 | -61.1045 | 2026-09-16 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f62facbb-a11d-3790-9838-ea090d7ae1de | -9.1123 | -45.7067 | 2026-09-16 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 3b030341-ecc0-3606-87d9-bbc05e3c37a0 | -3.1174 | -57.6779 | 2026-09-16 00:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 28cf57d4-663d-373e-b37e-cb2667f5c59f | -9.112 | -45.7294 | 2026-09-16 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 777878af-4b14-3fdd-b340-67764c3e591d | -5.1215 | -47.6146 | 2026-09-16 00:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 120.8 |
| c76d6311-83d8-37ca-9535-d7ab444814dd | -12.6242 | -50.8525 | 2026-09-16 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| d53f3e7c-ee3a-387e-b32c-9beb4a062115 | -9.0931 | -45.7314 | 2026-09-16 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 19023c3f-3f29-3ab6-a021-9642acd3b71b | -5.1401 | -47.6135 | 2026-09-16 00:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b0de1a82-9635-3a2f-8ced-62618e43b528 | -15.45671 | -53.78266 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 755d02c8-ebb0-3daa-808d-ec6cce38f698 | -15.50989 | -53.84108 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4195d16-92ad-3009-9cc5-7d1019bb85a2 | -15.45029 | -53.80245 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8589f973-f28d-3f16-a562-1197d2b7908e | -12.32647 | -47.95816 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f0f3e471-1791-329c-a9b9-d18fb53ebdfa | -12.31459 | -47.96024 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2e89c1d6-c600-3093-8894-34ac5c87da42 | -15.98568 | -50.35712 | 2026-09-16 00:20:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 45001a91-6954-36e8-8766-2cd131fdbdfd | -15.10582 | -49.562 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| b0fb5492-43d2-385a-81d7-99452b7514d3 | -15.25099 | -49.10755 | 2026-09-16 00:20:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 81811b67-7399-3435-bd8e-aa36a39ce00d | -16.66303 | -49.4154 | 2026-09-16 00:20:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 564da3fd-33ec-3195-bdee-b96941bd9ff3 | -15.44906 | -53.79319 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3b466c0b-b2f3-3bd1-beca-98b961a19dce | -15.13587 | -49.55668 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 99b05afa-ec56-3145-bcf9-9e7d6db44d57 | -12.75513 | -51.23209 | 2026-09-16 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9cf0ba47-cd17-3283-96fc-6d574bbe4edf | -12.75666 | -51.24235 | 2026-09-16 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fed77917-3ee6-3afb-b7ad-5f52000c9606 | -12.40849 | -48.48199 | 2026-09-16 00:20:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4515962e-40f8-3e25-88b8-9930ffc12948 | -12.14887 | -48.00053 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f236afa-d085-3e06-b31b-ab53ed133893 | -18.21482 | -41.24826 | 2026-09-16 00:20:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| c9c5adf1-140e-3ca2-823d-e13adbafe022 | -18.11728 | -51.69152 | 2026-09-16 00:20:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 7eadd679-6f8e-3c47-9a56-97c24c54c755 | -12.52304 | -47.12397 | 2026-09-16 00:20:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| d648035c-d446-3e63-875d-42edd5869970 | -12.19437 | -43.47786 | 2026-09-16 00:20:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f4a21ccf-6d7a-35ae-8f8f-0eb495fb4aa0 | -13.73128 | -52.0374 | 2026-09-16 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 262c89eb-e80d-3dca-849d-66fc392e677c | -18.10843 | -51.69292 | 2026-09-16 00:20:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba190b6b-d326-3f85-b713-6635a0eb85e6 | -12.75818 | -51.25261 | 2026-09-16 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9da47766-3461-3c75-b24b-857b4753871a | -15.49974 | -53.83307 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6dd409ac-be96-39c2-9590-8878a9de9368 | -12.15808 | -47.9814 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 86e2255d-0e9e-3b4d-974e-7d9336366e8a | -18.64458 | -50.17546 | 2026-09-16 00:20:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 579b5037-0607-3779-909b-9773fb74d271 | -14.99946 | -56.84442 | 2026-09-16 00:20:00 | TERRA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c5ce6f44-a865-3162-a9ee-9288e53362c8 | -13.77878 | -50.7687 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 211396c8-18b0-3399-a278-5670cfa535f9 | -13.55484 | -43.51245 | 2026-09-16 00:20:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a6344d5c-ad72-328d-b999-3873fd07cb6e | -12.32915 | -47.9752 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3fd5aecd-e4c3-3c7b-8c3f-ddfdc41f7fd2 | -12.61547 | -50.85149 | 2026-09-16 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 301.0 |
| ac4afc6f-8b2a-3300-b831-491312d2cca8 | -12.61708 | -50.86226 | 2026-09-16 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c47a8ed2-6b45-3c6d-9556-760cd2d6bb1e | -18.11859 | -51.70083 | 2026-09-16 00:20:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4ff1ade2-2968-3d68-b8e4-00d4256290f1 | -13.39492 | -57.0476 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e3280503-1e73-311f-95cc-d42210e89dd8 | -15.50099 | -53.84239 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 458e3e76-697b-3944-ae50-64b52b3ed482 | -12.62506 | -50.84998 | 2026-09-16 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 5669b8bc-6f99-39e1-a854-7656a7e87010 | -12.15445 | -47.99392 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| fa4fb007-a103-37f1-b427-13e169cca689 | -11.89173 | -43.83002 | 2026-09-16 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 1e99cb4f-e661-3db3-8a36-215a2ca113d8 | -15.13402 | -49.54469 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c4ba3d0b-a857-38e9-8a19-6f35a1deca16 | -11.88626 | -43.83796 | 2026-09-16 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 0ea4f340-8dba-3225-89d6-95c1efd7abc1 | -14.85879 | -49.96318 | 2026-09-16 00:20:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fb9172e4-d9b5-325c-94a3-85c7f42e9689 | -18.23183 | -41.2355 | 2026-09-16 00:20:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.5 |
| ba0b26a6-736f-3133-9b28-1ceeca694707 | -15.3019 | -53.18563 | 2026-09-16 00:20:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d2cca8f-9222-3a8c-9fd9-540b003c36c9 | -16.04113 | -51.74726 | 2026-09-16 00:20:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f430347e-74cc-3f02-b6b7-fc97e0a6dddb | -13.77723 | -50.75811 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 146ec31e-7500-3789-bab0-e9a5da7cf286 | -12.22235 | -47.13956 | 2026-09-16 00:20:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bbab6421-bcf1-39e6-9bd5-1fcca07841ae | -13.3934 | -57.03529 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| a1cfe295-f0a1-3294-8d81-ffba2ff72777 | -13.40211 | -57.0217 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2bf01b71-2c5e-3149-9284-0ca545979584 | -13.38469 | -57.04897 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f9020f86-5abc-3bf6-9ae0-5054cfde3f03 | -13.99954 | -48.634 | 2026-09-16 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8f208508-ae67-3972-807b-d13c2f9607e2 | -12.75312 | -51.2597 | 2026-09-16 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7e40ff59-d1e1-388d-a6aa-ab32039fa3d0 | -15.10767 | -49.57392 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 940df0af-5d68-32fe-ae63-e9eaf5dc73d6 | -15.44782 | -53.78396 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0fd098f8-e0bf-320b-949b-e1a82ca7db1e | -12.19059 | -43.48558 | 2026-09-16 00:20:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e4308f50-82fa-3f9d-a197-cb2795c2bf23 | -12.22199 | -47.13418 | 2026-09-16 00:20:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 734961fb-627b-31fa-b68e-bbee60cb1445 | -13.75937 | -48.79709 | 2026-09-16 00:20:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f7ced4a4-868b-37fd-8f44-fc920052930c | -12.7378 | -51.22007 | 2026-09-16 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1a84d9f9-4c84-31ce-8a8c-a9a3ee4dc707 | -12.16075 | -47.99843 | 2026-09-16 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 56ba6356-391b-3d72-840f-3f7352f78717 | -18.23207 | -41.24369 | 2026-09-16 00:20:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 074cf1df-f79e-3c87-949a-7506f1358b60 | -12.73929 | -51.23036 | 2026-09-16 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 4f503671-bd44-3f45-9c12-d6baa6a35bb9 | -13.54881 | -43.5205 | 2026-09-16 00:20:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| b1cb67c7-3b42-3ee3-a348-1b33bb7d880b | -15.51114 | -53.85038 | 2026-09-16 00:20:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5827402d-0847-3325-8106-ed939165db79 | -14.65293 | -48.96189 | 2026-09-16 00:20:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6bff676b-429c-3071-af7e-e10622fa19a6 | -16.67291 | -49.4137 | 2026-09-16 00:20:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| de154d18-11ed-3036-9534-37f411bac564 | -18.21449 | -41.2396 | 2026-09-16 00:20:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| ca0b04b6-367b-3cbb-b4f9-fc1c5d417dd1 | -15.00979 | -56.84303 | 2026-09-16 00:20:00 | TERRA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4b537941-a070-3741-89d5-1c65171241c9 | -13.38316 | -57.03659 | 2026-09-16 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e9d03799-0a0c-31ac-bdc3-e9efefa5d099 | -11.19582 | -55.03238 | 2026-09-16 00:22:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e74bfdbf-a9ca-31b7-ac92-c0842b253f7e | -11.72996 | -47.59876 | 2026-09-16 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a9f96341-19a6-3ad6-b701-13583d851a26 | -11.83649 | -50.03454 | 2026-09-16 00:22:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 329310fb-7a78-3333-852e-e2a00d769ec2 | -9.77752 | -46.48347 | 2026-09-16 00:22:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1433d4a8-db64-3c77-a6a2-83f63871e037 | -5.81101 | -49.85181 | 2026-09-16 00:22:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ace4308e-aecc-3f6c-a2e2-dd2995206334 | -10.90001 | -54.00909 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cec13a00-bcae-3e05-a30f-0c5efd6f477e | -10.58504 | -47.75033 | 2026-09-16 00:22:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README3.md)
