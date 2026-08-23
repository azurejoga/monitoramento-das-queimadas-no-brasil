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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 612585ae-1264-33b1-8d6f-6b9dc2d58bf0 | -13.2081 | -51.421 | 2026-08-23 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a383e825-a63e-395e-b515-e0af8d045666 | -6.9514 | -59.0666 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 261ddb6e-f3ff-3055-bc40-3c580c6d693b | -13.1886 | -51.4447 | 2026-08-23 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9cd42336-c474-37a0-85c3-23eebc3abf53 | -6.9513 | -59.0859 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 37810a3a-f787-301a-a958-8914aeddc9b7 | -9.1909 | -59.4619 | 2026-08-23 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 276b4b59-5f18-3e76-88f1-eed2884209d6 | -6.8008 | -59.5934 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 84e47ea7-586c-3273-aab2-a6c967864d97 | -2.9821 | -48.9384 | 2026-08-23 02:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 8f6ebcb0-3b88-37a5-a5da-0c3f36624f1c | -6.9698 | -59.0852 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6aa6ec46-1191-3f77-86a5-1760d009ae90 | -2.982 | -48.9598 | 2026-08-23 02:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| fc56d952-f433-30fe-9b5f-d63fd9bb0764 | -13.1889 | -51.4234 | 2026-08-23 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e0f5f017-7fcd-38e9-b2f2-1eb25ccf0aa3 | -6.1286 | -57.8198 | 2026-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 343789f7-c371-35f5-82b9-2628b763e379 | -6.9699 | -59.0658 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| fb545890-39d1-35e8-9414-f679c2247891 | -21.4748 | -46.1316 | 2026-08-23 02:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.3 |
| 25739102-3a36-3ad3-96be-8125b210a161 | -10.8361 | -50.9691 | 2026-08-23 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 4282385d-c933-3b0a-a553-0b85a895632b | -6.1286 | -57.8198 | 2026-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ed9aa2db-4748-3fbb-aaac-f7d846f507a5 | -13.2078 | -51.4423 | 2026-08-23 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 71ea9a99-ca29-322c-9f9e-64fba1bd7ac5 | -6.9514 | -59.0666 | 2026-08-23 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a665fb07-0f85-37c0-b644-2d271bf0247d | -6.8062 | -58.6469 | 2026-08-23 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7d12eb85-552d-3aea-9605-ac2b7a76520f | -10.8172 | -50.9711 | 2026-08-23 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c31cd2d5-edf7-30d2-94a8-5312a94d1512 | -6.1469 | -57.8385 | 2026-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4d8cf068-d1a0-3a82-b8c1-c4892cf97625 | -13.1889 | -51.4234 | 2026-08-23 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2846bb64-f53a-3c22-9f5c-3ee0ca9a7c4f | -20.2758 | -48.6518 | 2026-08-23 02:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 83.4 |
| cd481121-e11f-3564-95bf-fd7a47798b06 | -16.0706 | -50.4332 | 2026-08-23 02:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1e0827c8-db82-38c5-ad03-533087c179ee | -2.982 | -48.9598 | 2026-08-23 02:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e9190de3-74af-348e-801a-8c9423cf86e8 | -9.1332 | -65.9559 | 2026-08-23 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 211b6014-bbe2-3274-bc87-4b21734ea743 | -3.0005 | -48.9592 | 2026-08-23 02:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 18f24440-b107-34c2-9dfc-75994df9fb8e | -6.9513 | -59.0859 | 2026-08-23 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4bf3ce08-c800-387b-87d9-7c937ec897fe | -6.5487 | -58.522 | 2026-08-23 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cd940c8a-dca1-3234-ba3b-62593782f7b4 | -5.7799 | -57.58 | 2026-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 30ba36c3-bbef-37fc-92dc-d3d4097d5c37 | -6.8061 | -58.6663 | 2026-08-23 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4e82383c-05e2-3211-82d1-a03ac2d7cb1e | -6.1101 | -57.84 | 2026-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c82387c0-5974-3908-8244-c656a9138279 | -10.8358 | -50.9903 | 2026-08-23 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| be5db533-e209-31ce-98e4-9573eaac42ea | -10.8169 | -50.9923 | 2026-08-23 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 3d528f85-6f2b-3f35-943a-aad9a6faa403 | -13.1697 | -51.4258 | 2026-08-23 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d115bb99-1f06-3dd8-85d6-f6e4c7a448e9 | -6.9699 | -59.0658 | 2026-08-23 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 6e42bfbb-1f6f-34b6-88c9-cf265090221a | -6.8188 | -59.6696 | 2026-08-23 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d7fb58f8-d4aa-3edb-b58a-93b7f44f8ee1 | -21.454 | -46.1371 | 2026-08-23 02:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| 1d5aff89-ea79-3545-b498-057830972484 | -7.2626 | -49.9066 | 2026-08-23 02:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9e2cf934-1fac-3717-b0cf-d53ec263c70a | -13.1886 | -51.4447 | 2026-08-23 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7fa20689-1103-3aaf-8b65-e1b26d115af8 | -6.1285 | -57.8393 | 2026-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 109c4ff7-d414-34d4-97ee-0a30d8680191 | -6.1925 | -53.5231 | 2026-08-23 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| bacb18f6-6b0e-3f7a-9d97-5cd68ba66a2d | -6.1286 | -57.8198 | 2026-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9ce6d3a6-5eb2-3f50-b52a-a4478893a770 | -6.1285 | -57.8393 | 2026-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| c17cbbcd-e8ae-33e8-a1df-13f3041bdb46 | -16.0706 | -50.4332 | 2026-08-23 02:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e45a4852-1b7b-3de0-b066-8ccf00fc10a1 | -6.9514 | -59.0666 | 2026-08-23 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 651cc908-0c5e-3638-b84f-89c35103a216 | -10.8361 | -50.9691 | 2026-08-23 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 753ebb6b-ed1e-3da6-8635-3868d4c5d6fd | -16.0509 | -50.4363 | 2026-08-23 02:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 626a23be-9eeb-3cae-8d84-c7367330f2dd | -6.1101 | -57.84 | 2026-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cd10c1af-9793-3093-9889-9ddd13d40e58 | -13.1697 | -51.4258 | 2026-08-23 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 122e7761-d31f-372c-8f2b-9b0d8132f4a0 | -6.8062 | -58.6469 | 2026-08-23 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| dbeb4262-9b31-30d5-ab2c-5bc1f6bef90e | -13.6806 | -51.8511 | 2026-08-23 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 444e58c7-5193-352f-9f68-255247a70640 | -13.1889 | -51.4234 | 2026-08-23 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 2fe10b1f-1b6e-351f-a95a-df3b1c64244f | -6.8027 | -62.9024 | 2026-08-23 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6f7fb901-3243-3c3a-af35-6a5d12d3e8a2 | -2.982 | -48.9598 | 2026-08-23 02:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 1b278d68-3742-3951-87d0-c4b19afc3111 | -3.0005 | -48.9592 | 2026-08-23 02:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| be44f765-3bf3-3214-848e-b7ac8c7a7cb2 | -6.8188 | -59.6696 | 2026-08-23 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 17c88b97-2cde-3f0a-9fff-99131e14ae65 | -6.9699 | -59.0658 | 2026-08-23 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 1ef49a4c-ff5d-37e1-ab66-91b28c95da14 | -6.8061 | -58.6663 | 2026-08-23 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 69ee624b-a38e-3e53-9dbc-13175cba8eb2 | -21.454 | -46.1371 | 2026-08-23 02:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| ce3a7771-14b3-3d8a-9c8a-d1503f6e862f | -6.1925 | -53.5231 | 2026-08-23 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4bf67932-e75e-3ed6-8a85-794278cbaa8b | -6.9513 | -59.0859 | 2026-08-23 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3fc61495-7e9f-398d-9a8d-c8de0ba5d3f6 | -5.7799 | -57.58 | 2026-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c05ebee3-c1c2-365b-acb5-6dbd815a6f05 | -5.7799 | -57.58 | 2026-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 76f049bc-5bdc-372a-9cf4-7b469a282fd7 | -6.8062 | -58.6469 | 2026-08-23 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 03ff0311-51bf-37e1-94c5-df98ff6c3361 | -10.8361 | -50.9691 | 2026-08-23 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f6cd7dc1-3994-37cf-9abc-627b37691abb | -13.1694 | -51.4471 | 2026-08-23 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 013b0562-0fb4-3cac-946d-cac4e811bedb | -6.1285 | -57.8393 | 2026-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| e9158ce2-1209-3fd6-b8b8-54990b7f5599 | -13.1886 | -51.4447 | 2026-08-23 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 77a09345-17ec-3f07-9022-13869cad7b8a | -6.5487 | -58.522 | 2026-08-23 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 60054948-7afc-3dcf-8a34-76566c26d626 | -6.8188 | -59.6696 | 2026-08-23 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8ceda4ab-c9c7-315c-ac4e-626e85b1f86d | -6.9513 | -59.0859 | 2026-08-23 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1a1b3495-d792-3c4a-ae6f-e6b9394480d2 | -3.0005 | -48.9592 | 2026-08-23 02:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d1942532-d1d6-376c-a103-32faa7258121 | -6.8061 | -58.6663 | 2026-08-23 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c36d400b-c0fc-37ec-8cbf-ce26f139ae1e | -13.1697 | -51.4258 | 2026-08-23 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 57100be5-c61d-36d0-bbbc-e3ce477eda35 | -6.1101 | -57.84 | 2026-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c1d2cb9c-a786-3181-8678-14ff1f77a07e | -2.982 | -48.9598 | 2026-08-23 02:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ae1d965d-5eaa-3dfe-9365-b14c038c5c41 | -13.1889 | -51.4234 | 2026-08-23 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 378a7f1e-3999-368b-8af0-de114d46e2d2 | -6.9514 | -59.0666 | 2026-08-23 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5eb911b1-7f2a-3bfb-b68e-de8224b74345 | -21.454 | -46.1371 | 2026-08-23 02:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| aed74bf6-0b51-383b-b529-3cd87c06e5f7 | -16.0706 | -50.4332 | 2026-08-23 02:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2bffc135-3a5d-31d5-9fe3-cd1e41aaaa90 | -6.9699 | -59.0658 | 2026-08-23 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 56d00cbf-35e2-3e86-8bc3-271ee99ed481 | -10.8358 | -50.9903 | 2026-08-23 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cff78077-c404-3d64-a0f9-d418390b6639 | -16.0509 | -50.4363 | 2026-08-23 02:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 162.1 |
| bcf26a88-1af7-3900-8c88-45222d9dcb5a | -6.1286 | -57.8198 | 2026-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ae33dd99-62e5-3103-ad40-76d787181cc7 | -2.982 | -48.9598 | 2026-08-23 02:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c0c36283-647d-36da-8172-a06a0b495d75 | -6.8062 | -58.6469 | 2026-08-23 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6b99698f-9cd8-325f-96c3-8bf2fe90554e | -6.8027 | -62.9024 | 2026-08-23 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 64dee57d-9fea-3310-bab0-cec73e1e8739 | -6.1286 | -57.8198 | 2026-08-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 879edc6c-7473-30b4-a707-96b9522abb76 | -10.8358 | -50.9903 | 2026-08-23 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 25f7322d-0dbc-3ef7-bd06-2e6689cae6cb | -6.1285 | -57.8393 | 2026-08-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| aaf516ed-7c0a-3825-bda0-842f25a33e93 | -6.9699 | -59.0658 | 2026-08-23 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| ab88eb8e-c8f0-3295-8e57-3d9987245489 | -6.8188 | -59.6696 | 2026-08-23 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| eef5aae9-f4aa-3e34-9fc6-09c055b8a41d | -6.1101 | -57.84 | 2026-08-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e72897f3-74db-306d-a081-24b45823680f | -16.0509 | -50.4363 | 2026-08-23 02:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| af931fde-791d-3bc3-b4a1-6b6f0560baf1 | -6.9514 | -59.0666 | 2026-08-23 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 4e9dcfcc-437e-3ec6-9d3b-de264336dd6f | -6.9513 | -59.0859 | 2026-08-23 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 08a6503d-8dfd-35a2-b8b0-59a8e7891fcf | -13.6806 | -51.8511 | 2026-08-23 02:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9ae2a451-e57e-3ce2-8097-7465efaa947f | -21.454 | -46.1371 | 2026-08-23 02:50:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| 361eb44b-929a-3670-b933-be817aeb5a5e | -6.1925 | -53.5231 | 2026-08-23 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ef1510b2-3986-301a-b4e3-e742d0f3abf9 | -6.8061 | -58.6663 | 2026-08-23 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |


[Clique aqui para ver as próximas entradas](README8.md)
