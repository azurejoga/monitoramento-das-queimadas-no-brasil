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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abb7072f-771e-397a-a295-271bc941a23f | -14.30633 | -47.06644 | 2025-08-22 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be2dda9f-f92c-3ea8-960c-c55a934d77b9 | -14.65135 | -54.86098 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e15b46df-fb93-3af4-b667-049fd27bc1bf | -13.00186 | -45.22503 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 764bfc8c-62db-3a4a-a83c-8df917ead780 | -14.99635 | -54.86726 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adf5c5c5-6522-3a82-8327-167661d1ebdf | -19.93928 | -44.57801 | 2025-08-22 04:21:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5e3f48e4-1b7d-3fc3-9998-c507bffcfe86 | -14.86489 | -48.32113 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 268af987-5505-3803-9f99-e0340e4ebf51 | -18.61905 | -44.26318 | 2025-08-22 04:21:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bd7c75d4-b8f4-3cda-9cd9-1458cd41e4a8 | -15.89679 | -43.45419 | 2025-08-22 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| d24e6d71-ce16-3e02-a967-680660301200 | -13.14747 | -46.89928 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 65aef49f-db25-3d0b-9543-814b4b4a42c8 | -14.59139 | -54.77887 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa7f22b4-1673-329f-a461-017156266a3e | -15.5033 | -48.04941 | 2025-08-22 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 132246d2-48c9-3a80-9868-d70275030bc2 | -13.49985 | -47.05285 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd7cf77e-e36c-36b6-b6e4-3ac87c4002a5 | -14.75583 | -56.04584 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1489d56-4025-3564-a2f5-94d0f1415341 | -14.46958 | -48.35794 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8eee7e6a-0dd3-3b99-8c25-397756595605 | -15.56273 | -51.69891 | 2025-08-22 04:21:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4128d8c6-fed9-31ca-aab1-4962271adc6e | -13.37831 | -47.49326 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 239dbcde-41ef-382d-96bd-f301c9811e0a | -14.88438 | -47.94799 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23ec0d85-f23d-3b94-b159-c8e56b7f28c7 | -12.93039 | -46.18943 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88b829c7-be5e-3cdc-885a-1ec94a56d7de | -13.43674 | -57.16811 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f968e10f-76d9-31b7-8503-62afdab00a66 | -14.91647 | -49.45284 | 2025-08-22 04:21:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c69b70-cf4c-325a-aedc-1bd4e4dbd93d | -13.02743 | -45.19217 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 535ccb2c-3a43-3830-bc4c-09fea86f9e86 | -14.76499 | -45.43198 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d9a4df1-deb8-3d70-836a-c5805930edf5 | -12.92379 | -46.16666 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a3e7a8c-fadd-3faa-a656-649db3f98552 | -14.6465 | -54.85982 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fabab44-f878-3302-bb05-597244340e65 | -13.03692 | -45.19736 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17b42721-13c1-33a4-a408-65c4906b8737 | -13.42922 | -57.17543 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2eceb04-a062-328a-8016-002bad5bb483 | -15.7368 | -49.4511 | 2025-08-22 04:21:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29c97dea-5dbb-32ca-a21b-8e1643dc8c95 | -13.14706 | -54.91815 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd25c7c-0e35-3d66-a27d-a5ffeb845cfd | -12.9315 | -46.18238 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4a284ce1-58a6-3833-97a7-ecbc255f8444 | -19.96998 | -44.92603 | 2025-08-22 04:21:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da90ab82-14f2-3d8d-b522-4e3c2b7f9bdc | -16.18627 | -47.98977 | 2025-08-22 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cfe19d9-bb03-329c-8bde-8ac54e58fa7b | -15.89251 | -43.45802 | 2025-08-22 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 2fc37b95-b4c8-3581-9061-d55e4fddd405 | -13.19527 | -46.8963 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d60b0ce-7157-315f-8123-0e9781c4b26a | -11.34128 | -55.42614 | 2025-08-22 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e74febee-eaba-3195-96cc-c586b1b1944a | -14.87035 | -47.94955 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b374ad4-7834-3ec4-bbda-c45981961ff8 | -16.78424 | -47.65245 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a61ab16-6487-3da3-8167-c7182600d2b4 | -12.95359 | -46.25853 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd2b6807-b115-309d-8339-ccff42fd1bad | -13.00465 | -45.22916 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a76097a-356b-3cb2-bedc-7156fb43f9d0 | -13.15571 | -46.91181 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebb9da6a-614c-3904-b8f3-b358d182718c | -20.45238 | -41.68009 | 2025-08-22 04:21:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d2b04a6-5e2d-38ae-96c0-2ee27e96a4bc | -14.46217 | -48.36051 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1978f34-a85d-3e10-9277-24c563efec78 | -14.89082 | -47.97189 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c7894001-d7cc-3988-9c61-1bc26839e8a4 | -18.30934 | -45.51793 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f18c3f88-1a62-3430-aee3-cd06c6de8cab | -15.58585 | -50.31115 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5505c1b-d93e-3eb6-820c-83328e87e36d | -13.03689 | -45.17517 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d67f8905-97ab-3708-8d8c-d71e5e89a83f | -13.62924 | -46.88065 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 271dfe3a-f348-30f3-95b4-70405f1668ac | -12.98564 | -45.22641 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e47f3d09-c1b7-3bdb-b6ab-56f99c64e613 | -18.27844 | -45.51326 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c4cad40-396d-3871-9171-12095758be16 | -12.9293 | -46.17479 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c27c11b-56e2-3156-8333-bf0d0e2d310e | -13.16861 | -46.91381 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61595bc3-68ee-3954-a0b8-aa4466e20158 | -18.26987 | -45.5239 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3164b756-6b3b-38ef-a89c-c92140dce1c8 | -13.02906 | -46.33961 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ae1ab09-77ac-3597-85fd-ac4d1043072e | -16.55473 | -49.26587 | 2025-08-22 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef4bee4d-6ba9-3a77-bb0e-0b9b04c00ba9 | -12.51133 | -57.65964 | 2025-08-22 04:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5e5c77e-eb1b-374a-a5b3-3067bed2f510 | -20.27155 | -46.69492 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2377d92-d09e-3724-8d3e-1a16f4591718 | -12.98388 | -56.88317 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14032498-58e4-3983-859a-e60a58b2a698 | -12.99527 | -56.88594 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb89bf55-6911-3ae7-9771-c2fba78c8330 | -14.83782 | -47.92496 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96f34c0e-cbf3-39ce-b43e-83fdebe32e8e | -14.62218 | -54.85427 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48c5a30a-4743-3cb4-98c5-5551b9109963 | -20.30133 | -46.63397 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9af1c787-61d8-3c82-849e-3906c8890c2b | -13.03302 | -45.20045 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b84cf82c-bd76-3e97-a9eb-ea6cfc6c59ba | -18.29331 | -45.50754 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6749ad38-207f-3a48-9d7e-f2bab8690212 | -12.99446 | -56.88606 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3075cb5-5a28-3b65-9ab7-fadf5af32f28 | -13.45969 | -47.05024 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2778f689-5d6e-385f-9be7-6b0b1a7ee3c7 | -13.14202 | -54.91711 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a8bf8f-b952-3098-9e0a-c0d80211c3b8 | -13.49103 | -47.04403 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36204e44-a75a-3d8b-86f6-451a728eaacf | -20.24477 | -46.65541 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14ac2880-3cad-30e6-ae95-9c67911a854c | -18.27501 | -45.51271 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67539854-9b1b-304f-9833-025f14be9c41 | -14.62833 | -54.8488 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07700ac5-df61-31db-95c5-b80b5e6387d9 | -18.41527 | -51.97316 | 2025-08-22 04:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d855628-f481-37da-9349-73a3a89f7d86 | -18.29389 | -45.50359 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bdba5e5-45ed-30ae-bb1b-6fc26632305d | -18.93906 | -41.48863 | 2025-08-22 04:21:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f0f8a50e-27f1-3b07-96af-ebf0de013214 | -11.9017 | -55.89263 | 2025-08-22 04:21:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 358d64ba-9766-3600-b158-d0075a7c8f01 | -14.47638 | -48.35909 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7735edee-f968-3528-b501-6a3bec96514f | -13.02074 | -45.1911 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8100a98-65b0-3302-aa2c-b61e57e81841 | -14.74532 | -56.04356 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ece59cf1-5890-3005-9be5-7af19b9c8a76 | -14.76498 | -45.40947 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7611e983-b0b4-3a52-bab9-2bc32003b684 | -15.73749 | -49.44704 | 2025-08-22 04:21:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c997e4bc-868f-35a6-b50e-d54a979b1797 | -13.02631 | -46.33554 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9048679e-1a39-3c1f-800a-6458d3d0b53c | -13.58586 | -47.04509 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f5c84c-2c20-3dfc-8ccd-33d23a4dfce1 | -12.98552 | -56.90108 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 994d0282-22f1-3cad-a77a-749a1f2f5e49 | -16.56161 | -49.26713 | 2025-08-22 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec3e2e4-e4a8-3e06-8f80-ef43dafbe6fa | -12.51232 | -57.65673 | 2025-08-22 04:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff1d6f45-c4ab-3bf2-9306-a764092b0cfa | -14.89502 | -48.05192 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ef68cf3-6c78-3134-a201-996bed22a66a | -13.63643 | -46.87822 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32412149-e97f-38b3-b1c9-4a635ff6b526 | -14.46044 | -48.47617 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c407d67e-9468-33cd-b923-9a1d5f0a5e04 | -15.15284 | -47.95254 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1688be60-e0e9-30e2-befa-b20bbe0aef23 | -14.88714 | -47.95219 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d686082e-454d-3955-bbf3-52a4a122a30e | -14.65016 | -48.11322 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb9e28a6-caf7-3c26-8d2c-ce9ba81687d6 | -14.76441 | -45.3906 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7b465a4-3ef7-3347-8e22-816a66c34b3b | -14.89418 | -47.97239 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19bed973-d615-310b-854d-c8618bafa905 | -13.13694 | -46.90128 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1a69351-d015-3a96-bc9c-e47dd3b63061 | -14.73939 | -56.0458 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c23b1b2d-a431-3ab4-8417-5a30fe99d8c3 | -13.03744 | -45.17157 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d23f390-995e-30ca-bbd1-fa26efd4f822 | -13.0207 | -45.16891 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f712c6c3-2d04-352a-a9d5-646758f71bb4 | -15.56327 | -50.3116 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2b74321-3d93-3563-932a-fd613035a0c9 | -13.37523 | -46.2766 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b982d7e2-31f7-3153-8648-7e5099defe5f | -18.74034 | -48.31481 | 2025-08-22 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edb035c6-76f9-3cc5-b31b-74f019b3a6e0 | -14.97424 | -47.13801 | 2025-08-22 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f17b1967-35fb-3af4-ad92-3023287d7c54 | -14.88774 | -47.94853 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README40.md)
