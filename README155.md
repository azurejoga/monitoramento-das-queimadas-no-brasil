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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce2a72aa-f650-30c6-b7a2-63ea5dba7698 | -15.043 | -41.3576 | 2026-10-10 12:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 158.6 |
| 0c09a1a0-17ac-3886-8903-1f83a82fb577 | -11.0144 | -45.4042 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 9a33ddf3-2c4b-35ac-a03f-c80210f2f9d0 | -11.0328 | -45.4475 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 2a261e56-9eb5-305d-8d78-a88493c0def6 | -10.9097 | -44.8206 | 2026-10-10 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| aa8ca0b5-2652-3d38-af48-4aa1d425ae83 | -8.9085 | -45.4114 | 2026-10-10 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 218475c5-7a93-3651-aecc-c611cf833b6a | -11.1873 | -45.3347 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 91d310b5-aeff-3bb8-88c7-6d3dcbcc7bef | -8.9275 | -45.4094 | 2026-10-10 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 14c806fa-05df-3739-abb2-ccbbd7529c4e | 2.727 | -60.2586 | 2026-10-10 12:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 2b58cafc-6c1a-3551-ba40-b97607c8124b | -11.0379 | -44.012 | 2026-10-10 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| b1d5d90b-ad91-3a00-92f7-c62ac32155b5 | -9.9384 | -44.8791 | 2026-10-10 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 473d78aa-f8a2-32bd-93c8-727997a7e8fa | -9.9398 | -44.7869 | 2026-10-10 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| c15c5448-07e6-38d2-9bd7-28ce994551d2 | -8.9272 | -45.4321 | 2026-10-10 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 866e4b7c-e92c-3c92-be32-ae6dcaf92b97 | -9.9211 | -44.7662 | 2026-10-10 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| b4301ec9-1716-3931-8b81-d222cefc5def | -11.1876 | -45.3117 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 685202c2-281c-30e5-8888-4839c81130fc | -11.0937 | -44.0975 | 2026-10-10 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 35624d58-af18-3c60-aee3-00a2961f5d7a | -11.2064 | -45.3321 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 557edd69-be63-3787-97db-332cc466a2a6 | -11.0332 | -45.4246 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 2c1ab44a-8dd6-3d50-8060-ac7b5392fc0e | -12.2273 | -43.9481 | 2026-10-10 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 06f99d9c-4bcf-3a84-adb7-9440ffdeb814 | -10.8905 | -44.8232 | 2026-10-10 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 13e46850-3f55-3e97-888b-78a9bec7b081 | -11.0374 | -44.0355 | 2026-10-10 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| b4d1c3c1-bbc8-3f39-8ac0-3163aa7992b5 | -9.1009 | -45.1622 | 2026-10-10 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 01cc8dfa-022c-384b-bdef-528df126136e | -10.8909 | -44.8001 | 2026-10-10 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 1183b81f-f29b-3402-88a9-424531676623 | -9.1108 | -45.82 | 2026-10-10 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a1331802-5d14-3185-8f2e-5942b944f9a8 | -9.1297 | -45.8179 | 2026-10-10 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 84910adb-c2f1-3782-8228-b29ab3a5dde1 | -12.208 | -43.9512 | 2026-10-10 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e89697f4-3a74-3268-81c7-af8b909e5521 | -9.1924 | -49.7678 | 2026-10-10 12:50:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 4457bf0e-6c4a-35f8-ad80-b0498d132853 | -11.2068 | -45.3091 | 2026-10-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 7ca4a8fe-f746-3598-b66b-835a0ba4e13c | -12.1627 | -45.3547 | 2026-10-10 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 0a60643c-bc28-3b5b-8cf4-96d2daa4ad9d | -13.3666 | -43.8979 | 2026-10-10 12:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| ecea7979-770b-3897-9f8b-ea641c5b69ec | -8.9879 | -45.1292 | 2026-10-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 774f92f9-40e9-34a7-8ddb-15c60bc8bb8c | 2.727 | -60.2586 | 2026-10-10 13:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 39d3c671-2fdd-3a78-a6ba-2d845c52a41c | -8.9085 | -45.4114 | 2026-10-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6018a705-eeb5-31bd-a5b7-a5dbf33abbea | -13.3666 | -43.8979 | 2026-10-10 13:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 4ad24ae7-a5f6-3b57-aed1-72fe979fc025 | -11.5793 | -43.6965 | 2026-10-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 1565c041-2b46-3b78-8c7f-de690e6dc2b8 | -11.2064 | -45.3321 | 2026-10-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 423e359a-fd7a-3c11-b230-ef05316ac00a | -11.3374 | -46.6322 | 2026-10-10 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 80cf549a-afb4-3fbd-8f97-1f3fb194b1a5 | -8.9775 | -45.9023 | 2026-10-10 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2455e2c1-df71-33db-8962-d219ecde6c22 | -11.8978 | -47.3642 | 2026-10-10 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f62fa817-8654-3fd0-81a1-124079edea40 | -11.1873 | -45.3347 | 2026-10-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 0b0cf444-016c-3ad1-be41-9e7e90527744 | -9.1924 | -49.7678 | 2026-10-10 13:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 6eeb9f71-675e-394b-bc2d-6a5c0d66496a | -12.1729 | -44.7983 | 2026-10-10 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| b0d031ad-034e-35b9-9eeb-6583a6516c7a | -15.0233 | -41.362 | 2026-10-10 13:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 136.0 |
| 10356c1b-e637-3bdf-9625-efe937823be1 | -8.9693 | -45.1084 | 2026-10-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 23bd7ec8-8fff-364f-a943-bddbd439e293 | -10.9388 | -45.3687 | 2026-10-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0f9c97fe-5a35-353e-8aa9-dd3d17f7db65 | -15.043 | -41.3576 | 2026-10-10 13:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 165.1 |
| 938c34de-0aab-32b6-9600-7403c1fc3421 | -9.9384 | -44.8791 | 2026-10-10 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| d367a398-cfef-34af-a68d-f085d8a64e73 | -9.9211 | -44.7662 | 2026-10-10 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 173.4 |
| a2fd2a72-7194-310a-ad04-064f134f9fe0 | -11.2068 | -45.3091 | 2026-10-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 9c69c3ba-5c0c-3943-8dae-3ab1850fe8b1 | -13.3865 | -43.8708 | 2026-10-10 13:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| bc22b6eb-1485-34a4-b5c4-dc1b3d58d21f | -11.3183 | -46.6347 | 2026-10-10 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ff4efbcb-f571-3a47-b586-13d22f4af657 | -11.1876 | -45.3117 | 2026-10-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 4fac28f9-35f0-354f-ac88-d386b94ecba3 | -11.8787 | -47.3668 | 2026-10-10 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ee99aefc-e1eb-344b-9cf8-8ff7246bd811 | -9.1108 | -45.82 | 2026-10-10 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b3cfc385-16fd-337a-8566-a6d9e91d7229 | -11.8595 | -47.3694 | 2026-10-10 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9fcd0fbb-45bb-3cac-9312-d3b989b75824 | -9.9208 | -44.7893 | 2026-10-10 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 176.8 |
| d8205ef0-d222-3711-93f0-bb1f84fc398e | -8.969 | -45.1313 | 2026-10-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 3d13b809-27e9-3a5a-995f-9abec840094c | -9.9398 | -44.7869 | 2026-10-10 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| a7f4059b-ebee-3bf0-8ed2-f0730fbc5b48 | -10.9097 | -44.8206 | 2026-10-10 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| c684578f-860a-302f-9660-750ad2e94967 | -12.0507 | -47.3658 | 2026-10-10 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4706b5a8-5a85-3843-bb8b-c50ef4d8908a | -10.8905 | -44.8232 | 2026-10-10 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 57675c77-f870-3b7a-8635-473181ad8bbe | -12.1733 | -44.775 | 2026-10-10 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 9c548d17-3c2f-35b3-ba4d-d356260ba240 | -11.7772 | -45.4806 | 2026-10-10 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 1456e2de-6d4d-309d-bf17-c17aef6f4354 | -8.969 | -45.1313 | 2026-10-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b9380587-d688-303e-8d00-fa55ba538939 | -11.5976 | -43.7408 | 2026-10-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bda3f94d-3241-3216-9d7c-4aa84ff24df6 | -11.8787 | -47.3668 | 2026-10-10 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| f294d37b-69e4-3d26-92c3-239e18ee245d | -15.0233 | -41.362 | 2026-10-10 13:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 124.3 |
| f115894d-45c2-3f34-9a27-b6ebaafd5051 | -12.39 | -46.5761 | 2026-10-10 13:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 3305d170-e158-35ec-8ac9-ac54b726d14c | -11.8307 | -43.5866 | 2026-10-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 49612e83-5d97-33ad-b7f4-820b8dba1565 | -11.1873 | -45.3347 | 2026-10-10 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 1cab9d42-9a53-3b62-970d-62d45c6b3ea5 | -9.9384 | -44.8791 | 2026-10-10 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 339.1 |
| b83673d5-ad75-3e38-9305-063af3274fd0 | -10.9093 | -44.8438 | 2026-10-10 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 84ee9192-c7d9-3935-85d9-531bc063878a | 3.0368 | -60.5386 | 2026-10-10 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| de6e988b-2764-3e68-8864-090ca5421912 | -11.1876 | -45.3117 | 2026-10-10 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 48dd58fa-5670-3301-b7af-f4e9b7da8aa5 | -10.8905 | -44.8232 | 2026-10-10 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| e60bc276-885d-3805-91dd-1818c8f6abcc | -11.8595 | -47.3694 | 2026-10-10 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 99e645f5-06b1-32cd-a68a-3c0ed3cca062 | -11.5793 | -43.6965 | 2026-10-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 6f64fb01-5b35-3cce-8072-88a29ba7154b | -15.043 | -41.3576 | 2026-10-10 13:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 158.5 |
| af3db39b-4577-3398-88d8-e76a403f5e53 | -11.2068 | -45.3091 | 2026-10-10 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| ab26efc0-bf3f-3105-b9b2-abf8fd2c5144 | -9.9211 | -44.7662 | 2026-10-10 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 182.1 |
| ab6f8686-8c6d-302f-ab8d-97f16fe15ad9 | -11.0379 | -44.012 | 2026-10-10 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 52039803-789d-3df9-bb47-2646002ea0ad | -12.3708 | -46.5789 | 2026-10-10 13:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| aa12f9bb-c835-3cd3-9481-73422ae1b507 | 3.0551 | -60.5383 | 2026-10-10 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| abe21628-faf8-383e-b041-c15904c575bc | -10.9197 | -45.3712 | 2026-10-10 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 6eda8fec-366c-37aa-a86f-fb171753b087 | -8.9879 | -45.1292 | 2026-10-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 413e02f7-1ac7-3d49-b1eb-8f8f229acf60 | -9.9381 | -44.9022 | 2026-10-10 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 1c542ba5-1b9d-337e-a990-78998db099b3 | -8.9085 | -45.4114 | 2026-10-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b753e71b-e021-34c6-9670-e8fe4c66d5bd | -9.9208 | -44.7893 | 2026-10-10 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| e145c923-4f95-3269-beae-094d7ec75f32 | -10.8909 | -44.8001 | 2026-10-10 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6e9db007-d9f8-3c99-b4c8-db61566313ee | -8.9275 | -45.4094 | 2026-10-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| d6d64c30-481e-3829-9689-568044ae04dd | -9.9398 | -44.7869 | 2026-10-10 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 155.4 |
| c3aa73f8-01d7-348c-9548-4e6bd34c93f1 | -9.1924 | -49.7678 | 2026-10-10 13:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 57a71e61-162f-30b5-895f-7d501d14537a | -10.9388 | -45.3687 | 2026-10-10 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 281400e4-80cf-3af1-842c-e32a72325b6a | -9.9395 | -44.81 | 2026-10-10 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| be3ea1dd-1189-38ef-bf36-91a6126c487e | -12.1729 | -44.7983 | 2026-10-10 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| f57a74ca-af5f-3c28-a6df-84a8b8b4eaf9 | -10.9097 | -44.8206 | 2026-10-10 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 462.1 |
| 16b0a4e3-7f41-34df-81cd-a5b8594c40d6 | 2.727 | -60.2586 | 2026-10-10 13:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 796b4ab2-1876-3884-8213-39ce666a36ff | -11.2083 | -45.217 | 2026-10-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 639aed25-e000-35a4-80c0-932103343c8c | -11.5976 | -43.7408 | 2026-10-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| e51acb4e-44b9-31f2-b1b1-7ebac8ad1aac | -12.0699 | -47.3632 | 2026-10-10 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e9a454fe-abd0-378f-8489-f8b4582c4d01 | -12.0507 | -47.3658 | 2026-10-10 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |


[Clique aqui para ver as próximas entradas](README156.md)
