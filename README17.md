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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a65636e-61fa-33c4-84db-2b324fbb6b4e | -3.33729 | -42.79849 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36a7596a-7632-3134-b7b2-8f491856bc86 | -1.09741 | -48.0572 | 2026-09-03 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab98e326-817d-39b1-b790-42be1d92fbb7 | -4.03334 | -38.23348 | 2026-09-03 04:00:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 82e16b73-ae82-3668-a5df-91c604f9e830 | -3.34095 | -42.79906 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f456742d-6fe5-388a-85ce-b6537020fc48 | -1.79905 | -47.95152 | 2026-09-03 04:00:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 66156e2b-f1d5-3a6c-b349-a5e8bc543692 | -2.26549 | -47.012 | 2026-09-03 04:00:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d2635b6-94fd-369a-860f-e9107a0b812d | -3.33595 | -42.80704 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 643458e8-ff35-3431-b999-97e40ea86b07 | -3.33662 | -42.80276 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25639dd8-8366-350f-b4b1-0cb58a29bd03 | -3.33665 | -42.80214 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31d28a19-cd1f-3c4f-b14d-9cabc222c757 | -3.59567 | -43.01214 | 2026-09-03 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f729f14-d38b-395f-9496-bf49e792b6cd | -3.96427 | -40.05241 | 2026-09-03 04:00:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 059e9b34-dbb7-3c17-9171-6b47376ccf33 | -3.33961 | -42.80761 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc377d30-4367-3c00-8891-1faf4ce1a8e3 | -2.89523 | -40.03733 | 2026-09-03 04:00:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc92c4c2-26d5-3a01-a1df-64842e0dc6de | -3.33842 | -39.77018 | 2026-09-03 04:00:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f5dfd182-77c1-3c15-9d5e-f7edb00ba7a8 | -1.09686 | -48.06059 | 2026-09-03 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a4dd716-0d7b-34b8-b458-c4a7b0dce874 | -2.93542 | -41.73185 | 2026-09-03 04:00:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ede8311f-c357-3f6a-9960-ec0e1f608de5 | -1.09364 | -48.05959 | 2026-09-03 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee2bd470-613d-3471-a1f3-70062b5f89e3 | -3.96704 | -40.05638 | 2026-09-03 04:00:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5ad6ee3a-81a7-3d12-bab0-db5deb1bebb6 | -3.33595 | -42.80641 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3491d144-b42c-3c1d-ab07-3449c891004d | -3.33896 | -39.76674 | 2026-09-03 04:00:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97f03c19-7324-3e93-84de-aae647baf4ce | -4.02999 | -38.23297 | 2026-09-03 04:00:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 586860c6-7ba7-3cff-bf01-f26f264aef2c | -4.11074 | -51.02099 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3fc1157e-7264-35e5-959e-07387f89efa5 | -9.41622 | -45.60754 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f90478e2-d984-327b-bd2f-19e3c24d15c6 | -3.22109 | -48.81279 | 2026-09-03 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4bff03d-90ef-3db7-b97d-320eeaa0f96c | -10.87231 | -45.31153 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7e610694-7283-3547-9136-7e4576eaf066 | -3.64598 | -49.96677 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3539ad43-73c6-30de-8407-03fce0cbce4f | -6.43512 | -42.10682 | 2026-09-03 04:02:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a340e407-5100-32f8-82d5-cae55e15520f | -6.15761 | -44.64934 | 2026-09-03 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c243f42b-c569-39e5-b3b5-a1a8405d28e1 | -7.40889 | -49.74488 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49d7db24-2ead-30a6-97de-2b6374a5b967 | -10.87945 | -45.31114 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 204cbb75-7682-3153-b076-cc29cc907ebc | -8.46455 | -44.69631 | 2026-09-03 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ca92b8f-22bd-342e-9c89-5a4965099a80 | -10.56044 | -47.7234 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1183b5cf-7103-37fa-885c-921f3c2fd6aa | -7.85463 | -39.90122 | 2026-09-03 04:02:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1db42795-66c7-39aa-9368-575188909b14 | -7.12529 | -42.22736 | 2026-09-03 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d3824388-4991-3092-a86f-b9a3b1065e05 | -8.07942 | -50.96275 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7accb465-5a61-30bd-99be-4632f3498e7b | -8.46073 | -44.69573 | 2026-09-03 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55b1d05b-c637-385d-888b-5728e8deeaca | -10.99621 | -45.08198 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7dbf52f3-c14c-3fc3-9a94-29336a427b1d | -4.15092 | -51.07644 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58061c7a-bf35-36e1-be2f-d31f500baeba | -10.56652 | -47.71532 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9778475f-09ae-3472-b472-75741fb0d0ea | -3.24929 | -47.24903 | 2026-09-03 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| d6fac93f-009f-35f7-a6e3-55c3bff1a4a1 | -5.9784 | -35.26237 | 2026-09-03 04:02:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2129d466-e16e-3760-bdca-b46652af8365 | -4.10904 | -51.03095 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7955eaec-7743-3eb2-b42d-a6943c182013 | -4.94357 | -47.65758 | 2026-09-03 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cede998b-4389-368a-bc58-743c1569e26b | -3.9288 | -49.05553 | 2026-09-03 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b5cb23-5522-30ce-be9a-ae6445a8aa03 | -4.7378 | -40.43398 | 2026-09-03 04:02:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2ec941b-886c-3459-8f06-df50edaee08b | -10.87373 | -45.32654 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57cfdfbf-c5fd-330d-b31a-511ee804b579 | -8.08224 | -50.97995 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 634ad2ed-4624-3358-8d71-3efcc0988000 | -9.60071 | -40.34756 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.7 |
| f7ecf476-1fe3-3f1a-9f75-a66519b6a449 | -10.87612 | -45.31221 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e4ee759b-1f07-3761-924c-fc1fe6909df7 | -10.93171 | -45.34954 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cd7fe7f-7547-3a2c-993d-23d98e3de051 | -8.60816 | -39.55511 | 2026-09-03 04:02:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee5634b5-f112-3e8b-a1ce-416dd24f9982 | -6.65839 | -46.13901 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 574624be-9fc7-3f44-9740-87e11b4ed521 | -8.46782 | -54.64401 | 2026-09-03 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0de271a9-3877-3e70-9b45-05359b120f79 | -5.41547 | -44.79927 | 2026-09-03 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25950026-973d-32f7-94ee-f1dd1e432014 | -4.11612 | -51.02676 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| deff065d-c04f-3a29-9f1e-9d9422f2db8d | -8.07415 | -50.9914 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9f730da-1c9b-3b11-8053-d513e682cfd6 | -6.15369 | -44.6487 | 2026-09-03 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3808222-ab4a-3971-a8db-6aa8022248bf | -10.87453 | -45.32174 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b43b7bdc-32b2-3cce-8f4c-445c72f1aafe | -8.0865 | -50.98927 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ac572c4-75c4-3815-8b20-1e38605536fa | -8.08596 | -50.95961 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88d824ac-2aa1-3ab4-80cd-ed90d0b1019f | -6.68059 | -43.41877 | 2026-09-03 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 63c89041-6cf7-34ab-a0df-7b0f9f40a615 | -6.09184 | -44.90076 | 2026-09-03 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e4dd78-d0a1-3971-aa58-ade4f09761a6 | -9.15081 | -49.98246 | 2026-09-03 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 310827e9-914f-3b44-bf69-286956611d2c | -6.75835 | -44.56725 | 2026-09-03 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41c0785f-bb82-3b81-97cc-e1c3f21f449e | -8.44083 | -41.45692 | 2026-09-03 04:02:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3f88270-e33e-31d4-891a-9691306ecc55 | -9.60179 | -40.34057 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 44.4 |
| 3acfb1db-a353-3ff0-a3df-b72aec307403 | -10.99092 | -45.09053 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 51c89dfb-aaa5-383e-b297-48daa194a445 | -6.49068 | -45.92254 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e40778e-0839-394b-832e-24a166b6b8b8 | -9.15142 | -49.9791 | 2026-09-03 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95629037-40c5-35ba-a517-bcc1ec155a0d | -7.07869 | -44.35983 | 2026-09-03 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21a51137-2927-32a7-aa36-92e52b7801c7 | -4.10987 | -51.02606 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 06b0a681-51bb-376e-9d89-a74308ed64ad | -10.56282 | -47.72107 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7bce2de6-cd02-3030-b79a-75e3aeac69e4 | -5.72641 | -38.60599 | 2026-09-03 04:02:00 | NOAA-21 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3306088a-dd19-3891-95c8-e41d97167556 | -3.93483 | -49.05308 | 2026-09-03 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7569c345-a462-33e6-8cb0-bc15eb83883d | -5.30782 | -39.66032 | 2026-09-03 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc65cc55-980d-3b42-8d38-92996caffb4a | -7.12187 | -42.2268 | 2026-09-03 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c04e2da6-29aa-3078-bb17-e8f06eb7c1af | -10.56359 | -47.71664 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50c5b578-0762-374d-8e03-de12cedcca69 | -2.83002 | -48.65117 | 2026-09-03 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6fe7b3-cbff-3cd2-ac50-de3e2fd273c0 | -10.874 | -45.31995 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b371302a-2430-3f29-ba8a-c7c8fe111fd8 | -10.87615 | -45.33017 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a86613f4-ae7a-3e96-86a7-6079f8c9f43f | -10.56733 | -47.71086 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a43e6e37-b550-35d3-aa0f-c8b8112f7757 | -6.21161 | -42.52166 | 2026-09-03 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 945fc711-9169-329a-bd6f-7052a3929f0c | -8.07868 | -50.96678 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e5afac78-e5df-3b87-96f9-2b26fe4eba3c | -3.64527 | -49.971 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 345021c7-6c4d-3b75-8738-05c9262bc35c | -10.87768 | -45.30277 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 37285e56-22fe-3705-9350-f94df55a5679 | -5.80813 | -43.64354 | 2026-09-03 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8d47bb5-8543-36b8-a1a1-369a7de18069 | -4.17954 | -42.43891 | 2026-09-03 04:02:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e7cd46e-73f7-3f3d-92d0-01e295d662fa | -5.48309 | -45.24502 | 2026-09-03 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0759d9b-3c11-346c-bd45-2e1a6675e82b | -5.82758 | -47.03869 | 2026-09-03 04:02:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9878553-28d6-32fe-b8d2-1cfb74e666c4 | -6.6548 | -46.13418 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4445994-9996-39c7-a973-0b8fa49ec490 | -10.87646 | -45.30576 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 8143c3d1-7f2d-3b90-af9a-876503cc6c99 | -10.91647 | -45.34683 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2329c80-7a5f-3858-bd01-fea89b7450dd | -4.02539 | -47.7239 | 2026-09-03 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c8f33c2-8480-394f-a164-7483362f0b3b | -4.14485 | -51.07462 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 17a27bc6-ee68-3182-9691-8efe310c57b4 | -4.14569 | -51.07785 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d667972a-e065-3d90-8c63-9023a77927a5 | -6.94383 | -45.20469 | 2026-09-03 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b310f7b-2b07-381f-b818-bbd966cd2105 | -8.07916 | -50.9967 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f27ae765-2512-378d-8e9b-af403e19cff3 | -9.12604 | -40.64704 | 2026-09-03 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0670021-71db-3c8b-8f93-4a654653756c | -10.99467 | -45.09116 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| aa8bac74-343e-3c28-b849-4bcc2bd087d1 | -6.76014 | -44.56506 | 2026-09-03 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README18.md)
