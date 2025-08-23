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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 488fa839-f0ad-37e3-b3ea-9d8157df1bf4 | -26.59418 | -51.54427 | 2025-08-23 04:06:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c1eefdf1-f22d-3ea6-b3b4-8b4d59586630 | -23.90043 | -47.53345 | 2025-08-23 04:06:00 | NOAA-20 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d319963e-9b56-30c8-8827-79221dcb10a7 | -25.16476 | -50.07879 | 2025-08-23 04:06:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 65c32a91-93f0-30a7-9417-eb4751d70a93 | -23.49567 | -47.62584 | 2025-08-23 04:06:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04f9a718-eef5-3ba7-9928-eb6e671b7caa | -26.38494 | -49.9595 | 2025-08-23 04:06:00 | NOAA-20 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b3de53d-99d6-3e4b-8ee6-915151743214 | -23.41913 | -47.46626 | 2025-08-23 04:06:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 608ebde6-5e05-33b1-9aea-4cc862ad353c | -27.09459 | -50.64478 | 2025-08-23 04:06:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a2719ab-6b1e-328d-ab2a-4460ef978714 | -23.63176 | -46.44162 | 2025-08-23 04:06:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa830e27-4ffa-378e-9e6a-924dd7ed8a54 | -23.7441 | -51.09776 | 2025-08-23 04:06:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8763bf67-3427-3d5a-86cb-bfd29dae7f03 | -23.74317 | -51.10236 | 2025-08-23 04:06:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9999a178-e154-3540-9970-de414327cd8c | -24.80826 | -50.22556 | 2025-08-23 04:06:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cf051484-d116-3bec-a339-b0c6af6dba79 | -25.08503 | -53.17472 | 2025-08-23 04:06:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7e792c27-827c-3096-b87e-2cbebf9d9be5 | -22.96515 | -49.90899 | 2025-08-23 04:06:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 07e7850c-550d-37b2-b645-db50fc6c593d | -23.73883 | -51.10117 | 2025-08-23 04:06:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4b12754f-5f6a-31f3-89b2-32797977f81b | -27.0938 | -50.6488 | 2025-08-23 04:06:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbe12f5b-f7cb-3419-9965-7e1b8ea899b0 | -25.57071 | -51.0612 | 2025-08-23 04:06:00 | NOAA-20 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 4cfc01a2-c9b9-3c24-bfde-408e896f1df4 | -6.6044 | -44.5624 | 2025-08-23 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| fc95fa13-3877-3c2c-a486-25e03bfca5f5 | -9.968 | -60.1937 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 189.5 |
| ccc69cbe-01e0-3be3-a16d-40cc4c83ed52 | -8.5943 | -62.6315 | 2025-08-23 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| ba6fb4e4-4701-3d79-9eae-a0396ede7357 | -13.4155 | -46.2604 | 2025-08-23 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 351813c5-3f74-39e3-8a03-62adaed64c46 | -9.9495 | -60.1754 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 201.4 |
| ccdd9018-d529-3314-ae59-fb5e61cee439 | -5.7431 | -57.5814 | 2025-08-23 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a84132dc-05d5-3df0-929d-adeb80e1c63f | -9.9681 | -60.1743 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 8b5dd273-9a6d-32e8-b662-4a8eae96cfd3 | -12.9921 | -45.2252 | 2025-08-23 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5ef07731-3df4-3a69-b1cd-aef9077183df | -9.9493 | -60.1947 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 659.4 |
| a406fe2e-d12f-349f-916d-b12cc9f86b8b | -9.5179 | -60.5461 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fed1da21-96dc-3dcb-8635-edb83d114b08 | -9.9492 | -60.2141 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 3f43b604-7029-3da8-8ef8-67a9f97bb26b | -5.7615 | -57.5807 | 2025-08-23 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f0e89950-d474-32e4-9c17-53d6c58e3e7e | -5.7614 | -57.6002 | 2025-08-23 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e691378d-e9b2-37c8-b8b7-c31a171f5818 | -13.4151 | -46.2833 | 2025-08-23 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 9908ec62-c0b4-39a0-854f-cafc253b2096 | -13.4349 | -46.2573 | 2025-08-23 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1d4a1179-5d41-3762-b6b5-1b9f65335d82 | -8.5944 | -62.6126 | 2025-08-23 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 94a1dfff-2e0c-3426-8638-61d37cdd6da1 | -9.518 | -60.5268 | 2025-08-23 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4990627f-d8fb-3fab-a77c-098cd86045d0 | -5.7429 | -57.6009 | 2025-08-23 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 13855a2e-a720-35cd-aef3-bf347e2fc71c | -9.9493 | -60.1947 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 612.5 |
| 4b91073c-3555-34db-af3c-546217bec03b | -5.7615 | -57.5807 | 2025-08-23 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 50376489-f7d1-3d36-947b-418ac4926932 | -9.518 | -60.5268 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 213e5fcf-5f1b-3141-9886-dafc1199ec41 | -13.4155 | -46.2604 | 2025-08-23 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c705be41-b3c2-3cc7-ac39-e558523a6eab | -5.7431 | -57.5814 | 2025-08-23 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 518eb988-60b1-3a4e-9070-eaded444761d | -5.7614 | -57.6002 | 2025-08-23 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3c0ffeab-01fa-379a-91a9-1d5be2b479ef | -9.9681 | -60.1743 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 0c6b2908-daaf-31df-939c-1ef1b1c130b1 | -9.9495 | -60.1754 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 56c75f14-d885-3bec-8f7d-4c9baf22aea6 | -12.9921 | -45.2252 | 2025-08-23 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 71d7be7d-663e-3826-934e-10604e993371 | -6.6044 | -44.5624 | 2025-08-23 04:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0b53fc50-5e7a-3f63-9fab-bccb6023e51d | -9.968 | -60.1937 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 821341b6-3d62-3d0e-838d-2726b863a79d | -5.7429 | -57.6009 | 2025-08-23 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 3823b375-16a2-3d98-90b0-3a8e31d5efb3 | -9.5179 | -60.5461 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 3b091b66-05d0-3741-a7cb-fb260cd7ce04 | -9.9492 | -60.2141 | 2025-08-23 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8302085e-707c-3abc-acfb-bbe8106bf6e0 | -13.4349 | -46.2573 | 2025-08-23 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a685bf3c-aa4a-3509-86ab-2d9bf6aee1a9 | -13.4151 | -46.2833 | 2025-08-23 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| d7a93b7e-e523-37ea-ac94-d9e255d3b849 | -7.0164 | -44.6413 | 2025-08-23 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1cea8f09-687a-31ef-bbcc-63cb40c46db3 | -9.9495 | -60.1754 | 2025-08-23 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 305.8 |
| 4c75eba4-2166-3c01-a623-f6f0a1ba8cf9 | -9.9681 | -60.1743 | 2025-08-23 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 1b6e9b5f-a058-39b9-ae21-4732f3997e4b | -9.9493 | -60.1947 | 2025-08-23 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 564.3 |
| 6c014331-659b-3d00-a2b4-d207ebe74283 | -5.7614 | -57.6002 | 2025-08-23 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 3685ba1e-b68e-3a67-8509-89ebdbd36980 | -6.6044 | -44.5624 | 2025-08-23 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 912412d9-0991-3d6c-ab24-04fe0216403c | -5.7615 | -57.5807 | 2025-08-23 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bcbe0535-b83a-38a2-8926-5782ed5676f0 | -13.4155 | -46.2604 | 2025-08-23 04:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 331c0049-76f7-3a24-bcbe-d5519ef7e40b | -9.9492 | -60.2141 | 2025-08-23 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 2cfcced6-e419-327f-bbb5-da7ec3cabe71 | -9.968 | -60.1937 | 2025-08-23 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 33900453-36c4-393d-843e-97869b97ea7f | -5.7431 | -57.5814 | 2025-08-23 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e2c79a70-d8b6-31c2-aa17-be0e26b6b906 | -5.7429 | -57.6009 | 2025-08-23 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7d3c98d2-10ee-363c-b400-73760f99920b | -12.9921 | -45.2252 | 2025-08-23 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ccd1d2a9-347c-32b9-839c-eb0a2bf2ae8c | -7.0164 | -44.6413 | 2025-08-23 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a56773f8-5061-37ca-b63c-cf379445c527 | -9.1897 | -59.6171 | 2025-08-23 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b28de9a4-8f8d-3ef4-80aa-0524da234c90 | -9.9492 | -60.2141 | 2025-08-23 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2128188a-cb38-3a7d-b0d2-9c3b7c30572c | -5.7431 | -57.5814 | 2025-08-23 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 229fb5f2-a45e-363a-80b9-ca746ae17c1a | -6.6044 | -44.5624 | 2025-08-23 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a03cd960-9191-38ca-adde-b559eec59654 | -9.9495 | -60.1754 | 2025-08-23 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 204.9 |
| bb69d51e-2777-3ad6-a5d1-5d98b6d02f0c | -6.37 | -45.5356 | 2025-08-23 04:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dc0b463f-802e-302a-b1a0-60af76e42b2c | -12.9921 | -45.2252 | 2025-08-23 04:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8a4f250a-5c68-3ca7-b9bc-743d319a5e28 | -5.7429 | -57.6009 | 2025-08-23 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| af29a875-8b4e-3230-85cf-03657f7c37c6 | -15.057 | -48.4765 | 2025-08-23 04:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 6e3bb1c1-404f-378e-81a7-619079cbb224 | -5.7614 | -57.6002 | 2025-08-23 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| c7f856b5-43cd-38b7-a7fe-8f893b8a83a0 | -9.9493 | -60.1947 | 2025-08-23 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 547.1 |
| bee5b791-b3cc-310d-af8e-b4b503b0a9e9 | -9.9681 | -60.1743 | 2025-08-23 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| bbd3b91b-b6a5-33e3-9e99-35179e803a4f | -13.4155 | -46.2604 | 2025-08-23 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 963f5e78-9c39-33b4-9069-fa7614b5e6f1 | -9.968 | -60.1937 | 2025-08-23 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 191.1 |
| c9cc8440-35ad-3ca8-a947-e8fe69fbe050 | -7.0164 | -44.6413 | 2025-08-23 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d0bfa4b8-d352-3a53-a165-a15427d75292 | -17.5985 | -46.5481 | 2025-08-23 04:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b49ed84a-a557-3b93-8091-8fae38b50fb9 | -6.3698 | -45.5582 | 2025-08-23 04:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 766d13a1-cbf5-31d4-83de-4fd3fffdd11c | -17.5785 | -46.5523 | 2025-08-23 04:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2c0ed079-aaf9-3e9c-bc54-dbdc3f20521f | -5.7615 | -57.5807 | 2025-08-23 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| ff0886a9-a520-3d22-91fa-ddd75023afc0 | -15.0575 | -48.4541 | 2025-08-23 04:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 810ed4f6-edae-3c79-9c4a-e098ebb6bbb9 | -2.62387 | -46.84682 | 2025-08-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f50a598c-fa59-3424-bb4b-14f339a4345e | -1.69965 | -55.19213 | 2025-08-23 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a93e779a-562e-38b5-8426-1429bea15b65 | -1.55659 | -54.53906 | 2025-08-23 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c1edf8f-2151-3d71-be9c-14a241405b48 | -3.04882 | -47.0183 | 2025-08-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d9baa5e-5a6e-3b10-8229-83c785c03040 | -4.17389 | -40.71935 | 2025-08-23 04:49:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f298d4be-7276-34cf-855f-9a23e54ec3d8 | -1.56077 | -54.53565 | 2025-08-23 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34259761-974b-3aeb-8f10-b32effd55b27 | -2.71063 | -48.21144 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e284b51f-198a-3d93-9ad1-26cd6abafa52 | -2.44447 | -47.33088 | 2025-08-23 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 593f765b-0707-3953-a4f2-444e8aca0204 | -2.58384 | -51.91486 | 2025-08-23 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 563aba65-548c-35ce-beae-621a978d0376 | -2.25788 | -47.85252 | 2025-08-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 242aadc3-6e24-393b-bfe6-8531c5db8deb | -2.82337 | -47.72382 | 2025-08-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c7697c-e3a3-36b7-9c8d-ae77bada0eee | -2.44838 | -47.33148 | 2025-08-23 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 182ae747-6828-365b-959f-f78aaf5e2690 | -3.54856 | -41.62131 | 2025-08-23 04:49:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7bb28fb3-36fd-3319-b868-3ef4821352b8 | -2.91693 | -48.30658 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f13182e8-031b-3003-ae6b-e3fc372bfcba | -2.91091 | -48.24666 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3110dc0-b647-3166-9d08-21276f836557 | -3.04935 | -47.01472 | 2025-08-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README36.md)
