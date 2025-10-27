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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27eaade7-13c6-3a6f-a7ef-65db9400ab94 | -4.706 | -48.6328 | 2025-10-27 14:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| b2cd3159-f7c4-36e4-b195-c3539bf70080 | -7.257 | -44.9623 | 2025-10-27 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d7814ce0-6c80-30e2-a1b0-dfd4734e2a55 | -14.3551 | -51.8064 | 2025-10-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| c2684745-3874-30c1-a5ca-5c6c71949d44 | -7.0883 | -44.9319 | 2025-10-27 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 9aa5502a-a052-3297-8a28-3fe0809b682e | -7.8228 | -46.4217 | 2025-10-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a6d62e8e-eed3-3268-80c5-27856c9705bc | -3.3448 | -42.877 | 2025-10-27 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| edaeb3fc-1478-3a32-a8de-b5f60732cec7 | -4.172 | -42.079 | 2025-10-27 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 419033d1-b883-3056-8be7-d5f5f7ddc316 | -6.5603 | -41.6099 | 2025-10-27 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 203.5 |
| e9a7de84-cc53-3e0a-a7e9-70ebcf77f972 | -4.3877 | -43.3362 | 2025-10-27 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| edb665b4-0a97-3696-b83d-c49b90481de3 | -3.5834 | -43.5877 | 2025-10-27 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 7e854ce5-3f82-39c4-9e3b-99c06eb95b19 | -6.9069 | -46.1439 | 2025-10-27 14:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d35c2277-925d-399c-ac02-b227475ed50f | -11.4229 | -46.0781 | 2025-10-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| c7276ca5-1208-3f74-9790-3edd230ce5e4 | -9.289 | -45.232 | 2025-10-27 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 750f8155-c3e3-31f8-b3e5-2a27a89b9314 | -14.6304 | -48.4337 | 2025-10-27 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 7f8e52c6-af7a-3f17-8b36-e3efbab8f7f4 | -8.6526 | -44.7771 | 2025-10-27 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 1d81a1cb-9a6c-3c37-aa75-02d35cdcd910 | -7.8411 | -46.4646 | 2025-10-27 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4ae95150-6fb6-38e1-8ce5-1067359fd4e3 | 1.6387 | -55.706 | 2025-10-27 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fb2a7d12-4bb8-3f10-b939-9e8c27fa5db0 | -7.8413 | -46.4423 | 2025-10-27 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 64c14d2c-ae70-348f-8e83-65c81115980d | -18.3199 | -42.1385 | 2025-10-27 14:40:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| ea4ebdfd-27e1-3bda-8990-53284bfd0460 | -8.0608 | -46.9558 | 2025-10-27 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 70c6b2d8-dcbf-3ee1-b2b9-e89657236744 | -8.0971 | -47.0632 | 2025-10-27 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| a7a2068f-63fd-31c3-80d7-8177fe6e8d74 | -4.4066 | -43.3118 | 2025-10-27 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 452694ff-6c71-358f-9f59-e57e6f7df229 | -11.442 | -46.0755 | 2025-10-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 20b30e7c-af8d-3859-bb4b-3d8a572d4d2f | -7.9072 | -47.2573 | 2025-10-27 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 565f0c77-51e4-36fe-bd32-139a303dfcb4 | -8.5034 | -47.6646 | 2025-10-27 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 77d837fe-1cac-3399-88fb-512ca2796ef7 | -12.3488 | -50.1563 | 2025-10-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9346e323-fbca-3248-bf5d-97d2672bfd0e | -14.393 | -51.844 | 2025-10-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4502070c-1512-3698-bd35-78764d2ab542 | -12.1267 | -45.2219 | 2025-10-27 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 48ff5001-128b-31d4-bb8f-23a6aad5852b | -7.8159 | -45.3875 | 2025-10-27 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| a8130ad6-141f-3301-abc6-8adfe1a1ff12 | -9.33 | -49.2823 | 2025-10-27 14:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e50b5377-b4dc-3460-97fa-d406e552a554 | -10.0191 | -47.1305 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 8c062977-3d36-3adf-86b8-d1b682fa7a28 | -7.346 | -47.1515 | 2025-10-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 71404349-fe6a-3b2f-9f3e-8c3c677225aa | -7.6922 | -46.3443 | 2025-10-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a24e1e83-6955-35dc-be55-6a4436ae8c97 | -3.3447 | -42.9004 | 2025-10-27 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 0f93be62-219d-3d15-9148-6cfdea4ffce4 | -4.2457 | -42.2408 | 2025-10-27 14:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| cf0491cf-9e79-3731-8bf6-71bca32cefbf | -4.914 | -42.9764 | 2025-10-27 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 01a779cf-8536-3464-99e1-cd73d6388b2d | -10.0185 | -47.1751 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b9921322-9bed-3661-8488-7eab8eacf3a8 | -3.0203 | -44.3934 | 2025-10-27 14:40:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 9e3d7bb8-d568-3055-81b7-237a9cf25396 | -14.2978 | -51.7713 | 2025-10-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 0ca4536b-1845-3ef3-bede-0b3050ac4291 | -4.4602 | -43.6569 | 2025-10-27 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| fce457c3-e489-32f0-b16d-52ae52f4efe4 | -7.7592 | -45.4156 | 2025-10-27 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d8a5aac8-b7c4-38b4-9c4c-cf5296ffedbf | -7.8416 | -46.42 | 2025-10-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 70b7067d-49ee-3a92-9178-9c58a7005df1 | -4.4665 | -45.4589 | 2025-10-27 14:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b4751a0a-4831-3c8d-b7b9-47f8fbc4d9ff | -8.2682 | -46.892 | 2025-10-27 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 2ac70163-ea65-3af8-936f-f4e4fad8a937 | -12.3863 | -50.1947 | 2025-10-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 53fb08e4-b30b-308b-a809-ad637cdb0ce4 | -4.4479 | -45.4599 | 2025-10-27 14:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 25dd71c9-2380-30cb-bdd0-2443fd156a1b | -5.7758 | -42.9842 | 2025-10-27 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 04742f0f-b381-3dcc-b426-fca01312557d | -8.7438 | -49.5946 | 2025-10-27 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a8427442-9c0e-3204-92bf-572083f958af | -14.6499 | -48.4307 | 2025-10-27 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 395.1 |
| 78704ad9-e98c-3408-a20d-9c229999ff4c | -9.5679 | -46.9364 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 601653bc-df36-32ec-a767-0ad726b35e86 | -8.287 | -46.8902 | 2025-10-27 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| d2c245fe-d3a4-3802-b50c-f11815e374f3 | -3.7096 | -44.3409 | 2025-10-27 14:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9e2afb42-b71e-3e27-8ddd-754c89f11647 | -8.4593 | -48.2159 | 2025-10-27 14:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 411.5 |
| 3faac7ec-cfe8-3abc-9bb0-e392979c6c1f | -4.8744 | -43.2595 | 2025-10-27 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 864fea6d-9ccd-3328-86c3-3c64f7fe2a15 | 1.657 | -55.686 | 2025-10-27 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| da060ade-1e3f-3d9f-b857-9976e97a8b9d | -12.3484 | -50.1779 | 2025-10-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| ae203e65-4b5e-3288-af20-7e5a1f671c98 | -14.3934 | -51.8226 | 2025-10-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 57361fe0-46a3-3fb6-bf62-48b225a63169 | -5.9656 | -42.7574 | 2025-10-27 14:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 8acb255c-59d4-3c2e-b0e1-9e960b83c509 | -9.308 | -45.2299 | 2025-10-27 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 323c09df-d083-362e-9460-29acfd699c50 | -4.388 | -43.2896 | 2025-10-27 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 97d55877-f89c-3ced-904c-e1182f2dd09a | -14.2974 | -51.7927 | 2025-10-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| fe5ac9a0-db5b-32af-92aa-8b5db0a58947 | -11.4417 | -46.0983 | 2025-10-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 77830ecb-e7b6-3a75-8070-0c247ee47bbf | -10.0002 | -47.1327 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1e341d6a-eb2b-3f89-a9f7-e60ea75014ec | -7.8223 | -46.4664 | 2025-10-27 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6cd43bd7-d4ac-3d5f-a085-d99e8e179ddf | -14.781 | -44.9835 | 2025-10-27 14:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 7c38b514-eabe-3f00-9859-8655f7b49ca2 | -7.8157 | -45.4102 | 2025-10-27 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 9924a270-8e36-3fb3-9634-7e13e7c2d167 | -7.8225 | -46.444 | 2025-10-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 907148d1-ef44-3476-904d-e221598847a1 | -6.5605 | -41.5859 | 2025-10-27 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 209.5 |
| ab9d6ec2-a09d-3fef-9956-736d5f62cf8e | -9.3491 | -49.2589 | 2025-10-27 14:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 189.8 |
| bbae1c1d-e9fa-34b2-972d-d7d79ec44f15 | -3.6022 | -43.5636 | 2025-10-27 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0e6c2f25-c6a1-3953-8bca-7cdd76f6308a | -3.3261 | -42.8778 | 2025-10-27 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 3660f129-1168-38bd-9fde-f84f9e6c1954 | -7.0835 | -45.3865 | 2025-10-27 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fe2393d1-28e0-39a9-91cf-b2f9634652cb | -9.5676 | -46.9587 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 1f929c19-8519-3437-bd5d-1f1548adaafc | -4.9146 | -42.906 | 2025-10-27 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 3e6c136e-d683-3878-856f-f4eb4cdc0719 | -8.0444 | -45.1606 | 2025-10-27 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 025defb3-2d13-3fa9-ae1d-8ea103497f68 | -7.5242 | -46.27 | 2025-10-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2a368578-54ef-3349-92bd-d3f160ab8c39 | -4.8953 | -42.9776 | 2025-10-27 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 458b11d0-9b3d-3d45-adc6-a248671f1e96 | -9.4745 | -46.8575 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |


