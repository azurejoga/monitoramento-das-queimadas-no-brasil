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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 734c1cc6-571b-3065-8b1f-86fbc7f142c4 | -13.33013 | -47.78109 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6902f4d-7343-3a9e-a288-c436ecb87b3f | -13.26185 | -47.84529 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2e7f7b77-0ba1-32b7-8c57-0e467b8559d0 | -9.68016 | -48.40934 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 411b2935-9156-3944-aeca-1f036f1109e2 | -14.70463 | -48.36563 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd641209-2679-3b86-9203-81cfd4f062f1 | -10.14675 | -45.46256 | 2025-10-06 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1f81a29-81ce-3499-b374-22c13400063a | -9.62719 | -48.20954 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c70d0aa3-f418-3c3d-91f7-e01da435e70f | -13.31679 | -48.06036 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec2c1f0c-14ec-3399-bfc0-16198a9de70f | -12.41439 | -51.12143 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e1ee79b-68f2-3c1e-a46f-cab2ace08079 | -11.71028 | -45.41756 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86d13abd-0c72-3f8a-b16d-edf1d9fb684b | -11.09379 | -47.76132 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2224c886-5770-3593-b16a-045a417c2b73 | -13.55572 | -47.24488 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d0ffe8c-afff-33b2-b400-9507ab59d856 | -12.44588 | -45.51546 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7115b1db-02a7-3970-917d-fc5aa6adf5d3 | -13.25598 | -48.46667 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfdd6d9c-02a0-3316-9f27-f407994ec7da | -11.46074 | -51.51796 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c83c74b-52e6-32d4-8520-f43852de8418 | -12.91311 | -54.73984 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a28ca83-aa3b-31b8-9a6e-735d8791e475 | -14.61415 | -52.51144 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0078f7a-ec16-3d31-9455-dabe49a77995 | -15.33646 | -47.31286 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38bcffe8-c27a-3f78-8757-5aac9ed1056d | -11.86226 | -44.93998 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b4a7153-08fc-329e-b34c-ccccb263cbfe | -15.16056 | -45.74267 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22a36e4f-c31d-39f5-9162-802bb5bfaa04 | -17.07735 | -43.38074 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 874f0e75-ca82-3745-9e3c-334c5fe27ef2 | -13.25408 | -47.61307 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96f3bd4a-eeab-3a15-8432-6aa72e7ad427 | -14.85144 | -48.75108 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795cc117-e301-36b8-bc94-36015578a2d4 | -15.19958 | -56.82571 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1503d98e-3baa-3073-9799-f4f02fe27cee | -10.42803 | -50.35022 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddceef70-a9b4-3370-b65b-b6488e066872 | -14.26583 | -45.85473 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1021a025-dc01-3dfc-b8ed-76cd59721c7d | -11.93829 | -46.44061 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af48bd6c-7b16-30e4-a5e0-86ed169b9f28 | -13.34717 | -47.18591 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 798a2566-19d8-3986-a558-91b78f75d900 | -11.48097 | -45.04962 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb8f333-ab78-3517-b5d4-3b828370ae58 | -9.68443 | -48.21141 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6138f378-580c-3e28-a89d-23582ae34e40 | -15.19161 | -56.84028 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7db723e5-8eb8-31b8-a80d-2a854c559f28 | -11.91031 | -46.22573 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e3c7abe-00d8-3573-8eb7-512cd05fb66a | -14.90832 | -46.84069 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b33d868-6901-387e-b757-7883f10a2633 | -13.60754 | -48.69633 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a515f4ce-6929-39a9-802f-d874b80bcca3 | -13.26182 | -46.47625 | 2025-10-06 04:27:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbe56572-e7d4-3787-9559-824023226e33 | -13.27605 | -47.58054 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a482ab53-c9d9-3b7e-928e-c7e95539c371 | -15.60433 | -52.55541 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3f213017-bd9f-30dd-b755-f5b94b3b626a | -14.67379 | -48.38961 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab0e36db-ed9a-3fea-a805-abce488cd7ee | -13.3652 | -48.03214 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 826d9323-e546-3fd8-a875-d851119ff503 | -11.71708 | -45.39517 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2648c13a-0104-3c18-984f-be142d0f4e51 | -10.81552 | -48.82463 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4fd7a2b-c703-3499-a3d5-856726c0708b | -15.33701 | -47.30915 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4da55c0d-16a9-3472-bc14-83c83d86c67a | -8.06638 | -54.92396 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 688b863a-5154-31c4-8f94-afa9a4ed1fac | -13.36435 | -47.25069 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90da4872-808d-3fc6-958c-1e42656a8d39 | -13.0898 | -47.81738 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c76894b-eaa4-390b-b6a4-8cec010e0e1e | -15.36441 | -47.99788 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f584cd5-f61d-3871-9634-89d5750b684d | -13.68802 | -47.35717 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af752853-fe14-32de-a657-4dc2416af6cd | -15.35945 | -47.98608 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b9c2ece-8afe-3c52-9116-1a939c56ac3d | -11.64869 | -47.01917 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7198c0f0-d0d7-3eb3-9698-2fe74611bf8b | -14.55619 | -46.63494 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| add7bd60-b3f0-3c9b-bb02-0f0492e24572 | -14.16693 | -53.02281 | 2025-10-06 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1f3cbf0-f7ca-38db-afdb-0829e9a49773 | -14.51648 | -42.63158 | 2025-10-06 04:27:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 448e6fe5-587e-3f88-b290-b1cf0599be9f | -13.60812 | -48.69275 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15e45347-a14b-3903-b5b8-c7741d0408c7 | -9.25729 | -51.80695 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b147c4bf-59e2-33c3-8492-1451963be4d6 | -10.36073 | -51.237 | 2025-10-06 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b356a856-e5e9-3bb5-ab15-be881130b137 | -10.72976 | -46.62809 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64aab2ca-3d93-34d4-ad32-630bd779e3a8 | -13.05275 | -47.91951 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d88c70c-a28b-3abc-8bfd-b045417b47c3 | -13.63292 | -48.7078 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ddfd99f-cf07-359a-8427-6eef9a1e7b32 | -13.36268 | -47.23954 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2db7609b-91c5-3738-96ac-b20dec5312be | -14.48831 | -47.54858 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ff5ef5b-cd6d-37eb-9054-273275ddf5be | -14.91332 | -46.83029 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a3ea75cb-3a50-37ab-8986-085013f6d08f | -15.3545 | -47.99623 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3df2ca2a-2898-3af2-b67c-e7e2e470176b | -15.23596 | -49.28626 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a23f5891-1588-3cb8-8285-e861601aabb2 | -11.48619 | -45.03831 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b68bba1-8041-3eed-bb70-0f52cd811360 | -15.32967 | -47.3153 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40ce7133-90ff-381a-8611-fffbc84b784b | -14.87107 | -50.23977 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c32f9e49-95ef-3fe0-bf41-0c3e4a5ddb0f | -16.33334 | -48.06525 | 2025-10-06 04:27:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d6ea25d-5bb5-3d54-9fd2-7f97227d69a5 | -11.94049 | -46.42609 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1db77003-a1bb-3689-bf7b-9447c7e9562d | -13.04401 | -49.15222 | 2025-10-06 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfaa90e9-79f2-31c4-a21d-bfc357b7b198 | -13.05 | -47.91545 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 318b54ec-8434-388e-817d-436fefbadcab | -9.27398 | -51.80457 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f753603d-0361-341b-88b1-4eb650906e6e | -14.60235 | -52.48955 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 586b94d9-b60d-30e8-9156-133aa02f4408 | -14.84757 | -48.75409 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04eacbc8-22c5-3f0c-8d17-1fa251f251f2 | -13.13699 | -47.99091 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2b6ec27-6814-31be-97ca-9259a766f60f | -14.61289 | -52.49643 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6117cb82-7fc5-30c9-bc61-b25c282fcd09 | -15.91449 | -48.83058 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 919305eb-9a64-3adf-9f01-50bde9d0911e | -9.90763 | -50.22536 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9940c02-d71c-3a39-9b02-cf4ff2a9308e | -13.08482 | -47.87064 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6aee3124-b528-3133-ae9d-82d3d6a31380 | -13.08211 | -47.82333 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c775785-e43b-35c6-bf92-46c6d608570e | -13.25499 | -50.37425 | 2025-10-06 04:27:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8530a29-a9c4-3b34-8a2b-351b9d803004 | -10.40145 | -51.58732 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c954d87b-5ea8-3055-9399-9bad708e233e | -14.65683 | -48.34685 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e0c51c-235f-3bde-bcd5-ab187a1698fe | -13.63062 | -48.72215 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb9127a-a4bd-3a59-a662-162768e6ab1e | -9.96625 | -48.74994 | 2025-10-06 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa924827-d9f4-395a-bd48-dcd92e6315c8 | -12.99407 | -51.05645 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65c4f851-0d18-3c4f-b77f-65e1c8a21d5e | -10.2073 | -48.93665 | 2025-10-06 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb5bba85-52b9-3350-af30-4b3469ce6fce | -15.58038 | -47.27314 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b780b7f7-3d07-31ce-ae15-c6f210700fbe | -14.54279 | -46.96675 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 020fc560-2cbc-3870-8fc7-e604236ab9a8 | -9.67345 | -48.40829 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f2ae2ef-556e-3448-82f3-01b9df2f6bce | -13.26625 | -47.83879 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24d3ba05-bfb8-3505-bbbc-c3101df501b2 | -11.11048 | -47.20215 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a375d97-d369-3507-af0b-d739cbfbcb9e | -16.05209 | -50.94487 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fe7648-f793-316a-9b7c-f1f2d4bd6c15 | -9.38339 | -45.8741 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f448b8d2-4100-3068-8c6f-2fcf97892d27 | -8.62286 | -54.98853 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17a358fe-f31e-31df-b8e6-467a89eb325b | -9.68167 | -48.20728 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73efde1c-fa7c-3a2b-b734-00d200fc5dc9 | -16.05589 | -50.99825 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 527a0828-bf13-3166-acf0-ee2df55797ab | -16.05277 | -50.94078 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d188979e-7c5c-3b37-9964-a2dcf9b5948e | -15.9933 | -50.93406 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5c6dcda2-2a25-30c1-a467-ac13d997626d | -9.02593 | -50.6871 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48278ee0-0d6e-39ff-909c-dcfc3ec2237c | -15.24471 | -53.78533 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ff4ea8-2dd5-3ddf-a761-0359ea4ebaaf | -13.07001 | -47.92224 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README37.md)
