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
| bed6d421-ddeb-3913-baf7-1a8fedaf967b | -19.7784 | -48.3011 | 2025-06-20 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ed23a7b5-05eb-3c2c-8bde-8acdca4c1888 | -14.0404 | -53.3669 | 2025-06-20 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 6228fb81-29fa-31f5-bb99-2de537fa3b08 | -16.305 | -58.2474 | 2025-06-20 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 5042710a-c31b-38d7-bf73-5424274c3242 | -16.2852 | -58.2697 | 2025-06-20 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 4f58a9be-e6b7-376c-ab53-8d79f192246e | -19.7791 | -48.278 | 2025-06-20 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 159.7 |
| e8e99a9f-06cf-38c1-8967-9f51b63616c9 | -12.5046 | -58.3591 | 2025-06-20 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| aaf0c2aa-21ba-34cb-a6b3-8a3ca9f22845 | -11.9518 | -58.7574 | 2025-06-20 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d3b408b0-db8d-3161-b52a-fc1da06eb42f | -9.4994 | -56.0788 | 2025-06-20 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 8302fc61-1724-30df-a317-d91a50003620 | -21.6502 | -53.9667 | 2025-06-20 00:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 43583919-0c89-3fa1-bf91-4fa6a9c8281c | -9.4807 | -56.0801 | 2025-06-20 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 757f1c9c-6d97-3e76-9c18-bf1ee44ed42e | -16.3047 | -58.2676 | 2025-06-20 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 239.9 |
| ecebf208-04fb-38d9-8796-ab336469a9d8 | -7.2222 | -43.0447 | 2025-06-20 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| fda9313a-6962-31e9-b4fb-64e65c07fb0d | -7.2217 | -43.0917 | 2025-06-20 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.7 |
| eceb6cd1-f954-31dd-8603-0984ac6f35ed | -19.7587 | -48.2824 | 2025-06-20 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4eff2647-1c16-3eef-a97d-b298bbfe7320 | -9.4648 | -57.8449 | 2025-06-20 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5c06b3e9-7766-36c0-9d8c-39d7a0a54bd4 | -7.2219 | -43.0682 | 2025-06-20 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 360.9 |
| 918f1832-9563-3e50-a11e-78db01b2cccb | -11.952 | -58.7376 | 2025-06-20 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 30a780fa-3e95-3ffa-8ad8-fa4a6ca259d3 | -9.465 | -57.8252 | 2025-06-20 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a1549718-7b05-32ef-a356-88b8cbd55425 | -9.4461 | -57.8461 | 2025-06-20 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9603568b-c3f2-379f-bd4b-41fd688979ff | -16.305 | -58.2474 | 2025-06-20 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 9212cf92-75bc-3757-8c1e-b3cfd21badd7 | -9.465 | -57.8252 | 2025-06-20 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 10fb22fd-77e4-36c8-9716-b055b0ba41bc | -9.4807 | -56.0801 | 2025-06-20 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 78251a86-dba0-323c-955c-6694391382c4 | -9.4648 | -57.8449 | 2025-06-20 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2afabb26-f873-375c-af7d-faedebc6a1e4 | -19.7587 | -48.2824 | 2025-06-20 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 845b6e4c-1b27-3371-b054-03e2ce2f87b8 | -16.3047 | -58.2676 | 2025-06-20 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 261.6 |
| d44feccb-5e11-3af4-ad8f-2b227c46689a | -11.9518 | -58.7574 | 2025-06-20 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a40244f3-0796-3710-93f1-0882544f9d42 | -11.9056 | -51.7642 | 2025-06-20 01:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2435078d-1768-37b1-8ae6-376948911ccd | -7.2219 | -43.0682 | 2025-06-20 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 403.3 |
| 73a7c74f-b699-3181-9346-3994bf11c3d8 | -7.2031 | -43.0701 | 2025-06-20 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 9b69b837-e953-37de-8058-3bb73f24b422 | -7.2217 | -43.0917 | 2025-06-20 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| b047711d-5c33-36c1-875a-62153ea2e46e | -12.5046 | -58.3591 | 2025-06-20 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 16624433-62eb-3c6b-8208-c525083ec930 | -14.0404 | -53.3669 | 2025-06-20 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c315a41d-8b70-3ef4-a68c-111d556d729f | -19.7791 | -48.278 | 2025-06-20 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 164.9 |
| ea6245a3-7c11-317c-a9d5-bc07f6dbae2c | -21.6502 | -53.9667 | 2025-06-20 01:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 114.7 |
| e4384986-6df1-31c0-829a-d3571285f6b1 | -7.2222 | -43.0447 | 2025-06-20 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 73558fe4-cfb0-366b-b7ac-371e82f7ecf6 | -19.7784 | -48.3011 | 2025-06-20 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5c63fc0d-f035-3593-8ac9-4a342485da88 | -16.2852 | -58.2697 | 2025-06-20 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| eac30baa-eab6-3673-babf-19ba24d5941d | -11.952 | -58.7376 | 2025-06-20 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f1feb962-a32d-3d07-b929-146fdd9168ba | -9.4648 | -57.8449 | 2025-06-20 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 5a5f5261-cfa1-32ac-b6bc-060ceaa74df4 | -7.2217 | -43.0917 | 2025-06-20 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 4a3e5ece-7726-3cd9-a132-2a4d38246772 | -21.6496 | -53.9886 | 2025-06-20 01:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e464317c-98eb-3db7-9b56-9a2b4502bb8d | -16.305 | -58.2474 | 2025-06-20 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 0a11f0f6-7938-369d-a5dd-4996c33262a8 | -19.7791 | -48.278 | 2025-06-20 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 130.1 |
| b4ade2a6-c19d-39fc-b87c-9af0b2bf2c8e | -7.2222 | -43.0447 | 2025-06-20 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 820672e9-6f3b-3f5a-ab24-5235fabc0ec3 | -11.9518 | -58.7574 | 2025-06-20 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e72d96b1-dbf7-3758-b7a3-292cb8da38bc | -14.0404 | -53.3669 | 2025-06-20 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 230b6c44-7a17-332b-a7b4-d1a65eeb5b7b | -19.7587 | -48.2824 | 2025-06-20 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ab39f667-f5fa-3eaa-ad8b-4115456dc036 | -16.3242 | -58.2656 | 2025-06-20 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 53ecc469-8b27-373e-bcfc-97d4b00803fc | -12.5046 | -58.3591 | 2025-06-20 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e01b9dea-a169-31a0-9dc9-208761ddb781 | -16.3047 | -58.2676 | 2025-06-20 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 209.1 |
| a76f4b39-e94b-360a-9dd4-2a1be125ec02 | -11.9331 | -58.739 | 2025-06-20 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 3a7216d4-8655-3162-98f9-d5072cda1b79 | -21.6502 | -53.9667 | 2025-06-20 01:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5e355bb3-7592-3b53-9aee-8ea5301dee62 | -11.952 | -58.7376 | 2025-06-20 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| da1e5b26-ea66-3496-9908-a3a64581efab | -9.4461 | -57.8461 | 2025-06-20 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 47992a63-0224-36f2-8304-ba1f61266c13 | -7.2219 | -43.0682 | 2025-06-20 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 328.5 |
| 0615fe8a-601c-36af-8ab0-a4000d03f514 | -16.2852 | -58.2697 | 2025-06-20 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 0e0ec4a7-ad88-3461-934b-563deac10fd1 | -7.2031 | -43.0701 | 2025-06-20 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 5aff9ee9-3934-387f-9118-7684723aedb0 | -19.7784 | -48.3011 | 2025-06-20 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 02d9e997-c81a-3337-bdbf-8538b767249f | -9.4807 | -56.0801 | 2025-06-20 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 60f4b649-b6b5-3845-ab2d-a41493cd9e83 | -16.2852 | -58.2697 | 2025-06-20 01:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 5b075b74-c59a-387f-b8ac-4f8f84eb6f0d | -9.4648 | -57.8449 | 2025-06-20 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8670f84f-72ef-341e-9c8a-836e8ac99e03 | -19.7784 | -48.3011 | 2025-06-20 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 86be71bf-ade0-323d-bb44-37eab8b04c35 | -7.2219 | -43.0682 | 2025-06-20 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 326.2 |
| 02993a43-2884-3038-b7b0-b03f61f6bc72 | -19.7791 | -48.278 | 2025-06-20 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 9fee40fb-7281-3dfa-bc26-b7b23e0755ec | -7.2222 | -43.0447 | 2025-06-20 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 2f534ba5-4815-345f-9ccb-eb6be65ca772 | -19.7587 | -48.2824 | 2025-06-20 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1c9ea3af-d64a-31c2-b761-d05bcbfb6892 | -11.952 | -58.7376 | 2025-06-20 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| c44b389a-14c4-3fd9-9d93-7543830fafe8 | -14.0404 | -53.3669 | 2025-06-20 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 33ae7b5e-5bc5-3823-bb26-f6eadfbc7419 | -16.3047 | -58.2676 | 2025-06-20 01:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 207.3 |
| 139f2f73-5f57-36c6-ad62-1851c77ec9eb | -16.305 | -58.2474 | 2025-06-20 01:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 332ec78e-cc1c-316b-b74f-e12571edb402 | -7.2217 | -43.0917 | 2025-06-20 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| f1924978-060c-352f-a6bb-998c4dbe6ccc | -7.2031 | -43.0701 | 2025-06-20 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 4007083f-334f-3392-bd62-b5c2503ca613 | -11.9518 | -58.7574 | 2025-06-20 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ba9de654-7a26-3350-ba18-51a1d338ffda | -9.4461 | -57.8461 | 2025-06-20 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0a62b3f7-1fef-356f-851f-6f12f16a6f1f | -9.4807 | -56.0801 | 2025-06-20 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 730f63b5-9cad-3b54-8356-def492368e22 | -19.7587 | -48.2824 | 2025-06-20 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 735e91cd-dc69-339c-94f8-c7db66539cf9 | -7.2408 | -43.0664 | 2025-06-20 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 7d6e01ac-8748-36e4-af6e-fde7cd02c79c | -11.9518 | -58.7574 | 2025-06-20 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a959dd5e-9d51-3df8-b708-920d51d15b1d | -9.4807 | -56.0801 | 2025-06-20 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 78284662-f636-313e-ab59-b6bc97a9528a | -7.2217 | -43.0917 | 2025-06-20 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 1d701c7d-2545-3b42-a91a-67af0e65ce51 | -19.7784 | -48.3011 | 2025-06-20 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| be177263-c9a2-34ae-a53a-6f22b47442ce | -16.305 | -58.2474 | 2025-06-20 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 221b72a7-255e-3317-aee5-0bfc7982907a | -16.2852 | -58.2697 | 2025-06-20 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 6aabc9a6-bff4-3eb9-a6e8-b9ad3fcd19cf | -9.4994 | -56.0788 | 2025-06-20 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f44adb7c-3cc0-303a-a9ea-c8ccdb738100 | -7.2219 | -43.0682 | 2025-06-20 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 232.3 |
| f8d24f98-bb5b-3eae-a0a8-5dd4dd7904e4 | -9.4648 | -57.8449 | 2025-06-20 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| dd88a3cc-b36d-3cf5-ba7d-cd47e2420e70 | -11.1274 | -46.6598 | 2025-06-20 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 6dded1ef-3b6a-303d-a715-0c43ce15b20b | -16.3242 | -58.2656 | 2025-06-20 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| ced20e14-b902-374e-b70f-d5b08a146b44 | -19.7791 | -48.278 | 2025-06-20 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 137.9 |
| d41f8057-8bc6-3b08-954c-2366a2f4a2cb | -16.3047 | -58.2676 | 2025-06-20 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.7 |
| 55036f88-9f81-34e1-8e94-6a1a7950af71 | -7.2031 | -43.0701 | 2025-06-20 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 4ab2c4b0-61d9-3c83-ae08-9115faf44cab | -14.0404 | -53.3669 | 2025-06-20 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 37d77af7-d668-30c1-9a54-be1e5b95a79f | -11.952 | -58.7376 | 2025-06-20 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 66d3ca4b-c3e6-3dee-95ce-cdf9547b8dbe | -19.7587 | -48.2824 | 2025-06-20 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a017c38c-5bd9-3aaf-a366-15d0265fd179 | -7.2219 | -43.0682 | 2025-06-20 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 261.6 |
| 5f8565b9-d343-3b50-9160-9bf7eb3a5936 | -16.305 | -58.2474 | 2025-06-20 01:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| ede341a1-45de-3eac-96f0-b794fb19b22d | -19.7791 | -48.278 | 2025-06-20 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e98bc323-f5c1-3d55-9568-453df6382e3e | -16.2852 | -58.2697 | 2025-06-20 01:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 75ae4269-b248-3640-9bae-ed490e699729 | -16.3047 | -58.2676 | 2025-06-20 01:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.6 |
| 363b64d7-f854-36a3-844c-eeac71984c05 | -9.4807 | -56.0801 | 2025-06-20 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |


[Clique aqui para ver as próximas entradas](README5.md)
