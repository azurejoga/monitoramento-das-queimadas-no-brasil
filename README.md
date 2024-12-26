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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d093032-6d2d-3450-a263-bd0e68ab8fdf | -5.2227 | -44.9034 | 2024-12-26 00:17:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a600077-4099-3ee3-b372-c0f4dce6e8c8 | -5.2301 | -41.252602 | 2024-12-26 00:17:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f0b6b14d-e0ad-3168-954d-d71a70175078 | -3.9182 | -46.921501 | 2024-12-26 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d452c537-a48f-3c14-9a74-f7bf6191b400 | -6.3134 | -39.7113 | 2024-12-26 00:17:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7ab35c08-4aaf-325f-b15c-ccb2f8d7bea5 | -4.5608 | -44.123001 | 2024-12-26 00:17:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4af36191-17b0-306b-bd9c-33ec981ddf68 | -3.0707 | -40.0872 | 2024-12-26 00:17:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e5f5710-fa13-3734-85a7-dd84cc364c0e | -4.3371 | -43.5056 | 2024-12-26 00:17:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb59fb6-3553-38fb-aff1-aeca028f4cfe | -3.9214 | -46.9813 | 2024-12-26 00:17:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04db826f-cae5-3b3c-aac1-f8410710d431 | -3.9116 | -46.983398 | 2024-12-26 00:17:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e04afe2-1f45-301d-ab1c-b660da22d1f4 | -6.983 | -34.902 | 2024-12-26 00:17:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 060e5522-71fa-3748-8637-d71b9c84d504 | -5.9548 | -44.4519 | 2024-12-26 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fe3a399-ec55-3aa2-bb0f-a8bcee34e901 | -5.2283 | -41.244999 | 2024-12-26 00:17:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4796032a-56f1-3552-aa54-70274efac1b9 | -3.1896 | -45.975899 | 2024-12-26 00:17:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09991ef7-4a87-3a34-b382-dd61d016ca44 | -5.2211 | -44.896301 | 2024-12-26 00:17:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8739f25-583e-312f-ad8d-263652d2b848 | -6.4524 | -38.861301 | 2024-12-26 00:17:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6c752040-5962-3395-857f-25ae96d059cc | -5.9419 | -44.440102 | 2024-12-26 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 007b3e72-4279-3494-9171-05c0edfcf272 | -5.9911 | -45.388199 | 2024-12-26 00:17:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9de7134-2f6e-3d05-9c70-e4c5115e4f90 | -4.3386 | -43.512402 | 2024-12-26 00:17:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b70fe1c-41f2-3d1e-8aaf-2795c222d801 | -4.5624 | -44.129799 | 2024-12-26 00:17:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b65f1f20-065e-3244-9c29-f5f222b444e3 | -6.9788 | -34.884899 | 2024-12-26 00:17:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22d10912-614c-3c7d-8d7f-b8f162efcaa0 | -4.5639 | -44.1367 | 2024-12-26 00:17:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 236b4244-7a58-3ebf-a431-b267b8fa7d43 | -3.0686 | -40.078201 | 2024-12-26 00:17:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7a05adcc-2cc9-3daf-8c02-a1b176fa0ecb | -4.592 | -43.6278 | 2024-12-26 00:17:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5049a762-e332-33a3-96d3-69a368aee593 | -4.4592 | -46.6745 | 2024-12-26 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb012db7-8e58-332d-9678-20571e31cb7e | -5.2318 | -41.260101 | 2024-12-26 00:17:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d908c4b7-1714-33ad-85ea-45eac62381b6 | -4.0479 | -47.040501 | 2024-12-26 00:17:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56c266ab-da6f-360b-927f-91efa58e06c9 | -4.4513 | -46.684799 | 2024-12-26 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44bc0b5d-dc35-3422-8b4e-acdcf7a58609 | -6.4547 | -38.870899 | 2024-12-26 00:17:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d5220c95-442b-3fc8-8555-0914bc093d26 | -4.046 | -47.0322 | 2024-12-26 00:17:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcfb13b6-e24b-308f-8fb6-903fe4caa4f9 | -7.7648 | -35.147598 | 2024-12-26 00:17:00 | METOP-C | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c38b0403-3e20-3179-bb7e-48a7b50058cb | -15.4316 | -39.479599 | 2024-12-26 00:17:00 | METOP-C | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ea02c24-e92d-3259-94dc-499e17179504 | -3.9146 | -46.905102 | 2024-12-26 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2d977b0-bba5-3fef-adc5-399bf89eb6c2 | -3.1912 | -45.983299 | 2024-12-26 00:17:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8531faa-06dd-33ba-9a9e-76ae2edeff1c | -9.2319 | -35.655399 | 2024-12-26 00:17:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0efadbaa-8bf0-3276-9a96-8f446c3dee64 | -4.0558 | -47.029999 | 2024-12-26 00:17:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf63d31f-3b99-34d9-815d-c5deafb4c2e2 | -5.5287 | -38.9244 | 2024-12-26 00:17:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 679b6f3e-0632-39b8-a81d-89f43a008ead | -5.9532 | -44.444901 | 2024-12-26 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51eebf2e-57dd-3bc4-abf8-d8df99c26d17 | -6.7846 | -35.304901 | 2024-12-26 00:17:00 | METOP-C | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| a0c50ab0-bcf7-3625-bc3f-bc321dddcecc | -12.7653 | -38.475899 | 2024-12-26 00:17:00 | METOP-C | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61bd56b8-b270-3bc1-811c-d98e53fd7dba | -5.9434 | -44.447102 | 2024-12-26 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35c1a9cc-ac73-33c3-8f63-321f1dc56496 | -3.9201 | -46.929699 | 2024-12-26 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6258cff8-7c32-3e25-b551-34b11c1fefb0 | -4.4611 | -46.682598 | 2024-12-26 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5211e68d-3f20-3d95-a496-75ec0d08ac1f | -9.2283 | -35.6413 | 2024-12-26 00:17:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f9a507a-3f58-322f-b82f-782d29b5de20 | -5.9517 | -44.437901 | 2024-12-26 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61d367eb-57fa-3222-aad6-8d2d96d486e8 | -4.5951 | -43.641399 | 2024-12-26 00:17:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db2df75b-6116-37b5-ba90-010c009edf20 | -6.9884 | -34.8825 | 2024-12-26 00:17:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7dd5824c-3096-3320-b037-583c24cb7ce5 | -5.2266 | -41.2374 | 2024-12-26 00:17:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 540683b7-90f7-349e-9d9d-ef928000ba59 | -3.4208 | -44.593498 | 2024-12-26 00:17:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de2b74f5-3851-3f62-8aff-08e7e8b6b3ea | -3.9037 | -46.993801 | 2024-12-26 00:17:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a769b3f-76f4-3479-a1a2-adea11b29fad | -11.4612 | -41.152302 | 2024-12-26 00:17:00 | METOP-C | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f0faf47-25c5-390c-8dfa-71c852017b34 | -12.0244 | -43.004002 | 2024-12-26 00:17:00 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c365d356-5b14-32f4-a7a5-a95a0c8c31e1 | -15.4298 | -39.472198 | 2024-12-26 00:17:00 | METOP-C | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f64077a-f2be-311f-a443-b75d05347e20 | -6.1809 | -39.281799 | 2024-12-26 00:17:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7a047516-cf58-345d-9fe1-ed2095c3b8f5 | -3.9164 | -46.9133 | 2024-12-26 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6cf1ba4-d00b-334b-a6b2-6d572fdc92eb | -2.7639 | -44.696499 | 2024-12-26 00:17:00 | METOP-C | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea9cc00-f0bd-3442-8a45-4849be15a21b | -12.0228 | -42.996899 | 2024-12-26 00:17:00 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 28849561-819c-3aed-8bb4-22a7863a681b | -12.026 | -43.011101 | 2024-12-26 00:17:00 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d5ad9d26-7fd6-3418-b5f1-b633c1c9f829 | -12.7674 | -38.484501 | 2024-12-26 00:17:00 | METOP-C | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8701c3b5-be2d-366e-92a1-2209c06deaea | -6.4501 | -38.851601 | 2024-12-26 00:17:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9e805c51-22ad-341d-b239-8232c6a8d6d2 | -11.8904 | -40.954899 | 2024-12-26 00:17:00 | METOP-C | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 23326fce-3e9e-3d8a-99f9-3c9aee854dc9 | -9.2381 | -35.638901 | 2024-12-26 00:17:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9af3f24-3f55-366f-aa36-dd49628f78fd | -4.5935 | -43.634602 | 2024-12-26 00:17:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e657bc7c-ff7d-3e90-83b9-79e456c51bc4 | -5.2552 | -41.405102 | 2024-12-26 00:17:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d932d425-cca5-3ae6-b223-f4a0427be170 | -9.2416 | -35.652901 | 2024-12-26 00:17:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49695132-a85c-37c2-9957-c0137208b198 | -6.9927 | -34.899601 | 2024-12-26 00:17:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1ce52b4-be4a-3623-bd2f-90f5d86ea1ba | -11.892 | -40.962002 | 2024-12-26 00:17:00 | METOP-C | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 677eb260-53d0-3212-a332-f1a37b19c978 | -3.844 | -46.6833 | 2024-12-26 00:17:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd8a3ed7-3352-3c32-a461-5c8262ba0194 | -9.91974 | -36.32952 | 2024-12-26 00:43:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 171.8 |
| e3e3edb0-3a52-356f-b19f-3811cbe7d51e | -12.02421 | -43.00917 | 2024-12-26 00:43:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 334230d6-eb2f-341d-bf94-4b790b95ed24 | -11.89035 | -40.95668 | 2024-12-26 00:43:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 86e3495c-9bb0-3a90-8fe9-b280489808be | -9.93205 | -36.33263 | 2024-12-26 00:43:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 144.7 |
| 2f737a9d-b67d-3f3c-8244-762bcc218eef | -12.02255 | -42.99816 | 2024-12-26 00:43:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 9ebcd026-51fc-345c-b4ec-f1e4d4e4ba61 | -9.92593 | -36.29596 | 2024-12-26 00:43:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 118.5 |
| 9eab0a45-fc74-33fb-b915-2b48b79bf6fa | -12.0145 | -43.01066 | 2024-12-26 00:43:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d62d9fd3-546b-3479-bab7-7c9ffcffca63 | -9.9134 | -36.2933 | 2024-12-26 00:43:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 16fba80a-cb8f-3579-b8e7-fe1d47f573cb | -4.62642 | -47.05136 | 2024-12-26 00:47:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c06e7144-65b0-38e2-a4eb-c0b644cde082 | -4.58424 | -43.64196 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 183507bd-abe3-3e9c-9437-0bf20567b0e5 | -3.4223 | -44.59383 | 2024-12-26 00:47:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b50b90a5-b9d6-3a99-8b37-640bd5fbc35e | -5.21789 | -44.91285 | 2024-12-26 00:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b246ffab-e5c1-3b7e-8f93-6e8716013a3a | -3.46318 | -50.08996 | 2024-12-26 00:47:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f80eeef4-9818-3252-960a-cd1b66708c82 | -5.9415 | -44.4537 | 2024-12-26 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2719bc49-ab1e-3421-a739-9b1e4f356fb9 | -4.55235 | -44.12952 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f3e77d6d-d4ea-3b42-a400-e860d0d5c995 | -2.82187 | -45.93599 | 2024-12-26 00:47:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f2534a8-e6b5-33e7-8da5-4a91565b96e9 | -2.64198 | -46.10107 | 2024-12-26 00:47:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f17a5e3f-a2f6-3041-af79-fe839f7a134b | -4.3331 | -43.51781 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 76f0bc1e-2621-3acd-87c4-82e09b53a69d | -4.33129 | -43.50506 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 90b3cb40-b974-32ee-85bb-382b4113ef79 | -5.95114 | -44.4523 | 2024-12-26 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8653f205-6481-39b5-858d-6a519b1d7765 | -3.81533 | -46.71634 | 2024-12-26 00:47:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5de35100-fe47-37c5-974d-77168933566f | -1.72905 | -52.60205 | 2024-12-26 00:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4b042c02-b8a2-3f36-a86a-e88f54cb1fed | -4.55403 | -44.14112 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| df727770-76f1-3490-aa2d-2ed7b0ab4c76 | -5.94958 | -44.4417 | 2024-12-26 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c50e476a-d3ff-3735-95bd-8e882dfd51c6 | -4.00826 | -46.71321 | 2024-12-26 00:47:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a3ff9c41-bd55-3329-9cfc-79b5c9d16bdd | -4.56238 | -44.12807 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 8584e947-2015-3583-89f3-0a2a0de64947 | -3.99294 | -46.73367 | 2024-12-26 00:47:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d23b0919-cde5-3214-ab47-0450e039d324 | -4.32763 | -43.51225 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b4724753-9a77-3d81-8bd1-eed93ebf2ddc | -3.30056 | -45.61171 | 2024-12-26 00:47:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4cd08270-a427-326d-86f9-1a246f6dfe59 | -4.56406 | -44.13968 | 2024-12-26 00:47:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 994ad650-c06f-3695-9cc4-dd67bd5e482e | -3.46978 | -50.28138 | 2024-12-26 00:47:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 44d24373-472f-304c-a889-773f660a03dc | -3.98664 | -46.68884 | 2024-12-26 00:47:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3eadb01d-0014-3cc9-89ff-4e7d5ff9d80b | -2.29019 | -45.63061 | 2024-12-26 00:47:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README2.md)
