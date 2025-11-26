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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccd9eef2-de22-3cdc-9a15-854ab1fec75c | -3.74833 | -53.93502 | 2025-11-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbaacbe0-a038-3259-bdc8-1fcb18e3b19c | -3.3951 | -49.2254 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff2d31fa-6d7a-3bf8-be8d-b606a71777cd | -4.7048 | -43.9967 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e475ef21-06c3-3bff-a14a-08f4b71ad670 | -2.93188 | -48.21978 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc7ea292-8945-3505-aa4c-b59bbb7be2db | -4.55495 | -49.57433 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c00e598-be3c-3d11-880a-15c26103a5a4 | -3.13262 | -49.40589 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1cc77893-25fd-363b-bff8-f5f7a35edef7 | -2.57035 | -51.8237 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db061662-e212-3331-ba32-069ea9e863b5 | -2.93649 | -48.22356 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd933329-c653-3620-821d-49ee58443c26 | -4.17291 | -43.72028 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 97c6c407-1cac-3b74-9254-4982586899d4 | -4.17063 | -49.86824 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da15eb91-6991-3483-b3a6-36a21bbf8028 | -4.24904 | -48.56604 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dbda4e6-a52a-3327-8da2-e8753be87bc1 | -2.4993 | -47.82852 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aebfb4c3-10dd-328b-8090-37b529227966 | -4.17383 | -43.71384 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 93034e2f-2f81-33db-9d30-e1cfe1556a8f | -4.17451 | -49.87367 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e48038ae-9997-37fa-90e1-2b2f042ccec6 | -3.98418 | -49.28713 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7425471a-6303-3413-97af-23e46a7c3702 | -2.60699 | -51.21206 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63042fb3-3628-3a1f-91cf-4908fc7b8825 | -3.92556 | -49.21959 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f6b9524-7ee4-3c2a-ae5e-bdf52f578597 | -2.33045 | -60.06564 | 2025-11-26 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1507e6a9-4f9e-3ca3-9a3b-4ee77a4791af | -4.1655 | -43.7298 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d090507c-5a79-32e0-901d-5c4a54371b19 | -4.17024 | -43.739 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6b7efd6e-ea66-3560-9af5-9d2a3ab42d75 | -1.52052 | -55.88172 | 2025-11-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78d95d8-598f-327f-a969-1ba1091d6779 | -4.05659 | -48.82816 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f74366b6-d1a6-3e1c-a4d7-42477a7e4a3e | -5.03228 | -43.26003 | 2025-11-26 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 028691b2-b111-35d2-ad20-961c2cf68b7e | -2.94288 | -49.35917 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d60cb69d-2a73-30b4-a5eb-1149fbaa9a6e | -3.33117 | -50.2642 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cbab2dbd-2ce0-3800-8c62-db74be23cd85 | -1.35693 | -55.42477 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eeb26763-f9a0-3743-801a-5cf791944a7d | -4.17887 | -43.72759 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| f6adb2dc-61ba-3862-900f-84b634195ad9 | -3.01972 | -51.03655 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e844272-f1a8-3d0e-b65e-88aeb3e82064 | -2.489 | -47.82689 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 772c3b6d-135e-33e7-ba08-dfe9bffc9161 | -4.17523 | -49.86893 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b4b7a8f-23c8-3bd2-9279-2071886e34c0 | -4.17378 | -49.87845 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ec1d4d9-e476-35af-9f24-a8df8b61e1db | -2.50399 | -47.83235 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2c37ea3-f2d8-3c26-80ec-035e69e413c0 | -4.18024 | -49.86617 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3c2eeda-9b0d-3117-8b54-028f0a8da7d7 | -2.86555 | -51.78544 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f9bb21-f8a4-3ef0-8e92-6d42396f4d34 | -2.92641 | -48.22182 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c71ae47-4720-3e89-a3bf-1fa6b7f7e63f | -2.4391 | -50.26405 | 2025-11-26 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098ebd7a-ed19-3dc6-8d7d-ef821b4784e9 | -3.20826 | -50.21208 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4eda3cf0-d8f4-360b-8749-3147854f2e90 | -2.87825 | -51.80819 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91eaa877-7c6f-3d90-bb1e-7cd7d917b69f | -3.02129 | -51.14082 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efecbb90-6608-3e0b-ba0a-38ece157670f | -3.14239 | -52.40899 | 2025-11-26 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abc17ccd-bbb0-3088-8aea-333bab8b4c09 | -2.92008 | -48.22982 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed093758-8e7c-3435-a41d-e61843b8fb20 | -2.89296 | -51.81195 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c73fc400-dd1b-37ad-8f32-b5cc83151e1b | -2.72249 | -49.79018 | 2025-11-26 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad932612-d982-3076-9b3a-958a0d1c9e5a | -4.16466 | -43.73602 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6802a544-fbd0-360a-b4da-f45b198a6577 | -2.49039 | -47.81765 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a924007-f283-36b6-9d1c-922d5c722858 | -4.16636 | -43.72349 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 531162a2-46c4-3dc2-b48d-ad2c48597a7a | -2.92184 | -51.30721 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b0c2da4-4776-381b-aae1-c6afa333c167 | -5.03934 | -43.26155 | 2025-11-26 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6b347d15-540a-3874-ba7a-f174fea22418 | -4.82854 | -43.82192 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed5bc698-9d47-3e81-83e4-8e7c76832332 | -4.28457 | -47.30167 | 2025-11-26 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0ff9103-908d-3356-949f-e6807689257b | -5.70753 | -47.26976 | 2025-11-26 05:10:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b119a9a-6174-3feb-9c4d-99b45e670deb | -2.93606 | -48.22649 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0f706d0-eab7-3958-81bb-f83e1efaacc6 | -4.17318 | -43.72482 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1ec60c87-d27c-33e0-b0b1-35e36956cbbd | -2.87508 | -51.80251 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 563fa287-7fb0-3cbf-8b92-cd4eda9a2f70 | -2.93015 | -48.23151 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72f334b6-6a74-3fe0-b187-f7ca5dff5d80 | -2.88538 | -51.81444 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f1b0697-cf6f-33bb-b985-914c87c63691 | -3.14268 | -49.40254 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5f1e3e7-e79a-307e-874b-7d05ed024d7e | -3.35568 | -52.68539 | 2025-11-26 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 542cb915-b7bd-3ba8-9b03-82a3660afb60 | -3.02389 | -51.03718 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84cb5a0e-e249-356c-85e5-6f074be14189 | -3.09276 | -50.55376 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b3c47e-f9e8-399c-afe8-7ec3e4152091 | -2.89631 | -50.49506 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 772b41e3-3a7b-326d-aa71-98d599e1baf6 | -2.92685 | -48.21886 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c8cf55d-7a70-3ba8-bd06-32a82c7039f5 | -3.20318 | -50.21581 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a699826-d0c3-391f-aeab-29f8a8765ae0 | -4.17888 | -49.87564 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0eb2f73a-2bac-3428-aa84-49fb2605e277 | -4.71344 | -43.99636 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dba09b1-b075-32f2-b76c-e1cbf7180424 | -5.75347 | -45.11428 | 2025-11-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6a7f65a-91e3-3f6e-9f6d-09ea4f48de04 | -4.1 | -49.06413 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8b8fc21-1d90-3969-82d1-933065eb136a | -4.82169 | -43.82071 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 242b875e-4bbb-36da-b4af-4edc52434d87 | -3.32926 | -49.72058 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f458ca63-08e5-3d55-bc9e-195d0359931c | -3.6992 | -50.94506 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2df4970f-58ea-361b-8f66-92f2ea996cc4 | -3.36055 | -50.489 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6293493-eb8c-3840-a646-acfc4a5dc431 | -2.93821 | -49.35845 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 65e1fd7f-7d5a-395b-8c11-41212018eaa3 | -4.65315 | -43.96939 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c3749a9-3487-3189-9cc6-378e25270584 | -3.17447 | -48.03171 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6be9b7a7-2aef-3643-8e5e-8172d92aabd6 | -4.66076 | -43.97563 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 505e364f-d9cc-3e53-a7ac-e284d533853e | -2.49598 | -48.15303 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcd81d3c-fe01-3030-b761-6fa073f3cc0c | -2.85211 | -50.73534 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a69997e-bbe9-3427-bf47-4d91e23a9e0c | -2.88933 | -51.81504 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76bf2192-5c83-3a31-8c79-6cb5e18e9be6 | -2.75167 | -51.89916 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1822ac30-b02a-37e9-9dd2-f739d2b2b455 | -4.18176 | -43.71324 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b839b0cf-0659-3fbe-8716-61bfb853e790 | -1.30443 | -55.43447 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0780ae0e-d40e-3bb2-8cb2-fca1eba1177e | -3.18097 | -50.24353 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9ccff7f-74d5-378a-8f27-0b7748864118 | -7.74988 | -44.18794 | 2025-11-26 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51eb8898-95d9-390e-a16f-c74b5bb9863e | -6.77255 | -46.51773 | 2025-11-26 05:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e56b35f6-4ff1-3e97-8110-4369314b8da8 | -2.70248 | -49.51632 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46cbdc32-cbb2-3742-9e24-93c5cde3d8e9 | -2.7463 | -47.13762 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1d8ad5c-96ec-3766-8029-597615c708da | -6.58473 | -47.90451 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11869a91-76e6-3b2b-a2d4-1f258ececb15 | -5.29112 | -43.6427 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f3cec3e-fe01-357b-bed6-184bb9a593d2 | -3.70361 | -45.89423 | 2025-11-26 05:10:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ecd010b-046a-3f71-a324-42dd2909d0e1 | -7.16762 | -44.99064 | 2025-11-26 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6be3b95-b985-30c5-882f-3095350cc185 | -4.16991 | -49.87302 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78252f71-bea0-3fee-b657-fe7521bc2ae5 | -2.48525 | -47.81674 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56634f9b-cf11-3d4e-bdbf-4bfd804a623e | -2.42286 | -48.59539 | 2025-11-26 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9aff9d56-68c6-3724-a9e9-5961db7f4048 | -3.09706 | -50.55445 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bb2b8ed-994b-39fc-90ee-87d41cbc2632 | -2.99528 | -49.59976 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afe28e6e-1fdc-3bb3-a78d-ecdd9d18f0d1 | -4.17148 | -43.73728 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 423d47c6-221d-30f9-a1d1-51af961f2bbb | -4.3729 | -49.76992 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddc4dda3-68a7-3ca2-9f44-1084123db399 | -3.39373 | -47.18536 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e632e064-a288-3344-80b9-be111ac444b9 | -3.24467 | -50.1513 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c503fa0-966b-359a-9506-e8965de62cf2 | -4.66028 | -48.48413 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
