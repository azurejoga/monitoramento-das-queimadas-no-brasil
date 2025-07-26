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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3b1ff49-66b1-3c06-b446-288cb4025c0a | -10.62446 | -44.76632 | 2025-07-26 04:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4690e86-68b5-3751-a66e-d7a6bbfe86fb | -13.11679 | -47.3342 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b379ee06-b0f0-3d1b-b007-3b4f82269dc7 | -13.64119 | -45.70031 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b0395c-0736-391f-86b6-6b369e2b5c81 | -6.98615 | -47.08142 | 2025-07-26 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aeaa73c-94ba-3c1d-9c37-5a17fe195051 | -14.13679 | -45.28382 | 2025-07-26 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7a2e6d3-132d-3a5e-85a8-ee439e8c03a3 | -13.09516 | -47.34034 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f9a296f-355d-336a-b20d-d61a2d5b04bf | -13.10911 | -47.32836 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2b91937-9423-3bbb-a4a6-89414fa9c151 | -13.11535 | -47.34198 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 02af382e-1edc-3e49-afdd-8d44cc7e1ae9 | -8.06095 | -43.13054 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44cee56c-d0da-3cf8-86e1-51da86a36ed4 | -13.11645 | -47.34377 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2caa566-71ef-3534-9717-21e9a51138e9 | -13.23972 | -51.15006 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53e074db-e0ba-35e2-bdd6-0d670ac7ad10 | -13.09584 | -47.33654 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b742499f-2b5d-3dfa-9f63-f4f714a6dcc8 | -9.13972 | -45.86897 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60b9ab12-783a-3671-a246-f1208ed152cb | -8.38338 | -44.60583 | 2025-07-26 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 460924f1-1c13-3398-b15d-f548fcaee393 | -7.09834 | -44.87819 | 2025-07-26 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12857c79-3b2a-3dea-8e51-b6f417dc2ca5 | -12.72425 | -41.80756 | 2025-07-26 04:04:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 57fe9cb1-ac0b-3e68-99d8-a7b714c10265 | -10.66443 | -46.6372 | 2025-07-26 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 458ce225-fadd-3c10-a6e5-64bc9e3ec86b | -13.64307 | -43.8032 | 2025-07-26 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20a8e179-37a8-31bf-8a44-eb05c71a119b | -9.73708 | -48.01945 | 2025-07-26 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69835b4d-93ff-34fc-bc2c-e7e3185aaec1 | -12.43488 | -45.38036 | 2025-07-26 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0a31357-7e11-3aca-99b1-9826bfaeecb1 | -10.50113 | -44.88089 | 2025-07-26 04:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d02c9e6e-ebec-3e86-ae19-0ef4274fef3b | -12.70329 | -47.01043 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc5ad96e-ae44-32ba-abf2-c5249b6244a3 | -8.81287 | -46.75609 | 2025-07-26 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34d46ae0-d479-345d-b67b-3b44c7dc4b0f | -9.25544 | -50.2245 | 2025-07-26 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92085550-3d42-3723-b100-ab4ebc9987b9 | -11.59549 | -43.2064 | 2025-07-26 04:04:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9ca99e2-e2e3-311c-b5de-60288a86b87d | -12.04531 | -45.43539 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd93fb3b-5408-3652-8ce1-5e2516967db0 | -6.98889 | -47.08423 | 2025-07-26 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54d7c3d7-bc4b-3a57-b4bf-c22cdfe8ef06 | -12.29969 | -40.08669 | 2025-07-26 04:04:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36c3b954-c9c3-3367-9160-e38e3447a028 | -13.1146 | -47.34607 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5adc12f2-a214-395c-92be-0ce880fb5a59 | -13.50156 | -45.48172 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42ba79a2-e599-34fd-a0b0-224c450dd60c | -13.11328 | -47.32948 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9076be7e-d156-351b-84a0-d114247fd9fd | -9.13022 | -45.87505 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea04607b-c3a2-34a6-b8fb-df29adb5a123 | -12.2562 | -44.78324 | 2025-07-26 04:04:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d8b9070-3249-3376-8ceb-daf6b541ca55 | -10.61771 | -44.76041 | 2025-07-26 04:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6f4e682-4a5f-326f-b32f-1479e17534cf | -13.69254 | -45.67536 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3083bb3f-bb11-32b2-85a5-9c4717727f03 | -13.1185 | -47.33221 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fdd7ee1-d805-3c31-a9b9-d5cf6c44901f | -11.92688 | -44.5487 | 2025-07-26 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77e214da-8f9f-3bda-9c1d-6e56ca5ee66c | -9.35643 | -40.31225 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| cc63f37c-f92b-3a7b-9c76-4c3d5fd30dca | -12.04829 | -45.4409 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a412caac-d7b2-3650-b6f3-86034104a1db | -7.46096 | -49.39461 | 2025-07-26 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3436a48-7a00-399e-8480-3450a2b8a3e6 | -12.70062 | -47.00119 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29d095d8-6407-3113-a7b3-48cbf5b7a704 | -8.81878 | -46.74818 | 2025-07-26 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a79cbc1-3b5e-394b-add0-17812a9dd16e | -9.35975 | -40.31278 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 11fcb867-95e9-3041-b737-4b8b2933f532 | -13.22345 | -51.14663 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d832354c-1b08-3671-97fd-98614ecfb515 | -6.01118 | -52.17315 | 2025-07-26 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b95c4563-d1b7-3e8c-8e0c-d67eaa9455a4 | -8.28787 | -45.00248 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 797e5c64-cd92-37af-9f56-cdd76587d3b9 | -13.11426 | -47.35619 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e56e9084-a15d-38c4-b9a4-5ddb6d57c87f | -6.98995 | -47.08712 | 2025-07-26 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7277908-893b-3feb-aaba-cbf1dfef56c1 | -7.0975 | -44.88319 | 2025-07-26 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42adba70-1b41-3e13-ac3c-564c35498fb0 | -13.17906 | -42.32617 | 2025-07-26 04:04:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 079df53e-a671-3135-aa4a-e40dceea1f5b | -9.14635 | -45.86944 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edee8c6a-7cd9-31a3-8819-abf3d1ed33a6 | -9.02081 | -45.35082 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c7ed28d-0ed5-301f-8f72-f169867c3a62 | -7.99933 | -45.04321 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c9d98cd-c6f8-3771-81b7-b3260145b954 | -13.69551 | -45.68079 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a48e2ab-c883-39ad-ac63-3387fbff1995 | -11.1124 | -45.12082 | 2025-07-26 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0addc8a-2d68-3be0-814a-5dc2e521ec65 | -8.81439 | -46.74744 | 2025-07-26 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dca5146-4d37-3c07-92ca-86edad91cdec | -11.45659 | -45.19332 | 2025-07-26 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f26a2cd2-e6ac-337d-af87-f93dbac8738c | -9.58393 | -43.86148 | 2025-07-26 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d1f7038-aeed-346e-837f-751b992b9989 | -13.72351 | -45.69411 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 55a158d9-1afc-39bc-b87b-5a561490eabb | -10.36042 | -46.64465 | 2025-07-26 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b055fac-7ea1-37e1-9b34-0227bc2d6bfc | -8.00151 | -45.04169 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f35c1b9-f1c9-3559-b283-aec9522dd2b6 | -9.47332 | -40.36674 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce301bcd-9d93-3b38-987b-3447ea3e9553 | -13.10715 | -47.36264 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea39b27c-605e-3b80-80c7-34b886e42d55 | -13.69848 | -45.68621 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60545d09-394f-3141-9eba-57e2b4a01645 | -9.59778 | -43.86802 | 2025-07-26 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c9ef536-cc3b-3cb4-9897-99fef53dcdd9 | -10.35103 | -46.64828 | 2025-07-26 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79a1d869-23c9-34fb-bffd-ad9d2f0735fe | -13.2343 | -51.14892 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e0d1c2f-6aff-3a46-b73a-bb109c4f8438 | -7.55683 | -43.89649 | 2025-07-26 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5980ea20-8755-30b0-8b72-60a1b64797b8 | -9.1356 | -40.55563 | 2025-07-26 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be860f25-adb6-3f89-b1d4-15e7a155be91 | -13.64034 | -45.70508 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3c4dcc-716c-3642-b084-a7a815297870 | -7.56889 | -44.4879 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73d36517-04db-34c0-9003-4260e781996c | -13.64415 | -45.70575 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20f932d7-9c85-36c1-bea9-dd759c197323 | -8.17263 | -43.22348 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0581dce6-fc21-3f34-965e-c8b40423b36d | -15.18663 | -40.54506 | 2025-07-26 04:04:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b5def9a1-d8b1-369e-8ddf-84df8bda8184 | -13.11222 | -47.34293 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16f3c34d-6f7f-3c30-98e0-8781d3378776 | -9.02201 | -42.70425 | 2025-07-26 04:04:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49532d4c-4da7-3f55-b81f-d560b6f5ff5d | -11.10988 | -45.12325 | 2025-07-26 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 128348a7-4fb1-38de-8826-aba3403ecd47 | -13.2336 | -51.1525 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce2521eb-a274-33fc-8c78-efc8cc0d2f85 | -13.69684 | -45.69569 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0c2127a-9c89-3453-b18f-b8339ff97984 | -13.11787 | -47.33578 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca19cf71-d2b1-3e46-ad5e-458aab93954c | -11.92323 | -44.54805 | 2025-07-26 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14297aac-0fa0-30f0-aa16-876bc7f81b27 | -13.12229 | -47.3281 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09842c60-6a72-3624-b3fa-f4c9139f9ba4 | -9.46668 | -40.36568 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62c966f2-d05f-36c3-9d46-8ff78fd2cf33 | -12.71208 | -46.27647 | 2025-07-26 04:04:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e2b5d43-a514-311d-bc8a-7eb17394595e | -9.02265 | -45.35385 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f77cd5-22bf-3c74-bfd4-5970930d61a4 | -12.68809 | -46.99889 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 303c24ff-66a0-3cfa-80e6-ae9ee74ddf46 | -7.09123 | -44.87175 | 2025-07-26 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 619fe7db-afa7-3c6a-bbd0-c7d1a05060d3 | -9.36362 | -40.30981 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d2efdb58-6a88-3c3f-94fa-4c068471e621 | -10.59372 | -44.74211 | 2025-07-26 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ef2d41d-f3be-3681-a714-4ed379a95668 | -13.12584 | -47.33266 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8289731f-3de4-3910-93d6-11bc4ef5d453 | -8.87145 | -45.58369 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d608f01-805f-3a65-abb6-ba4d3e932eef | -8.38249 | -44.60375 | 2025-07-26 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3d6f3b1-0f33-3d5f-9a28-5220b929442c | -9.8121 | -46.7108 | 2025-07-26 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4da3c90e-2db6-359e-8a57-1fc6c5f99301 | -9.13085 | -45.8713 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8feefd5-22e4-3117-91c7-ae5e8d2b3a1f | -11.74348 | -48.18782 | 2025-07-26 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3871a412-3976-30ec-bc6b-296ba8481d51 | -9.36639 | -40.31384 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 57f63090-e53b-3bc8-854e-4e3ac435a4c9 | -11.73975 | -48.18222 | 2025-07-26 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8fe5ebdd-84b8-3408-95aa-f9d10f48f80b | -13.10413 | -47.36389 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51c62223-19f0-3ecb-9133-7c5f6595a240 | -13.10997 | -47.35565 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeabcaf9-6bf6-32e7-b36a-30b888a57d0a | -13.7149 | -40.47263 | 2025-07-26 04:04:00 | NPP-375D | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
