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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67c1f053-b980-3d27-9832-16495ffadc33 | -1.13144 | -53.61054 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a3407e7-6de4-30df-a073-b677fb77323c | -1.25669 | -51.77781 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 590090a7-3f42-33c1-810a-19176bcc3b6a | -0.81643 | -51.61375 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a9a3501-d06f-3d30-b010-5748b745b5ee | -2.58917 | -54.05052 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d452952c-f1a7-372e-ba62-8695c25cd49d | -4.44615 | -50.07961 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e9aef1a-2419-37f2-bf31-f6840a29611e | -3.55401 | -49.91093 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 252abde8-77b1-30a4-a181-4bcd3a9586d0 | -2.12782 | -50.81297 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5b0066f-2a70-3f1f-92e2-80dd697dd681 | -4.37341 | -49.74783 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a7581dc-95c9-3739-9600-819c1245770e | -1.47698 | -51.15039 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13dc95dc-127a-32d0-980d-92b267b3b55b | -3.24981 | -54.22437 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2eddde83-aea4-3633-9894-04952a181ea9 | -1.05383 | -51.81252 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c1e0fcc-2372-3857-a5eb-14d09208e7a8 | -1.14527 | -51.68623 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b77fb976-249d-31e1-b49f-bbe2bb3c13da | -1.76539 | -52.70189 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a988ce3d-b5a0-3b6c-a363-b2aa058efa5a | -1.98772 | -48.75051 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d060c8c7-230a-36f1-9888-f99ce1f6c428 | -4.61906 | -46.61931 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09068cc3-e7e0-38e8-be9a-c388d6f25bb3 | -2.27279 | -51.23913 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bfa3b1b-ac94-3e6f-8f92-dd7e94808914 | -2.86877 | -49.84826 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9694c419-0bfd-3f1c-bfd2-05d2643fbd90 | -1.64952 | -52.79072 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed4a68c0-978b-35c5-8935-70c3b5408cd9 | -3.78138 | -52.40525 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d671c911-1da3-3caf-b7be-aeee307f9b40 | -2.37112 | -50.38787 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bb5a966-d2b6-3b29-a3c5-cbb0a326dcaa | -5.1022 | -43.15145 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a9ea8dae-1936-38f8-b23d-6e8b45b742eb | -2.245 | -49.21584 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7794b2b-8a21-3ffc-bcc1-6649461ea6ce | -2.27507 | -51.13598 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a07f4f99-5142-331f-8f21-576104ef20e4 | -1.25936 | -51.76067 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f03cca5-dd4f-369c-a2a4-0a3aeb830c03 | -2.94251 | -54.0815 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba2a98bc-c8dc-37f7-87d6-32eb7874687f | -3.10395 | -53.9699 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| beaae42c-1e12-3ea5-b605-db8450c8e087 | -1.30379 | -51.73592 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9f19a77-20d0-38a8-9f40-cd6d8512e490 | -3.26729 | -53.8226 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 339ca0e1-e152-3f2f-9587-280803000643 | -2.76612 | -52.87242 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ff8a080-dbab-3906-9477-d7b44ef16e07 | -1.76485 | -52.70537 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72e66e6e-e8b7-3a1d-b1fa-3e6b37b6482f | -3.34112 | -53.30643 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23367d0a-b519-3804-9053-5c2d2045046b | -1.95405 | -49.52673 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d87f24c8-aef8-3749-a416-b5e5a2c7658e | -1.645 | -53.87178 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb53fd9d-80cd-3e62-ab1d-c4c8642ee115 | -5.10974 | -49.12999 | 2024-11-24 04:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29a7c3f1-503a-32d7-94e2-f291e856c36f | -4.0904 | -46.83037 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b74447da-0f26-3afe-9d35-4078a6e5fdb9 | -2.99417 | -51.45406 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 663c9db1-8079-37af-9c4e-c4cc4675a66e | -3.02371 | -54.05604 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3b5e35a-c33d-3517-8b85-c5f7ec68dea2 | -2.25306 | -49.00045 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09bca67f-1882-3054-b0f2-1033a55b45a7 | 0.40612 | -50.85668 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 99dffc8a-8c84-32c8-b5a4-e110e327d756 | -2.86931 | -45.83375 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 45a00c62-cd97-3abc-8144-c81ee944e54d | -2.59507 | -47.02874 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1209f049-f91d-380a-82ec-9d1ce3da3dfc | -1.11902 | -52.11451 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebdb22d8-e852-38c0-a02c-eb404ddf0e46 | -3.2379 | -54.10061 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4914104e-6691-3a02-8247-a41fa5a0294e | -3.23023 | -54.23671 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e70e1a2c-2294-3ac6-8be1-204e75d647f1 | -0.28709 | -51.6049 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 917d407b-bc9e-30f0-9fae-5568e814b559 | -0.91327 | -51.73453 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5d9adcd-21c4-3d92-8a6e-43ec0f3e71e2 | -3.20625 | -54.8845 | 2024-11-24 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59344fe2-9b2c-3b0d-a16c-542624c2f0cc | -1.76953 | -53.61472 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4691eed3-e1d6-35fe-aa7d-9e905f0be22d | -1.63577 | -53.3303 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef2ea0cd-132d-389f-843c-c5380a44996e | -2.31195 | -50.59139 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c9c56a-3f71-3134-b745-2459a085e7d2 | -2.30683 | -53.92741 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd804245-8484-32fe-9d7c-ee85da2ac783 | -3.07348 | -49.19993 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ec37fd6-9dca-3da5-818c-4adb6b486b93 | -2.31041 | -52.17459 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9142ae13-9117-33c6-962e-6059799242c5 | -1.37631 | -51.55751 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a053653e-38ac-3de2-b56b-194892fb3498 | -2.70761 | -46.26683 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dfa1c11-4a33-3fdc-9aca-17888f3eca43 | -1.92657 | -53.34917 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 220054fe-ae76-3dbd-8c1d-c2714bed0acf | -3.0639 | -53.22754 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70c767aa-6ca5-3421-8355-9cf5f48c4dd6 | -3.46852 | -49.91336 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67330164-2ce3-368c-8c46-0018a54dcd85 | -3.24399 | -54.23881 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a86134c-decd-3719-960e-a0e82f6bec3f | -4.08692 | -50.36572 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fca587f1-fd7f-365a-9ba3-cf0646ee4921 | -2.10165 | -50.36563 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 231d42d5-52a3-387c-a05d-adb409901807 | -2.55825 | -53.95819 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc41391c-296b-3d0c-8275-dacf9805e943 | -3.96109 | -50.20198 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| af424fbd-9e2b-3702-bcf1-cf2bb8eba8d8 | -2.44633 | -49.08577 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dcf5c00a-440a-3089-88c7-18760cf8bc0c | -3.22401 | -51.00323 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4427f332-73d3-326c-82ce-09bd44b2e9b6 | -1.62071 | -55.17323 | 2024-11-24 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27066975-b13d-381b-abea-49aea873490e | -2.19421 | -49.00379 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a26c8ec-fe28-3ecd-8c0b-c4d9d952c567 | -2.71435 | -46.27946 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48c47246-d982-3007-8bad-16fc254acf09 | -4.63415 | -46.86867 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b37c024d-d42d-357d-88c2-ab0522068461 | -3.25028 | -54.24362 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba4928ab-c95a-3916-b819-ebac94f47a2e | -1.14643 | -51.70044 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 962cf37d-4834-353d-b5b7-aa200997be1f | -2.22358 | -50.85279 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 410de347-51e2-3569-8c34-27ad3773ae59 | -3.23486 | -54.22974 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a15d5337-c479-35c6-a907-26837c1a0504 | -4.52891 | -49.81858 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce3068b-6cab-3554-97ed-8cc2f841bc6b | -2.37063 | -48.62906 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 335245da-df50-3c59-a582-0818b25f58a0 | -3.83892 | -51.70925 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cefefc1d-dec7-386e-866b-66c8f8fa9190 | -2.85945 | -53.96282 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91eaea94-4438-3ea6-aa46-6e128c8fe1a9 | -3.09507 | -54.55833 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d799a2f7-b298-3158-8585-1742d13f844f | -2.7155 | -46.27162 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83897874-6bbf-34af-8070-c8df41b5b25d | -0.33357 | -51.54537 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 746748e7-b989-34c9-9399-2fec42c83305 | -3.68282 | -47.13351 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccbd6a29-a750-3bc9-8532-e77f7e88fce5 | -1.73074 | -52.37976 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d916dd0-eb2c-3df1-9a98-93160a1b3b62 | -1.45005 | -52.45684 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcdb046a-58c7-3139-961a-afbee64db254 | -3.30757 | -50.02892 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22532ae6-b66f-3795-bee8-3a76782139bc | -4.12694 | -54.20701 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a51737aa-8120-3022-9eb2-efe888049963 | -3.10729 | -45.78185 | 2024-11-24 04:53:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d1bf27de-450f-39e5-ac17-b9cef57e0926 | -2.14342 | -50.49673 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae6bd26-af4a-3f21-863c-9a04aa594fc7 | 1.32551 | -50.62489 | 2024-11-24 04:53:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd647557-950c-36ca-aa31-a0e8140ee691 | -3.70557 | -47.60321 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bdef702-635d-31e7-9077-42e8e6ded98f | -2.41747 | -51.96974 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0752a376-751b-3d74-a647-751ae822c50b | 0.61347 | -51.77337 | 2024-11-24 04:53:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c1ce150-bf30-3d83-bbe2-75fc5bf66a76 | -0.21957 | -51.77302 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d9a6910-1795-3f34-b3d4-b593ee4bca72 | -1.19293 | -51.77077 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a68d85bf-cd11-3dcf-94ef-17e95d7c7a3c | 0.3223 | -49.72638 | 2024-11-24 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aadc20e4-ac46-3503-b062-f5d53a4e3801 | -3.31955 | -54.09409 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca055af5-91fd-37d0-ba48-b1ea010bbd63 | -3.67676 | -52.37842 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10f2f4db-7461-3587-bc7c-29727f84719e | -1.46472 | -51.12021 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc4a6a87-0643-32bb-bb92-1cfb7e4f82ee | -5.46194 | -44.83443 | 2024-11-24 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa948e79-b892-35ca-8168-a17a1f9c03df | -2.14006 | -50.49621 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34bf496b-1301-325a-8971-21c459d82424 | -3.04895 | -52.76043 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README49.md)
