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
| 5f041f24-5091-3275-bb3e-695cfbe828a8 | -17.2933 | -57.4857 | 2024-11-11 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.0 |
| d0e4ea4b-f4ae-3eb2-9c5c-a57d998c7766 | -3.0323 | -45.8377 | 2024-11-11 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 34d6956e-9202-3cf5-9b1e-04faca5f4784 | -3.1423 | -50.4352 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6d072ce1-09ad-3c3e-9d05-af15073983b8 | -3.2428 | -53.0519 | 2024-11-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| bc96a615-6375-3be1-83c0-9412e0f5a4ab | -3.2588 | -53.6994 | 2024-11-11 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 51b69182-d3a8-3f6e-9ddf-4428778f973c | -15.9982 | -59.3649 | 2024-11-11 00:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 90f56ad3-e0b1-3f9f-b034-5836f37a6e77 | -2.8508 | -49.4108 | 2024-11-11 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| ffbf99e6-1199-3d13-9513-34ec7f954502 | -2.2504 | -46.5282 | 2024-11-11 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a69656c7-e8dc-34b4-92d7-8fc3eeb7d3e4 | -1.2018 | -53.6366 | 2024-11-11 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1a9f9d23-432e-38bb-bb24-797cb0419074 | -17.2936 | -57.4652 | 2024-11-11 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 7eb5e4a6-aff3-38dd-8883-87c543c0e9b8 | -3.6032 | -50.5876 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2cbf6da0-9149-30fd-9d57-9de0297b7bab | -2.8324 | -49.4113 | 2024-11-11 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 87136c6a-bed1-3ec0-8c47-142ff0e6676f | -3.3403 | -51.6563 | 2024-11-11 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 05c6d4ef-920b-35fc-bfe5-5ed3d9f3f9ee | -17.6083 | -57.4482 | 2024-11-11 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 1b7868e1-2f80-37a1-81ec-dcf1cef758cf | -1.5164 | -52.1491 | 2024-11-11 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ee344cee-4f33-329f-a017-461e0d981655 | -3.0111 | -50.982 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 38f73658-7f69-3228-9e98-48c20259670c | -3.6033 | -50.5667 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d4c84e72-ef30-3689-9bca-b71fb3a4578e | -4.1101 | -49.0888 | 2024-11-11 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 47af9f27-933e-3a25-87a6-a7be94c3f49d | -4.1246 | -43.5833 | 2024-11-11 00:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 195050f3-2389-36f1-8aae-933f12a4853d | -3.5346 | -45.7061 | 2024-11-11 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 117.2 |
| d7372eae-3204-3479-ac0a-687f08967be7 | -4.0293 | -46.9703 | 2024-11-11 00:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7155164a-2e54-363a-b165-e1ab982c7b62 | -3.2168 | -50.2861 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9ecdbefe-7837-3a58-96a6-2abecf3f0119 | -17.5889 | -57.43 | 2024-11-11 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.2 |
| a6aec627-2921-325a-aeae-e5c5e1141c77 | -3.1458 | -54.4859 | 2024-11-11 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| f7821b0e-4462-3573-a85c-735a8eac8722 | -1.4057 | -52.3758 | 2024-11-11 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 4e173771-6fe9-3478-a26f-4e32c24edc55 | -2.9355 | -51.482 | 2024-11-11 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 608e673e-6257-3f4a-baed-4f4bed37a410 | -2.8323 | -49.4325 | 2024-11-11 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| f1f39b1c-2e8f-31d6-8809-9f87c86253df | -2.4504 | -47.6399 | 2024-11-11 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 3f3fa525-5f8b-3218-8552-f0dfaa29e06a | -3.6218 | -50.5661 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 51481bb1-172c-33fb-be7b-a73c1fc410f1 | -2.4319 | -47.6404 | 2024-11-11 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 89084b75-c75c-3de4-9d6b-435dae13d70f | -3.1274 | -54.4864 | 2024-11-11 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5f28915b-884d-33f2-a79a-130b55316179 | -2.9766 | -45.8397 | 2024-11-11 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6094c00c-4840-3024-bb49-3e05d42e6030 | -3.1983 | -50.2867 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a4626a7e-c7e9-3f31-9d9e-0ad371514fe4 | -15.9985 | -59.3449 | 2024-11-11 00:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 2e63234b-b04a-32bd-be72-a24b3c1c6b15 | -3.0214 | -53.2404 | 2024-11-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 1d630a04-6935-3dec-ace8-5b0ec244a77a | -3.0296 | -50.9607 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 840b2952-babc-3031-8471-f5b3a464374e | -15.9791 | -59.3468 | 2024-11-11 00:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 1c30ef28-01bf-3a01-973e-1cbcb1e36150 | -3.1641 | -54.4854 | 2024-11-11 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fe1e07a5-f0be-342d-a8db-6f474889c12d | -2.3863 | -50.3299 | 2024-11-11 00:00:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e41e675f-bb5c-31e5-af77-3348c5ddbd0e | -2.9901 | -46.9901 | 2024-11-11 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 1cb330fc-4dc0-3b5a-b365-36c738e21704 | -3.4021 | -50.1329 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9cf52477-5f89-3901-b2ca-89a2022f2871 | -3.0324 | -45.8154 | 2024-11-11 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 7a43c1de-3909-3d10-9295-0f31fa84854a | -4.085 | -43.9319 | 2024-11-11 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bf522168-1baa-3d5c-a7aa-8a7e3d69d791 | -15.9788 | -59.3668 | 2024-11-11 00:00:00 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| d09c10b6-ff4f-3993-a01a-fff8359844ec | -5.0997 | -45.5344 | 2024-11-11 00:00:00 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| fc6c78b6-340b-3a47-a250-27e98f49d5ee | -5.081 | -45.5355 | 2024-11-11 00:00:00 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 1659e39a-99a4-3dd4-92d9-11597045a500 | -2.4367 | -51.948 | 2024-11-11 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 20b0a699-1f67-3d38-bf6b-2485f1cf7e0e | -1.2018 | -53.6164 | 2024-11-11 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4f761d80-ecff-3780-9ee6-32a319fa0ba3 | -2.6031 | -51.7177 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c9ee6d43-46cc-3861-a20c-099b3ed258fb | -2.189 | -48.3815 | 2024-11-11 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 515a0382-055b-32ca-ae9d-eccc687ac60f | -4.11 | -49.1102 | 2024-11-11 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 78987f0b-3b6f-39ca-87de-3f41be58a44a | -3.0295 | -50.9815 | 2024-11-11 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 207.5 |
| e5fe46f8-6b98-32f8-b50c-44add51f1b4e | -3.3836 | -50.1336 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2a3bd62b-8a73-3428-8473-d75c69f90fc2 | -1.2201 | -53.6364 | 2024-11-11 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 7a6e60c6-aeae-3c01-9a94-fe73c2c72483 | -3.1458 | -54.4659 | 2024-11-11 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 33667084-6eab-3fb4-a82c-20ef9f134b46 | -17.2737 | -57.488 | 2024-11-11 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 6a5e8c58-7bce-3e85-8bf3-72516311f9dd | -3.2427 | -53.0722 | 2024-11-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9c869036-a803-3cf1-96cb-13766a0576a1 | -3.6789 | -50.2074 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 07f571e4-7044-31fe-b2a8-a5e0589a4854 | -3.2948 | -45.3346 | 2024-11-11 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 833603be-dda9-3cbd-9f80-100e61105d77 | -3.6954 | -50.6262 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 45a3d58a-ea23-369e-b7ef-5e88cf31167c | -2.8508 | -49.432 | 2024-11-11 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 996263cf-8b37-3c61-bde9-4fda8662830b | -5.8216 | -44.1196 | 2024-11-11 00:00:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 45f39fa5-efe9-318e-a674-54975d42418d | -17.6086 | -57.4276 | 2024-11-11 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.3 |
| 6c59cc43-5b44-3438-b779-e04e46ea2763 | -3.6217 | -50.587 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 07c982d4-d5ae-35b4-bf85-401b9aa9a98d | -4.0294 | -46.9484 | 2024-11-11 00:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6d45416b-4ea9-3b89-9644-3ca73912f8bc | -3.2949 | -45.312 | 2024-11-11 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 1f741777-834a-3b1a-b153-cca452d79b0a | -5.9119 | -44.4802 | 2024-11-11 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 12140355-35c5-3829-952c-233ca2b7ba44 | -2.2504 | -46.5061 | 2024-11-11 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 24341b12-b6c5-3400-ba62-4d4024b624f9 | -3.2773 | -53.6787 | 2024-11-11 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7c0040f2-cf51-3508-9951-4b3f817809db | -3.2772 | -53.6989 | 2024-11-11 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5e6c43c7-0f69-33d6-b098-5e9efdaa564b | -15.9793 | -59.3267 | 2024-11-11 00:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 32b96aa1-fdd3-33a2-a13c-3058ed9f9a2b | -3.1097 | -54.2865 | 2024-11-11 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5ad68db3-1ed2-36f8-bc99-e06c6f098105 | -3.6603 | -50.2291 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b9611f6e-097e-38c2-96b5-44e5a4681ae9 | -3.3507 | -49.2248 | 2024-11-11 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 638c53a9-f0a4-33ed-b186-f03f2b3e9362 | -6.1325 | -44.9199 | 2024-11-11 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ae41d907-8a72-3859-b8b8-b0015f36e379 | -1.2202 | -53.6163 | 2024-11-11 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c2933f59-98e0-3f97-97e9-1b6a3909dcf3 | -4.1285 | -49.1094 | 2024-11-11 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f3c8a674-2ee9-3c0d-b610-f739b8178fbe | -1.4009 | -55.4518 | 2024-11-11 00:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| ff3c3063-6e59-3d60-9542-d92fde6b821a | -3.0213 | -53.2607 | 2024-11-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ee6c7bff-8492-3458-8d2c-1d1271829d57 | -3.8672 | -46.0708 | 2024-11-11 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2bafa5a3-6b70-3163-b4ce-f825ca67df10 | -3.6604 | -50.2081 | 2024-11-11 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ac0c7f1d-e44a-3f42-86ea-e899e1c207dc | -2.76 | -49.32 | 2024-11-11 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee90f3b3-cb31-3ac6-9d8e-b00b4a183053 | -2.79 | -49.38 | 2024-11-11 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3312fd95-5560-35d3-94b6-d9f4b938b3d7 | -2.76 | -49.37 | 2024-11-11 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c281a8c2-f9c0-3e51-8e4b-9a7ace4aad1a | -2.73 | -49.37 | 2024-11-11 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1927a5a-1302-37eb-a303-a88ca0c29f0e | -17.59 | -57.51 | 2024-11-11 00:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8f0cce7-460b-3e9d-b62a-ed49491d6e95 | -2.73 | -49.32 | 2024-11-11 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4affddff-1f84-3483-aa10-b159f170663c | -2.79 | -49.32 | 2024-11-11 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a37b2a-5372-3205-a048-5497fd49b100 | -4.0294 | -46.9484 | 2024-11-11 00:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2523f061-fcd5-3513-8e72-a8d3973c7100 | -3.2352 | -50.3065 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 049055be-a785-3868-a74f-c0612a81fa58 | -3.0323 | -45.8377 | 2024-11-11 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d18b04f9-9d88-3c9a-a54a-e049f31f606a | -17.6086 | -57.4276 | 2024-11-11 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.4 |
| ff1d9afe-4cdf-35e5-a17e-66e035fa3da3 | -3.1458 | -54.4859 | 2024-11-11 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 890041b3-b942-3b59-9d73-e0f736a432b1 | -3.2244 | -53.0524 | 2024-11-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 69249f58-3fd0-303b-84d5-9e2de1e0cd0a | -3.2352 | -50.2855 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8347c2b7-a1cd-3ceb-b19e-6abd12925333 | -4.1246 | -43.5833 | 2024-11-11 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f48e540b-93d9-366d-9ad2-b742bf7c6b8a | -3.2168 | -50.2861 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 84b72b38-a832-3785-91c4-2097cbc8f1d9 | -3.6033 | -50.5667 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| aa689413-1293-3267-b194-f44d81f0c097 | -4.11 | -49.1102 | 2024-11-11 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ab2eca0a-f0fb-33e3-a252-fd113d934952 | -3.2603 | -48.7582 | 2024-11-11 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |


[Clique aqui para ver as próximas entradas](README2.md)
