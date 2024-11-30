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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 912601dd-8686-38bb-b981-933a8c861b04 | -1.23843 | -51.61905 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19f01465-2098-38e0-828b-ab0c998384c4 | -3.41254 | -50.23981 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9a63488-59bf-3d23-9aa4-7ddc3688663c | -1.86657 | -52.94284 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8578728-e658-3139-9103-4f25a8ea8244 | -1.97209 | -52.89517 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b555c32-7d97-39a4-9945-1acb88e6cdf9 | -2.72707 | -52.57301 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ce352e0-1fa4-31e7-a772-48a829d1f09c | -1.64872 | -53.86937 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5753a22d-611a-3f1b-bc04-a5525e31fd20 | -1.47588 | -55.37944 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 747517d7-23f3-36a6-9152-d322f3cf89fd | -3.30703 | -51.10979 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54cf22bc-96d2-3db2-ae54-8825f5f6b008 | -2.8652 | -53.32219 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8625b5c8-cd9a-314e-8da3-907c1b3aa9cf | -1.16373 | -53.68367 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a91b9b79-39c8-3aee-9791-3726a7ae1a56 | -2.80717 | -55.29994 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2b6841b-df9f-3698-a102-3e15998b6f18 | -1.68966 | -46.79057 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d4373cc9-8f4c-38f3-88d5-166f2a84aed4 | -3.38193 | -50.33441 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25d60546-af55-3b43-9161-418b31b9e7e5 | -2.0278 | -53.49889 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a58d9741-3fd7-32a5-b185-e5062294cd22 | -3.21754 | -54.08734 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12855cd4-dddb-375b-b845-f22c46a3d694 | -3.34586 | -53.305 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9085e544-d47d-331c-9c4d-5ae252a7eda0 | -2.78046 | -52.87885 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8c4e85-5147-3303-ba57-48ccf035d60e | -1.31326 | -51.74119 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54621c38-841e-3f8c-9006-568cc5e3c6df | -1.38217 | -52.56328 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22878730-891d-3f94-80fd-502e77c7504a | -2.76104 | -55.31762 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5df9d92-caca-3e23-90f4-c363dceccf5b | -1.29666 | -51.73036 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 855d1a56-b43f-32a6-9487-acf42d6f8bc8 | -3.11027 | -53.9807 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f115780-f0b8-3f55-b33d-a39dc5a1a419 | -1.41954 | -55.26014 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6526232-8173-307f-8d63-19a8749ac8ac | -0.14009 | -54.59583 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b96d91e2-1189-311d-9e38-fe176ee0f016 | -3.57555 | -53.7546 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1b487c2-e6c9-346e-9822-4154ef9b7827 | -1.00144 | -51.72893 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a5b61851-f826-373f-80ed-7cbaabe74efa | -1.06152 | -53.22015 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5625ead-b57c-3de6-a010-44f4a39f0cf0 | -2.33056 | -50.67232 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b409678d-e554-381a-ac79-0a2bd7848335 | -2.66897 | -53.03735 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f8ee789-c5e7-366e-91e6-5ac503804033 | -3.416 | -50.3241 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f9c542fa-f0c4-3412-82c3-e06b7d341b72 | -3.75245 | -54.73369 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1598a860-501c-33f2-a4af-6d49e0f2ab4b | -2.32779 | -54.50054 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe9b3f7a-1cb8-3815-84c4-e59bc2cb805a | -3.2744 | -53.42879 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4713f7e7-ef30-3a98-94d5-38538a39946e | -3.44131 | -59.28891 | 2024-11-30 05:01:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fac46ea8-b165-32b4-9dca-9b739d34b1fa | -2.21109 | -48.37954 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5be3e4c3-c0fe-3228-ab8c-53a160d86d3c | -2.51642 | -48.46417 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 97ae382f-9f80-318e-bf8b-f9e04c38b74d | -3.27157 | -53.42464 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09492b40-8b9e-3730-bb70-8a16ce39fa81 | -3.4628 | -48.93055 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e13ca7d6-b64f-3714-a17c-656b60c60502 | -4.43593 | -46.00879 | 2024-11-30 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e15defe8-f867-3b41-ada5-6fbcd97c7abf | -3.46325 | -50.53837 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31243119-7c73-3c44-96b2-6d8c605c1b09 | -5.20824 | -47.19345 | 2024-11-30 05:01:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f1264b-6dcc-3c71-bd46-7c234a29b6e2 | -2.90186 | -57.50707 | 2024-11-30 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b360dc13-35a8-3429-b3bf-a74482ac840d | -2.72633 | -54.119 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23389ec8-0ad8-3977-8645-44395ff60e2f | -2.98593 | -53.3516 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe40d727-1adc-3ab5-9c46-19ae84d7ec40 | -1.58344 | -53.85574 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14ae2355-cd93-3980-9ffa-6e689790d48a | -4.11198 | -54.4089 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7bf470b-f631-3e7c-ab1c-c81648f98f30 | -3.22829 | -53.83294 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81147d74-1067-33f5-b708-849f24eb3120 | -2.41778 | -50.47839 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e0eed1b-26b9-3ba5-b135-2b204092e140 | -2.69338 | -51.99614 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3c31a51-1f58-3962-b3c0-5b6ea832ad9f | -2.89973 | -53.05733 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a29c6b6-ff3c-377d-990f-2dff543b900c | -1.19037 | -51.76447 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0da024d8-165c-33f5-a96e-f4e5822f09e5 | -1.44998 | -47.70755 | 2024-11-30 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95aa8a81-8f81-3336-8d4e-d2801620c4e0 | -2.34835 | -53.81277 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ebac0f0-5e42-3930-8f7e-6f7bc3896adc | -2.37742 | -50.40079 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 219135ec-6feb-374b-868a-2a0e15444359 | -2.59646 | -54.23378 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3de1f107-e0fe-337c-8ffb-a77ae9312426 | -0.82264 | -51.60521 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d599127-9f0f-37b1-9a9e-e62221f500b4 | -3.77936 | -49.9815 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f24b137c-d655-3b07-8be3-98bf30530d91 | -1.07268 | -53.64096 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0945774a-8341-37ce-90e0-92b205ca0813 | -1.41344 | -54.80581 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19d050d-e9a1-368a-b33e-f6b34208e517 | -3.18991 | -54.33002 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8ec163e-6fd3-3831-99cc-18ac6e7fcfeb | -1.60206 | -52.29375 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 276467a4-5290-3b18-a035-27627a691fc3 | 0.99498 | -50.27055 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 074b9486-c7ea-324f-a02d-af35810066b7 | -3.27174 | -50.61586 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75e96465-7890-3f61-bbf5-668da4866fb8 | -2.83874 | -54.02527 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39d7064d-aadb-3ee5-aad4-df522b8ae17a | -1.25112 | -54.5478 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d466847-9f09-3dff-bf80-d5190911ad98 | -2.28015 | -46.43107 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1aa8f36-113a-3d51-a7eb-7e14add7ff56 | -2.56941 | -49.09599 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c24fcf2a-c5d9-375f-89cf-a1df5e64d51c | -3.32259 | -54.17536 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19f10dd8-0db0-3bc4-b281-4107e3a98906 | -3.17579 | -53.63876 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9df3ea23-3181-34cd-a8a1-431639bd456b | -3.31508 | -54.09174 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1ff0c38-cfb5-344d-805c-9f744b0f11cc | -3.12248 | -53.25971 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4dd6ef7-4674-3ed8-91ab-68ba3e097ab5 | -2.31421 | -51.95935 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f066711-c6db-3186-88fa-15b967391ce1 | -3.08584 | -53.25084 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 510abf05-7dc2-35f3-b077-963598939cc4 | -2.80646 | -54.03463 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c271ef4e-4ee2-38e3-ba15-d7bb20c14606 | -1.33885 | -52.13296 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e81b6ed-dcff-3bad-8eec-2d6146c81550 | -1.74882 | -47.35382 | 2024-11-30 05:01:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8503c871-9b7b-35c2-b6df-8f7f15faa2ca | -1.2193 | -54.19319 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79c07f77-5017-385c-aac1-784cc8a295aa | -2.58428 | -48.20259 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f52d284e-a870-35cd-a567-1ae28a187c99 | -3.1244 | -46.05145 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a789c0-3355-3c80-aa48-9fe1b24d2cbb | 1.20347 | -55.94103 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca86808-d572-3ce1-a8d8-118aa22c9adb | -1.23487 | -53.36277 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060c7b3a-b3c5-32bd-9ecc-6c54034856bc | -3.12022 | -53.27433 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3250cbf-2f9a-3eff-a38e-07aaee842509 | -0.249 | -51.60795 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 566416e7-85ef-3834-bd7e-b3d78c8ab0f5 | -3.95531 | -50.18906 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a52bbe6b-60a8-37c3-9b34-89981481dc1e | -1.53297 | -51.62276 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc86057-b5db-3684-9864-a331ce9601b2 | -1.69498 | -52.61786 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3c0dddb-2b83-3c4d-a377-e801a2aa5306 | -1.30974 | -52.86599 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b3d84e-d4cd-3563-8aff-c01cd0865094 | -3.30113 | -50.37227 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f87f9dae-087e-3079-aee6-e60a6be22b2f | -3.31116 | -50.28024 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e4428b0-6db7-31a7-b315-c2772c8eb61b | -2.55628 | -54.33763 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e81f69ad-baf8-3d44-8cb2-914334233272 | -3.26995 | -54.10278 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 875829e3-27b4-383e-b86c-ea5b95cc91d1 | -2.42411 | -54.01805 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb33b0c0-4c0c-36c1-89e9-dd91b91ee39a | -3.45253 | -50.03079 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d4b9582-dedd-3430-8872-7098eae4e82c | -2.80865 | -54.02062 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03f8616-e104-3ec7-aa1d-c904c8a8858c | -3.1145 | -53.75686 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6029c35a-a5df-3fb9-974b-f6558a19f0b2 | -5.03965 | -45.24543 | 2024-11-30 05:01:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 347c35e8-ee4f-3090-a081-ba45538b6518 | -2.87867 | -54.1138 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b5d59b7-625a-38c6-bc3a-eb746948ce33 | -1.10139 | -53.39321 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d6066ba-79e6-3111-9b3a-5bb1bda86fb8 | -2.3229 | -53.64613 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c050146-6780-3eb3-93a2-3bf0303a9bb9 | -3.33286 | -53.36649 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README99.md)
