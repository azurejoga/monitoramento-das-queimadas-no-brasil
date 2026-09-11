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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 186b5361-214b-3b80-8f68-7a53e8e4eeb7 | -13.285 | -61.8093 | 2026-09-11 15:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| d3af9bb0-920f-3dfd-af17-e895e10d51ad | -13.3555 | -51.7855 | 2026-09-11 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b80d5198-f9e1-362f-bc80-3a345163d373 | -6.7649 | -59.4216 | 2026-09-11 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f9125dc9-d3f7-3295-a33d-71749fb50047 | -10.5475 | -51.3578 | 2026-09-11 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 547.4 |
| a9f08433-5ff6-38df-8af5-b1a3913b9cf0 | -9.9041 | -45.91 | 2026-09-11 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 3a3626dd-e604-3198-96be-e8410c89ebe6 | -5.8572 | -53.8642 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c3816317-a7bf-365d-b397-50678b6298cb | -13.3552 | -51.8068 | 2026-09-11 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.6 |
| dde11979-39e4-3e69-adde-d7e9ebd2cf9d | -6.325 | -55.8451 | 2026-09-11 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 957cafcc-9942-3416-975e-4813092cd48e | -12.169 | -64.1404 | 2026-09-11 15:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e283dad4-381d-31a4-b789-f93dc92cfacc | -11.3513 | -45.7922 | 2026-09-11 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 666.2 |
| 095c7eb4-30c3-3a6c-987b-9d9989b99bfd | -10.5478 | -51.3367 | 2026-09-11 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 227.8 |
| d6e05a59-3e9b-3080-9282-4802423d455f | -6.4045 | -54.9842 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5b3463de-109f-392a-b477-f37a4a9d1262 | -8.5824 | -47.3488 | 2026-09-11 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4d63c223-6d49-32f7-bd0e-71db461975e4 | -9.0415 | -65.7349 | 2026-09-11 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8f177e3e-0a5a-3ba3-b0ba-57d18bf256d3 | -13.2848 | -61.8287 | 2026-09-11 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| cf7addb1-55d9-3af4-89fb-7a3f3ee4b69c | -6.828 | -55.3026 | 2026-09-11 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1e813342-033f-3014-af4d-84703d7e291a | -6.2427 | -51.7146 | 2026-09-11 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a44c8b44-ee0e-3ce3-ab3d-0790014f8f1b | -13.4198 | -51.3731 | 2026-09-11 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7c045651-a594-34b3-aa20-6a02b2f783cc | -13.2088 | -61.8338 | 2026-09-11 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 931ad180-4b0c-3812-b099-0c490dc90739 | -10.2559 | -45.2292 | 2026-09-11 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| ea341711-eb1f-3462-94fd-c5b5c67b9c4c | -8.619 | -47.4335 | 2026-09-11 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c9972b35-aaa7-3b58-b1b3-266ec6dc46cd | -10.641 | -46.136 | 2026-09-11 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| c902daa7-a572-30f1-a76f-f7f56a25de76 | -8.9428 | -63.2797 | 2026-09-11 15:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2e45c772-66ce-3f0f-ada0-9a4d2293f3a0 | -8.6311 | -66.5287 | 2026-09-11 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3e4d51b3-6a0c-3f6b-8bf7-d337150d3ead | -8.0748 | -54.8499 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7997477b-a6a0-30f0-abb5-4c1d1daaf219 | -13.3552 | -51.8068 | 2026-09-11 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 42cfcae4-8d23-3aa1-8f27-17c75875a0e8 | -6.2429 | -51.6939 | 2026-09-11 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ba21f4b5-7b1f-3234-b86c-135e97433a9e | -10.5475 | -51.3578 | 2026-09-11 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 677.0 |
| f00143c8-5639-34fa-a029-4c3bb6f5e150 | -8.6311 | -66.5101 | 2026-09-11 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e9554ed5-330b-3e79-b192-fe265aef1ecd | -6.325 | -55.8451 | 2026-09-11 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 8d354827-9516-32be-a678-87fe9dd4e684 | -6.7075 | -45.4861 | 2026-09-11 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 4fa97654-cf81-3452-84a8-9d1ab3cc08aa | -13.3555 | -51.7855 | 2026-09-11 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 8624d998-9348-3209-81cd-c68322c1b4c0 | -8.6378 | -47.4316 | 2026-09-11 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1ef35fc8-238a-3768-97a2-a6717ee9eac1 | -6.4047 | -54.9642 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b22a5a79-f8f2-313d-a349-ab55aa048f47 | -13.2107 | -61.6397 | 2026-09-11 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8549b867-8d88-37b9-81f4-484f1ff28a77 | -12.1501 | -64.1414 | 2026-09-11 15:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 582763cb-04d9-3a38-9d50-2dc72f19326e | -12.169 | -64.1404 | 2026-09-11 15:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 18f410b5-bf24-32a3-97e9-75254cda93ac | -6.1808 | -55.2748 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 443f5cd7-cf93-3ede-90e2-67ef69fc0bda | -9.1407 | -64.4024 | 2026-09-11 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c962eaec-1e31-3f16-99cd-f4d070e83b24 | -6.641 | -58.4987 | 2026-09-11 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5c369712-f2fb-3758-9df7-79d91f215996 | -13.3038 | -61.8275 | 2026-09-11 15:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 04d6e8f0-2a35-335e-bdd9-3636c99f6c77 | -8.9873 | -65.4379 | 2026-09-11 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 73a4fc2b-eb60-346d-b761-c5c3a80733e3 | -13.228 | -61.8131 | 2026-09-11 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 56bccb65-7175-3620-b90b-1a460493c3c7 | -11.3513 | -45.7922 | 2026-09-11 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 88c5a4e9-25a6-3e0e-828d-60eda3d3ce06 | -13.2278 | -61.8325 | 2026-09-11 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 111c3aef-21a3-3504-9dfe-c7acbcec0de3 | -8.6195 | -47.3893 | 2026-09-11 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f348b506-bd41-3ba4-9a4c-5c1041b24124 | -9.1523 | -49.9853 | 2026-09-11 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 29cc36cd-dcb5-331b-90a3-14ab8cc8a662 | -5.9814 | -57.7867 | 2026-09-11 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 56b8ee1b-a581-3cad-aa2e-a78e6323bbb0 | -5.963 | -57.7874 | 2026-09-11 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 01773ae5-1ca5-35fe-9cda-c42c336343e0 | -3.4241 | -59.2343 | 2026-09-11 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 965a08be-7528-31f0-bfd6-27ddbee57775 | -10.275 | -45.2268 | 2026-09-11 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 044e5f04-416b-399e-8a4e-09e14386a514 | -5.6314 | -51.6444 | 2026-09-11 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1f083bb7-4acf-321d-a2e8-62580355e2ce | -9.0058 | -65.4373 | 2026-09-11 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1f0c7a83-683c-3092-89be-adff2ff5cd31 | -11.0434 | -49.6851 | 2026-09-11 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| dfe543b6-38ba-3e7e-8ae4-4b3a728ed382 | -5.6313 | -51.6651 | 2026-09-11 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b8c4091d-37f3-3875-b170-b6504e0250cc | -10.4911 | -51.3423 | 2026-09-11 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 7682a215-d707-3c3c-858b-07563b53a3f5 | -6.8062 | -58.6469 | 2026-09-11 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4f14ccc7-974a-3236-89ff-a55e27b2fb0f | -11.9547 | -49.7512 | 2026-09-11 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| dc726f52-4837-3dc3-8971-c8ee00b9b074 | -10.4909 | -51.3634 | 2026-09-11 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| f2155c26-3976-33a3-bbb8-eff4f793e5a5 | -13.249 | -61.5983 | 2026-09-11 15:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 5fef97c8-7c04-3c45-ba06-bd70859fe875 | -10.5286 | -51.3597 | 2026-09-11 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| f2269ad4-c521-3499-9dcd-7c2fe71fa9b6 | -6.7648 | -59.4408 | 2026-09-11 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 247ab0bb-0d49-3af0-8533-480ab253f78c | -13.3623 | -61.6683 | 2026-09-11 15:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a03613dc-acb5-34ed-8b64-f9a4509c1539 | -6.0913 | -57.8992 | 2026-09-11 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d50da210-cc6a-38d2-994e-d6e6f74da61f | -6.1994 | -55.254 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 191.0 |
| c23862ab-5863-3c7c-b20b-2e5013975f18 | -7.1389 | -42.1051 | 2026-09-11 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| d13b79eb-d831-39db-83d5-20ce7e9bd3cd | -7.5553 | -45.1624 | 2026-09-11 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ec7e1295-4f2a-3273-ae11-a4f7e5c987b6 | -5.8021 | -53.8061 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 53a231b6-1716-3a5b-bfa8-5025f54c00a2 | -10.4722 | -51.3442 | 2026-09-11 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 171f14e9-ad41-3e74-acdb-e05c279d36e1 | -11.2488 | -54.1378 | 2026-09-11 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a05448a7-c67f-3da4-8f6a-8062e8b72c47 | -6.8281 | -55.2826 | 2026-09-11 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9686bf8a-a082-358a-a05f-43113d5ca209 | -5.8571 | -53.8844 | 2026-09-11 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 71deec65-1982-328b-a3a1-169932452be4 | -13.3055 | -61.6527 | 2026-09-11 15:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| be23ff2f-50c5-3483-be30-c8e2312417bb | -7.8379 | -56.58 | 2026-09-11 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c4863bd9-c60f-365f-a10b-aae32c1f058b | -5.8021 | -53.8061 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 01d1387c-75b7-3885-85e3-1cb5465bd11d | -8.0709 | -55.3121 | 2026-09-11 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 54279238-9fa6-34f6-9642-7cc728b836fe | -8.2201 | -55.2627 | 2026-09-11 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 77f9992b-f631-3151-a2dd-9c92bfb15fc5 | -6.7263 | -45.4846 | 2026-09-11 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c3b18c5e-d805-3ea8-ad31-676edad5f91b | -10.4911 | -51.3423 | 2026-09-11 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ac98de01-f8ba-3806-9cc4-f7c346f89c43 | -13.3559 | -51.7642 | 2026-09-11 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 75fcf7b0-80c3-3d80-b17a-d242bdb60dc4 | -5.8572 | -53.8642 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c259acae-1b26-3fe1-b7ba-3e15de1c0e38 | -8.2015 | -55.2639 | 2026-09-11 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 048e0e82-9f3d-3b92-8dba-8e253819f2e0 | -11.9547 | -49.7512 | 2026-09-11 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 217.6 |
| 77462cb4-d1ea-3f24-b151-fce6b58d3dad | -4.5229 | -54.9639 | 2026-09-11 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a2f0f587-f4ff-34b1-97d7-e3d6c9bbb91d | -10.2556 | -45.2521 | 2026-09-11 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 58825252-3d6a-328f-a8dd-5ee3e485a742 | -8.9428 | -63.2797 | 2026-09-11 15:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c4674f34-4594-3c55-ada7-87894e501ab6 | -10.7549 | -46.1441 | 2026-09-11 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 7ce94bbd-e777-3fb7-9502-7934d31c60b7 | -10.6413 | -46.1133 | 2026-09-11 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 9430b3c6-1a20-330f-9378-3e8ae3731342 | -3.4241 | -59.2343 | 2026-09-11 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 032e03e5-74f4-3c96-89d2-81caf13046b3 | -8.6311 | -66.5101 | 2026-09-11 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 379dfbcd-ea50-35a0-ae1a-5dd10273238a | 1.2797 | -50.6843 | 2026-09-11 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 998dccf4-e394-35f9-a5d9-95327b933c8b | -6.1994 | -55.254 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 3a69ab0d-a475-3dda-b4b2-d6d4f6bda4b0 | -9.0415 | -65.7349 | 2026-09-11 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| edc33bca-af4d-39ce-a9e1-eb6036ad431b | -6.641 | -58.4987 | 2026-09-11 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 338e90fd-76f9-3451-9fec-a1fbdf6d8b26 | -4.5413 | -54.9633 | 2026-09-11 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7f0670f5-8eaa-35c3-a249-89e92be560ec | -6.4047 | -54.9642 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 43803a24-46c9-310d-9bed-0e6c2eff820d | -6.8247 | -58.6461 | 2026-09-11 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2f204558-75c5-3792-8248-4c3b86484174 | -6.1808 | -55.2748 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ae7fa606-7119-3126-8f04-95bd5f1e67cd | -6.6888 | -45.4877 | 2026-09-11 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| df992576-de4e-3730-b048-80629fc8f017 | -10.641 | -46.136 | 2026-09-11 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |


[Clique aqui para ver as próximas entradas](README45.md)
