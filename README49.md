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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d38346b-565e-3315-8fea-2bf7d6377fb7 | -2.8589 | -49.55447 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9ba3e7-3088-373e-843f-fd65eb0156f8 | -2.85612 | -49.5505 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e812fece-9dd6-3d85-b4d4-468949e8a4c4 | -2.84515 | -49.86377 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c207cf13-98ca-3380-a53c-bd2077027b1b | -2.84462 | -49.86721 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c89a64b-390a-390d-8d0f-58f68c1d0ff4 | -2.82167 | -49.77145 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d496fab-6b83-3d19-b64f-b8a765154fc3 | -2.82113 | -49.77489 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f21e70ae-15cc-346a-8a20-9f807b528bd0 | -2.82059 | -49.77833 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c58c456-bee2-3782-bd0d-020f9ea62456 | -2.80541 | -49.70192 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ecb318-6420-34b0-94d0-849e74c1df13 | -2.7798 | -49.51749 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 175bbe51-991e-3e00-a0d4-7511acdb76c8 | -2.77896 | -49.82832 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4725301-9a03-34c4-b5b8-6eb1f3e8a010 | -2.77843 | -49.83176 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af014157-1f97-3e3b-9028-f51a6f194a2c | -2.77775 | -49.55262 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a969fbb-d921-3f9c-a07d-a7101ca318b9 | -2.77721 | -49.55608 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8abba3a9-99ea-3c80-96c0-b1b5cbadc00a | -2.77648 | -49.51698 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c597b5ff-0691-3611-8307-1e07d6e7a475 | -2.76851 | -49.83023 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63d51a69-83ec-3897-89a7-fa9a0bed8226 | -2.76798 | -49.83368 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e2e38db-cc43-38fc-8719-21c8d23a6d86 | -2.75476 | -49.83164 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bd2188-3208-306c-8d7a-3314647f933e | -2.75146 | -49.83113 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e519f2c4-4cc8-3c2c-b8bb-5553d0278f1a | -2.74815 | -49.83062 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 321e2242-38d0-3915-b68d-fb64ba5f4325 | -2.74762 | -49.83407 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a62062d4-8c5e-373e-a38c-7f0426c24960 | -2.74278 | -49.55775 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a91945-cacc-3592-9be3-7949af44f63f | -2.73557 | -49.8463 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4782ec7-c2f7-387f-a774-bdd100b30036 | -2.73513 | -49.87087 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33bbef16-ed3c-3f61-ab5a-a96b42015a33 | -2.7312 | -49.85266 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f6f82a-9a73-3c57-8bae-11496d153c1a | -2.73066 | -49.8561 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1677a49-b2eb-3d87-a04c-7cc27c0c1bd6 | -2.72789 | -49.85216 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 57c27fbe-8646-389a-b2bd-a5a1b650e312 | -2.72736 | -49.85559 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a7fa584f-e142-35d1-91aa-2c2830fa4088 | -3.55529 | -50.30536 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc9ac3e4-a655-3753-9bbe-bd8471a97b5b | -3.54753 | -50.2901 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c56abd5-a034-3938-a029-b9afff68ab00 | -3.54646 | -50.29696 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab3b4d90-0b05-315f-9e71-2160c41911e4 | -3.54476 | -50.28616 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85fe41b2-d54a-39dd-bf81-d601946bf2cb | -3.54146 | -50.28565 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3899f0f-64d7-34cb-998d-4b74decd9224 | -3.51059 | -50.28436 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c69801b-4a5b-3406-a562-39507b88d859 | -3.47858 | -50.38132 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c10e2fc3-8897-3bca-a423-4b6028d45213 | -3.47688 | -50.37052 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11e175fb-6fc1-3236-b728-fb12cd0a5e8e | -3.47581 | -50.37738 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4c7901d3-c2cb-3fd7-900e-e73685bb7e23 | -3.47251 | -50.37688 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 75057491-b6c5-3545-b7bd-e00d4ccdbca2 | -3.46992 | -50.28513 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 549abff3-8ef3-3a3d-b1d4-eb2a198c9dc9 | -3.46975 | -50.37294 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b27629e-719f-3341-95a7-eca287254689 | -3.46662 | -50.28462 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cec7e32-07fa-3dab-af6a-44eabc3ff090 | -3.42105 | -50.29516 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecf5387b-7383-35e9-a466-834233749b5e | -3.41704 | -50.38589 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1859559a-58ae-3397-9ac0-b38733ec5f94 | -3.33565 | -50.27435 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| febc14b2-f978-3421-81c9-eabe2115ab82 | -3.33235 | -50.27384 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64ee4de5-07d1-3df7-8201-291f0640675d | -3.32905 | -50.27333 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68002692-892d-32fc-a835-d3eee71e21ac | -3.32851 | -50.27676 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab7f11a6-1c5c-36c5-bc00-4c36aa80a0c5 | -3.32798 | -50.28019 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98d5fa4b-7e17-3dec-9d16-378a4a7d010b | -3.32628 | -50.26939 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72539a16-f4ec-3476-a440-ea19e5d3f5c4 | -3.32575 | -50.27282 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d58f9d2-1ee0-3a19-b1b5-de527a568712 | -3.32191 | -50.27574 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a2e005f-65b7-39b7-ac34-ce3a5f0f438e | -3.27874 | -50.35322 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd1e017d-3ca6-3a2d-906b-a3836098b54e | -3.2782 | -50.35664 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fd672bc-e680-31a5-81ad-661c6178b195 | -3.26714 | -50.3409 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2a2388a-9711-3ca8-b5ff-f384a739ab6a | -3.26384 | -50.34039 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61b6e166-a5cf-3c46-9192-cdc7724bfd6a | -3.25341 | -50.34229 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e4c5b78-ed3a-3d36-b533-1ccb080ffb71 | -3.24734 | -50.33785 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e19f1e95-28dd-3c32-a51b-9f453f7fdec7 | -3.21586 | -50.30138 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2a626c6-453a-362c-85e8-16c7db5c2be9 | -3.21194 | -50.28321 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b8418632-fe70-3dbd-b672-77e36bce985a | -3.20917 | -50.27927 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ff89ee1b-d6cb-3b52-aca9-a4000c283877 | -3.1999 | -50.29541 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abe912bf-be3a-37eb-83e3-33c44061bc9d | -3.14223 | -50.35668 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9eef49-7c39-3ac7-abda-f152147e24e7 | -3.14001 | -50.34931 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d0c3cd9-2e16-3292-a24d-a76b1dc3d038 | -3.11388 | -50.27855 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8fe6af4d-4105-38c6-90ec-8dd98ec60da5 | -3.1112 | -50.2957 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fc56a09f-cf55-3839-b36f-3f3e654838ce | -3.11058 | -50.27804 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 60363970-fa9d-33cf-88e4-25d97578ee04 | -3.1103 | -50.21479 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f9e3f8f-ffb3-3db7-927a-87a33d687a3c | -3.11013 | -50.30256 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 801d5600-f071-3425-9fdf-0fbd7bc05205 | -3.11004 | -50.28147 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1140efd0-22c3-3cca-a3cf-21e7532ca694 | -3.10897 | -50.28833 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1341def0-2206-3d4d-a702-f1ce8b35b39a | -3.10844 | -50.29176 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5805857e-17d5-3b92-9629-8ade9940ed3c | -3.1079 | -50.29519 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 68c2302f-c011-3c8f-b1e1-b129f4cc2c30 | -3.10737 | -50.29862 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fa15695d-ee59-33f1-a5fa-7e8cc2045898 | -3.10728 | -50.27753 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 251bd06a-e678-3105-8d5e-000864f33812 | -3.10674 | -50.28097 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4a6d9993-6647-382f-81e1-40c561c79f2a | -3.10567 | -50.28782 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 59389b29-eb4f-3c25-aea2-d7fb4693f593 | -3.10514 | -50.29125 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8571caad-70ca-3712-9cb6-4020057e6d34 | -3.1046 | -50.29469 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 08f62302-fc50-351d-8b80-d53708fdda84 | -3.10451 | -50.2736 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b56b4b7a-e80c-3f92-8bf3-0d4df0d50cf6 | -3.10344 | -50.28046 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e1cdd53c-7154-311e-990f-42db5c0e7b51 | -3.10291 | -50.28389 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5e8b65ba-c535-3313-b866-9fb62733b081 | -3.10121 | -50.27309 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d7be9034-1c34-3243-9578-50f375399f35 | -3.10077 | -50.2976 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6cb231d7-33d8-3ced-81eb-d70a1c9f8ec5 | -3.10014 | -50.27995 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 713de50d-930e-3899-ae35-1ada1906f76d | -3.0997 | -50.30447 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c6a68f1-025c-32d2-b7ea-b07dac6f9a2c | -3.09961 | -50.28338 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 16e35fda-e4d5-3d4c-93a8-8d757f06df27 | -3.09907 | -50.28681 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d704699c-30a2-3dd0-be2c-e2e7b7ed0ac7 | -3.07577 | -50.2368 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c528da86-6c50-3ae9-b129-10c7bfac376d | -3.073 | -50.23286 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d19286ae-b3a8-3ba7-aa1b-7e0862749f23 | -3.06586 | -50.49951 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ed91fae-caf8-3e7b-8ff9-80b23191be48 | -3.06533 | -50.50294 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20c237f9-1d74-375b-80de-a654b536b80f | -3.06202 | -50.50244 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3a153cab-f99b-38bb-8615-d7a982c3dd9d | -3.05872 | -50.50193 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d7b9126-78b4-3117-9fdd-27f074c66cdb | -3.03698 | -50.42048 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80b7fb6b-e99d-3b6e-a288-e83c92191385 | -2.98282 | -50.48593 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0708992d-a336-342b-bbd0-7efb661390a5 | -2.98258 | -50.29268 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48682e62-b33e-3a6c-8ed0-3e7eb7422966 | -2.97952 | -50.48542 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d25a0a0f-829b-3316-b4b5-e35afddf54b5 | -3.46528 | -50.4882 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfdd6a63-353f-323a-a4a3-79ea5b8e9737 | -3.23832 | -50.54729 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b7d8087-4ae4-30ff-98d2-f56923f73be3 | -3.18183 | -50.5843 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36bc952f-bd5f-3fdf-9f97-5d9093c11ccd | -3.18129 | -50.58773 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
