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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1051d38-5e86-3413-8c02-0e3ae92eafae | -9.52941 | -68.27325 | 2026-09-09 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6fcc4c8-85e8-34eb-af22-a7963ecdf97c | -9.00922 | -65.41579 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fe45003-334a-37f5-9d8f-aa604856dd36 | -9.65338 | -59.61002 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb6aeb7d-f105-3cfa-ac2c-f3111f3de18f | -10.65226 | -58.76748 | 2026-09-09 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 89a046bc-f3da-3cd8-8be0-f9af65495f95 | -13.21215 | -61.83152 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d49bbaf4-2c36-388a-ae82-d0734eb338ac | -9.32723 | -68.20777 | 2026-09-09 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ebd7a2-cc0b-3261-9cff-5313b89656c3 | -10.49458 | -59.6055 | 2026-09-09 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d371a95d-0fc8-35e6-b3b6-2f136d5127bf | -9.52102 | -68.6377 | 2026-09-09 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c95e1326-043d-3c23-b3b6-d65d4e51e1e5 | -9.14505 | -67.82468 | 2026-09-09 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4604766f-75a5-3325-9d4a-0b5caece2441 | -9.01145 | -65.42422 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4b760a9-5594-39d7-9daf-5dbf8245f5a8 | -8.98538 | -60.58058 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6d883de-16a3-3909-9c0d-99d4d6300884 | -9.24703 | -65.67268 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0227c275-9d71-31bb-9ba1-1fc7c6c97d41 | -8.74807 | -72.77046 | 2026-09-09 05:31:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7323e151-2067-351c-8cde-66208c5b57b3 | -12.08265 | -64.23867 | 2026-09-09 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4be159a-c8da-3468-a99e-b26452a0eea0 | -8.98823 | -65.41237 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7f3db45-258e-3cb8-a6d3-9a3f372785ad | -13.26281 | -61.67857 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb27e3f-3baa-331c-8030-3a91df41a161 | -9.69553 | -43.47684 | 2026-09-09 05:59:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 88c7bb8f-2873-3204-8283-6f2b3f1045d2 | -5.77604 | -45.06366 | 2026-09-09 05:59:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f195fe4b-210d-30a5-aed2-f5f5618be8db | -5.76129 | -45.09222 | 2026-09-09 05:59:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 936d7060-797e-36ef-bd5c-9e334af0e917 | -6.36805 | -43.58179 | 2026-09-09 05:59:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 41f55087-9937-3a46-a292-7154095fbbdc | -5.60267 | -44.84451 | 2026-09-09 05:59:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| cb74581f-df44-3bb6-98e7-6eb7b7799bcb | -5.75987 | -45.06115 | 2026-09-09 05:59:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| cb33b0a3-e3da-3c40-8b27-5fac744b29bc | -5.76706 | -45.05744 | 2026-09-09 05:59:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5f14cebf-244a-3076-b4e0-860efc79d829 | -13.17633 | -43.56385 | 2026-09-09 06:01:00 | AQUA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| def3ec51-68ee-33b8-9d39-946fefdd421d | -1.60792 | -54.91413 | 2026-09-09 06:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6a2f837-b292-3810-8b37-a31c3e908fc5 | 2.66277 | -60.1798 | 2026-09-09 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daba1d14-560a-3f87-aff2-383555960ae9 | -1.19021 | -55.72067 | 2026-09-09 06:03:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 542b7283-ba8f-31cf-b474-fc1e06b95f2b | -1.31603 | -54.65919 | 2026-09-09 06:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56dd99fa-acce-3514-a5cc-b0f420d4a10d | 2.66718 | -60.17908 | 2026-09-09 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33820820-87b7-32c4-9161-cddd500b0bdf | -1.61457 | -54.91532 | 2026-09-09 06:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 442d9edb-7a1f-34ae-9641-5f97ce091798 | -1.19095 | -55.71596 | 2026-09-09 06:03:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c82a2a9c-0efe-3c3d-a98f-c69153f05aeb | 3.21119 | -60.28744 | 2026-09-09 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 175870c8-39fb-35ab-8d97-9d1894872a0c | -1.19348 | -55.71968 | 2026-09-09 06:03:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 548906c5-973f-346e-8c9b-721fddf318c7 | -1.03815 | -53.73197 | 2026-09-09 06:03:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5a761a5a-9865-3406-a125-2fe34de13527 | -1.31517 | -54.6648 | 2026-09-09 06:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72e518b3-5a06-3722-ab94-885620ecc05b | -1.19419 | -55.71497 | 2026-09-09 06:03:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8fe1e33-486c-3c78-8124-06d0ada7f711 | -3.15021 | -60.65547 | 2026-09-09 06:05:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dedc673e-772c-349b-8085-d81efbf3b9e5 | -5.21968 | -55.99302 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f43961ea-5645-3cbd-af25-63133881517f | -5.37312 | -56.02101 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51c80165-eb12-3b3a-adce-5f2ba603d6f4 | -5.59167 | -60.2454 | 2026-09-09 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1634f34f-6e29-3cba-9e32-d5b4a280860a | -3.96126 | -59.36602 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66a3b08d-12a7-3bd6-bd18-b5c01b5df2db | -3.89348 | -59.60612 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f910b5ac-ab97-33de-b162-d2efce0e592f | -4.3809 | -55.04888 | 2026-09-09 06:05:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f9ea0da-57f6-35db-aa6f-85710b6d32de | -3.37199 | -59.40871 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6e57e67-8e85-3482-9ff4-90eec4f42dda | -3.83234 | -59.40314 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c024497-d01f-3471-8a76-9fd30cb77e10 | -3.43827 | -59.2587 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddea1d35-3651-35c8-bba3-f7c3b62d3f41 | -6.56268 | -62.89276 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d16a735-63b1-3669-b49a-7982c642981d | -6.63971 | -59.44017 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d962a9-1e78-3377-8e51-b2d00ee58994 | -3.13909 | -60.63364 | 2026-09-09 06:05:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df90c88f-9e24-3f70-ad97-c05c668c95a6 | -3.96215 | -59.36479 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8c2b150-71af-37e8-8f76-7085f97bd37b | -7.08895 | -59.81878 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6df7cf8-851e-3841-8972-336f7553d32a | -3.4414 | -59.26361 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f08a4ec-4228-3e06-ae0f-dd9b9638f253 | -3.36373 | -59.42892 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47d1fc36-1589-3840-bb23-360ba76156aa | -5.2131 | -55.99223 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0cc8c1d-69ec-3c69-8455-a98719a732a1 | -6.55785 | -62.89721 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bb5b151f-6de8-3dc6-bb1c-2be467c04611 | -7.1259 | -56.51385 | 2026-09-09 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 677823d2-3085-3ff1-b2de-52d688844540 | -6.79753 | -58.95043 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57cf8a9b-3020-3656-a74e-c211eb8c60a8 | -5.28459 | -60.11671 | 2026-09-09 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cffcf00c-19aa-338e-b48c-94dad57fc1fd | -3.15488 | -60.65623 | 2026-09-09 06:05:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1ceb7dd1-b706-3dae-a62b-354b40bf7553 | -5.37155 | -56.03211 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5694d65e-424f-3193-ac7d-9790d6b5044a | -3.36239 | -59.43788 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f58d1be-47a9-3f62-b143-41943c9c08d8 | -5.21174 | -55.99311 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cbe76da-c91f-390c-8783-636bc3c7fa92 | -3.89392 | -59.60318 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd8ad515-127a-3bbe-80a8-aad1bc2e70b1 | -5.28961 | -60.11745 | 2026-09-09 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 859b4a84-190a-3acb-bca6-6f55f8a8502b | -3.37485 | -59.42448 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 609801bb-9ceb-3059-bd86-d13a0feed958 | -3.43871 | -59.25568 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6067c881-4966-3a5c-961e-dc2b6006917b | -3.89901 | -59.60396 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b882d303-c986-3301-a3f5-22b5efdf465e | -6.55845 | -62.89213 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af6481ee-24a7-3a23-a1a1-6d5a2bd579d6 | -3.96304 | -59.35859 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24ed0cb8-ddb6-3fba-90ba-bde10c7ed829 | -3.56056 | -58.55784 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53aa4aa3-80ee-336a-b944-8d8c9f2c8171 | -3.83188 | -59.40619 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 668ce569-9c1f-39d7-a729-b8adc9363a93 | -6.55844 | -62.89329 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c12acfb5-4c5a-3c26-b722-c6da376e8d6b | -3.55686 | -58.55499 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9e533b-b79b-376e-8507-99794c8d65c0 | -3.56108 | -58.55445 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 518b582e-62ea-31df-b3ce-8435b7edc1ba | -3.36011 | -61.28514 | 2026-09-09 06:05:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d42e19d4-eeae-34f2-b7d3-e2d056e03c45 | -6.79591 | -58.95021 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c886cdb0-7e79-3388-98ea-269b35be2ee0 | -6.79701 | -58.95408 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bef5b09d-7c89-3cae-ae24-1bec2fbef6b9 | -5.36655 | -56.02013 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fd43afe-7f3d-33be-9855-7908d00cd8f9 | -3.43716 | -59.25676 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 935153c4-c3b6-3826-b338-a625bb092c0c | -3.13784 | -60.63175 | 2026-09-09 06:05:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a8174d4-c853-3902-969e-de4192693cb9 | -6.56211 | -62.89669 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ae2c309-6002-3771-8eec-25c449b8eb66 | -5.37233 | -56.02657 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2eaf829-8bb6-3330-a2aa-9c0a3cfbb268 | -7.08849 | -59.82199 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fa1be2a-fa53-3ea8-9461-191a6b6a1f98 | -3.35773 | -59.4341 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65008857-c578-3750-8f94-039825070f32 | -3.67848 | -58.52615 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6c20c74-845a-334c-b4b4-d52e7c9c16a6 | -6.55788 | -62.89607 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23ea49b1-1f79-3cee-a80b-924f5b4017eb | -7.12511 | -56.51025 | 2026-09-09 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89409443-0d50-352d-9cac-8b71d97e18fa | -5.18526 | -59.76078 | 2026-09-09 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ea60e97-06aa-3f2c-8d14-b6d754de9c49 | -3.443 | -59.26254 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 246cc7a3-6745-3f9d-a8de-3aabdb59cc3b | -6.63304 | -59.44895 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1433584-d937-32d6-a4fa-f70256d7492c | -6.80148 | -58.95092 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ad70e34-a7bc-3ec3-9277-435e55aaceea | -7.08323 | -59.82127 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb850f00-25a3-349d-906b-7db2f3702e60 | -3.96173 | -59.36294 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccbb4bcf-5492-3aa0-8c79-8279d0109beb | -5.21832 | -55.99392 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ff2a3f0-567e-347d-ab87-602f71208b85 | -3.55637 | -58.55835 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4041ca1e-37d0-3e5f-8456-ee9066dab36e | -3.95252 | -58.95722 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7177760-cc4e-3c7e-94bf-356e42000842 | -5.28542 | -60.11096 | 2026-09-09 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38d547e8-ec59-308d-be36-ef47444016ba | -3.43151 | -59.25904 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| a601d222-4d9f-3d27-ae77-8d7883cb7365 | -3.14252 | -60.63251 | 2026-09-09 06:05:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a59d8d83-aa3d-3aee-aaef-bad330cf1613 | -3.13982 | -60.62874 | 2026-09-09 06:05:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
