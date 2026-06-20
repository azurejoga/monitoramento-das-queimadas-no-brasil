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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99cd515e-228b-392a-8bf3-1c296a1d0f43 | -13.2935 | -45.22586 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 631c6a64-0a50-3fcd-91b0-025868d39d88 | -10.54524 | -53.73608 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 259fd0b1-0bc1-35fb-9c2e-42763cfe6c4f | -7.36576 | -49.85955 | 2026-06-20 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57a80533-1359-3ecf-8cf9-bb011d3f2b00 | -10.58504 | -51.77645 | 2026-06-20 04:44:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1203f8b5-7c6a-3aee-b05a-bf24289ed59b | -11.21961 | -46.76186 | 2026-06-20 04:44:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a2e7c8d-a2a6-3fc7-ba0f-aa5d6ff6552c | -10.63882 | -48.64695 | 2026-06-20 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 152e4b81-7f87-331c-8c1e-23b2f0ee9fb2 | -12.51315 | -48.31082 | 2026-06-20 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85de1a4a-bd0d-39a8-91ea-a86cb2f6f899 | -12.43229 | -58.40664 | 2026-06-20 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87e6b087-eba3-3543-a98b-73a384bd5af7 | -12.45313 | -46.52927 | 2026-06-20 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1793e026-ab9b-3c17-9cad-ff20b461a0af | -8.63741 | -47.75204 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3bb5abad-e079-3095-a778-de1dfcb6ae2a | -9.79037 | -48.08104 | 2026-06-20 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4ddafa1-e6cb-33fe-844f-763b60fc6726 | -10.46623 | -49.09114 | 2026-06-20 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e23e46-dad0-306a-b314-efeeeab1d6ed | -7.92647 | -48.25707 | 2026-06-20 04:44:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5883bd44-be96-3d0b-b70f-193af0930380 | -13.19919 | -50.34163 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 13287a9e-7624-364a-834e-54356f593202 | -8.97811 | -47.97906 | 2026-06-20 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c80def79-0d85-371e-874a-29b1910d00cf | -12.51765 | -48.28174 | 2026-06-20 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3065e045-4f7c-3f79-b00c-d17f0b4bd624 | -9.88748 | -48.73198 | 2026-06-20 04:44:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fd7e242-b2d1-325f-ac2e-c715ae0c4d93 | -10.60173 | -44.3253 | 2026-06-20 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d115d916-0408-3443-901c-96c18133b89c | -8.64859 | -47.76833 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d38dff98-06a8-3e08-ba7e-68beb2a285fa | -12.42524 | -58.41519 | 2026-06-20 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fc4dfd8-82af-3be9-be10-596d2717c4e8 | -12.79289 | -44.47087 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a40516ff-b695-375b-a14f-ffb7c23c3906 | -12.79043 | -44.48883 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 634103aa-958b-35c7-8f28-763dd9e6c8e8 | -12.43167 | -58.40983 | 2026-06-20 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99b4c90f-8d16-3c48-84e6-83b0a56992bb | -8.97477 | -47.97853 | 2026-06-20 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63289159-6ce7-3433-8125-9348f5dc0d8a | -8.64355 | -47.75664 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c118fdd-541b-3ad0-851f-b46e8f255090 | -14.85715 | -48.11362 | 2026-06-20 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ebe6051-ac90-3ba9-944c-404a87c4c639 | -11.2161 | -46.76134 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 861bc22d-1f6e-3e92-aeb6-460d009ff57d | -12.42981 | -58.41938 | 2026-06-20 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6565938-6ea5-3140-bd5b-0fc7f93cdaad | -13.38352 | -42.38846 | 2026-06-20 04:44:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 15f91e1f-fa86-33e1-a1ff-4de2c44b56f8 | -13.30125 | -45.2271 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91cb5402-c250-3bad-b935-9dcb1f4b33c5 | -12.54975 | -45.022 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b5908ae7-2a09-37f6-bd27-e676f0262c2a | -8.6441 | -47.75311 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 915589e4-4b8c-3a2d-afad-4bd01c397304 | -12.78786 | -44.47749 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f9e7e97-65fc-3bff-875b-bee50d289ff8 | -12.79239 | -44.47446 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0e104b6-0f48-3b72-bf2b-f68588009b89 | -11.66476 | -56.76417 | 2026-06-20 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf16666a-ff20-39f3-ac5a-aa068d483dba | -7.9298 | -48.2576 | 2026-06-20 04:44:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79bee892-0206-302f-a529-dfe85eb6ca13 | -10.11717 | -52.19968 | 2026-06-20 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99407cdb-9a8f-39f4-ae09-07a0910699fa | -10.59777 | -44.32472 | 2026-06-20 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0684baa1-c3f4-322c-bdfe-7cf5af89ba59 | -8.81604 | -47.0695 | 2026-06-20 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0687173b-879b-3ede-93a4-c507e2e9558d | -8.81661 | -47.06583 | 2026-06-20 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4dce2e8e-049e-3d8d-8962-4a4f9e58dc37 | -13.83248 | -44.7754 | 2026-06-20 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4e378f9-48bf-3cfd-ba4e-a909892b6e2a | -8.68574 | -48.31055 | 2026-06-20 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf09568b-3f5f-3e50-a6ad-bdb1756e58e2 | -13.29949 | -45.2117 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19562645-47d8-37e3-b5a3-4666108b4400 | -12.54195 | -45.02092 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 29d4abb6-b65b-387e-9128-6a43a37de853 | -11.21902 | -46.76575 | 2026-06-20 04:44:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1777e6fa-2db1-33bd-99db-c9332708260b | -12.78835 | -44.4739 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3e8ed03-ea49-3634-b61c-4275d1ea5a2b | -10.5726 | -57.32461 | 2026-06-20 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed44fd0b-b9cd-3b3f-93d4-488596f8f666 | -10.11789 | -52.19542 | 2026-06-20 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acd79bc5-6e99-3da5-9e31-ae56b9181709 | -9.85561 | -61.43278 | 2026-06-20 04:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64869912-601a-3bb0-8028-0f6273163fc5 | -13.19803 | -50.3488 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1749ecc8-bd74-35bf-b28d-babeb97ac566 | -12.51877 | -48.29683 | 2026-06-20 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1ed6c75-85a3-3a55-b95f-0cdcd910c97e | -11.35926 | -52.95638 | 2026-06-20 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 509cadea-0ac4-3816-8fc3-aff67896a140 | -11.63175 | -47.87849 | 2026-06-20 04:44:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dc6dbc7-93c4-351b-9eb6-75b3e535763d | -8.6413 | -47.74903 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 637ea0a3-dcc4-37aa-a076-a702af3532b1 | -10.45658 | -46.45313 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60e15d1b-af93-3ded-949e-19fa3f8b661e | -13.30167 | -45.22454 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0001fbdd-e6fd-379f-ba39-7b8fb25326a9 | -11.81501 | -47.34243 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f625460-001c-3323-aa16-929a8f9b8b62 | -11.8885 | -43.83329 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 07a94e9c-1e5c-3c72-ba84-896e330e10ab | -13.83651 | -44.77597 | 2026-06-20 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 416dce8b-5f71-3475-bfa3-c37d4fb9454d | -9.20505 | -58.06681 | 2026-06-20 04:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d35f6f4a-bb96-394a-92dd-4b25028d3860 | -13.83361 | -47.13075 | 2026-06-20 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03f2ec1e-55c6-397f-a2b0-550075639baa | -8.96798 | -46.94163 | 2026-06-20 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 197321ec-cda6-37f9-864a-6e7ac6800e16 | -12.78688 | -44.48467 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2398fda-2187-3ce9-baa9-18a3b1a99b76 | -14.86118 | -48.11016 | 2026-06-20 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72b7d1c5-60ee-3494-a7dd-9530f7fd67a8 | -7.36916 | -49.8601 | 2026-06-20 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e9c3ee-5902-32ab-9ea5-4828621e531b | -11.07187 | -52.47815 | 2026-06-20 04:44:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87a63608-2f39-3e1d-9923-7267da2900e5 | -11.37349 | -46.31163 | 2026-06-20 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4bf8a54-a42e-3a64-a4e8-c6d94e5a4d20 | -12.7859 | -44.49183 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f09cf75-8b0c-32d7-bd27-432900e59c8a | -8.68629 | -48.30705 | 2026-06-20 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f43f07ae-3f2e-39e3-a830-42b977481760 | -11.79802 | -52.51153 | 2026-06-20 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 258880f8-c383-382d-a155-76571cd4e057 | -14.85657 | -48.11749 | 2026-06-20 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 704d9d2d-b488-3908-a1b5-6169e37f722b | -12.54265 | -45.01597 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e5b1c8ce-0734-32d3-adb1-f73e18974021 | -13.29808 | -45.22153 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59020f14-2c07-3b49-bc52-fb6c17e32ae8 | -12.13742 | -48.26654 | 2026-06-20 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20696943-3d8b-3772-9d84-0670d328ac38 | -8.22667 | -46.84735 | 2026-06-20 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffc8bee3-69f6-36ab-a4dc-0f3bc851f7d5 | -9.62189 | -48.48757 | 2026-06-20 04:44:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95937dc9-5459-31c9-aac9-258bc3b54f27 | -11.18993 | -46.57523 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b4a2e4f-979e-32ab-a6f7-51892f4a10ec | -13.29879 | -45.21661 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68496806-b160-3f62-abe8-843cd9fe3ec5 | -13.38756 | -42.39426 | 2026-06-20 04:44:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 8d80d81a-5c13-377b-8815-de6e6ccf2c29 | -9.47162 | -50.8928 | 2026-06-20 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9847d1dc-764b-3eff-a3ce-aee71f5c452b | -12.54054 | -45.03084 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 664d6016-d028-3b9b-b430-8389b076266c | -12.55046 | -45.01704 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 30d2f1b8-c24c-3136-b5af-5f01f3e0395a | -8.64969 | -47.76125 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4de251f1-c5d3-385a-b7ad-94cde95b0e82 | -12.31377 | -46.73901 | 2026-06-20 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cbeeb4-0caf-3c74-ac4c-5f16c37fb1b8 | -10.46567 | -49.09465 | 2026-06-20 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d15965d-fd83-3d76-8785-84042ecf0118 | -10.79987 | -54.17239 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78ac0b56-8797-3c8f-a5e0-d7851e3b1eb1 | -11.89128 | -43.83444 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f4f8602b-b4ab-3025-9ea4-7de5ba334147 | -11.81559 | -47.33864 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ef13975-bb39-32f4-911f-5d0f28accda1 | -13.2949 | -45.21601 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef18e14c-0ee7-3b5d-a57c-de28bcd00c27 | -9.10465 | -49.65442 | 2026-06-20 04:44:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0922eff-5c02-3faa-ad22-cf80c9baf454 | -9.55878 | -48.67145 | 2026-06-20 04:44:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a2c3477-04f4-3bab-a909-c4516704a3af | -8.64075 | -47.75257 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 27bd6181-307d-3638-9b37-823612f79c57 | -19.15633 | -48.38657 | 2026-06-20 04:46:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed7a07b4-3ec7-3a0f-bbf0-4bd7ab475868 | -16.66457 | -49.13807 | 2026-06-20 04:46:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6ce1b84-f37b-39af-848c-706a37fec5f2 | -17.44768 | -47.15853 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 382345c4-b93e-3203-8ad8-dfc6f56494ea | -17.45135 | -47.15905 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34abcb31-1e46-3781-b252-a1e99de64ff9 | -14.91204 | -51.99808 | 2026-06-20 04:46:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a82410f-592d-3f8e-80e7-938d24b72282 | -18.49052 | -51.69339 | 2026-06-20 04:46:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6a6bdab-af9b-35e8-9a18-717745a4e72f | -17.3215 | -49.61067 | 2026-06-20 04:46:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 591e1fff-7e6b-33f1-a6a1-7bfe07e10ca5 | -17.45192 | -47.16129 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README9.md)
