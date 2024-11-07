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
| 3086c114-9d88-30ab-b765-329d58fe76a9 | -2.88194 | -51.30469 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4e73b44-6980-34c7-9f43-d62dfef2ede0 | -3.59656 | -50.23521 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 285f1b17-dba6-3ded-9e80-00ad0ca47727 | -2.94619 | -48.59608 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1651f411-d547-3444-a0e9-39aa0411a977 | -1.45949 | -52.58005 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11c9cc4a-88c5-3da6-9197-a5fc8da89cca | -3.02759 | -53.26879 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e24f0b1-c582-3f0f-9f42-ea15b38b0728 | -2.16896 | -46.44658 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce1cb5cf-fc31-3008-9963-8c0009719e77 | -2.78031 | -52.87444 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43b0ad26-6550-3aa2-b165-e2ad9390879f | -2.27761 | -53.79895 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ad66dd0-8fe6-33a5-8ab1-edf4dfd2619e | -2.99415 | -53.85228 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41ea3330-c4b0-3817-abe4-8aa08713a031 | -2.99609 | -54.12679 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 267f9e50-5678-39f5-ac44-b3857279d31f | -3.02823 | -53.2645 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2828cb1-f342-3c89-867e-c6f3ed08a1ce | -3.45425 | -50.38104 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 77ff366e-a93d-3187-9252-11307482b159 | -1.02374 | -47.06076 | 2024-11-07 05:10:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cbd5b2a5-5677-3698-a20e-1172cc1e21e9 | -3.24846 | -50.46076 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0e849b0-e3fc-37cf-87b8-4b20df52e464 | -3.4448 | -56.9367 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5efbfcc9-cd61-339f-9e0a-27723ac0e462 | -4.04971 | -49.26701 | 2024-11-07 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2303d675-d5e2-395a-97c2-5e7149339f97 | -3.45402 | -50.37863 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 023fc172-8d2a-3413-a67c-7f2008ab786e | -3.22012 | -50.38 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4439a320-61ed-3558-9a2d-a19404fb2d3f | -3.03254 | -53.26073 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2093d3-df2d-3d54-aa6f-701ea54f7a26 | -2.91976 | -51.04115 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28e6a00a-f60c-37d8-94be-380bc1306d7a | -2.16126 | -53.68436 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51e82efa-a4f1-3e23-9fde-11669113ff9d | -2.82938 | -52.92732 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c231b88e-ca4b-389f-8f17-89ccb6b02893 | -1.10208 | -54.20033 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3228cbb-5018-3983-af51-45ceca533dc9 | -0.04349 | -50.79082 | 2024-11-07 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2088502-542c-31cf-8263-835c32a3092d | -1.14547 | -53.71549 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8b9d692-bad7-3873-9ea3-2c35fa4beab4 | -2.8328 | -52.90519 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e6930f5-211e-367e-8dbf-0ac14e372798 | -2.8507 | -48.68243 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cd2a8aba-25f4-360f-9839-25dd3699b68b | -1.55017 | -52.2697 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7d62fae0-9746-3829-8263-f64d9fae3847 | -3.02777 | -54.08362 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeb42b1f-e205-3216-8fb2-ffbf5363cc6f | -4.39449 | -49.77019 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 25bbed1a-8133-32cb-a598-bd3fa2c51b96 | -1.95298 | -53.06985 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edebe208-9421-37c7-9998-112c561255ec | -2.82467 | -52.90849 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 027b875d-f08d-339e-85af-4ca6e162017d | -2.22893 | -46.53083 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c551bb6-f786-3d35-a008-31fac1aa39da | -3.41603 | -50.30376 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7e612e8-50e6-30d0-9fb1-327f81ba038b | -3.29044 | -50.08112 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 470a0774-6e97-3d44-92e4-6cce5f6af997 | -1.28686 | -54.56682 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2930b95-4032-3a4b-b73b-1e599a8cc720 | -3.88452 | -51.95993 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d7f3c6-61d8-336a-a1de-119482e13c78 | -3.73547 | -52.26302 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee60ec4-3763-331e-8d52-c25932b63140 | -2.91914 | -51.05166 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0f6be0-c82c-3a2a-b30a-0c1e1254d301 | -3.12597 | -51.10943 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f53eb8c3-45b3-3750-88c3-d8c0527592c4 | -3.34717 | -50.25428 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 576381a6-6b70-3bc8-8d5e-505b2836922b | -3.07986 | -50.95914 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7703e26-5a6f-3c15-95f8-c675fc8b7ba7 | -3.24889 | -53.36497 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49257d6b-f14e-3bbd-bbf5-e4680ffff2b1 | -1.41211 | -54.48895 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4fe05f4-154d-3ee0-b4c9-cd3338a95b71 | -1.15507 | -53.65335 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35900718-4db4-35ce-b899-27d6fe77640d | -3.05517 | -51.06709 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5961c0c-2c9c-381a-a7c7-5c01e062f969 | -1.21011 | -54.20493 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c571544-730e-326f-b741-fe19dc020f90 | -4.34676 | -48.62426 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9004a61-2bb6-3c2e-a9a6-228eda88d4c1 | -1.23757 | -51.75765 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 370b4a07-e8d4-3acc-b651-1d77c1d93c3c | -3.70417 | -51.38292 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe715172-ba98-3f14-bc0f-c000c890a582 | -2.97589 | -51.43078 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e72249fb-daad-387d-b7c2-2f4e704bf5e8 | -4.35138 | -48.62806 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6323283e-7480-354f-af64-463b5e5452e5 | -2.42504 | -53.66414 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0f2f0e9-9087-3aeb-8c5e-adf7452d4335 | -3.06146 | -52.49998 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 260ea105-e806-3ddd-ad20-51307dd2e9fb | -3.17857 | -50.59442 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e26168d-627a-380c-aacb-bc0cafc95355 | -3.51695 | -50.47192 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b75e660-8bd0-31ec-9222-63b28cdef79e | -3.74296 | -50.06555 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2e0f54b-fab3-3355-8610-1d9dc671b07d | -3.2279 | -50.44682 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e8a0b99-4308-34fe-9f54-b2db722b62d7 | -1.16592 | -53.72232 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfff46c5-8a5e-35c2-98a6-a26db06e4f3e | -1.28857 | -54.55587 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a3ec760-c3f5-3327-bf99-fd880278acf4 | -2.72407 | -54.14738 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e57fc373-3450-3435-bf5a-898cf5692d16 | -3.52316 | -51.53065 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a319ec6-3b15-3957-8b90-671d1607f09a | -0.2547 | -51.6423 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b12bc9e2-0ef6-30a2-b30a-460e2bf94fba | -3.44832 | -52.00755 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc837e6f-cf61-3425-ade2-483bceb1457d | -2.31491 | -53.9803 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27384021-3edb-3a0b-b1d1-ae6784dbcf37 | -2.72467 | -54.14353 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 647fcbdf-e1b9-3b68-997b-8f8a800b05ad | -0.36149 | -51.41745 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aac221e5-bd8c-3c97-8eba-89694735c04d | -2.87782 | -51.30406 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 550662a5-4fa9-34fe-a863-0c3dc9f06677 | -2.61035 | -51.75968 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6875ce4d-3289-3878-a4ec-9f46783e649d | -3.09494 | -53.71347 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fd6c9c-3453-3328-ad39-216ff0ee7a54 | -2.41231 | -47.78841 | 2024-11-07 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9bb7a006-c56b-3caf-a6c8-ff0e714fd0b2 | -3.66326 | -52.3407 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 543f8d7c-7f99-38b0-ab47-eabc51521f1c | -0.84559 | -52.84139 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9b6e2b1-b180-31e4-8613-d2d5e8403828 | -3.17912 | -53.84982 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd035d36-0a2e-3641-aeb9-e76acf7fd6b4 | -3.10272 | -53.71047 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9a0b626-1018-3a8a-bdd0-93456a79b3fc | -3.5303 | -51.59509 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6a8066b-0637-32d8-828a-c1dd9f7f5a0b | -1.52253 | -52.14876 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f32081ce-463e-307f-9174-50ca987d9e3c | -3.01489 | -53.42739 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e229e3fe-0851-3e12-8c64-d8015ae8d906 | -2.81656 | -52.91168 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8cb5c96-c3ad-3c60-9448-325974187f07 | -1.20198 | -53.65238 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b0b56dc-f00f-3661-8477-0bf2378d2986 | -3.7704 | -51.76991 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ab253f0-887d-3f10-9d28-a28d03b89770 | -1.95662 | -53.07042 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa36d29b-f196-371a-bede-79040f95b542 | -3.00082 | -54.0955 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0afa8eaa-820d-3338-96d5-2791c5008fd7 | -3.48944 | -50.38401 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd7edad9-4c9f-3cea-8698-6d6659bdd06b | -1.19002 | -53.90025 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ecb7a1c4-019a-39e4-8247-77a533668dfa | -2.67716 | -51.82862 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8688e9c8-f0e8-3ee9-9ff5-7edac32deff4 | -3.01066 | -53.23294 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50c7b5c-1e8d-319e-846e-1b69fb18c52a | -1.14487 | -53.71935 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1198f294-e89b-3ff1-a2c6-13221aeedcf1 | -3.569 | -50.54708 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ea9c19b-6f0b-3fda-8dca-4a8ecb4cf519 | -3.06529 | -52.50053 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1a04b78-ef1e-3634-9897-f3a2fc2b8dce | -3.03068 | -54.08807 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a33c1283-fc84-37cb-98d2-55d16320d109 | -3.1238 | -51.33216 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f51a4c7-8043-3b02-8d1d-86f4b5495ca7 | -1.23367 | -51.75705 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 292d87e6-5794-39e6-ad67-ed699d2648fc | -1.3907 | -55.4233 | 2024-11-07 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b425480-be0c-3be1-9b46-8d04ab0060c6 | -2.81385 | -52.92937 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4625c16-fe17-3664-8455-d1b8b0803825 | -2.10129 | -46.47256 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| feafc310-f52c-31a0-b752-77871f90d47c | -2.82096 | -52.90786 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b027fb87-7001-3593-94ea-0c33a67cd78a | -2.72956 | -51.71464 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd9985a3-f1a2-3219-a936-f1bbd6a37b56 | -0.26258 | -51.66842 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db43074b-b269-325f-a3cd-72bf8cd744db | -1.16241 | -53.72183 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README46.md)
