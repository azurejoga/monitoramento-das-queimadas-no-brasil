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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7605daac-e6c6-31a8-b63d-01670c8d9b35 | -3.06099 | -50.34344 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2edabc5d-0c52-35c3-a823-4997615ee165 | -2.63422 | -54.38 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f72351dc-7794-3e2c-9b23-96ef736fcdce | -3.06202 | -50.33644 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7107f219-16da-3eb1-ad06-4c9243dc5d1e | -3.49624 | -50.24789 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bba886e-906e-34f2-8298-68cf24ec549b | -3.34985 | -48.96119 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6fc7b910-a362-36d3-b6e2-2ac9fc854db1 | -2.93707 | -54.10191 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b8e12f-0cd8-3b3f-853b-49942d01cbbe | -4.56658 | -49.38789 | 2024-11-13 05:22:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cdacc38-11af-3b69-80e7-64c5347fc164 | -3.10518 | -54.30322 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03cc37b4-8cdc-3621-a860-e8ba7dac5450 | -3.52561 | -54.48481 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a40b0e4-198d-3138-a067-a4566ea2aef2 | -4.6547 | -47.42751 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4f5bf3e6-2664-3124-acc5-bbeb03e92cd8 | -3.94128 | -48.14773 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4c2f231-1f5a-3611-bb7c-457d22f6ec34 | -5.15306 | -48.17934 | 2024-11-13 05:22:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac9316f6-1a78-338f-94b3-7f81410ca04e | -3.9489 | -48.18464 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5c4834a0-6d29-3e82-ba42-c628a406f9af | -5.15314 | -48.17963 | 2024-11-13 05:22:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3436368-fc83-334d-97ee-51cc2f8cf153 | -3.16784 | -50.4534 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be8dd548-2d10-3157-8477-6019e7780bd1 | -3.79694 | -52.0951 | 2024-11-13 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12dffea2-8b47-3815-a865-0ceb49f4ae31 | -3.04464 | -50.33088 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 59be7e29-f0d6-3cd0-a651-97c37981ee23 | -3.801 | -52.1013 | 2024-11-13 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8224715b-f8c7-301f-bdc8-1d7f8f224bc3 | -3.24495 | -50.3092 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8235db2a-11ba-392b-bd6e-b9bf743aef7d | -3.40508 | -50.3688 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9ee022-03de-3ed2-9159-2708df53f5ca | -4.66223 | -47.4228 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8f314dee-f263-3c4e-b1ea-175a1461c92a | -3.34807 | -48.96 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| dd173595-4d9a-35ac-80e7-905cc4bf305e | -2.6259 | -54.27082 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88210151-6a26-3f81-a5b3-767b6f1fbd0b | -3.31522 | -54.91284 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46be1e49-7385-3c80-9845-f6696c9ff1f8 | -3.37694 | -54.64518 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 836a0fb1-5104-349e-8ad7-ff1edb79c2bb | -3.22492 | -50.68317 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1296065b-959e-35ed-b19d-65441ca18de0 | -3.23217 | -50.67088 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d87af46b-411b-38dd-a859-86014f80ee18 | -3.44533 | -54.63361 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af162e3-7faf-3ed8-bb7b-2debc763553c | -3.0571 | -50.33204 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea61427a-541b-391b-8367-ecc2475bcb18 | -3.05012 | -50.34175 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adbbc5a2-0bb5-3024-88ce-762ae82afe56 | -3.34873 | -48.9556 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 58ec4777-cbc3-3cd6-accd-dbbddb8a9026 | -3.06253 | -50.33291 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8712a3d-c261-3d7d-88f7-2555e202c3b7 | -2.88207 | -51.79581 | 2024-11-13 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f65da468-22d4-38fd-af08-affeea04a2e3 | -2.98581 | -53.97917 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64bf3b71-eb69-33ca-9499-3bf7137f07b9 | -3.06363 | -57.30409 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34a50151-5000-31d2-876b-895e38e73848 | -2.7704 | -54.73391 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4df61b7-7720-389c-93d7-3fdc21e677c3 | -3.35048 | -48.95679 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| be21432e-71a4-3172-9b08-6088ffce90d9 | -3.069 | -50.32679 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35cf4b72-ae3e-34ea-80ae-ad3401b93098 | -3.09994 | -54.30994 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 206a02f3-ff1f-3d1d-b468-d5ac32e59ecc | -10.73282 | -49.53042 | 2024-11-13 05:22:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9e551b70-04fe-3b9d-8363-6f775f94ddbe | -2.76986 | -54.73745 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c05eef1-e53c-34d5-b16e-b9fd8dbf6135 | -3.05166 | -50.33118 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d378627a-767e-3821-99b6-63cb279320f3 | -3.14766 | -53.24477 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53fa9d70-ab41-3da3-8e90-558e8b06847a | -3.8185 | -51.26329 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e6f47a6-ae2e-39b6-be0f-0fbbdebcd83c | -3.09468 | -53.26349 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9191a569-cefd-3ffd-8dda-ff249937a58d | -3.05266 | -50.32431 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa5af7b7-5535-39cc-b61f-b4a0412cd30b | -3.58071 | -54.64588 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4680938a-6926-3584-81d0-c1c532c5ae1a | -3.62862 | -54.1143 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9890586-c4d2-3739-a1e1-e481e778b995 | -3.24807 | -50.39876 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60e8cddf-9e04-3319-a644-16e28f6653e5 | -3.2544 | -54.52799 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b43a6502-fcd9-358a-baca-d9f93c1e6218 | -3.44941 | -54.63422 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a06c4c5-0d9b-3707-99f8-aea640389e3e | -3.25096 | -50.30639 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e48068b-47ec-3da4-8463-68f81cd21cc5 | -2.9427 | -54.23371 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 577bb287-6612-3a0b-bf19-28b1b43af84b | -2.93451 | -53.23064 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d9508ad-f7bf-3152-9c50-1b40bb4a996c | -3.04518 | -50.33747 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3b28052-8d4d-3126-b7dc-889db0f415d7 | -3.31259 | -50.08228 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a4402fd-e53c-39cd-8b7e-f7e8ff928480 | -3.15076 | -53.23864 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de475495-d3b1-3c9a-928d-f4e5678977e2 | -2.4816 | -54.0659 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9030b05f-2e05-3152-8e12-6da255f174ed | -3.25607 | -50.39392 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f3c3a7b-033b-3b99-87df-a9d96bc291f8 | -3.35471 | -48.9565 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d188b013-2254-3545-93c4-7a13ba12dd2a | -3.13539 | -50.43925 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e09e2ae0-417d-38c9-9cf6-a4ec44b27418 | -3.33492 | -56.95495 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3635b47-7140-37b9-937d-d8d22d1b38ee | -3.05552 | -50.33253 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cffef062-2741-3117-ad8d-5e8b1b1dd0b8 | -3.11709 | -53.70506 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9384a67-c88c-340f-9e78-753256be6de4 | -3.81229 | -52.35279 | 2024-11-13 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50e24d77-4ae6-32a2-873a-51f898e0bbdf | -3.13591 | -50.43581 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fed19d7-613b-3301-86c3-da36beafd06e | -3.86549 | -49.11601 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0fe93b12-b4a0-3be4-bc73-cfd160da6ede | -3.05444 | -50.33955 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fe9e914-7642-38e0-9904-5d7e3eeee0c8 | -3.76242 | -54.64799 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a918d47c-c1e6-35da-8d4f-3d764a1d05a4 | -3.16443 | -50.5879 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 925fd79e-0ec7-35c8-8b9e-a9aef8a550cf | -4.22407 | -46.45394 | 2024-11-13 05:22:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b585562-8794-3945-a5f7-8ad85367d341 | -3.06134 | -57.30281 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e235c25d-d17a-393a-af4c-02bab4701c75 | -4.3352 | -50.42009 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79585044-6db0-35f9-8fce-48f03a932da5 | -3.05658 | -50.33557 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dabcfe5c-1189-3c31-87a8-2a63d21b09ca | -3.07443 | -50.32766 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 812cd3ce-8509-3c85-b293-4355e5757908 | -3.30574 | -54.48682 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb935e57-9ce6-3350-bf3d-f42dc2fa18be | -4.16334 | -59.90457 | 2024-11-13 05:22:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5c8d2be-8a82-3f5e-b4f9-9dcdb6f71fea | -3.3445 | -48.95586 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 24aec72c-e8c8-33f4-9877-ca7beaf4217e | -3.49447 | -50.84351 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a080d05c-3e78-3741-bf2f-833c2dff5797 | -3.43683 | -50.30548 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7e767cc-8713-375f-8375-f1be49af3277 | -3.1501 | -53.24311 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dbbb0413-6094-3902-bb34-c987fe25e77f | -3.25556 | -50.39742 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0580725-6244-38be-b29e-9e73a214abce | -3.62444 | -54.70811 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05ea7c9d-b990-3e66-8cfe-8ed7d6003436 | -4.1054 | -55.17172 | 2024-11-13 05:22:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99106e53-bdc9-39b6-b537-b201632cb0d3 | -3.62561 | -51.49128 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c063900-e39a-34a7-a35b-2799db975ffd | -3.07341 | -50.33464 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eca42a49-af5a-3f7a-9894-5a460e43f3c8 | -3.85889 | -49.1196 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e94fd95f-5b20-3734-897c-5f418796b4b1 | -3.17377 | -50.45066 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 96e8d8c8-0ecc-38da-bd59-eb1c66caf937 | -2.95633 | -53.85788 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b722719d-a5b0-32f4-8bf8-4b3bf7b024f7 | -3.09634 | -54.3057 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1243be1e-4e25-3249-bd63-6663dd62283a | -3.26201 | -54.53292 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83282184-006b-3da7-9e39-a7e4f5a39b03 | -3.89234 | -53.43471 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe0c6c2-39da-3ce7-9a49-3a592a6a2064 | -2.86467 | -54.20391 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f63dcfda-6724-3e68-8d2d-3cb6dabbfd44 | -2.96474 | -54.68439 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab39bb64-dabd-3780-8a04-dbf4388bdc4a | -3.52616 | -54.48113 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72dff9d4-7a75-33a7-ad64-f85e39ee2a0f | -3.2793 | -53.66942 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c0cbca9-933b-35d4-8ef4-7d1810f44038 | -3.11217 | -53.70846 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b80cb81b-ee77-3cf2-83c7-4e21589f6660 | -3.52972 | -54.48549 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a829e626-7e20-31af-b6e3-3f966c788397 | -3.10464 | -54.30686 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a2846a8-7146-3ce2-911e-df8ced0df47a | -3.02782 | -50.96806 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README50.md)
