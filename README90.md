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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a4f14c3-7ccb-3cf6-b74b-693654cfb00f | -8.90963 | -45.04326 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77862161-b838-3d0e-8963-5e696b4d269c | -6.34509 | -44.30453 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 681bf992-f2e9-3467-b700-23e2066cba16 | -10.98599 | -46.67554 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1b9b8c15-b3bf-349e-90f4-009ccbda36c3 | -6.88104 | -39.28054 | 2025-10-03 04:32:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ffa3bb1-739a-39f1-9418-0dda08aee28e | -12.11674 | -43.44468 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77fb2b28-3886-3083-9374-09508c31b256 | -9.92716 | -43.72827 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 616b9918-c499-363a-bcb4-4f4fd399cb5e | -8.30233 | -44.85649 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8066a10-0a48-3f0c-b1dd-cb2e03ba07ac | -11.78066 | -46.83146 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a928cad-c694-387f-92f2-2fc39a9eba42 | -10.28389 | -50.303 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72dbb544-55f3-3dae-ae15-411375b6fb0b | -11.48617 | -45.11459 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d57cfa7-7fe6-302e-9f5a-305faff9b349 | -11.90642 | -46.29422 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d51e8aab-358b-392f-a60b-3f1a1248eb9e | -11.83578 | -44.9449 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3df6f62e-cfaa-3e4d-95cb-1b2ba07db703 | -6.04683 | -44.62625 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1bf76b27-d098-3214-8c12-6e0211d70d57 | -6.95353 | -45.34909 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b2f33b6-4182-30e3-b1c9-6bf8f2123c64 | -10.3384 | -54.18958 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bcb3250-0d2e-3b38-96e3-a53c1b233882 | -10.00517 | -50.24576 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 849cc494-bbdd-3ec8-8bd7-f68cfc9f38d0 | -6.37706 | -43.8861 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ecdfafa-b9df-3248-9d77-5b12b4338697 | -5.3526 | -43.75166 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 18bd54be-2a0d-3247-8743-463296ea90c5 | -9.07087 | -46.6566 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 973ef6b9-9978-3a71-85f5-eabf8d9631e5 | -11.61475 | -45.02907 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7c87bf7-7b5c-3193-82eb-12708613feac | -10.2668 | -50.36469 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7c1fd30-7034-38bc-8efd-493c99df5716 | -7.75363 | -42.56939 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| ec934e9a-47f7-3ea5-9eff-36c64efc3c24 | -7.77794 | -42.59193 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92b7f537-985d-30d6-bc82-35ffdcf29b3b | -11.10402 | -47.83556 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f74fcd-08e3-3d95-b157-2b42205c0edc | -5.81863 | -49.06325 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba873c1f-14ff-32d9-a61b-8a5ccaee3fff | -7.30215 | -45.26636 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9df30689-46e6-38dd-9ce0-bef2734c0928 | -9.91524 | -43.72661 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 33590809-adf2-3d66-8bd1-8d63ab56d2c6 | -6.87878 | -45.47767 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da186ba-b473-3f43-966b-d53da059f3a6 | -10.8989 | -46.72103 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b30a0283-3ba2-34f9-8c44-0c6dee7b1856 | -11.13865 | -47.19211 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c15811-6aa6-38fc-b3a0-82ff0a8bc847 | -8.86568 | -47.67168 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6db71b6c-9958-34ed-9c52-2226489e5ee1 | -9.09337 | -46.72009 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddcf3b49-4212-3709-8bf7-c9f447691bdc | -7.74426 | -42.59079 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e44118dd-69e6-3745-8441-983373ce1d10 | -7.56052 | -42.39411 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e1465bf-f50a-327a-a4ab-f11f4444f1c8 | -6.045 | -44.63847 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da03afe0-92be-3193-bac8-236be14add4c | -7.77545 | -47.37116 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2924f117-63ee-36e3-96bf-c436acff94e3 | -9.90408 | -43.71969 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3ccf7a68-cdbd-333f-92c1-334516237f49 | -9.9451 | -43.76447 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25a91e1c-9584-3acd-9694-0c5eb97c06e0 | -11.07266 | -48.36698 | 2025-10-03 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea4843a-dd88-34f3-b8be-6d54563c25e3 | -11.93569 | -47.88141 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c00046-e1f9-3bcd-aaea-d5f8382f1c01 | -6.06599 | -43.22 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6f59d8f5-e948-3998-bf2e-b54233f03656 | -11.53754 | -49.82458 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 783491cc-f490-3fa8-bacf-756bd06003ba | -8.58678 | -41.06695 | 2025-10-03 04:32:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c48ad474-415c-308d-942e-a8219624bbdd | -6.04744 | -44.62218 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39120a9c-8db7-39cc-942b-608e24593664 | -10.33715 | -48.18452 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebe58e0c-7fe9-3627-b007-2cd115e0a48c | -8.1809 | -47.00876 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 036854e8-fd56-3c18-aab9-71bee81d438e | -7.74583 | -42.57958 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 09b74958-f51e-3e40-a163-fe2f29082683 | -6.04121 | -44.62669 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 81eebbe3-6b88-39d0-8743-8e900a15b3bc | -8.51677 | -50.03601 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfa403ca-2c02-3031-b248-d6813bc7056f | -7.66692 | -47.28273 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4ac8831-9d2b-3f17-817c-7749eb9060af | -11.9159 | -46.2789 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 93ab45c2-22cb-369c-a759-fed5790df35d | -9.90263 | -43.72984 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6055e7a-0cc3-3f1e-a1c1-37ff1e93d13c | -10.3047 | -48.28339 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 377e7d04-490a-3bec-8713-8ae1a918cdcc | -11.4985 | -45.00491 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a71da627-38c6-3324-842d-9b4e2d602292 | -12.11267 | -43.44341 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90ce3151-c144-3887-984b-b19fc013e230 | -10.87429 | -46.72105 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da54c10c-d818-379c-9073-e529ab3f416d | -11.60078 | -47.65173 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0348c29-0f91-3aae-937e-7b210ac25d38 | -8.91087 | -45.03481 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d119fc52-859c-3684-8a8a-47279a61b0db | -9.94783 | -48.78138 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 860eee30-eef5-307a-902e-b22fb4944834 | -11.64659 | -46.86665 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcadb7c5-7765-3b57-a7d1-645140f42ccb | -9.95296 | -43.70789 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4db0104-d9d6-3ce4-ad18-3d2c621213b4 | -6.2379 | -45.36457 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 008c0b66-1244-3c24-b2f9-72b3ee72f1a8 | -9.94508 | -43.5757 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a753288f-e5eb-32cb-83b4-2d86f20d4117 | -11.55657 | -47.64841 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cd92772-37a3-3f7a-adcc-53f136d61a15 | -5.63058 | -44.70528 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83bdf646-0235-3533-8e64-3bdc95cc969f | -8.24174 | -47.03646 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77209748-a51b-38c9-b2f4-63184421b882 | -10.96708 | -51.08023 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fdcb254-b94a-31f8-908b-75a75a9abcbe | -9.42207 | -47.54266 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddce6fe9-8c63-3737-8b2e-f34639ae1c6a | -11.48805 | -45.11312 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95bd7ff7-7faf-36dc-8cd5-58bc9c0e69e0 | -8.59252 | -44.78837 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16d5ddba-b2c1-3fa1-add0-4dd82e1c195e | -8.7561 | -47.33051 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5c9e62d-7ea8-3169-92a9-a306d5795a31 | -7.74834 | -46.26506 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 223af519-5f6d-3227-ab6f-4c4a1b8ca22e | -10.20685 | -48.19331 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3656536c-ce7f-36ef-998d-983fda52dddc | -6.61184 | -44.29617 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af1af416-a5d4-37d3-901d-e1b5dd262c17 | -5.63104 | -43.91004 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| da195fc3-a487-33f0-b24f-cc749e617c19 | -11.58458 | -47.66763 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a06f3195-40d0-3f1d-864e-d958b2be3d83 | -9.6598 | -48.21691 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b173abd6-3de1-334b-991b-b28f4d6b00df | -11.45071 | -44.96433 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27bf553b-c4bc-36b1-b788-ab7221788ef2 | -11.16067 | -47.1843 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbf7f93d-ec4e-3814-8a1c-7b6fefbdf88e | -11.1505 | -47.18267 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00fc53f8-9058-33f0-bd88-601901c37789 | -7.74948 | -42.56878 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 09a85609-5bca-30f8-b9d2-f79a0ea83cbd | -12.11799 | -43.43565 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e952941e-d8b3-3a32-acd6-99d7f917cb14 | -5.82677 | -48.86246 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85df820b-34e3-3b4c-9342-f934ccd3f3ef | -11.66901 | -44.27428 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 989eb54c-55f7-3d68-b17e-0ff184f1f7ea | -10.00677 | -50.25739 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6598029-9dde-38d3-859c-d77a938450cc | -8.6482 | -47.71651 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 134ffdd3-52ac-3941-8c59-a8f60e48de0f | -6.70847 | -42.80616 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 244b7e6d-5b3f-31aa-bdca-be81d7647858 | -6.75795 | -44.80687 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 742b74d0-5418-3a8c-b8ed-567d1dc88b06 | -9.91427 | -50.50183 | 2025-10-03 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40a5505f-d51d-33b3-82b9-3a468f20cc1a | -7.8028 | -46.02147 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6af2d51d-9108-3b22-8b71-a1d4c445bd97 | -10.60361 | -48.71546 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 58fc586f-9114-3ead-b901-6c26e5c4a49e | -11.07192 | -47.80481 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 455aa8a7-f57c-3aaa-a0ec-25a6fd8fc6c6 | -11.81489 | -44.90262 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36bd6547-8b66-39c1-9f30-53ccba8d0c3d | -9.75735 | -46.3105 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 847bd992-0d9e-3e3a-a743-56fd359c94bf | -11.14089 | -43.39595 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 98b5402c-8139-3b66-822a-7a3e00ef482e | -7.3171 | -42.88008 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 686a4c7f-550f-3412-a026-bf5c0710ac77 | -11.4676 | -45.03302 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f8a16d2-e004-3094-96c0-00fac84b9dcf | -5.84631 | -43.37473 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 04ebedb4-d450-3a62-8fe3-45e50dffb754 | -11.77866 | -46.82802 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c7419aa-1313-30d0-97a6-72b2a580e22f | -10.86739 | -46.67346 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README91.md)
