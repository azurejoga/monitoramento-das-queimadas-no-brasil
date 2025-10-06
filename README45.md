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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d4cd530-72ee-392f-b3d4-88a5e9d4a1a7 | -13.26781 | -47.59003 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ea71734-5d5f-3b81-a975-59398f634bbd | -12.89789 | -47.29896 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 147b0f72-51ec-379d-acaf-4e2d696013de | -15.19811 | -52.809 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a19a9f6-bf85-36e9-868f-6d29d09d59b5 | -10.76902 | -46.6168 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 269de274-95a1-3871-afa6-3db44ea2e90e | -14.71174 | -48.38499 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 590cabb1-3fb6-39f1-b7b5-14f41e75e3ad | -10.3687 | -48.14806 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc69af2a-cd4d-3145-b016-2a68080ed156 | -10.34859 | -46.95783 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8eca702-6e5e-37c7-9a3e-e17e2d6975df | -14.69692 | -48.37163 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a531811-3ec4-3444-a2ba-0629abc5d542 | -9.68833 | -48.20838 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90c466f8-538b-3707-8c61-28d7cecba862 | -12.90836 | -47.29701 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cde1c4a1-f40b-3f11-ac9d-ce7764a2fa64 | -15.19897 | -52.80403 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1e4592d-f5a5-3b81-977c-9fc430c22f38 | -15.92864 | -48.99814 | 2025-10-06 04:27:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eda8130f-fa04-388c-963c-2892ded2563c | -14.67709 | -48.39016 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d379aac4-7eba-3987-a1d4-94d242e7a496 | -10.59466 | -54.35156 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0140ab85-9026-3503-89d9-c03180e2cb10 | -13.28045 | -47.57401 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ddc030b-95e4-3be6-b66d-22abf2af554a | -14.34304 | -47.67477 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 911284ad-1537-37e7-84a7-0e5de99606ed | -10.59745 | -54.36225 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57c0b127-83cc-3b10-b875-8fc2fac99f4e | -10.76625 | -46.61275 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5496c9f-f967-308e-8c9c-c9dcb328358d | -11.7075 | -45.41354 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33e513f5-ae32-3813-8715-c87496921e95 | -14.6431 | -48.32645 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c10653a0-358f-32a7-8403-baa7e0888b04 | -11.77755 | -48.89719 | 2025-10-06 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 436ad2be-39c2-379c-803e-8a5847353de9 | -14.63476 | -52.55053 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1442bade-1e19-3399-8a92-73a5483a89b1 | -10.60967 | -49.1429 | 2025-10-06 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca352d57-beac-3a62-84c6-9f11c849a82f | -9.48269 | -54.59859 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8995d718-2297-3586-bd4b-9cfc880035f3 | -16.35278 | -47.05482 | 2025-10-06 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db47a4db-83eb-33a4-95e7-ecf1739bbc21 | -15.5762 | -52.44576 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dcbc8dc6-a555-34f3-be68-e27a9a4050a5 | -9.15093 | -58.31664 | 2025-10-06 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70b2958c-1d00-38c4-9b2b-1d560181072d | -15.87235 | -46.24429 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cac30369-67fe-328f-9ef8-856ff49ebb78 | -13.11773 | -48.00581 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7fc70b8-b075-36e7-9cc4-bb346977e06b | -11.50559 | -54.46346 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df307656-572c-329a-ae7c-21d90577441f | -14.67884 | -48.33595 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e643695-aaa7-3381-96b3-21879051ae02 | -10.76682 | -49.708 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7107df53-d73c-324b-8989-5281044a12cb | -13.26836 | -47.58651 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebf97432-fe55-3361-85aa-8000ff7a247c | -13.73098 | -48.06696 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 354105d9-7722-38b1-bebc-386060cc4583 | -11.47749 | -45.04914 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e7bbdb4-06b5-37ac-933c-471861632190 | -13.36297 | -47.56984 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebbb949e-74ba-32aa-b325-8fb44c90c182 | -14.69747 | -48.36809 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf54fa47-239e-378b-82ca-629c2b8ed0cf | -11.71932 | -45.37988 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21fe1129-c6bc-38f1-920b-88e021893fb5 | -9.33321 | -54.52048 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 002f5afd-4ff1-30a9-914c-9674ab5ac2fb | -16.03145 | -51.04744 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 12a0a9a8-89b0-35aa-9500-e03809a51e6b | -11.70852 | -45.40567 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53858488-428e-3c5c-876c-56ffdbcd3f6b | -11.50245 | -44.97638 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22c39485-6a8f-3083-9b23-3d9f360c4294 | -14.49382 | -47.53484 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a72ee56-2acf-3ae7-bc1b-a3526c92c7a5 | -10.29014 | -50.28115 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88f183d2-f3f1-3b5d-a768-9699af6921a9 | -12.90174 | -47.29596 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edc25f02-2368-3fcf-870c-bce89f42e31e | -14.68262 | -48.37653 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3ecc77ab-9385-374f-9b0c-8a9bc5734d63 | -13.08815 | -47.82792 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc545c71-f14d-3089-8702-a6a00aa5d8ee | -14.3237 | -52.98405 | 2025-10-06 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbab2a14-0bba-3b57-8783-82155ba925d4 | -13.63017 | -48.70371 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae32d0bf-f4cc-3ad0-b4b3-fd009e5a9dcc | -15.98981 | -50.93362 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 08c5dd8e-a8b4-37df-8327-01cc0fee884b | -10.39897 | -51.58868 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aeac245c-20e1-35f7-98a5-e46f50f287df | -10.9633 | -47.05294 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 795be31b-881a-3dd7-a928-5ef91c7a4cf8 | -11.80462 | -45.11257 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bc6701f-8dba-3c1c-933a-a7a4aac63f61 | -14.91619 | -46.85703 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9da268ad-1652-3e12-a4d4-a2a35f269b9e | -13.83719 | -47.91064 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b58443ca-1587-3186-aeaf-5927e99ab730 | -13.69568 | -47.32952 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f38d302-8a9e-356f-8475-771a3da2de58 | -11.80402 | -45.09251 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df55d4b1-9680-3227-b374-3d579a369e34 | -11.92042 | -46.24223 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad29bf14-fdfc-36ca-99d6-5b409cb1a37b | -10.46481 | -47.82055 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b147219c-e71c-32ab-8c7f-4c76a56f33de | -11.44686 | -44.95608 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5600c34-8fba-3563-9694-7029a6719626 | -14.69144 | -48.36346 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78723f54-e706-3caf-abb9-58338b5f4e4f | -13.62354 | -48.70265 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e3edc05-935c-394d-8261-809bef75b257 | -11.18016 | -54.12325 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49c2ea6b-f0fd-323f-8891-9beb3dd8a06a | -14.88539 | -50.12844 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8899210c-adf8-38e7-8ed5-389aeeaf70e0 | -15.18202 | -52.76501 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8367fdd7-7222-3806-b548-f798aed9ee23 | -11.08059 | -47.75919 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 739f2a67-0842-36d6-8d59-1dda6fb2032e | -8.50174 | -54.59471 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0520550-3016-3733-8582-ca62a964ceb1 | -15.34766 | -47.35158 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6824da98-5658-3399-bfc8-4df4a30fe0b8 | -11.85116 | -45.03877 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79ad66d7-da80-3bf7-ae84-c898f958234b | -9.43732 | -49.24 | 2025-10-06 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5d1f7c-4a35-3f2f-9744-4912a029961c | -11.87348 | -56.86737 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71ed8ad-869c-32ad-a0df-dec24a54e0ff | -14.75102 | -54.69421 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d77ce4-054e-3d02-837d-ae5344e13e0c | -15.34367 | -47.31032 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| fbc6787f-3349-3137-ae16-1efef4c78cce | -14.69418 | -48.36754 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f44e51d-1f2d-3b28-b7af-62f948d17b96 | -15.59255 | -52.44724 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c9c55be-6fee-350c-be07-351d25204bd7 | -14.99881 | -49.97368 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 673a7382-f363-367f-be74-97a4b1a20987 | -14.63014 | -52.50983 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f10faa2-ba54-332d-8eb8-cc0948e3f0fa | -11.12305 | -47.1648 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d3d0e52-a66a-319d-9f60-bc7ee876a4f5 | -15.58804 | -52.45092 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d34e74b-af27-343d-8992-2bd51b75624c | -16.00997 | -50.94096 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ed29a38-22ec-3636-a274-cccf2f4b3656 | -13.11884 | -47.99877 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f045bebd-3b65-3c95-b87a-1443ee5d626b | -13.2613 | -47.84881 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 40966da5-1b19-3a61-b55f-cad65caf76b6 | -14.56153 | -46.68045 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c43d8019-b5c5-3d15-aba4-14a7e8427a91 | -13.34484 | -48.05411 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b07b60d7-b5e0-3000-b32d-5e51b73cb249 | -14.54164 | -46.95165 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2ab87a1-5d98-34c6-ae84-c0d196ef1f6f | -13.10839 | -48.00068 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bafdc37c-435e-3f07-9105-15ae9f644d9c | -12.98833 | -51.04673 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92449abc-f5e5-3101-8068-0b7f93c16ed9 | -14.29343 | -45.8591 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 042d8e18-6040-3732-b659-de72df4bcaf6 | -11.48503 | -44.97368 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c78f0277-519f-3ce9-be13-bfc2f72b5fa7 | -9.89582 | -49.94584 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b75d352a-cac9-3fc2-8c80-b4615264e0b7 | -15.62274 | -52.53896 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1decc1d-8081-31b8-904e-561687c1a746 | -13.77526 | -45.73874 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e0b8e05-f8c3-3be8-81f4-15ebd840c337 | -8.90307 | -50.66631 | 2025-10-06 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 345beaad-3e3d-397f-836e-1b6d870c2486 | -13.69623 | -47.32593 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb5f3eda-5e1c-3e33-9361-e561f359d5be | -11.5279 | -47.6848 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5d9531c-f2a6-3f10-8615-4dd3b7196d0e | -14.34964 | -47.67582 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33f7bac8-be73-338a-ad17-80ba89aa7cf3 | -13.71943 | -48.07592 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0801c2b9-7a69-3acb-85fa-b6ee114a2115 | -12.41801 | -51.09981 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 727cde7b-3531-3de6-a3cf-874cf9626052 | -14.6027 | -52.49212 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cec45a5c-040c-349a-a232-86a811715cc7 | -13.30031 | -47.77224 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README46.md)
