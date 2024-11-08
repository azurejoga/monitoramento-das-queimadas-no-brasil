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
| ca68aa53-cfdb-3bf1-8cce-5f46c8b72db2 | -3.5446 | -47.3855 | 2024-11-08 05:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3704c6b6-e7fc-37ed-99b9-68cf3abd2e20 | -2.82 | -52.9409 | 2024-11-08 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 628e8e56-91f5-37a0-8468-07bc1b962eae | -2.8016 | -52.9414 | 2024-11-08 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 225fd070-fa81-3fd2-a9c7-4f9c8f4080a3 | -3.068 | -50.5631 | 2024-11-08 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e8a8f37c-56b0-3eb8-a1b9-98093710f779 | -3.9669 | -48.1716 | 2024-11-08 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| d4c27cc4-ebd9-3270-8e4c-9b291234de9b | -4.6835 | -46.4074 | 2024-11-08 05:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 751e682c-18d9-3176-a285-a959e0507078 | -4.6835 | -46.4074 | 2024-11-08 06:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| adfa5ab9-c4c6-3ce4-ac84-575947b29574 | -3.068 | -50.5631 | 2024-11-08 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| a82f1e40-c5eb-3209-885b-035424be4b2d | -4.5209 | -45.6804 | 2024-11-08 06:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 0b0fc6a1-21e2-37e3-bfbc-7f70e6ad870e | -3.9669 | -48.1716 | 2024-11-08 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 176fd54b-cdf4-38b2-beae-3d02575cd90b | -2.82 | -52.9409 | 2024-11-08 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7d24bb77-1c68-33bd-b136-ab06c606d587 | -3.5446 | -47.3855 | 2024-11-08 06:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c509dcae-8287-3b5f-8867-35c73ce6294b | -2.8016 | -52.9414 | 2024-11-08 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 342c425d-47e2-30ed-b327-e34b9319a7f1 | -3.5631 | -47.3847 | 2024-11-08 06:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e30499f2-9d96-347d-91d9-fc5ad2d666f6 | -3.9669 | -48.1716 | 2024-11-08 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| acf9c4e7-4c21-32bf-9ec6-857f5b93941d | -2.8016 | -52.9414 | 2024-11-08 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b9715990-f0ab-3552-aa4a-e067df6b9a34 | -4.5209 | -45.6804 | 2024-11-08 06:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| cde742fa-d04e-3bd4-ab83-4e2011288086 | -3.5446 | -47.3855 | 2024-11-08 06:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3017c134-e606-3d02-a760-8b419af62854 | -4.5209 | -45.6804 | 2024-11-08 06:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| fe9c6541-47f0-3d33-be0e-985e7f6ca0e8 | -2.8016 | -52.9414 | 2024-11-08 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c80ab959-a105-3b00-988b-73a44fa7fa01 | -3.3833 | -50.2177 | 2024-11-08 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| fe5cd66f-afd2-3d9e-9ec9-bd2223e84d1b | -3.9669 | -48.1716 | 2024-11-08 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 1ef3127e-15fe-30b1-9bad-e5e10ab8ce89 | -3.967 | -48.15 | 2024-11-08 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| cf670281-0b50-3b12-a8d5-ba8c56ad1d56 | 4.34366 | -59.82995 | 2024-11-08 06:29:00 | AQUA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4dd5ea60-d81c-3486-aff4-c848c92314b9 | -3.9669 | -48.1716 | 2024-11-08 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 68f93cfa-352f-3ddb-969d-0e491d517b51 | -4.5209 | -45.6804 | 2024-11-08 06:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5f226f1e-9dc2-3172-8025-1808ff148f66 | -2.82015 | -52.93571 | 2024-11-08 06:31:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 376bec29-4464-3db8-b747-00bd93f41a56 | -2.80313 | -52.93289 | 2024-11-08 06:31:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9d08010e-b9c1-3773-9c7b-384745db2664 | -1.15422 | -53.64077 | 2024-11-08 06:31:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 28a8fbbc-6e64-324b-adb3-8f60aeca6fb2 | -2.8016 | -52.9414 | 2024-11-08 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0cac74d2-9a82-36e7-be34-75a23b750d3a | -2.82 | -52.9409 | 2024-11-08 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 619953e0-d2e5-343d-875f-ee633f63b3cc | -3.9669 | -48.1716 | 2024-11-08 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| f7b81e89-fdb5-38f2-8c5e-ad802742440f | -2.82 | -52.9613 | 2024-11-08 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d4c29ffc-3ae5-31be-bb5e-df6de6bf44fb | -3.5631 | -47.3847 | 2024-11-08 06:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4f629ab0-ace1-34e5-a452-58bdf5bbb9bf | -2.8016 | -52.9414 | 2024-11-08 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 07240081-228b-3545-8b72-68ee287ad867 | -3.5631 | -47.3847 | 2024-11-08 06:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3ab3f777-3d34-356a-b6dd-64a397ed04d0 | -2.8016 | -52.9414 | 2024-11-08 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 512c5d55-3132-3a10-bbab-cdf2b49379f9 | -2.82 | -52.9409 | 2024-11-08 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 09167d46-7ab0-309a-9f6c-8eaa582491ad | -3.068 | -50.5631 | 2024-11-08 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 7e3ece2f-40e6-3497-8fef-1b5a80e864a7 | -1.1467 | -53.6573 | 2024-11-08 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 14595769-9dac-3cd6-83b4-c39040de4bc1 | -1.1467 | -53.6573 | 2024-11-08 08:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 6e0d362c-3a00-3da5-9a29-eff0aefa1b02 | -1.1467 | -53.6573 | 2024-11-08 08:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e12e75e2-7abc-3d71-bc5c-b6888b74cf63 | 0.0277 | -49.4311 | 2024-11-08 10:50:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8d79273d-1dc3-3c88-b2aa-025926729733 | 0.0277 | -49.4311 | 2024-11-08 11:00:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fa145983-4fee-359d-ab25-3cc7a1e377dd | 0.0277 | -49.4311 | 2024-11-08 11:10:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| c5237439-f1b5-3584-9994-0b17e67a942d | 0.0277 | -49.4311 | 2024-11-08 11:20:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e75f46cc-dbfb-30b7-b7ae-8c4bbf8293e0 | 0.0277 | -49.4311 | 2024-11-08 11:30:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 79f5ee13-4524-3dc7-89e0-0659c9916f6a | 0.0277 | -49.4311 | 2024-11-08 11:40:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 4873db36-65e7-3383-bc28-eee050036564 | 0.0277 | -49.4311 | 2024-11-08 11:50:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 2e537ba9-3947-35e0-873f-ccea66bbfbca | 0.0277 | -49.4311 | 2024-11-08 12:00:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| af62e0df-264c-3ff8-9bed-0b0f6ef2b4ec | -5.45 | -43.24 | 2024-11-08 12:00:00 | MSG-03 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1228996-802e-3322-aa91-e535e0650d2f | 0.0277 | -49.4311 | 2024-11-08 12:10:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| ebfbae75-432e-3cd4-b86e-ded9ee987954 | -1.5164 | -52.1696 | 2024-11-08 12:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b42b7f7f-8a13-37cd-a4a9-3ec5896e597b | -2.96194 | -43.85319 | 2024-11-08 12:18:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 31e85112-fd04-3ac5-9bf7-3fa24d2a0a0c | -2.9604 | -43.86382 | 2024-11-08 12:18:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b849ddb5-50e5-3374-88cf-183bc21cb25e | -2.99704 | -42.27799 | 2024-11-08 12:18:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d5a445c6-c8f8-3ca8-8863-9c49217d7711 | -3.36079 | -40.52702 | 2024-11-08 12:18:00 | TERRA_M-T | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 32.7 |
| f11ec7f4-41c0-3317-b8f0-8f5392a3cccb | -2.08403 | -46.17679 | 2024-11-08 12:18:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8f754867-1c97-3414-b19e-a2d195cd1e59 | -3.06199 | -41.13058 | 2024-11-08 12:18:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 7943a3b0-23e5-3443-93c3-8b1e1e39574e | -2.17039 | -46.43299 | 2024-11-08 12:18:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a127f3d7-09be-3265-9402-192436c323d1 | -2.6764 | -51.8189 | 2024-11-08 12:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 209c4abb-43ee-339e-848c-ee9cc84c3e83 | -2.8016 | -52.9414 | 2024-11-08 12:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| b7a6b75e-8d06-3e45-aedf-2dd2037f4984 | -3.546 | -43.6126 | 2024-11-08 12:20:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 5b1fd4d4-f742-3806-81d7-e1e67556fb31 | -1.5164 | -52.1696 | 2024-11-08 12:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 636d0410-4bc1-3ff4-ae98-db6f9f31a1bf | -3.0865 | -50.5625 | 2024-11-08 12:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b25f9e70-676c-3d00-af70-17cd1f7758a3 | 0.0277 | -49.4311 | 2024-11-08 12:20:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| e0977e36-8248-341c-9dc8-94d55b10ada0 | -3.068 | -50.5631 | 2024-11-08 12:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| d54d38e5-3768-36bf-8c51-81116e85754f | -2.6388 | -46.7597 | 2024-11-08 12:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1812dc24-5f94-3455-9e0d-9eb7d5712ffa | -5.87347 | -43.17448 | 2024-11-08 12:21:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 1c992ce2-1da8-38b1-8a4b-479f586bf100 | -3.6009 | -42.56557 | 2024-11-08 12:21:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| a6d5e1ca-5dcc-3d34-8a0c-9e57c8726bd1 | -10.54199 | -36.9753 | 2024-11-08 12:21:00 | TERRA_M-T | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 534c0c05-d286-3446-83a6-3b80db4efed6 | -9.76137 | -43.59243 | 2024-11-08 12:21:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3f1f80a1-26c9-3eab-9621-3a59bd21b558 | -7.36599 | -41.02372 | 2024-11-08 12:21:00 | TERRA_M-T | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| cf7ada1a-2d0a-3f9a-a8c8-362e9be9d844 | -3.29673 | -43.51842 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9f18093f-2ff9-3414-8a35-2b72aab37307 | -5.4365 | -43.26179 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 1fafec72-4550-3eaf-9793-1ad7d0376703 | -7.06405 | -39.88363 | 2024-11-08 12:21:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1786eb61-6da4-3fb5-8772-9d7fdd321287 | -7.6316 | -35.22597 | 2024-11-08 12:21:00 | TERRA_M-T | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| be0e64cc-2b6c-376a-9951-f1abc5e7d790 | -5.54611 | -41.68906 | 2024-11-08 12:21:00 | TERRA_M-T | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 363c8d2c-b618-3c2a-bab4-2b3dcd1f4dd8 | -3.65799 | -42.61735 | 2024-11-08 12:21:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ffa56eef-bb3c-38a8-8d64-81292fe9d96b | -6.69411 | -41.46521 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| ef2d7ee3-659f-307b-93c1-3a13bcd16a5b | -4.43944 | -43.63993 | 2024-11-08 12:21:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f37a8f39-d682-3767-ae1b-7552c9446942 | -5.41762 | -43.3268 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c77e7505-1129-3631-9f55-27c7f834ead2 | -4.93993 | -43.63188 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6850e5bb-2f71-3068-a232-2af19b518d1f | -5.44701 | -43.2536 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 6a938467-9550-36ec-83f0-9a1ac81ca53c | -3.47206 | -42.18272 | 2024-11-08 12:21:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3dca8903-23f5-3edc-b57d-420aa82a20a6 | -3.34838 | -44.43333 | 2024-11-08 12:21:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 45de8413-4a45-3e95-b6fa-931dbdebc9a2 | -9.76273 | -43.5833 | 2024-11-08 12:21:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e4d1b336-fff4-340e-aa75-19fb6d8bc134 | -3.5883 | -43.02802 | 2024-11-08 12:21:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1f36c59c-4609-323b-831c-38bbe27149e3 | -5.73989 | -41.99883 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 19c24970-e318-3572-b626-937fc54d9791 | -3.60405 | -40.57084 | 2024-11-08 12:21:00 | TERRA_M-T | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a8d3af51-9ae8-3728-9925-bbe2bce82bd3 | -3.53408 | -42.07838 | 2024-11-08 12:21:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 08111c4d-4a17-3c2e-a176-feaebcebe558 | -3.83683 | -42.14913 | 2024-11-08 12:21:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 27539276-263d-3d04-a765-41abe4976a86 | -7.47781 | -43.55648 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ad536b15-e91e-30e7-be95-db70ea21837f | -5.5474 | -44.32059 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| a583a50f-fcf2-3c42-aae6-ad9f42022756 | -3.36181 | -41.48428 | 2024-11-08 12:21:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4ae1a515-b5b3-3c7a-82ff-611a9e395cff | -7.47641 | -43.56589 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| bb4b1a06-49a6-32c2-bc93-17e61c9bcc41 | -8.77224 | -40.38696 | 2024-11-08 12:21:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d6191887-43cd-3cc1-9e48-0cfa287fd7a4 | -5.43789 | -43.25232 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 426.2 |
| 31da3555-aa9d-34fc-aeb2-0457e9ec0311 | -7.98661 | -38.65119 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 185d6433-5220-33d6-b1d5-15bd2447fb80 | -4.14922 | -44.42122 | 2024-11-08 12:21:00 | TERRA_M-T | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README39.md)
