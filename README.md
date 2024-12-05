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
| b8258ae6-17d0-31d6-912e-188ef28f1257 | -2.1541 | -54.6266 | 2024-12-05 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ae04c1d6-cdb7-300c-b304-904cd1d876bf | -6.9156 | -43.5418 | 2024-12-05 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 602219a2-d73a-3d4f-8c0e-f6d5fc6930a3 | -6.9346 | -43.5168 | 2024-12-05 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| cb4f99bc-7ffa-3746-9238-21aa2574b31d | -1.5487 | -45.4313 | 2024-12-05 00:00:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 15972abd-a9c6-3394-9242-2761805b0a63 | -3.1191 | -51.6628 | 2024-12-05 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 0efaea3b-ff5d-3619-ad8c-1d70d46c946e | -6.9344 | -43.5401 | 2024-12-05 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| a65ccc43-1747-3c00-9ab5-3f3b568950cf | -2.4319 | -53.6584 | 2024-12-05 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d425a6fb-c44e-3438-9e84-0b3ad77a0528 | -3.3276 | -50.2825 | 2024-12-05 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4710929c-d41a-3a92-bfa4-97112316999b | -6.9341 | -43.5634 | 2024-12-05 00:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c22a07f1-ac99-3ca2-a559-4c874ba3f308 | -2.1724 | -54.6263 | 2024-12-05 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 511a8a38-255a-3821-97de-7d1355ca8a7d | -1.5103 | -46.035 | 2024-12-05 00:00:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7ecf9e2e-d309-3600-b944-09efe5a0ac35 | -9.374 | -57.5553 | 2024-12-05 00:00:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e42f88ff-d256-3387-af76-f17bec875acd | -2.9897 | -51.7902 | 2024-12-05 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8bbe8ac2-5ae9-37a4-9d39-0812aa2f69e4 | -3.5676 | -54.6946 | 2024-12-05 00:10:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 96668615-2195-3a71-973c-1aaedabdeafb | -6.9346 | -43.5168 | 2024-12-05 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| b193523f-08ed-3325-b1a1-7adee9de50fc | -2.9897 | -51.7696 | 2024-12-05 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| dece77c3-a229-3022-bf52-abd3024bbb78 | -4.0 | -48.9012 | 2024-12-05 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0a863220-665d-3f78-8b3f-5ebd43cbd552 | -3.586 | -54.6941 | 2024-12-05 00:10:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a642fd0d-1df6-3352-a51f-252c15f3ff13 | -4.0343 | -49.4115 | 2024-12-05 00:10:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| cd21f4d6-ae83-3158-bba2-6bc339fb8b7b | -2.9712 | -51.7907 | 2024-12-05 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| cc7b5cde-9e86-353c-a6ac-60d2bfdc2fbb | -6.9344 | -43.5401 | 2024-12-05 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 52797b96-cd61-3082-9a3d-e2e19acb9115 | -3.9999 | -48.9226 | 2024-12-05 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 01660005-b2e0-302b-8ae7-81244f02a72b | -6.9341 | -43.5634 | 2024-12-05 00:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 80c92126-7e64-3450-bbb1-f3f6a0303605 | -2.1541 | -54.6266 | 2024-12-05 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 20caf97d-0791-3fe7-966c-a0e2ea0256bf | -2.1724 | -54.6263 | 2024-12-05 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1905dfb6-ba0c-3497-a187-ce3224dccf0c | -6.9156 | -43.5418 | 2024-12-05 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5442e47b-69cd-33e2-b9ba-b21de315c2eb | -4.0342 | -49.4327 | 2024-12-05 00:10:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| eb51b6b5-5598-3a65-8bf2-6a016a3189d6 | -9.374 | -57.5553 | 2024-12-05 00:10:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4b760aa4-6a22-3331-a9eb-69a74483afa9 | -4.0184 | -48.9218 | 2024-12-05 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 31a1c4f4-653d-3120-9988-17f4297ce5f1 | -2.1724 | -54.6263 | 2024-12-05 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4882df37-e483-35e6-af16-96772085b51a | -4.0343 | -49.4115 | 2024-12-05 00:20:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1a597acf-d13c-3729-92b6-afda869ae1a7 | -6.9341 | -43.5634 | 2024-12-05 00:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 39ff8a85-4041-3578-9fd6-318c9347e172 | -6.9156 | -43.5418 | 2024-12-05 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4886a6ca-1cdb-3a51-9ca5-6ef03ab2b9d1 | -6.9346 | -43.5168 | 2024-12-05 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| b9231dc7-d222-3931-b249-a4402ad93019 | -2.1541 | -54.6266 | 2024-12-05 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| fa43d22c-a61f-364e-9c2a-8b10f7883d7e | -2.9712 | -51.7907 | 2024-12-05 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b5a1a792-3cd8-38b9-a208-c0b89574b35e | -9.374 | -57.5553 | 2024-12-05 00:20:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 4de8cd9c-2b8e-3721-89c5-37efb3156a37 | -2.7544 | -45.691 | 2024-12-05 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ffd6ca1a-54c3-35b8-a077-4caa12362a00 | -4.0184 | -48.9218 | 2024-12-05 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f2358ba3-12b5-39d3-9496-2e45cf8ccd7b | -3.9999 | -48.9226 | 2024-12-05 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d33bc20e-6dfb-3a07-81ea-7ac99fc8f685 | -2.7543 | -45.7134 | 2024-12-05 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| c5d4e446-42a8-36a3-8f79-e93a4a931e6c | -6.9344 | -43.5401 | 2024-12-05 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 185.6 |
| b505af4a-10f4-3782-8693-7ca49d2ddbdf | -4.0342 | -49.4327 | 2024-12-05 00:20:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| cf5fcb35-69de-39c4-8ca4-f70b5bd524c6 | -4.6469 | -46.3206 | 2024-12-05 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d30fcc4b-f83b-3925-b69f-33e7390ff490 | -6.9156 | -43.5418 | 2024-12-05 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 21e71b7a-dacd-36ba-a890-a2fa55eac7dd | -2.1724 | -54.6263 | 2024-12-05 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7831a85b-3b2a-3fc8-a34f-c641806209fe | -9.374 | -57.5553 | 2024-12-05 00:30:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 92a29527-3cdc-39c6-802a-3cb5d4c653fe | -6.9344 | -43.5401 | 2024-12-05 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 0a8882e9-c781-3ce1-b7dc-a98164900b7e | -2.1541 | -54.6266 | 2024-12-05 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 65f765bb-6f2e-3146-95cc-dac3fad2e1cc | -2.9897 | -51.7902 | 2024-12-05 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 472ccb93-2511-3515-823c-ad8d3b4282bc | -6.9346 | -43.5168 | 2024-12-05 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dab6dc6c-44e7-377a-9347-236ef3a55818 | -2.1541 | -54.6066 | 2024-12-05 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ff7f05de-f44c-388a-b815-aec57c03e685 | -10.178 | -36.4313 | 2024-12-05 00:30:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| cf7bcea6-1c93-3e34-b7ab-1a6021a2275d | -2.879 | -51.8138 | 2024-12-05 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| fa024ae7-5761-38d3-b249-e9b916786fdd | -2.1724 | -54.6263 | 2024-12-05 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 3d6cee2c-158e-3ade-b3b2-d794e76c65a2 | -6.9344 | -43.5401 | 2024-12-05 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 2f9e2a67-d46a-34a0-955d-566f99a520ff | -2.2668 | -53.5405 | 2024-12-05 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| da0f1a5e-5f76-326f-a5e8-3bada6b59f8d | -6.9156 | -43.5418 | 2024-12-05 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6d66599b-d9af-356b-a7d3-6b83491fa33a | -1.6993 | -52.6168 | 2024-12-05 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f81a3dfb-4bd1-30ef-9077-6f3705d0ef8e | -6.9346 | -43.5168 | 2024-12-05 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6385db3e-8f07-389f-8f57-aad76ef802b9 | -2.1541 | -54.6266 | 2024-12-05 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 86fa8409-2013-37ed-bcde-9b92274c46b7 | -2.7177 | -45.5803 | 2024-12-05 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 977380f2-c4a5-3f54-ab15-28a285d78328 | -3.9013 | -50.0938 | 2024-12-05 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b4ca100c-f242-3c3b-abaf-8b02078e9f9d | -4.0 | -48.9012 | 2024-12-05 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 11a629f8-1d1f-3f31-a3a0-5ae1ea8e5b67 | -2.1724 | -54.6263 | 2024-12-05 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3baeb4bb-94bc-3e69-b14a-1e536c159e4a | -6.9156 | -43.5418 | 2024-12-05 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e2b44aa3-7b92-3504-b768-d8c616e73b0e | -1.4401 | -53.8153 | 2024-12-05 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0295182d-c92c-3239-b47c-2ba53ee9027a | -1.51 | -46.1461 | 2024-12-05 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d735d043-1ea0-3f38-afcb-5f4935cb3d9b | -3.9999 | -48.9226 | 2024-12-05 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| bee203ef-cd47-3886-988b-45e8b3a947f9 | -2.7544 | -45.691 | 2024-12-05 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1ec1eb5e-6cc5-3bce-932d-aca633689cda | -3.1191 | -51.6628 | 2024-12-05 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dd3dbb9e-e108-3e58-ac33-e9d54e6439d9 | -2.7362 | -45.5797 | 2024-12-05 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5965bb29-6a61-360b-86e4-0314ec9ede2d | -6.9344 | -43.5401 | 2024-12-05 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 2dfd79a4-0049-3a2a-ae86-ae73233d96b9 | -2.7543 | -45.7134 | 2024-12-05 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f671f9ac-d161-3d0d-b5d6-b988d1729ee3 | -2.1541 | -54.6266 | 2024-12-05 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f4ce321b-413b-3004-b455-fa69082d8d4b | -6.9346 | -43.5168 | 2024-12-05 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 04bcd866-be83-3146-991b-c9a73dd8ba6e | -2.7362 | -45.6021 | 2024-12-05 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 06092eb4-6861-396c-803f-c3bc553b758e | -3.1243 | -51.660198 | 2024-12-05 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88d91e1-a794-3e28-a656-8e2787f9a70a | -11.768 | -54.685902 | 2024-12-05 00:54:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2779c02a-7c33-3562-916d-a13cefd42f36 | -3.3092 | -51.567299 | 2024-12-05 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 866a552e-3bcd-3aa3-9056-bd95e79fdede | -2.5772 | -53.682301 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd7ffee1-d925-343e-94d5-9373ac62f257 | -2.2197 | -53.696701 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057b46c9-5bae-3531-aa66-a18efd03815e | -1.6996 | -52.328899 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88b6f2e6-d8d8-3fd8-9f74-d2800eaf4dde | -2.4288 | -53.6647 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08ef17ea-8129-3f7b-b36c-49110366fa0b | -1.8738 | -46.3806 | 2024-12-05 00:54:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0207d89-62c5-32bd-8323-ba98c90115cc | -3.4956 | -49.9212 | 2024-12-05 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b576b9bc-cc73-387b-b21c-a1ec9c8a8612 | -3.1145 | -51.662399 | 2024-12-05 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a94a6bd-755d-3871-a28b-b1405146f6df | -1.3875 | -53.6661 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf80d28b-20b0-3a49-bb4d-686be6c4bd3f | -1.6473 | -52.1012 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 502d9849-f949-382c-829c-6c3687c487b8 | -3.1161 | -51.669399 | 2024-12-05 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1acb503a-a665-3d13-943f-cd46c2584e68 | -3.1129 | -51.655499 | 2024-12-05 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d6f952-9713-3b38-81b4-c98229f9ab1b | -1.5778 | -52.247601 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad02efb-32d9-3015-9eac-20d6b52a42bb | -2.7521 | -45.707298 | 2024-12-05 00:54:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26379693-ce27-3d9a-a288-7a57868d57ee | -3.9941 | -48.919102 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb6318e3-7600-34b7-8bf1-d9aa24fcf461 | -3.9961 | -48.927799 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb25b8d1-502b-30cc-8c35-67063cd3912c | -1.7003 | -52.7813 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5198a617-cefb-3b7e-8f81-4913bf430a72 | -1.7019 | -52.788101 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6538fe-2343-3ae3-9b8c-21f66ea9cc63 | -3.992 | -48.9104 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4b150a-bf16-36e9-8e4f-363856d4559b | -1.8921 | -52.852798 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ddd8395-6221-3869-9e19-11af5cff31ab | 2.4301 | -60.6376 | 2024-12-05 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
