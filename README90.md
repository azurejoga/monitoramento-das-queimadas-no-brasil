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
| 16710964-5b5d-371c-b006-b3306d5415c0 | -9.30622 | -46.93375 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ab11fa9-977a-35f1-9551-04b2fd0209d2 | -10.65453 | -45.28833 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55cac606-c943-39e4-9a33-cd043b6827f2 | -8.08631 | -45.43528 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ee17243b-05b1-3837-905e-d8c67ccf278b | -11.45155 | -44.20766 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72a76518-932c-3e68-863f-0acb799d63e3 | -11.4143 | -44.21323 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abe12f2b-2f8e-3fff-9ef1-5bbc38ead7e1 | -8.48833 | -49.04714 | 2025-10-17 04:51:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbb8b99c-1b30-3cc3-a1b8-6f8cf7a12b25 | -10.61565 | -45.23461 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3be157e3-bbf6-3173-9afb-c9c4f983d37c | -9.14948 | -46.64505 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10993be5-6c30-3099-a630-bdc979b3052b | -8.41662 | -46.28016 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b095de56-8412-315e-8723-1e74b7b223de | -10.50366 | -43.41742 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3594cc6-b5a7-3973-acaf-c1fb1ca3ceb4 | -9.34272 | -46.90737 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 379f3dbe-ee79-3a26-865c-620ee1049ff1 | -9.83932 | -47.54479 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be063a52-4993-37c2-969a-aa9a0026f79b | -11.18993 | -51.75814 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9aa990-a05a-384f-87b5-2cda371538a5 | -8.47502 | -50.10579 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b5cb64c-cfb3-3fb7-9afb-0dccb006774a | -9.15882 | -46.60954 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4093684-283b-337a-af13-cbcdaf756ee5 | -8.81748 | -47.30357 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af9185dd-59c2-34f7-8603-39fc62d76c63 | -8.94052 | -45.24506 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50de65d6-1bc0-3d6d-8179-26faadc353f7 | -9.13323 | -46.64292 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1d2dba9-dc35-3ed0-b48e-360121eccb3d | -9.21169 | -61.54474 | 2025-10-17 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 680cfaa6-8fcc-30b2-9b44-409ddfe91e57 | -9.26936 | -45.27835 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97800922-03b1-3b20-b59c-3381665a5494 | -10.53091 | -43.36954 | 2025-10-17 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f7229dd-43fb-3a68-9c5e-dc9a2c7dd612 | -9.64835 | -47.67376 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5e83e46-2325-3c0c-91a6-2faf1c055d09 | -8.7887 | -46.68233 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de31f654-d57a-361f-8495-caede1c67f3d | -10.27879 | -44.04182 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87d36dbd-11d0-3fd9-8fcf-fafc6d642099 | -8.07628 | -45.4124 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 737ee01c-e50f-3027-8dea-d241d03bdab6 | -13.41514 | -48.58126 | 2025-10-17 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de797459-168a-38d0-9966-99bc8aa34730 | -12.04902 | -54.24406 | 2025-10-17 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5daf2aa-1d2b-3ecb-80b2-bd79f0b54696 | -10.59287 | -47.40268 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fa7ff7d-d492-31d1-b507-c65c86e171a1 | -9.33943 | -46.91387 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 219bf194-23e4-3ccd-843f-16c2a7ed39ac | -10.26251 | -44.05096 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7500b12f-da37-30cd-a9bb-8b2ca2238bd6 | -10.2943 | -44.03842 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| cbee67e7-90fc-325c-b3d2-da430782a0be | -14.93513 | -46.71486 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b73468cf-bb2c-3e57-b863-f08f4f8f0678 | -13.43206 | -47.9659 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1930903a-7dfb-312e-901b-1c80509e1f1b | -14.34085 | -51.44157 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8bc0048-9b5a-358f-a49b-6e757d60232c | -14.67174 | -47.40568 | 2025-10-17 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 182c4228-d611-3444-a017-01d4ca67331b | -11.18939 | -49.80201 | 2025-10-17 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1183f01-e714-3280-acce-6c4b3ed55f53 | -11.43712 | -54.09731 | 2025-10-17 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a93f40d-5bfc-3283-98fc-a63a83edddbf | -14.35782 | -51.4671 | 2025-10-17 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4660a048-e5e3-3862-91fb-b9e178a39d48 | -9.98261 | -47.0134 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4e3de7ce-e566-35cb-83fc-2e6dfb6811d7 | -8.37551 | -46.24457 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a06410e-72c8-3189-9e3f-295c0f08eb63 | -10.10475 | -44.62897 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db9b32f5-2354-30f4-ab5b-49f9b27bdcf6 | -10.29506 | -44.0329 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 59d1cd40-29c4-3ef0-966c-140ab7cd5401 | -12.16741 | -45.07919 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba10df02-ff46-3b9d-83ea-6073aa16d9f1 | -11.97294 | -46.55169 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc5ee722-4550-38dd-9fd7-2def3a1d32f2 | -11.40712 | -44.22939 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58b8b564-d9a5-3ebd-9184-53aca94c4412 | -11.50045 | -44.06379 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6255e114-7c1c-31fc-b61b-2dff0e92d15e | -9.88765 | -49.1205 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 970471cc-c267-3a7f-9403-1b3c76f659ee | -11.59052 | -44.07038 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bb9018a9-6b48-3c66-acbd-e9e72e8815c1 | -11.57512 | -48.56989 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 51a2adb2-4068-347b-95fb-9b5439f4e447 | -13.1992 | -48.32032 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 694d98de-0078-3a97-8f66-0c85e2e76d1b | -10.9942 | -49.54464 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d5bffaf-2a5c-37b8-b472-c272f09fb68e | -9.98334 | -47.00817 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b84a437-03d4-397d-ba9d-258fb23479eb | -11.35171 | -45.26337 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 401c6f01-cb5b-3a89-bc92-b80003b99d32 | -9.27111 | -45.26552 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 989f3c61-e59e-34cd-af72-1270917dd5ed | -11.4562 | -44.0512 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70f95bef-be8b-3916-9991-ca0324a90dc1 | -8.73162 | -43.87101 | 2025-10-17 04:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd135276-81ad-3821-b35f-e44d00a8d6b0 | -8.37493 | -46.30786 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60e3db09-503e-3f98-8319-391a6863fd1f | -10.05373 | -43.82999 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5229d589-ec74-3536-8fb0-20e578d7b8ea | -11.39452 | -44.21059 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7662602-c307-3caa-aaec-48c3f8ca6dbd | -13.41182 | -44.06396 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5dcad6c4-4018-3c2a-80f6-30883826d6b3 | -8.59872 | -44.93842 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31e4ee1a-c372-35ee-b99d-00af9c3d8b0c | -10.13695 | -44.57987 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09f96a28-de21-38df-a837-9e1661739f41 | -14.32672 | -51.44312 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6bb5e648-0c6d-3dad-8128-9c00658b583b | -9.34994 | -46.91374 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d87b61bf-ce22-36f9-8bc7-399fded97850 | -7.71758 | -47.84642 | 2025-10-17 04:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2018547-d0f8-3e65-b2da-9528969cd8f7 | -10.5092 | -43.41518 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40a7762c-2d4b-3705-bec9-59b768da7df8 | -9.09147 | -49.79161 | 2025-10-17 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b4b784-1420-3db1-b59f-5aba9c832cd3 | -14.23314 | -54.90525 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88d6d554-52f8-33a4-a6e4-5b398ff7173c | -9.72827 | -62.95324 | 2025-10-17 04:51:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6713ba1c-0c08-3a40-9a5a-55efbb8ec2df | -12.17019 | -45.07133 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3f4c9b0-019b-3840-9d71-49a049e7c4c2 | -11.46197 | -44.04613 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62a604ef-b35f-3cd0-96e7-1eabca50a0c0 | -11.40935 | -44.21256 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23290c0b-f5d0-38ef-bd9f-46093525c0b9 | -10.92645 | -45.41248 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 529399f2-6231-3ec6-ad0f-3d05e639e324 | -9.88045 | -47.68144 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cbcee95-3a62-335c-8a44-41effdd34bb8 | -8.08686 | -45.4314 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b5582aa-51c4-38c4-a346-0124859faeaf | -13.01928 | -43.83991 | 2025-10-17 04:51:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17d52aef-f4ae-39bf-b88c-233bf278e21e | -11.97136 | -46.56355 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f897490c-eb96-34f2-bc5d-cfdd27b9677a | -10.49782 | -43.42202 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90198afc-6130-363f-a032-a72ca571102a | -14.33182 | -51.45534 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df04150b-66c6-3cd2-8a59-1c805d9e96f8 | -11.75826 | -61.07209 | 2025-10-17 04:51:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8d56ffe-16ef-34ee-9a49-869732b2f1da | -7.2371 | -60.64632 | 2025-10-17 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf76d3b6-8100-3303-84ad-1aa9fc32c557 | -8.36565 | -44.77397 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19f47b0b-2d44-30da-99a7-d4263efbb9bd | -13.42556 | -47.95445 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1e79c92-f9cd-3cca-b367-50b4ff74a7a0 | -13.43995 | -47.9672 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3bcd39a0-bfb0-3870-9215-4fe3ef0f1752 | -13.57815 | -48.48936 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 149d01e1-155f-3ef9-9af6-3442a0e4f289 | -10.49885 | -43.41411 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9bb15a3-44c5-35de-8185-4b22fec19b64 | -14.9158 | -46.76 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b15998df-d5be-3dbc-be19-04344c4a86f6 | -12.04681 | -51.37228 | 2025-10-17 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5285a773-649e-3e03-9211-1258a273ff98 | -10.81135 | -43.93592 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c145f2b5-25db-3568-a8e2-f835ac76c82a | -8.27453 | -48.00557 | 2025-10-17 04:51:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9093c0cd-95f3-321d-b418-a4cde1f7df34 | -8.82451 | -47.30956 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d95abf00-79c4-35e1-a871-0d1be5ddc4b2 | -8.69729 | -46.9849 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93b90835-8425-30c6-b9da-b99a0aa32465 | -12.4534 | -51.33253 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8bf56e5-55cb-318c-9694-06d1f0733675 | -10.52616 | -43.36563 | 2025-10-17 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e024624f-69c4-3889-869a-f16ffaec87cd | -10.11951 | -44.60225 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef35a368-1b44-3d57-bb20-a3fe1b18c962 | -10.27617 | -44.02435 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4069e5fc-92d8-3855-ab3c-eb88a260d215 | -14.33691 | -51.46756 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97a9060f-4fa2-33b1-8606-4f05d3cce905 | -11.57698 | -44.05679 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c90067da-4535-3ce8-8cd2-38e184ef6dad | -11.39799 | -44.22243 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 489acdfe-478c-3124-abe0-6e23b7eb04b5 | -10.5085 | -43.42054 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README91.md)
