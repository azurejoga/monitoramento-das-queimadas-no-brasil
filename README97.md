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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 852102f0-f072-32ac-854a-387dd241f524 | -10.30186 | -48.7907 | 2025-10-01 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d60d97f-730a-3f05-a2d7-880241e04b40 | -13.15415 | -47.40783 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6979b62-3af7-35bc-8897-5f78c42e237e | -10.19635 | -52.56053 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a9542f8-72ef-3f3a-8c54-d95335895e1e | -13.93605 | -48.11783 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c30dec3-5663-3f54-986f-a81a94b12b4a | -12.01742 | -46.63025 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7ab4612-cbbb-3690-a2d3-6ecd26ce9545 | -13.2264 | -47.32841 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a351b39-c417-325b-ad5a-6c5cc2323de7 | -9.92764 | -43.68642 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5451532b-9c95-38c2-912e-9f428f2763d4 | -15.16132 | -49.09315 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 59561394-41df-37b7-b5ee-6ab9313b7d44 | -14.03545 | -47.98383 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec3266fe-f178-3e84-8428-de8e2f6254bf | -11.44155 | -43.50401 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2927883e-f933-3c42-8c90-d44d426e3d02 | -9.92263 | -43.68567 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e705c4ae-e64e-39db-808f-a7c2477e2b53 | -14.72271 | -48.16047 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45e58622-1fff-3605-8255-5097bc6e4103 | -16.40825 | -47.06471 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5e292bd1-5796-30dd-8a19-4793cdde45ce | -13.58979 | -48.03936 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df1469b6-8b2d-3562-a2a9-a9b3bd1dff61 | -12.84188 | -47.03357 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0083d46d-edc9-360d-b467-b560206898ec | -14.90464 | -48.13308 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e1875b6-2481-305f-8437-e99a7c389138 | -14.96175 | -46.8781 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4587285-8bf8-3981-ab32-89251782fa0f | -9.85868 | -44.60625 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 671d5068-2cd7-3e4f-a8a5-5fbca78613bd | -13.37161 | -47.29921 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c43acd7c-7aed-310d-8a37-4df51ef96f2d | -10.483 | -55.62472 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1421cab-5b6c-33b8-977c-7bc887bab4c0 | -14.76071 | -45.75783 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 382ddd4b-a14f-33f9-80d1-a9e4cd5818c0 | -14.91297 | -51.67694 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c20a805-a513-36ae-ad97-117d138d0466 | -13.3605 | -48.14043 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98056015-a9ef-31f0-a209-acc3f30965fb | -16.57358 | -45.10837 | 2025-10-01 04:51:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10c0925f-36cf-3471-a118-2abfb1510b9b | -11.10281 | -40.9581 | 2025-10-01 04:51:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0e9ae22-99c9-32c1-aaf3-4c3ed6294c3a | -14.19165 | -46.10126 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 199de0b4-0dc3-3f1a-9fb2-8fe9b0d8d3d0 | -11.9212 | -47.89939 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1143ad39-e321-34f5-af2a-4c98031e1df2 | -10.93139 | -54.33293 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3826ac7f-23a4-3f36-86e2-85bb4672b6d5 | -11.47021 | -44.98481 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c95af6c-0eaf-34d7-8b64-4a76d518f76b | -11.05493 | -47.8315 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a04145e4-8335-33b5-be7a-02b5b6c964d3 | -14.54534 | -48.22783 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64ea6dab-9291-3573-b630-9b3f67f348d4 | -13.77636 | -47.98164 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 824153ca-5291-3505-9bfe-32e4b1c05626 | -10.90803 | -46.55496 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04aa4b7b-e027-3214-8048-f7e0e026e382 | -12.69622 | -48.56401 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c5b85fd8-7711-3699-873d-f98e46cd62cd | -14.97686 | -50.78382 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61296a1a-c76d-38e6-9bda-3e0c725123b4 | -11.39335 | -44.89946 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0f6e270-f5a3-3f59-b3dd-f448f2f2bbac | -11.57065 | -50.18945 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6d8ee7a-bbce-3535-a85a-1a79029be6d1 | -13.76619 | -48.40271 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 190639de-143b-3588-a6f0-7d838375d985 | -15.33448 | -47.94086 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c954f453-2698-3f1c-97b8-576c221ca3af | -12.78535 | -46.85343 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05a8a09d-648a-342f-a0df-9d129049ccf3 | -13.22919 | -48.44546 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a173a006-1e17-347f-9823-26fd8119257f | -11.58097 | -47.65897 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7da11c19-ba6a-30ab-bd2e-75d2500ae389 | -13.38802 | -48.08494 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aee3777-3b69-3bbb-9142-987af974c846 | -11.74474 | -46.86971 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 643e71e0-c76a-308a-8308-20bc3843991d | -13.41265 | -48.1959 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a9c203-910e-30a6-ab5f-08459edbd8da | -11.84743 | -44.98667 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ca690608-d67d-337c-b0ba-4f1009a9f9fa | -14.74879 | -45.77669 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96e2a3be-b34a-3f4b-a7cb-4eceb1dc5e09 | -13.73412 | -48.69336 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff82fe31-38fc-3a20-8c60-1b5d9772987d | -14.96554 | -46.88293 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdf6f3f4-e31c-33b3-a592-cb8ab542d163 | -12.45401 | -50.21262 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe224fe1-55dd-3d8c-8428-a8c7d34731db | -12.45459 | -50.20872 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85b6d53b-8cc8-387a-8bcf-557380d684f2 | -10.66276 | -48.53182 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2285b52-a31d-3ff0-86d5-82cf859e6d43 | -13.09361 | -47.04077 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e22562f-421f-3f4a-abe0-186420433032 | -16.1943 | -49.99609 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1db8a9f3-86e4-39b5-b892-3b5ff6a6f224 | -13.9445 | -48.11495 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a947c010-6d3f-30d1-bea9-2627993d5836 | -15.52992 | -44.3482 | 2025-10-01 04:51:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e93862a-2f17-3ff9-acdc-16fa70b3b410 | -16.02905 | -50.88985 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2707b8e9-bc16-340c-a1ac-b6900cb3c433 | -14.19556 | -46.09987 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cded4cff-51eb-37a5-b43b-edff4cb6302a | -14.78602 | -45.7678 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55cf92cc-5139-37ad-b178-3cc1face8feb | -15.33944 | -47.93356 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0c63dc0-50dc-3b95-8a42-e36b82fb8ffd | -14.55119 | -48.24418 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e84f5bc-0baf-35a2-af29-57b9cd0c4b0f | -15.27148 | -51.47245 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 923f5af9-c4c0-3205-b074-9ceaf4fb6684 | -15.41545 | -47.05333 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd911659-b71e-3fdd-acab-3750672e21f4 | -10.44689 | -51.2659 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfceae26-b3d4-3aea-bc59-d74c56adee6e | -14.59296 | -48.29174 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 995420c3-485b-3d18-a786-550058bbbf15 | -10.79341 | -45.35824 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72673670-1637-392b-80f0-f9ba15675360 | -6.94965 | -63.1053 | 2025-10-01 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4ab0ae5-4421-36f1-9ae3-98bf7a93851f | -10.91428 | -44.33749 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dae5f27-62ad-3beb-8034-93259efcaab0 | -14.35808 | -45.92482 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d95e460b-27a7-3795-b73c-9c52cc93b30a | -9.69076 | -49.94483 | 2025-10-01 04:51:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 975a2bd1-c2db-3925-a73c-a2fafdbc18ef | -12.82777 | -47.01251 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87ee8205-eefc-3a8e-a389-1c01f32a034d | -13.29009 | -47.23259 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e34b4d2-0a26-3b64-89a9-104a85863889 | -9.58508 | -54.58673 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfefcbe0-6486-3c2a-b72b-fa29be0a1f35 | -11.81034 | -44.97687 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c338706-21c1-3cef-9870-bc9758fac2e4 | -14.02133 | -44.97536 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6157fb60-3eac-3de5-944b-906cb45a5ad2 | -14.70048 | -48.26365 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4518006-4bb3-3774-82ae-b1bf23194c72 | -12.69313 | -48.55857 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70eb99eb-b4a2-3239-a0df-0038ce1d4d8d | -15.77562 | -43.67997 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee34784f-70cd-376e-a783-3cd74f4240c4 | -10.8323 | -45.37727 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 347860e4-88aa-3e13-bd92-2e4308ef0f99 | -13.8452 | -47.93835 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4aaac4c-e756-3f3d-ba47-7399bb13f25f | -12.78188 | -46.90927 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4488799-de3a-3063-8cc3-1606ef46b0a4 | -10.9604 | -46.54966 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc765181-4cb8-3f92-908a-7039a2f1a0d7 | -14.35792 | -47.14398 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef4647a4-a2c6-3cd3-abfc-f47dc5fbda1f | -12.8795 | -46.94605 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e6aa4b0-f447-3f1e-9ac4-b31b3012c843 | -15.32995 | -46.2765 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f1283d3-c01d-3d00-8148-8a1c57451a9d | -14.35409 | -45.91951 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5e4adb7b-efc3-317d-8cc5-f43f47a00ce7 | -9.2377 | -50.62798 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 801894f2-08d4-359e-8a1f-55a7e3b13d9a | -12.68935 | -48.55795 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5276c97d-73b8-3fa9-bf71-4e65b751018d | -15.17865 | -46.40964 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b584807-98d6-3451-b773-c57bbf0d391f | -14.89839 | -47.21 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb9bc18c-26a0-3650-afc4-080361362b69 | -12.85699 | -47.01639 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c919a8c7-fa1e-3280-b8c8-c25a9ce928fa | -14.49963 | -48.42135 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b58f95ef-4d96-34cc-b5e5-7721865fc32b | -15.61303 | -46.9073 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce220c0e-93cd-30a2-a0f0-419b96985fc8 | -10.02246 | -50.26104 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 546b0e09-8575-3027-9a66-2952acc174c9 | -10.03963 | -52.09879 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a76f602b-a5b2-3cfa-bb5e-28752eecdc0b | -11.18797 | -47.19806 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc3d2a61-27a4-3e82-a5e4-c6df2966a029 | -15.29962 | -47.8614 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e063f29-ff7e-3f8b-8075-a0895c9bc14e | -12.16216 | -47.7706 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 51971786-f84e-3c4d-b542-79c699c33126 | -10.64427 | -48.52923 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73315d30-c1ae-3a1c-a3fb-f51ea9a95238 | -15.94532 | -48.12302 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README98.md)
