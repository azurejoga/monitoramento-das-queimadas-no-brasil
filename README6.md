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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 565604cf-dc0c-3ab1-a51d-d1233f230b4e | -23.29107 | -45.78539 | 2025-09-20 03:17:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dcbcc7f1-66b5-39ea-9e0b-03082ac048c9 | -22.63751 | -44.52151 | 2025-09-20 03:17:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| acf9c38e-2373-3911-8df5-414edc6e697f | -21.944 | -41.36209 | 2025-09-20 03:17:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8488624-85bf-344d-88be-bdf224815a5a | -23.28433 | -45.78329 | 2025-09-20 03:17:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9781fc45-0277-309e-a61b-4b7692eb84c6 | -15.68011 | -42.47655 | 2025-09-20 03:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d696afc8-82e3-34c3-b358-eb0cfd238648 | -22.80556 | -45.27872 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 0a6b6306-1940-3cf5-9273-cf02a35e501b | -15.68319 | -42.47665 | 2025-09-20 03:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a48c82-fcc4-34dd-9e1e-d2c60ed6c59b | -23.32055 | -45.98174 | 2025-09-20 03:17:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9c1dd218-d831-374b-926d-45583c5773c3 | -13.0693 | -42.14177 | 2025-09-20 03:17:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a65b8c11-bcd4-343e-8078-d284e1393cbd | -14.72925 | -42.36959 | 2025-09-20 03:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1d435c67-1581-3838-b86a-734a35d8aaa1 | -16.32577 | -43.96618 | 2025-09-20 03:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67fdd39e-55e5-364e-a75c-8fc254df116c | -14.72601 | -42.37584 | 2025-09-20 03:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e763efac-cad2-3daa-a171-123d1184d6a4 | -22.80059 | -45.27018 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e240b5e6-536e-378f-89ac-2a8220085096 | -21.59973 | -41.26383 | 2025-09-20 03:19:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c0be1ddf-9c57-3b7a-9889-f6df55aa65ea | -21.59887 | -41.26767 | 2025-09-20 03:19:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d8a70f70-0f27-3561-8717-d7acb6334ef8 | -5.1181 | -43.1964 | 2025-09-20 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7f28d28f-7598-3bd7-be14-17bd5072b167 | -5.0994 | -43.1977 | 2025-09-20 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 2a1109ca-adde-3f8d-be21-ede110f690ec | -13.0747 | -42.1261 | 2025-09-20 03:30:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 2e8655a1-a06b-3cd5-8d17-56d279f80372 | -5.19703 | -45.48308 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1efa9e3b-bb10-370e-ba9d-32d269042cce | -6.1386 | -43.44387 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f94f5a6a-dc99-384e-bdc1-4775edb8b444 | -4.62028 | -40.20969 | 2025-09-20 03:34:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f57e14b-652e-3a71-8db4-72e974f44fcb | -5.55231 | -42.16484 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 15fa66a9-7851-35cc-abb7-21343cf08e2c | -6.95546 | -42.43874 | 2025-09-20 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f43e587-735a-3a41-818e-36c7b98447c6 | -5.10987 | -43.20881 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4fefb78d-c1bf-3e97-aa32-7fb3b0e297fa | -5.94932 | -35.61974 | 2025-09-20 03:34:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79cb99bf-c4d8-3000-9057-30d5057e2485 | -5.79123 | -43.65275 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18947947-34bf-38bc-892d-77b89e4de940 | -5.49284 | -42.6307 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 490310b7-ed3a-367d-99fc-46cf16aa5038 | -6.36377 | -43.47338 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b65ba74b-0587-30a2-a5c5-2bda58199f9f | -5.78429 | -42.78151 | 2025-09-20 03:34:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 373a9e65-9e92-3bfb-b7c2-9db5fadd32f1 | -5.95784 | -42.92447 | 2025-09-20 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| de0677fb-ca47-3f6c-be07-e50ff1712d88 | -5.78553 | -43.65167 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06cc3a35-48fa-39f4-bc69-7c6bb3f3aa26 | -6.09354 | -42.82924 | 2025-09-20 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94ebbee1-61a1-3a52-be01-a46007fdbc75 | -5.73325 | -42.58252 | 2025-09-20 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08b5be70-f452-3f24-9e02-e4dcc94525a0 | -4.91728 | -38.67848 | 2025-09-20 03:34:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b973036c-ea6a-34dd-b406-33fed5603c46 | -6.48348 | -39.69562 | 2025-09-20 03:34:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6fc7209a-f170-3316-a013-46b9c5200bfa | -5.19606 | -45.48847 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9f0aa75-0641-3890-8d46-8b18d74ad702 | -6.36445 | -43.46969 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f192fc39-3631-326e-8a9f-4bc160e15fa9 | -5.1043 | -43.20761 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 16619b00-66e8-3d1c-94b1-ea2102681028 | -4.19766 | -38.97442 | 2025-09-20 03:34:00 | NOAA-20 | GUARAMIRANGA | CEARÁ | Brasil | 2305100 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 483bca5c-e8fa-38cb-828e-3101b3f23a90 | -5.51643 | -43.86047 | 2025-09-20 03:34:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 705f07b3-d7c2-3f34-926d-70c852e77636 | -6.9612 | -42.43641 | 2025-09-20 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa9c9f3e-feb0-32c9-9f0b-57e3d34081d0 | -6.09416 | -42.82575 | 2025-09-20 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd5f52f8-3dff-35bc-a2e6-efaa42bff9a0 | -3.65172 | -41.11458 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fbec501e-d27c-3d14-a21b-06c5d630e29e | -5.73548 | -43.63477 | 2025-09-20 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bae3179-2bcd-3140-9dbd-eb4297fd42d0 | -3.502 | -40.4067 | 2025-09-20 03:34:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d50013ef-ec88-3fda-a820-ca2285b5b359 | -5.79328 | -43.64091 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37b35285-ab91-3537-8cfe-0b8d4f330ee9 | -6.48539 | -39.69394 | 2025-09-20 03:34:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 442ff181-ac67-3ea4-a996-e82c9741a960 | -4.91929 | -38.67861 | 2025-09-20 03:34:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 365e4c07-f05c-3e0f-9aea-f6eae6581d99 | -5.74348 | -42.58692 | 2025-09-20 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1714d2c9-ba3c-36a2-9559-f5064638bb58 | -5.08635 | -41.14395 | 2025-09-20 03:34:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fd612ce8-9a72-350c-893c-d3a3b16c2065 | -3.65671 | -41.11546 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14e31c52-8a65-3e56-beed-b4fd8c179d9b | -6.1982 | -41.22423 | 2025-09-20 03:34:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 55260a62-7c74-3637-98f4-e5517a2cf03b | -5.59499 | -44.09469 | 2025-09-20 03:34:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fddce25-c31c-37aa-8ac6-60aa624e10cd | -5.78743 | -43.64989 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27a2a9c3-bec2-3818-a727-e0107857790b | -5.73265 | -42.58598 | 2025-09-20 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d21656cf-b094-3a9c-a3fa-dca6308850ba | -5.7924 | -43.65495 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 619f3ae0-4ecb-31e9-bda5-9bc1f45a3f20 | -5.51515 | -43.21885 | 2025-09-20 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce83f27a-ee9b-3146-a822-401b9c293c6d | -5.11394 | -43.20469 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 683556f0-3b1a-3f1a-84ce-666476cee627 | -3.96471 | -38.51496 | 2025-09-20 03:34:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2962d92-892f-3296-9f2b-3160d37b517f | -5.79761 | -43.64988 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ab82d92-53bf-3e44-be09-e14bd7c353f3 | -6.17642 | -45.42979 | 2025-09-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f20559a-ceae-31c4-8c99-e1333ff7b5aa | -4.48165 | -38.53538 | 2025-09-20 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7b3c2f7d-9929-30f6-8424-2ecb09eb5b03 | -5.79598 | -43.63519 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca7f493d-c070-301b-a46e-43a69cf8f90b | -3.56566 | -38.89423 | 2025-09-20 03:34:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4abe0be6-5b4a-3a66-ba6b-8668f835bb1a | -5.79968 | -43.63795 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cac51712-0c5f-302a-ac22-79ec4658a12d | -4.98876 | -45.14768 | 2025-09-20 03:34:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94d0258b-f429-3618-9c47-ba99ef437d42 | -5.11052 | -43.20504 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e52fef9d-fe7b-335b-ba33-3c28e45b9fbf | -6.21316 | -42.6392 | 2025-09-20 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2514048e-4159-3067-94e5-b9a7261621aa | -6.33251 | -42.39125 | 2025-09-20 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 92c718b8-52d5-35b0-9831-5004f30fdff8 | -5.11327 | -43.20847 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aa6f3c0-0fe4-3f43-985e-d07885587dee | -5.55806 | -42.16262 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 244722b1-68c9-31df-9e24-7ce47743265a | -6.72383 | -44.15393 | 2025-09-20 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| beb6d68e-a3a1-39af-ac68-1636be610b40 | -5.05369 | -36.80947 | 2025-09-20 03:34:00 | NOAA-20 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de9671c2-c1df-3f42-9dad-f328a6ce3821 | -6.72962 | -44.15512 | 2025-09-20 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4da584d-ba32-36d3-a217-bbdcbb551d20 | -5.96633 | -35.57983 | 2025-09-20 03:34:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 375f0fef-7c13-3b68-8dab-547bb54904bb | -5.49343 | -42.62731 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27d1a159-95b3-3c65-bce1-b55cbb219803 | -6.35744 | -43.47643 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cb91500-f85d-3754-8a3b-0d6a22376073 | -5.78365 | -42.78516 | 2025-09-20 03:34:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b671e9c-61f4-3950-9d56-5f07667fe4c9 | -6.21256 | -42.64254 | 2025-09-20 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dc95f44-f5ad-38d5-a8c9-c91f73423656 | -6.48032 | -39.69745 | 2025-09-20 03:34:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2f680dc-932b-3cae-8b49-eec00adcc4c9 | -5.10495 | -43.20382 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c5849fe6-3abc-3fc2-9f92-2d9574d44079 | -4.35465 | -46.29454 | 2025-09-20 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da5700fe-872b-31d9-9f71-757da1f755f7 | -6.1837 | -45.42575 | 2025-09-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a8d0694-fd2f-3dec-b56b-39e88724217c | -6.33303 | -42.38824 | 2025-09-20 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34aa1fa4-3b62-366a-8ba7-e4eed913fb36 | -5.16673 | -45.42749 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ad28efe-b8f0-352c-9d77-f11cc1e61b64 | -6.32775 | -42.38773 | 2025-09-20 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60951bd4-944d-3600-99f1-a8c6ae3b1ac2 | -4.86913 | -46.82984 | 2025-09-20 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2468ae73-595f-390a-91fd-92d6cd1c7c95 | -7.00244 | -39.36551 | 2025-09-20 03:34:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a075b2c0-6006-3308-a177-fa3836096d22 | -7.08623 | -38.72339 | 2025-09-20 03:34:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86c8dbe0-66cb-34bd-bbeb-d870bf272dd3 | -6.96066 | -42.43953 | 2025-09-20 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 830cbdb5-ed7d-3f46-926b-2221befd293a | -6.13929 | -43.43995 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71edc581-de39-37e6-9cb6-3c6337451bf9 | -5.53141 | -43.87492 | 2025-09-20 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5c95b089-3f53-327d-8ec0-087db9ed12ad | -5.03407 | -45.57477 | 2025-09-20 03:34:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c9306d9-74fe-3321-93ca-ef7e67ca80ee | -5.54764 | -42.16092 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19d49896-9cce-3588-87b6-dd1061009903 | -6.48104 | -39.69329 | 2025-09-20 03:34:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1b1b48c-0c05-323c-aee1-e31da638ff40 | -4.06992 | -40.47493 | 2025-09-20 03:34:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65d33231-27db-36dc-85ce-e326b11a3fb5 | -5.1896 | -45.48729 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8873a0fd-4d5d-36d8-a5f0-edfee86abfb1 | -6.63164 | -38.54931 | 2025-09-20 03:34:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d3ab04f-0b2f-3ed6-bd98-cfcc42913647 | -3.81316 | -41.00961 | 2025-09-20 03:34:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3607d313-713b-376d-a5ce-c4ed5a625bc4 | -5.79383 | -43.6471 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README7.md)
