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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05f041bd-c309-32ca-8cb0-c46774ff924c | -11.85855 | -50.85821 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0627528-b737-3e54-a83e-3266ac40979e | -15.23949 | -43.27437 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ecd5831-5078-3f32-95ab-87db16ba400a | -15.89654 | -43.47966 | 2026-09-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e6c97764-9b9c-3d6e-8667-259d5d977cf9 | -12.26462 | -50.72819 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abe7fa4b-1438-3987-94c0-16c257615c0c | -12.12362 | -50.29564 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9bae9cc-0e9a-378c-9ac9-1f809d0a28fb | -12.16572 | -50.32261 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a8d2a133-66a1-3d79-b9de-aa51b7663de3 | -12.26655 | -50.32423 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f202c621-2fdf-3660-a13e-45a431f06356 | -10.76576 | -50.84119 | 2026-09-26 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98fc056b-1675-3d91-9550-009de33aa717 | -12.1695 | -50.32329 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b02bee43-68e1-36d9-a9bd-1c87dc162793 | -12.25521 | -50.32217 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e326c85-d02d-3590-8469-dcfdcde66336 | -12.17032 | -50.31859 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 89ec21c9-b520-3159-8169-37d19281ffc4 | -9.46323 | -40.32862 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c23d16b4-74c0-36d8-9b23-9e9fedf38ec9 | -12.59932 | -51.9488 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410c3527-4fce-33d9-830a-5bff15ce083d | -12.34771 | -48.19748 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 148a974f-6ce0-3398-88ba-c51a5456ffec | -14.87109 | -47.1393 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e2201b86-fd66-31e3-b4af-ccbe292b034c | -11.78986 | -51.00322 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbbf9f04-0b21-3604-a5f6-b60fb2166773 | -15.56294 | -44.11437 | 2026-09-26 04:27:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c5803da-5745-3ee5-b198-30eb5e38c8ec | -15.16146 | -48.81952 | 2026-09-26 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cb58444-cbe2-32ac-b08b-18c2fdf9bf0b | -14.86721 | -47.14231 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fafbb72-b3fb-3932-b199-73dfe62e60b7 | -12.25241 | -50.36047 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14bc821e-920f-336c-91a6-99119f19956b | -12.95084 | -51.06308 | 2026-09-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0c2e28f0-b1a9-3783-a600-11defad74726 | -12.67132 | -54.64541 | 2026-09-26 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d330cc9-af13-36b7-905f-f37f955c0e3d | -11.99923 | -50.29808 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b66e0775-9c93-3723-b697-719f4645005e | -14.47588 | -53.63539 | 2026-09-26 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a83b5ff2-b723-3151-813b-4417a1e4d465 | -12.26285 | -50.73807 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5a19e39-09ce-3d55-a71a-6eaf6514e602 | -12.16653 | -50.3179 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 69210dc7-93c4-3254-b827-634a89d6e89f | -12.66636 | -54.64446 | 2026-09-26 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a108174c-dd47-3a02-bd92-df594d5b3ca2 | -12.20952 | -50.34024 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 30b884c3-0a7a-3b04-9fee-8a495364a856 | -11.00032 | -58.66381 | 2026-09-26 04:27:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a78b23b-42fc-3f29-a17f-74b93830f179 | -12.00955 | -50.64037 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 816e0662-3e16-342e-870c-03332466a6f9 | -15.19119 | -49.29113 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48c61a8-065e-3a0d-9055-a6a638941d11 | -11.78807 | -51.01363 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 955a279b-9017-3545-9dbf-84a14635034b | -12.21628 | -50.34633 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ab3df43-5c4d-3116-99fd-6ee1b9a5dc62 | -11.93261 | -38.29687 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7b442ab4-a4de-33a2-bedc-57112bbe3480 | -11.94864 | -38.28774 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 977011e6-b7fb-34f5-97f1-0a5f0a4ba191 | -11.39987 | -47.42601 | 2026-09-26 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5e5b456-6ff0-325c-b622-2fe1d1615bbe | -14.86115 | -47.13763 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01a09a11-b2df-3e5c-88a1-e52ead39c53e | -12.03489 | -50.65514 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f035ef7c-f1b9-3c2d-bd92-bb0d68aa294d | -13.08135 | -47.4273 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddc9dd7e-7f8c-3721-a929-565c1ee5c0e0 | -12.59034 | -51.95108 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3eac57f-e6d0-3f32-af9b-10812c932a9a | -11.27113 | -54.43333 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7a484cf-590d-336e-8487-6d4697c91cb6 | -12.27323 | -50.72466 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e5d0631e-f09f-30bc-8587-978544a230ec | -15.2358 | -43.27382 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c91bde4-dbb1-3cfd-92ad-633b4654cbb0 | -12.2125 | -50.34564 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 60258e10-2a4c-32f7-89da-5d6a9b8131eb | -15.19815 | -49.29221 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67114f70-196c-367f-9dea-ee89be3f81a7 | -15.89286 | -43.4791 | 2026-09-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03bb9ae0-efb0-3385-b8fd-6a894a1bed00 | -15.89222 | -43.48355 | 2026-09-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 996592df-af02-3047-950e-c7f8f2e7e042 | -14.87052 | -47.14286 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e0e43b0a-28d6-366e-8366-521546e2eb1e | -15.8959 | -43.4841 | 2026-09-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4448edfb-6dcf-3e42-bf51-475c44d649d2 | -14.96108 | -47.53276 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11cab7a1-2c3e-3b9d-8c48-6c3e307795d9 | -11.99439 | -50.75018 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86c90092-f14d-3eaa-b3a5-1a6a4ec32ea1 | -13.20346 | -48.32832 | 2026-09-26 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a77e0e89-5092-3ef2-80c3-1b35b50d54f6 | -12.18004 | -50.33005 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 33c0a69f-31c6-3938-9ea7-95d0317f1c36 | -11.93332 | -38.29142 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d76513e6-02e6-3826-af3d-826c4197d03e | -12.77899 | -53.24927 | 2026-09-26 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06bab457-bf30-320c-8485-f8bbbefb731c | -8.19224 | -54.8308 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0b58da7-0359-3bae-b8c9-fd722c5b73c4 | -11.74173 | -50.62538 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d7a2de2-8dbb-3174-a0c5-ea2d56939bf3 | -11.78608 | -50.65128 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d5005de-a26d-30a5-8498-0521e15fa1a8 | -16.67405 | -41.85172 | 2026-09-26 04:27:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 42e8dea8-0fad-3bd8-a8a9-d03928c88912 | -12.04385 | -50.62632 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df673e2a-2281-3b17-8032-f8b55fafc77d | -15.42427 | -47.90369 | 2026-09-26 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9cd93bcf-6b98-3dc0-8b06-890e1feecf2d | -10.4118 | -53.81326 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf2c9677-3611-32da-bee1-d454f215bfa3 | -15.24446 | -43.2659 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 336ffd06-713d-3e9b-bec3-c67a8bee28f5 | -11.95055 | -50.6806 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48e3a996-84fd-36c3-9ea8-69a6c63a3722 | -12.25899 | -50.32286 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31ac2aff-b4da-3059-b36a-c97a48934376 | -12.23809 | -50.35302 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 973f195d-48d1-3e61-9df8-226d89f83011 | -13.21507 | -42.36205 | 2026-09-26 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3c61158-1560-32e2-b951-fb9474ea3f13 | -12.18085 | -50.32534 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 242ba794-59e9-3f64-ac98-29bf9401e345 | -13.7125 | -48.8107 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b77d11ea-28e4-3967-8d31-19e4bc0c0605 | -11.93359 | -50.5885 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae5de68a-f3f0-30aa-b895-e14a27464a75 | -12.26251 | -50.71761 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ada4ee42-f0f8-338a-8a2f-2877158dc721 | -9.46272 | -40.33228 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9a22422e-fb7e-319b-a7cc-07d1cd82cb65 | -8.49829 | -54.7769 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e6f83a7-045e-3e0c-bccb-6d73e023e71e | -13.20471 | -48.32074 | 2026-09-26 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1ebfaca-2b65-3568-8478-4283de69492e | -11.8933 | -50.59131 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55c02ccd-1ae3-3bec-9073-f073c6cedaa7 | -14.86835 | -47.13518 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 669c38fe-ee38-31ce-8b9a-81ded5f66edc | -13.20005 | -48.32773 | 2026-09-26 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 568396b7-fb6d-304e-b3ce-0e8e4e50158f | -11.93818 | -38.29205 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2f7c7ed6-796f-3f07-863b-0f7c5166ff57 | -11.89588 | -50.5766 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18b96b01-69bb-3bc5-b1fc-7fc3df10a586 | -9.42723 | -48.84923 | 2026-09-26 04:27:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 820f36b0-884e-304f-abc7-be0a045a2d8f | -12.26459 | -50.35781 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71d4caae-2174-37b5-a00e-77a7bce5bfc4 | -11.9366 | -50.59411 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e9952e4f-b084-3edc-9802-afda3248c067 | -11.95399 | -50.67867 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28f29c63-979e-3ca9-9d66-5ee749dd793b | -15.20163 | -49.29274 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17abed64-5638-3fbb-b92a-94ae90450917 | -12.20573 | -50.33955 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 245b111d-794f-3fac-a9e7-eed413d7d94d | -9.53598 | -56.16123 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 375a8f9a-7ccf-3ffd-a530-46ae59a97ce7 | -15.16956 | -48.81309 | 2026-09-26 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0113ad87-a632-3c3e-9182-d75d0f2f3c54 | -13.6959 | -48.80373 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b839c26a-8561-329a-b7b3-8ec0cf680e77 | -13.91787 | -46.1656 | 2026-09-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 983878b4-4fda-377f-bd16-6fc0e58cd48e | -11.89202 | -50.5759 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bf60d9c-a16e-301f-8dbb-9b8fb4ee184d | -11.94579 | -50.68485 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a129d598-79af-3a22-bce3-5aeb7911b1c7 | -11.94368 | -50.69215 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a42527-9c18-3c90-8f8a-a331e79dbe1c | -11.92803 | -50.59761 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3d99c4d-77cb-324c-8f6b-38d61b2c3374 | -15.24318 | -43.27493 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6b643999-7c0a-3dcb-9fca-78789ea29314 | -7.77015 | -54.68681 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4d53abc-50b2-3f8a-ad57-096ce343b38d | -12.59327 | -51.94346 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1292ac5-7cb2-3e20-9f7a-d5d4c9ddc30b | -12.15519 | -50.31586 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 886646d4-5d32-3686-b3ac-dae66249d167 | -7.77558 | -54.68774 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e0af877-95ed-3379-b21f-d114dafce4d1 | -12.26327 | -50.34301 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c28192a-44e7-3fc1-8055-fcb24bafab79 | -12.03103 | -50.65444 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
