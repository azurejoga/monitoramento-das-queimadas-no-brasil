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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e17a26e1-7cce-309d-ac17-c375d6031b9f | -21.217 | -44.03016 | 2025-09-08 03:17:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b863da44-b36a-39f9-bfd0-23d581847694 | -21.2184 | -44.02421 | 2025-09-08 03:17:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| affe27cf-9c4d-381c-88ad-0c6f18475d19 | -14.2575 | -58.3484 | 2025-09-08 03:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 9f59c905-ed8a-37df-8009-3766e9a65fc3 | -14.2578 | -58.3284 | 2025-09-08 03:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7463e9bb-c4cc-3975-82c1-599e71251ff3 | -11.3935 | -50.3976 | 2025-09-08 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6f21e739-0e9a-35cb-b45b-ab34bba04735 | -11.4125 | -50.3955 | 2025-09-08 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 35b57350-94a9-3177-95c5-e5e6e32e43c6 | -11.3385 | -46.5645 | 2025-09-08 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 2e9c4139-72fe-3b87-8418-edbea1013913 | -7.3983 | -61.6346 | 2025-09-08 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 94c0ad77-89bd-3220-b477-011da3e5cf75 | -7.3984 | -61.6156 | 2025-09-08 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9f1404f4-797b-3925-8f0c-644f70aa05ad | -11.3938 | -50.3762 | 2025-09-08 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 45b47f2c-0eb1-3c99-94d9-2572ba1a897b | -12.6153 | -56.9742 | 2025-09-08 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 1ade9e0c-0776-3423-94fb-73c2c3b8655a | -12.6343 | -56.9725 | 2025-09-08 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 9bc588bb-c4b9-3e6a-a98c-d626e50b735b | -14.5266 | -48.7833 | 2025-09-08 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| d8a731c6-51f0-3c09-afca-98c2b3482114 | -12.9477 | -54.793 | 2025-09-08 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b0ee7dee-c68e-3549-a8bb-2405c8ff18d3 | -14.2383 | -58.3502 | 2025-09-08 03:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| fc151fe2-6ef8-30b8-9437-a8f75ee01aed | -14.2386 | -58.3302 | 2025-09-08 03:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 6ecf4a88-9cfd-38e6-9403-e094ee6891a1 | -14.5067 | -48.8085 | 2025-09-08 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| fba74d24-af2f-35e8-98b8-98d4a965be39 | -11.2007 | -54.9992 | 2025-09-08 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| fb365875-32f9-3359-a1a0-480f9f38519e | -11.4128 | -50.374 | 2025-09-08 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c1f2d94c-1bb3-3e75-a106-2098511e0828 | -7.4168 | -61.6339 | 2025-09-08 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ff967a15-217b-3862-a3d4-e739bd6c9e6f | -11.3932 | -50.419 | 2025-09-08 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 541077df-0c8c-373a-b71e-1476cf1363f8 | -11.3742 | -50.4212 | 2025-09-08 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1f873aa7-8a6d-3f2f-8674-80eef871a908 | -14.5067 | -48.8085 | 2025-09-08 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1e5b0c13-591e-3920-a841-1a72d0f5e353 | -7.3984 | -61.6156 | 2025-09-08 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 952e1262-a882-3668-b595-64bb95cae95b | -11.4125 | -50.3955 | 2025-09-08 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c6260ada-33de-3927-8c3e-928657523bfd | -11.4128 | -50.374 | 2025-09-08 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d771a73b-a34f-301b-8927-4602941bc7af | -11.3932 | -50.419 | 2025-09-08 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 4bbb20a3-c666-3851-8a03-e12c33ad5988 | -11.3742 | -50.4212 | 2025-09-08 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 351be5fd-01d2-3bab-b4a2-9e113baf6273 | -14.2386 | -58.3302 | 2025-09-08 03:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 14bcc17f-c98e-3360-ae3a-9ae8cfeaaed6 | -11.2827 | -46.4817 | 2025-09-08 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 402af1d9-3895-3cc4-ae48-fe1020434e27 | -11.2007 | -54.9992 | 2025-09-08 03:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2702f287-82e9-3222-9106-6c17428d59c8 | -11.3022 | -46.4566 | 2025-09-08 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d8800077-73ed-3640-a8b5-13a30046bb8d | -11.2834 | -46.4365 | 2025-09-08 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| a60bba88-c587-368f-8eb1-84f311a2443a | -7.3983 | -61.6346 | 2025-09-08 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 13e593ef-c9e5-3d14-b36d-88455020080d | -14.2578 | -58.3284 | 2025-09-08 03:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 96a86c9b-7adb-3b6c-ac4d-d27bfab7c092 | -11.2831 | -46.4591 | 2025-09-08 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.9 |
| c1f4b438-ee03-3904-b35a-8ac71de56383 | -11.3935 | -50.3976 | 2025-09-08 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 35a0ddf2-f736-3fe3-86fa-7fdb135291bb | -14.2383 | -58.3502 | 2025-09-08 03:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 168.1 |
| ae80021d-f797-36dc-857e-c44c77eda5fc | -7.4168 | -61.6339 | 2025-09-08 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5b0beb44-0ae3-34a4-926a-c49206935359 | -14.2575 | -58.3484 | 2025-09-08 03:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 0725e9a9-bd1d-3f26-a7bb-8eaf7cc06268 | -12.6343 | -56.9725 | 2025-09-08 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1e8debb3-6164-356c-9929-0758cbf5f515 | -12.6153 | -56.9742 | 2025-09-08 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| eb16b03e-dc6a-3dbd-b80d-a7da7c0743fa | -5.86517 | -43.84617 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68b74d0a-582d-3ada-b2c2-793be6a9d2e1 | -7.0823 | -43.89951 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8c1ceb9-af23-39e2-ae0c-c47ed3a3cdcd | -7.84323 | -44.86028 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4455628-5159-3414-9a22-49acdf8458ee | -7.62123 | -44.66701 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cc987f7-b763-3ab9-b392-51adcbdc8d63 | -6.87561 | -44.25678 | 2025-09-08 03:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9adb7895-a4f1-3936-9489-093f2cd71444 | -7.74081 | -44.73161 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8adc74e3-157c-3eb7-892f-8f226191f4b7 | -4.94105 | -37.96385 | 2025-09-08 03:38:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e00434a-e664-33d4-92a0-271b7a73e4be | -8.61921 | -40.19547 | 2025-09-08 03:38:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff5b6e3f-e781-3299-8714-6dbfa83fe184 | -4.55775 | -40.34078 | 2025-09-08 03:38:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e3a44a2-da5e-34f2-8792-06bd8e4a3a17 | -5.64439 | -43.91511 | 2025-09-08 03:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 302f4d99-dfb3-3202-b0a4-97f9a8a81844 | -5.85195 | -43.85955 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c87c8ab-a3e9-320e-923b-a43ea291e705 | -8.62355 | -40.19625 | 2025-09-08 03:38:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8748d21a-a72f-3154-a86d-62c869b40e18 | -6.13292 | -44.24012 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbc5ee73-b060-30c8-895a-461a8bf730dc | -5.85998 | -43.84792 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 55d23d5a-99a9-3517-938a-ccef10997167 | -4.67479 | -41.01361 | 2025-09-08 03:38:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0475af78-2bfc-33f6-a30d-e6c8976bece9 | -6.2454 | -44.82762 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02c01e2c-bac4-3731-8623-f6a3fed202b0 | -6.94302 | -43.35834 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 265ea388-86b6-375c-b16d-5ecfd98a2b2a | -5.94059 | -42.96424 | 2025-09-08 03:38:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18db6536-7c87-3589-b344-9ed7dfa78730 | -7.1112 | -44.1352 | 2025-09-08 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aec9a478-a512-3e3c-b4df-db4c661141b0 | -7.98176 | -44.83327 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5df22fb-3c0b-313a-abe4-3bccc1f2fedc | -6.31207 | -42.20478 | 2025-09-08 03:38:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7712d7b2-e10c-3ba7-a490-a1798adb4166 | -6.92437 | -44.34325 | 2025-09-08 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68a0911e-1444-3e2d-b3d8-384ffeb4f984 | -6.19969 | -40.96967 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b4c8b39-3226-3fd3-b0df-b465e90160bd | -7.59687 | -37.80418 | 2025-09-08 03:38:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47510b00-8f6d-3822-aae5-658933cd7cab | -8.29989 | -45.38377 | 2025-09-08 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93224f00-a6f8-331e-9198-6ceede861c6a | -6.49601 | -43.97762 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 770c8f4c-3ad5-37ab-a034-c84ea34a7602 | -8.14005 | -44.86822 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13c69b92-c3b3-3bbb-9bf3-8d4fb2b2ce61 | -7.57103 | -44.67237 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 727039d0-9a45-3446-a427-f1c9631d421a | -5.43799 | -42.80213 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a77d500-bfbf-39e3-b445-b2f04dd50ecb | -5.88502 | -43.96936 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1276489c-6ee1-3391-83b1-db762fe78129 | -5.44958 | -42.80029 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be53353f-7143-32e6-88bf-61f80daa2ee4 | -6.37847 | -39.25147 | 2025-09-08 03:38:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08eff4c2-c831-300b-a246-55df61aacadd | -7.24386 | -44.83663 | 2025-09-08 03:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c0b72a7-7bb7-3e8d-b129-50974055a3ad | -5.07977 | -42.42137 | 2025-09-08 03:38:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ad20e6a-4ab0-3f2a-aade-2d30ee34ba03 | -7.57601 | -44.00181 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd3afcb6-71e6-3ae7-a8d7-266869971866 | -5.64051 | -43.91433 | 2025-09-08 03:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ae78259-74ff-31b9-8a42-923373fa3935 | -6.20411 | -42.64357 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0b74d15-3851-335c-8f58-3d3000a11c00 | -5.43189 | -42.80476 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af95ad14-baa3-3138-ba26-bfeab2dc406a | -6.29746 | -43.82682 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cc5c9ab-ed9f-3500-a3ff-66d14993efe2 | -2.82693 | -41.73808 | 2025-09-08 03:38:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 207de7c7-cdb1-3439-b4bd-545426b605ff | -5.82116 | -44.12089 | 2025-09-08 03:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15c821b1-f924-3602-bba1-e7c03c731745 | -8.15314 | -44.85104 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18d6ec5a-c54f-3fef-a82e-2917c6c93bef | -6.38923 | -43.81118 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dd4c4fe-286b-31b7-aa53-2dae88f88905 | -7.08159 | -43.90338 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96929e53-1aff-31f9-891a-0ba762ed00dc | -7.09305 | -43.90531 | 2025-09-08 03:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c5dbb0b-0cc8-3b79-8e1b-5117fc68588f | -7.61592 | -44.66247 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32eba5aa-75bc-3d12-a4db-139af48adc1a | -5.87998 | -43.9638 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03c8671c-a8b4-3423-9360-63e50bf2e03f | -7.35371 | -43.94273 | 2025-09-08 03:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6335e1b6-71b0-3987-91dc-e3721c37ba1c | -7.88036 | -46.25546 | 2025-09-08 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d074db2-2b5b-3b8e-80a9-d383aa42726d | -7.54613 | -42.52247 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f2f83320-16dc-3be4-8975-fae4e22a2cc1 | -6.21574 | -43.31934 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14180eb4-1b7c-3bcc-a8a0-55874c56e265 | -5.85934 | -43.8453 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c56c1602-ceff-3f02-9035-fc71535ac8b3 | -6.31261 | -42.2017 | 2025-09-08 03:38:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3d89110-dd05-3136-9744-dabc624b919e | -8.19839 | -44.78783 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 322476fa-6673-33eb-957a-26aa1eb441b9 | -6.19622 | -42.64266 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2f62559-e9dd-3e08-bcb5-2f3c33841262 | -6.12656 | -44.25858 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2adda3b-bd78-348c-b021-308f5c5a77dd | -7.82706 | -45.4285 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c99596d5-23bb-316b-852f-d71e6e9fe70d | -5.76617 | -40.95531 | 2025-09-08 03:38:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
