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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8444ad48-0eac-3a6e-9497-8db8f2be5c9f | -1.02869 | -53.73649 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa5b77f6-31eb-3175-857c-76d86d9520bc | -1.02629 | -53.72726 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5507d650-8927-3ba5-b13b-de083237bf0c | -1.0256 | -53.73162 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae37a4ea-d3be-3141-9305-239b340f4903 | -1.02491 | -53.73594 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcfdbab0-ac5b-3e2c-919c-d8dd9920ff69 | -1.02257 | -53.72641 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 047a1ea5-c617-3ff9-812a-4a7971c1c7bc | -1.02186 | -53.73086 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9801fb33-c094-308a-ba90-0d80199a4d09 | -1.02114 | -53.73535 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dfe600f-915f-3b14-9143-4b55b99853f8 | -1.78113 | -54.88309 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1c5a92c-40bb-3f8a-bb07-aaec162e4c42 | -1.7796 | -54.88242 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32164974-78fb-31af-b37d-fdcdf1cf08c9 | -1.74336 | -54.24229 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3bb62162-fd9f-33f5-ad79-aba3600161f6 | -1.7426 | -54.24711 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4f6e1f1-b2d9-3f7e-a956-9f8c13691dd3 | -1.74185 | -54.25189 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9e9edea-8d6e-330c-a531-fc9a7b53e555 | -1.73951 | -54.24165 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c9e59ebf-407e-3680-b27c-510da2b37941 | -1.73875 | -54.24648 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb9f4b41-2485-374d-b867-67b82536196f | -1.70808 | -54.39046 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019f1c4d-5ec0-35c1-a9ff-999a7f803c94 | -1.7042 | -54.38981 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b2caa0f-b069-3707-bf75-7c75764cce34 | -1.69255 | -54.38781 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6faf2443-81b4-3fce-837d-12412af31914 | -1.68868 | -54.38712 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a902a80d-299d-33a8-8498-e48adb6c043e | -3.56452 | -54.02894 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c36c486-3c88-3ed8-97a8-51d11050785f | -3.56447 | -54.33832 | 2024-10-10 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd505571-b5dd-370e-8751-8f16be04f7b3 | -3.56372 | -54.34299 | 2024-10-10 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43de9e45-a721-39ab-8be7-148bd08f7093 | -3.56299 | -54.3476 | 2024-10-10 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81cb0e7f-9573-3680-a539-a39e3b59980d | -3.55922 | -54.34692 | 2024-10-10 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9880bfde-8a7f-3c3d-8244-fbd4ec0c4d99 | -2.76676 | -54.04097 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b70094-ad01-349b-a7f2-fc275c64487c | -2.14307 | -54.85933 | 2024-10-10 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11f49087-5446-3fdb-a232-c13caa325030 | -3.27247 | -54.17686 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94083a5d-9266-3c0c-b9e6-61198abd1c84 | -3.25978 | -54.18393 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 64decf3e-c8f6-39f9-bfba-9943c683e13d | -3.25906 | -54.18838 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8b61aaf0-c680-39a8-9cdc-f32383acffc8 | -3.25835 | -54.19285 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c80c639c-5d72-3956-befe-1acdcf67cec1 | -3.25763 | -54.19735 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f1fd999-9e31-330c-bbbf-51cb8a783f8f | -3.25603 | -54.18327 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 88cd965b-3334-3852-98fb-bebaf7f70820 | -3.25532 | -54.1877 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 50d6385b-ac8e-31d3-b844-5b22ed201f77 | -3.25459 | -54.19221 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0c085ee-6331-3c68-bb1f-83c8b47b2c16 | -3.25387 | -54.19674 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f488348d-c998-3007-a033-569796c4956a | -3.13298 | -53.73605 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c82f3504-4691-3f97-8eb8-1fc0f0c635ec | -3.13229 | -53.74036 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 649c8ee8-6605-3b21-911d-7aa8f000dfff | -3.12931 | -53.73544 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddc38dd0-bd1f-3578-9bd9-45afcd0de061 | -3.12862 | -53.73977 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b532288-3307-3ca4-b0e6-ce4b34eef8fd | -3.12564 | -53.73485 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 408e7b1e-68d1-397a-a223-5ac5eee25489 | -3.12495 | -53.73917 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa21f5de-92c5-32ec-b830-50027abf5297 | -3.12197 | -53.73426 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebe6d5a-cb5a-3cda-b140-55ed6f464016 | -3.12128 | -53.73858 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eb7dbcd-522a-32b6-91ad-ce931c55dd8d | -3.1206 | -53.7429 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5d6e51e-ca10-3a11-b6ca-90372cb5c551 | -3.1183 | -53.73368 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aad761d-a61b-385f-b58d-eac24c8ea952 | -3.06839 | -54.77637 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 490b60b7-c74e-350c-85e0-9f2cfdabb36d | -3.06448 | -54.77576 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88d21fb-4ec0-3914-9918-7fc92848b98e | -3.02325 | -53.86287 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad3fa8bb-8892-3fc7-8ec1-58cf1524fce0 | -3.02211 | -53.8612 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55eeb2cc-29e8-3897-aea1-02c0c4f38591 | -3.02022 | -53.85799 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7fcd7b1-4ef5-3310-b57e-e7557cc1752c | -3.01955 | -53.8623 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f9a659b-7928-3edf-a0d7-9a96b9fb27db | -2.97768 | -53.72153 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddebd630-5747-32b5-bb7d-ff6f44475746 | -2.9747 | -53.71664 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0e6835d-0afc-3b75-b93f-992d28af11f3 | -2.974 | -53.72094 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4653f53e-7b07-373c-bbd8-ea6d8e1d9290 | -2.95039 | -53.7039 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d3a0adf-febb-3dae-8101-4db1d869b0a9 | -2.94714 | -53.70517 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29d82a0f-ea25-37ca-b104-e02386e62d20 | -2.94672 | -53.70331 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38c9aa9e-766d-3618-9e58-8e906a7b4e32 | -2.93551 | -54.17501 | 2024-10-10 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfdebfd8-c5ec-3cbd-9c15-ad6ad8057f34 | -2.91949 | -54.13033 | 2024-10-10 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e293aab-bbcd-353a-a328-cbd3bebab1da | -2.91387 | -54.04586 | 2024-10-10 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9be3cd-0a5b-3947-9d4f-7e6c6cdfc6d5 | -2.89113 | -54.25813 | 2024-10-10 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d4d85a3-b559-3c64-83a0-22c55a1217bf | -2.88855 | -54.49393 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ec89b2-d2eb-35f4-9f8e-345c16a1758d | -2.8847 | -54.49328 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c9512bc-15a2-318a-9447-14a6f8911553 | -2.81744 | -54.01879 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6634d762-d147-39e5-a1cf-9774af7faf25 | -2.81623 | -54.72123 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96281fef-f351-3f7f-9e03-a8d9aa19eafb | -2.81279 | -54.36294 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08c02b67-bfbc-3348-a368-a68656df4232 | -2.80123 | -54.5862 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e54ee8a-05a2-3362-874b-610cdbfd12b0 | -2.79735 | -54.58558 | 2024-10-10 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6cfbd5-db2e-3140-ac81-3c672d778c6b | -1.25296 | -55.70498 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a3c348ba-4e02-3a2a-8ab8-9a03b9a265bc | -1.24996 | -55.6964 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f946b17-d24b-30b5-b713-07ecd9724166 | -1.24934 | -55.70027 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 522da3e9-0a37-3b9a-8997-5399188af421 | -1.24872 | -55.70415 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8a1834ca-93b5-3f38-88ce-0619fd49c149 | -1.24806 | -55.70823 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c68052c-f026-32dc-9bca-6f5c621a174e | -1.2457 | -55.69571 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf79f9d9-0236-3f0d-8cd8-c224e9a9f1da | -1.24508 | -55.69955 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0e5b594-004b-3aa5-8fa5-548cb370e011 | -1.23781 | -55.69038 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88cd4a2e-bf82-336e-a50b-77dd14463e7a | -1.76484 | -54.97729 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8821356e-4ef3-3aaf-81dd-9b50b8e3ef00 | -1.76167 | -54.97712 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a05402c-0c4e-35ab-8ea1-3485f844a584 | -1.76081 | -54.97664 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f06e6db6-9d52-3ce8-a2e0-3bb51329cb9c | -1.67282 | -55.11245 | 2024-10-10 04:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7858893f-dc40-3fab-804e-d52ddd99d977 | -1.67192 | -55.65805 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40157ed3-eace-360b-a594-4d6ddd052c0b | -1.66875 | -55.1118 | 2024-10-10 04:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b27e14bb-b00e-3bdb-a7e0-a501509c1e9e | -1.62046 | -54.91814 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b86bad3e-da1d-3f97-b2a4-6d9df83d6950 | -1.6199 | -54.92165 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25740f55-b834-37e8-9500-37bb78263e0e | -1.5198 | -55.41809 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 681b74ff-5276-3965-8d39-4a3bd9c57d12 | -1.5192 | -55.42187 | 2024-10-10 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4677279-2d78-3eec-ae37-8d47a6eddbf2 | -2.08697 | -56.71503 | 2024-10-10 04:42:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c236c66e-893b-30db-adbd-fe34c800d2ca | -2.08622 | -56.71973 | 2024-10-10 04:42:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d5a5a59-1e7d-3e78-b915-f2d7e0bd253d | -3.13993 | -57.06201 | 2024-10-10 04:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f346c31-502e-3fa7-b9b3-35056e9b0814 | -8.99462 | -61.62391 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ab8f182-6c4f-3f9c-9fac-2c24c6728227 | -8.98975 | -61.61895 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbace4de-621d-311b-beeb-5079c3978f00 | -8.98903 | -61.6228 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0df93436-7859-3005-adf8-161cc42a7db2 | -8.9883 | -61.62668 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1319e86a-a16a-3a28-8333-b45dc9faceaa | -8.84384 | -61.49125 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f92c0b72-00e3-3de0-8ff9-d7a019e51e2a | -8.83828 | -61.49017 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d70abb7-15d3-391d-ab12-db30c9beb360 | -8.23653 | -61.17908 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 695760ab-79b3-3084-9841-b405ead46cf1 | -8.23586 | -61.18276 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6f64f2a-a984-3b7d-b40a-8b85ae17bff5 | -8.23519 | -61.18643 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497e0729-3109-346e-9f6a-ac5e612c8a35 | -8.23453 | -61.1901 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb226fec-0caf-359f-856c-80c6fe69adbe | -8.23386 | -61.19375 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8e6a6d2-e880-3e45-840f-2d33c25ed080 | -8.2332 | -61.19741 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README95.md)
