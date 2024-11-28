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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a587330c-2727-3dba-8266-b82ae886d9f0 | -3.24823 | -50.77374 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5cb6aab-479a-39cf-9aa5-fed0f1a7fd88 | -3.10267 | -53.25581 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d83c35f4-aa15-3632-8f13-86266f024a72 | -2.63598 | -49.90826 | 2024-11-28 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f5237ea-1362-3b84-a710-4ac6340cb93b | -3.48698 | -50.08714 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57335ef4-0b6b-3588-859d-32f442d12266 | -3.43639 | -50.02852 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a80620b-9fcb-358e-a4b5-f095fae415ca | -3.16235 | -50.58162 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 077ccb7d-cfde-3000-b0ae-026a0b71e1a3 | -3.38395 | -50.1043 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6f818074-7e9d-3eb0-9e3d-68608ade5d18 | -3.17333 | -48.43742 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 683b203a-7098-32fa-a817-2fde8af0d7f1 | -3.25388 | -48.89322 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b64a5dd-bc42-3ca1-8fd6-cb027f1e23c3 | -3.39522 | -54.28605 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a7f0a5-03f2-3a97-ac4b-80c4a85c888b | -3.34076 | -50.51259 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 890beff1-0a50-385c-8aa8-8404f07c9f2c | -3.69698 | -50.22932 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e19353e-5412-319e-bfd3-36b0211fb434 | -3.59575 | -50.35645 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07e6af16-b9bf-3ba5-a759-3a89bc4a3064 | -4.09951 | -46.11465 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e9085b1-7050-3e35-990c-513632caccd7 | -2.05932 | -51.18854 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2842f199-445b-3f7b-8c36-7756643fbfdd | -3.24222 | -53.63398 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cacc5d64-429c-3498-930c-2a2bed05b70c | -1.49782 | -54.46193 | 2024-11-28 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 864b52a1-6fb0-3272-b86e-1838461dbacd | -4.21765 | -50.88794 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2fd4a81-9de3-3bce-815e-05c9230678ab | -15.10153 | -54.63279 | 2024-11-28 04:25:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6350911-3021-32a6-adec-0fa7e476a91c | -3.28551 | -54.74236 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42ba9954-133e-31aa-9426-f413e8341b1c | -2.80062 | -51.59184 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 584eada5-3811-3d9e-a85c-6a61af74abe3 | -2.83606 | -54.12192 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b94944e-0bf2-3db3-b2cc-ee947258d82b | -3.59301 | -47.3437 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab8ec149-224c-31a4-9b37-5202a406d677 | -3.62926 | -42.40398 | 2024-11-28 04:25:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b41f1ab6-8722-3184-b7bf-7ea4d86e9265 | -3.30711 | -46.67613 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02cc8c7d-1db6-3532-9b0f-13aa2768f7fe | -3.4991 | -50.45996 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ead7980a-8b50-3784-86e9-89356fa2c3ea | -3.94174 | -48.1415 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90697d4b-52c1-3073-950a-785a557c5839 | -10.41717 | -49.24436 | 2024-11-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9239be4d-5690-306f-8940-a1a93664a5ba | -3.24957 | -46.41917 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f39d0df7-36dd-32ee-ac47-879599f4b8f9 | -3.04561 | -48.51018 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c94940f0-9610-352c-9cf0-21625d828a57 | -3.59065 | -50.6917 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00733b5c-4f29-3c54-95c5-9953979cc127 | -3.49576 | -53.80883 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 407f1303-f641-3343-8d2e-7413fefa2313 | -3.04753 | -54.04017 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d897c67-9c84-3be6-88ce-6ce17fb5ad6f | -2.83236 | -46.83918 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab5ea85-233e-334d-9601-98a80f753af4 | -3.24225 | -53.63506 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b591f440-f9c9-320f-9a0b-5675527b0318 | -3.56113 | -46.33909 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15051f5b-4545-34c5-a6ee-552f63f93836 | -2.59032 | -53.97523 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 176f01e7-ee87-3549-94ec-555442b3b93c | -3.98192 | -46.98931 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47c540aa-b788-3cc1-b854-c94cfc98e145 | -4.53748 | -45.87998 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8f4f4a5-a3e2-3e09-9523-4b469692b7ea | -2.00262 | -51.16861 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af3a88de-b367-3194-9f4d-68d49d64fd97 | -4.17859 | -46.83836 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce08791b-c108-3ee6-abb5-774a4bdde808 | -3.77225 | -46.68005 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae16d831-8eeb-3aa7-b6d4-706e05c3edf5 | -2.87 | -46.8414 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 602cf7b8-b5e0-3d37-84ef-dfd86ebae252 | -4.30743 | -48.18548 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74b35df2-1690-3da9-9359-7f435adc58cc | -3.38743 | -50.10679 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed882fc1-c833-3b45-af79-e98ddf0407a5 | -2.80555 | -54.13798 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f54f397-cfe5-34ea-844e-14ba6493a32e | -2.84921 | -46.8418 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f1f50d1-bc66-3447-a0d5-3ad753743687 | -3.15772 | -50.58452 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ec7e65d-00d6-3c57-9d0e-552ddf555ffc | -2.87419 | -50.73678 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d316a9bc-0a40-3e70-8a3c-068eb1a2769a | -3.38896 | -50.3189 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9614ff5e-5344-3ada-9547-1e390ccb1d18 | -4.04344 | -48.09705 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91ed207c-3bdf-3b28-a79a-8c5eb9c58eaa | -2.0123 | -51.19097 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bcb008e7-8555-3e76-a183-e2d9d4e64a8e | -3.09526 | -53.81152 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57b50d06-5e68-3cbf-b4c3-b6e486b831ef | -2.86943 | -46.84497 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f39dca-56cd-309b-8706-03bc1e4f9d6e | -1.97761 | -52.09625 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb5b7daa-9efb-3607-936d-f62bc82108d1 | -3.26566 | -50.56224 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd557325-5918-34cb-9caf-a3b3a90ab995 | -3.12046 | -50.29587 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3794a6bd-4286-3123-9196-b8984efcce2f | -3.6936 | -50.22726 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 635a8c25-9f63-31af-b02a-e4a26854c9eb | -3.71051 | -47.13416 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43bb965f-96af-3956-8b24-0fcaa33b45c2 | -3.61032 | -49.89509 | 2024-11-28 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1286065-4c29-337b-a94d-08f5466c4be8 | -3.25297 | -50.61494 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47c96e8e-e697-3f2c-8591-8b3ec61f54ba | -3.09779 | -53.73232 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8efbf532-9956-3946-b10a-3446a7ff1e85 | -2.18195 | -53.77423 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 114dbe18-0d02-327c-9eb9-aedc0c54a5a2 | -2.86938 | -46.86704 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ea1b553-7de9-363b-8f06-7ec987d8338d | -10.00152 | -48.50099 | 2024-11-28 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aefc3433-6417-3f80-83ea-cc0dda610e58 | -2.85481 | -46.85003 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc7a669-e46e-3194-a16e-2d151f0491d9 | -2.85932 | -46.84339 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8bf2083-1695-35d2-a8b4-bd02ecfc9773 | -3.96468 | -50.19068 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| e1054ac2-1d92-3979-b262-c5e0815eb9ce | -3.49476 | -53.81488 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c161cf-2fc5-32db-955b-69cd4359d361 | -3.04986 | -48.50664 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee39ff99-6fe2-3ec5-b31a-1ddcb14a9589 | -3.37454 | -50.11291 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11db66a8-9e02-3838-8989-1cd5b428e131 | -3.29905 | -50.25545 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffee7cdc-0975-381c-9b6a-48967ef87836 | -2.84247 | -46.84076 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e367af8-5a36-3490-acf7-730e4676d02b | -3.62717 | -42.40262 | 2024-11-28 04:25:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 247b81ea-845f-376f-b46b-44c88bcb8be7 | -2.90557 | -54.18532 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0acd697a-94f8-3647-8e28-ebdd2504d343 | -3.34421 | -50.51668 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62162b20-b9ae-3a90-b665-9ab5293a8649 | -3.23005 | -50.78207 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 555cfbe4-fac7-3138-9aa1-fcf3613d4d2e | -3.12607 | -51.04579 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab1f4815-5f26-3a0f-a89b-17586927cb82 | -2.87503 | -46.85321 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f8a3e7e-c9d7-3045-bf76-a57aa7be0ec7 | -4.05418 | -46.82971 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c229c1b5-79d6-3f11-81db-fb468203870d | -2.82744 | -46.83865 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5dd1c9b-4f35-3c8b-8bb9-4455d22512aa | -2.86093 | -46.87674 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5154e63e-bd21-30fc-99e5-5917364f3df6 | -3.23732 | -54.22901 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a914fdb3-2f99-3cab-a205-182c1a9fb14b | -3.11007 | -53.2583 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86358775-5181-3ba9-a522-77a8d9e52daf | -3.46195 | -50.53632 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ba0b797-1f9d-314c-aaf8-ca6f8f615f5c | -4.76064 | -46.38239 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6d88f49-6f3d-3399-972a-4b870b908a44 | -4.19567 | -48.56455 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a852dbd-2b78-3652-bae9-9333dc02f1fd | -3.26862 | -50.62111 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d47a895-295a-33bf-9193-bfad0d2baef7 | -4.29961 | -48.21191 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2900ce05-9392-3e2f-8314-19b593b32b57 | -2.85709 | -46.8357 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 062fb177-ecd9-348c-acc1-38fb70ea3cb6 | -3.83617 | -46.60022 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3932ad3d-4bda-35a8-b975-bcb05b10fd19 | -3.36132 | -50.99376 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c03dd7f9-35b0-3aad-82bf-5a2c8749e94d | -4.66235 | -45.03964 | 2024-11-28 04:25:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99e2c16e-0726-3ebc-9e62-3fe7b4d93df9 | -2.87166 | -46.85268 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4dd8b3e-616e-3d53-9153-b3dfc6262286 | -2.90039 | -51.37043 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7a4e06f-7b94-3e87-a1d2-56bae6aee71f | -4.14937 | -46.61764 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00675f44-6c3e-3923-b454-e89b53a38872 | -4.11482 | -48.48222 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a39dd215-a59a-36c2-80e8-4936729837fc | -1.78785 | -52.73686 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f727271b-b42e-3974-bdd0-0f24a1751ba7 | -2.83853 | -46.84382 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f66fa5a8-79a1-323c-a8d0-5574bc3a9621 | -3.56315 | -41.9644 | 2024-11-28 04:25:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README69.md)
