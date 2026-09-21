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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9d39248-c0a2-378f-9069-ad855189f944 | -11.0237 | -49.7304 | 2026-09-21 18:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 290.0 |
| c0e1841d-d96e-3bfb-a0b9-43994cc137de | -3.2817 | -57.8685 | 2026-09-21 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 12b70a7d-df11-3451-9bb2-dbfae3ba012d | -6.728 | -59.423 | 2026-09-21 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| eec0c937-5b2d-3df8-9719-840a3490fa74 | -8.7911 | -60.7935 | 2026-09-21 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 3f10e268-c6c8-3c50-8cb3-f63dc7552a9d | -8.8095 | -60.8118 | 2026-09-21 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 89398d12-4dd4-35d1-993f-5ff799c87b59 | -2.9326 | -58.3397 | 2026-09-21 18:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 5cce4346-b1d6-3dfd-ba6c-9c74cfbe2f4a | -12.3216 | -50.6751 | 2026-09-21 18:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 33e57560-dc0a-3719-835a-2bc108252e49 | -12.3021 | -50.6988 | 2026-09-21 18:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a47925f3-c33f-3880-ac65-84ebd6182cab | -10.7251 | -50.7896 | 2026-09-21 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 51205749-c128-32a8-92b7-aff1421125f0 | -12.0836 | -50.0378 | 2026-09-21 18:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 8259cf79-334d-31ca-83bc-2210337e09a3 | -3.4032 | -60.19 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 69ab0d70-5cd7-3ab0-9ef1-67160f5b475e | -11.0223 | -54.1379 | 2026-09-21 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 00e496bf-1ddf-3469-96d8-c7b84a5c96e4 | -6.7484 | -59.075 | 2026-09-21 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.9 |
| a6694235-1aa6-38db-af7e-dd92349b84da | -6.295 | -57.735 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 42272db1-c6f4-3bfc-a87c-e0f7ed93b019 | -3.6264 | -58.9228 | 2026-09-21 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 425d124b-adc9-3c9b-932a-e27a2a152dc4 | -10.8924 | -53.9652 | 2026-09-21 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 4cb607dc-488e-3dbf-9c26-9f3a48d39e25 | -8.7723 | -44.3031 | 2026-09-21 18:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 260.6 |
| 00f31777-0a20-32b3-91b5-8c423273d0be | -2.9528 | -57.623 | 2026-09-21 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 62592351-1649-336f-a2d1-4c76d5e7e043 | -6.3135 | -57.7342 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 0a520b18-4c5c-3be4-9741-e2509df7cd1e | -8.1878 | -54.7017 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ae838b65-3149-3790-afec-6e2883fb4705 | -8.7911 | -48.7502 | 2026-09-21 18:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8e262939-4f97-308c-911e-ead28aafd9bb | -3.5136 | -59.9401 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| def410f7-c8cd-3eff-841e-6579cb518437 | -6.3287 | -55.2677 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| cefae618-2022-3c5a-9c76-633b10ddbcf6 | -5.4012 | -42.9423 | 2026-09-21 18:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 9dec87aa-3e03-3e2a-a95d-0bf63dfffa7b | -1.3792 | -57.9747 | 2026-09-21 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| da11a593-d542-3ec3-b442-473a6df02161 | -6.9871 | -47.4885 | 2026-09-21 18:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 8109b72b-0962-35da-95f3-913336235641 | -9.419 | -68.7499 | 2026-09-21 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4df9fa02-812c-3f35-a8de-0d94cbd33e2f | -8.7919 | -44.2546 | 2026-09-21 18:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 6b793342-1e2b-3d51-876d-52066d0d2803 | -7.2519 | -55.5994 | 2026-09-21 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 49333200-9523-3b4e-bebb-96cec345885f | -9.6108 | -43.9477 | 2026-09-21 18:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 99081192-858e-3607-8124-6b3c310d9544 | -8.8635 | -68.8169 | 2026-09-21 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 5899e127-8a97-32da-96de-096135c0dc4f | -3.6632 | -58.8643 | 2026-09-21 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 63cccd88-77e1-304b-88eb-4f58c32c9a1f | -2.9525 | -57.72 | 2026-09-21 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 1d13d243-892a-3ea5-a93f-341234f94f12 | -5.8159 | -57.7346 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 226.9 |
| 3e870db1-8641-3458-92bb-b9835b25a91f | -6.3251 | -55.8252 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5dab65b3-1881-3ec0-805c-95aacdd40489 | -11.6798 | -43.4446 | 2026-09-21 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 7728acc9-a95c-3129-9241-7295f2dbdb1f | -4.6853 | -55.6343 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 02ce3fcc-57f0-33c0-9068-010bd92b5534 | -7.3444 | -55.6142 | 2026-09-21 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 330796cf-9a0c-305d-b805-a553a8aaf3a3 | -7.9445 | -45.6467 | 2026-09-21 18:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c76777f0-c58a-36af-afc9-d6a4713b6117 | -8.5984 | -54.6139 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 35b2f53b-b57f-3b1e-b6e1-6f6aa8556199 | -10.1622 | -68.5663 | 2026-09-21 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a2ae588d-152d-384e-83f1-c357119763f9 | -3.8957 | -60.5984 | 2026-09-21 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 7a7e2aab-d445-3aa7-bf79-e99200e5da5c | -4.2042 | -56.3412 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7f1b07ab-7705-347f-8789-8fdeb9475d28 | -8.0892 | -55.3511 | 2026-09-21 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| d3ddbc8d-47ab-3cda-9505-dc43c9aa2a5b | -11.0234 | -49.752 | 2026-09-21 18:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 1b8ba352-00d9-3260-b05b-90d9f189f73f | -12.3293 | -50.1802 | 2026-09-21 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 53a835fb-c548-3cf6-aa3f-3b3c486d869c | -9.9755 | -68.7929 | 2026-09-21 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 3cbf8db8-abc4-381a-b8fd-3196101bb57d | -9.053 | -60.5119 | 2026-09-21 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 5ef46c1e-5808-35a8-8839-0bf3eba04ee1 | -10.4764 | -69.2073 | 2026-09-21 18:30:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 070f05df-38c4-324d-bafe-9f6a3236b3c4 | -3.4578 | -60.265 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c10b4b92-aa51-3875-8642-5363ccdf6078 | -10.4288 | -50.3305 | 2026-09-21 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 39e11e89-b146-3cb4-8ea5-e13f53b1856b | -6.0127 | -47.9083 | 2026-09-21 18:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b940d353-4bd9-32ae-bbde-f973a19ea7ed | -10.7223 | -54.0008 | 2026-09-21 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c1211103-dfaf-34ee-9bb6-8b386aa5793b | -9.2383 | -46.1668 | 2026-09-21 18:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f057a943-a9c8-3655-9151-394a17ebd542 | -9.0169 | -60.3598 | 2026-09-21 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| dba963bd-640c-365b-9a41-41d44d4823f4 | -3.4599 | -59.54 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a07de4f0-115e-3de8-bbdf-11fb330a923f | -7.1273 | -48.4366 | 2026-09-21 18:30:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 205.2 |
| e8cffca5-c287-30ee-a2ca-1ab6c8f33204 | -6.7464 | -59.4223 | 2026-09-21 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 997a1e58-e590-3246-9a21-53a52b922db7 | -3.6947 | -60.5645 | 2026-09-21 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 46eedec5-3ca3-3efe-a527-dfc313a81fc4 | -3.6448 | -58.9031 | 2026-09-21 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e75d9416-6925-307f-a7db-c4e581d4be98 | -7.5661 | -61.3239 | 2026-09-21 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 369fb38b-7596-3a89-b3a6-6d405b3c74a8 | -10.3725 | -48.9153 | 2026-09-21 18:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f8e40d8c-850c-3314-a1cf-371d984ee13d | -9.0227 | -49.8262 | 2026-09-21 18:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b3d5b032-0833-3996-87f4-1cb703a97530 | -6.4671 | -59.9711 | 2026-09-21 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 0e04197c-11d3-3dbd-97ff-4028a8408df7 | -6.3436 | -55.8243 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1ca8e74b-5e8e-3b86-8de4-2c7c08d102ac | -8.1874 | -54.742 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| d53e5ae6-89f7-3d14-9490-211e33e2e327 | -3.4974 | -59.1944 | 2026-09-21 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| c04da53f-c9f4-3943-aa7f-6ddb5f4317bc | -5.6094 | -44.8446 | 2026-09-21 18:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f0ef82e7-fbb6-3492-b77b-e3ff5e05d47e | -5.9333 | -53.5362 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 193fce91-adf1-364d-8540-75fdbca29a6c | -9.6665 | -54.3332 | 2026-09-21 18:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| af8fe687-18c6-3f77-8b09-ad932d9a2e71 | -6.922 | -42.9559 | 2026-09-21 18:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.2 |
| ecb5ae3e-4a7e-3be9-88b9-9cbd8e221081 | -6.2396 | -41.6634 | 2026-09-21 18:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| e73d9237-6335-3ff2-9d37-75e6c461f38f | -4.5774 | -42.9512 | 2026-09-21 18:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 6cbff343-3020-394d-843f-0847e9996dfc | -3.6264 | -58.9036 | 2026-09-21 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 974e9d06-bedb-3688-b500-1f63c7d3fdaa | -10.8285 | -50.1386 | 2026-09-21 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 3e508c92-1ea1-37e2-867f-685f276ef066 | -9.247 | -57.1488 | 2026-09-21 18:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 18dd46cf-4898-3d79-a066-b9d1c43eb66c | -12.0645 | -50.0401 | 2026-09-21 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 31569e00-b2a7-3821-8cb4-7b29b2bc919e | -10.8469 | -50.1795 | 2026-09-21 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e5a0ab46-352a-3864-8daf-1ae8eefe3025 | -5.1838 | -49.3358 | 2026-09-21 18:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 501ca1ab-abd2-3f98-b00b-d65cecf48bfb | -8.8635 | -68.7985 | 2026-09-21 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| e8d28636-b86a-346c-8025-ca06869398c2 | -10.4285 | -50.3518 | 2026-09-21 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3f118133-eda3-3426-883f-001a08c4c11f | -6.5898 | -44.15 | 2026-09-21 18:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 304.3 |
| fa54effc-4a1e-374c-8798-a1e99d081c65 | -10.7064 | -50.7703 | 2026-09-21 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1231f259-2ac8-384e-8e83-0ea5150003d8 | -9.8683 | -48.4689 | 2026-09-21 18:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c9b28008-524b-3f70-8e85-0dc84f012ecf | -3.4599 | -59.5209 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 39a62ef9-4f44-3bec-8115-2c65cde2af88 | -6.5569 | -45.566 | 2026-09-21 18:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cabf20ac-3d30-3b1e-a050-f382a87bf6ad | -10.7248 | -50.8109 | 2026-09-21 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| f42cf923-6c02-34f2-8c92-8a6a41466939 | -11.9316 | -46.506 | 2026-09-21 18:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4bc1ca29-0a25-3f52-a04e-5d13ed1a7398 | -3.4555 | -50.5927 | 2026-09-21 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| aa134c97-e573-39cd-9d42-4434750bcb12 | -2.6002 | -59.7653 | 2026-09-21 18:30:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f5f3922f-f667-3462-9637-25a5e50ccd17 | -8.1496 | -54.8049 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2ed9b4f5-44eb-3c0a-ba99-3bea1edf655c | -12.3018 | -50.7203 | 2026-09-21 18:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 14b9ae6c-ac03-3fa3-a907-7c1bfa9f449d | -5.8876 | -52.1064 | 2026-09-21 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 66d41913-dd8c-351a-b345-bc2af044a6bc | -1.9301 | -56.587 | 2026-09-21 18:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 811ab772-8fd1-38a6-b03a-483d89159e7d | -9.6853 | -54.3318 | 2026-09-21 18:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 082a1047-5324-3458-aa60-e8d463fc15ba | -7.403 | -55.2314 | 2026-09-21 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5ad9d8ff-ac5e-38a1-a68d-a12eabdaba6c | -6.2949 | -57.7545 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| d9f597c2-d173-3dd2-9aee-27e1f870c2dc | -6.9034 | -42.9341 | 2026-09-21 18:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| f20c92a7-c50b-35f4-9d35-1fbb85397562 | -6.2766 | -57.7358 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a8f4ed9a-dc7e-30bf-8ed7-d5e0001b9cc0 | -3.5894 | -59.0581 | 2026-09-21 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |


[Clique aqui para ver as próximas entradas](README190.md)
