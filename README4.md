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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61dd2f26-64f4-30eb-896e-b56dee4f4b69 | -8.1267 | -43.1154 | 2025-06-19 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| e40d239b-ae5b-3e95-865e-0fb2d3c2e355 | -10.6489 | -49.4483 | 2025-06-19 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 594b4eb5-3ba7-3bd6-a350-b183bd42b0e3 | -16.305 | -58.2474 | 2025-06-19 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 126af9c2-5dcb-3393-b9cb-d7e63468d07c | -11.9329 | -58.7588 | 2025-06-19 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| bfdeea21-f07f-35fb-89eb-ba934c8ddaf8 | -7.2219 | -43.0682 | 2025-06-19 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 05b05810-1453-3424-af52-513c1e82de41 | -11.9709 | -58.7362 | 2025-06-19 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| cea17845-f1b6-3a5c-847c-e4491ae152eb | -11.952 | -58.7376 | 2025-06-19 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 94876fb6-82e6-3eaa-b896-e4ffd3156a81 | -8.1264 | -43.139 | 2025-06-19 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 105d8c7c-380f-36bf-bb86-44249f59c2cb | -7.2217 | -43.0917 | 2025-06-19 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 8eec88d0-41e4-3c32-9b10-e0e34ca8668d | -11.9518 | -58.7574 | 2025-06-19 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 311.8 |
| 257e4e41-2772-31b9-a2b1-e9f6b54ae62e | -11.9707 | -58.756 | 2025-06-19 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 180b3310-d4fe-3a19-92e8-cc1ba3c12a66 | -4.7872 | -47.5676 | 2025-06-19 00:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 80900111-f83e-369b-86c0-e12ea0c44f87 | -16.3047 | -58.2676 | 2025-06-19 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| c3a84920-f65d-3710-bb2b-a657098d1aa4 | -7.2405 | -43.0899 | 2025-06-19 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 217.5 |
| 5293d8fb-a8b9-3c49-818b-cafbd635ce90 | -7.2408 | -43.0664 | 2025-06-19 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| a5e14943-029f-339c-8960-4719823bc864 | -10.6489 | -49.4483 | 2025-06-19 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 188b751c-696d-3f44-bce2-452c38270cef | -7.2217 | -43.0917 | 2025-06-19 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| cc95cb5d-1189-32b9-a2c9-1c2e4140085c | -8.1264 | -43.139 | 2025-06-19 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 13efc9fc-754c-3e86-9b3f-218cc7606258 | -16.3047 | -58.2676 | 2025-06-19 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| ba61f3f6-c06f-3159-a22f-5752084419cd | -16.305 | -58.2474 | 2025-06-19 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| da2dee72-d93f-3605-a949-cfc6a1fbe5f3 | -11.952 | -58.7376 | 2025-06-19 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 232.1 |
| fc4ea9fb-0204-3164-a9cb-3f6b041a83ce | -11.9518 | -58.7574 | 2025-06-19 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 290.5 |
| 87bc560f-d6dc-3d7d-99c2-70d3a15ee539 | -11.9709 | -58.7362 | 2025-06-19 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ccf47fc0-7941-30e5-8720-b6ba826b02d0 | -7.2408 | -43.0664 | 2025-06-19 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 6d1ee009-2bc3-383d-b491-d7e43a9b7666 | -4.7872 | -47.5676 | 2025-06-19 01:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 130a6e4c-0cc1-3f2a-8689-49deaaf1eec9 | -11.9707 | -58.756 | 2025-06-19 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f274efcc-25b6-35dc-bd1d-839a6de4018a | -4.7686 | -47.5686 | 2025-06-19 01:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 213e4cc5-e3c1-3b2e-925f-36156e82b876 | -7.2405 | -43.0899 | 2025-06-19 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 218.3 |
| a0c83053-139d-389e-854f-39d76d4968d2 | -11.9329 | -58.7588 | 2025-06-19 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f8ec3c61-e08a-3439-ae82-aa51010e746f | -11.9709 | -58.7362 | 2025-06-19 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| d0ef4747-5602-31ee-996b-a1238b31c994 | -10.6489 | -49.4483 | 2025-06-19 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 319ec276-db19-3352-b028-1bd45e3eb3c0 | -7.2408 | -43.0664 | 2025-06-19 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 8520200a-93d3-33d7-ba08-c04d4833fddd | -11.952 | -58.7376 | 2025-06-19 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 08cda768-fea6-301e-87a0-13a0c6cf388c | -16.305 | -58.2474 | 2025-06-19 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| ea62fed3-7be6-3d08-a79d-4a011998e75f | -7.2217 | -43.0917 | 2025-06-19 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 5b8a1fed-ed97-3d64-85fb-aa304197ed9a | -7.2405 | -43.0899 | 2025-06-19 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 254.6 |
| 6ad42779-2c55-39e2-9f7c-9ac8ff44346e | -11.9518 | -58.7574 | 2025-06-19 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 215.3 |
| a1cc76a4-88b5-38c5-97a2-60444d2015ce | -8.1264 | -43.139 | 2025-06-19 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 609a1bcf-526e-3a64-8e7e-884222f9aa9d | -16.3047 | -58.2676 | 2025-06-19 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 62c909c5-f5bd-3e6d-a64b-69b0120da8ee | -11.9707 | -58.756 | 2025-06-19 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 4349a6c7-82c4-3782-b946-4dcec3d250a2 | -4.7686 | -47.5686 | 2025-06-19 01:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d4b1ea5a-8415-3ef6-ad2c-9989de28e97c | -7.2405 | -43.0899 | 2025-06-19 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 241.5 |
| 8bdd8803-cd00-34f7-a9e4-515f2698043d | -16.305 | -58.2474 | 2025-06-19 01:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| fefd0d7c-97d1-38f2-ad32-a2808c486fee | -16.3047 | -58.2676 | 2025-06-19 01:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 198d7f14-91ab-34fb-b885-9c11ccf9f884 | -10.6489 | -49.4483 | 2025-06-19 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 161c3195-5ed9-3dc0-a3ac-3ac2a5a3fe47 | -11.9707 | -58.756 | 2025-06-19 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 49606036-0a40-3ba9-8410-e029ed4c55e1 | -10.0972 | -52.7376 | 2025-06-19 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a23e50bd-eb49-312d-9cb7-de6b9633e72e | -7.2408 | -43.0664 | 2025-06-19 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.8 |
| 75b62ea8-1be7-3a35-838c-d6f6f15fa5de | -7.2217 | -43.0917 | 2025-06-19 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 775a16f0-83b2-3b4d-8d90-664490bc94b0 | -11.9329 | -58.7588 | 2025-06-19 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 776e932e-f746-3806-aa7f-fa88f5f01055 | -8.1264 | -43.139 | 2025-06-19 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| f74aea59-f91f-3fe6-8c88-efac90bc88bf | -4.7686 | -47.5686 | 2025-06-19 01:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1af81f61-dad4-35be-b5e2-6b1bdbb7c5ba | -11.9709 | -58.7362 | 2025-06-19 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 05f63b0c-ca36-3b33-b3da-14324871e871 | -11.9518 | -58.7574 | 2025-06-19 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 229.9 |
| a212296f-1da9-3f98-8202-60bde3e7efdd | -11.952 | -58.7376 | 2025-06-19 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 60244879-db16-3ac2-af56-4d3e318cae3a | -11.9518 | -58.7574 | 2025-06-19 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 686fa57e-9f2d-3d3c-b416-594ebed2756e | -4.7872 | -47.5676 | 2025-06-19 01:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 82c42bdb-2097-394e-91df-22e3f7381ed2 | -8.1264 | -43.139 | 2025-06-19 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 4a732336-4099-34e0-bef9-874d3f16c330 | -11.952 | -58.7376 | 2025-06-19 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 57423541-e533-3c7e-9fe0-300c889a3be3 | -11.9707 | -58.756 | 2025-06-19 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 12a54be4-9e96-3387-8d44-283de312931d | -11.9329 | -58.7588 | 2025-06-19 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c72363c9-99e8-3f68-bb45-2c4eb38d93fc | -7.2405 | -43.0899 | 2025-06-19 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 229.1 |
| d83a831b-9173-365f-a04d-eea9eb0b4862 | -16.3047 | -58.2676 | 2025-06-19 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| c9f8125b-81e4-3f73-88e4-feb689f4784e | -10.0972 | -52.7376 | 2025-06-19 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6fe3fc53-1467-37ba-9c5b-c72185988d60 | -8.0703 | -43.0981 | 2025-06-19 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 4bbc4003-67f0-3504-b90e-449ea25ab5e4 | -11.9709 | -58.7362 | 2025-06-19 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 90d349dd-6f3a-3f60-94e5-1614159bafa7 | -16.305 | -58.2474 | 2025-06-19 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| b5177283-b86b-3e2b-8e9e-1ab44effafda | -7.2408 | -43.0664 | 2025-06-19 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 164.9 |
| a4bdbcbd-7370-38e9-afc8-dfc602d3a0d5 | -10.3065 | -57.133801 | 2025-06-19 01:37:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| baaf3f87-2e57-3468-a09e-2d866612c4aa | -16.318701 | -58.252499 | 2025-06-19 01:37:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d5af1e5-a37e-395c-99b4-f89aa0d33e8d | -11.9603 | -58.752602 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 297b460b-de49-3afd-b658-665e942dec5c | -10.0918 | -52.747398 | 2025-06-19 01:37:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b63c762-7355-3632-ad29-a5d5438f0d11 | -11.6209 | -58.286598 | 2025-06-19 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b754f897-4a68-30f4-9e3a-2c05d851b35c | -11.9428 | -58.7659 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30052972-20f9-3225-a73a-b4b708886fac | -11.9485 | -58.746399 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2231ab89-a41f-3562-b8e7-1d449df87e51 | -11.9408 | -58.757401 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbe73e4f-6d02-34e6-9710-86b4270263cd | -11.9721 | -58.758701 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbab9362-9b70-39fd-a58e-bdc56ef4abad | -11.9583 | -58.743999 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e938e094-0299-3030-95ee-2c48d0d8a85b | -16.320601 | -58.2607 | 2025-06-19 01:37:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae2abdbb-552b-3bfb-ab49-848b5905bc0a | -13.589 | -59.211399 | 2025-06-19 01:37:00 | METOP-C | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d014198-0350-31e2-b905-d8b6c0013fe2 | -12.2404 | -63.604099 | 2025-06-19 01:37:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1a9e8ba-4801-3332-a9b0-acc69605730c | -11.968 | -58.741699 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87f71c0a-e23e-3972-8b82-c65ee5152f81 | -11.9623 | -58.761101 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcebf26f-f38a-3b7e-9ba0-8bcc25eb3c7a | -11.97 | -58.750198 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39ec1e6f-d977-38d0-8992-0ce7e850d16d | -18.6616 | -55.750198 | 2025-06-19 01:37:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| db98a86e-52f0-3b7c-a8f2-ad133df4e3be | -16.308901 | -58.255001 | 2025-06-19 01:37:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54724a02-582c-3388-bc48-e86b1c671f0d | -16.312799 | -58.2714 | 2025-06-19 01:37:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c8f00c4-62a9-3b00-aa69-bde60894bbb5 | -13.5871 | -59.203499 | 2025-06-19 01:37:00 | METOP-C | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1eb5b03-3ac2-32e2-8534-2df67de30fb9 | -16.3069 | -58.246799 | 2025-06-19 01:37:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5184deca-79f7-3eba-8320-5c0559bc5a05 | -11.1347 | -53.941101 | 2025-06-19 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0b41383-6135-3eb7-bb54-88e4b6235f97 | -11.9505 | -58.755001 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b95415fb-7123-3556-802b-0a74a94e6b51 | -11.532 | -56.989399 | 2025-06-19 01:37:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb405b54-a9bb-3d39-9262-760bf0bea594 | -11.9525 | -58.7635 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b91dbbe8-8654-3b1c-9669-38759dd42cbd | -14.0338 | -55.120399 | 2025-06-19 01:37:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94028869-2fbb-376d-acbf-68594e30ec45 | -21.7918 | -52.7612 | 2025-06-19 01:37:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| debcb968-756b-3401-8904-c7b67c19a72b | -11.9562 | -58.7355 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f19f3297-6474-3882-8955-bdd1ca33de3d | -11.5347 | -57.000198 | 2025-06-19 01:37:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80136441-9907-3aaf-9dff-de54cc2e9760 | -11.966 | -58.733101 | 2025-06-19 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 400ba4bf-9a7f-3571-a9a1-c6d2f750f656 | -12.4817 | -58.4697 | 2025-06-19 01:37:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e9c161c-1b12-3462-8967-d268fe9209b0 | -16.310801 | -58.263199 | 2025-06-19 01:37:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README5.md)
