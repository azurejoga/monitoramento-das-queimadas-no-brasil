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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d410d264-6149-3352-9ad1-7232814ba540 | -7.28333 | -64.69938 | 2025-08-15 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0a9e84e-95da-3fba-afcf-0c4b877964d4 | -7.27628 | -64.69843 | 2025-08-15 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f58fc2f3-f704-3f5b-9143-60204a7fee5e | -7.28421 | -64.69253 | 2025-08-15 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75a1275a-589a-35e0-ba6e-a73951e53916 | -9.4994 | -60.5278 | 2025-08-15 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 74014df8-a67f-3fab-ba53-50b9e0a7699f | -13.4759 | -56.6537 | 2025-08-15 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 828b879c-9662-3c66-a5dc-445392d9c6e9 | -13.4757 | -56.6739 | 2025-08-15 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ebe21396-047f-319e-b242-b2f0bf0196cd | -13.4568 | -56.6555 | 2025-08-15 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| eacfb93e-63d7-33a8-a8c5-e715d09bb443 | -13.4566 | -56.6757 | 2025-08-15 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 0052ced8-8241-3c3b-af3c-f9523805f9b8 | -5.455 | -60.1391 | 2025-08-15 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 94de1b31-d905-3727-b8dc-4e9c03610002 | -7.5292 | -61.3254 | 2025-08-15 06:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| be9214f0-793e-34ec-9cb0-6a9b69cb65af | -9.1706 | -59.6762 | 2025-08-15 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cfa0b2e2-1e40-3a3b-ac4c-4c306cb95783 | -9.1894 | -59.6558 | 2025-08-15 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 89965ae8-b284-3bc5-b290-03107fd37b08 | -9.1892 | -59.6752 | 2025-08-15 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 297518b7-1d3f-38a8-a71b-aa96fab9c8fa | -6.0807 | -59.9465 | 2025-08-15 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c4e324a4-6168-3ccc-8839-3620042119ce | -9.1708 | -59.6568 | 2025-08-15 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e5f92cc9-7af7-3f53-a7ca-c65be65eaab3 | -6.9303 | -59.5305 | 2025-08-15 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 86628934-0823-3448-a306-4a087153777b | -6.9302 | -59.5497 | 2025-08-15 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 8df5afd9-680d-3679-985a-7f638bd3bf21 | -6.0807 | -59.9465 | 2025-08-15 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 88bd2467-af9d-3f79-b0c4-3c7a3d210f6b | -9.1708 | -59.6568 | 2025-08-15 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| eaf0d4b1-497d-3f1a-8add-bfadb5d8ab97 | -6.9303 | -59.5305 | 2025-08-15 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 9ab89d11-8259-37c1-bc52-90cdf532cb1c | -19.4881 | -43.5931 | 2025-08-15 06:50:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 33dc2cf6-676e-388a-a6f1-b4b34f8e3604 | -13.4759 | -56.6537 | 2025-08-15 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 2a4c5bb3-87fa-3318-b4b2-519786f3c376 | -19.4874 | -43.6179 | 2025-08-15 06:50:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 109.8 |
| af882c94-2b19-3408-8433-e395a91c5555 | -5.455 | -60.1391 | 2025-08-15 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a4988def-4ca1-342a-9c46-752aa5d977a3 | -6.9302 | -59.5497 | 2025-08-15 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 897e0faa-917f-333c-bd95-e87e02056b85 | -9.4994 | -60.5278 | 2025-08-15 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c58a0a39-aa1a-3559-93ab-4cd28c78f8b8 | -13.4757 | -56.6739 | 2025-08-15 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| cba3ce3c-c5c3-3827-9c54-54b251bd6012 | -9.1706 | -59.6762 | 2025-08-15 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f8472b51-c047-333b-8147-65a33edba799 | -6.9302 | -59.5497 | 2025-08-15 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d33a3775-af1a-3ded-a704-8f7d0cf6adb2 | -9.1708 | -59.6568 | 2025-08-15 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a5e4c14c-c1bd-3588-bfd7-820b33568d58 | -9.1706 | -59.6762 | 2025-08-15 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 4b9f0d2d-b0a0-3c91-84e7-e41dfe53ce91 | -13.4757 | -56.6739 | 2025-08-15 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 96a9be7d-2a2e-356f-9ab8-cdce8ddb663e | -19.4881 | -43.5931 | 2025-08-15 07:00:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 86efa9e2-d9f2-397e-98ba-4762eefc4c5b | -6.9303 | -59.5305 | 2025-08-15 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 0e2b976c-f945-31b6-8098-dd4d6f5873b0 | -19.4874 | -43.6179 | 2025-08-15 07:00:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 276.9 |
| dd1af37a-c133-3cb5-b5d9-a5ae2be24598 | -9.4994 | -60.5278 | 2025-08-15 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 26cb5dd3-dbff-3483-9eca-fab8856e3c33 | -13.4759 | -56.6537 | 2025-08-15 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| a95cdb88-9686-36b9-b4dd-7dd8b1dadaf5 | -6.0807 | -59.9465 | 2025-08-15 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 334cdac6-6cc7-3ea5-ac39-835e6753ab7c | -13.4566 | -56.6757 | 2025-08-15 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 82195e77-f1d0-32f6-b6b5-51e40e494dd1 | -19.4669 | -43.6233 | 2025-08-15 07:00:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ac7990de-6b7c-3c77-8e1a-49fe7537fbf0 | -6.9302 | -59.5497 | 2025-08-15 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2411d222-e330-3bdd-913b-7f5cd89a1f5f | -5.455 | -60.1391 | 2025-08-15 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 27d44959-a2a1-3196-9336-5e205219acea | -19.4874 | -43.6179 | 2025-08-15 07:10:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f8d17827-0e49-3cb4-87c6-dba976c1e897 | -6.0807 | -59.9465 | 2025-08-15 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dced25e3-2760-3ae6-84d7-e65eb8fbd596 | -6.9303 | -59.5305 | 2025-08-15 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 61c053b5-9d03-390d-92f2-2679c41707f6 | -9.1708 | -59.6568 | 2025-08-15 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 72bc16c4-e4f1-3003-a173-8c5d4c7b3816 | -9.1708 | -59.6568 | 2025-08-15 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| e822052b-8335-3441-b486-d6857d68d46e | -6.9303 | -59.5305 | 2025-08-15 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 1161e858-e512-31bc-a355-15bd6219d7fa | -6.9302 | -59.5497 | 2025-08-15 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 488cfdfe-1b78-3927-a7c7-3f83df8c413d | -19.4874 | -43.6179 | 2025-08-15 07:20:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1199a15f-3b54-31eb-8ddf-5bc31cb730b1 | -6.0807 | -59.9465 | 2025-08-15 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6836f105-3ae8-3ad8-909e-281afafe84a3 | -5.455 | -60.1391 | 2025-08-15 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7bc5cdb9-7ebf-3951-a655-a01cabb227b4 | -6.0807 | -59.9465 | 2025-08-15 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 84797dce-42d8-33a2-b861-53a9c74c3341 | -6.9302 | -59.5497 | 2025-08-15 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 7a895dca-5f46-3bc3-9879-19ee57845a6e | -6.9303 | -59.5305 | 2025-08-15 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 90837db4-1ea1-3887-9081-59a25fc9bffb | -5.455 | -60.1391 | 2025-08-15 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5df65613-9d39-3d3f-ad80-7f77519e400e | -9.4994 | -60.5278 | 2025-08-15 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 47a4bd5d-6346-3e48-a947-260f0bcc509f | -6.0807 | -59.9465 | 2025-08-15 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 93166f67-25eb-3dfd-a135-87efacd9d139 | -5.455 | -60.1391 | 2025-08-15 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| efea4267-22d8-389b-84c3-a263c2dafa36 | -6.9302 | -59.5497 | 2025-08-15 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1aa083a5-46ed-3d10-a7e8-a252baedfb6e | -9.1708 | -59.6568 | 2025-08-15 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 7d0569c3-3cf7-3033-80de-e4d4a42bc517 | -6.9303 | -59.5305 | 2025-08-15 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 3d12465d-bc6c-3239-8794-7475e539f0cb | -6.9302 | -59.5497 | 2025-08-15 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1a75ce60-4205-36cf-b213-a779eee3748b | -6.9303 | -59.5305 | 2025-08-15 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 13c3a1eb-678e-3ba9-94cb-88c11b080c6f | -5.455 | -60.1391 | 2025-08-15 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 274402fa-a1e3-3d32-8d65-34d3e8e25481 | -6.0807 | -59.9465 | 2025-08-15 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e60de872-3aab-320a-8b79-570714d62dac | -6.0807 | -59.9465 | 2025-08-15 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 31b4e0da-7818-3eeb-9589-05245b40086c | -6.9303 | -59.5305 | 2025-08-15 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c94ad4aa-23f8-3456-8bf9-0fc8e46654b3 | -9.4994 | -60.5278 | 2025-08-15 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 414abfd5-46c3-3092-9d3d-ca0fdcadf189 | -6.0807 | -59.9465 | 2025-08-15 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 20fc3ce4-5f7b-3817-868d-ea42228d9ba7 | -6.9302 | -59.5497 | 2025-08-15 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 220e9d9d-6fd2-349e-8e5c-5fcaa6e2cbda | -6.9303 | -59.5305 | 2025-08-15 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6dc0a17a-815b-3fb2-907d-1a8ff4b53970 | -6.0807 | -59.9465 | 2025-08-15 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4604224a-b4bc-3fd8-9185-b24682b6640f | -19.4874 | -43.6179 | 2025-08-15 08:20:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fa3226bb-1a40-3833-b043-5d243f9d2482 | -6.0807 | -59.9465 | 2025-08-15 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 66abbd2f-1830-3a04-9118-dfbe5f096662 | -9.4994 | -60.5278 | 2025-08-15 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| b2a1e861-68cf-39cc-9551-338abd2a07b3 | -15.3912 | -55.7791 | 2025-08-15 08:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| f367313b-3708-315d-8abe-f5b565a0ab8b | -6.0807 | -59.9465 | 2025-08-15 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7cf62f9e-a913-3002-9596-70e30934b7c6 | -6.0807 | -59.9465 | 2025-08-15 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 97c4d340-3778-3a63-b828-b54072be6374 | -15.0988 | -60.2227 | 2025-08-15 08:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f6416d5c-1b87-3587-9e58-2625fecf2ae1 | -6.0807 | -59.9465 | 2025-08-15 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 14c66648-0741-385e-b039-995c9b745728 | -15.0988 | -60.2227 | 2025-08-15 09:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 30d77456-3eed-37a6-a3f1-d036e2e07e1c | -15.0988 | -60.2227 | 2025-08-15 09:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 91f8618f-c2d7-3228-a41a-0b01d0574997 | -6.0807 | -59.9465 | 2025-08-15 09:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 807b15bb-2088-3dca-b8ef-c9f6b91375cf | -13.3203 | -45.2177 | 2025-08-15 10:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 645d420a-f461-341f-a68a-4740947f3d26 | -13.3009 | -45.2209 | 2025-08-15 10:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 2594c9ea-d1d1-3f9e-8e34-a8054a4a67d8 | -13.3203 | -45.2177 | 2025-08-15 10:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 3ecf9b29-fc51-3887-a12e-431d796670f4 | -13.3004 | -45.2442 | 2025-08-15 10:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| dc72ae68-e80d-3b20-88b8-2ce23f9372b4 | -13.3009 | -45.2209 | 2025-08-15 10:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 260.7 |
| d28604eb-0c37-3e5f-bd65-176164923d5b | -13.3198 | -45.2409 | 2025-08-15 10:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 19926cfa-16de-3199-84f0-7471bca652da | -13.3198 | -45.2409 | 2025-08-15 10:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| d96c5b29-9833-3467-8c7d-6c1a00cda10a | -13.3009 | -45.2209 | 2025-08-15 10:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 268.3 |
| ec65c25b-681c-3bce-9584-f526f95b19c2 | -13.3004 | -45.2442 | 2025-08-15 10:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 2cf5e5e4-6352-31ce-8f88-afa8dae7e019 | -13.3203 | -45.2177 | 2025-08-15 10:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 413.4 |
| d167b3ff-a0a2-38c4-befb-06d447f3b4d3 | -13.3004 | -45.2442 | 2025-08-15 10:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 97540ccc-c76e-352e-9d3d-fbc2bc1b26e7 | -13.3203 | -45.2177 | 2025-08-15 10:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 417.7 |
| b252a8c9-9c8f-36fe-8ff9-5411d57fd8a1 | -13.3009 | -45.2209 | 2025-08-15 10:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 334.8 |
| 72b894d7-c361-31c2-979a-04960e6ba511 | -13.3198 | -45.2409 | 2025-08-15 10:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 304.8 |
| e4c7dcf5-80ec-37d0-9c37-9dfd96af4771 | -13.3004 | -45.2442 | 2025-08-15 10:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 0a97150f-8800-3e40-a1d1-3dc845df704c | -13.3198 | -45.2409 | 2025-08-15 10:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 655.2 |


[Clique aqui para ver as próximas entradas](README72.md)
