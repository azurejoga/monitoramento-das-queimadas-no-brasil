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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b80f6c7-5da7-3a10-a2ce-e791514b77a2 | -5.53652 | -42.85386 | 2024-12-14 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 702ebb61-55f9-37a3-846f-1073dde1afce | -3.29259 | -42.52115 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9055479b-e6e8-39fc-8456-22fa25e6f258 | -3.62732 | -46.7114 | 2024-12-14 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b47d7c68-7618-32ba-b519-976c22df144d | -4.17277 | -42.43317 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b65213b1-3db8-3d71-9ad5-e5e617539e88 | -3.28828 | -42.52478 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70e3fd56-70fe-3584-b2e4-7541faabca03 | -1.33109 | -45.31164 | 2024-12-14 03:59:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d96e50c2-70d7-302d-957e-d3bdb673bb5c | -3.68931 | -42.60506 | 2024-12-14 03:59:00 | NPP-375D | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2db4ea86-f1ae-392e-a8ad-e8e5391d34cf | -3.32899 | -46.8259 | 2024-12-14 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0304326a-117d-33d7-81fa-97b2193d1599 | -5.64966 | -37.25809 | 2024-12-14 03:59:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a6b534e7-7e90-3fc3-b9aa-851269b9a18d | -4.72376 | -43.19395 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7db14c31-c63b-36b0-b50a-9925a9f5806b | -3.29985 | -42.52045 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d876b1c3-3c17-3973-85fb-29414d57816e | -6.51473 | -41.28379 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f69c153-9c81-3d55-bdbb-81316f4074a1 | -4.10229 | -46.67213 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108839e4-5cfb-34ec-ad58-77d8cd2933a1 | -6.45258 | -39.70311 | 2024-12-14 03:59:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6b3042e-2b00-3b82-a3f9-0e9b44b66036 | -5.04443 | -43.21524 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feee4e3c-a8b0-3a91-a519-36226444aa57 | -6.51416 | -41.28738 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f84f8042-3315-3d28-a581-d876502e4bb4 | -3.29257 | -42.5193 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa35ae7c-2fe7-3ce2-8690-8b3c7f1846a1 | -6.45312 | -39.69963 | 2024-12-14 03:59:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f8ab6664-7186-3723-b632-ab64770d708d | -3.30054 | -42.51812 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a72fd35-f3b7-31e3-9f03-573c4410422d | -2.88853 | -44.36953 | 2024-12-14 03:59:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63867d84-5d4c-32c3-935f-bf07ed7f4531 | -3.30715 | -40.55219 | 2024-12-14 03:59:00 | NPP-375D | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9b52046-6002-37bf-b731-36bfb77c63f5 | -2.96112 | -39.96317 | 2024-12-14 03:59:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b9e40be6-68f0-386c-b3ce-55559131d263 | -4.10263 | -46.61176 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 445ee532-a332-3d2e-8695-d3448dd36761 | -6.52204 | -41.28127 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f3029047-6f56-3fee-b913-2e3583649465 | -5.43131 | -37.84877 | 2024-12-14 03:59:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01596ef2-ec3e-3ac2-a015-fa3e8b003b9e | -4.41522 | -45.82999 | 2024-12-14 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48fc9883-6253-3596-be81-ca802d4f95ed | -6.62336 | -39.17875 | 2024-12-14 03:59:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9208db31-a0e4-32ae-bd61-8552dd617634 | -3.46037 | -40.81539 | 2024-12-14 03:59:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cec11cbd-d20a-3907-af13-18de9c8eceef | -4.67292 | -42.7317 | 2024-12-14 03:59:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38d9796d-b507-313c-8794-02bf790896bd | -4.93931 | -44.06809 | 2024-12-14 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e220eb1e-71de-36ed-9509-0f3701a75d07 | -5.50778 | -45.49062 | 2024-12-14 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f750fa96-4d42-3394-a947-f23b4c36e1b3 | -4.72304 | -43.19835 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee0533ff-7722-3b8d-8c20-d68b2b9ee660 | -5.69157 | -44.95117 | 2024-12-14 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80891a9e-15e6-3e61-ba09-461c7dd7de3e | -4.24651 | -41.92245 | 2024-12-14 03:59:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7be9e05a-9278-391f-b99a-e296ec696846 | -6.51135 | -41.28326 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f2999e85-e885-33cd-a455-07d7311d3b40 | -6.92328 | -35.71731 | 2024-12-14 03:59:00 | NPP-375D | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d263280-6e7e-3da3-8dcc-30578bb11291 | -4.4081 | -45.8433 | 2024-12-14 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0741dd98-0e57-3b82-b0bd-1a7471d1af5f | -4.1057 | -46.6142 | 2024-12-14 04:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 6aa6dd03-3e2e-3cf9-b8ec-e62a078974ca | -12.5499 | -57.6996 | 2024-12-14 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 57f83c15-ea47-3f22-9f20-80e2fcf02615 | -12.5497 | -57.7196 | 2024-12-14 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 04059be7-b48c-3939-975c-c40300d4e29e | -4.4269 | -45.8199 | 2024-12-14 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b22396e4-6550-3447-8aa0-64ee4005eb42 | -4.4082 | -45.8209 | 2024-12-14 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d2ab3953-3651-3851-9324-4b68d1dccdd0 | -8.93936 | -44.247 | 2024-12-14 04:01:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ed3580b-eb09-36d9-b2cf-e78472979458 | -7.99451 | -39.43044 | 2024-12-14 04:01:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c219aca-0f73-3fd1-97f6-7b2ab4f8f017 | -9.04493 | -35.34869 | 2024-12-14 04:01:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7a9d415e-3006-3206-b3ae-7a1d0dc62125 | -6.02444 | -45.81097 | 2024-12-14 04:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b35c86d-cbe3-3c01-9894-d061b5a074e9 | -6.93134 | -42.84782 | 2024-12-14 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c6a406e-5d9c-3f7a-b2ad-8ee3ac545837 | -7.69929 | -37.5369 | 2024-12-14 04:01:00 | NPP-375D | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22bba0b1-5dc2-3a12-af87-0f74d30bad8e | -6.73499 | -42.52996 | 2024-12-14 04:01:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c5b6b4b2-413a-30c6-8c5b-1939c8fdda27 | -7.89073 | -42.44114 | 2024-12-14 04:01:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7bbc853d-5c5f-3d8d-b7ad-7b8290e7c5b2 | -9.48982 | -35.61272 | 2024-12-14 04:01:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62b8db14-e61d-304b-acc0-fbb9e5ec7b7b | -7.99561 | -39.42339 | 2024-12-14 04:01:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c9bdb2ef-04a2-3854-b516-bf8e26f9fdca | -7.92677 | -35.26461 | 2024-12-14 04:01:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c062eaae-98df-3f88-8bc7-39ba02b1d741 | -9.21616 | -36.45708 | 2024-12-14 04:01:00 | NPP-375D | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ce867b98-bed3-3ef7-a7f9-8a738d04483c | -6.01585 | -45.80963 | 2024-12-14 04:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7f1643d-d178-3d86-bc02-4f42603f6ab0 | -7.89011 | -42.44494 | 2024-12-14 04:01:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9d549fd7-3768-374f-9fbd-22aef0d8a30c | -10.17845 | -37.21766 | 2024-12-14 04:01:00 | NPP-375D | GRACHO CARDOSO | SERGIPE | Brasil | 2802601 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2c9f3e8c-c284-3201-9d9b-50f4ab502aae | -6.02015 | -45.81028 | 2024-12-14 04:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d037cfa-8aa2-3c14-8088-e84a98c97135 | -10.24753 | -39.37195 | 2024-12-14 04:01:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ca2d5211-f5ac-3891-86ac-de6f2b637945 | -7.38346 | -38.73905 | 2024-12-14 04:01:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0902df5-039a-3515-b038-66f9dd0a4c41 | -8.94309 | -44.24762 | 2024-12-14 04:01:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0dfe61bc-bb80-3ba2-bd78-1f4cfc47494b | -9.00638 | -35.23741 | 2024-12-14 04:01:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c4767b03-292a-33f7-b3e8-9b7044790cce | -10.25092 | -39.37246 | 2024-12-14 04:01:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fd4a76c8-b44c-3766-8b3d-bdf833f7f24c | -10.69433 | -37.04992 | 2024-12-14 04:01:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 60cbe36a-3f19-3e25-936c-b51b0041baa5 | -9.81745 | -39.14916 | 2024-12-14 04:01:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b0785af3-6d06-3785-8f4d-782e3d28e29b | -9.28152 | -40.17352 | 2024-12-14 04:01:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8d4d8c6c-9ec4-3e5d-afc0-1a02bd1212db | -8.2139 | -40.60006 | 2024-12-14 04:01:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8e28e4c-b89d-39dd-8530-ad9db28bdf1f | -7.99896 | -39.42391 | 2024-12-14 04:01:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be340277-d0f6-3588-9c75-74b709904519 | -8.93564 | -44.24638 | 2024-12-14 04:01:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69620aed-2bf6-3836-96a1-588f80e1ffc9 | -7.92324 | -35.26037 | 2024-12-14 04:01:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 47afd48b-f918-329a-8e1e-a3367e721046 | -7.38741 | -38.73595 | 2024-12-14 04:01:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1495a4f0-79ad-30ba-b094-1ad893706641 | -11.80207 | -37.97228 | 2024-12-14 04:01:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8574d90-f23a-31da-bcc7-e9408d90ad69 | -9.28097 | -40.17702 | 2024-12-14 04:01:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2203e2c-d905-33f8-9601-158c134dbca3 | -9.81689 | -39.15285 | 2024-12-14 04:01:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8857d2b-5848-3562-ae6c-da905780ad02 | -7.99786 | -39.43096 | 2024-12-14 04:01:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b9536900-bce9-32c9-bb77-f718899dc622 | -10.00629 | -37.6881 | 2024-12-14 04:01:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc93cf09-99c0-3e3c-b616-19d92c6e19c6 | -6.92779 | -42.84724 | 2024-12-14 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f093b3e-c5d6-348d-9f38-d70cee06e685 | -11.49902 | -39.04762 | 2024-12-14 04:01:00 | NPP-375D | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e352e58-bdfc-35f7-b0fb-dd58773f7dff | -7.93289 | -35.25094 | 2024-12-14 04:01:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 819477ad-0a64-3edb-8801-92b5984cb756 | -9.25982 | -40.95473 | 2024-12-14 04:01:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 281f2dc2-8f59-36e6-a3c0-31b5b76098a0 | -9.69512 | -36.17785 | 2024-12-14 04:01:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 63f5e6dc-1167-325a-9ba9-a2a83f98b06b | -9.21418 | -36.45443 | 2024-12-14 04:01:00 | NPP-375D | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 778a03e6-9d5a-3144-8416-189088d73ba1 | -7.99506 | -39.42691 | 2024-12-14 04:01:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6528d637-7f64-3963-9269-6987953fbdae | -7.99841 | -39.42743 | 2024-12-14 04:01:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7662cf05-6738-33ba-b26e-00d60ddc8e80 | -10.59128 | -40.21596 | 2024-12-14 04:01:00 | NPP-375D | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e062c37-f6da-3caf-a5bc-b5525eb3da54 | -13.94704 | -44.19968 | 2024-12-14 04:01:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef88d5cb-0bfa-375e-a35e-9bd9f7270f96 | -9.25927 | -40.95824 | 2024-12-14 04:01:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7b22157-6e15-365e-9b83-e929b5dd496e | -7.88727 | -42.44055 | 2024-12-14 04:01:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3a8f0f48-347a-3a6f-bda9-100710de4e07 | -9.3892 | -40.52016 | 2024-12-14 04:01:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d9827d8e-8075-3ab3-ae26-31510c4912b5 | -7.44201 | -38.97359 | 2024-12-14 04:01:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0278250c-e026-3fb6-b1f5-ac28cfe07c37 | -9.04083 | -35.34807 | 2024-12-14 04:01:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ee00eef9-ddd3-3f02-892d-214563951580 | -6.93201 | -42.8438 | 2024-12-14 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d835ebb5-d9e2-304b-9eec-478206e0c6f9 | -9.27765 | -40.17649 | 2024-12-14 04:01:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 283c53b8-a66b-3abb-a01a-03cb57e42be0 | -8.35257 | -43.82109 | 2024-12-14 04:01:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17753ae9-4cca-343f-a68f-b5be4ce8578c | -8.21723 | -40.60059 | 2024-12-14 04:01:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b509486e-3f10-3db0-a5db-92252faa7e12 | -7.7749 | -35.23107 | 2024-12-14 04:01:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca80bd37-2599-3496-9a60-371c8fcf3700 | -9.21231 | -36.4566 | 2024-12-14 04:01:00 | NPP-375D | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bbbee45f-1349-3330-9ef1-168deccc9263 | -9.27819 | -40.17299 | 2024-12-14 04:01:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 139ee345-d386-3ab7-b989-b00202c91de7 | -17.967 | -44.93037 | 2024-12-14 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3c705a7-1762-3565-8250-288559fdafbc | -15.06724 | -42.33541 | 2024-12-14 04:04:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
