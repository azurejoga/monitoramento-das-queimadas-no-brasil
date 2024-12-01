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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d30102a-bc2c-3f21-a4b4-deb53d00ca3d | -4.899 | -47.1478 | 2024-12-01 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83c65cdc-d23b-308d-a6a1-163825b135b8 | -4.3198 | -48.084702 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06fe745-33fb-3dcd-835c-0451a9dc7f2e | -2.7704 | -55.3316 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72826180-1857-317c-a3bd-4c07315a4f7c | -4.5348 | -45.708 | 2024-12-01 00:38:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 963b061d-18ba-33b9-97d4-e24664d52260 | -4.268 | -48.354198 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b53206-2493-3180-8c3e-c5a3f3a5c9f2 | -1.6954 | -46.1426 | 2024-12-01 00:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c2887681-da08-3a37-b423-1b7f630dae76 | -2.8491 | -49.8763 | 2024-12-01 00:40:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 62ad6b4f-958a-3d17-a4b2-58b058cb8346 | -3.4755 | -50.2566 | 2024-12-01 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 47a93c0e-cb1f-3ff0-966b-8d9c0907ecda | -4.558 | -45.7008 | 2024-12-01 00:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 8dd789b4-92fc-312a-ab65-efc72fa16369 | -6.9158 | -43.5185 | 2024-12-01 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f982104a-3af2-3fc3-9ac6-2aa248f38c5f | -4.5578 | -45.7232 | 2024-12-01 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 701fc06d-479e-3902-813a-d74cf952ad8c | -3.457 | -50.2572 | 2024-12-01 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b5daf80e-4336-3695-aa00-40b44f11daa2 | -2.1535 | -54.8659 | 2024-12-01 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9d3c3431-9ae2-3027-b29b-897ea9cd7f43 | -2.1535 | -54.8858 | 2024-12-01 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| eca3885f-4e0a-3f34-bcf2-11011081914c | -4.5562 | -43.3028 | 2024-12-01 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 116cbfe2-c8f3-3bc7-ba30-68bfa39903cf | -4.8899 | -41.3143 | 2024-12-01 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 9211fe1e-b66b-3605-8038-b3542161b369 | -3.259 | -53.6388 | 2024-12-01 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 8d8cdeae-d0af-3140-954d-4646a26e701d | -3.4569 | -50.2782 | 2024-12-01 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| b5629552-4c1a-3e82-872b-d616f6d9146c | -3.1273 | -54.5264 | 2024-12-01 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 1382d32e-3c93-31e6-9739-fa8f77c19f16 | -6.9156 | -43.5418 | 2024-12-01 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 282.4 |
| 0e390797-4f19-3540-8aa9-f8a0e4143229 | -4.5375 | -43.304 | 2024-12-01 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1cbac65c-bd30-34d7-8eb7-623515ceda7b | -2.8013 | -53.043 | 2024-12-01 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b4880513-b24e-391a-bc7d-3ccdaf0eff5a | -3.1456 | -54.5259 | 2024-12-01 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d4f5dcba-81fe-377b-b0a4-95b882f24c61 | -3.2057 | -53.1341 | 2024-12-01 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 07b91b0b-0d23-3270-80e5-d29f0e819e31 | -2.6578 | -51.8811 | 2024-12-01 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 525872ed-bd6b-3467-9bb7-32904272d0ea | -2.6068 | -45.4269 | 2024-12-01 00:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| be1a6ac7-1bd9-3ab5-bd44-c4f14fc30e1c | -3.0081 | -51.7897 | 2024-12-01 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a4ae375d-50e7-3556-a71d-fc2fe3c1b3fb | -3.4974 | -53.8339 | 2024-12-01 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 769e8a1b-2b94-3780-bcfb-899e613ba080 | -4.5392 | -45.7243 | 2024-12-01 00:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 08fb8fb5-bf45-38db-9826-94b92be09889 | -6.9344 | -43.5401 | 2024-12-01 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 445.2 |
| aa1ab3b7-8c1a-3282-a96a-cf9e480f4334 | -6.9153 | -43.5652 | 2024-12-01 00:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bdaa2d75-69db-3d79-a5f4-21df506e8a1f | -6.9341 | -43.5634 | 2024-12-01 00:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 19e85ddb-6964-34b9-8926-ee301b97a59e | -3.4754 | -50.2776 | 2024-12-01 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| e38e5372-a9bb-3b65-9b58-f2eaeb5c8fbd | -6.9346 | -43.5168 | 2024-12-01 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| e9192b4b-8edc-3d72-b8f7-a75cb66ae1b9 | -2.8197 | -53.0425 | 2024-12-01 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| fdac1a45-152e-3e66-acd5-10bf126bb42c | -3.2058 | -53.1138 | 2024-12-01 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e4cd371a-f21b-3427-85f1-3dbc187d047f | -2.1215 | -46.2439 | 2024-12-01 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 00ef15e0-64a4-309c-a113-ce5bfff995ab | -2.7503 | -51.7553 | 2024-12-01 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 0ada9c94-6fc9-3528-ab4b-6755815a2f63 | -4.556 | -43.3261 | 2024-12-01 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b909f1cf-2f56-3aa4-9293-cae6d96e81ee | -3.2591 | -53.6186 | 2024-12-01 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| ae1a712d-c650-3dd0-aeaf-6633d78d9b2f | -3.3134 | -53.8592 | 2024-12-01 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 02948e05-19f3-3574-be6b-7b3e48f0a708 | -4.5394 | -45.7019 | 2024-12-01 00:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 9bb5ed6f-b0c6-3ae6-b9ac-ad35732fd6b2 | -3.5158 | -53.8333 | 2024-12-01 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4f49ccb5-c62b-3ac7-8f32-fda8e21c8908 | -2.6579 | -51.8606 | 2024-12-01 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ee1957e2-0e76-3778-992b-b21c74ac8df3 | -3.69 | -51.8101 | 2024-12-01 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 1c430589-a027-3854-9bc1-b5f645211dc3 | -3.2774 | -53.6383 | 2024-12-01 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| f29fb5d4-0772-36bf-873b-501bed9e8474 | -2.3376 | -54.6034 | 2024-12-01 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 50981171-645a-366a-b4d6-fd66f227395d | -4.5563 | -43.2795 | 2024-12-01 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 62b8213f-30f0-3b6d-acf7-fb51e950390b | -3.0081 | -51.7897 | 2024-12-01 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fd6be366-fc06-34f4-8dcd-f106d0a0a810 | -6.9346 | -43.5168 | 2024-12-01 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4d8d5e18-70e7-3581-9f62-2d97438d5ae0 | -2.8197 | -53.0425 | 2024-12-01 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 88251926-3b22-39a0-bf5d-4659bbc0a6c7 | -3.457 | -50.2572 | 2024-12-01 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| e4e9838d-4b20-37e9-a452-21b73fbcc6c7 | -3.259 | -53.6388 | 2024-12-01 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 57b1c9ed-d39a-3271-82ff-0f2e161ef013 | -2.8012 | -53.0633 | 2024-12-01 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6866ab3c-9268-33a5-ab03-2b8945ef4d61 | -6.9158 | -43.5185 | 2024-12-01 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 10bd0039-e944-3825-9517-678e775bfb2c | -2.7503 | -51.7553 | 2024-12-01 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e33d5cfb-83f3-3a3d-a193-afc0ac00edfb | -4.5394 | -45.7019 | 2024-12-01 00:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 130.5 |
| a50a897c-92dc-3373-9e56-3c93fcecbdc2 | -2.6578 | -51.8811 | 2024-12-01 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 719fab83-0ef6-339d-878c-eaf8809b5fc5 | -3.1272 | -54.5464 | 2024-12-01 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e163adcb-8cbc-34d2-a169-4d59ef49094a | -2.8013 | -53.043 | 2024-12-01 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c617922a-6518-399a-8ea3-e950a63ac21d | -4.5578 | -45.7232 | 2024-12-01 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 175.7 |
| b1126636-78c0-3a71-9f16-89665e68d287 | -6.9344 | -43.5401 | 2024-12-01 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 311.8 |
| 1322bba3-0d35-3144-bbf1-ac0692265101 | -4.9087 | -41.313 | 2024-12-01 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| f04d659b-7644-3301-b330-ff76a98bfa93 | -2.5504 | -45.608 | 2024-12-01 00:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c52fb135-e587-3666-8d38-5089e8a52a6f | -4.558 | -45.7008 | 2024-12-01 00:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 648a4c8a-7517-33cd-a6a0-1506f88a8be8 | -3.2591 | -53.6186 | 2024-12-01 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 9495a09c-7916-3fbf-a199-b56730555811 | -3.4569 | -50.2782 | 2024-12-01 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 83dd27d1-9ebb-3d35-bed8-70944c9aa692 | -3.4755 | -50.2566 | 2024-12-01 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| e17dcdc0-78f4-358d-8951-058a81f807ac | -4.556 | -43.3261 | 2024-12-01 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 372c7414-e4a4-3916-902b-7f84b4d551e9 | -4.5562 | -43.3028 | 2024-12-01 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 73e54bd5-1548-39f7-9de3-04483fe36785 | -4.5375 | -43.304 | 2024-12-01 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| db25b975-1be3-397e-a86d-badc574a2a0d | -1.6954 | -46.1426 | 2024-12-01 00:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 49588ecc-2e36-323a-8e08-00f12e7afa34 | -4.5563 | -43.2795 | 2024-12-01 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c0837ca3-fc4c-314b-b052-1406cf0e197b | -3.2774 | -53.6383 | 2024-12-01 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e1b9a825-c4ac-3164-aa1e-de1d89379199 | -4.8899 | -41.3143 | 2024-12-01 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 6d29accc-2714-3973-aad8-2cc2656da880 | -3.4974 | -53.8339 | 2024-12-01 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 2f9f6857-c83f-37ea-ad6f-314d6f82b754 | -2.8491 | -49.8763 | 2024-12-01 00:50:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9ed869ca-e338-37d1-a9b0-0b0c17fce2ea | -2.0988 | -47.6271 | 2024-12-01 00:50:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4f9504e4-f1ed-3fea-95d0-30c914766f38 | -6.9153 | -43.5652 | 2024-12-01 00:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 72911e92-b8dc-315f-ae8f-5fa305cc6fc6 | -3.5158 | -53.8333 | 2024-12-01 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 74fa62cb-7496-368b-af6b-2c291ad79625 | -3.1273 | -54.5264 | 2024-12-01 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 0e40fc40-3e4c-35a0-ba24-fbd43683c0c1 | -4.5749 | -43.3017 | 2024-12-01 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 03a3169a-c98a-3889-b792-9c95e8e9fa1d | -1.7139 | -46.1422 | 2024-12-01 00:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| d4d417cd-8e91-3f85-8c9f-974937fda95b | -2.1215 | -46.2439 | 2024-12-01 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 32689d09-58a7-337d-9622-04ccbab05aab | -6.9156 | -43.5418 | 2024-12-01 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 191a3d3f-733e-3de5-bbe8-ed20f45fa4bf | -6.9341 | -43.5634 | 2024-12-01 00:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 36e5bf51-77cf-3ff2-8cec-3fdf3679880d | -3.69 | -51.8101 | 2024-12-01 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4fbe0c83-557f-3410-942d-76507930c60b | -3.4754 | -50.2776 | 2024-12-01 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 2db0a59f-3881-327c-b8bf-22dba938cc3e | -3.4974 | -53.8339 | 2024-12-01 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| fd65aa3d-5255-384e-be36-13e334b64208 | -4.8899 | -41.3143 | 2024-12-01 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 6c0a169e-cf86-3702-9967-a88222144d28 | -4.9087 | -41.313 | 2024-12-01 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 6a1bd798-68c7-3f4c-b0a2-fbcba95e01de | -1.6954 | -46.1426 | 2024-12-01 01:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 6f655b14-131d-3b47-b5d7-7c8585add419 | -4.5578 | -45.7232 | 2024-12-01 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 85ddd652-fcc6-3c58-83be-1218e06ea1f6 | -3.4754 | -50.2776 | 2024-12-01 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| ebc6277b-572c-3b9b-a091-f040187bfb34 | -3.4569 | -50.2782 | 2024-12-01 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0c1404e0-20cc-3ac9-a053-662d3e8b9c69 | -3.0081 | -51.7897 | 2024-12-01 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1de11567-dcb5-3af4-85d3-565740d4d6f5 | -2.7503 | -51.7553 | 2024-12-01 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7951c7f8-427f-3941-b6a5-e992c12e25f2 | -4.558 | -45.7008 | 2024-12-01 01:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f0853c63-ec88-37ec-9e51-6bcf76e03e45 | -6.9156 | -43.5418 | 2024-12-01 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 278.3 |
| b9802e23-d965-3e1b-b817-e9e0a4c213eb | -1.7139 | -46.1422 | 2024-12-01 01:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |


[Clique aqui para ver as próximas entradas](README15.md)
