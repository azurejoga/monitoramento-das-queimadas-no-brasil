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
| 02d82f3d-c3a6-3860-9f22-16ed0c35b416 | -4.4805 | -43.4237 | 2025-10-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 774f1096-08f7-35dc-b287-1b618b18f214 | -3.71 | -47.6621 | 2025-10-27 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 64a8ca71-508e-3ec1-8607-70f514bdd836 | -9.1371 | -51.299 | 2025-10-27 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9ac377b5-5d68-3b51-852a-6ff053d81eed | 0.4326 | -50.8163 | 2025-10-27 00:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cc5622be-8a3d-3e88-a471-3967f99a9bac | -13.316 | -54.3841 | 2025-10-27 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c4cb8cc5-a122-34b2-bc07-9ff322a254df | -4.462 | -43.4016 | 2025-10-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 58622e2e-27ac-3df4-ad6e-a5ca9f6468df | -4.4617 | -43.4481 | 2025-10-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 868fbe58-97c6-3e78-a883-146a2c4ce82a | -3.8658 | -49.7998 | 2025-10-27 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fcc11ab9-9620-3eaf-8d6a-02f4e99ed7b3 | -12.5258 | -47.5678 | 2025-10-27 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 678dbd46-420d-3d09-b5fc-a678a5ffd940 | -3.7286 | -47.6613 | 2025-10-27 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 25df446c-4ea1-321d-99ef-a43424b57dc7 | -10.8401 | -56.959 | 2025-10-27 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 02bbd605-e322-3789-ab25-3fa5314bc8ce | -3.7287 | -47.6395 | 2025-10-27 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| ce510cf3-b23b-3fe7-9865-387977c35755 | -9.4627 | -47.7447 | 2025-10-27 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| ecc9efac-64fe-3d88-be95-e0c75365cce8 | -7.8599 | -46.4629 | 2025-10-27 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 64d8b765-4e9f-3510-a4c4-fe557fec5f36 | -4.4433 | -43.4027 | 2025-10-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9b6ce2dc-f16b-365a-9bb2-a024772afdd9 | -7.8411 | -46.4646 | 2025-10-27 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f7f899c6-3ca8-32a8-b5cb-fed097c1554e | -9.463 | -47.7227 | 2025-10-27 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 88fe64f0-6115-30fe-91cd-d89d102a6006 | -12.2884 | -43.7732 | 2025-10-27 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9841863e-452c-301c-b8a3-d6b890468af2 | -4.4431 | -43.4259 | 2025-10-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5db81ba1-24bf-313e-8573-75add07c982a | -10.7484 | -44.1932 | 2025-10-27 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1205f0fe-8ad2-3145-b97d-a8af98ce2fb8 | -12.2888 | -43.7495 | 2025-10-27 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 380.1 |
| b21cf7dc-3ac0-379a-9521-cc4fc496bc99 | -13.2777 | -54.3882 | 2025-10-27 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 72f41f74-3ea3-3057-9dd3-8f5392bfa98b | -3.1612 | -50.3298 | 2025-10-27 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| dfc75bbc-dc76-39b7-8cc9-c9dde7dbac07 | -13.2969 | -54.3861 | 2025-10-27 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ca998b5d-540c-3e0a-9726-b9bcddfcf4b9 | -12.2893 | -43.7258 | 2025-10-27 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| cd34cb3f-0c47-32ee-8b93-5694ed137dc0 | -6.8794 | -45.1775 | 2025-10-27 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 57f4a292-cc9d-3b31-a2ba-bc64f0005bdc | -13.2966 | -54.4068 | 2025-10-27 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a5ef592b-17d8-377f-9b8b-990e05d8f3d3 | -12.5262 | -47.5455 | 2025-10-27 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 886785aa-024f-37eb-b6f4-fd5a41edfc5c | -4.4479 | -45.4599 | 2025-10-27 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| f50e3ba2-34fa-3391-a156-901fa92dbd7c | -3.4768 | -49.9619 | 2025-10-27 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| f83bd631-78d8-3c73-8be1-99f60978d8fa | -12.2695 | -43.7526 | 2025-10-27 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ea446f9d-69c4-3b8f-92ec-1a430870d533 | -3.125 | -50.1629 | 2025-10-27 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 159687f7-eea8-3767-b492-a60f61c03f4a | -3.7101 | -47.6403 | 2025-10-27 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| e6e7991a-6313-3ae7-9234-095486b69fa5 | -4.4618 | -43.4248 | 2025-10-27 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0920151e-b484-3dc3-85ba-4c58aba52a15 | -7.8408 | -46.487 | 2025-10-27 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 8958611d-c38a-3bc4-b0cc-5016b4779014 | -19.63586 | -45.39161 | 2025-10-27 00:09:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 114e7d88-9509-3218-a441-cb0729fea7aa | -20.72394 | -42.77966 | 2025-10-27 00:09:00 | TERRA_M-M | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 2bb9dfc6-fd6f-3f35-8f6c-d3b512a32b55 | -20.76473 | -43.23008 | 2025-10-27 00:09:00 | TERRA_M-M | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c2138928-0c60-35bf-925e-feb15f67b962 | -21.47286 | -44.49225 | 2025-10-27 00:09:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 09b246ae-ecc8-3357-b232-6a77bb52d02a | -19.75076 | -42.05739 | 2025-10-27 00:09:00 | TERRA_M-M | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b6a9f332-30e3-36a9-95d0-ee019076d6fb | -20.1726 | -42.17031 | 2025-10-27 00:09:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8b38dc59-c0e2-3528-a603-ee8e1b02e1c8 | -19.99612 | -43.754 | 2025-10-27 00:09:00 | TERRA_M-M | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4d4d8449-b551-3f56-929c-f531f055eaa3 | -20.22243 | -42.74726 | 2025-10-27 00:09:00 | TERRA_M-M | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c1f8650b-d859-3b16-bfd7-6b623819611b | -21.47785 | -43.86018 | 2025-10-27 00:09:00 | TERRA_M-M | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 201b9976-5184-3f68-baa0-686226fcaa66 | -19.93064 | -44.31343 | 2025-10-27 00:09:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 86ef3990-effa-3548-aa4a-128457d64c23 | -20.8022 | -43.30522 | 2025-10-27 00:09:00 | TERRA_M-M | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 94119783-db5f-3c3c-9535-8589af30faa4 | -22.88756 | -42.45795 | 2025-10-27 00:09:00 | TERRA_M-M | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e871ad8d-1d09-3a8b-9211-f01ec081bc18 | -20.22116 | -42.7378 | 2025-10-27 00:09:00 | TERRA_M-M | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 69b44562-7c26-3025-8a0d-964cab8eeef3 | -20.40583 | -44.2905 | 2025-10-27 00:09:00 | TERRA_M-M | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 9a8e84aa-f716-3dc4-8b7e-b44a502e9c81 | -19.67017 | -44.66425 | 2025-10-27 00:09:00 | TERRA_M-M | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a9cfd1c2-e55d-3f23-90e8-de3e21adfe01 | -21.59001 | -43.49911 | 2025-10-27 00:09:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| b0829a5b-9e8f-3d53-bdf6-0ff49b3cd117 | -21.06694 | -43.64338 | 2025-10-27 00:09:00 | TERRA_M-M | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| f6a6bd4f-4b95-37a0-9dfc-c9900d13dab3 | -21.66808 | -44.51044 | 2025-10-27 00:09:00 | TERRA_M-M | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d86eaed6-bb8c-3239-bbc7-95139a650dcf | -21.81611 | -43.33231 | 2025-10-27 00:09:00 | TERRA_M-M | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1e41675b-202f-3646-a39b-1cbc40ad18b1 | -21.34798 | -45.23971 | 2025-10-27 00:09:00 | TERRA_M-M | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| cf12e7da-be88-35a3-92c9-5276e78fe3ea | -21.58868 | -43.48882 | 2025-10-27 00:09:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b99be941-1a13-3462-9c9e-9150c38a8cbf | -20.9802 | -44.32621 | 2025-10-27 00:09:00 | TERRA_M-M | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 109a593d-fa40-3f71-9f22-07d7b1568960 | -20.75567 | -43.23139 | 2025-10-27 00:09:00 | TERRA_M-M | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c490e1c3-6475-316f-869f-684d4012a022 | -19.44384 | -43.04075 | 2025-10-27 00:09:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2b143035-6601-39b9-8537-1fa27d8861a3 | -20.66142 | -42.72664 | 2025-10-27 00:09:00 | TERRA_M-M | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0b6972f6-7a2f-385a-aa24-8a445c1700ce | -20.6627 | -42.73623 | 2025-10-27 00:09:00 | TERRA_M-M | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 09568838-9caf-33f4-8fea-cf43aa49ffe1 | -19.98793 | -43.7515 | 2025-10-27 00:09:00 | TERRA_M-M | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c82c471b-766b-3ee4-8c10-e8670d512246 | -19.52674 | -44.52141 | 2025-10-27 00:09:00 | TERRA_M-M | FORTUNA DE MINAS | MINAS GERAIS | Brasil | 3126406 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cfdb71a2-6c5b-36f3-afbb-0ae2ce1b672a | -19.63436 | -45.37947 | 2025-10-27 00:09:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c5d6af92-0c9f-3cd7-ae13-7272574b1422 | -19.82041 | -46.15753 | 2025-10-27 00:09:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cf3f67b8-ffa0-3a91-99e4-c134cee85497 | -3.1428 | -50.3304 | 2025-10-27 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 582fa610-4172-3d28-8926-beab4afbdf83 | -3.71 | -47.6621 | 2025-10-27 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| f1c3b538-da97-3e7c-9e14-0feafee4e192 | -11.9221 | -43.8318 | 2025-10-27 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a45edae3-4514-3a87-8fd4-6b870ce1503a | -7.8596 | -46.4853 | 2025-10-27 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 16590d7c-9ac8-3c45-bcee-57452a7e1481 | -4.4433 | -43.4027 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| de714b3f-ddbb-3b76-bd30-6aaa43a26d67 | -10.7676 | -44.1905 | 2025-10-27 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7ca47ccd-444b-3851-bf2a-14bdccb18b0f | -6.7935 | -40.9821 | 2025-10-27 00:10:00 | GOES-19 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| e2fd8b79-891b-3674-ab9b-cf22e3b6dcf2 | -12.5258 | -47.5678 | 2025-10-27 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| a59be4dc-bdf1-32fa-b0f5-3cffb1dc1c07 | -9.1371 | -51.299 | 2025-10-27 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2ebc64be-2137-3fd6-820b-a698e01bb3cb | -12.2888 | -43.7495 | 2025-10-27 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 7028e16f-fcc0-3943-9433-f387a33689f4 | -4.4992 | -43.4226 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| a34bfe4f-2879-3558-b50a-0e328ae643bc | -4.4618 | -43.4248 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 51a4cf7d-cd74-3891-b4a9-2282214cdc07 | -3.7287 | -47.6395 | 2025-10-27 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 92f00e9a-e598-3f4a-91b2-4b53c382706f | -10.8401 | -56.959 | 2025-10-27 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| f9f753a6-b068-3556-8167-e212a3a54aee | -3.7286 | -47.6613 | 2025-10-27 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 98e97e1a-efdd-3294-8248-a4abd7531755 | -3.7101 | -47.6403 | 2025-10-27 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 71393673-9e4a-3dc7-8708-7eac47fbe1f8 | -12.545 | -47.5651 | 2025-10-27 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 1f67a9ce-3262-3cec-bef0-ff2abe4e2998 | -14.3982 | -51.5443 | 2025-10-27 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b0ba6bd2-ee80-32a2-94aa-ea71b1cf53bb | -4.4431 | -43.4259 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 715d9b47-7d54-3a5a-89e1-4075d9531922 | -12.2884 | -43.7732 | 2025-10-27 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d9abed5d-7482-3b64-b465-44f41a17fdc0 | -11.9225 | -43.8081 | 2025-10-27 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9a6e0c10-4cac-3eee-99d1-2c961da4d57a | -5.5423 | -43.9558 | 2025-10-27 00:10:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 10fb884c-ac12-3f44-a2f6-1f95187749f0 | -7.8411 | -46.4646 | 2025-10-27 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 81674447-6248-3923-a470-e3bbbb2d592c | -12.2695 | -43.7526 | 2025-10-27 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 51dccf12-4133-3b42-a1fd-3b2277889aef | -10.8213 | -56.9604 | 2025-10-27 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ad3977fb-5d39-3cff-aa5f-d586f338c4cb | -4.4807 | -43.4005 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3f86ab98-2890-3340-b753-41d1f58bfe75 | -7.8408 | -46.487 | 2025-10-27 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 214603de-4027-3e72-91c5-40e40c890d20 | -10.7484 | -44.1932 | 2025-10-27 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f49004d6-559f-3ab1-a9b9-2759c4ee0a82 | -7.0692 | -46.7541 | 2025-10-27 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| b12b1f8c-39d2-362b-a5ae-8a52f1cbd8f1 | -3.1612 | -50.3298 | 2025-10-27 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 53f88e4f-f298-3403-9854-4422d28f3778 | -4.462 | -43.4016 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| dc53cbe1-41d8-383a-9987-3672bbaac0f3 | -4.4805 | -43.4237 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 248.6 |
| 0a4b8d7a-7e88-347a-bfc3-d502b419f2d3 | -4.4804 | -43.447 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 49410221-fd15-3eb9-b1ed-a33a33139394 | -4.4479 | -45.4599 | 2025-10-27 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1fdcdd8e-048b-3df9-84b8-6abbffae217a | -4.4617 | -43.4481 | 2025-10-27 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |


[Clique aqui para ver as próximas entradas](README2.md)
