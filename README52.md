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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87695871-6cd8-3d19-9ffb-610b23124029 | -2.30612 | -53.60411 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ddc5009-5834-3bdf-b3ba-bb335e8a416f | -3.28466 | -53.84359 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64b6ef7e-81d6-334a-a310-17f1df5f15ad | -3.51473 | -53.8118 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fad9154-a2cd-3f9d-848f-fbe7ee2df130 | -4.38051 | -50.49472 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c566bd6-8c5f-3dad-8e6e-8642ede269ea | -2.08911 | -50.33083 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6b04f6b-8307-351a-8d41-cdb3e91122cd | -2.91109 | -53.06524 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d8ab582-49e9-3f45-8626-611974421b8c | -3.25687 | -48.89397 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cd7e54d-ab01-389a-9f51-7bb42644141e | -3.42706 | -50.98422 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6c83bd8-6950-3149-a563-ef80604fe9b0 | -2.86049 | -53.96328 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7eb000-64b1-3b2d-8fcc-a1fea7ae0b9a | -2.88169 | -53.96287 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3add7de-5010-3068-a5cc-d679c6e6536a | -2.20858 | -49.86931 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f17c1f3a-6eb2-3cfe-8279-85501224a15e | -0.02439 | -51.19513 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a47add68-8aab-3cdc-8f6a-344ae0ce8d1b | -2.67913 | -46.08767 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6e4669-9f90-3550-b367-8d835e9ab95e | -1.11389 | -53.39572 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 161251ea-3760-373f-8b80-e856678e8008 | -1.33777 | -52.24494 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c6326e8-4293-3e33-ba1f-c3d9988d527b | -3.38166 | -52.45636 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30b839ba-579e-3b92-9a87-274a54f9894b | -3.58819 | -55.45308 | 2024-11-22 04:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f36a01d6-3255-319f-a787-76c46c79091b | -2.2822 | -46.56107 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a80d259-3aa3-3d2e-b130-ef4c51fb5324 | -2.84834 | -53.96889 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6d7b3ce-5ec4-3769-a6f8-b29b3abfdf5a | 0.46598 | -51.34192 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d92ede5-f9d6-3b22-b232-16706835a530 | -2.70895 | -46.08751 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92964e04-f186-3076-86f1-6e6db0e925da | -3.83319 | -52.25441 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 821911dc-e8a0-3a62-a329-07ff27483e1c | -2.69497 | -46.08537 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71779c68-7368-3b38-96bd-e965a23445cf | -0.93392 | -51.71896 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 755a3cbb-510f-327a-91ab-826090baf5c1 | -1.28718 | -52.46543 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6fe37c9f-388c-3a3e-9f71-fea2e1bdbc15 | -2.25017 | -50.46498 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db09cd23-19f5-3911-abe5-12fa133f529d | -2.6496 | -47.12971 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c95c2cb-39ba-3094-9d55-a5596a68c0cf | -3.66354 | -51.57388 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e47efe1f-a95d-3943-9f34-b11415c673be | -4.4397 | -50.69755 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1cc7625-b25e-35bd-8699-c106a8b27458 | -1.51527 | -52.08377 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 074d5c14-9066-3fd0-abbb-fb6bbb41c36f | -3.33817 | -51.16261 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89a080de-7d87-352a-9e94-3334cba48864 | -0.30617 | -51.54628 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fac126f0-ab22-3f02-a18a-d1215ea9c6f8 | -2.51745 | -48.34474 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6c5d038-b44f-33b3-aac3-7de4c7a1896f | -2.18659 | -53.67291 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb48f31-9900-36b6-a2b9-d4b3851935d6 | -2.24958 | -50.46869 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77305b17-cdf5-3dc3-9655-a4db2928eca5 | -2.52361 | -46.40311 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd502d5a-2533-335b-89f7-deb19dfaa321 | -3.17822 | -46.54285 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deb1808b-acdd-39ca-8ae8-992c7f350f35 | -1.78241 | -53.62111 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68979b2e-81af-3116-a9ea-def93030a35a | -2.55932 | -48.1646 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f15264a-e6d3-3e3d-a258-217a760eaa53 | -3.24511 | -54.23501 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eaa1b7c7-c909-308a-ab78-884aa069a1fd | -1.77025 | -48.64658 | 2024-11-22 04:36:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ce445a8-534f-344c-ad18-52dce0413131 | -3.29079 | -49.19566 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| caf27b68-e1c1-3822-b043-7a5f48e243cd | -2.64448 | -46.52834 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e31cf2-805e-33b7-9cee-2354527618c0 | -1.58949 | -53.80629 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2fb4abaa-a4c0-358c-ab56-e7e78e480042 | -2.27392 | -51.13432 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f414101-a3ae-34a9-9123-3e2b1a87a79b | -2.69333 | -46.25811 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 297cb30e-500b-32ec-ba9b-1d661c00bfe8 | -1.20174 | -51.78018 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aadf1ccf-cde8-3ffb-a842-347bb3ddd5ca | -1.62447 | -52.61439 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a7189cb-e7e6-3425-8ccb-bfe658ee5dc3 | -3.22572 | -54.24004 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2e7a5043-98f1-3bbe-96a0-0a8d5979c7af | -3.79328 | -46.66458 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d105eea8-f3e3-3710-8074-b0b09b8e9675 | -3.52104 | -53.79818 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4259e765-6496-35c6-9af7-fc74468b77f5 | -4.13796 | -54.65635 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aced856-e89f-38fd-aae0-fa93107dd355 | -3.25756 | -46.53193 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c3c090-c2fd-3d1c-9a65-07f37071eaea | -4.40297 | -44.12268 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63595177-b8bc-3e88-bd2d-fc6a0c0ee731 | -4.24315 | -49.08049 | 2024-11-22 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a957c1c-905c-32f8-992a-46344c63d30e | -3.31536 | -54.09211 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 530cb7a3-61f4-3619-b45e-bf26d3299632 | -3.23886 | -54.23815 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1e2ca42d-da7e-3289-a0f6-839cae444869 | -1.61753 | -52.6084 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 173143f3-f153-36af-a9e7-db12ecadc045 | -2.39382 | -49.00134 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f9d2927-66b1-399c-abba-c9e541b72255 | -0.81377 | -51.79135 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c0699703-232d-39d6-a9ce-49c0988acc80 | -2.12366 | -47.67216 | 2024-11-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82ed88f1-d4a6-3b71-bc93-55b3abb0ca69 | -1.78061 | -47.1061 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a0ff67c-3111-3e91-a170-6e9748241b67 | -3.10154 | -53.74094 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41839c12-505c-35b0-af67-b199ae60bd24 | -3.29523 | -53.85656 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96ec15ab-c0c7-3724-ba26-1a4e885ebd19 | -2.84187 | -46.67897 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7488c2b-fe5f-3fc8-b8be-6f159a53f423 | -3.06967 | -51.25692 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d7e4f49-748a-3ed0-9303-993d3b7a16d9 | -4.57236 | -48.01926 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cac796f8-da30-3de1-b5c9-5c5fe7dec210 | -4.29025 | -48.2402 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6bfd886-e9c8-3f0c-9963-ce3ef80af164 | -1.21364 | -51.97113 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 988b83d2-9d06-37fa-b186-444a7bf1ebda | -4.30341 | -50.74016 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e28c0ebc-f033-377e-a43d-b2ef7429d39f | -2.23345 | -50.08328 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b093f94d-e42b-399f-9362-bb1abd77fa23 | -5.00891 | -41.95958 | 2024-11-22 04:36:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ae449f28-a489-3532-ba84-3f76e21dc539 | -2.34109 | -48.79578 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 700e5922-e41b-35dd-8755-82231e2f1394 | -12.18665 | -41.3527 | 2024-11-22 04:38:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ccab1148-3aee-3239-9e66-c40417b3a58b | -10.66126 | -48.11166 | 2024-11-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4a155a1-7467-3a24-bb84-9f7449e5ba46 | -8.71884 | -44.01738 | 2024-11-22 04:38:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dace885c-a236-3a1a-93ef-4335515cd0e7 | -11.36645 | -57.57461 | 2024-11-22 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e1c82c6-e3bd-3fe3-8e75-db42138b59de | -13.25828 | -50.8942 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 541d11a1-5495-3e25-a1e5-ef61d54036e7 | -6.91937 | -46.11276 | 2024-11-22 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9709469b-1bfe-396a-87a2-7d68aadfdcfd | -7.28601 | -45.0819 | 2024-11-22 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09364adc-af64-3071-87cf-24c3780d9eb0 | -7.73738 | -38.61445 | 2024-11-22 04:38:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 13bdb0bc-f709-39b4-83e8-acb0e4c630bd | -12.00758 | -47.46312 | 2024-11-22 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 758193e0-138c-3b43-8800-981618940fd7 | -13.10867 | -50.1111 | 2024-11-22 04:38:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0193712d-7b59-39a8-a5b9-20c98043cc3b | -8.39548 | -48.05405 | 2024-11-22 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 533bee24-a3b6-3790-a9ae-7af754adeb5b | -10.84763 | -48.96609 | 2024-11-22 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0296c10-3cdf-3a2a-aff3-c7a5e82d500b | -12.33778 | -50.00303 | 2024-11-22 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4774c053-c6b4-38ba-aa06-a6db50a5432e | -7.73848 | -38.61771 | 2024-11-22 04:38:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 725030f7-92c4-3a47-9574-cc55b1de33fd | -8.39491 | -48.05777 | 2024-11-22 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f863b6a-87f9-33d3-b443-19c7b9fb1d86 | -7.2141 | -45.07873 | 2024-11-22 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fed75bc9-659e-3a30-b135-0237d5cb1e81 | -12.25626 | -52.67117 | 2024-11-22 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a4bb323-119e-366d-8591-b90bc278ca69 | -10.87247 | -51.94484 | 2024-11-22 04:38:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d97b2d1-ea83-3287-b34a-ad43e2a3db7e | -11.65983 | -49.75808 | 2024-11-22 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36d8bf47-7b9b-3307-9808-cde97fb0a985 | -9.99301 | -44.7334 | 2024-11-22 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32190544-42a4-3f79-906b-8ed4c71f05b1 | -13.25442 | -50.89719 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 42957c71-6e97-3542-8e1f-d70f0bd1047f | -12.44127 | -46.6642 | 2024-11-22 04:38:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f72de7f-ce8c-3c03-948a-ef1d6f2122b4 | -10.65837 | -48.1073 | 2024-11-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 288ba999-7f3b-35b5-87bf-c6d9506b236c | -13.25277 | -50.88605 | 2024-11-22 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a5319e3-5526-31f2-8037-4eb97c83fbc6 | -11.86386 | -52.34536 | 2024-11-22 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24afbc40-8feb-383e-b696-6afd5435288a | -10.66183 | -48.10782 | 2024-11-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c65ee04-36db-37d6-973f-1fce602d1ca2 | -9.2959 | -43.12882 | 2024-11-22 04:38:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
