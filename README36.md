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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecdedb1e-c5c0-351d-be5c-ddd4fbe2d9aa | -6.42953 | -42.92015 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18afbd0c-4dae-361e-ae40-e9c46dba0352 | -5.81795 | -42.80172 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a77aea6b-c59e-37bc-b9fa-6fd3b385f34c | -5.8166 | -42.80994 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4590d63a-df79-3da0-9a32-19f7382816d1 | -8.67568 | -43.98663 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa173314-f8ec-356c-b76f-e8287c30c78e | -5.35696 | -45.04193 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee429586-6608-3877-9f59-e10908b9a237 | -5.42146 | -41.32502 | 2025-09-28 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c63aafb2-f75d-33c4-b199-3fd566142f86 | -10.00934 | -46.70108 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61650138-577d-3b8c-b3b5-a3d080365207 | -5.33936 | -45.64052 | 2025-09-28 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0edc492-bb72-3e5d-839e-f415b07af6e0 | -9.44693 | -43.70275 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9866838d-f410-3038-80e3-4882a4dff798 | -5.04842 | -45.31322 | 2025-09-28 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e599797b-6e66-3ea3-85f1-dc60548b3fe6 | -5.81856 | -44.44741 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e577641-64fa-36f2-be24-849ddfe08f49 | -6.21714 | -42.85044 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 08a8f76f-756b-334b-9a40-75b2174dda54 | -6.32352 | -41.88339 | 2025-09-28 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c551b23a-0d05-3c58-ac63-570737277de2 | -5.74827 | -42.81292 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e7fa365c-0df3-386b-9d28-e5d192d905f6 | -7.74705 | -47.00644 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0970507-e600-3cfb-8010-614bc3aaaf6c | -5.94593 | -42.90628 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e2fe4042-a8b5-3024-a52c-7c6a93c72c57 | -9.28797 | -45.71267 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3caf8e1-746f-3cbe-8f7f-596154a9c59a | -8.48059 | -47.80972 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af65b1c6-1c6e-308f-87b4-da88cb52494d | -6.45563 | -42.54202 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 69e6c9bc-59a3-3453-9e36-ca0926d3a60f | -5.74926 | -42.82975 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| db237145-e1e8-3cbb-993b-4845fc2e0cd3 | -7.36229 | -43.1256 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d2611a41-2621-3fca-a380-cad547ae2e56 | -5.76499 | -42.82383 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e01ebda2-3980-36f9-80a1-f8c0f51f83ca | -4.85654 | -45.75791 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4341544-a951-375f-b892-04249b34f5b5 | -7.59823 | -43.05354 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30d22071-57ea-3b68-bcb1-eae07106d6c5 | -5.81727 | -42.80585 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f6160c4a-16a2-3cd9-a1e4-abc93702e332 | -6.38311 | -38.30446 | 2025-09-28 04:04:00 | NPP-375D | MAJOR SALES | RIO GRANDE DO NORTE | Brasil | 2407252 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 78adc188-e292-38e2-b462-81ac8b453bdc | -7.18695 | -41.70152 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8515f3f7-07e0-3e78-86e9-f1ec25c0b01e | -9.29051 | -45.69825 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63e60ede-ecd7-3c68-ade2-b7201355f2d7 | -5.75549 | -42.81401 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9eccc233-9928-3ba9-a307-d7ba0d400d42 | -5.9662 | -46.45127 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa224f8a-c676-3271-91d3-924d8fb37a22 | -3.74714 | -39.51439 | 2025-09-28 04:04:00 | NPP-375D | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2bedfb66-e44f-3349-ac50-3fda2bd6b580 | -9.29703 | -45.68481 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49f83892-1b07-322c-8629-d795afc09d49 | -7.16638 | -41.72077 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1fcbac7-34ae-3ce5-8bf5-6b462e0d66e2 | -8.81922 | -46.212 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16074b37-b67f-3f40-9bb6-652eaa161fb4 | -5.36108 | -45.04264 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5a7b591-c07b-3bb1-8aef-5ae08356b711 | -9.57118 | -45.44869 | 2025-09-28 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69673012-114f-3871-a8d7-ef8ed3407c6f | -7.18458 | -41.71621 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3bb14e03-ca20-3b16-b2b8-ed0f44f04b56 | -7.37787 | -47.02493 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d39dd89c-5274-38d8-8056-94e03372dc0d | -5.41136 | -42.28426 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 83788878-a6d5-309e-ab94-0554c7ee6a59 | -8.46488 | -44.60147 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f474692-848a-3679-a28e-375723b1c9e8 | -6.7633 | -44.59406 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a731a48e-a328-3db0-a75f-439fe527f607 | -7.03352 | -44.77898 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a985df1-1265-3e02-a9ab-eeaa27410cb3 | -6.05979 | -44.8617 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed48c900-3d4c-3965-b868-4db76946f474 | -3.29946 | -42.18104 | 2025-09-28 04:04:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54cc318f-d718-3f3a-87a4-e9eaaaefd9ae | -5.90447 | -43.68776 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ffc5cad1-962b-3b51-bd96-0e530829d82b | -7.03073 | -34.8892 | 2025-09-28 04:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d77fd7e7-81cf-3c96-bd6f-40469c1930cb | -6.08315 | -49.40214 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7efc3205-e175-300e-b486-2a2a7f7ae7de | -5.27502 | -44.73445 | 2025-09-28 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eaedd63c-d581-3d86-b587-378dd2eb27c6 | -2.58219 | -48.4058 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| df17bc49-c91a-3cc6-862b-098cbc0c8fac | -5.46087 | -41.07869 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 66d6cb79-64fa-39d1-a100-4e4026231495 | -6.09531 | -49.3972 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8dfa406-3f0a-3e5a-bf54-c6419036bfb4 | -5.51919 | -42.73146 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 06cc1e1a-f14b-36f9-8791-eae84fa65532 | -5.68672 | -42.32203 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4928b698-6782-3151-9953-e3f8ecd9bbca | -5.41551 | -42.28093 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54a4eeae-8532-33d3-acaa-2f645518d8c4 | -5.76078 | -42.83482 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d1eea7f4-ea3c-3ca7-aeb3-d7b341339f32 | -7.77882 | -47.01408 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44203293-6323-3233-b535-c374b9b939d5 | -2.58652 | -48.40737 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bfdf7dc9-8c65-3204-98b4-786037843136 | -4.86782 | -42.9562 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 231c75d3-6142-3036-8b6b-8dad9a0fff19 | -4.82776 | -45.82117 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b50ebe37-3a62-3134-80c7-056d7961cf06 | -6.31673 | -43.46486 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 425d1a7f-919c-365c-8ac0-77c3fa2a23ad | -6.32042 | -43.46552 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ed4e93a-b797-3d19-bb92-e0632983b593 | -6.91428 | -46.16293 | 2025-09-28 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7b333c8-3594-352b-8f68-16a5ce821a63 | -5.75719 | -42.83419 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a089d1ad-912b-3f4d-8ba4-ccb3658b04b2 | -5.69669 | -42.63278 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd98db9f-daad-343c-92eb-57bd9869a814 | -5.76042 | -42.88163 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| aed52cc9-0123-3e90-ac06-63733e31c200 | -5.72924 | -42.83918 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 52818aa5-13df-3677-9135-a5042335894c | -9.11841 | -46.67076 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cec8cc0a-8129-3a77-91ae-bb5db965bc69 | -6.46252 | -44.2142 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7026a5b7-ae9b-3684-b2ea-75a7b6ff6b68 | -4.78814 | -50.80868 | 2025-09-28 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0732878d-5a87-36a6-8169-249a39b3389d | -5.80039 | -42.84129 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 656b88ab-0e6a-3911-b070-22b0f9f4e6ee | -6.69046 | -44.57479 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17b62b9c-9d23-387f-92f9-ee0f272667fe | -7.71722 | -41.29125 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58b2201c-848d-3e52-bd32-468d9f2cd767 | -7.62812 | -43.80077 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48dff367-0156-380b-bdb8-ff6a09dd7e51 | -6.57718 | -45.10028 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bf1072e-9841-3ba8-a797-d2930530078c | -6.43557 | -43.51384 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7492abd0-c52d-3069-98db-4477ae945fdc | -7.30924 | -42.94724 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ecc535eb-906e-3e62-963e-d82725603b84 | -7.24959 | -44.75647 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2c84943-4489-3637-9fd8-48239c6a3ac4 | -8.16942 | -46.40049 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| df9b9ea4-1b5e-3b9e-bef8-dd5de474cd9a | -5.80894 | -42.83426 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dfffcb0b-411d-3657-8ae1-7b958a3ff436 | -7.75907 | -45.73824 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55efb959-37d4-3b5e-9ab2-b17cc1a072c5 | -6.48006 | -44.25195 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c23dbca2-9b32-38bd-92b4-422ef79f34cd | -7.87042 | -44.5682 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee8e3340-7606-3889-b403-5ca665c174d4 | -8.28338 | -45.45807 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 642e26c2-77e7-365c-a651-7d47cf99f802 | -6.61643 | -43.77276 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41bdd28f-633d-3092-b603-785660ed336a | -7.31876 | -45.98747 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bf791f9-9f98-312a-bc42-58f812a2c486 | -6.57536 | -43.74031 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45841198-67d2-3690-936c-f5d6d8beb3a2 | -6.70849 | -44.58747 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73f08d48-5a42-36e8-830d-9caed30e64a9 | -5.76761 | -42.79366 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d8b83197-f1af-35f0-b580-657aaca3eeef | -6.59231 | -44.93258 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73725d4d-60ef-3ddb-9d48-d2a42273f0b7 | -7.18296 | -41.70461 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 14370be4-d679-33f5-ab8d-e67f5a8ae65f | -6.98837 | -42.39259 | 2025-09-28 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c50dbd0-8e64-395a-a732-2e2739dc2957 | -2.47667 | -47.6589 | 2025-09-28 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4ed99ca-f004-387e-ae9b-1db5cbb8ab38 | -6.0366 | -43.58707 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f109b6f-9091-3e3e-8742-8ab7ade0ae49 | -5.86856 | -45.75384 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b965581c-1aa9-3828-8855-3c9c161d4cf5 | -9.29881 | -49.10264 | 2025-09-28 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3b3901c-9821-3dc6-9f96-02b42e32b5cb | -9.21664 | -46.77774 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bb200fe-aa90-345f-80ad-3c216d70ba6a | -5.76765 | -42.88276 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 29bf1d96-bd53-3e2d-a54b-68e34604cfc8 | -8.82409 | -46.20893 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4423fa1-ac10-3723-bc05-e2d5df29c665 | -7.25503 | -43.00924 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15911c57-ade7-305c-8a8c-874c90bcd566 | -4.82749 | -45.82278 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
