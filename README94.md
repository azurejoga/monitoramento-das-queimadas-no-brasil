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
| 4c5caa85-d1a3-3fe8-8b9a-a8fb10cdf549 | -2.80247 | -54.0267 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8decb6f2-ca49-37a2-8371-51d9283dacc3 | -2.83285 | -54.10614 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0341331d-21ed-3a91-9a5a-fef43403b2ae | -3.42184 | -54.02459 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef71164d-9711-38ef-be7d-4ddcd3061b70 | -2.87789 | -53.32645 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 817a6425-02f0-3031-aa73-1428de09517c | -2.76003 | -54.02402 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff5f04f7-a061-3f43-9a40-611e870bf208 | -1.65506 | -53.42182 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd70419e-9cca-3dc9-a6a4-813311dc21bc | -3.43895 | -54.12296 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86553511-5f11-39c9-95c3-1081dd90fbae | -3.06577 | -53.26759 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ff8a974-1e72-3bad-ab7e-c7ff8429b143 | -3.21049 | -54.17294 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 298c40b3-11fa-3fce-b9d6-fdb43071ee77 | -3.50586 | -53.83143 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d147d109-e0c8-3498-9366-f50a0f074dd0 | -3.33481 | -53.36907 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 444dc0f6-0086-3daa-b0d6-955dda46940b | -2.57513 | -53.97728 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49e9afb9-e11f-32b8-9feb-8a047c122001 | -2.98159 | -53.87335 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31eecac0-8540-3fb4-ad93-750be0821d45 | -3.0907 | -53.23147 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ced81f56-ee41-32ea-9bf5-374de03ed6f6 | -3.12674 | -54.5313 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 556221d2-b95e-32a8-87a3-ca20041c7051 | -2.48438 | -54.02246 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 938e350e-7bf1-305f-ac86-48c02b84e7fe | -2.94197 | -51.50568 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ea705c0-42ab-304b-8d45-38a3a1eefcbd | -1.90672 | -51.00975 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c17cb008-469d-3dba-b2e2-d18042384641 | -6.71393 | -47.27454 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 652b7f0f-dcf8-3ab8-8e83-c0a3be71e510 | -2.03682 | -54.66747 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea68b19f-ad89-393d-850d-1fca21963558 | -1.29816 | -55.74012 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f57cae1-b9ab-3df6-98d2-32b0164508e5 | -3.42125 | -54.02846 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0323f32f-abb4-3e6d-883a-9f1a89f1ac48 | -4.03718 | -46.92811 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| acf98498-d3f7-3326-b8df-83a610395350 | -3.26366 | -53.64074 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aaf274dc-3029-357c-9098-8cd856f898bb | -2.88387 | -53.33565 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c8ef80-3247-3471-9b7f-d3fb7761e0e9 | -1.70085 | -52.46641 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a747e170-9683-381b-ae02-85d629fe1931 | -3.25234 | -53.64315 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66b4d398-8350-39e6-b5d2-f8ff8d59e203 | -3.24645 | -53.63389 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feda2f20-694b-3b92-a243-b2d19348aa91 | -3.60214 | -50.3734 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c06e76e2-338c-31b1-969b-2a2f19e4732b | -3.25672 | -54.23029 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69b24fff-8807-3453-b5f7-028010104323 | -3.24816 | -53.64665 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad18cb51-feec-3404-923b-edf2b6d44954 | -2.99568 | -51.06506 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2848230d-1938-3b01-8fd2-2b552ee7ea5c | -3.43118 | -53.89294 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c732bbe3-96c2-3c1d-a1d2-96e2192425fb | -1.90396 | -52.87304 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc3484f6-a846-3c63-92b2-5244934748a8 | -4.49668 | -49.6409 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84aa6f1d-6270-3bba-906a-9c9e5ca895c7 | -2.97807 | -53.9003 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45488802-eb9a-3ace-8af5-e7305c770b48 | -3.97687 | -46.75265 | 2024-12-01 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22124656-a59a-3dce-b92a-6498ec9527a3 | -2.84464 | -54.03963 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b270dbb9-f1a7-3aa0-81be-eb9f785579ad | -1.40436 | -54.09478 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96e20cd6-5389-36ca-8b44-be3ef65d1410 | -2.7665 | -54.18949 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4725d7d-09b0-3621-85a8-4043aa842cc3 | -2.80116 | -54.05806 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ecda534-556c-337f-af19-49cff98b6247 | -1.14169 | -53.80647 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 540d0a14-d756-38d4-8e74-2e2092ef4df8 | -2.80858 | -53.0455 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 03798dd0-a879-3309-b992-f8d1d3b10417 | -3.99605 | -44.76059 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b936fa80-1532-3a3c-9650-57b7680dd158 | -2.83632 | -54.10667 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fdfab75-e972-3b5c-a30e-008fba6741b7 | -2.97866 | -53.89643 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfd9b672-2a7f-3e6d-8d79-3809743bfabb | -1.38827 | -53.55411 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 72287d83-9eeb-303a-a833-1d4bfb664b76 | -2.83783 | -54.05182 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09e5ccb7-cbb5-3454-913b-a799a88ca84c | -3.32395 | -50.19177 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95c2606e-7827-3987-93db-8a34606098a7 | -1.72488 | -52.48376 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbe5854e-306b-3012-88cf-e9e1a401d0fc | -3.09606 | -54.02534 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a97eb76-c8f6-3b4b-8408-c8e924e505cc | -2.42059 | -54.02042 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d57244b1-457b-349f-9d49-e1ff6af276c1 | -2.59145 | -54.21427 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e76e93f8-956c-3b6b-aff6-22028bc306ef | -1.42269 | -54.31401 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdb052b7-1b85-3f5d-98c3-455291720d91 | -3.3281 | -50.22339 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47d13aef-11d9-31bb-982b-2d6386ff9efc | -2.26403 | -50.72273 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 589064e6-0781-3777-b38b-05e0d4eaf678 | -2.5451 | -55.22086 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69e331e1-ad1d-315a-b10b-a68a36e055e6 | -2.96325 | -53.89849 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5e1cba-d7b3-3014-a249-9c0c0bdf911c | -3.7414 | -51.83569 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7da48117-3e10-3d82-a68f-99db838f36dd | -3.09017 | -54.04031 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d331a5de-dddf-3441-ad8b-00b44bfa4026 | -3.99137 | -46.65223 | 2024-12-01 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776e0dbd-33eb-311f-b0c2-769023e8b0fe | -3.58897 | -50.3715 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62841fa0-2ef5-338b-889d-8ddb6da6f685 | -1.78502 | -52.74645 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1e70ad8d-6a4d-3323-9d93-caa6d5f774a4 | -2.88488 | -54.01024 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89ee58d4-fdba-3aee-ad7c-306b90f575f1 | -2.86511 | -53.99925 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fd44582-01e7-39cb-b810-9982a476d14b | -3.03472 | -54.04463 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e28ca245-77db-3404-916c-aeabeaba4c50 | -3.30895 | -53.8639 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 33f84213-4d32-325d-9e7c-c38022a2e221 | -3.5017 | -53.83487 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e30b1582-a00b-3f23-8580-4d29a352cfc5 | -3.28231 | -50.16804 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bafe9c5-91d2-3d62-817c-9c40e086f831 | -3.2099 | -54.17677 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84380336-9b9b-39cb-9212-c00043e943ec | -3.3729 | -50.82422 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e4f7e69-6340-3366-8864-8ee5cae8d267 | -3.74546 | -52.26014 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2714a39-9ea8-3989-9083-8204df5f5514 | -1.62281 | -53.88445 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80402980-af72-3607-8355-d9d730dd8b39 | -3.14727 | -45.37729 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 01777c5a-ae74-322d-a214-5dbb78cf4710 | -2.36488 | -53.86339 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71940648-620d-342e-a669-524574146bba | -2.60427 | -54.08757 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cdbfddf-a1c7-3aba-ab92-311399be1e9c | -2.53143 | -54.02931 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 101cc69f-ebc4-3ebd-906c-c1782741ecb2 | -2.45782 | -53.70566 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fc3f157-15d8-315c-94f6-0249be65b9f6 | -2.86689 | -53.98762 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54980628-e4d4-36a5-ae08-5bbba58ba64d | -2.87091 | -54.00808 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52f57a60-5673-34ae-a768-fee264da5025 | -2.60761 | -54.28551 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46d5cb73-c6de-37da-9de6-94465ba1b5ba | -1.91979 | -53.00954 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 737ec389-00d0-3f1c-8ab1-441ccd8a2aac | -1.75897 | -53.63926 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 221fffd2-9aef-395a-b9d9-3c4fef5c43d7 | -3.67512 | -54.04625 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51a9cf52-0eec-392d-babf-a7cf0781f960 | -3.26848 | -53.63315 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a1078328-bd6b-3c66-8b2f-b604d2ea0a2c | -3.11096 | -53.81054 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab101020-a6c4-30a9-98a1-0d320595ac36 | -2.4473 | -54.00884 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bd75c38-ebf6-3128-b52e-ef73e32611f2 | -2.84313 | -54.0408 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe45573c-2943-3e80-bcb2-32db31569f88 | -2.89243 | -55.23065 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ec51b7-ee94-3fe5-a8c3-6c230c362998 | -3.03243 | -54.03635 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38ad0fcc-6f89-3a9b-9efa-a3a23512140b | -3.21322 | -54.08617 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 856aa020-f6cd-3d4f-aef6-11925ef9d611 | -4.25221 | -50.83799 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a278125-ddf6-34e3-a27e-39caaf7cd77a | -2.81093 | -53.05462 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| eb0cdbec-e474-3997-893f-7edfdf637525 | -1.44883 | -55.19209 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94378325-82fb-3b1a-9f13-3f2f233223a3 | -4.41172 | -50.70134 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4591965-bd0f-319b-8de2-abab145dbd41 | -2.45202 | -53.62745 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f1748c96-9e0f-34e7-8383-0b80eccdfb7e | -1.43945 | -55.22998 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95f7c3fd-6a79-3f4a-acca-f18e5873e13d | -2.18967 | -53.77796 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67b1af28-9af3-322a-a36b-d40b69d1bbc0 | -3.52461 | -52.15811 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1865f907-20ab-35ac-a6b1-e5fa47f3b374 | -3.09856 | -53.72851 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README95.md)
