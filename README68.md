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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8f75edd-f52c-38ec-bd22-7f917139a27e | -9.56724 | -64.62566 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b399543-c2e1-3421-957e-e93eeac7d232 | -9.56665 | -64.62001 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e921b14d-0856-37d9-8c47-ac56d046ae50 | -9.56605 | -64.62411 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb383d2a-e338-3f4f-a7fa-3d5fdde34665 | -9.51557 | -65.60435 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68b4affb-a633-38d1-818a-79c2b873a31c | -9.51214 | -65.60381 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a245a4-9366-34bf-a265-dfbbd7fa4f66 | -10.40079 | -65.37659 | 2024-10-16 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2333e126-fa2f-3fc9-a81b-09805409f23a | -10.16938 | -64.78408 | 2024-10-16 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a86c63e5-91a5-3b06-a878-439c934ef344 | -9.14995 | -68.87068 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35dac595-ae69-3ada-bf86-3ec3117e5abb | -9.14103 | -69.14098 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce1b4221-e290-3a1b-819a-4e4b36a2c502 | -9.04066 | -68.87499 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff1c609b-9cdd-366a-8fee-a8e483e544da | -9.0297 | -69.24486 | 2024-10-16 05:48:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a3d4959-8354-34f7-888c-fb3d3f9d1e49 | -8.97773 | -69.54341 | 2024-10-16 05:48:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bd522e4-c3b0-3782-97ae-ab73058a831c | -8.97426 | -69.54282 | 2024-10-16 05:48:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5aa802c3-8293-38dd-8a93-edbccf96b1ac | -8.6719 | -70.06778 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3dabf62-d12c-3c7a-a212-567ea522166b | -8.61906 | -70.03403 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd026a31-a808-3b17-8c26-b88234b09d61 | -8.61551 | -70.03345 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1d19ef1-38c6-331d-93c7-7683dcc7f7f1 | -8.61483 | -70.03746 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a7cd89a-5ce2-372a-90c3-051c8421b23c | -8.61368 | -70.03045 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a2aff1e-5404-3c84-abf1-25e9fe68f052 | -8.61303 | -70.03447 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ead0bbc-bf2e-3b84-91ee-cba76aba1b04 | -8.61237 | -70.0385 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 030a4fc1-d3f4-356b-ab73-e6c5dcc966a8 | -8.61061 | -70.04091 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bf9850b-b7ab-3058-a29a-b773fbccd923 | -8.03885 | -70.17044 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 100ef471-00e4-3c72-9906-4af3ed409635 | -9.80706 | -69.08522 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a99f87-1666-3197-af39-0d0a6fba9594 | -9.57835 | -68.98772 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50cc2886-89e1-340f-af6e-e0e69e67cf28 | -10.46083 | -69.25476 | 2024-10-16 05:48:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56dbe91-0cc0-364d-bfc9-5f55e51168ca | -10.45372 | -69.29892 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf6b672a-42d4-3f70-9f5d-2b546767c405 | -10.45031 | -69.29837 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61f229f1-8555-3e3a-883f-f4c04e2e5eb4 | -10.32429 | -69.47254 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745eb6c0-715c-3331-82f2-00e8043bba48 | -10.23363 | -69.40387 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f98a1c3a-fd23-3d33-8b0b-abfc715b9a7f | -10.14944 | -69.32197 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7881831c-588c-31df-8e2f-5adb740f59cc | -10.14883 | -69.32565 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5121f108-9c8a-38da-b364-22a8c5134ad7 | -10.11482 | -69.16892 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea508a38-48b5-3c7e-98cd-e7e593fcfc5c | -10.11423 | -69.1726 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4040893e-db41-34f6-ba05-0d80cee6d55e | -10.11143 | -69.16837 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aee4a06-4528-3c95-9cf8-bb7ab9258165 | -8.03345 | -70.2037 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acb62034-6f88-3abd-b63a-7504096c17a1 | -7.98956 | -70.29073 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cc48aa6-5d08-308b-aefc-e8f6bd6696c9 | -9.12552 | -70.78455 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f59e11a-a09f-3018-9340-de1114fa47df | -9.12482 | -70.78886 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f80716-22ca-3aae-a0e2-74acb016b8e3 | -8.86628 | -70.90571 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b61cbb10-eb06-3c3d-9531-a0df05911b09 | -8.69367 | -71.03767 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3335fe9d-8986-3da2-8008-060be81bc28d | -8.3724 | -70.97148 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8e782cb-875e-32f6-a80f-dd155ad48566 | -8.26782 | -71.13277 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e226a7b-7f0b-3680-b7e3-83878b0f1e56 | -8.19973 | -70.48844 | 2024-10-16 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cc7e5da-dd04-39d6-abb1-602fec779f7a | -8.04645 | -70.95448 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 641b903f-4d54-3085-b41f-c15135851509 | -8.02416 | -70.90216 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d8fa81a-f354-3e8e-a991-701ce37a3813 | -8.01059 | -70.82144 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9581fed-b454-3a6a-9323-1cb18d94db8c | -7.96357 | -70.89656 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcf15be5-7042-3cd0-95d9-b55a26ee5be9 | -7.93643 | -71.5332 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a17da831-6a40-3d06-aa80-749a0b614e23 | -7.93618 | -71.53493 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b0ffcb0-c385-389a-b935-c58e0a80f3cc | -7.91992 | -71.56071 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8821c0cc-1516-3c19-a0a6-0b5022b2da0b | -7.91947 | -71.5624 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e3d6eb-cb70-3b22-bf34-e37396a3559a | -9.42806 | -71.8868 | 2024-10-16 05:48:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f70fad5-12a9-3472-8772-5b0e8cbc5424 | -7.85388 | -71.76441 | 2024-10-16 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da61d607-18b6-30f5-908f-d1316e743649 | -7.80918 | -73.10018 | 2024-10-16 05:48:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 956f06de-d535-3bef-a023-9427182ecd98 | -7.75773 | -72.28766 | 2024-10-16 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 091ab04c-69f1-3544-8815-cbc26686eca6 | -7.75365 | -72.28691 | 2024-10-16 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b54b8fc5-ca86-37cc-8368-346a6499d346 | -7.40849 | -72.61416 | 2024-10-16 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e70bf25-5c83-30ce-a61d-22fb7f2db17b | -7.40364 | -72.61732 | 2024-10-16 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 711ac677-5954-393c-b215-79d9642615ee | -7.36742 | -72.62704 | 2024-10-16 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa60190f-4727-3646-bb48-978bd06c7721 | -7.32841 | -72.44841 | 2024-10-16 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8ab2b88-8dd9-36a1-ba7c-9229b5d106af | -7.32778 | -72.45216 | 2024-10-16 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82910135-7d49-3fb5-9534-6c818e8fdb8a | -8.18056 | -72.92667 | 2024-10-16 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 625f0323-e3a3-3535-b0e6-06d440987d65 | -10.79218 | -68.78387 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99e72cbf-4a1b-3bdf-a7ea-1e812423ce55 | -10.78767 | -68.7905 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46df29c1-088e-31b9-bce1-bacd2c5d76a7 | -10.76213 | -68.66198 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212dda15-eb32-3391-ab07-20ee5576e359 | -10.73004 | -68.86252 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f500c00c-c137-393d-9aee-67173add1129 | -10.66782 | -68.57294 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b6bdf8c-1aa5-3d96-8115-b9471e5c36ec | -10.66 | -68.57897 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2825c5dc-e032-3955-8b0f-c906f8831b60 | -10.65189 | -68.6727 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27b21b93-358a-3889-8ff1-cbbd79bb3046 | -10.63652 | -69.01389 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 490e1d15-a460-3c6a-b719-ea8a47d01ac6 | -10.58485 | -68.79028 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97c6f914-1380-37f5-9a88-2a25d54df638 | -10.58427 | -68.79387 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c2aa11f-864a-3620-814e-7d1cea2426c4 | -10.57767 | -68.7707 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 094e9c79-555e-301b-918c-0cfaffc334ba | -10.57431 | -68.77016 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da2eea1b-2c07-3a51-bbe2-fdd7013c327d | -10.56167 | -68.82705 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24bfe3f9-4ea6-3846-b169-7f186eefdfb2 | -10.55831 | -68.82651 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31608463-71f3-3d2a-8074-617a2103215f | -10.55441 | -69.17186 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 658fb752-3c7d-3268-933f-e906877f3551 | -10.83033 | -68.27659 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c14c86c3-6e46-3e0a-9762-0a4118c307f8 | -10.82189 | -68.35126 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f3695bb-7611-3f58-89cb-949b86966011 | -10.76307 | -68.31272 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a90c5ee-f48b-3177-bb75-b3a03fc0b47b | -10.87085 | -68.22862 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb9d2579-9064-30c9-9a92-1b0896bf6dcf | -10.79103 | -68.79105 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4afd03bd-4873-3d22-a883-0b21d80d8cec | -10.78756 | -68.81257 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86deab21-40f5-3e3d-b31c-b0d705b3c9ef | -10.7627 | -68.65842 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dfd26ca-b1cb-3cd1-89c3-7bad2dd4191f | -10.75974 | -68.31216 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0e98e8-dedc-32f4-b547-61caa122604d | -10.70892 | -68.56557 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98ff17ad-ee33-3157-9a01-890cf3640470 | -10.70321 | -68.60115 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2ece145-33b2-396a-ae2a-09e59a607c03 | -10.66725 | -68.5765 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c2dc4f9-c6b7-36dd-8076-44fd21c7241a | -10.66553 | -68.7709 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8d05b2d-c258-3e5f-8708-b83ce2d2d4aa | -10.66391 | -68.57596 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d20c2ab5-c2fa-37cf-9dc8-f4243724dcaa | -10.65745 | -68.68096 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 036739be-b847-3c6b-a35e-ca369761cb65 | -10.65544 | -69.04674 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 860925eb-7605-3f6c-8c27-0741fe5f3587 | -10.65219 | -68.85338 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8a1c352-93a6-3291-8ff9-db4c0dcc920b | -10.95627 | -68.24976 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 284d7029-ab28-348f-8f35-d07ee4a96b8d | -19.58595 | -56.96916 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 95efac5d-82ca-3f16-8b9c-ce5b7fecb491 | -10.93058 | -68.36868 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 837a720b-8d76-3bcf-95cd-ed9a529e7d62 | -10.8842 | -68.20911 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7c92860-c9e4-3db1-b9c7-c8e04e804f65 | -10.90703 | -68.65954 | 2024-10-16 05:50:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e8cd641-db16-3b00-b905-1d70a2529ff8 | -10.90126 | -68.29507 | 2024-10-16 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7619b676-6d0d-3872-a40f-76c73271c462 | -15.91774 | -56.30668 | 2024-10-16 05:50:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
