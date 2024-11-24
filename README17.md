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
| 2b3cfd52-fa87-378a-935b-b4f585e86c7f | -3.61284 | -47.51194 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ab7328e9-7082-314d-95c7-3e3834568a42 | -3.98311 | -44.79003 | 2024-11-24 00:49:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b2a1fcb-f8ac-3ab9-a882-7a687a2cf6ff | -2.1503 | -46.74128 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 33686e9e-38f5-36f3-98ff-dc7a139503cd | -2.28563 | -47.30838 | 2024-11-24 00:49:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| aa8fbc88-fc89-3337-9e97-dcb7198a28a0 | -3.2455 | -53.27613 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4875cc09-e564-3c94-a542-2783823a499c | -1.73681 | -52.72226 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 2ad1f4f8-3962-3e43-a7a4-96c39d32c3bb | -2.35155 | -49.04803 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1ae9567-3302-3085-94ee-65a680b18fd4 | -4.08361 | -50.36255 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| fac4be0d-da84-3f73-9be2-c46ed580edeb | -4.19393 | -45.3539 | 2024-11-24 00:49:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a2364eae-1a50-3518-994b-57dde8dacfc4 | -2.21783 | -48.41695 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d132707-83e2-34d7-8d2d-da2cde8d7a95 | -4.24649 | -48.7024 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| f3a1b6ab-f1ec-35b6-a364-5f8712c954cc | -3.24259 | -45.54216 | 2024-11-24 00:49:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96965776-949a-3a5f-a927-693be47509ec | -2.58571 | -51.88718 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2174d4b1-ec25-3192-8794-ac58f54dd574 | -3.2822 | -50.04494 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 72859179-8c94-3adb-ab62-ff8ab6e7da9a | -3.8454 | -46.01842 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 9cac3376-a9f0-3428-b612-26b62419eb2c | -3.07361 | -45.96739 | 2024-11-24 00:49:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5bf78fbd-1ecc-328a-9f46-11ed95403aef | -2.07051 | -48.94643 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c2387191-b9c0-36c3-b6c1-be96726fd1f7 | -2.22 | -47.77026 | 2024-11-24 00:49:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cba30c99-4834-39e6-ba1c-efd694ae50ce | -2.7657 | -45.94298 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b7ba24db-82f6-3bd2-951a-12f87300a2f0 | -3.67968 | -47.1368 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4884534d-9bfb-3977-92ed-eadf2e2bedbf | -2.6551 | -46.13499 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b28f8055-298f-3227-a9e1-a621fbf8b0d2 | -0.57352 | -51.72722 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 130ef7ec-dcc6-3ad6-8ff6-15e0d0febc93 | -4.24539 | -48.62694 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bccf0545-c3c3-363a-8b57-f3dcc70db881 | -2.13373 | -46.62309 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fb679bdd-16fb-3686-b3aa-52c0006a613d | -3.44341 | -50.02113 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 60643218-7c35-3f70-9b85-86fbb29f32a8 | -2.72007 | -46.2717 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 81f3d999-d47f-3953-a69d-a23c80f2118d | -3.08202 | -49.19955 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| f6178a27-7e7a-3a42-9e2c-01c3a51ab090 | -2.74116 | -47.54346 | 2024-11-24 00:49:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f7cf267-19c8-34f3-93c3-7a307651a398 | -0.37602 | -51.55898 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f8762985-5fe2-38bf-8592-ee0da077955f | -3.98262 | -47.72976 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02f088ac-b636-375f-877a-c7762a129ba3 | -3.52741 | -53.51514 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 2744b34f-6702-35be-b5aa-511cc154ed93 | -4.42864 | -47.69023 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c48ace92-7c86-3f06-b56d-dd55f82fd426 | -3.67936 | -50.08858 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ffad7b39-4a41-3f98-b9bd-d4cb5da7b624 | -4.0467 | -48.32189 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ecd378b0-4adf-3e27-9eb8-445ae02c35d6 | -2.6861 | -46.16257 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 71a54b08-f1a6-3202-8fac-933ecf442390 | -4.40476 | -49.65247 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e2df4379-c3d9-3203-b256-a9056a6f3e0a | -2.44868 | -49.08529 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4c1acbb6-72a4-31a9-ac44-abdb861a5523 | -3.70817 | -47.60045 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd3ce7b5-3db5-32ce-abb9-989c7ca90879 | -1.37394 | -53.84184 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8b7e8466-9f46-3203-9e0f-a2dcac2d2422 | -2.39944 | -49.0602 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9cb9c73-2e2b-3ec3-b07c-0c3ce207cbab | -3.15972 | -45.53992 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3f943cbf-83f6-335c-a44e-d9ce5d597dab | -0.19228 | -51.48936 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 096f9459-ffac-358b-a61b-a5f8dd09d3fd | -3.60277 | -47.50438 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ddaf9b60-9eb9-3288-8ed4-5ba435aa5b39 | -3.2561 | -52.85596 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f6300f26-0a2c-3494-a4c2-38eb799ae026 | -3.68607 | -47.11787 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f4ac7892-7a8e-3141-bef8-c0f601660d1a | -1.27724 | -47.87448 | 2024-11-24 00:49:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ae5e9e04-6c33-32ea-87f4-9e2b8c9da8ef | -3.00382 | -52.50777 | 2024-11-24 00:49:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2008eabe-22b9-3867-9da0-1c5273526eb0 | -2.47537 | -47.08845 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 582241cb-2199-3241-a40d-488a59fa05a7 | -2.59809 | -46.25755 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9c6db9fa-0444-30a3-b782-d0beae08a7f0 | -2.95736 | -45.79581 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 232d7b41-bbe5-3330-9753-c06ce1be6dff | -3.95302 | -46.00034 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 01c1f28c-10f9-3fda-801a-4c2c431c4ed5 | -2.36685 | -49.83282 | 2024-11-24 00:49:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f19b1cd5-d013-3e54-bee9-d50739f9fa35 | -3.06955 | -50.94842 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 0b849256-4d82-3524-a74d-6f27cd3c1d06 | -4.36433 | -48.08733 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45e31c5f-4118-3232-ab81-ac78f160eed8 | -0.04626 | -50.81165 | 2024-11-24 00:49:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 995039ac-9c3c-3221-a804-9d9ce502230d | -1.5184 | -51.629 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9a18fd70-720e-3a85-9be4-17fe2bfce76b | -3.54688 | -51.52681 | 2024-11-24 00:49:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bdf7149f-214e-367e-b745-b785fa3810ff | -3.15832 | -45.5301 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 578555c8-8da3-3c51-b720-64e32217bff6 | -2.70838 | -46.2544 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7cb31bd2-348d-3e3d-96e3-d69795c3e07e | -1.47045 | -46.03678 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| bef161b2-9d85-3517-b6f7-0ff6e4147daf | -3.22991 | -53.93043 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 80af1de8-cd61-36ae-adc1-94da79e25c35 | -2.65777 | -46.61413 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9cd1c68-ecd8-33d1-8416-c2779711af8f | -3.80677 | -46.59839 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 53738b6e-9c8b-3b8f-98df-9f8bc7ac97cd | -3.86785 | -48.95761 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a0cd0ac-7041-3b80-9722-63b471ee0603 | -4.59854 | -44.72243 | 2024-11-24 00:49:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e5a3bb4b-798f-31db-8e8e-740c4327558f | -2.71231 | -46.28226 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 9686fecb-cebf-3181-9972-c617bf8f468e | -3.98188 | -47.91982 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f267320-e593-3061-b80d-de28f71f9f00 | -2.74954 | -49.12949 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a876f7fe-5f35-3757-93ee-a69644089100 | -3.46765 | -45.69575 | 2024-11-24 00:49:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9828e88c-8103-392e-8321-73af03b1beb4 | -4.84829 | -50.80722 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 08af22a5-907e-3985-a68c-529ffebb5dbb | -2.79592 | -51.68406 | 2024-11-24 00:49:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 02022f33-fea3-365c-9a9a-b7f7dabe6288 | -3.10208 | -45.78263 | 2024-11-24 00:49:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 5629021b-8d55-397d-9cba-2cd4dd0193dc | -2.24344 | -46.87825 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ca88e46-00a9-397c-9b47-858257372e09 | -2.64366 | -46.57907 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3a457590-f788-30a6-ae73-4943c1418427 | -4.40616 | -49.6627 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c35e54ee-5cee-36d8-9549-15423588beb5 | -2.57612 | -45.63657 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 27ecebad-e6b3-3bd5-828f-5671b8f5ae14 | -2.70706 | -46.24512 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 32c64fee-757c-3cf8-90db-fa20fa28343b | -2.45763 | -49.15054 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fe733079-7177-3751-b448-c7a5014c3153 | -2.72138 | -46.28098 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d87f4338-011f-3a5f-9c36-cba04ae02d58 | -1.35646 | -53.83224 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e479fe61-f24e-312e-9fe9-d30809f54744 | -4.53786 | -46.42681 | 2024-11-24 00:49:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9436e8d-ec59-3d72-9b80-ee323cfea4b1 | -3.64464 | -50.21882 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8e1f35b9-d6f8-3404-9d13-ea57b9353fa2 | -2.35028 | -49.03878 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| acbb3195-59c0-3683-bf83-35dbb7ad4de9 | -3.28258 | -53.83642 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 48f61d81-2e25-3808-8426-a12921b633d0 | 0.08357 | -51.49315 | 2024-11-24 00:49:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fdd6ce77-e535-34e7-8058-069783c19fd5 | -3.53748 | -50.78164 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e3c5e0d-d130-321d-b42c-327dd6b41537 | -3.07285 | -49.20084 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 342eb876-1d50-330c-938f-e69781e6813d | -1.73702 | -52.04606 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 102784c7-31cf-346c-a2f3-7d860acdd16a | -2.21169 | -46.38995 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 67a3584a-da9f-3a8a-b4d5-f155247d708c | -3.10746 | -53.99318 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f334cafe-077e-3e4e-9cfa-fe5ebbb1afe6 | -3.80803 | -46.60742 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a93f322e-4d9e-3d61-b491-6d2151065b46 | -1.60404 | -52.59521 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6839dab7-e620-3679-9021-e6f63bae66e8 | -4.11802 | -49.5039 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 82e766e6-d254-30d0-8485-f0a4cc4e3c10 | -3.85576 | -50.05765 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 89496812-3d28-3a1c-a01c-4cd1549d9a99 | -1.81192 | -46.62774 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 8d96984f-e79a-37bc-9080-30b48e515f84 | -4.01005 | -44.33859 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70d93bce-ba5b-3550-94ac-ea4d403a480a | -4.18613 | -45.63158 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 93c24c92-f193-3aca-97ca-ba62fe110600 | -1.79339 | -45.71653 | 2024-11-24 00:49:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fc19d0f3-209f-364c-825c-8581b8f2d109 | -2.5914 | -54.22831 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 585d017d-3ea0-3a46-ad5c-f4c1efe645aa | -4.62342 | -46.05015 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README18.md)
