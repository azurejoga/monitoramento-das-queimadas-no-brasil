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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e585ac-f521-3715-821d-193caac76f06 | -9.382 | -56.826698 | 2024-10-29 01:11:52 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cbacb72-47b1-3627-8be9-6fc4e2b3786a | -6.6049 | -47.362099 | 2024-10-29 01:12:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2502fb13-3539-30b2-8db4-1a0d4c6fcff5 | -6.5109 | -47.0289 | 2024-10-29 01:12:01 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3838a6ab-28cb-3a00-a0d6-a032f04b8b90 | -6.5953 | -47.364498 | 2024-10-29 01:12:01 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d845939-80b6-39e5-8fd1-23b5c52bd241 | -6.6016 | -47.389599 | 2024-10-29 01:12:01 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0ed4d15-f1c1-30c3-aa78-50f63b7a866e | -6.4946 | -47.004601 | 2024-10-29 01:12:01 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1984f326-0f5a-3425-825d-33613f6d08f3 | -6.5013 | -47.0313 | 2024-10-29 01:12:01 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10f3de70-6c20-3adc-88f0-9e3cd33d8ea8 | -6.5857 | -47.366901 | 2024-10-29 01:12:01 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c93d53-7592-3e6a-b99f-f04d7eda18ff | -6.5919 | -47.391998 | 2024-10-29 01:12:01 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbe7ebc-94ad-3563-9a03-578e504754d6 | -4.2635 | -46.071899 | 2024-10-29 01:12:33 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc534413-006f-31c0-a5e1-524cb8685c94 | -4.2539 | -46.0742 | 2024-10-29 01:12:34 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac41055-b28e-35ee-b51d-da8ba314ea4e | -3.2495 | -46.867199 | 2024-10-29 01:12:53 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5711f33f-6786-3d54-850e-56574c927f33 | -3.3033 | -47.172699 | 2024-10-29 01:12:54 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00ab5ac1-b05b-3e7a-811e-fe80c9ea23d7 | -3.3104 | -47.202 | 2024-10-29 01:12:54 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92df5f2-5514-391d-afc4-12c15fff69df | -3.2937 | -47.174999 | 2024-10-29 01:12:54 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b990fcde-e2a0-355d-bc0a-0e0b21dbbe26 | -3.3008 | -47.2043 | 2024-10-29 01:12:54 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0512d4cb-f0b0-3156-9bed-a9b166556730 | -4.0973 | -50.518002 | 2024-10-29 01:12:54 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa9fccf-fbb2-38c3-b6f7-dad2004cf943 | -5.3164 | -55.8167 | 2024-10-29 01:12:54 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e630d2c-91e0-38cf-aab7-9a1ed6c459ee | -5.3182 | -55.824299 | 2024-10-29 01:12:54 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 196aa387-bc1b-393e-95e7-19f76f6d449b | -5.3066 | -55.818901 | 2024-10-29 01:12:54 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ec0a66-91e2-3712-b58a-562042ce0ec6 | -4.2034 | -53.455299 | 2024-10-29 01:13:03 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f4061b0-e1e0-3ff7-b685-5a68c6648940 | -4.738 | -56.036701 | 2024-10-29 01:13:04 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e6fe05-1473-32e8-a36c-8c4602d308c1 | -4.7398 | -56.0443 | 2024-10-29 01:13:04 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9fa7ac-6fae-3aa6-a373-389745a6f422 | -3.3237 | -50.281502 | 2024-10-29 01:13:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f79330-e77c-3df1-8327-eb2a996144c8 | -3.328 | -50.299301 | 2024-10-29 01:13:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e39c98-c02d-38a1-9105-dbcdf44bb535 | -3.6921 | -51.841801 | 2024-10-29 01:13:05 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c618c0-3c71-3fc4-977a-b958f0253e9a | -3.314 | -50.283699 | 2024-10-29 01:13:06 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2607da1-116e-3fe7-b4b4-e6979b6df437 | -3.3183 | -50.301498 | 2024-10-29 01:13:06 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd010ef0-cdbf-3135-9e18-2a694da58a6b | -4.1079 | -53.93 | 2024-10-29 01:13:07 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 643f8f8d-52ae-3d7d-8838-8e234cd11dc0 | -4.0959 | -53.922401 | 2024-10-29 01:13:07 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9eab413-fb51-3393-a3ec-46137ae0a2d6 | -4.0982 | -53.932301 | 2024-10-29 01:13:07 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d399e8b-bba6-3a79-bbb3-c7210d25eb2c | -2.5102 | -47.424999 | 2024-10-29 01:13:08 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fae33b6-f0f4-3e04-b6d6-70d906d115c6 | -2.5171 | -47.453899 | 2024-10-29 01:13:08 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe06dbf3-85b9-3881-a590-61b9fe1c746d | -2.5006 | -47.427299 | 2024-10-29 01:13:08 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d00f13b-c116-3263-8929-097959819c45 | -4.1158 | -54.2747 | 2024-10-29 01:13:08 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7446fc44-295b-39fa-ad45-21c9b478e293 | -3.1812 | -50.371201 | 2024-10-29 01:13:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e435d3b-6be9-3018-bfc0-6ddf93f12bc2 | -3.1854 | -50.388901 | 2024-10-29 01:13:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86ee690e-3733-399f-9580-bed4dbc530dd | -3.1715 | -50.373501 | 2024-10-29 01:13:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0272d2ae-c26a-3ce4-9a0a-5fc567bae150 | -3.1757 | -50.391201 | 2024-10-29 01:13:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04f3466b-4276-3bfa-85c4-53a84b539e31 | -4.3935 | -55.747898 | 2024-10-29 01:13:09 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd25d8d4-4dac-334f-9af6-fb4beba58a08 | -3.1584 | -50.578499 | 2024-10-29 01:13:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b0da43-b960-3290-8059-9b0fa971810d | -3.9856 | -54.112999 | 2024-10-29 01:13:09 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 422af910-9382-34df-bbc2-f81305f407cb | -3.9878 | -54.1227 | 2024-10-29 01:13:09 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2885066-e848-3b76-9d0e-e264c85748c4 | -3.1487 | -50.580799 | 2024-10-29 01:13:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afac45cf-a608-3fe7-ac50-90c46394a330 | -2.8168 | -49.2225 | 2024-10-29 01:13:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea25aac-5e58-3c7a-b828-93724d487239 | -3.0453 | -50.403099 | 2024-10-29 01:13:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494b587c-40b3-3b65-8476-7bf1a6a2be24 | -3.0356 | -50.405399 | 2024-10-29 01:13:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6fc865-0891-36f1-9d97-8f87abedf20b | -2.0748 | -46.497002 | 2024-10-29 01:13:11 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd7b665c-78b4-38dd-82f5-ebc31d63b338 | -3.5495 | -52.989201 | 2024-10-29 01:13:12 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 906bd57a-951e-31b8-8ccd-467270ab945e | -3.5998 | -53.780998 | 2024-10-29 01:13:14 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f59cc9b4-538c-30b0-8600-721d5da43de1 | -3.6982 | -54.25 | 2024-10-29 01:13:14 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9260d3b-4464-361f-867b-09ec9a2ea64c | -3.4179 | -52.821602 | 2024-10-29 01:13:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be42ae3e-7c67-3b55-b5f6-506a610246f8 | -3.4317 | -52.880901 | 2024-10-29 01:13:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6bf511-24c5-3e90-bbfb-dd2fd1b2aa1e | -3.4755 | -53.245701 | 2024-10-29 01:13:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3f93626-95a0-3ae0-a101-181062b72b7e | -3.595 | -53.760399 | 2024-10-29 01:13:14 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64be951e-4d13-38d5-9f3c-bb0d412ec1d2 | -3.5974 | -53.770699 | 2024-10-29 01:13:14 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 043122e8-35dd-37d4-adda-8603e30e8f80 | -3.7159 | -54.415798 | 2024-10-29 01:13:15 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2927ab97-b2be-37aa-a5d1-7eb9e529d8d9 | -3.7061 | -54.418098 | 2024-10-29 01:13:15 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a6600b0-d669-3c82-94af-3f88dc9cb798 | -3.6701 | -54.306801 | 2024-10-29 01:13:15 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b9c250-0c2f-3806-88e6-73781b83d226 | -2.3393 | -48.887001 | 2024-10-29 01:13:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba515eda-421b-3a60-83d1-15bcba0c014a | -2.3447 | -48.910099 | 2024-10-29 01:13:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1cfec8a-130f-3079-ac48-3546c7ca8e54 | -2.3296 | -48.889301 | 2024-10-29 01:13:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a69629b3-cd80-31c1-a60a-f258dde17577 | -2.335 | -48.912399 | 2024-10-29 01:13:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f3b6731-1ec0-3e39-beb4-3acfbb1a64be | -3.6399 | -54.666801 | 2024-10-29 01:13:17 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40769c93-0704-34c2-b8ae-4b91dce350ba | -2.9091 | -51.742599 | 2024-10-29 01:13:18 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8928196-7594-35c1-9ca7-677418794d94 | -2.9125 | -51.756901 | 2024-10-29 01:13:18 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee6e39c9-e0bc-333b-8187-265506a5d87f | -3.577 | -54.661999 | 2024-10-29 01:13:18 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8515c518-7c2a-3c6f-9523-c717fc26b20b | -3.5672 | -54.6642 | 2024-10-29 01:13:18 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cabd6d68-e729-39fc-b620-a79b6bb38bc7 | -3.2104 | -53.388401 | 2024-10-29 01:13:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424f0f6e-6da1-3ba3-ba96-6c12bf35bfd8 | -3.472 | -54.6087 | 2024-10-29 01:13:19 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb1433bf-bd2f-3f1f-8557-66f60cd818af | -3.4622 | -54.610901 | 2024-10-29 01:13:20 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb056a5-9393-3670-b939-38e530487b8f | -3.4126 | -54.4851 | 2024-10-29 01:13:20 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a430231-6fab-3d18-967c-b23eef1cf277 | -2.9928 | -52.894299 | 2024-10-29 01:13:21 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c986c70-dad9-3f37-96e2-5561eedd9615 | -3.2764 | -54.162102 | 2024-10-29 01:13:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 053ba746-84d7-33e2-bb97-e24508dd1e2c | -2.6489 | -51.7267 | 2024-10-29 01:13:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddaedbb5-4cf6-3c7a-993a-2a962b2d1292 | -2.6523 | -51.741199 | 2024-10-29 01:13:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c2f2c5-fe49-3fcd-bab0-dbfd5dfb35dd | -3.1093 | -53.706902 | 2024-10-29 01:13:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89689be7-ff9d-30bc-85bd-1134cf1b5edd | -3.155 | -53.9044 | 2024-10-29 01:13:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48aa06e3-d894-3f14-8d64-4a0e14418633 | -2.6392 | -51.728901 | 2024-10-29 01:13:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d91599a9-9821-3480-8ccf-83e983386889 | -2.6426 | -51.743401 | 2024-10-29 01:13:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 506f4d54-2962-3052-85fb-7bd6c9ff259a | -3.0995 | -53.709099 | 2024-10-29 01:13:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 915efe03-3bd0-30fb-a7d1-adf4da1d164c | -3.0994 | -53.797501 | 2024-10-29 01:13:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8215af1b-2bf3-3385-8e47-f106d49320f2 | -3.0002 | -53.4133 | 2024-10-29 01:13:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56d71d9-4097-3da8-9a8a-798d01df7ad8 | -3.0028 | -53.424301 | 2024-10-29 01:13:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd9e2587-1c12-3905-aec5-356fec8c6e37 | -3.0053 | -53.435398 | 2024-10-29 01:13:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d2a9c06-e6b5-39aa-8432-463d855ab345 | -3.0897 | -53.799702 | 2024-10-29 01:13:23 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13a92b42-3ed5-3c95-ab26-fb982cd9ac9f | -3.0921 | -53.810101 | 2024-10-29 01:13:23 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 081b30ae-77bd-37ff-a514-942a31b655bc | -3.2988 | -54.706001 | 2024-10-29 01:13:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e60a03-90ea-3f91-a515-16ddbce5c883 | -3.1335 | -54.256599 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67051550-9406-37a2-9e0a-4200eb52a151 | -3.1357 | -54.266399 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ddc90bf-54e1-348f-955a-4ae2bca2083d | -3.1237 | -54.2589 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea126ba7-9c36-3de9-9a1a-bbaca218cc0a | -3.1259 | -54.2687 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebbff31c-88f6-37b6-bb17-1c418939a65c | -3.1281 | -54.2784 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0634f5df-a600-3931-be86-e66874073459 | -3.114 | -54.261101 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15e19a16-48b1-3963-b441-d91025d0c4b9 | -3.1162 | -54.270901 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e49f431-cc99-3853-80e4-c05d2120787d | -3.1184 | -54.280602 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32da36b7-61c4-39b4-90f4-2361919ebe4c | -3.0792 | -54.155102 | 2024-10-29 01:13:24 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccfa682-945f-387b-bd53-96a603268488 | -3.0815 | -54.165001 | 2024-10-29 01:13:24 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac8d7785-1a9c-3ec6-8c7d-b44c5699dd26 | -3.1042 | -54.263302 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35824feb-ea94-39a6-9c69-3338337c7d63 | -3.1064 | -54.273102 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
