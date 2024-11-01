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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1217b5ac-f68e-328f-869b-ed3cfaafdc1f | -3.2416 | -53.3764 | 2024-11-01 14:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| b0a70ff8-c6f0-3d85-9585-785cb7efc7bc | -3.7701 | -43.5554 | 2024-11-01 14:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4652008f-f154-3398-8146-833cb2bdbe08 | -3.7703 | -43.5323 | 2024-11-01 14:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d096d1da-5337-38f9-bb29-ddd0228728da | -4.1392 | -44.2048 | 2024-11-01 14:25:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cadac8f3-1f3d-355f-b6d9-5a5d8cd9ab84 | -4.3869 | -43.4525 | 2024-11-01 14:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| aa9ea2f6-5e43-3fc9-b435-312a3ad621ae | -4.6349 | -45.3594 | 2024-11-01 14:25:32 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d85b2e87-9d5d-3bda-84be-8552cb35f9ef | -4.9757 | -42.2887 | 2024-11-01 14:25:34 | GOES-16 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| a9a965a0-dcb6-3b75-937a-b5ce9f337dc5 | -7.9523 | -72.604 | 2024-11-01 14:25:52 | GOES-16 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4ff63bb5-78b9-3f3a-b8e5-50959d3661f3 | 2.58 | -60.6973 | 2024-11-01 14:34:51 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| de89acd2-80c2-38b4-997e-a56d8c4b9edb | 1.796 | -50.4467 | 2024-11-01 14:34:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 61b9f79c-026d-3526-b469-0b86052f5154 | -0.6896 | -51.6847 | 2024-11-01 14:35:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 374d4fad-698d-3930-91ea-46d7b5efb970 | -1.4426 | -52.273 | 2024-11-01 14:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 99766857-a7d0-3eff-b0e1-3dd427e7f742 | -1.5535 | -51.9845 | 2024-11-01 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 15d998ae-0992-35d1-a616-1ed5ed76b541 | -1.6079 | -52.3935 | 2024-11-01 14:35:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e589d98f-d994-384a-a63c-f5176213a0ea | -1.6079 | -52.3731 | 2024-11-01 14:35:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cc3d3801-d7ef-37df-a632-db2ae4add530 | -1.5532 | -52.1076 | 2024-11-01 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 33d2f717-a257-3a92-a463-d39c43519a48 | -1.7366 | -52.3507 | 2024-11-01 14:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e518f00c-9b0e-3b89-b407-fe21beaa9510 | -1.8654 | -52.3077 | 2024-11-01 14:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 85689332-8a23-3dc1-a128-0487c259b0ac | -2.1563 | -53.6636 | 2024-11-01 14:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 336154cd-9b6d-3553-be45-076d1d1ac6c2 | -2.1695 | -48.7252 | 2024-11-01 14:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 543667f6-8244-33d1-864f-c00ae4ece17d | -2.0051 | -55.7011 | 2024-11-01 14:35:18 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ee82c615-347e-36a9-94aa-dda60535a756 | -2.2684 | -46.6821 | 2024-11-01 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| bd4f87f9-f629-34a8-8cf6-31620272cd5a | -2.1747 | -53.6633 | 2024-11-01 14:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bb2faa23-82ba-3b73-9634-084de2c68f5b | -2.3545 | -48.678 | 2024-11-01 14:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 73d82104-6ffe-3d42-9a68-3326ca5cfb6a | -2.3537 | -48.9133 | 2024-11-01 14:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 2fe74979-3ebd-32c3-8ba8-c62457e6a74a | -2.2499 | -46.6606 | 2024-11-01 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| b7d30cdd-c7c9-303c-9843-801f38f9bfcf | -2.2681 | -46.7702 | 2024-11-01 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 2fe88b55-d375-38e0-9acf-c0003639344e | -2.2685 | -46.6601 | 2024-11-01 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| b235f777-cba4-3c73-8299-d978bfa038da | -2.3259 | -46.1275 | 2024-11-01 14:35:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| bde86ffa-f105-3e18-8ab6-6087c967ba8d | -2.2866 | -46.7697 | 2024-11-01 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 2740db46-dc3e-3c9b-a868-b0ab6b04e37f | -2.2134 | -46.5071 | 2024-11-01 14:35:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2cf2138a-49f6-37b2-96d5-a81f1333ad54 | -2.5192 | -49.1649 | 2024-11-01 14:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c83f49e6-6753-3433-998a-2437e7c7d254 | -2.5377 | -49.1431 | 2024-11-01 14:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 380e9c8f-54c6-386b-9c06-08bf828fea23 | -2.676 | -46.7365 | 2024-11-01 14:35:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 860c8c2d-f68c-3116-8f25-6909b3e76c60 | -2.8544 | -48.471 | 2024-11-01 14:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bc158f75-cab2-39fe-81fb-0394786f9f76 | -2.8722 | -48.6636 | 2024-11-01 14:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 426da92e-176d-3646-ae79-84e01eaa406f | -2.7961 | -49.2211 | 2024-11-01 14:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ac9c30b0-0caa-3682-9519-04391c740167 | -2.8537 | -48.6642 | 2024-11-01 14:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 76b84ef0-0cd5-3ddf-ab07-93b4f31e2359 | -2.8509 | -49.3895 | 2024-11-01 14:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6d4a8500-75e9-3d4f-8451-d6349c79cc22 | -2.836 | -48.4501 | 2024-11-01 14:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d5c62e68-8da5-39c7-b02a-d917ea70f418 | -2.8754 | -52.8989 | 2024-11-01 14:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ec67658a-c01f-3d73-ae26-c3653bdd04ee | -2.9354 | -46.7722 | 2024-11-01 14:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6b02b93c-326c-3d1d-afd1-a775a36b70ed | -2.9094 | -48.6196 | 2024-11-01 14:35:23 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 18070559-9663-3f81-bd4e-b19a3d465ab5 | -3.4078 | -41.6192 | 2024-11-01 14:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 8f57d193-a7fd-3b7c-a9dc-9a072786dc44 | -3.2611 | -53.0717 | 2024-11-01 14:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 49344da4-c51b-3c47-85a1-1d205a636da1 | -3.42 | -42.7798 | 2024-11-01 14:35:25 | GOES-16 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dd2880d2-3b80-3bae-9433-c925d254adcc | -3.2535 | -50.3479 | 2024-11-01 14:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 1a29e925-9047-3c82-8118-429c00d5cc4b | -3.3891 | -41.6201 | 2024-11-01 14:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| b5194a10-8d23-3889-9beb-c56f148c6dc9 | -3.2535 | -50.3269 | 2024-11-01 14:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 5231bceb-5434-3706-878b-3abce4791d6b | -3.272 | -50.3263 | 2024-11-01 14:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 30ff1e9f-0289-3b9f-b677-e2ee8412bd9e | -3.7703 | -43.5323 | 2024-11-01 14:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ddb25fda-d9f7-3a58-9900-9d984b4be380 | -3.7701 | -43.5554 | 2024-11-01 14:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 90a5dc02-b4e1-37ed-aafc-c9e2d6a5799e | -4.0146 | -43.2641 | 2024-11-01 14:35:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ec0d5f80-c1c7-34b5-8a38-e11ac92c99e5 | -4.2033 | -45.8538 | 2024-11-01 14:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 4cac8ac7-34a9-3d60-97dd-aab4bf3cdab4 | -4.4056 | -43.4514 | 2024-11-01 14:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| a4dcddac-a35e-3628-a93d-281d029e784b | -4.3869 | -43.4525 | 2024-11-01 14:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| af9adeaf-fd5d-360d-ac95-f7c01f0c5fb6 | -4.3867 | -43.4757 | 2024-11-01 14:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 199.1 |
| c94f0e1b-9249-3c9b-b0c0-43dad79cf802 | 3.4157 | -51.2606 | 2024-11-01 14:44:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 987f0c2f-0907-33e7-bdc0-16f5d141a412 | 3.4342 | -51.2601 | 2024-11-01 14:44:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f7069b48-2192-3b3a-9cf0-1538f1151ad7 | 2.58 | -60.6973 | 2024-11-01 14:44:51 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 40a45112-67c7-319b-8277-5387ba58007b | 1.6751 | -55.824 | 2024-11-01 14:44:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a958c774-7797-3bd9-b499-7b8f69fb0344 | 1.796 | -50.4467 | 2024-11-01 14:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 978a63f0-7986-3baa-b6fc-2bdf9af8b9c7 | -0.6896 | -51.6847 | 2024-11-01 14:45:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 75.1 |
| bfa17c3f-75b9-3061-b548-23d40ccab4d3 | -0.7915 | -63.0797 | 2024-11-01 14:45:11 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9e0df61b-0514-37e3-8dca-403181f9b480 | -1.165 | -53.6773 | 2024-11-01 14:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 19f58139-f889-3163-811c-ba436bd49d2d | -1.4244 | -52.2118 | 2024-11-01 14:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| ca4e332a-70a1-36f4-a4ac-9d758be4c3fd | -1.406 | -52.2121 | 2024-11-01 14:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7386f1f7-3a8f-3623-89ab-2e8d97ea46d1 | -1.4394 | -54.2169 | 2024-11-01 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 634956db-2519-3dd0-99c3-878928855fcf | -1.5077 | -47.225 | 2024-11-01 14:45:15 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c762e0fc-1a28-37a7-9b9c-8fef457ac2ba | -1.6079 | -52.3935 | 2024-11-01 14:45:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 74338b2c-472b-3798-9ea3-002c211f51cc | -1.5348 | -52.1489 | 2024-11-01 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b817af52-2967-3fb1-9377-c90e3201c3b9 | -1.5349 | -52.1079 | 2024-11-01 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4caff81f-3d05-33ea-ae9c-cbe8abaea90f | -1.6079 | -52.3731 | 2024-11-01 14:45:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| da5e674b-0352-3fa4-9cbb-4230982cde3e | -1.5348 | -52.1284 | 2024-11-01 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 71ac4ad7-6f8a-3745-a15c-bce42052d2ff | -1.7366 | -52.3507 | 2024-11-01 14:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e3fff4ff-c143-34ab-8d3e-ca009808c3f6 | -1.755 | -52.3504 | 2024-11-01 14:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f353d8d2-7870-3829-8cf3-5371603e73ab | -1.7366 | -52.3712 | 2024-11-01 14:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a7e8ea02-d2a0-3ab7-a70c-10de6587df3e | -1.755 | -52.3709 | 2024-11-01 14:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b62debfb-4ec5-33dd-a094-0c5116c1be16 | -1.9565 | -45.6019 | 2024-11-01 14:45:17 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 45af549d-e64c-34d0-8607-489c29de4358 | -1.9751 | -45.6014 | 2024-11-01 14:45:17 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0b4966b1-f8e8-3c8d-8234-2f30ad7d3b9b | -1.8654 | -52.3077 | 2024-11-01 14:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f8b033e8-ffff-3977-bcf2-cde9b8d1e45f | -2.1563 | -53.6636 | 2024-11-01 14:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6a6894e2-06a5-34c2-bcac-49461b2adbd7 | -2.1563 | -53.6838 | 2024-11-01 14:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 400338d7-0637-330e-948a-92ff1567b4f8 | -2.1695 | -48.7252 | 2024-11-01 14:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| c986ad75-d826-316d-be60-27a7d5c50ad7 | -2.287 | -46.6596 | 2024-11-01 14:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 972c16f8-9dae-31c3-b6c7-722224b1ebbe | -2.2134 | -46.5071 | 2024-11-01 14:45:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 267398a9-7175-328b-9947-6048ada36cec | -2.1747 | -53.6633 | 2024-11-01 14:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4cb9195f-d253-3b27-a780-f1827945a375 | -2.3545 | -48.678 | 2024-11-01 14:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 1be5d633-bf63-316a-a357-1210472799fb | -2.3537 | -48.9133 | 2024-11-01 14:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8903b415-fe83-307e-8670-06cfc5b32bad | -2.2499 | -46.6606 | 2024-11-01 14:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 919159f6-fa51-3960-a184-f5531b36b98f | -2.2681 | -46.7702 | 2024-11-01 14:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| cb209987-411a-3829-a2a7-df5f78fedc94 | -2.2685 | -46.6601 | 2024-11-01 14:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| c77c0830-98a7-34ac-b86e-e75b2d2737c3 | -2.3259 | -46.1275 | 2024-11-01 14:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 5792a14e-bc02-359f-86a8-73ffb5ce29b4 | -2.4344 | -46.8976 | 2024-11-01 14:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 80d108ee-20df-378b-baf8-0de1a6a74b2a | -2.5361 | -49.6313 | 2024-11-01 14:45:21 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 69190b5c-bf00-30f9-94d9-83a3575fcf51 | -2.5377 | -49.1431 | 2024-11-01 14:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| da72e2fa-bc7c-3600-b341-61cdddf20b88 | -2.8545 | -48.4495 | 2024-11-01 14:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 355777af-5970-3339-b4f4-a05cef139109 | -2.836 | -48.4501 | 2024-11-01 14:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| dbb24e56-b851-3107-a858-fe25e19bb7f9 | -2.8544 | -48.471 | 2024-11-01 14:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 770ff870-2af1-319f-b23c-a0bc1e45d09f | -2.7952 | -49.476 | 2024-11-01 14:45:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |


[Clique aqui para ver as próximas entradas](README63.md)
