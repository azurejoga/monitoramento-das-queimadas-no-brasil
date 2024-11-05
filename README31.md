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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 618c9045-a894-3e2b-a095-4f12c5fa6bc3 | -21.55807 | -54.20373 | 2024-11-05 04:59:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6f7595c-79ac-3904-a846-83eebbdd1cca | -17.66629 | -57.52433 | 2024-11-05 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| aeeccec0-455c-3afb-84d2-e6557a9b3f75 | -17.62855 | -57.46166 | 2024-11-05 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 77b872ff-e5d1-3195-b7fb-a45ad5e42200 | -17.66297 | -57.52374 | 2024-11-05 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 17927000-4438-3038-a1ee-7a066b11131d | -17.66961 | -57.52491 | 2024-11-05 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 023e7682-f714-34e7-9c8f-962a3c172a2d | -17.93719 | -54.5897 | 2024-11-05 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 195314b4-c4a6-3f9c-b806-1d85d92b2b32 | -17.71862 | -57.51479 | 2024-11-05 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a0ad5643-4589-3216-97d8-5b54918cb7be | -17.6225 | -57.45686 | 2024-11-05 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a223370c-eb34-31d7-adbd-53a33e083bf2 | -3.563 | -47.4066 | 2024-11-05 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 68cce18d-1195-3593-bd2c-45cb7bc8edc0 | -3.5444 | -47.4073 | 2024-11-05 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| afedf6f9-c983-3606-9018-f1bb647f5072 | -3.0397 | -53.2603 | 2024-11-05 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1616eccc-6334-34fe-8131-a73426946d67 | -2.8065 | -51.4855 | 2024-11-05 05:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f38ff5b5-1ba9-3265-9994-b8c73808db4f | -3.5447 | -47.3636 | 2024-11-05 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e6007f7a-a1a0-3af3-9d86-d9aa4fa29f01 | -2.6507 | -48.5629 | 2024-11-05 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 3b264f52-3668-311d-b488-bbd8e1b2f9bd | -3.5446 | -47.3855 | 2024-11-05 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 221.3 |
| b1614dcf-95c7-3cee-a34e-e4f955603a4e | -6.1043 | -43.9362 | 2024-11-05 05:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9550e9a3-a9fa-33cf-b652-a781116f6564 | -2.6691 | -48.5624 | 2024-11-05 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 28f75c20-63e8-35d1-8e99-372169f496b3 | -3.5632 | -47.3629 | 2024-11-05 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a45c5556-1ac4-35f3-ac6b-3ada0e14a223 | -6.1041 | -43.9593 | 2024-11-05 05:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| cdd89d4d-8002-3b6a-a1d8-2f8751aaf7ca | -3.5631 | -47.3847 | 2024-11-05 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| a2482edb-6079-3ed6-aed2-4750d0deeb53 | -2.6506 | -48.5844 | 2024-11-05 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e0241a13-473a-32db-b61a-6acaa6628e8a | -3.56 | -47.4 | 2024-11-05 05:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5a0c1b-70d6-3463-81f3-4f8b4ba98ef2 | -3.563 | -47.4066 | 2024-11-05 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b82d799a-1642-3e44-af18-17cacfa85717 | -4.0481 | -46.9255 | 2024-11-05 05:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| bfac3b82-1227-3413-961f-ad8bfcecfd0c | -2.8065 | -51.4855 | 2024-11-05 05:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| cf47ad09-0298-342d-ad3c-64a8ad31fd18 | -2.6691 | -48.5624 | 2024-11-05 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| fff22dbf-6bb0-3f36-b6ae-9c86f7b15dc8 | -3.5631 | -47.3847 | 2024-11-05 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 5c0bb166-9bdf-3a00-8625-a99afcb4199a | -2.8064 | -51.5061 | 2024-11-05 05:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 8826ee83-930d-3309-840a-8ee828391d49 | -6.1041 | -43.9593 | 2024-11-05 05:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 91803b32-00b8-3c00-b162-82f51176a30a | -3.5447 | -47.3636 | 2024-11-05 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 93a10026-0853-3b08-940c-1603a6a24290 | -3.0397 | -53.2603 | 2024-11-05 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0f5e9fc1-0dd7-3cf7-b26c-bc6a228ef507 | -3.5632 | -47.3629 | 2024-11-05 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1b30d865-7a68-3d9b-99a5-444596e0604e | -3.5444 | -47.4073 | 2024-11-05 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 81b42635-0d87-302e-9bf6-7d3a6a883a42 | -3.5446 | -47.3855 | 2024-11-05 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| af68ea4c-2343-3488-a186-a98473321280 | -2.6507 | -48.5629 | 2024-11-05 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1f9e24d4-60b8-37dd-9822-6c534fd492ea | -4.048 | -46.9475 | 2024-11-05 05:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f48d5602-a210-3e2a-ac33-30493ef5c9f5 | -6.1041 | -43.9593 | 2024-11-05 05:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c88f7d6c-0d7c-3ca8-ba60-46702333de7e | -2.6691 | -48.5624 | 2024-11-05 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 976b1d9b-b839-30f6-8a65-ea76e8b3c87b | -2.6506 | -48.5844 | 2024-11-05 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a97972cc-4b66-3759-bddd-bb1894e32543 | -3.5446 | -47.3855 | 2024-11-05 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c7d44bbf-9fd5-3001-8b9e-20bc1b434fb0 | -3.0397 | -53.2603 | 2024-11-05 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c10a8e3a-29ff-38db-884e-8197e1f01807 | -3.5631 | -47.3847 | 2024-11-05 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9cb7a7ae-dfcf-3940-a578-d5cf2a93c23a | -2.8065 | -51.4855 | 2024-11-05 05:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8db7b868-a584-3dbd-ba91-1b59491633bf | -2.6507 | -48.5629 | 2024-11-05 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| df7fb368-19f9-31b0-b7db-6b33dd023c41 | -4.0481 | -46.9255 | 2024-11-05 05:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1146edde-4c99-3101-a311-5a2dab975ff4 | -2.8065 | -51.4855 | 2024-11-05 05:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b53e160f-585d-333d-babe-9551efa67e99 | -4.606 | -46.8758 | 2024-11-05 05:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 8b01b15d-4aac-3855-b294-971450d7093d | -4.0667 | -46.9246 | 2024-11-05 05:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f030b624-b853-3fef-a099-19593d9673db | -3.5446 | -47.3855 | 2024-11-05 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| b124d2ff-fbc4-30f5-a5f5-bef3854229e1 | -4.0666 | -46.9466 | 2024-11-05 05:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| d47fc543-2968-3763-a7c7-b584b0fb55f3 | -2.6506 | -48.5844 | 2024-11-05 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d0c4ce99-eb01-3475-bcc3-41bd60a3f29c | -3.5631 | -47.3847 | 2024-11-05 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a5e6dd04-e711-3db0-9d50-8f5802bfa08c | -2.6507 | -48.5629 | 2024-11-05 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| daa55fa5-1d0d-39e0-b951-be6c8030974d | -6.1041 | -43.9593 | 2024-11-05 05:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c006c770-4426-357e-85de-b6a97f7b6c7d | -2.6691 | -48.5624 | 2024-11-05 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| aaf39ee4-9f7b-36f5-a216-b3c77b10eff8 | -3.5446 | -47.3855 | 2024-11-05 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 17490ac2-8a9e-3b99-9a9d-b28638298395 | -2.8065 | -51.4855 | 2024-11-05 05:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 494cc577-7081-315f-a264-de758fc17869 | -2.6507 | -48.5629 | 2024-11-05 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 32077df1-d99a-3dec-a600-abdbd6a9b0a2 | -3.5631 | -47.3847 | 2024-11-05 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| d90889f3-31ce-3811-b14e-ad16a60d3905 | 3.51466 | -51.25716 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3c08317-1146-35be-8617-0f202b1292d8 | 3.49541 | -51.26527 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ca6ed834-ebc7-3183-9c5e-4dc64035e072 | 3.50816 | -51.25604 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 418910b2-c041-308f-99b2-d0930c070a07 | 3.50702 | -51.24942 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b2bc0501-efec-3291-a305-c659a32307b4 | 3.52204 | -51.25344 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c1f1c1-9213-33a8-8765-7cb3c5bf9ac8 | 3.5151 | -51.25475 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2dc95a5-6cd8-3563-be8c-9f5e0ec330bd | 3.51349 | -51.25055 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de4a2446-0988-3bb4-805e-98af4fa14901 | 3.5216 | -51.25589 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59f9b279-a77a-3a1a-a6b0-d3641291a7d3 | 3.49427 | -51.25865 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f311dc5-b483-3012-932a-c2a9116f7c83 | 3.50121 | -51.25734 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ca484b36-100b-3390-bd5a-6e4ac6bf07d0 | 3.52317 | -51.26004 | 2024-11-05 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 633055bf-a025-3005-bb55-4581b4749ee9 | -0.80613 | -63.07624 | 2024-11-05 05:48:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 062dad78-8bd3-38cc-a46f-ef5a328d425c | -3.21487 | -53.1026 | 2024-11-05 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a94d1a10-4554-3470-b62d-c661ffdf1d80 | -3.09057 | -54.50068 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a5175bb-fa5a-39f0-9277-d49dced13d55 | -3.08668 | -54.50598 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48cba80f-670c-37b9-b422-476d9690215c | -3.0874 | -54.50097 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 908b0907-8adc-3006-942f-2c9b028aa73c | -3.08981 | -54.50573 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2b1da0d-c4b2-314d-9d19-0dd64bfaffba | -0.81083 | -63.0758 | 2024-11-05 05:48:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a857327d-1a63-3ac7-bead-d6cf51f67657 | -3.08042 | -54.50478 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2832fb9-7a11-3d28-b6ba-1e5fdbadd182 | -3.08428 | -54.49968 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4c03ed1-67b0-39f9-8025-e54e5e2dc805 | -3.08354 | -54.50464 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cd0310c-00ae-3e3e-afb3-225820a2c451 | -3.0828 | -54.50959 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f708ef3-032e-38e3-b75f-329c5e01c971 | -3.07971 | -54.50975 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1e92c50-dcd3-3343-af8b-4ad79fdd9854 | -3.08597 | -54.51096 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d79e4d55-f6fc-310e-bea9-b68cf352c909 | -0.80964 | -63.0768 | 2024-11-05 05:48:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00147ce5-2d09-3db0-b8c6-96843639902a | -3.08906 | -54.51076 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eacdc552-ab13-33e3-9009-5f44c05c7bd7 | -3.08527 | -54.51585 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68c09436-e056-3e62-87af-c664e49d0715 | -3.08206 | -54.51452 | 2024-11-05 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cd9608b-20eb-3a38-8738-4be21047ccce | -2.6507 | -48.5629 | 2024-11-05 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| ccace804-37c9-389d-9fce-7cf6bef7e520 | -3.2396 | -45.2242 | 2024-11-05 05:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0faef1ff-f7a2-3657-bb33-7d30ff3f2c1e | -3.5631 | -47.3847 | 2024-11-05 05:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| a793e713-e5c5-3957-b295-be143fb8bcaf | -3.5446 | -47.3855 | 2024-11-05 05:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 32f2a5f3-7b3b-3367-9d9b-6ff51e7c88da | -2.8065 | -51.4855 | 2024-11-05 05:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 3426a6f0-ded7-3db1-acea-34396b01331d | -3.5447 | -47.3636 | 2024-11-05 05:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 20eeaf2b-ec80-3d34-94ba-8c47f16e6100 | -8.83183 | -71.25575 | 2024-11-05 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 055c6472-6f3f-3bf5-b291-038e0dce0535 | -8.92428 | -65.03062 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b8720ba-266c-3343-b57d-46facaf93686 | -10.08992 | -68.36211 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 228a4ed5-09c1-32b6-8bdc-c224f521727a | -9.5064 | -66.55878 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01a09801-d09a-3e3d-a36f-875e87f48df1 | -9.54007 | -68.52617 | 2024-11-05 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67843aaf-549d-3bd4-8522-003e3a0fc65e | -8.92079 | -65.0301 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc93752-ca78-3b10-8d29-6d5b7009d947 | -9.56592 | -66.21517 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
