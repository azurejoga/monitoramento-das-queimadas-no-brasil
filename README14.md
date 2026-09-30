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
| 84ac802a-ac23-329c-8a82-d25cdc37878b | -7.2718 | -45.32037 | 2026-09-30 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7894faeb-e29f-303f-9344-da223981ac69 | -11.38202 | -43.37612 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9bfe89ba-36d1-3ea3-80c2-2b3668702321 | -10.90461 | -43.85551 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21c38989-d457-37e4-a20a-72954794b1e2 | -4.94985 | -49.4131 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca9fdf4d-15e5-39c5-b7e6-6b9bb0fb882b | -5.73027 | -43.50875 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0747c60-e9b1-3cd8-bd14-be7552bc3a4a | -11.41593 | -43.46935 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d3c02fe-907b-3e4e-8f0d-5b01ee7d4278 | -9.8623 | -44.93848 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79c01e58-b4e2-3f9f-aa42-50bd8d6595ce | -11.18341 | -45.1217 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c286e9a4-c550-3691-babc-a3e0e1d46764 | -5.81929 | -46.2182 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2731f50-7f81-38fe-ba61-c5727449315f | -7.51983 | -44.54017 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 769eb8a9-bad7-315a-8f55-c96290396100 | -7.92434 | -45.44087 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e7a74a1-8aa4-300e-a7c0-41dcb72a3d9f | -9.80969 | -48.21236 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aaa540bb-49f3-38fd-9362-609dc2ff86b5 | -8.71737 | -47.59393 | 2026-09-30 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04d9e654-8864-378f-b5f3-5e962823744a | -11.17628 | -44.82452 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ed17252-8384-3e8d-8c10-90162dc60ba9 | -3.51093 | -50.31149 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1aee9b1-18cc-3345-b40f-d3c67e1665ef | -11.41375 | -43.47176 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eed33f9f-9139-3922-b68b-d0b8f8b10721 | -8.24998 | -45.44315 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8ab299e-57a3-38da-b1e0-de00a72449f7 | -9.82125 | -48.20781 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4c7c0f1-c933-3089-bd72-3c68ee877e37 | -9.81434 | -48.21614 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3465784b-e289-31fd-abe6-8ec8780735d6 | -5.75523 | -45.1718 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 25ec83a6-8c61-37ab-b5b0-4dba922199b4 | -5.75974 | -45.17261 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 21c0f349-dcbd-3d0a-8af3-9b1ffb4e49f8 | -9.78415 | -44.8123 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dd7abc3-6dd9-3923-992b-48728b766049 | -8.25793 | -45.44958 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba64dde4-5873-38ed-a672-b6f97f8e9372 | -3.97026 | -48.00795 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e05ae935-6bb4-3d8f-916a-56b81ec60d04 | -11.68017 | -43.50087 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8e3c05d-1168-300c-a8d1-59bdb12d2387 | -11.71507 | -43.45176 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c821cb4b-0b89-3e01-8c7a-b751586f3a94 | -4.94886 | -49.41282 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 710d074d-e48b-3020-b000-b90925907fda | -12.19412 | -38.24402 | 2026-09-30 03:55:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c73a4b1-ce20-371b-a943-fa4a80ccbdd2 | -9.81968 | -48.2083 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c18dbdb6-ec04-3200-aa77-5a83aec71b89 | -6.33146 | -43.91364 | 2026-09-30 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f92e7b50-a8eb-3e2c-ac0b-6ab859cfff98 | -5.73641 | -45.17326 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a3ebb14-95a6-35a7-9ffc-4dfb820b3805 | -6.7055 | -45.99207 | 2026-09-30 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02f29cba-dc2f-3775-94ac-d7384aeb4854 | -7.50206 | -45.82769 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d7aefd9-a507-3842-8062-459ad9861b66 | -7.81976 | -45.81715 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1f6f3f44-405d-3eb3-b3c5-9afad3e98780 | -7.01708 | -45.29918 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f2bc5fe-4ae1-37e2-86be-85c1c9f88072 | -9.12911 | -44.75027 | 2026-09-30 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6c245501-f486-342a-8dec-83d27e98dc72 | -6.07828 | -47.29154 | 2026-09-30 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e453863-65a3-3de1-b376-d0ee6bc23a1c | -9.66576 | -45.11336 | 2026-09-30 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2778b368-242d-3832-ab9e-6e19a1002929 | -10.83472 | -48.69878 | 2026-09-30 03:55:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d3435d1-efdf-30cf-8d3e-b702d8380f38 | -9.76564 | -44.82085 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e8bdf7c-d64f-30b4-937d-30d5b4c101f5 | -9.80899 | -44.74293 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c58f0410-c210-34cf-8fcc-d8453221f97b | -5.09164 | -46.04041 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5e4598c-52d4-3d70-acf1-dfb06c0f9149 | -3.37694 | -50.9446 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b59ce561-400e-3ba6-bd78-559b6871f62e | -11.70475 | -43.44539 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17155d56-c72e-33bc-a537-8b0347b80637 | -5.74994 | -45.17564 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba7521eb-69d5-3d09-bb64-17d8b2c18f68 | -7.84264 | -45.8206 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e193ec9e-5701-374f-b34c-26197fc841aa | -7.02154 | -45.29998 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 962b1a50-e1d6-3893-9f59-4453215d463b | -9.66086 | -45.1166 | 2026-09-30 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 029f911a-94cb-3515-959a-cf1991ade9ee | -7.84721 | -45.8213 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5b21d826-7b10-3dca-8026-a76ba4538790 | -11.41453 | -43.46728 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01099bc2-d9c3-3beb-b682-54d58af6f762 | -7.81061 | -45.81574 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c6bb956-158a-3f40-b26e-493e2337d556 | -9.78904 | -48.2298 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e4ae18d-ba4c-3bf1-987d-935e12feb120 | -11.41369 | -43.48285 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a56a3481-da63-370d-be6b-bf60ea9e11ed | -11.41775 | -43.4264 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94e3d673-e941-385a-a1a7-a1a21fe4b4a3 | -12.33702 | -39.75294 | 2026-09-30 03:55:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 04a4c309-009b-32a7-af3e-be5ef42db958 | -10.50425 | -36.97638 | 2026-09-30 03:55:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 14883b24-dd75-3b2f-89a5-16dc168e0cde | -10.15021 | -36.23808 | 2026-09-30 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b759bf97-70c7-30af-a558-6285e7659e84 | -11.3855 | -43.46875 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a2efcfca-343a-39e2-94b6-cfd3f943499c | -8.25185 | -45.43523 | 2026-09-30 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70ba7e27-a87f-3d8b-8c55-c88176457d62 | -5.97596 | -46.61139 | 2026-09-30 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b9767d3-56db-3682-855d-b53ac85b01b9 | -5.33707 | -46.19271 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f87fb30f-15f0-320d-b1ac-c69c3927cc13 | -6.33082 | -43.91742 | 2026-09-30 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f99314e0-45a6-3163-98e8-c97c38ff6fc7 | -5.09251 | -46.04427 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a71ae32a-c690-3844-ae9c-5fdcac55d1db | -10.5213 | -45.37349 | 2026-09-30 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a20b302c-a99a-399e-92f3-79eab865f8a7 | -7.85178 | -45.82206 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 81d8276a-0546-3b49-8ced-7964a9d42fe6 | -11.63774 | -43.52597 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b945976-997e-34e7-a4ed-4c9b26bf4084 | -11.39959 | -43.47578 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 06f41a4d-0284-3ca8-a61b-f7de5252e69a | -11.1776 | -44.82108 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 17026ebe-fee3-3eb3-bf2f-ade948c81055 | -6.33567 | -51.15591 | 2026-09-30 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cdf31fef-c99d-3243-b5a6-86a35b45e2af | -7.52826 | -44.54501 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d283926-88e4-3731-ae85-8e9ac4aa374a | -10.70281 | -50.83426 | 2026-09-30 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e33542e-9d6a-38fd-8508-8ffc9639ff87 | -6.33201 | -43.91779 | 2026-09-30 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1540d28b-6082-3fd2-99e3-1a74a45739cb | -10.91218 | -43.85048 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ea98874-46f1-36bd-80a3-91325587e0ed | -5.72584 | -43.28426 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85ef66d1-e6f7-3dde-967f-631559526a24 | -11.63326 | -43.52983 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd503f6b-b190-3e5c-9b89-2fdc26444991 | -11.40191 | -43.41623 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e04d677-5c05-3cc0-9235-f675373d60b2 | -11.42515 | -43.42767 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f71b5bf2-f42d-3031-9ed6-12bb0bf3d492 | -3.37869 | -50.84536 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5cce5474-368b-351e-93f4-a5223ab14f28 | -11.70769 | -43.45049 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 53518a21-2ae2-3fda-abe7-6299cf87e7d6 | -6.37916 | -43.4263 | 2026-09-30 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef8218fc-7318-36f6-8cd1-478d302362be | -4.80523 | -45.64102 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bba6494-6646-3063-9e32-ba5e845d8bb5 | -10.08766 | -50.30627 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 929ff1d1-6ed8-3fda-8d66-579f9feca3e1 | -4.81471 | -49.45925 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7b0e6ae-754d-3eca-8745-af534ffc345d | -6.94916 | -41.59406 | 2026-09-30 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35c2505c-6b24-37ea-a7c3-61449c0c2aa8 | -10.90207 | -43.86338 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5460bf79-ca4d-33f0-8134-d8be11d7e3dd | -11.63697 | -43.53048 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd94b3dd-f0a5-3e6e-a284-c18d6982583f | -11.44289 | -43.43531 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fbb6afa2-9289-392b-9d2d-dcf4e5b74459 | -11.44212 | -43.43979 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1a478ed8-531c-324f-97a7-1694c2721179 | -4.80436 | -45.64619 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c6cdf3b-be87-3c23-8d54-a42eb197d3e5 | -7.05116 | -41.54796 | 2026-09-30 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3e665e34-f4ef-33b4-8849-12a94842caf0 | -6.18615 | -44.64773 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b68c257b-9c44-30c8-aabe-3e69e19c337e | -7.92986 | -47.37718 | 2026-09-30 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee83f7a5-400d-347e-b7ef-1a640551b9a7 | -10.08597 | -50.31493 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8ccb246-6a75-3713-bd57-39498acebdf9 | -5.70226 | -44.73157 | 2026-09-30 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49600991-1638-30c5-bd9e-3df51e39f11c | -4.29859 | -48.60625 | 2026-09-30 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce37867d-87ac-365a-b9a4-5f8ceba8e2f3 | -5.74212 | -45.05736 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 301861c4-a60e-337a-b974-a11f6940a4ea | -10.71361 | -47.82728 | 2026-09-30 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 962a5a45-62a7-352f-91d7-0c77c7de3462 | -11.36213 | -43.35898 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6af18eb9-df62-313c-ac14-2ce6fe5c8800 | -11.41592 | -43.48138 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 902a7b2b-a8a0-353a-bf71-63c6043d01d8 | -11.413 | -43.41815 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README15.md)
