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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bf185dc-ad0a-3b94-ab4b-32a5371b1112 | -11.666 | -47.5288 | 2025-10-09 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 298ceecd-845b-397c-b334-3c8226b9cb74 | -9.1018 | -47.9575 | 2025-10-09 01:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7860416c-c6a0-31b3-b648-059a8ae30886 | -9.191 | -46.8881 | 2025-10-09 01:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3c3ff6f6-6db0-385c-a41b-1b379b67cc55 | -14.4334 | -43.9635 | 2025-10-09 01:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 168.4 |
| aa4e91b2-5e41-3ad9-8b95-5ed6bc802ad1 | -4.2864 | -44.5171 | 2025-10-09 01:50:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a4c5663b-1c6b-39ed-b41c-363cb71ba639 | -6.6808 | -46.2961 | 2025-10-09 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |
| cbb7605a-a0dc-37ab-a09f-063c9d9e1075 | -10.8554 | -44.6431 | 2025-10-09 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 514.9 |
| 2084242b-bb64-3881-856f-630cd415a02d | -7.7569 | -44.0183 | 2025-10-09 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| dc575137-d69d-341d-a9a8-7808a4605f79 | -10.8558 | -44.6199 | 2025-10-09 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 769.0 |
| d400da30-ce97-3733-8fa2-a4878c938f3f | -9.0829 | -47.9594 | 2025-10-09 01:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d0c8918f-ae96-3112-bb32-c91f1eceed48 | -13.7913 | -45.8321 | 2025-10-09 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 21b70a1a-429c-3f7b-b902-cb0da20d24a6 | -4.9721 | -45.1362 | 2025-10-09 01:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 179b2666-133a-319f-a80c-acc70ca1a630 | -4.9908 | -45.1351 | 2025-10-09 01:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 3c37251f-1869-3b81-9cda-7b0b2fb1570a | -14.4334 | -43.9635 | 2025-10-09 02:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 160.3 |
| f0c47263-fa9a-3d52-b22c-65b08e38ccb3 | -10.8562 | -44.5966 | 2025-10-09 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 35e52cc7-5888-3aa2-9064-58d163dde934 | -4.4446 | -43.2164 | 2025-10-09 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b2e5c2f5-0132-3e2e-afc6-92b77ca8f63c | -19.9568 | -44.8867 | 2025-10-09 02:00:00 | GOES-19 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 74.9 |
| baa29927-57b1-3727-a430-ed841e4561a7 | -8.1993 | -43.3424 | 2025-10-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 503ea882-afb7-37fc-97bb-79e396884e4f | -5.4187 | -40.9841 | 2025-10-09 02:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 813f6ed8-4391-31c5-9e88-61711021123a | -18.4125 | -45.2155 | 2025-10-09 02:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1ba8d4e2-f315-3bb5-b659-ec309be2a4c5 | -19.9363 | -44.8919 | 2025-10-09 02:00:00 | GOES-19 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 79684193-5dfe-3d0f-bd4b-bf39727bb4fe | -10.8554 | -44.6431 | 2025-10-09 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 443.7 |
| 635894ef-fa05-3707-a2e8-b2428804f3c1 | -7.7569 | -44.0183 | 2025-10-09 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ea801207-6efc-3952-b6a0-b7675861dc3d | -5.4001 | -40.9613 | 2025-10-09 02:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 230.5 |
| 243cb3b1-ab65-3849-865f-b51a64a145a6 | -17.8413 | -57.6459 | 2025-10-09 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 9f524773-3429-325f-ae41-cd46a87afc95 | -4.9908 | -45.1351 | 2025-10-09 02:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| a8906d8c-d70e-3d52-9fd6-64796d2095f8 | -6.6808 | -46.2961 | 2025-10-09 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| d1791daf-75ea-3649-86da-5fabac006d53 | -5.3999 | -40.9856 | 2025-10-09 02:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 410.9 |
| 208805b5-abd0-30f1-8cc5-3a9c04793721 | -6.6993 | -46.3169 | 2025-10-09 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c71712d7-7057-3546-8e96-43436bc1e2a6 | -10.8558 | -44.6199 | 2025-10-09 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 915.9 |
| c035a0a0-50ce-333e-ba26-5dc28fc1616a | -4.991 | -45.1124 | 2025-10-09 02:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 1c9e8565-34b2-37bd-b28e-7981285d890c | -10.8745 | -44.6404 | 2025-10-09 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 2536012d-03db-39f3-ab29-5c1b211b3289 | -7.7755 | -44.0396 | 2025-10-09 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6c828cfc-0b78-3469-baf1-704ac8124919 | -14.4138 | -43.9672 | 2025-10-09 02:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 3ac03029-0b99-3bb5-ba25-3d63513f3ad4 | -14.4133 | -43.9911 | 2025-10-09 02:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| cb6d8cb6-dbe3-38d2-90c8-61631e01b597 | -9.0829 | -47.9594 | 2025-10-09 02:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1eb15eb7-dff1-3107-920c-112888098587 | -18.4118 | -45.2394 | 2025-10-09 02:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 4b66b453-5a3c-39e0-b99c-ce845316b332 | -14.4329 | -43.9874 | 2025-10-09 02:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d539b0a6-38d9-3606-8374-a27ed29e2855 | -7.7567 | -44.0415 | 2025-10-09 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 34317de9-77a4-3276-936d-689f93145173 | -6.6806 | -46.3184 | 2025-10-09 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1b50ba58-f65e-37f6-aadb-2bf31d8c4b5d | -8.5021 | -46.222 | 2025-10-09 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9f6296b1-ae4f-3737-b7b6-083c02b57805 | -6.6995 | -46.2946 | 2025-10-09 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 387d79a1-6109-38a1-8e74-a5cf10f505a8 | -10.8749 | -44.6172 | 2025-10-09 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 373.4 |
| b5ceec08-0597-3417-8b6f-f55df619ada3 | -5.4187 | -40.9841 | 2025-10-09 02:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 95a957d0-e00d-33fc-9134-7a0988bf4ec8 | -10.8749 | -44.6172 | 2025-10-09 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 8f5fb29f-8626-372c-ba86-05133748a86e | -7.7567 | -44.0415 | 2025-10-09 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 99da8f72-14e9-3a1e-a809-8c12e442b446 | -8.5021 | -46.222 | 2025-10-09 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 972038f8-f5f6-3605-93d4-0e6d4fbededb | -10.8745 | -44.6404 | 2025-10-09 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5ca0d6c6-209d-380c-bb0b-e27400a2f9be | -8.1993 | -43.3424 | 2025-10-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| f5280466-da45-3877-a173-cad53d7f6a06 | -10.8558 | -44.6199 | 2025-10-09 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 515.4 |
| 0a5763a3-8d30-377d-ac60-64d0bdb04309 | -6.6995 | -46.2946 | 2025-10-09 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 9d3eabac-60fe-36a3-a038-690172e40a31 | -14.4133 | -43.9911 | 2025-10-09 02:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fd478ebf-3b78-3043-9da8-59468e523713 | -18.4125 | -45.2155 | 2025-10-09 02:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ef32205e-c107-3b64-bd3c-703fc7d3e791 | -5.3996 | -41.0099 | 2025-10-09 02:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| af42dd3b-4069-341b-bc51-1bee5bf2d21e | -9.0829 | -47.9594 | 2025-10-09 02:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e3ad5605-ce38-380b-b90f-a2fb27d1912c | -5.381 | -40.9871 | 2025-10-09 02:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 83ff394d-729b-35cb-8f52-d1214b7b1299 | -7.7755 | -44.0396 | 2025-10-09 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2d9c2a90-fdd3-3902-8c80-90cd57df436b | -14.4334 | -43.9635 | 2025-10-09 02:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 493306cb-be81-3c0f-a8ed-08b620e1b35b | -6.6808 | -46.2961 | 2025-10-09 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| dac6ead9-431e-3236-a25f-01213ef4093a | -8.5398 | -46.2181 | 2025-10-09 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 279f0cd2-9d52-327c-9e97-0f3337b636f5 | -10.1901 | -44.5703 | 2025-10-09 02:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 700b710c-0620-3530-a099-ed029c002f67 | -10.8554 | -44.6431 | 2025-10-09 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 5e522aec-9c55-33fd-806c-911365333d2f | -18.4118 | -45.2394 | 2025-10-09 02:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 150.8 |
| ff72fbc4-e30d-30c1-9c52-130d9c3ebfbe | -17.8413 | -57.6459 | 2025-10-09 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| d1152705-ebeb-3d49-9d25-6cad202b8cbf | -14.4138 | -43.9672 | 2025-10-09 02:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 1ec4818d-fbf0-3975-9ea3-440abd55f2c2 | -6.6993 | -46.3169 | 2025-10-09 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d29c5437-d3fe-3124-9e4c-3a021881ce20 | -7.7569 | -44.0183 | 2025-10-09 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9ecbe28b-e17b-333e-bda6-76a19b897fa7 | -5.4001 | -40.9613 | 2025-10-09 02:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 335.8 |
| b5944815-0478-326c-b9e1-be5393ad457e | -5.3999 | -40.9856 | 2025-10-09 02:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 583.2 |
| 97b5ef2b-4645-3ae7-a30c-b98c900b8772 | -6.6806 | -46.3184 | 2025-10-09 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 6792f60b-5a68-3e18-877f-a7a8cb029911 | -14.4329 | -43.9874 | 2025-10-09 02:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c1bf0152-93b5-35b4-b9ee-50f431a67407 | -10.2092 | -44.5678 | 2025-10-09 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| da68480d-bdf1-301d-bd43-033a96068ea5 | -14.4133 | -43.9911 | 2025-10-09 02:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4149309c-1955-3337-8dba-6d27d121f2de | -14.4329 | -43.9874 | 2025-10-09 02:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 98.5 |
| af8512f7-fe9d-3bc2-8545-a823bcefdb8c | -14.4138 | -43.9672 | 2025-10-09 02:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 44d22255-cd6a-3b71-8e88-15dc5f1f6f03 | -9.0829 | -47.9594 | 2025-10-09 02:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a2912d4e-6cce-3363-b1ae-1930e348113f | -5.4001 | -40.9613 | 2025-10-09 02:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| fff7b23c-9b13-3006-b21a-7f0b06126d68 | -8.5398 | -46.2181 | 2025-10-09 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8eb6ddec-d653-3f23-8cb0-968cdc271e66 | -10.8745 | -44.6404 | 2025-10-09 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 97ca8a9b-9562-3c76-b6ad-12e86a454ca2 | -10.1901 | -44.5703 | 2025-10-09 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a28e406e-b377-368c-aa05-81490916c75c | -5.3213 | -43.5316 | 2025-10-09 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3d93ad7f-69eb-3958-9644-893b033ab01b | -10.8749 | -44.6172 | 2025-10-09 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| c3a178ef-9726-3371-98c5-2605e4a17212 | -6.6993 | -46.3169 | 2025-10-09 02:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 08dc89b1-a7f8-3daa-bbd1-6957b2b3b3ba | -5.34 | -43.5303 | 2025-10-09 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e17c584c-3346-3473-8300-eda92162bda1 | -5.3215 | -43.5084 | 2025-10-09 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| fbc34aa9-e536-3fb7-9b58-91e8c696830c | -14.4334 | -43.9635 | 2025-10-09 02:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 11899c0d-f426-3de7-867b-7e57e1174298 | -7.7755 | -44.0396 | 2025-10-09 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 9e549089-d941-3b05-81e8-01f250858cf4 | -6.6806 | -46.3184 | 2025-10-09 02:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 774aaa43-3108-38a9-8b47-ee8f5eb9c741 | -18.4118 | -45.2394 | 2025-10-09 02:20:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 09d0359b-a814-3f05-b310-c1aa0f635a0d | -7.7569 | -44.0183 | 2025-10-09 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c83678ac-fecf-3207-9867-90c3a3d84f4d | -18.4125 | -45.2155 | 2025-10-09 02:20:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 2616e8fd-be73-3e75-ad11-65fa05318ef2 | -18.432 | -45.2348 | 2025-10-09 02:20:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a3f39dac-63d1-3675-836f-edadecf0c7e8 | -5.3402 | -43.5071 | 2025-10-09 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 546251f8-a4bb-3a84-ad3b-1785d631c523 | -6.6808 | -46.2961 | 2025-10-09 02:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 1ee24d3a-4ef9-3546-ace2-409161ad0401 | -8.1993 | -43.3424 | 2025-10-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 1bbada7d-1c1c-387e-967d-4f17f6d16900 | -6.6995 | -46.2946 | 2025-10-09 02:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| a743b4cd-1713-3866-a18a-031cecc85029 | -10.8554 | -44.6431 | 2025-10-09 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 6d1f7996-b0e3-3216-9e93-d679d8e8b6d9 | -10.8558 | -44.6199 | 2025-10-09 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.0 |
| 8b71f0dd-0dcd-38fb-a53c-1502a2e56d1a | -4.4446 | -43.2164 | 2025-10-09 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| f17b47ba-6316-37b7-8fb4-e05012e2f13c | -7.7567 | -44.0415 | 2025-10-09 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |


[Clique aqui para ver as próximas entradas](README8.md)
