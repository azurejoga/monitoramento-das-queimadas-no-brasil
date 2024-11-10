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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fd23f0d-f98f-30b8-af2a-8f5c977b19bc | -5.07445 | -46.05564 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 652da80f-90c4-3b97-b92f-43b133881405 | -2.62031 | -54.39658 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5158f8de-4890-3574-bfa5-fa0863bbedfa | -4.04101 | -49.73048 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8776836-0d7e-3c35-8436-ec08dda2d92e | -3.02933 | -54.20694 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8db054-5956-331d-b98a-6096809e5f0a | -2.65568 | -49.86996 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a959bba-0b3a-3ced-be7b-3b82e7aa2c64 | -3.24426 | -50.45652 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75e1bb2d-149f-3c1f-ba5a-517e69a091f4 | -2.84257 | -48.4692 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674fb800-2634-34f8-a1f4-0eef13d3e400 | -3.23452 | -50.27451 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a918398d-ac10-3074-92c8-33066769e6ae | -3.42086 | -50.31046 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62e988b7-15d7-3cad-8fbf-2ba910c1933a | -3.24629 | -46.48561 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaa0c590-8f7f-3e1e-84e6-b2c4ec1bdd23 | -2.91583 | -49.50761 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e64e2e91-8f04-3e8a-8535-11e75a63250d | -2.61298 | -51.74355 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5bbed64-531b-3278-82ea-80f9d48d3342 | -2.26753 | -51.89285 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| befd49e5-ef64-35c2-9b99-7917d6911e93 | -3.22868 | -50.68233 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1fb16082-13db-34b8-870c-22b75ec6e8df | -4.49854 | -48.46329 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28bf59a4-e9b0-392d-a17b-6299a21909e1 | -3.15261 | -45.94687 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69315425-31e5-37c0-bcab-be9a6c29b51c | -3.95534 | -48.14723 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7068f04-69e1-3310-bc09-343c04dfb958 | -3.28619 | -49.62305 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ed2963b-1170-3de8-bf1d-7b621e901b99 | -2.71525 | -51.71087 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6130d15b-270d-32de-b6a7-9baefb66f264 | -2.89229 | -49.25326 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7238f93-213a-31d9-9e83-d33559eecad7 | -8.37921 | -44.145 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3e476f8-22cc-333a-a31a-63bd348757b0 | -4.13198 | -48.23525 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56da5f41-6379-328d-a53a-c64da155cf7d | -2.44488 | -49.83373 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90fa20a8-f394-3f92-b207-7017a1093951 | -3.69517 | -45.81501 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1a36e1b-824c-3ec6-be6a-a4da8203e300 | -4.43487 | -47.26208 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28aeb9b1-0f55-3cd4-83d8-16ec59beeea5 | -3.82593 | -55.66911 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 832d38a5-9e46-3db3-a790-1f31d3b68cc2 | -3.18852 | -54.31545 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b908298-1536-3b93-88f7-b88af95565ea | -3.04349 | -49.53832 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74aec143-5aaf-35a9-a598-fb17e383e955 | -3.38189 | -50.22652 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1b787fa-a333-3f6a-bb99-d8c9ff2bd10a | -2.92481 | -49.58112 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba1de889-f0eb-3366-9273-9bbd48892a4e | -5.12337 | -49.3297 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bb9bc1c-7640-3ebe-a5e2-78856cb1708f | -2.41766 | -53.67226 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9599461-6127-3885-a0d9-d22a953167d9 | -2.91393 | -49.23866 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 609feaef-12a2-3efc-8f7b-9ddadb62f10e | -3.22771 | -50.27343 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5baf7536-ce05-3693-ba3a-b39b2dffb843 | -2.4611 | -53.69008 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebbafea6-e33f-30df-8523-6d7c85e13daf | -2.19679 | -50.34129 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da413427-8eaf-3da2-bab0-69917cd8ff36 | -3.10051 | -49.40684 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c9b61e9-0682-355f-ae63-7bc1ad71df5b | -2.86844 | -49.27453 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe90b124-652b-316c-96df-c8eb95091ff1 | -6.09168 | -44.02691 | 2024-11-10 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e09c3b08-315d-3fbc-9676-3a71d6f29259 | -2.83599 | -48.08301 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e479972b-1576-3183-a2d8-ad2252bec101 | -3.45535 | -50.35704 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ae304e-70e5-301e-a225-0134beaa2fa7 | -2.19854 | -50.52969 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f78d5c6-8093-3b6a-be01-a799d1638520 | -3.23588 | -46.53026 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89c38168-fbe5-35e0-a94d-07ce3c6a8a1f | -3.14615 | -45.94184 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 454cb3f1-2525-3e3a-b91d-7d297b9bc833 | -2.41844 | -50.48579 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cdb1c07-0075-339b-a38f-9cc6d48dcf99 | -3.45862 | -50.18254 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60179f6b-1e1e-34bb-ab61-3a200587ce49 | -3.28507 | -49.63009 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed675fd0-728f-3dc6-bdba-d305d5d8fc7a | -3.96601 | -48.18806 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 792f3905-6425-3fc2-be7e-61b9b4a839e6 | -2.93981 | -54.46044 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ca5557-bb2a-353a-bdbb-8d9af4120aef | -2.61622 | -51.74688 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1752fdbe-e9ea-3885-9d1d-18e797e28619 | -2.30643 | -50.73276 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6add015d-b004-3dea-b15f-287cab545702 | -3.15179 | -50.2247 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ed699af-5748-3b6c-b385-f536851aa782 | -2.86018 | -48.4437 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee6a7b1b-24ed-32bf-941c-53c8547af96d | -3.34018 | -50.35811 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6100e2f-0594-35d5-99d1-a19ae13dcadf | -3.01827 | -53.26615 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e97d305-85f2-36c1-b814-4b133a9466b1 | -3.11008 | -45.96455 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94d783c0-2e05-3ea6-a490-8d4a9d93f71c | -2.64043 | -49.90065 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d7adcfe-09a9-3198-a42c-9190b313df94 | -2.37277 | -49.82978 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e83aa50-48df-30d7-aad4-cd6e3aa193c5 | -4.74584 | -48.9129 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23426397-eda1-3255-8a4e-a8ae5c898b2b | -4.11802 | -46.92172 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acabfcd-b838-388a-84bb-fd44e7cbcc01 | -7.17526 | -45.39148 | 2024-11-10 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33bd036d-1477-354e-b0d7-90f0121f7571 | -3.99516 | -46.4195 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 250f92f6-9ce1-3b3d-8647-dacb860c5b08 | -3.63263 | -50.18767 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84f6a530-0d97-3f97-a464-adee59169382 | -4.43977 | -49.67458 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7ec2787-cc2e-3862-8119-a7d4c662432a | -3.22772 | -50.45012 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e227fe4-29b1-3980-bf83-bd023e3413da | -3.10765 | -48.61345 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3915c812-3595-3cac-8a82-ee71e437ac86 | -4.38411 | -47.27293 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f4bb8c9-d4f7-3d47-9233-43b13d018d5c | -2.73008 | -51.71138 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9f090ae-5def-3d68-a9cc-a699d45533ef | -2.61553 | -51.75109 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0bbf42b-04cf-3759-8867-746f223198d4 | -4.60422 | -48.69567 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8e95304-e63a-342f-8bf5-a083a43153e0 | -4.69123 | -49.62136 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cce509f-3b81-36ce-957c-d5b3dda52142 | -4.07179 | -48.31476 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1913fd86-4189-3e77-b723-16a9f0516475 | -3.89646 | -50.3064 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd30202e-5c5f-3637-b894-470134292b02 | -3.327 | -49.90874 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fc83496-91ea-3c88-92ba-ded3c7652f03 | -2.80223 | -48.66061 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b805a14-d8a3-352f-9b90-76d4dbc9e5a4 | -3.98362 | -48.14096 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0640bda0-1872-3886-8bce-bf802daeed04 | -2.42008 | -53.65754 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3142b7ad-3120-3349-9ae6-68fff0eb0b42 | -2.86952 | -49.51835 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d152b31-f9e9-363f-8339-ffb557132e64 | -2.87016 | -50.41395 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e6aae7c-fa1b-3783-8bc0-03f44064984d | -2.6476 | -49.23608 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d874378-a1d4-352f-b5ad-e8b3e03e4fc6 | -8.40361 | -44.12485 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b3fe0ad-6494-35ae-8000-c648c7078ae6 | -2.31309 | -50.48885 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9c94824-9451-3311-8b5e-4245845d709d | -2.82249 | -49.43566 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e000dc7-b204-36cb-a55e-acd82fcff61f | -4.60319 | -49.57896 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91d99c67-f843-3312-886e-e4957c206117 | -3.7949 | -47.47047 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a858ec5-5dae-33af-91d5-f52f83898478 | -2.88891 | -49.23133 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e29de80e-251f-3867-a417-389469fc4d31 | -3.68739 | -45.81795 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03050c91-34f0-3907-a67f-1b4965f993c1 | -2.93838 | -51.48151 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5732b20e-8a29-3323-af1c-5f1827825c6a | -3.96192 | -46.70681 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 883b1c49-6782-36aa-a86e-7c0e6a283da1 | -4.74778 | -48.81407 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf658727-c8fa-3a9f-9e66-785d2bf97591 | -4.31803 | -45.66393 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d4dad5-d6d5-3d1d-a6f4-2b0f81941db5 | -4.0646 | -48.3172 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76f9445e-4684-34d7-9648-f703548d5a42 | -1.42464 | -55.26805 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f80b436-df45-3645-b41a-57cdaf2a51b1 | -2.23604 | -53.7732 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 667ae401-ec61-37e5-87d9-1760015da88d | -4.70343 | -43.87017 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e07404fb-adeb-30ad-9209-32c7ad7a64d1 | -2.87946 | -49.22629 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f9c004e-ebb8-3151-a71a-6bb5c24e83b2 | -2.66407 | -49.13167 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 619e7df2-9c8f-341e-a47f-f9e9de5d4c70 | -4.41125 | -50.08516 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39adb22-da0c-324e-9c4e-da865ef8820e | -4.43624 | -44.62271 | 2024-11-10 04:38:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dd41a137-6a03-3567-9f37-7600aba4b002 | -8.38509 | -44.13396 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README95.md)
