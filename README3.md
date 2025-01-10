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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3bf8cff-12a0-3c1e-8417-e7dcfd9da949 | -7.17517 | -35.01686 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 97a6f73a-90cb-3736-adc4-0955f8c45791 | -7.17451 | -35.02131 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 9ed0c6af-726b-33d5-a1af-69144af35bb8 | -8.23017 | -35.50273 | 2025-01-10 03:55:00 | NPP-375D | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5424c887-f703-3e18-9f51-8c7f48674aec | -7.1789 | -35.01741 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| b95e64bf-6414-3691-ac75-1f18a4010c8d | -10.6285 | -37.06185 | 2025-01-10 03:55:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4c07e94d-74b6-36c5-9e56-4483ece0f6c1 | -8.63659 | -35.79259 | 2025-01-10 03:55:00 | NPP-375D | BELÉM DE MARIA | PERNAMBUCO | Brasil | 2601508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7f14b413-7152-3831-a92e-3f708f814790 | -7.96682 | -35.20258 | 2025-01-10 03:55:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6c64c57-e419-3c8e-ab92-a6b5b8b23d42 | -10.18178 | -37.44475 | 2025-01-10 03:55:00 | NPP-375D | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5a8579a7-265f-3d17-b292-cc8a5221fe1e | -7.1721 | -35.01184 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3d24b88d-aa14-3dd8-9518-3f2c162f3853 | -7.53031 | -35.30103 | 2025-01-10 03:55:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 63ffa355-2c5f-3c70-b610-da212306b1f6 | -8.42061 | -35.23835 | 2025-01-10 03:55:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ec9b26ba-bb70-330c-bf9f-ae5034d54f8e | -7.56336 | -37.03946 | 2025-01-10 03:55:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ccfa3352-60d6-3098-b885-0e78fd099f1c | -7.16837 | -35.01128 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8da44644-c650-3dac-87d4-f4481cb67377 | -7.80732 | -35.16749 | 2025-01-10 03:55:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6adb073b-11d4-3f61-bfc3-1188756bacc5 | -9.86381 | -37.1015 | 2025-01-10 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d987620-b932-3c16-92d6-22f905fc8763 | -7.72857 | -40.18316 | 2025-01-10 03:55:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b30b1f34-a4c5-3959-ba59-eff98739be0d | -8.40384 | -37.03637 | 2025-01-10 03:55:00 | NPP-375D | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 29fb5070-784a-3ff7-821b-0250e64d5d05 | -7.16771 | -35.01574 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e856fd23-1644-3b67-9cd5-db97e56f6538 | -7.23168 | -35.10453 | 2025-01-10 03:55:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6da50eac-f648-35d0-bbab-7d05d97ba9f6 | -7.53095 | -35.29669 | 2025-01-10 03:55:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| daf69515-3f7d-37a0-8121-d5dbf0b9b6e4 | -5.93835 | -44.44548 | 2025-01-10 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 491ae53e-b753-392d-ad2b-b8fd8a961312 | -8.42436 | -35.23884 | 2025-01-10 03:55:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 41b39aa9-611a-31f1-979a-263629bd0c0c | -7.17957 | -35.01295 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7bff7ab1-b100-30e4-bc3d-e5b8f4993b75 | -7.5282 | -35.29818 | 2025-01-10 03:55:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c8c8018-da6d-34ab-b55b-e938502bd36d | -8.63658 | -35.79065 | 2025-01-10 03:55:00 | NPP-375D | BELÉM DE MARIA | PERNAMBUCO | Brasil | 2601508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 445cde9f-d0d8-3fbc-9c4b-59de0af59b7f | -10.62499 | -37.06129 | 2025-01-10 03:55:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c8b79f0c-4df9-34e6-bd5c-404ecebb3649 | -7.17584 | -35.01239 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 56c19c45-4644-3c90-9bed-a9d998c27545 | -10.09534 | -36.28874 | 2025-01-10 03:55:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c05c6574-47f1-34ef-a132-29802c83d7ac | -7.23017 | -35.10651 | 2025-01-10 03:55:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a3786713-179c-35f7-9316-0864ef894f87 | -7.23103 | -35.10894 | 2025-01-10 03:55:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f7561a55-bc5f-31bf-bdb6-bf473f808354 | -7.8036 | -35.16693 | 2025-01-10 03:55:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d58aaa1e-f481-36bc-b421-5dbc79aacbd2 | -7.17144 | -35.0163 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| db42e583-bf7d-3bb2-a638-19590f32120e | -7.53399 | -35.30169 | 2025-01-10 03:55:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 238dd178-2bd1-31dd-a9cc-0017bb205e04 | -8.46335 | -36.95978 | 2025-01-10 03:55:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c45f542-6d01-3302-8ae2-4fd447db75c9 | -7.65699 | -35.06259 | 2025-01-10 03:55:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f9ddd710-73f7-357b-9f4e-9f21c2e91c7b | -8.33477 | -35.13925 | 2025-01-10 03:55:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8be16378-66b0-338b-9150-63c891671bc8 | -6.78131 | -37.51989 | 2025-01-10 03:55:00 | NPP-375D | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e956b8e8-5e18-3ce4-b3b0-fa5626177108 | -6.78076 | -37.52346 | 2025-01-10 03:55:00 | NPP-375D | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4dedb88e-ebda-3be0-ba0b-3ee79cdde689 | -10.27608 | -36.9636 | 2025-01-10 03:55:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7cbdc3fd-6633-33c0-b095-b9d1cf4caf8f | -7.17078 | -35.02075 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8c3ef501-cc90-3169-a41f-dfa889959699 | -10.09173 | -36.28819 | 2025-01-10 03:55:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2e7d329-892f-31d0-8ecf-ecc17feff50a | -7.17824 | -35.02187 | 2025-01-10 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| e69f2888-605d-32e9-b9f5-e299d8492f35 | -17.65451 | -54.16851 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9e27af5-cfe0-3793-bfaf-cbe0d5a11ee1 | -17.31564 | -53.73452 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31ce54fa-fe2e-3a4c-ae81-185a1b38bf33 | -17.66298 | -54.17102 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62e2aff7-8661-372e-a1ae-b671ca81774f | -17.31656 | -53.72957 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7514836a-2303-3f17-b416-d7cdb8624eb9 | -17.31682 | -53.72917 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 558ace57-4637-3889-a815-ca331c4576c4 | -17.6617 | -54.17674 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 433df9b0-65f8-38f5-8e96-e6dd1d1603e6 | -17.31535 | -53.7349 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 587f40bd-565e-3b5a-89ad-ddb491f1fb04 | -17.65966 | -54.17591 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7b80370-320f-3e84-9c88-6fd4c31ad84c | -17.65652 | -54.16926 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5055910-8c8f-3eb0-83fc-be55b561e3e1 | -17.65522 | -54.17502 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f161b7f9-15fb-3f1e-ab7e-718bb69d2e7c | -17.65317 | -54.17427 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bb594c1-036e-3fda-b6d4-c25f74bc678a | -17.66098 | -54.17019 | 2025-01-10 03:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d91c3711-770e-3bb3-89d7-cd24f50ab4dc | -20.87717 | -49.87183 | 2025-01-10 03:59:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7a3dac99-9dc8-3f31-9c9d-795925d65139 | -21.62686 | -43.46894 | 2025-01-10 03:59:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5750be44-f6b4-3a6e-9dbb-10813e7236dc | -20.97665 | -49.77349 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 58bf30b8-f9e5-32aa-8d9a-275e73f36d68 | -21.6275 | -43.4651 | 2025-01-10 03:59:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c964a512-b4cf-3d53-8198-cec26c6cf713 | -21.30438 | -52.06405 | 2025-01-10 03:59:00 | NPP-375D | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1737e219-8051-3cf7-8871-404c9059b8fc | -23.70449 | -46.47839 | 2025-01-10 03:59:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6645d6ff-faee-301b-865c-d6ed04289537 | -23.3539 | -48.5268 | 2025-01-10 03:59:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d2d3d23-20ee-352b-b7c9-a56e2214f79a | -20.97999 | -49.779 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e5c8568a-11f0-3cf3-919e-ce592e49f2e3 | -20.98108 | -49.77361 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 335a6e87-6caa-3062-afba-2c59e695d163 | -23.59253 | -47.43799 | 2025-01-10 03:59:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ef6cbc5-c373-34b7-b468-a4cf89425e03 | -22.54761 | -47.2558 | 2025-01-10 03:59:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9df81ec8-0b87-3fec-bb4e-0bbe190cd68a | -22.01575 | -49.11804 | 2025-01-10 03:59:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a600aef6-baea-375c-af04-3aea008b85c5 | -23.10319 | -52.09892 | 2025-01-10 03:59:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 352f54d0-e150-3075-98b1-ea79ba8742a6 | -23.98564 | -48.91756 | 2025-01-10 03:59:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ad717ec-9fce-3b3f-bb11-6b8dc0fb5e48 | -20.98469 | -49.78007 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5fef247f-09ed-3c64-aef4-b11d12e7f5f7 | -20.98491 | -49.78102 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5e41daa6-4159-3552-a39f-adf88e6b6f06 | -23.98229 | -48.91882 | 2025-01-10 03:59:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca59f742-a8be-3c5f-83c2-82dff354196a | -22.01043 | -49.12152 | 2025-01-10 03:59:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23e5e3a2-a1ab-3a91-bf17-effd86b195f8 | -20.98133 | -49.77459 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b473c715-0d9b-306f-b6c9-203a1e079f92 | -20.98021 | -49.77996 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3c6c95c3-1cdb-3b6d-9c3f-7e4d2e6cd7a3 | -23.35309 | -48.53091 | 2025-01-10 03:59:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79e582ec-9a3f-35ce-a8d9-95a2a8ba0049 | -23.34892 | -48.53002 | 2025-01-10 03:59:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 09118a60-333a-3b71-aca6-67a14f707050 | -22.01483 | -49.12259 | 2025-01-10 03:59:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88281d95-d236-3111-8806-16d5cb4587b1 | -23.1025 | -52.09826 | 2025-01-10 03:59:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c14c1a64-f17f-3482-bd14-5301db9a9912 | -22.78487 | -43.75872 | 2025-01-10 03:59:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d0cd47b9-2559-3e87-acc1-2adba0b524e0 | -23.98649 | -48.91978 | 2025-01-10 03:59:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 247754ce-dafb-35ee-8b27-7e922e00dfbb | -20.97639 | -49.7725 | 2025-01-10 03:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2125ef75-40c0-3459-bdcf-91ad8f55a377 | -21.30358 | -52.06766 | 2025-01-10 03:59:00 | NPP-375D | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e9e8203-a42a-3317-94d4-949055a38086 | -29.20244 | -51.50298 | 2025-01-10 04:01:00 | NPP-375D | GARIBALDI | RIO GRANDE DO SUL | Brasil | 4308607 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a9d771dc-0cbf-3c40-8dbc-8e2ea2b6df05 | -2.89553 | -40.00086 | 2025-01-10 04:16:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b08a4b93-8bbe-3815-87ca-b87e743d6503 | -1.57602 | -45.77394 | 2025-01-10 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 966d1c94-0ac3-3952-b661-793bae70e497 | -2.42685 | -48.05653 | 2025-01-10 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27f6c9c3-9177-3cb8-bd1e-c1a83077ad76 | -0.75476 | -47.75943 | 2025-01-10 04:16:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63503021-1ed8-32d4-ac2c-b365df312579 | -2.89478 | -40.0029 | 2025-01-10 04:16:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7aff02f8-3570-31a9-a766-aa813a342361 | -9.88406 | -36.29286 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c5b15761-e4e5-3c5d-a39b-cc5670bf3017 | -9.88175 | -36.29428 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| cccaa4d3-3a1a-3103-a5f3-92375dcf474f | -7.80603 | -35.1659 | 2025-01-10 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 62e0e917-d3b7-3fd1-88f3-dfe836d9713c | -5.93818 | -44.4439 | 2025-01-10 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 345f0e11-0796-363d-8fb7-603541f56708 | -9.87247 | -36.29821 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9c744350-8a06-3808-a13f-20a0ff6315b0 | -7.80412 | -35.16961 | 2025-01-10 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bffe421a-a42a-3988-8c54-3ee6a37307f6 | -2.79453 | -54.17019 | 2025-01-10 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1732d659-5d24-3018-b3b6-621d75dfd1d8 | -9.88218 | -36.29088 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| a59902cf-e1e8-3894-b96f-fd89fec341ac | -3.0977 | -54.60286 | 2025-01-10 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4a9eeab-69ef-303d-b3fb-857cb352da56 | -9.87736 | -36.30231 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 065db236-17d5-31f3-8637-739820bbac09 | -9.87917 | -36.28875 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| f3b3b20f-4451-33fe-95a8-80321eadf069 | -4.66965 | -37.82946 | 2025-01-10 04:18:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
