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
| c8c08356-f0c7-351f-a335-68575074e2d7 | -27.68536 | -48.75047 | 2025-02-08 03:40:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ccd6f6f2-6e95-3d52-9edd-66596e22ddda | -27.68456 | -48.75396 | 2025-02-08 03:40:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 694f53fa-6868-3b10-927b-a05e94b42bf4 | -13.6258 | -55.4602 | 2025-02-08 03:50:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f910e6b1-19a7-3376-a05f-884b894cdccb | -3.13041 | -40.99522 | 2025-02-08 04:25:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aeadc08c-8bd1-36ab-a683-cb91a56729b3 | -7.98396 | -50.70677 | 2025-02-08 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43e5cbb-78a3-3331-b9d2-42ea3d4c5c1f | -7.89933 | -43.91778 | 2025-02-08 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c462fc8d-e0bc-30d1-9010-f4bdccbc5322 | -3.13429 | -40.99581 | 2025-02-08 04:25:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 71e0fe5e-badc-3fd0-84b7-53283f2d1acb | -7.94859 | -49.76202 | 2025-02-08 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04012b53-2bcb-3bd7-a2ca-13daf0c84122 | -7.9558 | -49.76316 | 2025-02-08 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88b6021a-4e47-3182-a66b-0222ff155f51 | -5.72461 | -43.4041 | 2025-02-08 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 794bbf6c-e596-3ef6-9f16-dad0bd3bfdda | -6.17665 | -42.62418 | 2025-02-08 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5af823ad-28b6-3602-bb46-1d0b32679cd7 | -7.95288 | -49.75842 | 2025-02-08 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9381abd6-391c-3701-9d8c-5e7e6be5aaca | -7.9522 | -49.76258 | 2025-02-08 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a77154f-748f-3c73-ac4e-2657a48c23e7 | -13.57414 | -48.66027 | 2025-02-08 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5c30425-c52c-30f1-bd63-d60365860ff4 | -11.74422 | -48.73671 | 2025-02-08 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab31a005-91aa-33d9-924c-94d5fc98c44b | -17.50104 | -45.17467 | 2025-02-08 04:27:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a04b568-a5e4-3bd4-ab8e-91ca97fc18a2 | -12.59709 | -45.0704 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 893cdbb1-c104-3838-ae8b-6bc23742d526 | -12.75026 | -44.83894 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fa2f879-428b-3eeb-a4fb-dfb64ffd2d92 | -10.28457 | -52.83709 | 2025-02-08 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c460aae-71ee-3f68-a528-f79c17b13fe2 | -11.88355 | -46.94261 | 2025-02-08 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e589bf9-ab09-3458-9742-aefe8da19a82 | -11.45693 | -49.32479 | 2025-02-08 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11e3f9ec-cafd-3408-87b4-98a7b6caf6f5 | -11.84779 | -46.64445 | 2025-02-08 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cdd70b7-50ed-3a25-b002-c9d26981358a | -11.44042 | -52.92501 | 2025-02-08 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb821bcc-349d-350c-bf18-8f6fd78e0679 | -14.50062 | -39.38873 | 2025-02-08 04:27:00 | NOAA-21 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06990bdc-b3b2-3cad-a12d-a7ae22a27883 | -10.86241 | -44.78843 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cba679a4-22d9-3c07-abc9-0a0ba86dbe01 | -13.48112 | -44.01706 | 2025-02-08 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c8aef18-4295-331b-b643-ea09a619ed70 | -12.76372 | -45.95652 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03305142-b171-3d5a-aff3-c03596144a42 | -12.80679 | -45.52294 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51a59f8b-bc66-3075-9100-26a0fdf1a1d9 | -11.84834 | -46.64091 | 2025-02-08 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25ada9b1-d63f-307e-a2ef-9dc95f34f32e | -13.25087 | -46.53789 | 2025-02-08 04:27:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b433dd4-3845-3fd4-aa5a-85f2b0a73982 | -11.74087 | -48.73615 | 2025-02-08 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3f38968-2cfc-38f2-a2a4-4ca4165b0a54 | -10.85893 | -44.78789 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70390519-83c3-3c2a-96da-7620d3eebbb3 | -12.53491 | -48.3242 | 2025-02-08 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52ecd72d-75ae-3067-a69e-c70a7b7afeb6 | -17.50097 | -45.17646 | 2025-02-08 04:27:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c87514be-0a3b-3890-9234-3909c7f307ec | -12.35225 | -52.4817 | 2025-02-08 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a09ec83d-12bd-3d35-b778-1f20864e4e94 | -13.62632 | -55.44911 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b6cc49db-fb78-39f0-9d91-ec645a5e88b7 | -16.54292 | -45.14148 | 2025-02-08 04:27:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2565a2fc-61df-343b-b835-d5ed1afa4cd0 | -12.35317 | -52.47651 | 2025-02-08 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e035fd5-cdd1-3b38-894f-018a769cc65c | -12.53435 | -48.32774 | 2025-02-08 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35fa1b73-dfca-3f18-9184-1924279a12f9 | -11.88025 | -46.94209 | 2025-02-08 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e63af9e-98fb-371c-ba0c-aef2ff1c581f | -13.62203 | -55.45586 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 96f30df0-0160-30a0-b89f-316c9f05ff4f | -11.44934 | -52.9227 | 2025-02-08 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0b4738-90bc-35b4-aa55-972876a316ff | -10.86589 | -44.78897 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b4ead6e-6df1-3df1-a407-ec6a21c3a178 | -11.79233 | -44.71085 | 2025-02-08 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f1c055d-5a2c-384c-9085-3a1b2ffba868 | -12.53766 | -48.32828 | 2025-02-08 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d49c59f4-2517-34b6-ac0d-c9f555b44783 | -10.86184 | -44.79234 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 688f455a-75fb-316f-8df4-f90b529d7416 | -15.07762 | -48.9452 | 2025-02-08 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f71e304-4f3c-3118-a597-d23104e1a46e | -13.62535 | -55.45434 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f6b2c09a-8013-317b-b4e1-1d3b96756d36 | -13.62772 | -55.4516 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 43ceac6c-b33c-3815-80bb-42c1b8bec134 | -12.60001 | -45.07489 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 503cf172-30e1-305b-815c-ad41a5c222f8 | -13.62066 | -55.45337 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 755a7ce5-c9f1-3a68-b5d8-13857f56b444 | -12.59652 | -45.07434 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 244a12bb-bb3b-3dc4-84e5-d92f812b5e03 | -13.631 | -55.45007 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 533cd870-449c-3b9a-b233-f300d576e1d1 | -11.00114 | -44.87237 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc5b2b00-51cf-3c7e-8c39-9b0bdd888e13 | -13.62304 | -55.45062 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ea7dd784-b046-306a-bd27-74476af217cb | -11.88409 | -46.9391 | 2025-02-08 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec86a79-8f78-3b37-9960-2fbc01311198 | -11.95799 | -44.66724 | 2025-02-08 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa12bce-53d8-3840-9229-28d1d798e43c | -11.74145 | -48.73253 | 2025-02-08 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48a2374-6246-3042-ad9f-892998cf718e | -11.7448 | -48.73308 | 2025-02-08 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259e494c-9ebc-3e5e-86a6-0b7fb3f862e6 | -9.94611 | -45.17829 | 2025-02-08 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a16218b-d874-3ad8-9f79-cc5642549b8e | -12.74672 | -44.83839 | 2025-02-08 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0f06569-e7c4-3e8a-a059-64229ae564c2 | -11.44521 | -52.92197 | 2025-02-08 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c68e8d5-244b-3551-addf-f9684b61599b | -11.96558 | -48.35043 | 2025-02-08 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20920675-dd6b-3b1b-98cf-878e07f93558 | -10.8595 | -44.78399 | 2025-02-08 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01cd519e-40bf-308c-80cb-1502e3d90c94 | -11.84502 | -46.64039 | 2025-02-08 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 036d3373-34d7-34f0-9206-3d13f9dcc6d6 | -10.28038 | -52.83633 | 2025-02-08 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28af6978-ac72-33c2-9779-d3c1b7df6985 | -23.40808 | -46.55671 | 2025-02-08 04:29:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6eb527a0-b0d0-3151-831a-2483cd77d85e | -17.06783 | -49.37937 | 2025-02-08 04:29:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb40c98b-b072-3a20-ac75-42f7cbd7e84f | -18.67909 | -47.50681 | 2025-02-08 04:29:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 509497bf-aac8-34a2-82ff-b8f47a61c2b0 | -22.90281 | -43.75329 | 2025-02-08 04:29:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 97584d85-2b61-33d7-883f-b778017f6896 | -20.1639 | -46.67845 | 2025-02-08 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5f2d7ad9-1820-35a5-b057-fd47bd19e8dc | -17.01028 | -49.78122 | 2025-02-08 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b3234a-845a-320f-be09-31c21992f0db | -20.1674 | -46.67907 | 2025-02-08 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c272f71-00f4-3714-9685-813681e1e2aa | -19.97165 | -44.21796 | 2025-02-08 04:29:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe3ce831-38c2-3d17-877d-bec6ac8d3bf9 | -23.06165 | -46.6407 | 2025-02-08 04:29:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 863ea6a4-f067-306d-b772-7b509e29c423 | -21.89249 | -53.72499 | 2025-02-08 04:29:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d326059c-2ecc-3eb9-a5b0-5bb193b32595 | -16.3631 | -57.71985 | 2025-02-08 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 877d7297-460b-33b2-8cbf-bcbada78130c | -20.16506 | -46.67014 | 2025-02-08 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dc1f1112-2da6-3653-ba83-08517618b16b | -20.16448 | -46.6743 | 2025-02-08 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dc1d30d-b3a6-35b2-9249-e7fcc5cb0b8d | -23.40679 | -46.42278 | 2025-02-08 04:29:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d8b91ad-3e7a-3245-9a78-c969d29325f7 | -18.58418 | -39.94705 | 2025-02-08 04:29:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 59c11aea-b6e5-3323-8cde-070610c51471 | -21.05962 | -43.86051 | 2025-02-08 04:29:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64ccd2f3-a031-3b46-8bda-349c5133a551 | -20.16798 | -46.67491 | 2025-02-08 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64b1baf7-bcbc-3e5c-8e24-cdd65bb7ee98 | -23.33929 | -46.77033 | 2025-02-08 04:29:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e056f198-2f25-3c32-aa75-d3efa382c764 | -20.21325 | -43.94632 | 2025-02-08 04:29:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 21f6af05-3a93-3dcf-9948-c863024a2fe4 | -19.45543 | -45.30767 | 2025-02-08 04:29:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49434721-8484-3357-b4d9-0a3c152ddad9 | -21.89334 | -53.72029 | 2025-02-08 04:29:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07724946-2c65-3922-9759-8aa941aa39e1 | -23.33783 | -46.77281 | 2025-02-08 04:29:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d9ce31a-4c95-3b50-b1fe-e61f4b73a8f0 | -23.40442 | -46.55623 | 2025-02-08 04:29:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0282d06-8c5e-3d35-b45f-0555a7c3a953 | -20.70059 | -48.81133 | 2025-02-08 04:29:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cfb25bdf-e3e8-3bd5-8910-24815ac5e055 | -20.16681 | -46.68325 | 2025-02-08 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 80910dce-53cf-3b53-99cd-f4ff2e09948d | -21.19737 | -44.93665 | 2025-02-08 04:29:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a52a0d2-4075-3f30-a8e3-ad989b97b562 | -22.58291 | -48.01726 | 2025-02-08 04:29:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3150094b-a6ac-3674-9503-7a17cd50400e | -21.05913 | -43.86457 | 2025-02-08 04:29:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 689515d2-021f-36d0-b11c-eb6378fa6720 | -20.89992 | -43.8204 | 2025-02-08 04:29:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 85470e4b-bae8-32a8-badb-5f80fd946ab5 | -18.58349 | -39.95366 | 2025-02-08 04:29:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ace1471b-8dff-3c18-8d96-56ae36e68c75 | -23.3387 | -46.77491 | 2025-02-08 04:29:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 63e16e22-dbe7-3b09-847f-beebfaecc4e8 | -26.42505 | -52.33226 | 2025-02-08 04:31:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d613391f-1834-3f08-b893-3381a044ec72 | -22.88366 | -52.72932 | 2025-02-08 04:31:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f88d2525-c35a-35ec-9354-3ba9b7ce95df | -28.57979 | -51.07729 | 2025-02-08 04:31:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
