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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 219c3617-e63c-3836-8262-131b86159bca | -3.61776 | -47.28453 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e96e8be-ab69-3c46-a150-77ec2fe6b439 | -3.61721 | -47.28814 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f82e5c4b-7a63-3763-a5e8-032bd84238d3 | -3.61665 | -47.29176 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35ced0d5-7dff-33d0-a452-74b431515080 | -3.6161 | -47.29538 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ee629eec-dd9c-3674-9234-15f23155dfcd | -3.61576 | -47.28453 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edae1eb5-e4d6-357e-9f1a-78a19f45d3d1 | -3.61555 | -47.29897 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b82a32a5-d6fe-3e3d-994f-a9fd8c0a2c22 | -3.615 | -47.30254 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71a7ba73-1f0e-3561-b0dc-77f6353744f4 | -3.61463 | -47.29177 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6973a461-4551-3278-a22d-b5637cb09d00 | -3.61406 | -47.29539 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e5a5836-f685-379d-9339-61da50388d7d | -3.61352 | -47.2548 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6600d358-9d2f-34fb-b36e-b89940268b37 | -3.6135 | -47.29898 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 796883f7-0941-3910-9c3f-787c88fef447 | -3.61294 | -47.30254 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4baf905e-d83d-3fee-a22f-780354a47728 | -3.61071 | -47.25069 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6449551-1d08-3278-92e6-d316cd990a33 | -3.61069 | -47.29487 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32319f23-0e91-3fea-a8df-2ec6c9ef977c | -3.61013 | -47.29845 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06a1317a-53e5-371f-955e-3a306c07f063 | -3.60957 | -47.30201 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 840d4bd8-b7d8-354a-ae47-540e1c712c61 | -3.60791 | -47.24657 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8800e4ac-c888-3d2c-aff4-0ff52cb5c956 | -3.60734 | -47.25018 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a734955-3c92-384b-92cf-b328011a6755 | -3.60733 | -47.29434 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24f684f9-3a61-373a-884c-159865f05a15 | -3.60677 | -47.29793 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2631a538-b295-335d-af33-dc93049bbca9 | -3.60621 | -47.30149 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82725913-b780-33aa-953a-d17fd32ff9c4 | -3.60454 | -47.24605 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67c408e8-40ae-35a2-b71e-4a20a550a12d | -3.60453 | -47.29018 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 481dff0c-d5f3-35ba-b566-56f809b91c83 | -3.60397 | -47.29381 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49cbfd22-dd19-3f0d-a9ad-d73b49d3466f | -3.60397 | -47.24966 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b176f79-3cfc-310c-ab17-dcfa674b2d59 | -3.6034 | -47.29741 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0543124a-77df-3361-9320-bb906e274045 | -3.60284 | -47.30097 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45fd6d75-bf95-321c-9ae3-0a5269bc6418 | -3.59499 | -47.28506 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a7e2fc4-b7fc-38b8-9ad8-61036d99b3f4 | -3.59218 | -47.28098 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc739a58-2484-357b-99c4-a6be8fcb9961 | -3.59162 | -47.28457 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a6cf664-4165-349a-a3a5-6db079beb5b3 | -3.58825 | -47.28408 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d0530fe-6150-3ade-a46a-df08a9143cc5 | -3.58769 | -47.28767 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3dfefdb-69d1-3d78-b365-1c00e08fb7f3 | -3.5491 | -47.3586 | 2024-10-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c10ddef7-0c1a-32d9-b058-a2c7cc210f5f | -4.35035 | -46.78303 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 358c6f5c-d685-33f5-b417-747411e242e7 | -4.34977 | -46.78687 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6cce1fd3-90d6-363a-91b0-8f2405b7a3fe | -4.34928 | -47.31186 | 2024-10-29 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aea07774-1598-3c98-a2ad-19cc58090469 | -4.3478 | -46.77945 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19da70ba-bba2-3c4d-b69b-d97bb56dd6ce | -4.34633 | -46.78631 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| dbb6d2a8-ac0d-39cc-8a58-ed0577ed2ac5 | -4.34317 | -46.78656 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e4d1f3a-f119-3fa4-9e4c-3874fa32c24f | -4.3348 | -46.70416 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c236431-6e2f-3572-aa11-406346742e38 | -4.23938 | -46.86668 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17ca073-e482-3d8a-be68-6a53c0ba7df3 | -4.21709 | -46.87536 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a295ea5-f4ec-3698-a2b8-76457f026e0c | -4.21651 | -46.87908 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 147f6598-32b6-3565-8326-5c8b0a481a44 | -4.21365 | -46.87486 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1057f78d-d732-3a2a-9dd7-d0dc3accfa2a | -4.21307 | -46.87859 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9f22c84-156b-3ec2-aa7e-db3a16b61115 | -4.13375 | -46.89291 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6468c271-e73f-31bf-9d98-079bbac5656b | -4.13318 | -46.8966 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ac9a89b-3f72-37b1-83d9-2bb7a8cba02e | -3.95939 | -46.4113 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b58d3be-9ae8-3b4b-86f7-24699a794f47 | -3.9559 | -46.41079 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 766e9b2d-b593-379b-a24c-a9f8e25f0a1b | -3.95365 | -46.40232 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b4e0688-60a2-3ac4-b8df-18e3ec77cc68 | -3.95304 | -46.40625 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b7a7e9b-40e2-3f7b-8cd9-d1c61e9e674e | -3.95122 | -46.41796 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df805a9a-11b0-3db5-88e1-b30007c6ce25 | -3.95018 | -46.40172 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eabd0d54-0b7d-3acf-a52c-9b8b6cb4cac8 | -3.84425 | -46.45273 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09f73f6d-3eba-3a53-91e6-095886c91772 | -3.82909 | -46.48163 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1852a06d-3316-3b5f-a150-374b8c9c570e | -3.82504 | -46.48486 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d15a041d-7d5a-33ac-8d0b-99ac05fa6dbb | -3.8245 | -46.46545 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a58a7ee-c34f-31e7-a4ad-135ec2fdf673 | -3.82046 | -46.46865 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62780e9a-9b5b-3138-b6cb-d596d127969c | -3.81928 | -46.47622 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ade5d85-14ff-3af8-919d-25e9c5db1a1c | -3.8187 | -46.48001 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffc66672-e407-39f8-ad9b-a032496ad6b0 | -3.77708 | -46.49683 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d527103b-5042-35c1-8c94-c8e90b43b20c | -3.89287 | -46.33335 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 570fc960-77c0-3772-b1a9-5e0f7618aa5e | -3.8911 | -46.34499 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b24f52a1-0cb5-3170-b15c-558d19ed4df2 | -4.32917 | -47.57339 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12e08d00-1272-3256-bd2a-0c179fad53cf | -4.44317 | -46.63859 | 2024-10-29 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48c1c818-c2eb-3b25-a649-4688061e1919 | -4.42603 | -46.28269 | 2024-10-29 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f97ce18-0aad-3c94-8a8d-f3693e5b7a89 | -4.4251 | -46.28368 | 2024-10-29 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9caf8a65-d614-3778-a9ec-42e56a4064e0 | -4.35893 | -47.0929 | 2024-10-29 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cebc3807-d724-3899-9e6d-6492f82426cb | -4.3472 | -46.78327 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e5cc6846-1434-33ad-af39-10a57c2e935d | -4.34691 | -46.78248 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 96201e37-71c9-33b0-923b-43e720606e85 | -4.34661 | -46.7871 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a70185be-ee6f-3092-9daf-02a79c8188e7 | -4.34376 | -46.78273 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0bdf2736-2c77-362e-8a68-194b83e4350a | -4.33408 | -47.25356 | 2024-10-29 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d256791b-ece2-3afd-bbd0-6e402e111bc1 | -4.27713 | -46.28213 | 2024-10-29 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b63febc-2e4c-3513-86c1-56a5e381017e | -4.23595 | -46.86616 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3472887-75ce-349c-b565-118b9de22266 | -4.13033 | -46.89236 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b051fa8-d608-3689-897c-d67dc1511fa8 | -4.12976 | -46.89605 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2322ee0-7e5d-3409-bd76-6df86b2e4516 | -4.12634 | -46.89552 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e478c3fe-e434-3178-8970-057e3522eb46 | -4.12349 | -46.89124 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e36b9d36-45c5-3d8b-945c-8ad848860122 | -4.03034 | -47.21843 | 2024-10-29 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b0d916f-3810-3fe3-b102-02d6b958f629 | -3.98918 | -46.48518 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac35ec3b-aa7a-3b2e-bf08-4ad2f0455f58 | -3.96001 | -46.40731 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f445f3c-3878-3cbd-8031-d215647f609f | -3.95652 | -46.4068 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8dc96e8-3c21-3d03-a512-500452792c61 | -3.95411 | -46.42231 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0b9e187-66e6-3937-8b77-fe54d5ee0493 | -3.95243 | -46.41022 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c84c98f-9e63-3353-907d-4dc9b0b64e6e | -3.91168 | -46.44342 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ac2cc13-88b1-3552-9d57-7a54fe196482 | -3.90762 | -46.44669 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b1a6781-6582-3f54-9d10-ce1f2d51590b | -3.89459 | -46.34554 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0a16d3c-6511-314a-b5d9-2db3114324a0 | -3.89228 | -46.33724 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b4905a7-71d8-3d22-8401-d1e7d59abb80 | -3.87204 | -46.63197 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 063865d9-89ae-3104-8ef6-59361fd4b033 | -3.86227 | -46.62664 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ee403db-1731-372a-a9a2-0e5272ddef90 | -3.86168 | -46.63046 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee4a5ab0-4ee0-32a1-a67c-e09a9ac25eae | -3.8611 | -46.63423 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75d9ed44-5d1b-3671-b3bc-f56dc076b227 | -3.85549 | -46.48554 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7674fb9c-421f-395c-b7b1-7cd2e65c2f3c | -3.83256 | -46.48217 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f5e0cb7-d9d8-3870-bb03-e0d9864a1f51 | -3.82783 | -46.94153 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85ff2db7-097f-3714-94ed-817548788fe1 | -3.82509 | -46.46165 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f5bdac-2015-340b-9a5c-e4a69f2967eb | -3.82274 | -46.4768 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67938116-064e-315c-a3f9-1bdd4c9fffa3 | -3.81987 | -46.47243 | 2024-10-29 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d348ba2f-7868-3397-8aed-89bbfab4b4a1 | -3.80566 | -46.9269 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README39.md)
