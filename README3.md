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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96191907-8b54-309c-9997-3daa36e7f155 | -9.0036 | -65.9412 | 2025-10-22 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 47b4cd8b-2680-3c67-b37b-39b7c6a3fcc7 | -9.0222 | -65.922 | 2025-10-22 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9f33564e-7cf1-3a24-b88c-bf166bfd5d15 | -9.0036 | -65.9226 | 2025-10-22 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 8d0483fb-4d0b-3c5b-a1f5-9c752208186b | -5.066 | -40.475 | 2025-10-22 01:20:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 8033f6c2-a383-3d94-9d5d-cb98ca057d10 | -4.4066 | -43.3118 | 2025-10-22 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 4e87f49f-bc6c-3159-811f-ee0c8f65681d | -9.0036 | -65.9412 | 2025-10-22 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 7f1e53ed-1a92-3fef-abca-d02ca9d51712 | -9.0037 | -65.904 | 2025-10-22 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8ca02674-91dc-3229-aef0-4dc83215aeff | -9.0221 | -65.9407 | 2025-10-22 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 925c795e-484b-3782-995e-04511c4aa144 | -3.3831 | -50.2597 | 2025-10-22 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 8fff9dba-aed1-30a1-b2ab-6ebc62eaadba | -9.0036 | -65.9412 | 2025-10-22 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 498aaca4-86e9-34c7-af92-5c3a08af3143 | -2.2527 | -51.9313 | 2025-10-22 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 106b84fd-c3a9-3fa0-8dd9-e26ddd533732 | -8.9851 | -65.9232 | 2025-10-22 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 64c7255e-e68d-38aa-8e4a-e04a2563d889 | -9.0221 | -65.9407 | 2025-10-22 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 191c95cb-0f68-3f2a-9a77-43c61fdb048f | -9.0036 | -65.9226 | 2025-10-22 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 2e6dd1f6-29f3-336c-9b34-dc38eb94edbe | -9.0222 | -65.922 | 2025-10-22 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| cb6ec92c-993e-3a50-9ca8-bd52fd5d5414 | -9.0221 | -65.9407 | 2025-10-22 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1e40cbb4-d82a-3a58-8be9-bec7a420c7b4 | -5.066 | -40.475 | 2025-10-22 01:40:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 69.0 |
| d30c73dd-d784-3c73-95d6-0099a5141f29 | -9.0222 | -65.922 | 2025-10-22 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 77bd1881-67b5-3b15-8da3-2f56b57041e5 | -8.9851 | -65.9232 | 2025-10-22 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7bfb606e-3cf2-3c20-9076-bfa31b94629c | -9.0036 | -65.9226 | 2025-10-22 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.4 |
| a11a28f3-4123-3320-b057-c29916016c36 | -9.0036 | -65.9412 | 2025-10-22 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| aa71282b-4339-3f5e-b3f7-0e662c648a8f | -9.0036 | -65.9412 | 2025-10-22 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 0b270db2-2896-3fdc-90e3-0f2ad5d84ebb | -13.9867 | -45.7529 | 2025-10-22 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e45ff0eb-fe18-32c7-9323-375065e97523 | -13.9667 | -45.7794 | 2025-10-22 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e3e61447-8c9c-38db-99df-df9d8384bc17 | -3.5161 | -49.4528 | 2025-10-22 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 30118cd6-d829-3c47-8a3f-7b11ba1dda86 | -18.3621 | -49.5001 | 2025-10-22 01:50:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 4c619704-c577-3765-b7a3-526e415ab9fe | -18.3421 | -49.504 | 2025-10-22 01:50:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 113.5 |
| ddca1a63-202f-344d-a1fe-28e61b62af60 | -9.0036 | -65.9226 | 2025-10-22 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 41d008c0-5876-378e-896d-1cdb7226a8c8 | -13.9672 | -45.7563 | 2025-10-22 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0db2856b-2a24-3e91-824c-7aa70db7f1ba | -9.79882 | -67.03088 | 2025-10-22 01:52:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 273ec78d-8809-3fa0-8a97-b63ea48f227b | -8.99135 | -65.91578 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 659ce1c4-952d-3f6b-a1e6-77a252f25dcc | -10.93121 | -68.58907 | 2025-10-22 01:52:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2ee1424f-327f-34f1-8358-b4cf5be67d1e | -9.0143 | -65.9352 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 5396ee6e-47d8-3759-8be1-6f12d348ca6e | -9.00283 | -65.92549 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 284a6b4f-388e-3480-937b-18eb994ea24f | -9.55471 | -66.74853 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 81ca121f-baef-3289-9781-881ff63ae46e | -10.30554 | -68.85897 | 2025-10-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae1af266-8196-33ec-9bb8-ca859b0f3ac0 | -9.00119 | -65.91428 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f30a6315-905e-308b-8473-565fcac84983 | -9.91229 | -65.02393 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f2964532-3fff-3d12-8d90-9558b8e3b1bf | -9.0061 | -65.94783 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 862189a6-e90a-33a4-8f18-263eb1cca720 | -9.71578 | -67.48215 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ed488f7-74ff-3562-b391-2051fb052fc8 | -9.57261 | -65.21493 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 328afa9c-c044-33ee-87da-d9ad3148076d | -10.25818 | -63.12607 | 2025-10-22 01:52:00 | TERRA_M-M | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f6de2367-d18b-3384-9e6d-edebd16bc975 | -9.6514 | -65.25239 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7906422c-ce7d-3f94-ba42-55e765974428 | -9.1167 | -65.93623 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de37b989-baf4-3709-b87f-f0898f886545 | -8.93054 | -66.89563 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e21156aa-80fd-39c2-9bc9-cc28ec155bc7 | -9.48355 | -65.64102 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f3b97728-c8bc-365a-9ca7-a340d0a14c2b | -8.8518 | -66.79035 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1386b857-ef69-3791-8d95-3d0f0d05b18c | -9.57555 | -65.22026 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a873de20-4793-3ea1-a47f-6e403b5212a5 | -9.54945 | -66.64677 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 561cb38b-7782-3c30-8d19-7d811a5c1197 | -10.92998 | -68.58014 | 2025-10-22 01:52:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfc73ed6-2aef-32d2-bf98-f1f23bd997ba | -9.73299 | -67.47379 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a7a02b36-5a16-3108-a290-898d17c6bd72 | -9.57448 | -65.2271 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5d3eb027-3532-37d5-b791-2ce56406fd95 | -9.01592 | -65.94633 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| be470633-8926-3e10-b41c-433b02628f43 | -9.71454 | -67.40969 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c824f4e7-7d76-321f-b484-42f56dd4f1fc | -12.12788 | -63.20793 | 2025-10-22 01:52:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f9eea9f7-ba57-3e12-b354-4a056936ce81 | -9.85013 | -66.37814 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a834bb7c-fb25-385a-9ecc-5704ebcf0c47 | -9.01267 | -65.92401 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b03e1602-165e-33c5-b6f1-7c7f7ff0c9b7 | -10.24969 | -63.11672 | 2025-10-22 01:52:00 | TERRA_M-M | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2c0c73f8-b83c-3f78-a318-7057cbd5cef2 | -9.11443 | -65.36026 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9aabf380-d9fb-36c2-b27f-e6cbd7524240 | -9.80553 | -67.59579 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6de10abc-eba0-3504-a394-a0754a003d6d | -8.9897 | -65.90453 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b480e475-633b-3bbc-87ed-9bb6c11fbf7a | -12.27882 | -63.87379 | 2025-10-22 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8797a24d-397c-38ce-8892-efbad2316132 | -10.25232 | -63.13371 | 2025-10-22 01:52:00 | TERRA_M-M | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2f52b559-eed1-3e82-ab90-e82444a06b33 | -9.72397 | -67.47515 | 2025-10-22 01:52:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 1a4513a5-dfd9-372b-acea-b339f2037a47 | -8.93198 | -66.90558 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97682894-aa1c-3715-b3c3-f0b036826485 | -12.13003 | -63.21416 | 2025-10-22 01:52:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 421cecdc-fc9b-3fcb-9db1-897478acf8b8 | -12.38072 | -63.86526 | 2025-10-22 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d98b0a91-0139-378d-882e-fb94684427f8 | -9.09115 | -67.69347 | 2025-10-22 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fbd2c09d-4807-3b33-985c-6e93e0bdedf8 | -12.38285 | -63.87902 | 2025-10-22 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 817faf80-05de-3a4e-b853-a5d4d7a6f895 | -9.1069 | -65.93778 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9ef56b75-a3f5-3d33-b4ff-72533d42bd0c | -9.00447 | -65.93668 | 2025-10-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 070bea59-ecd6-3dff-bf77-7cd5680869f3 | -12.13038 | -63.22345 | 2025-10-22 01:52:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9f566593-2d43-31c6-aeac-78cfa4bc484d | -3.017 | -49.4482 | 2025-10-22 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 7dece442-b0be-3f5c-8a7f-7500412e62ad | -9.0036 | -65.9226 | 2025-10-22 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 0f31d010-4629-334b-bee9-edb3cb9366c2 | -4.4632 | -43.2386 | 2025-10-22 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 499f9da8-9a64-30a8-84bf-c5a6a0977428 | -9.0222 | -65.922 | 2025-10-22 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 51609ac3-d32d-3017-8f9b-f1ef056e799f | -4.4445 | -43.2397 | 2025-10-22 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 6ef41975-be59-3916-9eeb-af4a3c6c8cb6 | -9.0036 | -65.9412 | 2025-10-22 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| bc5890e0-fdb4-3b0c-8652-028cf5e13a35 | -5.066 | -40.475 | 2025-10-22 02:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 60.3 |
| fedf1277-5ec9-3fc3-9b49-6af743568dcc | -3.017 | -49.4482 | 2025-10-22 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 58e6aad1-c66d-3a32-8bbd-12853edab620 | -4.4632 | -43.2386 | 2025-10-22 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| cad3eae0-c307-3680-8f73-d0221fd25185 | -23.6991 | -51.7459 | 2025-10-22 02:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| 54a4c07c-9e96-3fda-9720-7412f2663b7e | -3.0169 | -49.4694 | 2025-10-22 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d2665e44-d2f5-3e1f-8abe-74f6fb9eb8b5 | -9.0222 | -65.922 | 2025-10-22 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 95cee055-5a55-378d-b13f-9e59310f9cfb | -9.0036 | -65.9412 | 2025-10-22 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 21e098ba-c8a8-3b8c-b6ca-38ed6c05ebd9 | -4.4445 | -43.2397 | 2025-10-22 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 29d08700-fe0f-3143-9b6c-32ba2a9fe9af | -9.0036 | -65.9226 | 2025-10-22 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 0da85124-ce8b-3fb7-9d77-9369f16db625 | -4.4632 | -43.2386 | 2025-10-22 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| df2009ad-c6fe-3dd5-b7a8-b08bdd0606b3 | -9.0222 | -65.922 | 2025-10-22 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7c63bdae-4ebd-37e5-908d-6ab119f64d40 | -3.0169 | -49.4694 | 2025-10-22 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b91e2fb5-9a80-3dcb-b58a-6f884e5be22b | -3.017 | -49.4482 | 2025-10-22 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 81a0d158-b96f-347b-9f92-13dc0d9e8e68 | -4.4445 | -43.2397 | 2025-10-22 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| ac363988-9261-389b-a88e-f314889b682c | -4.4443 | -43.263 | 2025-10-22 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 571925ac-3fa4-3324-bcbb-29037eb02aca | -9.0036 | -65.9226 | 2025-10-22 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 7aefdddc-be57-3ceb-a8ae-33b0b995bc3c | -9.0036 | -65.9412 | 2025-10-22 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| e646adca-3212-354a-8a2c-f58c21612c05 | -9.0221 | -65.9407 | 2025-10-22 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a150c4af-fdc7-31dc-88ca-47e328c537f5 | -3.017 | -49.4482 | 2025-10-22 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7a11c468-eea3-3035-bb66-0c0a187dfe82 | -9.0036 | -65.9412 | 2025-10-22 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c4d59d99-25b6-338c-ad65-a85e867d005b | -4.4445 | -43.2397 | 2025-10-22 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 245a9c90-3dd5-3c91-982e-77f9ec72a449 | -4.4632 | -43.2386 | 2025-10-22 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |


[Clique aqui para ver as próximas entradas](README4.md)
