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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c107a413-8c91-35d8-bab8-aaed9fe8c9f0 | -1.51208 | -52.21744 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9da9de74-0f4e-3126-bb82-be6d67df2fb9 | -1.2621 | -51.7497 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77c9f555-46c6-37ae-923a-b5e3a4578c27 | -2.62028 | -54.20432 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5c8d4c3-98c5-32c6-94b1-d4396c5389e0 | -1.06332 | -51.79583 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abbbcfea-ee07-3337-b9e0-5b51f2610b36 | -1.126 | -53.62397 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08a7d367-41b2-3d0c-8fe4-dd818c312ef2 | -2.25445 | -55.87597 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d83622d-b8f4-3216-9152-c2ee5195ba03 | -2.72224 | -48.66138 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbd4b675-b999-3557-9a2e-98c3de34a25a | -1.60159 | -53.82211 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1905f02-b3e2-313a-bd7e-924501ea8945 | -2.98129 | -51.45763 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d9e01ff-2cfe-3328-abc5-1e85d701c862 | -2.95975 | -51.00499 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 124240f6-1475-30e4-b227-b536648709ce | -3.1678 | -48.58671 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ddb008a-0363-3791-b59a-89edb6e2961f | -3.22643 | -54.17932 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25196a60-7a6c-3926-901f-f9c292242477 | -2.88905 | -53.96769 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 348ceef2-2f40-3f17-bd6e-724a907c9102 | 1.85381 | -55.8152 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89401448-4cc9-352d-892f-909b3d69e5c2 | -3.38611 | -53.50352 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc5d26e2-01ab-3321-ad7c-29b522563f6f | -2.63559 | -49.51857 | 2024-11-29 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f886d8e4-068a-37af-aeb4-c2ef51fa8d07 | -2.41432 | -53.84716 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 867daa1e-42f7-3410-9d3c-4257430159a8 | -2.82214 | -54.04541 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18d61086-5cfc-3241-9998-edc0f060c0d7 | -4.48611 | -48.11796 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52a9fcd0-1437-3a87-8fc3-26ec9d231977 | -1.2401 | -51.62433 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7176589b-1217-37de-b498-6b18ef8a0e3a | -3.3791 | -51.24566 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a4e2218-ee9e-3650-80d7-0a98e2b67de8 | -3.06231 | -53.68504 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d116146c-4a11-359e-8097-d6a7bc50dd09 | -2.83368 | -54.03661 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0855a14d-3e52-3720-9206-90428d3d76d9 | -3.68503 | -50.92485 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12ca6d0e-3975-3bc7-bdf9-8e5296434b3b | -2.52547 | -54.26765 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 089c5746-cde2-3796-a06b-69b6ab968ecb | -3.38324 | -50.11421 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38e08d50-0114-38ff-bc3a-2bdda41757f8 | -3.03741 | -51.77895 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c50caee-ef63-36ca-afca-d122b4e6d717 | -0.77367 | -52.39313 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54b7c10-99ed-3c05-a1b7-0858c946b842 | -2.43151 | -54.01897 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6eae67e-a691-3b20-88f8-0c7c38ed576a | -3.74403 | -49.85035 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 157473de-bb33-334f-b433-8e1ba5da1e28 | -1.67308 | -52.49297 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d26ef10f-167e-3219-9388-aae164fabc94 | -3.6427 | -52.22192 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90e453ab-f6a3-32f9-a428-238a1b428af2 | -2.01501 | -51.19424 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d69c4f67-f1f5-39e1-9448-471356bf046d | -1.35566 | -54.98001 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af80986f-aca9-3859-b368-3f3962e00f43 | -3.38725 | -54.28266 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82dc031f-1285-3757-b2a7-b524f59eef40 | -3.05628 | -52.76134 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 635f9032-0a02-3b6b-a9c8-694bddb7d725 | 0.94386 | -50.72912 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1646430a-1be4-321e-99f7-7d1e0fd2ab9b | -1.10702 | -52.34864 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 334cceea-86dd-3db2-abbd-857edbc1e794 | -2.84379 | -46.87109 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 803f43c7-a7f5-36ad-a714-098699d2408d | -3.33065 | -50.21907 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4bb8ac4-f65e-32c3-915a-cedc81672f70 | -4.69334 | -46.66794 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 895a4cc7-67b1-360e-96ce-d851679cced7 | -1.06763 | -53.21454 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc0fd5e3-093f-3f2b-b984-ba28b5195102 | -3.98184 | -46.73245 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 428c8139-a68e-3744-b470-73e3e55e36ca | -1.25422 | -54.54565 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bd3ff5f-5cd5-30fb-b7d3-5abe569a9856 | 0.98193 | -50.12885 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4bcb1785-e421-3fe9-978e-970d864bcd19 | -1.60053 | -55.43204 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d7a793-a090-3ad3-97a2-d30ab905486a | -1.2627 | -51.59066 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 837ffe97-3476-31af-bf5e-5469cc19f44b | -4.068 | -46.68655 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10da63e4-c44a-3178-823f-a5dadf834d6a | -3.49961 | -53.82436 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5dfa8cd-8be5-3af9-b500-7bda44423708 | -1.94897 | -53.34213 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35e2f460-086d-342c-b6cb-7d1dbee6b864 | -3.34952 | -50.51296 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7760d9d5-0016-30d9-a497-f489c7c4e089 | -2.94798 | -51.58345 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5468394-a01c-3e6d-8560-e97542de0532 | -1.72429 | -52.4907 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 019e6f1f-81af-3fd9-b938-1d228b512e6e | -1.15719 | -53.57596 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c97c83d-a09d-34de-9108-de215bf9a314 | -0.5643 | -51.70528 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1abd80f-fb90-3f3e-bdd9-ce6b736da7f6 | -1.9898 | -51.52009 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a6664cd-9c48-399f-bde0-65fbf7a19e6d | 0.58156 | -50.79168 | 2024-11-29 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbbbeb7a-762a-3451-aed9-01efbe289fea | -2.45659 | -53.68487 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b27bcc39-c856-32ae-b750-1208dc9fc112 | -1.13004 | -51.67741 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 309ab62c-658f-31d9-a726-0deb85fa90f6 | -3.2034 | -46.56951 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1d6d0f10-c807-3a7e-9ea6-30d6629a4f09 | -2.20568 | -52.10256 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7757b21f-8416-3001-b4f5-aa7fabcbfe79 | 1.45599 | -55.90202 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ac1fa06-6a6d-3abd-9e31-199da042ec1b | -1.61824 | -53.87052 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e92bef6-2ca0-381d-83f4-d0de117105e1 | -1.14726 | -53.70462 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0d858ec-2817-3ce3-9509-7ae7e8f5d6e3 | -2.96526 | -53.8915 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e656cf76-bea9-30c7-b1a4-fcc599e52c19 | -1.19446 | -54.01292 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a259c327-7271-32bd-969d-80dc6397b40a | -2.98475 | -51.45818 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59531283-2004-3f42-90ab-56ca4b430d26 | -3.70554 | -47.13213 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be367186-9c84-36ae-b4d5-0e73fafc6f52 | -4.7875 | -46.11953 | 2024-11-29 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| ddd5c10b-33e1-3fa8-b58f-74399899b462 | -3.41733 | -50.16428 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18bc4a81-9424-3927-9d14-96a888dc0e33 | -1.57595 | -53.74767 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c18f460d-b562-3b46-851b-f5fe6f6d1097 | -0.25032 | -53.76301 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe24aeb4-64d4-3114-bca4-e6fde31e2c78 | -0.14032 | -54.60022 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 272f4452-932c-330b-a09e-db9285395184 | -2.76936 | -54.0796 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee54397d-0fc2-3169-b804-c9d33218dc78 | -3.59088 | -50.37733 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df770f1b-d48a-3fe8-aabb-83080b4f86d2 | -1.71647 | -52.4752 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a3e453f-c85e-3003-b97d-b4405489899a | -4.02636 | -48.88922 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 132fa948-2479-3a7f-b263-d1d5f6964870 | -1.0343 | -53.1848 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc07f93a-eea4-326c-95d5-883b81f6709c | -2.93996 | -51.58989 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9992b91-6631-3b52-b810-5b2ae4c214f6 | -2.55276 | -55.2239 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9a5334e-cf62-3814-9d91-60832f19c482 | -3.07438 | -50.98914 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea61ed00-ccc9-3eda-88d8-e0335e2b0b38 | -1.44882 | -54.53968 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68a2fdca-47bd-3189-b69c-226e512a79df | -1.3217 | -51.66609 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7414160c-1a4e-3371-916f-41d79d3405ae | -2.60521 | -46.83605 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33dc1417-1b45-3f2e-aa68-a38cb3bb4a4b | -0.27127 | -51.62377 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 373fc819-5278-31ba-bb70-825d17ad0565 | -1.21541 | -53.554 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 91f8c990-adbd-3143-88aa-7fd1bd93f6d1 | -1.12619 | -54.16626 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e7f15a8-84b2-3615-92b6-01e2d21a15fa | -1.25526 | -52.72992 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eabc7ffc-df84-3394-ad3f-1519100d63ff | -3.34637 | -50.2392 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09b21783-fb0b-3df7-a434-f5a3691638be | -2.98055 | -53.3558 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631731d0-b772-3746-bbe7-d626c8194236 | -2.62856 | -54.30488 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 390745f6-8076-3250-a0a5-5b542fc0e3ea | -2.7831 | -51.92856 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c05b67a0-5109-3a01-bb6c-cff6dca0e356 | -2.68293 | -46.28038 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24d7d1a7-40b4-34bd-93db-8d3a90ba83a2 | -1.2736 | -51.82089 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2afd98bf-1a81-30a4-bf9a-fa57f666f911 | -1.28469 | -51.64974 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e87b5cc1-8613-3f05-84a8-036c5501f363 | -1.20416 | -51.74446 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74d37e8b-35cb-38c4-ae67-3b4afe6350a8 | -2.86266 | -53.98117 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 269b738a-eb7d-331d-ae27-ef1c23ed96ec | -1.42054 | -55.25982 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f8c41ac-51db-394f-9235-592597da9643 | -3.30886 | -53.71678 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d63ddf0-c4c6-36d4-ba7d-d633f6667407 | -0.78812 | -52.40951 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README63.md)
