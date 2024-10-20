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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cad376ba-1a6b-3ceb-bb2e-9773bef29006 | -4.1985 | -46.6318 | 2024-10-20 03:25:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 870df112-1ad0-317f-97b6-982674801f51 | -4.8224 | -42.7242 | 2024-10-20 03:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4216e5f8-b7b6-30db-a745-d7ddb91f5457 | -13.0082 | -55.9699 | 2024-10-20 03:26:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 34ef7425-2d6d-375f-bd58-549b0dfb516f | -1.165 | -53.6571 | 2024-10-20 03:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f594b417-c43d-3687-865a-d5bc3d75750d | -2.2994 | -48.5722 | 2024-10-20 03:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 72f4a7c7-cfc7-37cf-aeec-3465aa81e71e | -2.2993 | -48.5936 | 2024-10-20 03:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 92efa74c-64c0-3275-b224-a136b8767c6f | -2.7773 | -49.3067 | 2024-10-20 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 58030a66-1286-3fe5-86fd-da8f9a0fdf10 | -2.7958 | -49.3062 | 2024-10-20 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 4207c45f-f541-3091-adbc-ec5f2d980359 | -3.0478 | -51.0226 | 2024-10-20 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 95b4f62a-fa41-3739-bec5-b1dd07b376cc | -3.3813 | -50.6788 | 2024-10-20 03:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 3364be05-1ab6-307c-bc4f-ad9506b5ca02 | -3.3814 | -50.6579 | 2024-10-20 03:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 519e402c-63de-3f02-9cf9-84cd376e9025 | -3.5861 | -54.6741 | 2024-10-20 03:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6111bef5-49f8-31f0-b02a-6a025f118486 | -3.7023 | -42.4129 | 2024-10-20 03:35:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 4891ac03-fbf1-3740-ad09-ba484558f764 | -4.1985 | -46.6318 | 2024-10-20 03:35:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 611105de-4e75-3e7a-8c7c-b276f9766c6d | -4.8222 | -42.7477 | 2024-10-20 03:35:33 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 918358b2-7ebe-396f-98e2-ba6213d0bfd2 | -4.8224 | -42.7242 | 2024-10-20 03:35:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9c7ad851-e31d-374e-85f4-dfd703c6859e | -7.3638 | -72.8628 | 2024-10-20 03:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 78881d26-583b-3bf5-8745-cfa7e1c94a5e | -13.0082 | -55.9699 | 2024-10-20 03:36:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bcccb27e-40f6-32b9-ae1f-f0c8bc2205cd | -1.165 | -53.6571 | 2024-10-20 03:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4891c0c9-6b2a-3f71-91de-ef73331133a5 | -2.2993 | -48.5936 | 2024-10-20 03:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ae7c675d-25e5-30fc-b5a7-8ae9fe268918 | -2.2994 | -48.5722 | 2024-10-20 03:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ead48636-7819-3ed6-81bd-3397955ec1af | -2.7773 | -49.3067 | 2024-10-20 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 9a23aadc-47a7-31d8-ae23-5b76f6a3032a | -2.7958 | -49.3062 | 2024-10-20 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2ca2a7a7-b6b9-36ef-91d4-659f805e11b2 | -3.0477 | -51.0434 | 2024-10-20 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d9217377-b5ce-3fbf-9e3f-4be2d28d1198 | -3.0478 | -51.0226 | 2024-10-20 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 1cd03db0-4130-3a8e-8fe5-20e07d8af355 | -3.3998 | -50.6573 | 2024-10-20 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fe84e285-d9f6-3ffc-81b8-133d7aa4eb0d | -3.3997 | -50.6782 | 2024-10-20 03:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3458bdd1-dc6f-3bd5-bfee-2040e65159ce | -4.1985 | -46.6318 | 2024-10-20 03:45:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a1965787-c7b4-3ee7-9ba6-0db613be91d9 | -4.7052 | -45.9611 | 2024-10-20 03:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 03c9ff0b-711c-35ca-aa14-12d046b72bb5 | -4.911 | -45.8374 | 2024-10-20 03:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f0a157e2-ba8f-325c-a3e9-1e76bfa24ac6 | -7.3638 | -72.8628 | 2024-10-20 03:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 282ef774-98c2-3b30-a4b8-4e5b36ff528c | -13.0082 | -55.9699 | 2024-10-20 03:46:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4fdf0448-f929-32d1-a5ca-5ddd7bdb1f58 | -1.165 | -53.6571 | 2024-10-20 03:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 74a4a86d-ea1a-30d5-b242-bdea9a48628f | -2.2994 | -48.5722 | 2024-10-20 03:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e6cbbb36-0a4c-31df-9a01-a10246836c48 | -2.2993 | -48.5936 | 2024-10-20 03:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3cbb8145-0956-3cf3-97c4-760dd1846ccd | -2.7773 | -49.3067 | 2024-10-20 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e1337357-09d0-3fae-a179-65b693ac5042 | -2.7958 | -49.3062 | 2024-10-20 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 3a19fedc-02ee-3de3-8e8e-ddc224a5ecd6 | -3.0293 | -51.0231 | 2024-10-20 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5aa114ce-b070-35f1-b2cc-a2d279aa85e1 | -3.0478 | -51.0226 | 2024-10-20 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| eae82bf5-720b-3f70-9b02-08c52cfa9c42 | -3.3813 | -50.6788 | 2024-10-20 03:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3f0cbaec-6b3f-3245-b688-a8853fbce017 | -3.3814 | -50.6579 | 2024-10-20 03:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 34d2cc85-00cd-30a9-b05b-73ff89a187f5 | -4.8758 | -48.2145 | 2024-10-20 03:55:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ad499412-2c38-362d-9725-942117b12d54 | -4.911 | -45.8374 | 2024-10-20 03:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| cca9fba5-ca05-3cf5-bea4-79fab6f83927 | -10.1216 | -36.3607 | 2024-10-20 03:56:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 3538c512-0d1b-3df8-a455-59ed4b2397b3 | -10.1221 | -36.3337 | 2024-10-20 03:56:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 188.6 |
| 66c300a5-f807-3fde-998a-a046f8720ce6 | -13.0082 | -55.9699 | 2024-10-20 03:56:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 24c09741-9ce6-3825-8252-280012645965 | -2.2993 | -48.5936 | 2024-10-20 04:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8b36e6c3-fbfd-348f-8ea6-8513e66fc9fa | -2.7773 | -49.3067 | 2024-10-20 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d0b4d14b-d744-3ef0-b8ea-2bab4970328f | -2.7958 | -49.3062 | 2024-10-20 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 8767d5f7-0557-392e-a36c-0e1bb0c0a500 | -3.0293 | -51.0231 | 2024-10-20 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| dfcc5626-8108-387c-8720-d937589b43e9 | -3.0478 | -51.0226 | 2024-10-20 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 412ac2ce-3e2d-369f-a59e-de8cf5ba40ae | -3.3813 | -50.6788 | 2024-10-20 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f496268b-e5a3-3145-bf08-11d77bd436ba | -3.3814 | -50.6579 | 2024-10-20 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 914a35f0-8fdb-3334-9b98-065e22f32801 | -3.3998 | -50.6573 | 2024-10-20 04:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 00f17fa9-cf89-3605-9eab-12e2572cde86 | -4.3898 | -45.7995 | 2024-10-20 04:05:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bdf06638-5eec-3539-9448-812ed445f4ed | -4.8758 | -48.2145 | 2024-10-20 04:05:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5bd59cd4-4c32-3949-b384-082531f7a776 | -4.911 | -45.8374 | 2024-10-20 04:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e658e26d-98ed-3432-be45-4fcfe22996a7 | -1.96708 | -45.59543 | 2024-10-20 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c43861c-584e-35f7-9818-7b16dc63c02e | -1.96304 | -45.59477 | 2024-10-20 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9056ea02-8404-3e3f-9f3c-7313860a19e4 | -1.95957 | -45.59059 | 2024-10-20 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b2073f9-3d24-38a7-a8ad-68fd4d0058de | -1.95553 | -45.58996 | 2024-10-20 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c0c048d-ab69-3dcb-bcf0-32a1cdabdb2a | -1.95149 | -45.58933 | 2024-10-20 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384c8273-4861-3df7-8fc5-6b8a9ac483de | -1.50745 | -47.21385 | 2024-10-20 04:06:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d8f4d8-772e-3185-bcb0-b2028fe0bf6d | -1.50671 | -47.21846 | 2024-10-20 04:06:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57796d95-df06-3cc0-9f37-817255cb85a0 | -1.5029 | -47.21317 | 2024-10-20 04:06:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a4571d9-3708-3461-9c74-483e9f4c2cae | -1.12757 | -47.26532 | 2024-10-20 04:06:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a21b9b4f-d4a2-3269-83d8-9ce014b6f13f | -1.12732 | -47.26635 | 2024-10-20 04:06:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 970c5c49-52f0-38a5-9058-ed5c3a4319ce | -1.12298 | -47.26461 | 2024-10-20 04:06:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee465257-7857-3db4-978a-979116ad6ba4 | -1.12273 | -47.26563 | 2024-10-20 04:06:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 424b8ab0-6bff-38af-bd59-519d9b21db73 | -1.06131 | -48.25856 | 2024-10-20 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21a96ce3-f5e5-398b-b2a8-d690e13c5fa4 | -1.05799 | -48.25977 | 2024-10-20 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40a770ce-b4b5-3378-af52-adb0119ce040 | -1.0564 | -48.25776 | 2024-10-20 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f662060c-94e4-351e-aa85-02bda07585d2 | -0.76489 | -48.64154 | 2024-10-20 04:06:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3d7ebef-a6d6-388b-b1c6-97c57d5ff0a1 | -0.76442 | -48.64452 | 2024-10-20 04:06:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3b55c47-7db1-35fb-832d-2ef6bdce3baf | -1.10001 | -49.18008 | 2024-10-20 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc1770e7-53e4-3ade-9291-181e20427822 | -1.0995 | -49.18328 | 2024-10-20 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9b10627-5523-38a2-926b-c2a99620883a | -1.01803 | -48.85286 | 2024-10-20 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e6c1ef7-185c-3ab4-a55e-3c202771e5aa | -1.01754 | -48.8559 | 2024-10-20 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765940f4-bd15-35f4-b47b-cebef7bb2f62 | -1.01436 | -48.84295 | 2024-10-20 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d79e7c7-99e9-33ee-a315-eeea5a01dc22 | -1.01387 | -48.846 | 2024-10-20 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f4252ce-813d-355f-9300-d51b5903a06a | -1.01338 | -48.84904 | 2024-10-20 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11c6f417-29dd-30f2-a5c2-cfbe0ed593de | 0.65694 | -51.87085 | 2024-10-20 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f179ac76-b2cb-354b-b3a6-97132f78f821 | 0.65613 | -51.86572 | 2024-10-20 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 500a6745-9be8-3107-8dc4-332f8f21b324 | 0.65052 | -51.87174 | 2024-10-20 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82d8c2a5-f103-3b01-b66b-99c0064f479a | 0.64972 | -51.86665 | 2024-10-20 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfb864fa-932b-3556-a6a0-9739dc864b55 | -0.23367 | -51.52826 | 2024-10-20 04:06:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eae53aa8-cca6-3b8d-adbf-60ac21539020 | -6.3749 | -40.47706 | 2024-10-20 04:08:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2ba8a5c3-7f8b-3d9e-81ca-52646e41dd6b | -3.60332 | -50.57967 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 957eef85-0746-37d5-8553-355160d9d2ca | -5.86815 | -35.32899 | 2024-10-20 04:08:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4476754e-1125-31a9-908a-0345c9cbdf17 | -5.50009 | -35.41904 | 2024-10-20 04:08:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 868eb186-5b28-3195-8bf7-a0cac8a6b59e | -5.49951 | -35.42304 | 2024-10-20 04:08:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16eb0ff0-5f39-3317-aed3-eb898f26d2d3 | -7.11395 | -35.27299 | 2024-10-20 04:08:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9cbb4e9f-ff30-347d-b4b4-66c78e88bc7e | -7.11345 | -35.27565 | 2024-10-20 04:08:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cdd0e51a-1857-3f6f-b750-f5c8a60d3281 | -7.63442 | -34.96107 | 2024-10-20 04:08:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8915d745-acb7-3c76-a414-1c96545ff01e | -8.07264 | -34.97617 | 2024-10-20 04:08:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed49e31c-4492-39cd-835a-e610e50ae040 | -9.92141 | -36.19056 | 2024-10-20 04:08:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 8f4bf24b-20e1-3f8c-aadc-e4896673599b | -9.92085 | -36.19472 | 2024-10-20 04:08:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 77826188-f643-381d-89c0-237e748aa0a6 | -9.9171 | -36.18994 | 2024-10-20 04:08:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 17479501-88e7-312f-88e7-297101098ee2 | -10.12994 | -36.33935 | 2024-10-20 04:08:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8245947-47a1-3d3e-93d4-035d34d798d1 | -10.12566 | -36.3387 | 2024-10-20 04:08:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
