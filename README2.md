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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fae61cd-ae84-3711-a66d-cd3d7f570378 | -4.0538 | -49.041901 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48f43856-a525-37ec-9907-235f87a6da69 | -2.7243 | -45.590401 | 2024-12-05 00:54:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b48c3453-c2f6-30bd-9307-24a2d0cf612a | -1.8401 | -52.311798 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0985d6-5745-3d45-99ef-42121b31a379 | 2.492 | -60.680099 | 2024-12-05 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 368de79b-e069-3df4-9f3d-eec07ff95a56 | -2.7208 | -45.575699 | 2024-12-05 00:54:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30bfb75f-4e60-32a1-85ca-999f5e95402e | -1.7442 | -54.188099 | 2024-12-05 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f60040c-32c3-34ac-a6c2-2236f37b7929 | 2.443 | -60.6264 | 2024-12-05 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 24572357-722a-3f2e-8600-34fedde9e4fb | -11.814 | -57.8074 | 2024-12-05 00:54:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c799db1-ce68-3050-9845-b1f9a47755d7 | -2.1599 | -54.608299 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 413cc3ae-2a9e-3421-8ec2-3eb76740cf80 | -1.6616 | -52.746899 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21cde77-ffb0-3346-ad9b-3974436385d0 | -1.7005 | -52.6021 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0c32236-d596-3d8e-a093-26d5d34c5b22 | -1.6631 | -52.7537 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5564fc0b-a5a0-319b-bd2b-6919d8cc58e5 | -4.0183 | -49.9506 | 2024-12-05 00:54:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215f23c4-ac3a-3237-8989-dfb34798ff30 | -1.1779 | -51.764801 | 2024-12-05 00:54:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeac5076-0c5d-3934-a0ac-3388ccb1884c | -1.6009 | -53.382099 | 2024-12-05 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820451bf-905e-3575-a105-d4a0f83f4012 | -2.8067 | -54.054699 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb2e1375-927e-340c-bc91-641e589ac0c8 | -1.6729 | -52.751598 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 312512b7-95eb-3f14-b65b-5eb9cfd1c379 | -1.6988 | -52.774502 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 694f7634-a4e0-36af-aefb-2fa25a9725fc | -6.9194 | -43.529301 | 2024-12-05 00:54:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a2f8dabf-8078-3836-8a61-c1537c4a494d | -2.9574 | -53.7211 | 2024-12-05 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8024abb9-0dae-3d5c-999a-21cf24d72302 | -2.2661 | -54.577099 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8070120-134f-386b-a058-f65494aecd95 | -2.5757 | -53.6754 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 821e8994-1091-36cd-b377-5d903b87314d | -6.9335 | -43.544399 | 2024-12-05 00:54:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04218b08-e6f8-3952-a571-97e4fb41d01d | -12.8443 | -51.9291 | 2024-12-05 00:54:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce8c487-05fe-374a-bc64-eec2d59616d4 | -1.6788 | -53.947399 | 2024-12-05 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee66be47-8715-32eb-a3c1-d0ac1a300086 | -4.0018 | -48.9081 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50a9fad9-1b6b-305c-9d3b-fc5575a8cc4f | -3.8947 | -50.084599 | 2024-12-05 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfb5b466-b1df-3c38-a71b-1fd7d28d9055 | -1.4416 | -53.812302 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a34e11-3863-3d80-873a-438126374bff | -1.6871 | -52.633801 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee2a913-0c0f-30a2-8ee3-802540532c5e | -1.6938 | -52.618 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 328b3438-6f59-3657-b395-94d7c214b3fe | -2.4273 | -53.657799 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7a7849e-00b8-3766-a3c6-de24d5e80ee6 | -2.15 | -54.6105 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f346031-6877-3e4d-aa1f-68f7c0dc90bc | -1.5317 | -52.675701 | 2024-12-05 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3e7dd2-a473-33df-b719-700eab43dff5 | -9.3574 | -57.544399 | 2024-12-05 00:54:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9111376-96f0-306b-9d8b-37f5f510d48f | -2.4257 | -53.650902 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da848fa7-79d6-36e3-a803-c2c8333cd618 | -1.4401 | -53.805401 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 063ee11b-7919-37d9-a517-10b6cd40f37f | -9.3672 | -57.542301 | 2024-12-05 00:54:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb21e271-109e-3fe0-acd0-5de732d426a4 | -1.871 | -53.300499 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8c8cfd4-9b1b-374c-9f7c-23f1d2657c08 | -2.8738 | -54.032398 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8caba0b4-371a-33c2-9f66-8d40e33e90ba | -1.9986 | -53.271999 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef55a737-f86b-3e93-b63d-875749bd4457 | -1.6253 | -53.8941 | 2024-12-05 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36e6f0f1-382b-30d6-b2a8-031e216fd40d | -4.0675 | -50.028999 | 2024-12-05 00:54:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2fcc2e1-4e39-3447-9f7e-5c171fef941a | -2.7486 | -45.692799 | 2024-12-05 00:54:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b24b3e0-9511-3301-a4b8-6175a2dd1ea1 | -2.1632 | -54.622601 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 324288e8-0edc-3b35-8cab-910cc405135d | -1.698 | -52.321999 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7ab9625-a4d9-39ae-a150-f6ecf25e54e8 | -4.0039 | -48.916901 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0310db2-e94c-3032-9e7b-6e4c692754c0 | -1.4318 | -53.814499 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c2bf901-d80f-3d89-8929-a44908f367b0 | -1.6807 | -52.785702 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 409a187f-08d8-3223-8b52-eb42a785215e | -1.6887 | -52.640598 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e94c3bf4-21fc-375f-b035-9ae830e38191 | -3.8965 | -50.0923 | 2024-12-05 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 450ae532-9def-302d-b11b-98ca33f2d22d | 2.4398 | -60.639801 | 2024-12-05 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 34f7b2dc-dba2-3440-9f87-6eda73de149b | -6.9238 | -43.546799 | 2024-12-05 00:54:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe89977d-0db7-3ed0-84a9-33665a1ec5e4 | -2.8573 | -54.0508 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61811fd9-d6fe-3839-8114-8ebf0efc1f01 | -1.7871 | -52.7547 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4126d065-2636-3dd6-b1e4-82e498d75534 | -2.4175 | -53.659901 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf5113f-68df-3ef1-b4c5-0610363cbe7c | 2.4367 | -60.653198 | 2024-12-05 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7940214f-ad1c-323e-83ca-7074e00749c0 | -1.5008 | -46.147202 | 2024-12-05 00:54:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9eaff17b-c9ee-3a66-ac8b-c6f934d69fac | -6.9267 | -42.818802 | 2024-12-05 00:54:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| add54f33-3cd5-3c5d-af02-d7b3ff76481e | -1.8386 | -52.305 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a45feff4-c4aa-317a-b05f-fd05068bfad8 | -1.6457 | -52.094299 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| debf7190-83a4-31a6-828d-97845156ad14 | -2.1516 | -54.617599 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdcc1f29-9d84-3db6-aedf-f7f2da2a416f | -2.8589 | -54.057899 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 562ea963-3b0f-3a58-9b69-b23cccd8b212 | -2.2694 | -54.591499 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebe7a85-ff41-3710-b3e1-644c8c075380 | -2.9558 | -53.714199 | 2024-12-05 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e0efe4-c43b-3896-9d38-9d3c993e70f2 | -1.8906 | -52.846001 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58411bcb-7da2-375c-af9a-b7e512fc8346 | -4.0558 | -49.050499 | 2024-12-05 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ee4ee4-a424-3050-9b0f-90fba361cf9a | -1.6243 | -52.3601 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2ead62-ebdc-30d2-a317-de6872f181b5 | -1.6714 | -52.744801 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5d0ffbf-b129-351d-a69a-a6bd343c8d1f | -6.9291 | -43.526901 | 2024-12-05 00:54:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4491f7d-9152-3780-88de-b184c9f1b667 | -3.8929 | -50.0769 | 2024-12-05 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8a9b96e-98c9-3562-8af8-17be2b0b5c24 | -1.9471 | -51.207901 | 2024-12-05 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff1c840-4dbb-3940-80c8-4a14465b7b4c | -1.491 | -46.149502 | 2024-12-05 00:54:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc4d2af-d798-363a-8658-c366b3cb8d21 | -2.0002 | -53.278801 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc859c45-0031-3182-b327-916448c765ee | -2.1615 | -54.615398 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bb433fc-7642-36ec-8579-0101e7a8df55 | -1.4302 | -53.807598 | 2024-12-05 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e258b5b-e1c0-30a5-bbe1-3cdf909e3e82 | -2.2678 | -54.584301 | 2024-12-05 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97d2087-aaa7-3250-b562-fdc4cdd7f03e | -1.6823 | -52.7925 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8a56d1-3307-3361-9b76-7ffa91deb8b4 | -1.66 | -52.740101 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29dd456d-8b35-3f86-991c-e3c2048dd732 | -1.7117 | -52.7859 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf05a6f5-01f9-3edf-a9f5-0877132d52c6 | -1.6699 | -52.5588 | 2024-12-05 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcd471a7-3ab0-37f7-9426-df788f187780 | -3.9999 | -48.9226 | 2024-12-05 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| bae28d7d-3480-331e-8346-66b53810ec4d | -2.7543 | -45.7134 | 2024-12-05 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4a680c2a-a018-3474-be80-40e8e300b76d | -6.9344 | -43.5401 | 2024-12-05 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3216d209-c12c-30e4-a860-9fb95e825edc | -4.0184 | -48.9218 | 2024-12-05 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ca259f24-7437-3722-9c55-4342cff41807 | -2.3479 | -45.1422 | 2024-12-05 01:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b5fc6c59-c069-3f90-8bff-372c63a0f9d0 | -2.4319 | -53.6584 | 2024-12-05 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d9081a6c-64a5-3842-b47e-d11feb4a14c1 | -2.7177 | -45.5803 | 2024-12-05 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f6edb7c3-a44a-3ca2-a68c-24b843e1c9cb | -6.9346 | -43.5168 | 2024-12-05 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 05b36293-5e99-39a1-bc9b-3d6859bff0e4 | -2.1724 | -54.6263 | 2024-12-05 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ab893540-f2f0-3175-be61-205753eb9c8d | -2.1541 | -54.6266 | 2024-12-05 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 68d68e81-2c06-3896-9270-1d30fbc16a06 | -6.9156 | -43.5418 | 2024-12-05 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 03dd98df-e03b-3bd5-8d0f-47962927c63a | -2.7543 | -45.7134 | 2024-12-05 01:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d9298d3c-2e88-3117-a952-3f727fb3880e | -6.9341 | -43.5634 | 2024-12-05 01:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 36ac9a27-f68d-31e2-a0cf-cea323b0f168 | -6.9346 | -43.5168 | 2024-12-05 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ddf71bea-965c-30f3-93b4-bb0bde973b68 | -3.9999 | -48.9226 | 2024-12-05 01:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c966994d-d473-3c6e-9cd7-b04d2f650bee | -2.1541 | -54.6266 | 2024-12-05 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5fd47c94-6ea0-30d0-8f84-cbfab6e5a6f5 | -2.1724 | -54.6263 | 2024-12-05 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| baa4f6fa-fcb5-3b1b-997c-404c83162cd6 | -3.9013 | -50.0938 | 2024-12-05 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 3ff1910b-2efd-3b1a-8501-7cd2424ce48d | -6.9344 | -43.5401 | 2024-12-05 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 183.5 |
| f9f48ac0-b583-39e5-b4a1-7dc70a88cd25 | -4.0184 | -48.9218 | 2024-12-05 01:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |


[Clique aqui para ver as próximas entradas](README3.md)
