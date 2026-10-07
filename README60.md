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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb51a9f4-ea46-3d24-a91e-02c8a5683db3 | -13.06807 | -43.60985 | 2026-10-07 04:21:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82c88aa6-661d-363c-95ea-a217f4781830 | -10.147 | -36.24615 | 2026-10-07 04:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 65ca090a-5b76-385f-b1e8-0a8a000c8eb7 | -8.7815 | -47.57597 | 2026-10-07 04:21:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 848c12de-bfd8-31e3-bb5b-849b7d912187 | -8.6996 | -45.21262 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50c77b1c-c254-314c-9c47-672b040c04e5 | -9.02188 | -45.18406 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48f32709-6ff4-3897-9787-c0cf6dbab6a6 | -13.37597 | -43.87347 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a2d2a28-c2d9-31df-bed2-2425bcd9d3db | -11.22761 | -44.86241 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e2d4c81-ede5-31c1-832e-ca735aee42e5 | -12.18664 | -44.7278 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce4202bd-05a4-3954-a626-e17a3e59fa6f | -11.72582 | -43.64115 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a7e188-a519-3f36-aed0-abb022d65990 | -13.38933 | -43.87563 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20466477-8166-393e-b19a-b4711b66fbee | -8.70692 | -45.21012 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6753d9eb-58c0-34b7-b758-5a1d5981f88f | -8.28917 | -50.27372 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3811e8ea-0172-3422-97fe-ccc574ef80a0 | -11.69676 | -40.10888 | 2026-10-07 04:21:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21f3c8ab-fea1-36fc-b404-6b4c336993b6 | -11.23036 | -44.86647 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c2f82cd-c6d1-3b94-a9d2-08036507f2d3 | -14.89074 | -44.80844 | 2026-10-07 04:21:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1cb53cc-5d9a-3e1e-a491-abd42b454f6b | -12.03864 | -43.39296 | 2026-10-07 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 107aef57-a953-3375-9463-dce0ad1313a4 | -8.71718 | -45.18957 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9d24b436-a8b0-3730-821d-d097b9bc4635 | -9.26959 | -50.66779 | 2026-10-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba2bfd6a-eab7-34f2-b4c5-022d08185fba | -16.0383 | -39.83563 | 2026-10-07 04:21:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 96bb703d-aefc-35fe-983e-47294e7fee9e | -11.3487 | -46.64548 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e09022-5af2-3636-be5f-21354e211ff1 | -10.49092 | -50.43184 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db8db879-4339-300e-8fd7-31ceb48d959c | -10.48228 | -50.43022 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 91747cdf-a18e-34e2-9eea-bb610b37247c | -11.72749 | -43.65235 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e4e7070-3f1f-3271-b54e-0c6e2b0f9bc0 | -9.35146 | -45.4302 | 2026-10-07 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28615375-73e2-3e88-be49-44800031324b | -11.10261 | -45.68244 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b28643be-2964-3ef2-96b6-cc155d1ee6ac | -8.88155 | -45.38003 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc286b56-7b6d-3cc4-bce3-4a2bc1d259b7 | -8.79044 | -47.56825 | 2026-10-07 04:21:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2f98675-0170-36a4-a493-560a0a2517f9 | -12.19273 | -44.71078 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbef3f62-538f-31fe-bcc0-eaff741ef977 | -8.716 | -45.1968 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a818300d-7b10-3ff5-91ae-8e537ffe3d99 | -9.76373 | -44.79314 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b3d1faa-2bdf-3e17-af6f-85359d31dd83 | -9.34533 | -47.844 | 2026-10-07 04:21:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35b27531-3d5f-3f36-9b44-7dd34e934731 | -11.32632 | -46.67326 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65191e9a-70e7-32c0-a77a-87a6f55b39f0 | -11.3345 | -46.66682 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4b0679-7ce1-3aa8-a482-fe30beb32e4e | -14.25292 | -41.62601 | 2026-10-07 04:21:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0e02a025-d682-353d-a05a-b2e53be56835 | -15.42099 | -43.7015 | 2026-10-07 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 5e37796e-be66-3d66-8d6f-79afaa9e8d7b | -10.84468 | -50.65728 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfcc8826-59a9-3b79-b4e2-323eeb4baa04 | -9.45343 | -44.60963 | 2026-10-07 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a91745a2-bf4d-3b08-b0b8-80db2b0c9bcd | -11.73471 | -43.64985 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08306cfd-b026-34b1-8b4b-0f67085fc8c2 | -8.70119 | -45.22405 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ca95b1a-299a-3d23-9bc5-0a019bc9fef6 | -11.23149 | -44.85943 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fb06189-d240-3b40-820b-312dcdd37723 | -16.02846 | -45.13068 | 2026-10-07 04:21:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92e8f22d-e908-389e-84be-75cdfb5d4e04 | -11.84513 | -43.55086 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82b6406d-f6e5-35fe-81fb-b486373777d6 | -9.67879 | -47.89742 | 2026-10-07 04:21:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d88148f1-98b4-3ed3-a2d3-881757ae95ee | -11.78825 | -46.5764 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69772262-17bb-3ede-9836-b07b063c4d27 | -9.35484 | -45.43075 | 2026-10-07 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6920593a-11a3-3cd5-a644-f617c0ec27af | -11.10945 | -45.73548 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c8bd61c4-e048-3867-91b0-e997479dc3e5 | -11.50206 | -48.47882 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e31f761-242f-3d70-b017-4dcc519a7267 | -12.16684 | -44.70293 | 2026-10-07 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b5483f3-141d-3745-a7f4-14be1e4e8b43 | -15.24799 | -43.27021 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.6 |
| a728efd2-add4-3576-a07a-d04a2fe0b456 | -11.77451 | -46.57411 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 983e94d8-135a-34d7-aa69-b38af9cab60d | -12.17616 | -44.72969 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cc06b51-0c01-3412-89c4-24a2e1bea401 | -11.46906 | -43.39555 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef812bea-84b0-328e-ac81-44ae33b3c141 | -11.57448 | -48.44159 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1acbf3b-1364-3ce9-aaa3-75b4cd5043ec | -15.11038 | -43.62702 | 2026-10-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2270de1-e26a-3921-87f1-d310b3ff3f73 | -11.11019 | -45.72095 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fef3977-49ab-3302-84e5-8b850fa9d7b9 | -10.98871 | -45.41631 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 293f04c3-3062-302e-8b88-e44a99ca496f | -11.07766 | -45.64495 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de9f6c03-97c9-30d6-b16b-4be4e1048968 | -12.08018 | -48.11971 | 2026-10-07 04:21:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13990768-eedb-3b74-80d1-49c1b2b00585 | -11.77486 | -46.69994 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddaea996-162d-31a9-9cef-2f62feb47af3 | -8.71659 | -45.19319 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 406d0e6c-da57-3c4a-8076-3d8b817799a3 | -13.6336 | -44.42426 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2855a08-62dd-3ac9-8358-a44491aa3e14 | -12.18942 | -44.71024 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34c024f6-e103-3677-b95f-5d32f5996343 | -15.15989 | -41.29297 | 2026-10-07 04:21:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ce284b6-ac17-3a95-bfbf-eca7ba62b5f2 | -8.71482 | -45.20403 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b1b5883-3692-3d25-903d-c43fe100df5e | -8.84224 | -48.78466 | 2026-10-07 04:21:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45d807ad-c294-34d8-be9f-81130cc4cf71 | -9.79647 | -44.78038 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65492d00-1fbf-3e8d-ba45-fb4e1b01d45a | -8.53026 | -55.37806 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ad4b23b-df74-30e5-b623-e18f6b31b1e9 | -15.32414 | -43.09152 | 2026-10-07 04:21:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fd098c7d-9ef2-3347-b95e-5c5c7380bab5 | -8.70078 | -45.20539 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb53c426-493e-3820-98d1-fa4088d3bdde | -12.43552 | -47.99437 | 2026-10-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 493970c4-94c6-33b9-8be3-e4263389911b | -9.60747 | -45.85999 | 2026-10-07 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8e22e8d-679d-3897-be62-c8dbbbf8093d | -8.70633 | -45.21374 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ac5b7bdd-3f49-322e-933f-146334f82438 | -11.05048 | -45.8119 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55496a18-f960-377f-a13a-c04831fe3004 | -11.66751 | -43.62094 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c6f1ad7-b8ed-3985-aa3d-fa2695130d72 | -9.77094 | -44.79069 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cad96f5-ac16-3815-a0d1-72c5d8230980 | -8.91012 | -49.98378 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0c4abc58-e113-3b29-a17e-7c405b0573c2 | -11.82123 | -43.55061 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fce563bd-86eb-3123-be6c-8d6823b87899 | -8.70751 | -45.2065 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f41faf6e-5ae0-3e8b-a25d-a83f1385eb88 | -11.01182 | -45.46444 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6b59e75-8a72-375c-bb76-f7dfbe93ccd1 | -11.25658 | -45.18949 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ddf53c3-e63b-3b95-a35e-5eae9cc34b45 | -8.71146 | -45.20345 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 099d77e2-7136-3cd3-9eef-b4b451c5eb50 | -8.53734 | -55.38305 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99cf69fa-6fa2-3fb7-8543-1457c8e14908 | -12.19329 | -44.70727 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02d3dbd3-daee-38f0-905c-5a8d9a8414f3 | -12.19559 | -44.65002 | 2026-10-07 04:21:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00cbb7bb-b725-3d6c-ae41-1eea296b4bb5 | -13.6685 | -44.30955 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 386c2d34-5344-3372-926c-d95bdab1305a | -8.28551 | -50.26852 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cb050622-d72e-3941-8fc8-17911722d190 | -10.9826 | -45.41165 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e09ccacd-d152-39e5-9a96-412de28b577f | -15.41703 | -43.70471 | 2026-10-07 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 667272bb-20e6-37b3-988c-ce36924305fa | -8.91319 | -43.88544 | 2026-10-07 04:21:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99ae3e23-553e-389a-971d-3e0dfb86ca84 | -14.21291 | -44.60584 | 2026-10-07 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e62506d-1523-32a9-971c-1d2d0865d09d | -12.21313 | -44.71053 | 2026-10-07 04:21:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc80e634-3f6b-35b1-aa88-2caf6d987ff2 | -12.17671 | -44.72618 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7deb2efc-828b-31cf-b54f-0325cf97e6aa | -9.26335 | -45.64498 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2b70849-709d-3bf3-9eae-b93b54be6796 | -12.08459 | -48.11598 | 2026-10-07 04:21:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90c5a3ef-508a-3a94-ae3f-4dc37fe0d2aa | -13.7535 | -43.62417 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93686021-21f6-3f68-9784-7927f8ea9464 | -10.99147 | -45.42045 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6cbdef98-f9f6-3e39-aafc-9cbe76e28ef3 | -16.04506 | -39.84879 | 2026-10-07 04:21:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbd2d14d-cb10-34d6-b83a-69a927e40021 | -11.70142 | -43.66641 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c7e1df3-fff2-39ae-b96f-1634d77c4b0a | -13.75686 | -43.62471 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dddcd8d-def3-33bd-909d-562216d6daf3 | -16.12417 | -42.07463 | 2026-10-07 04:21:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)
