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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 745ccedd-7e9b-3636-ab8a-e3fa95df3563 | -2.21246 | -50.78704 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c54815d9-59e5-3258-9bd2-3c8437bf025e | -2.15773 | -51.01432 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 340c251d-4492-34d7-b65a-fec7544e1963 | -2.0679 | -50.87439 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a7fac18-926f-3d6c-9387-c119a5a67863 | -2.95836 | -51.0026 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce41457c-8273-3ab2-abd6-21e279b1e4d1 | -2.95814 | -51.00012 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f082a3c-926c-3760-9bd4-694a5360fe67 | -2.95531 | -50.99742 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8530068-1d2f-3a7f-8bd1-d03a9a2037b4 | -2.95459 | -51.00201 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a979d8b0-1344-3464-862f-783c054d8925 | -2.92606 | -51.75243 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f8106f-adaa-3e94-9fcc-89eeddb20264 | -2.92178 | -51.75608 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0337d6d-9409-3f00-8807-a3331032f69c | -2.91751 | -51.7597 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b02e8a05-9bff-3021-ae07-9e4dca030c65 | -2.91389 | -51.75912 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b8a2349-98d8-3a8b-a4f8-f17006f68a19 | -2.91325 | -51.76325 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fec388a0-96d5-34b4-8932-70e05b2a8066 | -2.88425 | -51.83089 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117095d6-a3c7-35eb-8c80-a43d5dedd8d5 | -2.88129 | -51.75411 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23d99a4b-f188-3856-9dd2-a98a757240a7 | -2.88064 | -51.83038 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f89658b3-0135-3920-b644-27549e99ccf6 | -2.87959 | -51.31046 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54c45361-3d27-33bd-aaca-140805b8151a | -2.87588 | -51.30989 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 891120c2-bd86-3d05-b8dd-d0da22162bb5 | -2.84408 | -51.80375 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 737238bb-ce15-301e-9974-e57ea0bcfa19 | -2.84282 | -51.812 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7373e89-a546-3edb-ae20-43fce6e11c40 | -2.83984 | -51.80733 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bdaa941-c5a8-3dbd-9e29-9481e5837034 | -2.83921 | -51.81146 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9877aabd-146f-3de8-82bc-86227d90e8ae | -2.83623 | -51.80677 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6bdd5e0-fa9a-39c0-8767-ecd9b000ca1e | -2.8356 | -51.81091 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de8d9a03-76ac-3d16-91b1-763ba3f97d06 | -2.83537 | -51.80816 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20423f03-0db4-3248-a13f-0f3154462709 | -2.82934 | -51.03625 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a283202f-9dd2-3506-95de-abc0fbafbba7 | -2.82426 | -51.90969 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 111d649e-9c89-3c62-9b3e-40542a398c3a | -2.79929 | -51.80255 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd7ed4b5-2afe-38a1-994c-5fa43896c8e4 | -2.79439 | -51.8103 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 165b27e0-9425-3ed0-99af-f900d1faf848 | -2.79303 | -51.96047 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c701d12-e3d0-3dd6-8bba-d4e13e1266f6 | -2.79218 | -51.46115 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f1b554-ae96-37b4-9a29-375a62fb8239 | -2.78851 | -51.4606 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f46c52d-3b65-35e7-8bd6-acbdd04a8fd3 | -2.73715 | -51.72522 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a72351d2-693d-331b-a8d7-a35313cf76fc | -2.73613 | -51.72652 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7355cbae-0538-345d-98ff-d87d9935b450 | -3.27562 | -51.61607 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55d77f0d-0dd7-3e3a-8ea8-542a53093ec4 | -3.26259 | -51.57904 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ba09dfe-19f7-3eda-8535-36871ab602ef | -3.00907 | -51.77221 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82a5e811-fd82-37dc-b41f-4f820aee69a8 | -2.92541 | -51.75661 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb02ea4b-2179-3cec-af6e-a47a72b79b71 | -2.92243 | -51.75191 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bdf4ea-b4ce-3c5e-bd9f-468439cae268 | -2.91027 | -51.75854 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75849550-01b1-3c85-84fe-19f6ff96045c | -2.90963 | -51.76267 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f405ae4-92f3-3365-8f20-96d972c202c7 | -2.88149 | -51.65583 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e43ac93-9ee8-3b3f-b7a5-5b0d60901fe4 | -2.88128 | -51.82627 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 936d957d-f875-3565-afb8-43ae9b4cde34 | -2.84345 | -51.80788 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3699c8b-b343-302b-8e3b-41946ea8c9c2 | -2.84047 | -51.80318 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa07ef78-cfb3-3610-bd28-b044c7f4ebf7 | -2.83602 | -51.80404 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bc601d2-29e9-365e-8201-29a3171ece34 | -2.83199 | -51.81033 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea53b3f7-df9f-3893-9c2b-832cfd560994 | -2.81223 | -51.59929 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41055bc2-c4f7-3545-8b48-732abf2ed3ec | -2.80289 | -51.80312 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0af5e0ff-a283-3d7b-aaee-99628d60447f | -2.80225 | -51.80727 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27c618e5-8143-3c7a-8a1d-eb2ac6a7d455 | -2.80063 | -51.6019 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 023e415c-e1bd-3691-b291-b31b365348bf | -2.79864 | -51.80669 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 576710d3-f0b3-35ea-bb39-5e8a9d2c86c5 | -2.79504 | -51.80611 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb54bba-2eea-32eb-b930-ecc472c2508f | -2.79367 | -51.95642 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbb1960b-e4c9-39aa-963c-1a9afdb49aeb | -2.7865 | -51.95532 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 331f6328-59b7-3a2b-81bd-c9e497deb0f4 | -2.73679 | -51.72235 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47777292-f910-383c-92b3-a7c5bb658944 | -2.64608 | -51.73386 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55600830-1be6-33fb-a1be-40717896f1e5 | -2.64482 | -51.74215 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b526b36-84cd-3410-86a2-9c95fbb88dbf | -2.64418 | -51.74629 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 09293aea-156e-39f0-bddf-aa8e4a30ddbe | -2.6412 | -51.74159 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 924b9ab2-a79d-3a70-8f57-e6916eccbbef | -2.64057 | -51.74573 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 861e686a-32a6-3beb-9215-a75aef19f923 | -2.63885 | -51.73274 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71538ecd-21e7-30b2-9b1c-5c71541c98de | -2.63587 | -51.72804 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e06d9dd8-b4b9-33fc-932d-639940319bf1 | -2.58379 | -51.93877 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 303b69ed-eecb-3ead-9a3f-f3fc455028e2 | -2.58274 | -51.92212 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6941443b-8633-3250-abf3-e1578e3ca5b1 | -2.57985 | -51.84674 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f89daad-22c4-3c7b-a2eb-ed239704fb42 | -2.57562 | -51.85029 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f889ef-a037-36f5-83ea-1e5c625f4455 | -2.22223 | -51.87067 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c2a1676-5122-3b21-8f2c-63832cc1526b | -2.65078 | -51.75154 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ab6e8eb-f85a-336e-85b7-52857c82681c | -2.6478 | -51.74684 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cf6e406d-7219-3269-a397-142637c1b9d3 | -2.64716 | -51.75098 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23fa759e-ccb1-343d-88a8-d88e2a669344 | -2.64653 | -51.75512 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0bffcf1-8963-3298-b94f-4fddbc063d2b | -2.64545 | -51.73801 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d806e7ba-b408-3c5d-99c0-01476997a7ba | -2.64355 | -51.75043 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 319a75dd-ce96-30a7-b74f-b1446f2a6f3d | -2.64292 | -51.75457 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a67598ce-7f81-3b46-968d-b0cbde22b1a8 | -2.64247 | -51.7333 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d081ce5d-7d06-3fdb-a49c-5f77500655f1 | -2.63994 | -51.74987 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0bc7cba1-fddb-33a0-9f22-408c2c7c51a6 | -2.63948 | -51.7286 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 100f3b56-a858-34f1-aaa3-a614e4c6907b | -2.63759 | -51.74103 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d555137-96d8-3210-8c55-d8f28bbcefe4 | -2.60155 | -51.7787 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08aefbd9-15a3-34b9-96d1-f492352fa839 | -2.5973 | -51.78227 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba6ecb33-c720-36fb-9bca-e3bb15ded573 | -2.59413 | -51.10963 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c26ede66-58c5-3e93-99f5-a5a4b1606e62 | -2.57626 | -51.84619 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 227b6798-398f-3094-ac33-478be4f9b456 | -2.54516 | -51.17922 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ef8c82-7e4c-33b3-8455-193b2bc61db0 | -2.54076 | -51.18305 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a00ff41-a22b-3645-b949-2f63ea1be8cc | -2.5384 | -51.17365 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc3217a9-2543-34ff-ad69-a0013bfc5720 | -2.53704 | -51.18248 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76ff258-cbe3-3758-9ab7-f1e34ad63587 | -2.534 | -51.17749 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bbd77a2-c076-3e9d-89e0-946ba5afe82c | -2.53332 | -51.1819 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11bde2dd-0913-3e7e-b963-241d375341f9 | -2.53265 | -51.18633 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be0821ec-d0ab-3ea6-a4d8-c19dc14efa36 | -2.52893 | -51.18575 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed2ec027-32f5-3108-ac59-3ebc5121a132 | -2.52825 | -51.19015 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eee295d1-61f6-3328-9c15-4e27eb064764 | -2.52758 | -51.19455 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce4194b2-bc4e-3229-a980-4bdb2a21c9ee | -2.52751 | -51.04458 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37dd512b-d99d-3007-9a1f-dbc367c62fcc | -2.52656 | -51.17634 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9fa13b9-a11e-3722-8b64-679cdda33ab7 | -2.52588 | -51.18076 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14750519-2469-392e-b24d-436f25bb24ce | -2.52521 | -51.18517 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b451d18f-efe2-3142-bc26-f5e2fbdbd5e5 | -2.52376 | -51.04401 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bc2c9c7-8fce-3cf3-9bd3-4f4d8824968f | -2.52284 | -51.17576 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a40ccce-8e74-3ede-8af6-5a66e4f77833 | -2.52217 | -51.18018 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 362f0668-85b9-31a8-993b-83b4b7291370 | -2.51845 | -51.17959 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README78.md)
