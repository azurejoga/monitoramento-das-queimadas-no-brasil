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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796e10a6-31e3-3090-9861-b3b06a83fe3c | -1.5862 | -53.8514 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bde77881-41ce-31b2-9f92-b9e653587d49 | -1.35183 | -54.63214 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98630122-6ea1-3550-b2fb-9625be16c9dc | -3.39576 | -50.31406 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b3acc5ab-fe53-3f8f-a7e4-43ffad0b4a22 | -2.98603 | -49.58875 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5271520f-ffa9-3f51-9e1b-3c0854ed61a1 | -1.03924 | -51.73561 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 174eea30-7727-38a1-aed2-3b26bede55c8 | -2.55076 | -47.9744 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d41596-bc37-31a7-b364-f6233bd25747 | -3.99716 | -53.92286 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9aaa88b-80f9-37d1-aca8-c43818eaea90 | -3.34722 | -50.23685 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae22798c-6e83-3eae-997c-911dcbfb9e33 | -3.02499 | -52.3847 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71644d9f-20a4-3469-b5f3-9e0e9a4cc55d | -3.33614 | -53.36065 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39ecb638-914d-358c-a047-f487d9c02b64 | -3.13778 | -48.53021 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05805bc0-1f37-3fea-a1e3-b2b7c96621c7 | -3.10061 | -50.35561 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 857924a2-33f0-380f-8a03-f7a251333c24 | -3.25773 | -53.86826 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16945f89-1e42-3a20-9401-dd957d2712fb | -4.01776 | -49.01702 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d05bc759-f474-338d-9b52-2feae9a59bd4 | -3.77244 | -46.69139 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b598d176-0612-37ca-81a5-18fcb288a571 | -4.8668 | -44.00705 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8248089a-303b-3b85-87ea-02eb6d538e5d | -1.42573 | -55.27776 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 824edc46-890b-3de4-b77f-66ff8770139b | -3.81997 | -46.59171 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7363da21-694c-3636-920e-a7e251353f18 | -2.19528 | -48.40066 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 596d1460-6111-3497-844c-ff6abc5ec654 | -0.94992 | -51.65884 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92542c87-09ec-3709-a038-4890e4433236 | -1.33412 | -51.40161 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94f7b20e-d711-3da8-b2e2-4671cb7b0dd1 | -3.86715 | -52.39473 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98a6de33-06cd-3ade-ae34-23e4f26e22e1 | -3.41644 | -50.16129 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce169b14-7c15-3af8-a839-dae96bd5ab19 | -2.79783 | -54.05097 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1c9f5f4-6519-3f5e-a016-a708d1c0b1ff | -2.00634 | -48.0856 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0451e04-fdcb-31d0-bc31-ddd50874a6a2 | -2.41021 | -46.76786 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9357752d-fefd-3d1e-a65e-5f2d00efa218 | -1.71832 | -52.77868 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6cc39e7c-ab63-37c9-8220-d89b1de82330 | -1.77271 | -46.12589 | 2024-11-30 04:40:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83300414-769a-3184-84ef-74532405c2c4 | -2.59719 | -53.97457 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0f1b6a2-1ef8-3936-be83-352aa97b0b4e | -2.33167 | -50.67166 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 209751e2-f247-3e97-8a61-8e4895e4340d | -2.72019 | -48.65525 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c4a6fa0-c2d2-3dfc-81ee-429051bd194e | -1.45325 | -52.61499 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d24d64e-685c-3046-85ea-4ffa5aaeafca | -3.99113 | -41.51911 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 80dee6ac-e253-3d5d-bf88-477be1840300 | -3.83842 | -46.52554 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c8f5e9a-e2fc-3498-80dc-306d98dd8414 | -4.40644 | -47.2674 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17fb8e45-80eb-38e1-b2cc-71054410b38b | -3.7294 | -54.22983 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0212005-326a-31d7-8f95-c2926b58e4ef | -6.7023 | -47.26604 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed667bad-d5e7-3cc9-97d5-17576c12fa6a | -2.18309 | -50.58837 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4785ea43-8d19-34e7-9ed0-7fcffa454b4b | -3.95141 | -48.17324 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 273f3995-8d25-3c31-a438-d10e23f737dc | -3.97355 | -46.65762 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afa8131b-bdff-359b-9395-fe17eb91f406 | -3.07841 | -53.91346 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb5c087c-4a4b-31ae-b75f-94fbc0c9aade | -1.0966 | -53.38227 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24a52ad4-32fb-31c0-96fe-c71b694f7f3a | -1.42421 | -54.94683 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b91f9d06-a088-3be7-95a9-fc50a811211b | -4.59351 | -44.70369 | 2024-11-30 04:40:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7997908-cb50-3306-978b-5f27f9fe01e5 | -2.52244 | -48.46225 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 112ea461-cfe5-3242-8f96-005c1ff90c57 | -3.86143 | -50.16583 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50217d19-c2db-3d65-bfdc-b8a07e175caa | -2.23679 | -46.43412 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c90ce42e-bbbf-33d5-9d7f-9509bc78fd9e | -3.82019 | -46.544 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 271e398e-1ef5-3e7f-8e84-6333af27b351 | -2.36352 | -50.51507 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a52b2a9-f720-3ce7-9b17-a93d7dd74581 | -3.88648 | -46.68027 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2630142-45c8-3f27-bf4b-ebf02be5207f | -2.54594 | -47.34523 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93651ce2-4d65-30f7-841a-dbf678f63f4b | -2.78549 | -51.71483 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a21dc5f0-3797-3757-97b4-73126ef9ec9a | -2.91737 | -48.59132 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c4f3c7f-0963-3767-aabb-f6dd2887385a | -1.82131 | -50.90388 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ebc4b522-c1c5-3d7b-99c0-1ee08bc36a07 | -2.60067 | -53.97878 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d71bb49-473f-3aba-82de-c8335363ccc5 | -3.04081 | -48.51879 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb68ca31-7c76-38ca-b179-e765b2b0b105 | -3.91081 | -47.20508 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 403c25ed-8748-3f5c-ac30-9ededa2d8c3b | -3.97041 | -41.52638 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6123e8d6-bdea-379e-8673-43dfa212628d | -3.4668 | -50.3796 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 141cce24-c4c1-34d3-aded-56c210c84fd2 | -3.19406 | -46.57098 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 213c8bbf-63b0-3648-8711-9dd8200cc747 | -3.24001 | -53.92662 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 84ad0c59-299f-34b4-a68e-9c569fc4903a | -4.41103 | -50.82134 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39829eb1-9a77-35cf-8701-7943881a696b | -1.72276 | -52.48354 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1acf2a4-67e5-3e88-bb45-1e64611443ee | -2.75877 | -54.08554 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40405b6f-a389-35b0-999a-cdb0ee977a72 | -3.48138 | -53.80414 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 819690e5-83f9-31f6-9197-f5d31ccd5809 | -3.96665 | -46.91128 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a1b4800-2a4f-3ad6-85d4-5d30769f38dc | -2.73047 | -53.19561 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d232a15-d0ba-32ab-a035-caeed790f90f | -2.88854 | -54.16153 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09439294-222c-307d-b8ae-54b5b2303eda | -3.04966 | -48.52721 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 126f6b64-d711-3ff6-8425-8dc326f23576 | -5.04239 | -45.25006 | 2024-11-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7922d506-7c08-3f16-b41f-cb3bad8cf715 | -1.09102 | -53.39178 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 490db477-0927-3cc8-9099-b011db9dfaa4 | -2.16288 | -48.5434 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd745cb0-b37c-3ee8-a981-ad70c2414740 | -1.61079 | -47.173 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bac52e10-c613-3346-8a56-ee68b77d8b62 | -3.37002 | -50.17879 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 733519f1-9be5-3130-a93c-d119bb78e972 | -3.06937 | -54.41083 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11bd7e1c-480b-367e-b095-ee212cdefda9 | -2.01257 | -46.5018 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d36bf13-1f02-3697-a541-f4789a0706a7 | -3.78942 | -58.97959 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 232cd590-6569-30c5-92f3-7be15f3ffd3a | -2.29699 | -50.6894 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43af9072-f801-315a-9754-1ce8bfa2a3ab | -1.33134 | -52.18848 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79010255-cd6a-3ebb-a89f-c6e524c28c6b | -2.26784 | -51.91296 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e844d453-4b6a-3b97-ab84-ee81b794edb4 | -3.40903 | -50.98488 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3f99e96-deab-3a2b-9cf9-6d4568d868fa | -3.14055 | -48.53417 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2be9d158-ff5b-3e09-b85a-e2829641a0f9 | -3.72908 | -50.20657 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12b6580e-1cb8-3ac1-8426-67951417fb0e | -2.59949 | -46.5659 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edda0256-4612-3832-98a3-eb10255144f9 | -3.05404 | -48.52083 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef1d51bd-8a03-3cad-8bc8-52dbe35d7388 | -3.55835 | -42.16569 | 2024-11-30 04:40:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b2970dee-064e-30d5-ba00-4b58111c6412 | -2.01573 | -52.08297 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6039507b-b72a-3898-82da-98c7ccaeb0ee | -3.93574 | -48.14215 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28a61eb0-3200-345b-854a-396684ee86bf | -2.46486 | -50.37838 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 795ee20b-98ee-31f0-bc68-e13cf63a2d36 | -3.59208 | -50.36251 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3725db7d-a35d-3e0b-bd61-0f128ae4088e | -3.96319 | -46.91079 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 225be94c-e713-396d-9e5e-690a2ee0c2ea | -4.04372 | -46.86397 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8656fdd8-6e14-3991-a9ed-03e2250263a3 | -4.43958 | -46.59297 | 2024-11-30 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44c78e27-fd42-3688-bf07-9a67df52d399 | -3.98675 | -49.389 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bddee12a-1645-31aa-9f56-8e4dfc73581d | -1.32071 | -51.73724 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5255fe11-6d5d-3bef-b85a-82831bf33d54 | -2.78344 | -49.21086 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14cb8ca9-7d11-3e36-aa56-14b0869343cd | -3.46992 | -50.53411 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62714f57-3d53-3e31-b443-f562621d4731 | -1.17946 | -53.88737 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 437d937a-e916-37f8-9386-15f1a44f90cc | -2.22676 | -46.39377 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8ada6b-aacc-347d-b1bd-fbd352795e89 | -1.66454 | -52.40757 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README73.md)
