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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ccbfdd2-6a40-3132-ab32-9923bcc6f882 | -3.24493 | -50.42559 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aa8f0dfd-4db3-3740-a9a7-8c061b9ae7b9 | -3.55468 | -50.40129 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aaf309d0-d281-3009-b8e7-a26e136cfd44 | -3.32732 | -50.22115 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 906d4180-167e-384e-9df9-ef0176d615b0 | -2.46496 | -45.91211 | 2024-12-04 00:54:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d27b60e1-bb73-3eb1-82a5-a71432af8a4e | -4.10834 | -43.91717 | 2024-12-04 00:54:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 4e783219-4fdb-323e-8cb2-95139ae1a204 | -3.28089 | -53.25259 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 242f01f9-4463-3c6e-9d69-ad914fead23f | -3.84636 | -46.56422 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1d7263a-ae91-35df-be77-dce7b2d2cf84 | -3.26538 | -45.37391 | 2024-12-04 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e915856-3e12-3abd-a014-6177daec48bb | -2.72684 | -45.5401 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ba8ab265-20a6-3b75-acf0-95a671fbd4a9 | -2.90284 | -51.82273 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| fa34929d-129b-3f25-8f14-38424c62b863 | -2.17256 | -46.65627 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e542e1d7-7677-3b26-bb08-06a822421390 | -3.71579 | -51.36064 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| efb7dbe1-7e01-38fb-a5a2-164f9ee432e6 | -1.79178 | -52.29478 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 553ab121-3fe3-3083-bce2-4fd9063b9b5d | -3.49943 | -49.93618 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f17b50d4-d8f7-31a2-a8ff-1833d54e3802 | -3.36982 | -51.06319 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 37f57e31-7dc0-3591-9d0b-33ef73bdf162 | -2.06767 | -45.47831 | 2024-12-04 00:54:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| aeb013d8-aa6c-348b-952e-e157ceaa3f86 | -2.10032 | -46.58448 | 2024-12-04 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 6566f067-7a4e-3af9-8927-4b1d22c3caf9 | -3.73047 | -51.07825 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 721c4b81-0947-38c1-9f7c-d90b6af651dc | -2.23993 | -53.70068 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dc0f5475-91db-3260-bb38-11d3e7bc8c47 | -3.41657 | -50.2678 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36b24132-849e-36c9-bbf7-d40f616c1294 | -3.70761 | -50.44331 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f3f0f6d-1ac4-3b82-a13f-9e422d270d28 | -2.05362 | -51.20378 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 13a0974f-43f9-37d7-a02e-b493e91c368b | -4.30985 | -48.08205 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21e21f07-b0d1-32c7-a3ff-6017a29de5cc | -4.11743 | -46.90679 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df7d7eb9-4f65-3c8b-b87f-45940bf54526 | -3.85807 | -52.16131 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 80b62771-700d-3529-a851-dc2ed4378346 | -2.20529 | -45.6778 | 2024-12-04 00:54:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 61010d16-fa17-3639-b79e-9b22b0a91e7d | -2.72778 | -51.81651 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5db50a13-1858-3462-a96a-d25185266d2b | -3.06063 | -53.26121 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 02ba7693-5138-3566-80ac-e4649402527e | -3.09727 | -46.61401 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e935c165-1b69-3bb6-bf31-71de1d976fff | -3.81328 | -51.01035 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b398b378-aee9-3646-b89d-a137ff810047 | -3.81921 | -49.84854 | 2024-12-04 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20885fc3-6745-31f8-8aad-f7637f2af3e9 | -3.66973 | -47.13205 | 2024-12-04 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6d74c723-124f-30d6-ba77-e1b43ac1b784 | -3.12162 | -45.9997 | 2024-12-04 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fc850c44-c386-3364-a9a9-ffe11c985dab | -3.53405 | -50.38544 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b230332-9204-3586-9dfc-a8e91e91359f | -3.18389 | -49.25092 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c0cf81f1-365e-3705-8c53-7e0fe2da8bcd | -4.74564 | -45.70013 | 2024-12-04 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| c753631f-5da0-3279-9a3d-a375979cf7f9 | -2.28754 | -47.91527 | 2024-12-04 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8311bd99-b631-32af-8503-fb80de297c1d | -4.08181 | -46.20803 | 2024-12-04 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bfe74e23-9b42-37f7-a61b-68fbefef177c | -2.02458 | -46.3356 | 2024-12-04 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 025843b7-4cf8-3bb6-b78f-6c91f7815134 | -4.61524 | -48.02951 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| acaef06d-cdf9-3175-928b-69af4956ea1a | -3.02846 | -54.18858 | 2024-12-04 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4b4a9fdc-19a4-3c18-8730-1177690079f3 | -2.68673 | -46.61699 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35941406-1b02-3435-8d0b-cb445d26b198 | -4.50409 | -48.02353 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e9f498a-f6e8-3e61-b4c6-0079404a21d5 | -4.03195 | -48.33825 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a55b36f8-887c-3f37-a75e-fbf310f0d9ec | -4.04619 | -46.87648 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4d400fc5-21fd-39a3-acb7-18dd394c7706 | -2.88075 | -51.80436 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 36d521d7-d62f-37e9-9b40-bd7d32ab15e6 | -1.62789 | -53.52992 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e7d94f16-fa5f-3877-8fc5-338cf985acfb | -2.84703 | -46.79609 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| dc249b44-f17f-3237-b652-376e141bc3c1 | -3.73182 | -51.08809 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4a527da7-5c12-315d-a557-4f54e864ed48 | -3.1752 | -54.33672 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f0381e53-f8b7-3f9d-a3b7-5da0f88fd56e | -2.97606 | -44.98308 | 2024-12-04 00:54:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8567b7c0-3490-3984-9858-fc664d30b280 | -2.20349 | -45.66541 | 2024-12-04 00:54:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4782676e-fcfd-3679-bf38-8ff47741245c | -3.09698 | -53.25038 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 088f5875-6977-32e8-8d9e-ec050526a31b | -1.50985 | -46.75589 | 2024-12-04 00:54:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 27541260-5c1b-36fd-b7ed-a8a1e813bda1 | -2.9014 | -51.81226 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| f5c2f8e1-23b4-3891-875f-8ea80c8cd426 | -3.99896 | -48.29735 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a8d99cb-42af-33d6-a967-089b8663371e | -4.02516 | -49.27544 | 2024-12-04 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 66ab6dca-678e-3df4-877b-98acb3b3a974 | -5.01263 | -47.64491 | 2024-12-04 00:54:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9da3e7ea-5230-366b-a678-abd21f829da9 | -1.83444 | -46.22388 | 2024-12-04 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9a2859b3-f34d-3614-bd7c-1b2cad04ab79 | -6.27392 | -44.73936 | 2024-12-04 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4aa71781-1a85-3ead-820f-9a0e50fdfe30 | -3.49147 | -51.5603 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4bb5ece7-2844-3825-9ea6-3499f689d7ac | -3.74379 | -52.44714 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c1751ff-250e-330b-8db7-39582c4159b6 | -3.05635 | -51.0655 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a7fbd37-306a-3ed8-ae11-2c4a7dbd8cdb | -4.10569 | -46.95909 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7af1ed0a-e106-3b14-999a-d24172745ebe | -5.58914 | -45.16655 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7046a064-7e29-3531-bb99-700027f63287 | -1.83386 | -52.311 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14434dbf-64d9-359c-9b64-2336bb8bdeb9 | -3.85003 | -46.52119 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6d40038a-59a4-3bf5-9887-a03311a94172 | -2.19912 | -45.6846 | 2024-12-04 00:54:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4332edc1-49bc-376c-90ea-11d6aaf2bf51 | -3.65921 | -50.69511 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 614ef610-7491-344d-a344-5ecef927cd94 | -3.98259 | -50.36787 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 15a50ba0-8510-35a0-8ac8-9e74bf8ca134 | -3.33934 | -49.7735 | 2024-12-04 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ddb2911-d62b-37f4-be91-9ecc33908266 | -1.22352 | -46.52852 | 2024-12-04 00:54:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9d829d53-11e0-3b74-b7d3-6d1f9f776e3f | -3.3752 | -51.1022 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5173f15c-bce4-3b8e-8f71-22c07fde8c00 | -4.6814 | -45.68089 | 2024-12-04 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4e82ab9e-e171-3a62-9cfb-3c25f86b7d22 | -2.88218 | -51.81485 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f011af3-e1f8-3822-aa6b-e0087b4d3ad8 | -5.63711 | -47.3705 | 2024-12-04 00:54:00 | TERRA_M-M | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3dcbebc-e048-3c8b-ac26-cba7ee9b8a89 | -3.2628 | -53.63264 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 240e3c9c-5612-3f0d-a2f5-6e7f50311351 | -4.31992 | -48.21815 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 874ba76c-f7c0-3efe-879d-2ad24609aefc | -1.9671 | -48.38922 | 2024-12-04 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0b83c84-9b54-335a-81c4-89c7c3e551e8 | -1.8361 | -46.23542 | 2024-12-04 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 41a89669-3acd-3eb9-a094-b69ad3ab8364 | -3.26471 | -53.64665 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| abbfc0d5-f78c-3884-8fd5-931254dae692 | -3.32564 | -50.34242 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7090af6-e20b-3890-b15e-fcad1c0c35fe | -1.40243 | -46.42142 | 2024-12-04 00:54:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b375497-5f17-37c7-bb00-452ec004f8ec | -3.34701 | -49.76335 | 2024-12-04 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 125b3acb-d641-3c6c-ade3-55f5be1affeb | -3.10226 | -53.28943 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 16037c83-ef53-344a-9d3c-a576f0fe75a1 | -4.72241 | -45.68044 | 2024-12-04 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a7388404-b294-3bf5-a861-0f0c7aaaed00 | -1.48571 | -53.79834 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 70f8005d-da47-393b-bc2e-bca713522315 | -1.51135 | -46.76667 | 2024-12-04 00:54:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 7929b98d-bd3e-3ad1-ad38-0e55a474876f | -3.82078 | -51.66674 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 197b17ac-3854-3bb9-a7f8-8321e3276fc1 | -2.96524 | -44.98462 | 2024-12-04 00:54:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 112ff644-6063-3e93-8f94-f0e7f8d914b0 | -2.81519 | -53.04731 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 93d82851-90e1-3afb-8491-b607a0883444 | -2.69649 | -51.87424 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0fa44050-fd66-367f-86b9-f11a197ebf0f | -3.93948 | -46.63947 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8c2a7a2-6ad1-3077-a70c-c0024688569d | -2.83152 | -46.75596 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8791cc50-14a0-3a25-b9b7-4e8589d14d9d | -3.51489 | -51.30845 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b6c5da09-7e51-395f-9fad-1e2e41f949f7 | -2.23879 | -46.11803 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b41cff3c-e2d7-30d1-8259-e6609d2b6ac0 | -2.80647 | -53.06125 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 663ebec6-1a44-36e4-9700-9172bce6231d | -6.74585 | -46.29873 | 2024-12-04 00:54:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f804610-8b78-32ec-b06c-76375edf78ee | -3.55439 | -52.92254 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c20bc686-7768-3882-bcdf-b5fd8d652207 | -4.21394 | -48.12039 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README11.md)
