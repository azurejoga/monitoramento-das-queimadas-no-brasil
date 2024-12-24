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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8368d9d-f2f9-35b5-8278-177adae37415 | -2.3649 | -45.5912 | 2024-12-24 06:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e39068e9-b894-383f-94af-3599571a5125 | -2.3463 | -45.5917 | 2024-12-24 06:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ea6bff49-3085-3337-8441-444b080f78af | -2.3464 | -45.5693 | 2024-12-24 06:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d96f957c-df23-37cb-9b58-161a0ed38c39 | -2.3463 | -45.5917 | 2024-12-24 06:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4ed4ca74-5700-31bf-a23a-896e704b1767 | -6.2339 | -55.6308 | 2024-12-24 06:40:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f071397e-c94c-3841-968b-96d91ca7a955 | -6.2341 | -55.6109 | 2024-12-24 06:50:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4380f9a0-9b53-3743-9d4c-5d7a683f4dcd | -2.3463 | -45.5917 | 2024-12-24 06:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 773e0e5e-4282-3747-bf8f-09d3962bbb82 | -6.2339 | -55.6308 | 2024-12-24 06:50:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cf09bc8e-65ac-3af3-b837-f4b2b212502f | -2.3463 | -45.5917 | 2024-12-24 07:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 87f2cb1f-aa4c-3b01-aeca-3c5e8cc9d9b5 | -6.2339 | -55.6308 | 2024-12-24 07:00:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c94a9944-2d1e-37ab-af3d-a65edbbb3086 | -6.2341 | -55.6109 | 2024-12-24 07:00:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 13f2f364-94c2-306d-8f8b-c4388388f327 | -2.3464 | -45.5693 | 2024-12-24 07:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b83c144b-63c4-3ee3-aa3e-6f22526d1f8d | -6.2339 | -55.6308 | 2024-12-24 07:10:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8bafffa3-8259-3f7b-8551-dd42ef687f2e | -2.3463 | -45.5917 | 2024-12-24 07:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 000602ca-a86f-3913-a177-2eca9b7847fd | -6.2339 | -55.6308 | 2024-12-24 07:20:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 760de7bd-c712-3733-bae2-2302e9d4d583 | -2.3463 | -45.5917 | 2024-12-24 07:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 780d8af3-d84b-333e-87fb-18d76243114e | -2.3464 | -45.5693 | 2024-12-24 07:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ed7f8fe3-a348-3a6c-b8e1-e14548e5cf1a | -2.3649 | -45.5912 | 2024-12-24 07:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c7b0a648-65e0-3d5a-80b4-8311cd49d0da | -2.3463 | -45.5917 | 2024-12-24 07:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 958ce9e2-e011-39d8-a94a-8292711017ec | -2.3464 | -45.5693 | 2024-12-24 07:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 06585656-8d70-3b4d-9604-a112eac72f2b | -2.3463 | -45.5917 | 2024-12-24 07:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| dd985a83-c1a2-3ce0-bb9d-0adb104b44de | -2.3464 | -45.5693 | 2024-12-24 07:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fb8ff4da-7d53-3800-acd0-4505ec12281f | -2.3463 | -45.5917 | 2024-12-24 07:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| dc32690b-43f4-30e5-b665-d95ef1361402 | -2.3464 | -45.5693 | 2024-12-24 07:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0c840120-e341-3b34-9b11-2c3beafa7b9b | -2.3463 | -45.5917 | 2024-12-24 08:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 324dcadf-a223-3577-9136-bee9ed7aae07 | -7.52975 | -38.31958 | 2024-12-24 11:49:00 | TERRA_M-M | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 980bf70c-c009-3b6f-97dc-5998f3c5fb5b | -9.42311 | -36.00806 | 2024-12-24 11:49:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 735b0278-abd7-3243-a863-9dfbadc8f2ea | -7.24466 | -37.43087 | 2024-12-24 11:49:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 695513cf-925a-3546-84cf-2e6b469c5f65 | -8.27038 | -37.62012 | 2024-12-24 11:49:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 1c595bf8-f075-3511-bef3-08c6b59c53b0 | -7.27039 | -37.39017 | 2024-12-24 11:49:00 | TERRA_M-M | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 11.3 |
| deefb997-8646-32a1-aec9-ab859929e247 | -6.69924 | -35.45541 | 2024-12-24 11:49:00 | TERRA_M-M | SERRA DA RAIZ | PARAÍBA | Brasil | 2515609 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 680ee830-9e3f-37e4-a22a-0e9c3c00ab34 | -6.59803 | -37.36855 | 2024-12-24 11:49:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e6a66dd9-b9a4-3196-8bbd-597409b09847 | -8.2688 | -37.63065 | 2024-12-24 11:49:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 5ea1e795-e8f5-3178-b696-c58b64e288f8 | -6.08906 | -37.81446 | 2024-12-24 11:49:00 | TERRA_M-M | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 98a24f62-8f48-34ed-848b-09288ec74083 | -9.11179 | -41.28995 | 2024-12-24 11:49:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 3fce9b7c-d4e9-3447-b3bb-58d22813401a | -10.1912 | -39.15158 | 2024-12-24 11:49:00 | TERRA_M-M | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 9c9702ba-6a8c-3bef-9207-52797164c012 | -7.5868 | -35.43761 | 2024-12-24 11:49:00 | TERRA_M-M | MACAPARANA | PERNAMBUCO | Brasil | 2609006 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 9c22230c-4c80-3240-a64d-e3259afa9e01 | -7.52241 | -37.9646 | 2024-12-24 11:49:00 | TERRA_M-M | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e4277a87-487b-3eac-90ad-f874361de93a | -9.1197 | -37.55957 | 2024-12-24 11:49:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 21a943a0-0e88-3c54-ab44-c6d55fae214e | -6.31185 | -37.56144 | 2024-12-24 11:49:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ed744f37-4252-39e2-b78c-909b58d61a97 | -6.08734 | -37.82586 | 2024-12-24 11:49:00 | TERRA_M-M | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 6540aea7-980b-390f-a9b9-efcd3d027d5f | -6.36977 | -37.11217 | 2024-12-24 11:49:00 | TERRA_M-M | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 1c396d08-4a75-3fd4-b1fb-233bbf35a1cc | -7.51963 | -38.31808 | 2024-12-24 11:49:00 | TERRA_M-M | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d91d2a5a-29ee-3841-877d-d3e27e981bc9 | -8.40244 | -36.42189 | 2024-12-24 11:49:00 | TERRA_M-M | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4d4c4b91-8808-3dd7-b531-2cfa19dc0798 | -8.92656 | -36.93356 | 2024-12-24 11:49:00 | TERRA_M-M | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e7799940-16cd-3773-9e0e-dff82609d0cd | -7.14829 | -38.3345 | 2024-12-24 11:49:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 08d944e3-a1a7-38cf-b066-05d53f17b678 | -5.76573 | -36.8964 | 2024-12-24 11:49:00 | TERRA_M-M | SÃO RAFAEL | RIO GRANDE DO NORTE | Brasil | 2412807 | 24 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 19591be7-23ea-390b-a11d-951832bd284c | -9.42443 | -35.99905 | 2024-12-24 11:49:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 4489c577-2263-308e-a2db-b8897578a120 | -6.66751 | -38.25668 | 2024-12-24 11:49:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 249b955e-81f8-38e7-890d-b39f0821cd1e | -6.14515 | -35.32352 | 2024-12-24 11:49:00 | TERRA_M-M | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| e36c87cb-6c0e-353a-a8c3-0a0df7db79c9 | -7.25533 | -35.56322 | 2024-12-24 11:49:00 | TERRA_M-M | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 4da2711a-bf95-31f1-8073-f81a0bc9009f | -10.74905 | -39.31024 | 2024-12-24 11:51:00 | TERRA_M-M | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 9a9d09f5-4a4c-3870-a69b-0cfe7b65bd63 | -10.14751 | -42.21174 | 2024-12-24 11:51:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 7a217a4d-ba1d-30f9-b14d-f934640130f2 | -10.68183 | -42.38912 | 2024-12-24 11:51:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 44631554-9c3f-329c-bc56-a76d19b70e5c | -10.751 | -39.2979 | 2024-12-24 11:51:00 | TERRA_M-M | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 27.7 |
| ab3174ba-8fd9-3936-b3c0-cf8f7c5661f6 | -10.7407 | -39.29622 | 2024-12-24 11:51:00 | TERRA_M-M | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 4c13b6e6-20c0-3177-bc02-90d69e90ee5b | -10.68501 | -42.38358 | 2024-12-24 11:51:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| f21913df-3cd8-3cb5-943e-be1dcb6f2a76 | -11.24504 | -38.56376 | 2024-12-24 11:51:00 | TERRA_M-M | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 45.3 |


