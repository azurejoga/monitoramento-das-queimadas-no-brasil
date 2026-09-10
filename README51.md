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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c09fd5f-0776-3c0e-b890-230a44fb5d14 | -8.7254 | -62.3987 | 2026-09-10 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8c9f3d8b-b912-3cdd-aae6-892c55f5d00d | -13.5227 | -50.9534 | 2026-09-10 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| cd6989ef-9c05-34d8-9014-1301b50498b9 | -10.6798 | -46.0858 | 2026-09-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 82ed5959-b7ed-3818-a615-246d29c996ff | -6.641 | -58.4987 | 2026-09-10 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 753a41a2-1401-3a4d-a036-baad96db898c | -8.6311 | -66.5287 | 2026-09-10 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6ac1f1b2-4021-345c-baa1-5d9e18c5d521 | -13.209 | -61.8144 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c4b0c5ef-397d-3551-980e-d9c1cf72f927 | -10.7585 | -45.917 | 2026-09-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e4870538-09a1-3d59-80a4-7641b842aec3 | -13.2282 | -61.7937 | 2026-09-10 15:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 739463ca-e361-3d2f-b09f-c2be291d5dc5 | -13.2865 | -61.654 | 2026-09-10 15:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| cad26326-59b0-3af0-b71c-975b66e204c8 | -11.4026 | -43.935 | 2026-09-10 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 541fa33f-dcfa-3cc2-a49f-18428eae5292 | -9.6944 | -43.4453 | 2026-09-10 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 117.9 |
| dd062c14-2ca0-380c-b4db-8371faed122e | -6.5126 | -58.3876 | 2026-09-10 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cd621b96-428a-3060-9877-f6dd669844ec | -3.4028 | -60.3232 | 2026-09-10 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8ad96a61-8399-3f70-9a49-583154f7c06b | -7.5167 | -45.2569 | 2026-09-10 15:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 6994248a-d789-39db-9f41-3da7a8e147e9 | -6.7123 | -58.9412 | 2026-09-10 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7e49833c-f436-3f56-ad81-1b236ea43176 | -3.4241 | -59.2343 | 2026-09-10 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 41ce0e70-2137-3e38-ac5c-539d302b24b0 | -6.7695 | -58.6097 | 2026-09-10 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 005ac774-2222-39db-ad1a-1291f84ea15b | -7.4976 | -45.2814 | 2026-09-10 15:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4d123169-5650-35be-a4cf-f0c772c1a26d | -9.6947 | -43.4217 | 2026-09-10 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 5732a1a7-4d43-34a9-8c95-6cef7e7fa8e0 | -8.6311 | -66.5101 | 2026-09-10 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 4811d2a8-f768-373d-a5d1-5ba763471794 | -10.7582 | -45.9397 | 2026-09-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 9ea0fb5f-b3bc-3489-9199-107df4a0f7a6 | -9.006 | -65.4 | 2026-09-10 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c8a5be99-5a0f-3b58-9975-452086c3c6ef | -8.3717 | -62.716 | 2026-09-10 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7886c786-9e28-3b05-8955-3c202208d254 | -7.1198 | -42.1309 | 2026-09-10 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 152.8 |
| b349dfc0-5643-34f2-9df8-49843d52f358 | -8.6311 | -66.5287 | 2026-09-10 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| ee680229-4eba-3b9a-9916-9dfd4192c7fc | -10.7395 | -45.9194 | 2026-09-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c535a1a6-0424-37de-b2bf-40e80c16d905 | -2.7332 | -57.6077 | 2026-09-10 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 5febcb1d-5008-3859-a0ae-d7b23ba025f3 | -13.2289 | -61.7161 | 2026-09-10 15:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| cbfb31a1-42fb-339f-96b8-2ea1443e692a | 1.0029 | -51.1033 | 2026-09-10 15:10:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5d0884a6-6ec5-3f41-969b-31fabe908833 | -8.9522 | -44.9731 | 2026-09-10 15:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 57cc182b-bb3d-3de9-9fea-bd6bdd18110e | -9.043 | -65.4175 | 2026-09-10 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b81a6b7d-1ad6-3b14-95cb-37ac80321bdd | -9.7698 | -43.4825 | 2026-09-10 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ba28f89c-3e3e-3ed3-ab76-ea531bbd95b2 | -10.0697 | -46.2516 | 2026-09-10 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 4cc813af-b645-3393-883d-f844d40bafda | -3.3687 | -59.427 | 2026-09-10 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 0c4a7c42-66cb-35ff-bf9b-09478054edc4 | -9.1168 | -65.4898 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b06143c7-8429-3eed-b504-96954e3219b5 | -9.1998 | -60.793 | 2026-09-10 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8901f8e8-f219-3d1e-b1d5-007167d39703 | -10.2365 | -45.2546 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 949c2d21-d12e-3f7a-b671-7b22abee182e | -10.2556 | -45.2521 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 259.4 |
| fd425565-a38f-30fa-9867-09517d3ee9d8 | -13.2094 | -61.7755 | 2026-09-10 15:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dc31c671-3187-3158-850c-4047e7c78986 | -8.9875 | -65.4006 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8acd3ff3-91a9-3ae9-9c1f-017375bf7c34 | -9.043 | -65.4175 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 70eec09d-4a04-3f8e-a401-d0175c89e19e | -9.2276 | -65.5797 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| bdd383a8-e3ed-32cf-8b37-df8e9ae41afd | -9.0058 | -65.4373 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2db5f72b-5e2a-3028-9cda-b1f3301e9c28 | -8.6311 | -66.5101 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| d01bc3c7-1874-3f19-b1ea-ec8ce3a3ed74 | -17.1078 | -56.8304 | 2026-09-10 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| a57a3c35-d141-3213-80d4-05ba00ecc849 | -6.5004 | -47.5909 | 2026-09-10 15:20:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 80d6f281-8d25-339b-ac6f-bad4e7bfd506 | -13.2476 | -61.7536 | 2026-09-10 15:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 66108ea3-1909-3e6a-aa72-37b4bf5e2186 | -8.3718 | -62.697 | 2026-09-10 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9c00cd02-4131-3ff5-afd2-181706cd8463 | -6.7833 | -59.4208 | 2026-09-10 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 366fff5e-f9ea-3862-8a21-cc96b6c86c46 | -10.2743 | -45.2726 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 327c98cd-286c-3a98-b9d1-c36a2e9deb92 | -13.2293 | -61.6772 | 2026-09-10 15:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e90e0002-fb2b-351f-adaa-ebdbaf3740af | -10.2362 | -45.2775 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 270.0 |
| 7341fe85-5a50-3332-8883-d0d52b07e7b1 | -6.5637 | -62.8908 | 2026-09-10 15:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 7c8635be-9d42-3d77-a6f7-e5f6198626b1 | -10.2559 | -45.2292 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 172.7 |
| a0c01f95-5d2f-3350-8b52-79a5b5bec2ef | -6.7695 | -58.6097 | 2026-09-10 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 142.2 |
| f5f9243c-ff4e-335a-beda-24e1552d4ab4 | -13.6516 | -59.4734 | 2026-09-10 15:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| fc4e40ba-9e96-3bde-a015-66ffe08b6f96 | -9.6944 | -43.4453 | 2026-09-10 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 67e45b5c-a801-37f1-8f7d-5bedf5e2d666 | -8.9874 | -65.4192 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 55e3078d-c9d4-3c33-939b-a49d85c561e9 | -10.7582 | -45.9397 | 2026-09-10 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 134c173c-cf01-3077-8959-71fdafce8002 | -13.2667 | -61.7329 | 2026-09-10 15:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2d797517-464f-3fb7-bc52-b3f490cc91f0 | -10.2358 | -45.3004 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 247.3 |
| dc19e096-84f6-3a9b-8a2d-8ed01c869121 | -8.6311 | -66.5287 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| fcc4463e-197c-32c2-b367-2df8f0f95708 | -9.0059 | -65.4186 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c8da1477-5bf3-32e5-ae13-15a5048beb5d | -13.3298 | -61.1064 | 2026-09-10 15:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 67ff56fe-e064-385c-bbf8-978246170b5f | -10.2753 | -45.2038 | 2026-09-10 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 264db4a0-aa30-32be-96c6-33d9fb90e47e | -10.6621 | -45.9974 | 2026-09-10 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 21501cd8-cb67-3882-b5ac-9386750763dc | -7.5167 | -45.2569 | 2026-09-10 15:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d73e69f1-0174-352f-8f1b-82bb925c82fb | -13.2666 | -61.7524 | 2026-09-10 15:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 83b9d545-b843-36bf-8e12-2d759be7a9f1 | -7.0211 | -59.7769 | 2026-09-10 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7ee7402c-9c06-3876-8631-df79b8868129 | -3.3688 | -59.4079 | 2026-09-10 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f105a449-6bbf-3eed-98bc-12a8072cd484 | -2.7332 | -57.6077 | 2026-09-10 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| fb18ea7a-375f-32ce-8d06-f00a853c512f | -3.4028 | -60.3232 | 2026-09-10 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| d1fd4335-ac3c-37be-b908-ba06fa17b5d9 | -9.006 | -65.4 | 2026-09-10 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 6c5604b1-806d-38cf-8656-a815f28f02f2 | -17.1034 | -55.9219 | 2026-09-10 15:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 7434f3d1-dcc8-3441-9804-8269ced02bde | -11.4026 | -43.935 | 2026-09-10 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 1384c6b2-ba13-3754-96e2-01a0fa1df473 | -17.1078 | -56.8304 | 2026-09-10 15:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 702dbbbf-c28c-391f-af75-73d2052b8344 | -3.3688 | -59.4079 | 2026-09-10 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c5871c5b-07db-30eb-bcb5-2af52da4477a | -2.7332 | -57.6077 | 2026-09-10 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| a8bd7017-7a49-34b4-86bc-dbaf84650c0b | -9.0982 | -65.4904 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b5554f44-ae4b-3689-904c-40838ac6d552 | -6.7094 | -59.443 | 2026-09-10 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2e5d47ce-b9c9-3b9c-b75c-efda542b9625 | -6.7833 | -59.4208 | 2026-09-10 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5b813f7c-1d18-3187-8a30-ad0439740b83 | -10.7582 | -45.9397 | 2026-09-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 6aea5317-08f9-3b4e-ad7b-b5ac6752d5e5 | -7.5164 | -45.2796 | 2026-09-10 15:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9161c3bc-78a3-3de9-b625-6875f54f8f89 | -10.0697 | -46.2516 | 2026-09-10 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 088b85cc-f11e-3a60-92b7-d23555a6d391 | -8.6311 | -66.5287 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 8e84f57a-18ab-3a1c-b62e-86073af143ea | -17.1234 | -55.8986 | 2026-09-10 15:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 1159cc62-0f5b-3486-8019-2ad09754ad5a | -8.9875 | -65.4006 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b6fede0a-a5cd-34b0-b47c-e1f803c382b7 | -9.0981 | -65.5091 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 200faca6-da96-3d80-9207-62ccb7795782 | -8.3718 | -62.697 | 2026-09-10 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| baa7ebdc-3095-3fb7-afd4-bbd4d5d88133 | -8.6311 | -66.5101 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.0 |
| edf4a710-8907-3b4d-bec4-c7f1cca117f9 | -10.7395 | -45.9194 | 2026-09-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 341f2153-e6ad-363d-a69a-70c23b87fb33 | -10.7585 | -45.917 | 2026-09-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3234aab0-3cb9-3903-81d0-fd695ad70b32 | -13.2725 | -61.1299 | 2026-09-10 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b08701d4-e784-35c2-813c-5d9581301282 | -8.62 | -47.3451 | 2026-09-10 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 40484fa7-4f1c-34a5-bdd8-d3f8623cc83f | -13.2092 | -61.795 | 2026-09-10 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 858884d4-f4d3-3151-9f04-d7cb7f3ba462 | -8.6009 | -47.369 | 2026-09-10 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 8fe14d25-79ca-3b6f-a1b4-3f9c10aa2219 | -10.6621 | -45.9974 | 2026-09-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 3655b0e9-4f6d-3637-b0b4-dcb8a30c6c2a | -8.9874 | -65.4192 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cb1ecbe5-eabd-39da-a810-314a4d305885 | -3.4028 | -60.3232 | 2026-09-10 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a3a0d937-a0f9-38a4-8b81-7f72f0b349f7 | -8.6012 | -47.347 | 2026-09-10 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |


[Clique aqui para ver as próximas entradas](README52.md)
