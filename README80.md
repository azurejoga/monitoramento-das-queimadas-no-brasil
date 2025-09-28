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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 872ff8d4-5eba-3bb1-99c7-a2f74550e7da | -19.49966 | -41.10701 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 68847f29-af31-380d-ae4d-36bec23f02ff | -16.26691 | -50.21744 | 2025-09-28 04:27:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46a13d28-53af-38bf-b269-981672bbb808 | -14.77331 | -45.64849 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afcac186-d386-33a1-b0d0-1fe9217b8364 | -15.03316 | -46.97269 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a301785-38a2-3d4e-bbc4-fdba217dd3e3 | -12.97828 | -49.43229 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba7a9f1a-671e-3fa0-a2f9-8a31e5c30c0c | -14.59504 | -48.26146 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df690acb-8e97-3dea-a8a1-1d9f74836f98 | -12.65059 | -51.66459 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81df17ef-cffe-3ba7-a125-0035db99e622 | -13.77706 | -47.89323 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ce08697-3aaa-3020-9a10-abae4ab11885 | -14.70858 | -46.83176 | 2025-09-28 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63c292a1-f819-3cec-8100-d50be3cfa8fc | -12.64123 | -51.69658 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 894771ca-f1e3-3dd7-b34b-60612d5f785f | -15.60734 | -53.17041 | 2025-09-28 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b63e74cb-2077-3fa0-99c2-beb52c7eba68 | -13.97644 | -49.67719 | 2025-09-28 04:27:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c1ad43e-7201-39de-bda4-ceb8488dc490 | -13.34558 | -47.2893 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 963cede2-55f5-3050-99c8-23f190fa7d9b | -17.75902 | -48.76175 | 2025-09-28 04:27:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ccb6b4f-4ffc-3e67-aa9a-c2a7c7fc5dd0 | -18.18647 | -53.32607 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e22d782-9b92-3003-a0a2-507c4a2104e0 | -15.62273 | -48.3555 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f55ea1db-b19c-3e0c-8ab5-a7eea79f4d40 | -13.61549 | -48.07773 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 473e6546-9084-309b-954e-1b446cbab5cc | -17.7324 | -46.69847 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6235eabb-e5d9-35bc-af26-436181d53670 | -14.76926 | -45.6761 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8863a63-c3a3-3ad5-b1b7-76f430af380b | -13.77981 | -47.89732 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6095a19-f3cd-3a5e-b36d-67c09e11a7ab | -19.31373 | -43.81554 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6282b47c-4598-385f-9fb3-4a240ddeceef | -13.56348 | -44.10097 | 2025-09-28 04:27:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a02f4f35-eed8-3e74-957a-a32b006e653b | -19.32507 | -43.82413 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04b35a97-e2c9-323f-8764-d46ee1f2df53 | -15.32861 | -47.89343 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fa7a5e4-384a-3e28-aa12-d891731f339c | -19.20551 | -46.1112 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7eaaf7c-eadb-3eb6-8111-c781a35068a3 | -15.3336 | -47.88324 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78e4de78-456c-3346-add5-e6c2799bc880 | -15.96447 | -50.8777 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 799efe7f-fa69-375d-9031-eec6d680a9e3 | -15.793 | -45.38585 | 2025-09-28 04:27:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d3865c-c362-3e92-b183-f092dfb18170 | -13.19419 | -47.43211 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0399b426-6d90-3a74-8c81-4383d2c832ab | -15.88363 | -46.20185 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c283ec3b-b239-3086-9f2f-a2aaf751c932 | -19.32725 | -44.39948 | 2025-09-28 04:27:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0959e3ef-0b5b-3880-a481-d0d5b27baade | -15.19466 | -48.46358 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1a512d5-2bf4-38e3-bbfb-d670849c59b4 | -13.40111 | -48.16569 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07d9c48c-6cef-33a0-b0a2-2746d216ffe8 | -15.5521 | -55.99888 | 2025-09-28 04:27:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ee7732a-dbdd-33c4-a812-2d142dbebce4 | -13.58843 | -47.32142 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fbaa015-a7ad-33f8-8562-9b33908c10d3 | -15.62009 | -46.25702 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c755b20-8ab1-37f2-ad45-7ce6f8c6e0f2 | -15.33248 | -47.8904 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2537068d-6f03-3c92-bed2-a4af73fe57a6 | -15.21197 | -48.05354 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d01e8cb2-2d69-342f-aed1-d42ca828b9cc | -15.15543 | -46.42179 | 2025-09-28 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79519df6-7bdf-30c8-9649-cbb36b9fa9d2 | -13.7765 | -47.89677 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7355bd4d-6358-3dd1-ae19-fe966073f136 | -12.98601 | -49.449 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 15e4c6b6-3110-3ce5-b73c-b3a1efcb54ea | -12.99623 | -49.45061 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f4cb2728-66f7-3e2a-8623-9cc2d412c618 | -18.03967 | -51.1642 | 2025-09-28 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5fffb83-dc22-31b9-b2d9-b203bc5955a1 | -15.62353 | -46.25755 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc470c0d-8dbc-3c4c-882b-7163243c8a4f | -19.50087 | -41.09585 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| 94da9a9d-54e6-3da3-ab78-618cf1641a75 | -13.70955 | -48.34001 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44fc1161-0441-3e1d-a874-904cad755b5d | -13.60549 | -48.0979 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ded95f2-264b-3582-b645-79f4331a5e4a | -13.62514 | -47.32384 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 554df023-a0a1-39e4-ab70-65d76e8608e9 | -15.2081 | -48.05655 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b1e82da-b9e5-3a9e-8680-02f305894ef9 | -18.18077 | -53.31399 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbe70260-c479-37b3-a40a-305fd7aceba3 | -18.19079 | -48.4329 | 2025-09-28 04:27:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2553fd52-e3a4-30c5-a799-05c5bc922c34 | -15.9525 | -50.41872 | 2025-09-28 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68003dc9-320c-3177-99c8-88ce75323b4d | -13.40499 | -48.16269 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5ad7a7d1-c005-302c-98f6-35173f6caf05 | -19.92812 | -46.9536 | 2025-09-28 04:27:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 312b5395-c8ca-3139-9e39-987b71f7f2a6 | -12.64283 | -51.68726 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb2f984-487a-36f7-bb5a-dfd1f7176fc3 | -13.83605 | -47.95036 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4024788-cb0f-31b5-858a-34706c03ff89 | -13.00241 | -49.45555 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaf24e98-4128-3b0d-928e-220fcb8fafd7 | -15.52672 | -47.90723 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ec9c979-f493-36a6-b134-a6a262d0a3bd | -16.96433 | -53.6991 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1943b7a6-168e-3d72-bd2e-c8470f08213f | -13.29009 | -46.44218 | 2025-09-28 04:27:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8915f9e-0927-3345-b8a7-560a1f6379c5 | -15.89448 | -46.22398 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d93fa9ee-d47a-3bb3-94d4-54b235568f55 | -13.77099 | -47.8886 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02ba3271-1066-3aee-99c7-f4fe57deeeda | -18.18366 | -53.31982 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94d8f5c1-9587-3029-bfb4-1a266cfc3109 | -14.58236 | -48.25568 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4e793ae-dfdd-3320-acdb-2866c1631df4 | -15.43497 | -48.23252 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81a85f3e-3dbd-34e8-8f06-86f16682c04f | -13.38185 | -47.92257 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 926b75f4-5f0d-3ce1-b8a9-2c0cb7511ef9 | -14.72874 | -46.835 | 2025-09-28 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 075ffb11-bbf0-3410-8af1-763d76907fc5 | -12.64043 | -51.70123 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a88ad64-83b9-3786-bbe1-d34afccdd327 | -13.71286 | -48.34058 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 077cc48e-cbd3-304e-bdd8-305659b4faac | -13.01879 | -49.46227 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c8a76ad-e328-32a4-8603-b4d946217740 | -12.98168 | -49.43284 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48cbd9e6-8a62-34fd-9aa4-fbec11954e62 | -15.53446 | -47.90119 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98014908-5bd9-3f5e-84d5-6d8f24acccb0 | -11.86429 | -56.87456 | 2025-09-28 04:27:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6243798f-6550-3a7a-8ca6-7bd9cd209b9f | -15.61585 | -43.87933 | 2025-09-28 04:27:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04a0c13f-aaa6-3641-8280-a7898455a76e | -15.27612 | -46.45557 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d8238a2-7ed0-3484-836e-10c4e24da344 | -13.34779 | -47.29694 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb38239-fca6-3957-9bbc-573d742c341f | -19.50024 | -41.10169 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| a3116ebb-cc95-355f-b150-9d73523f376e | -12.64683 | -51.66388 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7019625e-c800-3959-a0d1-00c3a980869b | -15.90367 | -46.20956 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06d8627c-a9af-3457-a15d-5971be65f9b2 | -12.99901 | -49.45501 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52e4d0f8-c5b7-3f21-9f2a-aeca34455a8a | -13.80239 | -47.92648 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06db6f5e-0972-3c62-99eb-987c1fcafc3e | -15.32419 | -47.90001 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0336e49-4679-3dce-8f4d-3bb30691f4c2 | -15.28792 | -49.48997 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abab41b1-9a9e-3708-8e26-b6c7bc9e1018 | -15.21472 | -48.05766 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1f8dc97-6322-3df1-9775-1260cb145726 | -14.59511 | -48.23959 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5a432e0-7316-339c-9921-6d41171bdbec | -15.02756 | -46.96436 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d587d968-75df-3271-accc-c143ce2a747b | -15.19958 | -48.4754 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce1f0cff-5a25-3572-a762-2dc4381a355e | -17.50231 | -43.48801 | 2025-09-28 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20cd4739-4519-3a1e-8208-f61a88f4d3ce | -15.63247 | -43.0074 | 2025-09-28 04:27:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d5d5fa2-6230-3274-aac1-6c65107f080c | -13.78037 | -47.89378 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cdb1615e-c818-3c80-8b53-5241029f52da | -13.43389 | -46.51596 | 2025-09-28 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3fb48ef-2181-3c43-9441-67e53ab01a90 | -13.00922 | -49.45665 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bed0fbdc-51e9-35c8-8882-86c1c9e10d7d | -15.23977 | -42.71561 | 2025-09-28 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 763c7f3b-5dcf-3397-a09c-977e7ce2e676 | -17.71749 | -46.70415 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1cf4654e-537c-39c6-89e9-b0bcdcc38091 | -13.78316 | -47.87607 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f014712-3661-3a61-99f9-2755d40238cc | -20.163 | -41.72878 | 2025-09-28 04:27:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 40afd1cc-0075-30aa-ae0c-6f520d533ea4 | -15.03372 | -46.96907 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1f51d61-b59d-38d5-8a26-824f72602dba | -15.18517 | -50.0946 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4728ded-120c-33b0-bdcd-171d1687ef43 | -14.33895 | -44.49736 | 2025-09-28 04:27:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de8c8ab3-8e15-3249-b8da-a54e70581859 | -14.89169 | -45.55563 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README81.md)
