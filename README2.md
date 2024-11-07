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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a20ce4cc-a978-3ab9-921f-0fbd71630fb1 | -1.2014 | -53.8983 | 2024-11-07 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8673ce22-6442-34e5-abf9-86cf591a4e80 | -3.7033 | -48.9986 | 2024-11-07 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 789c68a0-8fc3-3780-9d07-6ea40a9170f1 | -3.9854 | -48.1708 | 2024-11-07 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 4378eb29-b627-31e5-b056-97ba5e6bbaed | -17.7058 | -57.498 | 2024-11-07 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 60d14faf-dba8-339b-b722-b850e721de68 | -10.9961 | -49.0191 | 2024-11-07 00:10:00 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 303e9d12-fd96-3cb6-a897-ed80c1bd4710 | -5.0342 | -46.83 | 2024-11-07 00:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 7682fb03-5a32-3114-b5ca-3819ccf011d2 | -2.7639 | -53.2265 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e144f8e6-f636-3837-b99d-62aec6cfe7ae | -2.8536 | -48.6856 | 2024-11-07 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 46845508-a594-3712-acbc-132362ff3b37 | -5.1397 | -47.679 | 2024-11-07 00:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0b8ec886-c981-32e5-8d94-85194301e7d6 | -2.4048 | -50.3085 | 2024-11-07 00:10:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 5f9fb367-bd53-316e-a6c3-236c8303f21b | -4.4596 | -46.508 | 2024-11-07 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 68f18c84-4bc9-37ab-b98f-388bbd616d7e | -5.0526 | -46.851 | 2024-11-07 00:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e54d8a14-bc37-35e3-8c80-bf7abe183d9b | -4.6653 | -46.3418 | 2024-11-07 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 02e906c0-b264-39c7-8a19-ecfedeb60375 | -3.9485 | -48.1508 | 2024-11-07 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ee07d32f-1c80-3e9f-b785-b2bd35a6abfe | -3.7218 | -48.9979 | 2024-11-07 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e651a986-b589-332f-8fdb-68f713fba4f5 | -5.9975 | -45.3607 | 2024-11-07 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 728610d8-1c38-3511-8638-97a0db687767 | -9.876 | -36.1077 | 2024-11-07 00:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 160.2 |
| 6b5f4384-2ac4-353a-a722-db90f0ca0257 | -3.4564 | -50.3832 | 2024-11-07 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 29098b3a-842a-3db2-b0ed-7540eb557daf | -2.7939 | -45.128 | 2024-11-07 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 2bd8b9d4-634f-3be0-a26b-cd358c08d1b4 | -9.8567 | -36.1111 | 2024-11-07 00:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| c0761713-f8cd-307f-9de4-2164c9a53105 | -3.0413 | -48.0339 | 2024-11-07 00:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3c21139b-357a-3e72-ab8f-f7b9dbc3d061 | -2.6645 | -49.8603 | 2024-11-07 00:10:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 74d71480-9814-3407-ae7b-f3653b90915d | -5.1581 | -47.6997 | 2024-11-07 00:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1d33adfa-d859-324e-b62e-a485f6c95b58 | -2.82 | -52.9409 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 196.8 |
| a9026621-7222-383c-8c4b-38984f3b2743 | -17.293 | -57.5062 | 2024-11-07 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 55b0c158-bdb7-342c-93f6-1e1fd03fe5f5 | -8.0313 | -49.6341 | 2024-11-07 00:10:00 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f01178f1-3319-3de9-a77b-4138f97933c6 | -2.7753 | -45.1287 | 2024-11-07 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d691d528-7f44-3880-bcaa-e372075bb866 | -4.6655 | -46.3196 | 2024-11-07 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6ee041ef-3ada-3dfd-a66f-508b381ec4e7 | -3.967 | -48.15 | 2024-11-07 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4d7d6f8b-c6dd-3f8e-8354-28f6c35b6fb0 | -3.1616 | -50.2248 | 2024-11-07 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b2ee2dad-4ab5-37e5-8c6d-1a608da83131 | -5.9788 | -45.3621 | 2024-11-07 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 3949a4cd-470d-37ac-8b15-f496ce421db7 | -2.82 | -52.9613 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| c42f9e98-3271-33a1-bda5-c3e980e24d32 | -1.1283 | -53.7179 | 2024-11-07 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2fdabe3e-7bcf-3de0-b3e1-ad7dc35d7a7c | -5.0154 | -46.8531 | 2024-11-07 00:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b91f8796-6fbc-326b-b4d3-84ee1ef3624a | -2.8352 | -48.6648 | 2024-11-07 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9ce005ff-92da-3f50-9415-462304f455ba | -3.9854 | -48.1708 | 2024-11-07 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b5286cb7-6b75-3acb-ad19-d600ae3d9b7a | -3.7033 | -48.9986 | 2024-11-07 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 409e4ffe-b319-38a2-8930-62a54ee2fe50 | -3.6602 | -50.2501 | 2024-11-07 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 77b2bbce-e7f7-33ea-a8e5-79677d092838 | -5.0342 | -46.83 | 2024-11-07 00:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 123.4 |
| fb4f464f-6d0a-3dcb-a0e6-5a8115a46748 | -2.8016 | -52.9617 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 95a6f2d6-74a2-3c74-bb29-7b514609de3b | -3.7218 | -48.9979 | 2024-11-07 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| daedc425-365d-33d0-80e9-1d598151dc3a | -2.925 | -49.3449 | 2024-11-07 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| f3b8a72f-31bf-3a30-afd6-3b86e54b6a44 | -4.684 | -46.3408 | 2024-11-07 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8a3ecfdb-78a1-3a4c-9cd7-f4cad38d15da | -1.1831 | -53.8985 | 2024-11-07 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8f84acc9-c999-36e1-98d5-2b287b9c22cf | -1.165 | -53.7176 | 2024-11-07 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| da61b591-28ae-32f8-a45f-9fb28d9d816b | -2.82 | -52.9409 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| d4a0cdbb-6ffa-3e05-ae21-b4fe04cc61f4 | -5.9975 | -45.3607 | 2024-11-07 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 278cddc7-6c4e-38bd-bd0c-be2b366c9bae | -3.4564 | -50.3832 | 2024-11-07 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 20cb90ac-7038-343a-8282-b78565e92295 | -1.2014 | -53.8983 | 2024-11-07 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f75a4c02-f596-3b66-a7df-1fc609a83f11 | -1.1466 | -53.7379 | 2024-11-07 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b04d3541-ba79-32ee-9700-03b9496d1338 | -4.5031 | -42.8854 | 2024-11-07 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| dc156fdc-2ed4-3961-b188-9885721fad36 | -5.5352 | -47.064 | 2024-11-07 00:20:00 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 3c74441f-95c5-3ee8-9896-b2c0b92f4bb2 | -8.0313 | -49.6341 | 2024-11-07 00:20:00 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d631d49c-6cbc-34bc-9c3d-931557a2b24e | -1.1466 | -53.7177 | 2024-11-07 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| a8eda121-7c81-35cb-8673-c561c3355642 | -2.8016 | -52.9414 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f6e6bd49-9f24-3ec4-89b6-c02b4dbac87e | -5.0155 | -46.8311 | 2024-11-07 00:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e3965979-f614-3b69-a72f-5699d5bf7f05 | -2.4319 | -53.6584 | 2024-11-07 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ddb6883b-7c5e-35d9-b937-e40115412718 | -2.8536 | -48.6856 | 2024-11-07 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| df680b4d-f1ff-33f2-98c3-3a36a96ef43a | -5.9788 | -45.3621 | 2024-11-07 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| c68dedf3-c42b-3c4c-8725-3caa2518e166 | -3.4565 | -50.3622 | 2024-11-07 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fd52f44b-7351-37ef-be47-6ffd569543f3 | -5.6935 | -45.9443 | 2024-11-07 00:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3642ff1b-5ef6-323d-8802-51b4b5d42a13 | -4.6653 | -46.3418 | 2024-11-07 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f0298fa4-ef28-31bb-8bef-9854f54b3341 | -4.5033 | -42.862 | 2024-11-07 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 94c94834-cf04-3285-8453-d20e088aa865 | -5.0526 | -46.851 | 2024-11-07 00:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 74c0e0eb-a30b-3f7e-9ecf-9409a7ce1b79 | -3.0397 | -53.2603 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6eb02402-dd35-39df-9f9c-f435d9c7f5a1 | -3.1617 | -50.2038 | 2024-11-07 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 20f5cf4d-f8d9-3993-9198-8631f969749f | -6.0782 | -44.719 | 2024-11-07 00:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 36090753-1d7e-3d66-ae26-46fda7d51296 | -2.7753 | -45.1287 | 2024-11-07 00:20:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2aea9b62-84d3-33cd-93af-d5cb9df33506 | -4.522 | -42.8608 | 2024-11-07 00:20:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 393d7614-b18a-3fc1-ad98-7e3f91bc4de4 | -3.9669 | -48.1716 | 2024-11-07 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 81285b1e-fda0-3f0c-8e46-cc56589ca8e3 | -4.4596 | -46.508 | 2024-11-07 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4eb91e45-d97e-3502-8534-a249215b7a92 | -5.5538 | -47.0628 | 2024-11-07 00:20:00 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 37b9a7e3-02d4-3205-8a00-df1dead2d3a6 | -3.0207 | -53.443 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| c0e76bf0-21b9-3dca-bf8f-68073cb5b8ea | -17.293 | -57.5062 | 2024-11-07 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 86826648-2714-3ce6-b7e5-dd036c6e5953 | -3.0207 | -53.4227 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 720fb39f-f4ad-3551-ad9a-acd5c60084c3 | -2.82 | -52.9613 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| ff3fe6e9-7112-3848-b2d0-440e3fd98dab | -3.0396 | -53.2805 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 984bb061-8664-3d7c-acf8-c1d75e394ccc | -2.7639 | -53.2265 | 2024-11-07 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 928c6d93-b25a-3707-a8d4-57c32c938464 | -4.5218 | -42.8843 | 2024-11-07 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d9de13f3-d141-30e2-ab27-db618bf4c20f | -2.8537 | -48.6642 | 2024-11-07 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 79b51716-78af-3763-8648-0213528d29f6 | -5.9587 | -39.6837 | 2024-11-07 00:20:00 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 0dac73f0-a4bb-3052-ad49-4ae1a93bf58a | -4.0815 | -51.0084 | 2024-11-07 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 42335984-59ec-3a0e-876b-b73342df5a93 | -3.9485 | -48.1508 | 2024-11-07 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b204a29d-d194-3431-8be8-d56a86c57911 | -3.967 | -48.15 | 2024-11-07 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ee31ef11-bd18-3935-a237-2329ef9966ba | -5.034 | -46.8521 | 2024-11-07 00:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 1c8cd0d7-0e08-3225-81de-78867765f55e | -5.7122 | -45.943 | 2024-11-07 00:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3ac8cd46-926b-3ad8-91bb-a1757ed49891 | -4.5033 | -42.862 | 2024-11-07 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6ea77177-88da-35aa-8731-ced57d1fc004 | -3.9669 | -48.1716 | 2024-11-07 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 03a5ddd2-96d8-3725-b57d-6f7fde2f45fb | -4.6653 | -46.3418 | 2024-11-07 00:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3f9f1cc8-9649-3550-bf80-29b6c0bbe540 | -4.522 | -42.8608 | 2024-11-07 00:30:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 64faa45c-a831-3804-a488-4e74d3f0b523 | -4.0999 | -51.0077 | 2024-11-07 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 0f69489e-5e98-345b-a6d8-c29dd091222e | -1.2014 | -53.8983 | 2024-11-07 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 107455de-36fc-38be-bdfa-34559bda7af5 | -2.603 | -51.7589 | 2024-11-07 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 13f5b866-da36-353d-a1e9-510e58073048 | -3.0023 | -53.4434 | 2024-11-07 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 945430b5-9d7c-3cb7-8288-0e80ae14e691 | -2.82 | -52.9613 | 2024-11-07 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 5c58b66c-c770-3682-9062-5c6831aba51e | -5.7122 | -45.943 | 2024-11-07 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1a04b2dc-09b7-3468-a593-5180a614fc29 | -2.4319 | -53.6584 | 2024-11-07 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 98af8669-0f64-3f62-b623-602bbb7722d6 | -5.034 | -46.8521 | 2024-11-07 00:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 149.4 |
| fa9207b6-7f7d-3aed-b5ad-ce7400e673f4 | -2.82 | -52.9409 | 2024-11-07 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 3c4bbebc-bb9f-376c-af65-cf840d071e71 | -3.0207 | -53.443 | 2024-11-07 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |


[Clique aqui para ver as próximas entradas](README3.md)
