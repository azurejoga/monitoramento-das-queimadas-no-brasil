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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 755d8f07-6534-3f0b-bd91-897dd40e0898 | -11.6527 | -52.191 | 2025-09-02 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| d3d0da84-f771-3ed2-8ea2-ad54031a4436 | -8.8659 | -45.7788 | 2025-09-02 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e7ccd35c-530d-30c9-9d14-4951870b19a0 | -8.8467 | -45.8034 | 2025-09-02 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 66c147db-8d31-350d-b584-010dcb117f89 | -8.8656 | -45.8014 | 2025-09-02 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| b2c1bbde-ea14-37b0-aa12-d09a471b9b4f | -6.8911 | -45.8538 | 2025-09-02 12:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d4485ef5-b53a-3b31-98be-5e320ec6daf0 | -9.7483 | -48.9814 | 2025-09-02 12:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 91e7608b-fb1e-3551-b1b7-b8cfc0618f59 | -11.1033 | -44.6548 | 2025-09-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| db5b63f2-34d1-3e58-806a-848c32e68570 | -10.062 | -48.1197 | 2025-09-02 12:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 29038eda-7e24-37e5-87f6-5cb2fa418fd5 | -11.853 | -51.453 | 2025-09-02 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e154cf12-a00c-3753-b9a3-8146151ac692 | -6.2038 | -43.3475 | 2025-09-02 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 26e207da-5bfd-3e75-b240-9dc7efc471a6 | -11.9224 | -50.6153 | 2025-09-02 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| caa8d7e8-2c09-3193-9718-93e7506ef09c | -10.2976 | -47.5201 | 2025-09-02 12:30:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c063ca1b-6042-3a2b-b792-93c079759e76 | -8.8659 | -45.7788 | 2025-09-02 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 12aebd2c-a54f-3eec-b94c-bb1bedcda223 | -11.8518 | -51.5378 | 2025-09-02 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2c0b385b-0138-395d-a98d-0102244ca55d | -11.9415 | -50.6131 | 2025-09-02 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 44f04df7-b03e-3f14-a600-c53c888b2753 | -11.6715 | -52.21 | 2025-09-02 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 8b8b1b6d-8163-3e3f-a7f6-6dfdaf169a5f | -9.4794 | -46.4994 | 2025-09-02 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 15a1b48f-8a85-34aa-8977-3203a7dc008f | -8.8656 | -45.8014 | 2025-09-02 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 158b2cec-b859-3860-9ae0-3a4a3ca9ed9c | -5.9511 | -44.2937 | 2025-09-02 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9bacdb76-f650-336c-99bf-3f15ececd356 | -11.653 | -52.17 | 2025-09-02 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| faa688ce-9fce-371c-915d-93ac2f4d30e4 | -11.672 | -52.168 | 2025-09-02 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a714ea56-1bd0-3ea0-a674-27558181c5d1 | -10.0623 | -48.0978 | 2025-09-02 12:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f1de3191-58b9-3792-9f9a-b7289a67d681 | -11.1037 | -44.6315 | 2025-09-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| b598725b-3b5a-3825-b3bb-8e563cfbde34 | -13.3082 | -46.8229 | 2025-09-02 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| bc7b9130-2f15-3e2b-a71e-44dd72f388c9 | -11.6717 | -52.189 | 2025-09-02 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 66ac397f-fccb-3e3c-a2e2-3d5aba9b7eba | -8.847 | -45.7808 | 2025-09-02 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 06ac1934-8e5c-3529-9005-6fcfaefed6af | -11.6527 | -52.191 | 2025-09-02 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 38424124-f569-3611-8049-e55d5502e95b | -4.9124 | -43.187 | 2025-09-02 12:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f02b4f6f-ded6-37e1-b5d0-1deda1a00d85 | -7.9165 | -46.4354 | 2025-09-02 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| aaa8f687-6a6d-3d7f-a1be-fd59cc78b95f | -6.8724 | -45.8554 | 2025-09-02 12:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 49816fa9-900c-368d-b74d-724b5aab2680 | -5.9698 | -44.2923 | 2025-09-02 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 66c8cef9-2a96-3e0a-8681-3b92b3ee3c88 | -11.8527 | -51.4742 | 2025-09-02 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 2666b26e-ef36-3611-8eb0-06c91664fe16 | -6.8911 | -45.8538 | 2025-09-02 12:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 8b227042-e9e0-34b0-ae31-bd47cbc90b0c | -9.7294 | -48.9834 | 2025-09-02 12:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 50fbf9ee-d010-378d-a343-7fd2a78d5da2 | -7.9351 | -46.4559 | 2025-09-02 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d93eacfe-b5d6-37d1-812e-4fdac1d1f437 | -11.5694 | -47.6081 | 2025-09-02 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 0cdfc13c-e2d1-3125-9392-2aa1f48324ca | -8.8638 | -50.5847 | 2025-09-02 12:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 351f4ffb-7948-3174-9d07-36e1e4b0d960 | -8.8467 | -45.8034 | 2025-09-02 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 39742c6e-675f-3c8c-813e-f56235ca52d2 | -7.9163 | -46.4577 | 2025-09-02 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 0cc2e303-931b-32cf-9d1c-2ab6f33ad2c7 | -5.04043 | -45.11945 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 0ee20b01-7818-3484-8d48-057bb7486faa | -5.54677 | -43.89512 | 2025-09-02 12:34:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 68b4b647-7adf-32ef-9c1b-850ba6d58756 | -10.05351 | -48.0978 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5d22ab69-ec46-3960-87ca-759804722166 | -4.26585 | -47.60827 | 2025-09-02 12:34:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6bb9f2ec-8afb-3059-a807-97e9e1d34b8a | -7.12003 | -44.75882 | 2025-09-02 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5f634360-2715-398e-b5db-b30cbb8d5a5c | -6.03052 | -46.01288 | 2025-09-02 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2d8ef454-e81f-318d-b22f-6783823074ba | -10.05196 | -48.10933 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0381f2af-c264-39c0-ba50-ee918417b2bb | -4.78241 | -45.31741 | 2025-09-02 12:34:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c24c5aac-9552-3d06-af86-9303ef318eea | -8.85239 | -50.58489 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 136817c8-9cb8-3974-a95e-2d713662b3fa | -7.47541 | -44.82407 | 2025-09-02 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 3b2a875e-4a78-36ba-ab5d-fa029a340cb2 | -3.2377 | -47.12882 | 2025-09-02 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf7eb934-0bfa-39b7-9858-ad949d79d305 | -9.75208 | -46.91616 | 2025-09-02 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 38589a15-da90-33bf-99ce-86de5bf710e8 | -7.50189 | -45.35498 | 2025-09-02 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b0a33ec4-f06b-3859-8c9b-f67d15ba86fc | -8.0615 | -52.3551 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c3033cf0-2212-3c07-99c3-9991eb08d325 | -4.29832 | -46.26053 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1cd9d0d8-521a-3318-b163-dac77fd16420 | -8.21052 | -49.51786 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d06e19a1-2729-383e-aaaf-cead18df4ecc | -10.06046 | -48.12265 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ee646c1d-6dbb-3ab4-a643-bf2f031be722 | -6.29087 | -44.39604 | 2025-09-02 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e4e4ce93-538f-31b9-b5aa-87dd1a1bdd77 | -9.46442 | -48.30047 | 2025-09-02 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3789e051-5178-3fc8-97c0-08314bba31e6 | -7.69758 | -50.27873 | 2025-09-02 12:34:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0763c81b-1b62-3227-a9d0-4856a6a9967c | -6.58658 | -45.39395 | 2025-09-02 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 41facd80-dfe9-38ea-8cb4-3fea7d5a62f6 | -9.646 | -47.78981 | 2025-09-02 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| d1bb98df-f839-3240-bb0a-8291b0f6f133 | -6.00567 | -47.58599 | 2025-09-02 12:34:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2173ce10-0038-38b3-9a3a-cd26f359767e | -6.96408 | -44.34261 | 2025-09-02 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d6fa5999-8b96-3493-880d-1e2f85753598 | -7.92024 | -46.46983 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| c04bdb1f-63f0-369d-8069-d72fc3c9b98f | -6.66571 | -45.89899 | 2025-09-02 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| a1485389-480f-3869-b7e1-3c0f75143dd3 | -4.92108 | -43.20579 | 2025-09-02 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| c04e3c61-e24f-395e-bc9f-ba3c78b8abe8 | -6.87553 | -45.87587 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 151.7 |
| d6353097-f08c-3537-8b93-79b30d32e134 | -9.65511 | -47.04025 | 2025-09-02 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ae0fc8da-768a-3944-83a8-1cd66eec1017 | -6.19349 | -43.35974 | 2025-09-02 12:34:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| b7ddeef0-1a20-3f1d-b6e5-08fb82ee4576 | -6.88879 | -45.85262 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c726d1a1-df7b-3854-b629-283d408b53fc | -5.81364 | -41.94823 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 0a0708e3-9cc6-316b-b600-1f95585744b7 | -7.11871 | -44.75305 | 2025-09-02 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 627f3f34-cb8e-330d-9a7b-544c8dc27d50 | -6.33456 | -53.43336 | 2025-09-02 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b1a0c48e-dc02-3432-929f-ce8d333f734b | -4.90729 | -43.20414 | 2025-09-02 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 49ce91f8-9ba6-3c84-8b68-0e090ad45db0 | -5.96507 | -44.28999 | 2025-09-02 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e4a78f5d-0e86-37ea-90c6-f9ae7c176b41 | -6.59241 | -47.70803 | 2025-09-02 12:34:00 | TERRA_M-T | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 666e0105-a0bd-3d50-823c-a4382c771a73 | -8.85271 | -47.54166 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ca2c5c52-afe8-3c02-a142-31757bebd2b4 | -5.87631 | -42.99746 | 2025-09-02 12:34:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 10bbc7fd-6212-3ca3-86c3-6f5a9ef0742d | -5.80198 | -41.94123 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 15a7f89a-5859-3178-a72d-43cd72844935 | -7.91288 | -46.43948 | 2025-09-02 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6bbf1dc6-3321-3e5a-862d-5bc877e3cd18 | -8.85334 | -45.80912 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| f8cff3bb-ab90-3e9c-9336-a1c8c035bf96 | -9.83 | -48.31598 | 2025-09-02 12:34:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 31a8825e-7619-31f3-865a-c134889f6d0c | -6.89119 | -45.84646 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 6ea86235-e1d8-3dc8-9ca3-816fe745c62d | -6.35128 | -45.5971 | 2025-09-02 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 71384a76-c292-3e7e-a263-3f745e0b9a13 | -6.77024 | -45.71571 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 55607c9f-daab-323a-99ea-150e157f865d | -7.69886 | -50.26971 | 2025-09-02 12:34:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 63992253-9d56-35b2-88fb-fb66b08d91ef | -8.74518 | -46.11995 | 2025-09-02 12:34:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8d052382-2395-3479-8fc3-3c27212cb88e | -9.25569 | -47.11729 | 2025-09-02 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d56a3243-1ff6-391f-893e-da4453b30cbe | -8.05248 | -52.35389 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5def3dd-9eb0-3fb3-ace3-c41e390d70d1 | -10.05514 | -48.08572 | 2025-09-02 12:34:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 8792d5f4-6c8d-3259-8685-00c02ae5aa66 | -8.20138 | -49.51661 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d4014579-e2cf-3f77-8348-f27230dbb371 | -6.87733 | -45.8511 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6976fe3a-b8b5-3b68-8819-ae15bfd8cb00 | -5.76549 | -44.60144 | 2025-09-02 12:34:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0a229b7f-693a-3bfb-b696-64dd2910bd94 | -5.78555 | -43.8581 | 2025-09-02 12:34:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4485cce0-c813-3849-8b53-c253bc563ead | -10.25983 | -47.52534 | 2025-09-02 12:34:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 84757e88-baa4-3724-aaa9-172920cb36d7 | -9.50032 | -46.4766 | 2025-09-02 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| fc755927-9e3c-363b-9468-e995660949ab | -8.83179 | -45.78864 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 69f0fea2-1fb3-32a6-8eb2-b6f368886ed4 | -10.0624 | -48.8797 | 2025-09-02 12:34:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1c3136ae-69ae-3556-b8e3-24eb151ce9c4 | -6.87534 | -45.86665 | 2025-09-02 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8379c156-4dc4-3799-93af-d03929303d9c | -8.43708 | -47.34766 | 2025-09-02 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README90.md)
