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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b566c6b-d4cf-38f5-9fed-cae1cd6c6147 | -9.97 | -36.04 | 2024-11-03 00:04:26 | MSG-03 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f07f94b-2077-3ae3-bcee-ee59e730aabd | -9.97 | -36.08 | 2024-11-03 00:04:26 | MSG-03 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d90f0906-1cb2-3f23-a46a-d814e6a86d5b | 2.5498 | -51.0981 | 2024-11-03 00:04:51 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 41.6 |
| a390d96f-3d95-3766-ae79-574d667d12e2 | -1.2572 | -53.3938 | 2024-11-03 00:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fdb27b9c-ca7c-320c-9e19-4ccd1738fe6e | -1.2572 | -53.3736 | 2024-11-03 00:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3e176729-bf10-3734-a097-2dae661da762 | -1.2756 | -53.3734 | 2024-11-03 00:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| a26a6fcd-f8f5-34f5-a754-1b7b4d4535a2 | -1.2755 | -53.4138 | 2024-11-03 00:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d6c23516-9e2e-3480-b899-c35388639425 | -1.2755 | -53.3936 | 2024-11-03 00:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 74eb97ec-3047-350a-831e-bac6c283c3ba | -2.73 | -54.45 | 2024-11-03 00:05:13 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023b54bc-0d5e-31a2-bbd7-169efe23d78b | -1.3777 | -47.4453 | 2024-11-03 00:05:14 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 114f8cb9-0ca2-3277-a8fd-d6b6bf6dea10 | -1.8788 | -54.6908 | 2024-11-03 00:05:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e227b1c3-9c48-3f23-a509-7d4d34ce0360 | -2.1746 | -53.6834 | 2024-11-03 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 4476cd41-8b36-3732-a914-5c75dad5f418 | -2.2082 | -48.1657 | 2024-11-03 00:05:18 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 77811798-35ce-3f7e-8448-5079d9294993 | -2.2802 | -48.8082 | 2024-11-03 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 8ebf475e-6aef-30e2-b7de-db6900552f60 | -2.2986 | -48.8078 | 2024-11-03 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 229.3 |
| a392a08d-44c2-31a7-b645-5b5b105be277 | -2.2987 | -48.7864 | 2024-11-03 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 34bb9078-fb4d-31d4-b688-8acbcbec0a19 | -2.5696 | -57.1242 | 2024-11-03 00:05:21 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| abadcd9a-7a5d-3435-899a-cba406e126d9 | -2.5697 | -57.1047 | 2024-11-03 00:05:21 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| cc274acf-06b5-3099-ad83-06ec32b83dc6 | -2.5796 | -53.3927 | 2024-11-03 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 860990a5-e4bf-3bf4-868c-b94482983580 | -2.5797 | -53.3724 | 2024-11-03 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| d60351cd-94c1-39ae-801f-3b9c858c6df5 | -2.598 | -53.372 | 2024-11-03 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e31612da-441a-3ea6-a058-f45ec2c7e128 | -2.6321 | -48.5849 | 2024-11-03 00:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 94b9e603-edab-37f9-b084-6e2ffe937a16 | -2.6322 | -48.5634 | 2024-11-03 00:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 555ef7ec-f140-3dfd-aca9-04b6ff8451a4 | -2.6506 | -48.5844 | 2024-11-03 00:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| dc281798-5378-3282-8122-68ff61db61d8 | -2.6507 | -48.5629 | 2024-11-03 00:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 5d9a52af-8076-3b5d-9248-01ab7f4160e4 | -2.7419 | -54.4353 | 2024-11-03 00:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 629ddb2e-e403-302a-9e28-9d972166dd94 | -2.7419 | -54.4153 | 2024-11-03 00:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 188.7 |
| f1f4cc10-6991-3e7f-98d8-b48a8a6435c7 | -2.7602 | -54.4349 | 2024-11-03 00:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 200.4 |
| 9d4f8c58-d125-3e3f-85dd-15a1c649290f | -2.7603 | -54.4149 | 2024-11-03 00:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 180.3 |
| f5abfb8b-e4aa-30fa-b87f-45771301cd9c | -2.7876 | -51.6099 | 2024-11-03 00:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7257a4a9-9450-34a9-b028-1cea66412a73 | -3.055 | -54.1675 | 2024-11-03 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f8f533a9-8668-3845-87b3-062d0c37ebb4 | -3.0365 | -54.2081 | 2024-11-03 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1be348ad-4d8d-3060-aa03-6eb762b76c1c | -3.0396 | -53.2805 | 2024-11-03 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4f7e422a-ad15-324c-a9c1-927e2bb55334 | -3.0397 | -53.2603 | 2024-11-03 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 35f647a5-b86d-320f-8e7b-2eae6bf1ccb5 | -3.0732 | -45.0275 | 2024-11-03 00:05:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ab5cf5af-d3bc-3352-bad4-75dd37b4f715 | -3.055 | -54.1474 | 2024-11-03 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 03b393b0-a53a-32db-99ab-885149d7cd56 | -3.0734 | -54.167 | 2024-11-03 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 1b677246-7acd-3264-8c08-06db43737589 | -3.0734 | -54.147 | 2024-11-03 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 180.2 |
| 168ed48c-dfbe-34d8-9cd8-d5694bb6a49d | -3.0917 | -54.1666 | 2024-11-03 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 810d0a08-b26f-3821-8d20-446811400d6c | -3.0918 | -54.1465 | 2024-11-03 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5c09ab67-fcd2-349a-b549-aa2928f58160 | -3.106 | -50.2896 | 2024-11-03 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 845bf418-66c4-3f25-b476-e254864bb306 | -3.1212 | -51.1244 | 2024-11-03 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 1b0d58dd-6229-319d-82e6-a93b1bca825b | -3.1213 | -51.1036 | 2024-11-03 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 418b5bec-8e63-3f50-9403-cddc8513b934 | -3.1282 | -54.2459 | 2024-11-03 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ab66aa8f-857f-3dc0-8705-5524ce578915 | -3.2231 | -53.3972 | 2024-11-03 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| deb8b383-bb0f-3c46-9e61-6a6e442e3647 | -3.2415 | -53.3967 | 2024-11-03 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0f48bc92-90e4-3bce-8c03-792707dfb4f3 | -3.2599 | -53.4164 | 2024-11-03 00:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bf43e0e0-478c-36ef-aa89-7dc5877b6ce0 | -3.2624 | -52.746 | 2024-11-03 00:05:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3ae1094d-6300-3c42-a7e0-f43b47f69b38 | -3.2624 | -52.7256 | 2024-11-03 00:05:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5acbb5c4-1cc6-3776-b1b9-3c7ae6d23d15 | -3.2808 | -52.7455 | 2024-11-03 00:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a92fdf06-d25d-318b-a7a7-37afbfc61762 | -3.2808 | -52.7251 | 2024-11-03 00:05:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 24db087a-08c1-34dd-b68b-bddd90941e96 | -3.3276 | -50.2825 | 2024-11-03 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 7c3214fb-74a8-3322-a6af-75714a042f24 | -3.3277 | -50.2615 | 2024-11-03 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 74973dda-27ed-35b6-a038-a8c591782f4d | -3.3461 | -50.2819 | 2024-11-03 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 604d798d-d669-3321-b045-e02b872b5308 | -3.3461 | -50.2609 | 2024-11-03 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 866a29dc-29a3-3532-98d8-a3102a811469 | -3.4749 | -50.3826 | 2024-11-03 00:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| db0401be-982b-3556-bae6-d2bd1e05505b | -3.475 | -50.3616 | 2024-11-03 00:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b9e4cc2d-e00f-3d45-be89-6d4a96ba52dc | -3.5492 | -50.2961 | 2024-11-03 00:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e8622b17-4f90-34e1-b470-6e3d3ecd1748 | -3.9473 | -48.3666 | 2024-11-03 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3a2766b3-5d8c-336e-8b24-c827153726b2 | -3.9474 | -48.3451 | 2024-11-03 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 467f225f-be53-398e-81a5-ca56ef4fdb08 | -3.967 | -48.15 | 2024-11-03 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bac8f67b-ed74-32c4-b74e-b841c1866786 | -4.0283 | -47.146 | 2024-11-03 00:05:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7f5d871a-c502-3504-a3e9-1489ae346e2c | -4.0469 | -47.1451 | 2024-11-03 00:05:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f31c6152-a57d-371a-8271-855e9d4d3a70 | -4.4054 | -43.4746 | 2024-11-03 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2d2f26d9-3448-36f8-b2ed-6ea7dadfbe80 | -4.4056 | -43.4514 | 2024-11-03 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 8e95a066-f304-36a0-a9d0-6ad3c4df3244 | -4.4241 | -43.4735 | 2024-11-03 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9ce8e5e2-cd38-31ec-af2a-a274d5484fca | -4.4243 | -43.4503 | 2024-11-03 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8189a86b-50c8-34af-85fe-cca284016b89 | -4.8723 | -48.7318 | 2024-11-03 00:05:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3c054371-454c-32ab-ae67-d0d834f311d3 | -5.9728 | -48.2366 | 2024-11-03 00:05:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ab52799c-cdf9-3cfa-a667-1d7210b1a346 | -5.9729 | -48.2149 | 2024-11-03 00:05:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 53946617-e1f3-395c-9f62-bbc1a9fd69d9 | -8.7059 | -48.0181 | 2024-11-03 00:05:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 17e8c9df-12c1-352e-bd8e-3cc4dc33ab2b | -8.7062 | -47.9962 | 2024-11-03 00:05:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c5a5d45a-d40e-3e45-8337-3a5c4b5c9f9e | -8.7247 | -48.0163 | 2024-11-03 00:05:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0cd3fba5-36ab-363b-8503-76a31f0bf610 | -8.725 | -47.9944 | 2024-11-03 00:05:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1863698d-a4b2-32e7-aa28-8c890601450d | -9.9731 | -36.0634 | 2024-11-03 00:06:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| b843212a-61eb-3643-9691-b3cbde152720 | -10.8423 | -49.167 | 2024-11-03 00:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8bcbf00c-9be9-3437-9c8c-e73aa68f28b6 | -10.8426 | -49.1453 | 2024-11-03 00:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| eac82c0a-8c22-3e81-986d-0bd393e253b0 | -10.8812 | -49.0975 | 2024-11-03 00:06:08 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e49ba0c1-e4fd-39ab-958e-d29dac94719d | -10.8815 | -49.0757 | 2024-11-03 00:06:08 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 4e8bfd38-5ae2-377e-bc5d-7d7c61c697ad | -11.2819 | -56.144 | 2024-11-03 00:06:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b2d984ef-76f7-34c5-89c3-dac713bf0959 | -1.2572 | -53.3938 | 2024-11-03 00:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3e609077-dc17-3a92-b5e2-e2ba321c906b | -1.2572 | -53.3736 | 2024-11-03 00:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bc9c6ef8-e86e-3468-9af7-2622d59ac64e | -1.2755 | -53.4138 | 2024-11-03 00:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0eff926a-4feb-3f75-b18e-93c6426bce85 | -1.2755 | -53.3936 | 2024-11-03 00:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 102dda07-9e5f-3c92-8dbe-7c16e85e4cad | -1.2756 | -53.3734 | 2024-11-03 00:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 1e15c346-7124-3ef2-9281-86d41768b6be | -1.3777 | -47.4453 | 2024-11-03 00:15:14 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 0f1bda94-d12c-3247-86e6-764f905ccb60 | -1.8788 | -54.6908 | 2024-11-03 00:15:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2b967366-5df3-3f30-a396-1d9fb5ade51d | -2.1746 | -53.6834 | 2024-11-03 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6bab3eb5-520c-357b-96c6-f174516f1b03 | -2.2802 | -48.8082 | 2024-11-03 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 2a8ff735-fe20-3e03-a568-286a07a1af76 | -2.2802 | -48.7868 | 2024-11-03 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 661f6e63-36b7-330d-8e2f-498b3222ebee | -2.2986 | -48.8078 | 2024-11-03 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 309.2 |
| 7c4e6ded-ac38-326c-a480-55c552ceb58f | -2.2987 | -48.7864 | 2024-11-03 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c297e363-82a7-3b72-99b4-6d93c5217d8b | -2.5696 | -57.1242 | 2024-11-03 00:15:21 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 67542aab-b2dd-300a-ac2c-e975364bb2e2 | -2.6321 | -48.5849 | 2024-11-03 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| fe010e8e-0380-3cf3-a41c-9b6643ac0abf | -2.6322 | -48.5634 | 2024-11-03 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5c9d7f83-5788-3dfd-b4d1-697e834efac7 | -2.6506 | -48.5844 | 2024-11-03 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| b569e13f-5ee3-3721-b91a-1b985e437bd5 | -2.6507 | -48.5629 | 2024-11-03 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 49454284-5b82-3cfd-a742-13956b2acd26 | -2.6694 | -48.498 | 2024-11-03 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b88bef7f-952e-384f-958b-31a8b3b75aef | -2.7419 | -54.4353 | 2024-11-03 00:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 88818e7e-f67e-3506-809e-c3002a198a55 | -2.7419 | -54.4153 | 2024-11-03 00:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 208.5 |


[Clique aqui para ver as próximas entradas](README2.md)
