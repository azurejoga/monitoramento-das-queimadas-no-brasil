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

## Dados Diários - Página 274

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0459d318-a91e-3052-8ee3-6f15a03ee6cf | -6.66029 | -41.70996 | 2026-10-09 16:01:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f2faca90-7c25-3d0f-b35e-40a2fe07d15e | -9.91429 | -45.71078 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2cd23f96-1479-3e9d-878e-a40cd0de0f79 | -11.26247 | -46.26467 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8e26f411-3a22-3cf6-bf73-45fff6504bfd | -9.86581 | -44.87203 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 355e797e-6d29-3639-b6ac-0dddaeaab6c2 | -9.86638 | -44.87664 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e4ab4b5e-ee3d-36d7-9b59-5d653b85b07e | -11.05355 | -44.05743 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a2814dc6-5cf6-35d7-8b78-db6044980a53 | -10.92102 | -45.37972 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 8da995e3-86dd-3af4-9ef4-d207f926ed7c | -6.77773 | -43.77788 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaf320ea-7dc7-3765-914b-465531914eb2 | -7.49165 | -42.83757 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 751bcb5f-456d-3432-9e00-6172e238ff08 | -9.92817 | -43.57103 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 112d9af8-b221-3964-9236-0ca6da50b9f4 | -8.93558 | -45.13972 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 90b1579b-a225-352f-913b-074eef10e35d | -5.08216 | -43.06031 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a708aa45-5a41-39a1-97a8-2611f7a03883 | -10.88016 | -45.5284 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 061312a2-adfe-365c-be8e-79c5be5bf2dc | -6.01174 | -40.98154 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 35b38db5-c31f-30d8-8a14-9e3ec281e777 | -10.53342 | -47.31564 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4fd6edf2-044a-3a9c-afab-8f1e31c29d7f | -7.04171 | -41.54692 | 2026-10-09 16:01:00 | NPP-375 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2e95f374-5e97-3f74-a891-33a50ad957ca | -7.00827 | -47.68449 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 42355124-95c1-339a-9396-03a2809cd82c | -7.07623 | -43.50183 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62bbc53e-62ab-3bf2-972a-9cf05abb77e5 | -8.53298 | -46.88784 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7b6f2f55-097a-3738-b958-7deff796ba06 | -9.13044 | -45.82215 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 49474c03-e054-3f8b-bd2a-2ca6b6dd6017 | -5.52367 | -44.11348 | 2026-10-09 16:01:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 46d9bb81-418d-3a69-a28a-c08085a5a3a6 | -6.132 | -36.61094 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9a3b6b76-3581-3b54-9552-a3ba612d9c98 | -5.97369 | -42.84683 | 2026-10-09 16:01:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b0abb922-7866-383a-ba84-09a614340ecc | -10.46408 | -47.1938 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 2259d147-3407-3ab7-bbcf-e751abb544cc | -10.88389 | -45.5189 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0cdbdce0-dd41-3a68-b441-d9f7a71a120e | -7.46184 | -42.81036 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1e572abc-2e82-3699-af7c-f83977de5de0 | -11.05253 | -44.04905 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| af305fa7-6f93-30a9-8729-e44764140d01 | -8.90674 | -45.20497 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cbd009c6-e0ed-3807-a5b2-087bfd5b3c2d | -7.02429 | -45.31417 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2115ece-8ee2-35b5-91c9-b94d6e617d98 | -10.48462 | -47.2041 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4c10646d-ca15-3391-8202-e902a81f050d | -8.39548 | -39.56184 | 2026-10-09 16:01:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5e8cceba-b344-312a-a30c-4be66e63ce7a | -4.98921 | -43.16058 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7fd9b3f7-a651-3c88-916b-352fd5df792b | -7.07718 | -43.50871 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4f113ca2-eed3-3802-b3e2-44483472e26a | -11.20831 | -45.2509 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7e107c07-3121-3079-a0cc-a4be529ff0f7 | -10.83461 | -47.33782 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4b8f2e19-4ed5-346d-b0f5-e265e9edbb77 | -10.47648 | -47.258 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7c7a6d9a-3631-3a83-ba2e-4570f9fbd1f7 | -4.54408 | -40.71054 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4cb32873-b443-3ff4-9001-e70886770e2d | -5.52468 | -43.05648 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eb32d432-47a6-3460-88af-f9bdbe6a5d9e | -5.75586 | -42.08862 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| ec31f0dd-f9c9-343b-a59c-95ad38ab5982 | -9.72119 | -45.54236 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09760f4c-6dac-3ebe-be15-a5fc1c83a5b4 | -11.04283 | -44.06725 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8ea9686e-1c60-352c-a15c-549757e67865 | -11.07402 | -44.12791 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 5f22a64b-8b1f-3591-a5f3-aa9946fefc76 | -6.19855 | -37.9065 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 2704d676-0bbe-3181-beab-c2818b36a49c | -5.75852 | -41.63678 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 6e2f9db8-5b4a-31a0-8924-b87953b19cc7 | -8.96516 | -45.12358 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d0a8fcc-6db7-3db0-bfc6-06df6d08e322 | -11.28158 | -45.1929 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c9a3feb-8189-33a1-aa26-3bee916fdae4 | -9.90411 | -44.78329 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44b3c6b6-74c5-3855-a0bf-98e4c3385adf | -11.05865 | -44.09962 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 4a729161-61f0-3c0f-8012-30628158ea01 | -6.88422 | -45.03318 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 811e9a20-7e5e-3e2b-a7f8-8acb3b58a099 | -9.10349 | -45.13956 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bcd06967-d378-3405-8595-a798f4cb1872 | -5.3331 | -40.8997 | 2026-10-09 16:01:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ec00931-e909-3933-b30f-f094e81135a7 | -10.66817 | -44.12375 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dae6065-b275-33fc-ab4b-5a2f053c99ec | -6.07946 | -43.99793 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0c1dd271-8b01-3ff7-be15-6db6d55111ce | -8.94108 | -45.13439 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6be3a821-b5fc-36ab-94d4-4b79f91046a7 | -7.48054 | -42.83283 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 83ccd163-f7f4-3a14-88e4-2189d6b2ef43 | -7.39943 | -44.74997 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 03052cc9-b6a6-3d47-863d-8cc219363214 | -5.60843 | -44.12325 | 2026-10-09 16:01:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9beaebf8-6382-3de1-81c9-708855306514 | -5.95553 | -40.93134 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 70ac422e-199a-3b5a-bf9e-79e3aa342939 | -9.4135 | -45.97668 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e2163f38-5a0c-333e-bf34-e7f10731e449 | -7.12812 | -41.81373 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| dd96fa26-12ca-3331-ac98-6322df1c44fb | -8.0865 | -45.64427 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e1d3c2e3-65ba-3ada-aa6b-b285c11aa0e2 | -10.4704 | -47.24628 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e09dfc73-57fa-34ec-a7db-b5445cc2555c | -6.57491 | -38.84402 | 2026-10-09 16:01:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b2405dbd-c7a0-3f8d-af80-b592a4f6bbd9 | -5.94084 | -43.58069 | 2026-10-09 16:01:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa62846c-3bad-370c-aea3-9641037d04cd | -6.93664 | -43.6641 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 88a989e4-040b-3034-b694-883e2db9c458 | -11.27115 | -45.18682 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ba8c8b0-ee79-3f08-9722-ecdae33c9c66 | -8.23233 | -46.42026 | 2026-10-09 16:01:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2eeef282-2794-37c7-8a3e-5f45760a1f2b | -5.71504 | -41.62845 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1c5415be-2592-3a1b-9e4c-78f597c75512 | -7.68773 | -45.44566 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| bfd0d35e-9f60-3016-bdcb-ef88f004c2b8 | -9.97104 | -43.55075 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 156feb19-2968-36c1-a343-3d7dbcbc5c58 | -7.4129 | -44.76525 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 16b4f307-192c-33ef-b99d-5609ff9af598 | -11.23521 | -45.31512 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 90144a63-c6b0-32e0-996a-f11b4c30492b | -7.5076 | -45.30292 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9c938485-45d2-37a1-a63d-380122450e9c | -8.48395 | -35.41066 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f01698d5-70c3-35ff-9d04-c1ef601bd11c | -8.93066 | -45.14959 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1fab8bdb-9a3f-34ee-ac96-40880d69a2eb | -7.48218 | -42.84496 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| dfd7f303-9862-338a-8e17-2aed2cf71478 | -7.41131 | -44.75312 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 000bd046-60e7-3b00-a627-329531d8174f | -6.07989 | -44.00094 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a4e9dfc1-b3b7-35e6-abb7-d465e3c3f5f3 | -6.73433 | -43.06664 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a5252879-3096-31f3-907c-8fc708701317 | -6.59385 | -37.88794 | 2026-10-09 16:01:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 2288be38-1c22-3c81-b35f-909819773966 | -6.48135 | -42.6972 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 69398e35-7111-3431-b62b-79c564b7b2b3 | -10.87815 | -45.5252 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2174f25c-850a-3f9e-9e87-4f793e1e0390 | -6.48216 | -42.7031 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 2d7b1f06-2db9-33f7-a388-a32f81dc314a | -7.07765 | -43.51214 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d339527a-3e65-306a-a4e7-ca6ba66bb79b | -11.0989 | -45.65999 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e5d15b0f-315a-3203-848d-09f808ecd50e | -5.24021 | -40.59312 | 2026-10-09 16:01:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ae3c9b48-d88d-329a-b8e0-57c7e79d36d4 | -10.63484 | -40.03721 | 2026-10-09 16:01:00 | NPP-375 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 73c5b48e-2dc1-3e5d-8741-e81a6bc53043 | -8.99112 | -36.45596 | 2026-10-09 16:01:00 | NPP-375 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fed811d-726c-3343-9e44-8e99fb78b701 | -10.89187 | -45.53086 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3305e746-7293-3f0b-960f-2b22243f070c | -10.917 | -45.40014 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 85e9923c-81de-3f74-bfb3-8ae4e07f19bf | -11.15291 | -47.3126 | 2026-10-09 16:01:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4395f120-bd16-3697-b05c-ecd79093cb17 | -11.1186 | -44.01214 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ebea788a-81ed-3165-8a45-8b5fcec46d0d | -11.11497 | -45.68554 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c68b2461-3a06-3a8d-9199-4c76197bea1e | -6.99697 | -47.69365 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 6be4e7d4-7b29-3ad8-b1d0-4f274e498ade | -10.42759 | -47.30883 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 142fbbe6-4cdf-3b9b-b954-c186f7e6abad | -7.42895 | -35.09371 | 2026-10-09 16:01:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 276ca7dc-b475-3929-a50b-a3dda4bd5e2f | -7.0162 | -47.67847 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fed96b96-08f4-3b69-8be2-18bcd65d35bc | -7.28787 | -40.42241 | 2026-10-09 16:01:00 | NPP-375 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 55e2aa60-cc6a-3ad6-8085-08ab9fd0c7af | -9.02154 | -45.94041 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 410932ab-81e3-3ed4-a94c-30a107cf7484 | -7.49125 | -42.83458 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |


[Clique aqui para ver as próximas entradas](README275.md)
