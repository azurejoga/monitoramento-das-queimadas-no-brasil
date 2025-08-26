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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd00e291-2119-37c5-9b63-f2e7a39a5a3b | -7.20939 | -45.31099 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65c2482b-1d82-37e2-8217-67d4065be077 | -7.664 | -42.6627 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ecfc686-89d0-3c77-b353-efa45b83b996 | -5.30907 | -60.2014 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14f55271-898a-3cb7-8249-afa2e7c5e9ba | -8.46559 | -45.84096 | 2025-08-26 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 829e3595-9881-3060-a5b6-b49e358040c3 | -6.92589 | -52.77589 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff53dac-4975-39c7-878a-9735cf6647de | -7.59557 | -45.22802 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 708e9c34-cea5-3308-aaa3-28df39594a80 | -5.466 | -42.60496 | 2025-08-26 04:44:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 134c28b7-bcac-3885-9f16-2b0e21ee3dd6 | -5.47064 | -42.60853 | 2025-08-26 04:44:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90af8134-540f-34e1-ba87-5259805a4885 | -6.94448 | -44.17699 | 2025-08-26 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60eab289-e22e-3b4d-b7ff-1a54f4575116 | -3.69624 | -49.54646 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 256ecc81-bcfd-3f0b-96d4-16546c2826de | -5.30847 | -60.20486 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6620ab2-1193-3326-bc3b-f8be2c99d661 | -8.07524 | -45.01172 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3916b604-4ac5-3245-9321-c8938d8e8bc1 | -6.24608 | -60.02277 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c030941-badb-3141-9ed2-10d96c1955f5 | -5.52242 | -60.21376 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3991d0ef-488d-361c-939a-c4120f87e8aa | -7.74428 | -50.30291 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03f63490-6d92-3154-9c82-75e331ce96ee | -3.65129 | -48.32646 | 2025-08-26 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29192ec-82d0-3228-8672-5e9c958c60fa | -6.86585 | -45.65344 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49101233-d5d6-3be0-bbec-597f2f9c6340 | -3.98639 | -47.88708 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ba289576-db7d-34c5-ade3-e9b29edd49b1 | -5.29769 | -60.20293 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52ab54b1-f479-36d8-818c-e6bf58a250a1 | -6.50609 | -42.94513 | 2025-08-26 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4644f2b0-6df0-3f56-b63c-1a31e7687b42 | -8.07038 | -49.6679 | 2025-08-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b70e0934-bb4f-38d5-9a09-fed317462541 | -7.58556 | -47.49894 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26c3cc23-ae91-367f-ae7f-aca86a6cc33d | -2.97056 | -49.3017 | 2025-08-26 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d70f2f72-ce80-3f6c-bf22-280969389957 | -8.11214 | -47.12881 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 747d0627-3ea9-3c19-a96d-e39cf065abdb | -8.46841 | -43.67119 | 2025-08-26 04:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2041be55-6bd2-3f37-9aeb-0f5c4f0ddb01 | -8.30809 | -47.23998 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da9f1a52-08cd-328d-b966-363c345b7804 | -6.76051 | -42.98803 | 2025-08-26 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d842f9b8-6d29-3c6c-b794-cd3d7628bd72 | -7.73784 | -49.83095 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7319819-b086-363f-ba83-14c0a7352c73 | -5.57065 | -42.62241 | 2025-08-26 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 021c2136-f8cd-3a61-b538-b345bc14730c | -2.29017 | -47.88795 | 2025-08-26 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e41f1fc5-468d-3b84-be20-d6b82100ae94 | -2.4727 | -47.77797 | 2025-08-26 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efaefd3b-5f36-3db4-8ff9-6b489dc558c2 | -3.10543 | -48.59394 | 2025-08-26 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 381c1935-78a2-3857-83a0-fc4821308d83 | -7.46482 | -45.01268 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58e94328-7a31-3f37-9738-3452b83bd0f2 | -5.79874 | -59.21438 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a60d74-30df-3323-971b-889088e08096 | -5.79087 | -46.13873 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9a24766-ca85-3638-902b-4a7edd8f6e7b | -4.48267 | -47.66672 | 2025-08-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce05d73e-3ad5-3f5f-9102-4c2e494a2bd9 | -6.0247 | -44.00191 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b3db535-9ff1-329d-8a52-a32849bd2777 | -5.52779 | -60.21472 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 879526bc-0b9c-3c71-b8b3-bdd7ef64793f | -7.73597 | -51.13767 | 2025-08-26 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 197da451-3c4e-3823-b792-f32042bf8976 | -5.30967 | -60.19795 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ec394aa-4514-3da9-8e2d-440d708a45ac | -5.82733 | -46.35711 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ada0cad-e08d-3aac-b25b-3505c281739b | -4.01824 | -49.50694 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53c271a-a309-32ff-b7ee-76d48911ca5b | -6.20029 | -44.14877 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0ee93d9-14ed-38af-b3d9-3efa3f2e5367 | -4.29065 | -48.26489 | 2025-08-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74884822-e772-3166-a1ab-ca81804c94a0 | -6.8951 | -44.42358 | 2025-08-26 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f8ed43e-128e-3b43-97bd-cb1ae88dfaf5 | -8.15836 | -45.05829 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28273c0e-2387-36d5-84fe-50bfd377d3c5 | -6.40111 | -55.55738 | 2025-08-26 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3fab134-6573-3412-89ff-d284133905a7 | -6.98264 | -46.93165 | 2025-08-26 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33531637-64d6-3cd4-a40c-b9e2674d62f6 | -4.48206 | -47.67082 | 2025-08-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9ded865-b77d-345c-84a6-f2a01ea9f082 | -6.26313 | -60.0159 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da00acb-d6c2-3939-bf46-e18a09b539b2 | -6.69517 | -48.38024 | 2025-08-26 04:44:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15b8e818-3d63-3f9d-a518-2f8fc5c60f42 | -6.89148 | -45.65295 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4efeb24b-eda5-3c24-9f00-9ebfb72ff226 | -3.3908 | -59.45193 | 2025-08-26 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1770fea9-2536-3794-93fd-13ac6b4e4bd4 | -7.21034 | -44.41452 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee3159cb-6a4c-347b-a481-2946c92abc65 | -4.40903 | -40.48806 | 2025-08-26 04:44:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab7802ed-4f90-3a68-962d-bbe91c44632a | -8.2915 | -46.33495 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86f3fa4b-92c0-3d4f-b20c-71a31d742320 | -5.78873 | -46.13624 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de20997c-e1f2-33d4-9ef8-e3ef0b4d6aaf | -4.02775 | -49.53363 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d80c98b-fb52-3f87-9744-97025e4db3a0 | -7.73543 | -51.14114 | 2025-08-26 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a034d859-6c46-3f05-be62-a07eb371149f | -6.38581 | -45.59481 | 2025-08-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e3c9444-43e9-357e-84f7-b46c4d19ad43 | -6.30542 | -59.86953 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4191b95-4690-371b-aa72-29d5602f631b | -6.24312 | -60.00864 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 402e4b40-c3bf-30e7-9baf-2909a30db143 | -6.32022 | -42.88644 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f069374a-c8b3-388f-b26b-6157371c93e3 | -3.42807 | -50.17249 | 2025-08-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeecf367-95a2-340d-bcbc-94aaa114ef76 | -4.95541 | -55.81066 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ceb102b8-8ef4-3c88-9623-44b94af57bc3 | -7.30201 | -44.52419 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4c8d355-251c-3a98-aad8-a63915b980e3 | -6.19989 | -44.15123 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 783db58d-7f28-3d89-a1ae-71b705b282f8 | -8.37826 | -48.01985 | 2025-08-26 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b690b823-bd5d-341d-98b8-dcd9368e3390 | -7.74873 | -50.29635 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbd318ed-f05d-3253-8965-71b44f915c53 | -5.29889 | -60.19605 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 402e6e2b-b2b9-3b99-a3c7-854beda604d1 | -5.79722 | -59.22317 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc4ce6ca-5897-3f2f-a1e6-39fa650470fa | -7.53367 | -50.54196 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7612a319-d381-32f7-b772-aad73a756963 | -6.4007 | -43.52145 | 2025-08-26 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b527594-c361-3a84-a539-f83de6b8908f | -7.82054 | -45.2239 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 997ef02f-6749-32aa-a965-a49cd3cc9629 | -5.5231 | -52.00613 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afda80ff-b848-346b-b910-aafe56a6d7a3 | -4.01489 | -49.50643 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e4036e8-361b-3652-9891-6cc961943937 | -6.8747 | -45.65118 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc65667e-a8e7-38bc-97d0-967f9dec9d18 | -5.86731 | -46.41095 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61805a46-7ab9-389b-b936-4cd53ae0981c | -11.53475 | -50.45426 | 2025-08-26 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0658a087-b8a6-3d7a-bc3b-3720025dedf6 | -8.91101 | -62.41789 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f040e0-ddd1-3fe7-812a-42a4cf16c091 | -9.17731 | -59.52211 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 82889303-90af-3a3f-8fba-4687bf4a4a4d | -11.64255 | -44.86401 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9e09e45-c3a8-36d8-b73a-74c3a273b3f1 | -8.59562 | -62.59039 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15166375-7d15-3bb2-893d-f2de02fd3eed | -6.91421 | -59.36653 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 683a5cb4-f4d5-3628-a4ca-57b553b85ef3 | -10.87253 | -55.79051 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 147cf502-bed6-3db0-9e20-292887676c37 | -15.07281 | -48.6577 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e0e7a64-8e33-3eaf-9f94-4df119102762 | -9.17046 | -59.50433 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9b0a15f-6f41-3487-b54c-ac6ae725c885 | -13.42912 | -46.93267 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6b7e2e5-8aa6-3774-9065-eeeb888fc505 | -11.56911 | -52.11447 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2d6647d5-f124-3a02-9674-71a00ba884bf | -9.23136 | -60.91919 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a63b9aa-d987-374b-8ac6-8ef38fa02e7d | -11.56027 | -52.10584 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e39d50d-8cff-37d9-ae3a-8d00c6695ef6 | -9.19019 | -59.44364 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a53c232-f6fc-36a5-9285-5ea17fda5e30 | -11.54869 | -52.13636 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a5f1898-71c7-38ea-9b47-6bc9f48b869f | -12.74978 | -48.16193 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6d011cb4-0e49-3ca0-8a48-3de4c2df260a | -12.72732 | -48.15384 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e191168-642e-3b7d-b843-75a08f0f2555 | -8.59647 | -62.58599 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6297f309-8386-3fe6-9631-9cbfef6f0dd6 | -12.7382 | -48.16031 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57f83aa0-1da1-395b-a5f6-2bbe26761213 | -13.48884 | -46.87415 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c58e3121-5af4-36c1-a665-98808fe4a82b | -9.27175 | -59.78453 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9e3fd74-a159-30af-acb6-b6b126e60640 | -8.56056 | -62.63186 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README58.md)
