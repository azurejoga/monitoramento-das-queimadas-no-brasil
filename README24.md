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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95a20c7f-cef5-36f1-8cbf-64ca257429df | -6.22927 | -42.53386 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78569d70-52ae-3b0f-8fcf-7ea71844f259 | -12.12218 | -45.21934 | 2025-10-28 04:14:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf4eb9d-3e7b-3e5d-9d22-459c3327249e | -8.63522 | -47.71264 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06e315c9-8856-3aaa-83f7-368dabb18ee0 | -9.88063 | -44.88833 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f74c5f50-d71c-31f4-9972-c0645ba4559e | -6.42413 | -42.32978 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 41b212f6-7b33-3a5f-a424-92bb90c92b66 | -10.56242 | -49.77545 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9ba33a3-b650-367d-afb4-b2adb2cbc79c | -11.06544 | -45.22895 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c075859-f666-32e7-8416-0b438ae14bb0 | -12.69604 | -46.31892 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4beac6db-165a-3e30-9cde-f280f2c37971 | -7.94577 | -45.48473 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca1327e3-caca-3050-9602-2950be3f0ce9 | -9.86999 | -47.46403 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 497ffb3d-0c4b-308a-a4d1-110f2eed6f24 | -12.08719 | -45.67131 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 452b6cc9-1d31-3947-9b1b-179db0d3ea28 | -7.97821 | -46.75208 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5eee55d3-ea08-38f9-8cde-8c806425054d | -9.96371 | -47.10324 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c280468-08b8-38c6-af49-140b776ad364 | -13.03814 | -45.85552 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52b0feaa-97d5-384b-b356-f7ecaa80cc3c | -6.24159 | -44.65486 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7999453f-14f2-3cd4-bc83-0d71bc9c06f8 | -6.22044 | -42.5254 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f21b6cc1-a2a8-33d0-b93b-c41b89ab8d89 | -7.47238 | -47.15585 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0669c88d-8b05-35ac-8bb1-b50db35aa260 | -5.36586 | -46.96947 | 2025-10-28 04:14:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab5e4840-a2b6-362e-ad27-c4dbaa357b42 | -10.91566 | -48.00879 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f32c4d4-037b-3144-b4a2-cd5766cdfa9f | -7.43318 | -47.20595 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e037772f-ecee-3654-ae01-0247fb2e4d6d | -6.88812 | -45.0286 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7618747a-3bbf-3adf-96f9-70b25e48bf0b | -7.83921 | -46.40631 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| acd2c4d8-95a4-3625-9987-5cc1a0fd5ece | -11.02827 | -44.65099 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33c6407b-ce0f-33b7-af0f-151d515d0352 | -9.87364 | -47.45829 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ded48972-5389-3c5a-b232-5e209693f265 | -8.70662 | -47.9792 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24d03691-9c91-3617-b6c4-2d5e818725fa | -7.97528 | -46.74714 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 87e9c320-ce48-315f-a5cd-1d328a3bd336 | -6.13729 | -44.58199 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77315690-5120-38a3-ad55-d94801a1a3a3 | -13.54173 | -44.13429 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b641818b-f4bc-3743-a5ac-75b7c215ca9d | -7.97891 | -46.7478 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47e9b095-7a02-33c6-a27c-e2bb5d812312 | -7.23209 | -44.98868 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c35cf26-bbba-3eb2-ae41-24be99e24201 | -7.98092 | -46.7129 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d649171-8694-3319-af7e-1649fc7f0297 | -7.29686 | -45.0634 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6217b37d-d7c1-367a-a025-f3676b53169e | -12.05172 | -46.47323 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d0ed1a3-7a82-3670-b5a7-3a6c880f8285 | -9.27839 | -43.11799 | 2025-10-28 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 267b4dbb-ed0f-3f69-b405-f26356278517 | -8.49841 | -48.27871 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6e08a413-e0ad-39d2-b031-c671fb9dea99 | -10.52628 | -44.9171 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ca30ecd-c95e-3ea0-ac05-a3b0dc90ae06 | -7.08103 | -44.94144 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a9da63e4-c799-3f39-a750-223c832f0e15 | -7.30971 | -44.10351 | 2025-10-28 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff7263b7-cb90-3ba9-a904-5e5e15e8bdbb | -7.95743 | -45.52172 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad44416c-e689-396b-989d-9225971ca960 | -9.53931 | -46.9456 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8131d14-2307-3b09-b849-3471b66857b6 | -7.09301 | -47.26397 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58e72892-4948-3b14-b5f5-38e93c5d579c | -7.81399 | -46.47066 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 841bc08b-3948-3a5e-ab54-19d0480e43fc | -6.58974 | -42.68593 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae73aa1c-b276-39d0-aa3c-a5b0b076d60b | -12.04832 | -46.4724 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2de0ee78-dc31-3b12-848c-1302289ecfbd | -13.22382 | -43.52457 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 336f2789-3f94-3e90-9316-05f25ab03c03 | -9.26917 | -46.27496 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a55e9eb-461f-3b92-a4c8-7b8496b3fdf9 | -7.62385 | -46.6932 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdd0d575-5a72-3606-a236-ca6053a2dfee | -12.95987 | -44.61786 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a17d5998-6d64-355a-990e-f3c96b2f8b8b | -9.58818 | -49.67445 | 2025-10-28 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faf5aea3-f33b-349a-adf7-cb69552f9f9b | -7.95583 | -45.50981 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a1080c9-3cc6-34bd-95bd-df8747dff734 | -7.84906 | -46.39093 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b7f8a68-39aa-31e6-9fe6-19a130b57fd1 | -8.16526 | -47.00741 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5ccb523-55be-3907-a720-dee02ba31e3b | -7.95424 | -45.49781 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e812b324-688a-302d-898e-09e220afd135 | -9.95143 | -47.10987 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38df8470-fee1-3b24-ae8a-663e8ffc2e57 | -5.66844 | -47.82407 | 2025-10-28 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76b380ea-9d02-3383-a5fa-d17321365978 | -7.27451 | -45.00678 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0366083c-7dc3-338e-a20a-e3c21ae8a351 | -12.09013 | -45.65311 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fff0e899-ec6e-3eab-aed8-ae2b7df3ed08 | -11.14986 | -44.63513 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7eb2e29-c903-30e6-8d5d-badfdf78e33d | -12.87287 | -44.5858 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0180b7f3-49aa-35a9-9ba1-bf97d66c60d0 | -6.61239 | -42.05917 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2245b6f-9b70-3e7b-b185-53458d3cd59d | -11.1614 | -44.66946 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2faa4449-579a-326b-8f8a-1bb644421c7c | -12.70347 | -46.3163 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30cfb54d-2855-33b1-9b6b-b8e505a6e636 | -7.47704 | -42.95388 | 2025-10-28 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca441e01-dcde-36d4-bec2-84213990309d | -6.28998 | -42.86449 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8900f1d6-e0fe-3445-bc00-107b0bada34c | -7.89658 | -45.69965 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aa38e98-6944-3bb6-8e74-5f0d19634f14 | -7.85263 | -46.39159 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6fa5c04-de1b-312b-af26-ca151a2a8f75 | -10.58209 | -49.7626 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f9f321fc-d363-3022-86e3-5e6a1a724819 | -7.97749 | -45.52882 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f483197-a6c4-3266-9e8e-932d05289c52 | -9.52116 | -40.31453 | 2025-10-28 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 39b3ce38-0b70-3a38-8efe-5a6b7586daf9 | -6.87724 | -43.58742 | 2025-10-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f69d6bd-edc9-3fde-9dc6-11415a8d0037 | -7.78865 | -46.44513 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6811a5f0-ebe1-347d-b4a1-cb116f7e32f2 | -7.27791 | -45.00732 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80889733-5cd0-3698-bbfc-19dee1e41c07 | -10.36365 | -47.16222 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60565773-a628-3441-9597-20bf9e6f4c59 | -7.98897 | -45.95473 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b672584-058f-3f7b-8bce-66c1f7fd9922 | -7.03202 | -47.62724 | 2025-10-28 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82723295-d741-3cd4-b94e-1c8553443c28 | -6.82682 | -41.20206 | 2025-10-28 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8356815c-ea19-362a-a1ad-3900d6d58f11 | -7.25506 | -46.8091 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87a3a222-e7c8-3676-8b43-d23498c97f8f | -7.95706 | -45.50221 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02a2446e-e4a1-360c-8007-80a3a471c6e7 | -12.61882 | -44.25254 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a75835e3-a399-3c3f-a685-c2826a6243e0 | -13.377 | -43.45692 | 2025-10-28 04:14:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48527c9e-02d0-3aea-924b-5f93ae26978e | -7.00039 | -46.99783 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1221a903-4924-3511-a6e3-11ba3e5de2b1 | -7.76592 | -45.40231 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1e2840e-58e4-388f-84be-95f4f082ec1d | -7.53686 | -46.76476 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbbd9f59-d61a-33b6-8a6b-911853e86fb9 | -9.03996 | -46.94085 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb3623c8-3338-31de-b7a5-bf4added7d61 | -7.25869 | -44.99672 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b411fa3f-9b26-3a9b-8943-5a0e89a9c42c | -12.62111 | -45.07931 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ae512b1-4c0e-3ee0-a811-211c6c21a081 | -12.91065 | -45.0363 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 158d65ca-d0e4-3870-ad00-b4cf33125d90 | -7.98325 | -46.74414 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b307972-e93e-3d54-9e18-5206c7df543c | -8.63943 | -45.28131 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0790a446-e22f-3200-b819-ea7ae2e05885 | -7.2275 | -44.99551 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fa7e904-006b-394a-908a-96579c20f1d2 | -11.10275 | -44.02807 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07b8b250-b992-3111-a054-84b6a771930f | -5.60668 | -47.10843 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2a4035c-e009-3a6d-8627-f50288c0f0d9 | -9.0435 | -46.91943 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09d70050-217a-302f-befa-ea9982e65a17 | -5.29891 | -48.6984 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 324a2b8c-28df-3194-a502-719092e27fcb | -10.35262 | -48.04713 | 2025-10-28 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9c60794-5970-373c-9ed8-651bf7b2e260 | -8.50669 | -45.73456 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfe9099d-017c-3248-8bbf-551e1b5a6d9e | -7.99028 | -46.19152 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 369854bb-343e-324e-93fa-41677fb67e0f | -10.91193 | -48.008 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14b13c05-032c-3bff-b2d0-503cb84ee57b | -6.26453 | -42.71944 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d7c2913-9118-3f80-bb21-a6cc22d6da25 | -6.59305 | -42.68644 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
