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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52bfa200-ac01-362c-9280-60e632e05bbd | -12.49581 | -50.24387 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fb36ac2-9fd0-32d8-a9a0-0396e820465f | -11.84178 | -44.96091 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02d59090-1e25-39c1-8d99-e22ff18b3652 | -12.57188 | -49.89683 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55330834-af6f-3de2-aa4d-9b167067365b | -11.27413 | -47.82092 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1583061-14f6-3c1d-985d-9033c3d1185e | -13.21511 | -48.49448 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d28e5fda-cff8-3325-922c-90484d055e7f | -9.93412 | -43.7161 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35502b46-f0c8-38a6-80ec-65d8c81f0b75 | -11.08687 | -47.71203 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83fe6fce-dbec-3ef0-a7b3-fe45425699c8 | -12.41263 | -54.36543 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70560a8c-3926-3e62-abcc-cd05efdcca96 | -13.31609 | -47.00501 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11ffc94a-b79a-336c-852e-81aff2a8f4d9 | -16.36794 | -47.05747 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a724afb-69b8-321b-ae5d-fc583988971c | -9.80351 | -47.82996 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a491b46a-2e8e-38cf-8aba-e028b8b34d09 | -9.93556 | -43.7486 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b10eb3a0-fa0a-3d64-a9e5-c00cc0223f4a | -11.60482 | -45.06161 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1e9b88b-e7e3-3051-a192-99cd68fe88e2 | -10.84652 | -48.00614 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb85ee38-abf5-341f-8c87-7d9d301f1ac0 | -14.29888 | -45.89777 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9989171-8060-3917-8500-b0140e4e4a23 | -13.04803 | -47.05726 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54009e82-be87-35e5-9c58-f7a02217e929 | -11.59813 | -47.23156 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c89e3eb0-a707-3552-9a75-5068cb90eae6 | -13.94474 | -48.13287 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce1cc58-757b-3099-abfb-8ccf732c5fd3 | -13.20938 | -48.50542 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b781c88b-3c9e-386a-a6c3-d5a219e456e6 | -13.67854 | -48.0892 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 477b5499-1904-3765-872f-d8c22bf8cf31 | -12.25519 | -47.83034 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b3714a-3a6c-3894-a90f-5e3516b8d811 | -11.5231 | -43.54634 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 728da12f-033e-3748-8e2f-96345e7899f8 | -16.0622 | -51.0098 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03fc2909-e091-3c1f-8b34-eddfd228176f | -11.67114 | -47.48923 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fbd0e6d-a485-3d96-856e-87c7ea887b97 | -11.18214 | -47.18952 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c037dbe-4a56-3779-b131-87ae005cfac9 | -12.81544 | -47.01669 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67aa537a-9d76-3104-a097-723ed0f3b03f | -11.00922 | -46.5897 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c3ca9b9-8116-38fd-bfb6-6b414f629908 | -9.84358 | -49.96025 | 2025-10-02 04:51:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8666c37-f729-3687-9fbe-f98965c17512 | -14.41802 | -46.13387 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a7bc864-42a8-3163-b4c7-76c91c3408b7 | -13.39644 | -47.78425 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| a45f8023-c2df-3416-9290-bb19d2e88d9e | -11.59443 | -47.22035 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4766ddbf-7cb7-3f74-8191-83950755c5fd | -11.85858 | -44.99418 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53895a1a-0acf-35e1-b239-64d0f01438fd | -9.45174 | -50.90052 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cd0c66d-35e4-3012-9ef8-7e00f2b22b36 | -13.01185 | -45.20548 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d6f29f7-7517-3929-ba5c-09af88cfe317 | -15.24631 | -48.08422 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d057ea-e319-38a9-8b5a-e57eb7c2efb8 | -12.41763 | -54.35539 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcdd598a-2ea9-35f0-a78f-0f4685db4d00 | -14.86929 | -48.29493 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f1fd3cb-efe9-383d-9266-1e0dff4544ad | -14.91919 | -47.2309 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2542ac6-c494-37a9-bc9d-d7631032b8c2 | -15.79552 | -43.73681 | 2025-10-02 04:51:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef89b52-dca4-3755-8b8c-e4c63812a07b | -14.70299 | -49.61264 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b879871-c114-373f-876b-1a90df712e82 | -10.85055 | -46.58879 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5947c1e-4224-35f5-a9de-96f6095be558 | -11.46777 | -44.96837 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7d2b034-c76d-3c4b-a2e7-7cc0c735ab95 | -15.94441 | -43.32549 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fafdd1c-3572-368c-b65b-38db68a3b9f1 | -9.92552 | -43.74001 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 397b6552-250a-3754-9740-2ab9b2b0ea7f | -13.81021 | -47.53556 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 542b886f-3f76-3200-9c4d-7fbf893bda93 | -13.17592 | -47.82607 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 460196b2-8e89-3c9e-9350-be68cf24df64 | -10.82448 | -47.95245 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b00fc3c0-80fb-3bce-9dd0-f62c289f47bd | -13.16366 | -47.81841 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e7efc34-8b39-36bc-905c-6344252f0794 | -10.99402 | -46.52945 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4605e565-4a9f-3c95-b84c-ad6b386bdc19 | -9.92435 | -43.74371 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| d9b625ce-bbcc-35b3-b6eb-9155e4628afa | -10.23858 | -50.31936 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1f1164b-de68-3fdd-92a5-5ac430e34402 | -14.31675 | -46.00074 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c3f28e4f-bc1d-3976-b05c-05c3718cdc44 | -9.89572 | -45.95086 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b1eb303-65f2-38e0-9b7d-5901a7ddb4c7 | -11.41942 | -43.50299 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd1a2c3-4ce9-3e9c-8679-0fa2698b11a2 | -11.35862 | -44.96912 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27888955-bedf-30d5-b198-6a657f7ffa86 | -13.30287 | -46.9987 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2a29751-ca5a-34bb-82cb-794e696d3ddf | -9.93333 | -43.7662 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a4ff17cb-df79-3b89-860a-15a30ebc3cf9 | -11.92879 | -47.88635 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f218650-a1b9-30b3-b265-4a059fbd3f46 | -13.96325 | -48.1109 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da93d1b-d5a0-354c-9edf-be82dfab91e3 | -10.68488 | -48.56107 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69309917-7d25-3f49-9a8f-e94cb2afd77e | -14.21852 | -44.93545 | 2025-10-02 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e2210a-1c36-373b-a5d5-ae38931a7fd6 | -11.13775 | -43.3876 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74898d51-efff-3f68-9774-290d50a28f8e | -10.81766 | -46.62671 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71d60c4d-a0b3-3b14-b158-9022f3cd4314 | -14.21968 | -46.12001 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5bdd544-e79e-3ffa-af44-4395f031b8ed | -11.59304 | -50.1721 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 150321db-5798-3041-97ac-081e3ec55cd5 | -13.01583 | -45.21561 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3507aa0-7b9d-31df-a495-66a768f64d5a | -14.90668 | -48.32713 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cec58fc-ef2d-3182-acb4-f98c94976661 | -12.0204 | -46.63604 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbd2358d-81c7-38f8-8c57-318b05780af3 | -13.80961 | -47.5401 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4f08e558-0152-3016-99fc-62c2b4e40da1 | -10.80262 | -44.24073 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 345e62af-7e28-3102-9a1f-9b9d7da1febb | -14.40647 | -46.09549 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf01ba6d-2534-3dad-b23f-eead92fda3d1 | -9.70923 | -48.94791 | 2025-10-02 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e2571d2-d0f4-3d95-abf3-6024e06ff6bd | -11.01118 | -46.57539 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54118996-becb-31c7-929b-276d23f28601 | -13.40956 | -47.786 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8268af0-38b0-3967-af33-bb1ab6c4bb6a | -15.99206 | -50.37376 | 2025-10-02 04:51:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 819612cb-132e-398e-9055-0ffef716f8fe | -12.90494 | -54.74878 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f1409f-527b-366e-afb0-44e2c0d8d72d | -10.65053 | -48.50213 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e07045c-540b-3870-b3fe-9047a9b9bbb0 | -14.35384 | -43.84034 | 2025-10-02 04:51:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8186ba10-32bd-3cff-9909-993e637abcd1 | -13.70342 | -48.61539 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a10e9159-2a27-3df8-bf17-a622ab102a2e | -14.18838 | -46.12898 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a96b5d91-09fe-38d1-8959-fc526c7bface | -15.5971 | -46.92111 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eab50764-c549-376b-b3c7-daaa27ae39f6 | -13.17202 | -47.85551 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 920fed41-9fc2-35f9-97c7-d18ca4cd533c | -9.91381 | -47.70978 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d220dcab-9a68-3f49-9529-740650494ed5 | -11.10508 | -49.80938 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7b749cc-a283-3626-87af-ed484108e4c2 | -12.91117 | -47.17787 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5897b89f-350a-34d7-9ec3-53c025a1c6a2 | -13.80314 | -47.54231 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7f03f783-ff0e-333c-a949-21aa750332cd | -15.56015 | -48.18218 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba62d7a0-ea4b-3820-9464-c064f0e90f86 | -10.65351 | -48.50976 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4cc9534-ed89-3878-8ab4-89ab4ee77f29 | -15.26139 | -49.29142 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5620ed1d-f98c-3a3a-98c6-7d5528465f05 | -13.56482 | -48.10392 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c901d124-b2d4-3127-a9d4-6e51835fdaca | -9.94879 | -43.73227 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e9a3e3f0-fe6a-3498-a4b7-c4dc1bc2b62b | -11.21917 | -48.21221 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54b0276f-c0f9-36d3-ac75-07197868ee49 | -13.2075 | -47.3427 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19e65e75-6484-36a2-954a-b848b2627e3c | -12.94259 | -48.43464 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc68d773-890f-3cd1-8ded-cee05cfce583 | -11.35612 | -44.96668 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9603517e-04ad-31d2-8922-3308b38bcc0b | -10.48548 | -49.37047 | 2025-10-02 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44cd4bd7-7f8f-38b6-b7c6-931d885ae3a4 | -11.47367 | -45.00499 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2004717-f940-3b20-b458-5d7c6dfd6a40 | -13.21774 | -48.44403 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f1ce6a0-c28a-3dda-91a8-b165987abd68 | -11.47949 | -45.00024 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 925a4328-a513-3e9c-aee8-09df9843dfb6 | -11.14097 | -43.38033 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README132.md)
