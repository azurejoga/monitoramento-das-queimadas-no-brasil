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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34d7bc0c-eecb-3c76-b376-9b1a7c7ceb63 | -8.7729 | -44.2568 | 2026-09-21 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| b779e803-c374-310a-9c74-2b380abd0d35 | -6.5759 | -45.5419 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| f05e9e91-4365-3fbd-93bf-d8eda23dc433 | -7.4092 | -44.7885 | 2026-09-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 824c4b85-b396-3454-8941-94e4c4afcf0a | -8.1872 | -54.7622 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a19c2783-af24-32ee-9d3e-0bce55873103 | -9.2567 | -46.2098 | 2026-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 01a815ad-189d-3691-9e04-3425ed76d8ab | -7.3259 | -55.6153 | 2026-09-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0d691792-9c45-3b69-9ee3-7e58ee01b9a5 | -13.3443 | -51.2973 | 2026-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| cb7a0058-7860-3216-977b-e81f58083353 | -3.2189 | -60.8011 | 2026-09-21 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 815f1c04-c968-3c0f-8610-525b82d4eeb7 | -10.7655 | -50.5939 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4c0c2184-a6d5-32a7-b6e2-3103be804a2f | -10.279 | -50.2391 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8cb2f30c-ebcf-36f8-bf35-f169ef38c9db | -3.4599 | -59.54 | 2026-09-21 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| bf7b1801-0923-3899-a412-f77e3933134e | -2.4636 | -49.2301 | 2026-09-21 14:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 8a2aaccb-dcf4-35b0-bc1b-decb68895470 | -6.4671 | -59.9711 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| a677d3e5-d5e6-359c-bc21-58d221290a3f | -6.5634 | -44.9084 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| a609cf7a-7135-3787-8343-a2e41ddc7107 | -11.3422 | -51.3394 | 2026-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 09fbb23f-3c14-3cef-94a4-71ed18e893e8 | -5.6594 | -43.4139 | 2026-09-21 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a5e0e134-808d-3d5f-bfcc-e8b042ec5316 | -4.4112 | -55.2466 | 2026-09-21 14:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8c91bc2d-95a5-396e-b63c-0cdb01ba2831 | -9.247 | -57.1488 | 2026-09-21 14:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| adc36b65-6ec5-3dfb-8699-4b04a2de53b0 | -3.4554 | -50.6136 | 2026-09-21 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 85759e12-1d7a-3b42-942b-51606a9594ed | -6.467 | -59.9902 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 264a3640-e523-3d29-9711-e2c64cb8c87c | -12.3018 | -50.7203 | 2026-09-21 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| cf04ac56-6dc0-3009-b3bc-ea72910af2e2 | -11.8168 | -50.0482 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6cba457c-facc-3e3f-a92b-c5e377abfc21 | -10.3917 | -48.8915 | 2026-09-21 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 6d192c1c-2ebd-3c75-8674-9d614b5064c7 | -13.0678 | -50.6256 | 2026-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b2cc537a-fec7-31da-9d3d-3f4537795aaa | -6.0196 | -51.7893 | 2026-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a177e084-d00b-3240-8906-ad2697de6759 | -5.6221 | -43.3934 | 2026-09-21 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 425.0 |
| 992214a3-e0b6-31bb-a294-7755a347fa6a | -8.3167 | -45.9934 | 2026-09-21 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| a43f5554-5b40-323a-a3c4-e3514bee5e94 | -10.4099 | -50.3324 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a557bc16-40a6-3784-bffc-e65b489093b9 | -6.3918 | -45.2175 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 71b49114-da4c-39b3-ad82-5014de2a4484 | -6.3196 | -59.9956 | 2026-09-21 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 735e7e65-1698-3404-8f5a-3add82532e5b | -8.1686 | -54.7634 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4ac1888b-9506-3e69-bb4f-dd3c7f443f68 | -10.4288 | -50.3305 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 697c983e-2e4a-37f5-bc27-405117d8f350 | -5.9985 | -45.2476 | 2026-09-21 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d995b0c9-7d69-363f-addb-c6f3a4a6a947 | -5.6223 | -43.3701 | 2026-09-21 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 14bf75ec-6856-314d-b5b4-81bcdfb7ae47 | -10.8853 | -51.5347 | 2026-09-21 14:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 9b099f31-42b3-37be-a3a9-d07b6bb6897b | -9.2796 | -45.9143 | 2026-09-21 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6ff37be1-b3e3-3d4c-a478-c7c2e34471ad | -7.428 | -44.7867 | 2026-09-21 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e5731b99-4363-3c41-af81-9898b3dcfa68 | -10.3728 | -48.8936 | 2026-09-21 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f64ebfa1-1ac9-3829-8084-c8db652d95a9 | -6.001 | -51.7903 | 2026-09-21 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5308856a-090f-391a-ab77-b13ff21e2220 | -5.6594 | -43.4139 | 2026-09-21 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b8cd5351-3e31-37ab-9743-3d7525c745e8 | -10.7652 | -50.6153 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 1b1ac204-f9e5-3c1a-9d72-2067cca055e9 | -8.0465 | -61.3427 | 2026-09-21 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c296ac6c-6fb2-3c30-ba19-479cf1781de7 | -6.183 | -47.6133 | 2026-09-21 14:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a22172e2-cc9f-3d7e-acf1-bad651f887b0 | -11.0997 | -51.0687 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 00bfc258-8e58-3f7f-9ca2-af1501e61677 | -9.578 | -66.0353 | 2026-09-21 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 16b7de2e-eefe-316b-9e45-3951dbd98856 | -7.3291 | -55.1955 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 12f9bfbb-527e-3725-810b-2c3ed8884f6a | -11.0221 | -54.1584 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 56436a34-4bc9-37ff-917d-c695416cc887 | -5.2023 | -49.3348 | 2026-09-21 14:50:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| be7addaa-685c-3cbd-b9b8-3a6e73b34ad7 | -8.7911 | -48.7502 | 2026-09-21 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 2ddccb0c-7f9a-3b3c-a6ec-c407c822acc6 | -10.9361 | -50.5759 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3745940e-50e5-3bfa-a051-6cc32266fdc1 | -6.8263 | -55.5421 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| f45b13de-a2c0-37d9-aea1-1b4d69c151c0 | -3.4974 | -59.1944 | 2026-09-21 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 56aa88dd-2225-3923-86c6-e8497ce7d286 | -10.3725 | -48.9153 | 2026-09-21 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| d2ca11c6-d403-34b3-bfa2-d833296ce9b7 | -6.5451 | -44.8643 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 270.4 |
| 70bd14e2-4b17-3011-b9fa-eb377029a13a | -10.8735 | -53.9668 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 57477a0c-6f12-3d26-b4cf-4db934f5eb74 | -5.6781 | -43.4125 | 2026-09-21 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 9ceb68cd-87f5-3c22-8a91-012e35bf2f4c | -11.041 | -54.1567 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 253.5 |
| 0484c9f4-15a4-374d-83b7-836f4a2de5f9 | -14.0421 | -52.0812 | 2026-09-21 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 242a1219-96b0-3246-83e1-83d7d12d176f | -8.1871 | -54.7824 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 542fa6e6-5c8d-395d-9733-baec1d51ae15 | -9.977 | -50.248 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| da8fd3dd-9f9a-3283-9a57-5e754f837b72 | -3.753 | -59.419 | 2026-09-21 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 93e70602-c781-31ce-b9ac-fced14cc14d2 | -5.7504 | -43.7091 | 2026-09-21 14:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 340.5 |
| 3433fc53-8103-316b-85b7-d1c14b5ad784 | -6.0973 | -53.913 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 13f1da84-01dc-36c4-83cf-69f6aa8d1de3 | -10.3363 | -50.1905 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 381ca2f0-ea4f-39c5-ba89-d2eae72d6054 | -9.2756 | -46.2077 | 2026-09-21 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 35622e40-5a2a-368b-831f-409eeb79f9d5 | -3.3454 | -42.7597 | 2026-09-21 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 25c1d3a8-7196-395f-a3ef-64b21dad86f9 | -10.8909 | -54.0882 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 14a6b090-357e-3023-8dfd-b32fc335483c | -10.6947 | -50.2386 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9d1c5a3b-220f-3db5-987a-01295f3f019c | -6.8058 | -55.8217 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 65dc93ef-b004-3d83-a46c-7f84639eb7f3 | -12.3216 | -50.6751 | 2026-09-21 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5cc00430-5d35-3c2e-87b9-95b770125d64 | -10.7655 | -50.5939 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fb7a93d6-30f1-34d9-9e55-95b0ca978692 | -8.1874 | -54.742 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 652f0293-4e8c-33cb-9746-3f10385781cc | -7.2519 | -55.5994 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e5ae0713-1995-3d0e-9a79-9b3ec6127aa3 | -13.2407 | -51.7784 | 2026-09-21 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 85fb56d6-ba08-39b8-a427-e5c870e76749 | -10.2793 | -50.2177 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 88a41b5f-83a7-3c16-9d0b-1149de2a0d1f | -6.3197 | -59.9764 | 2026-09-21 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 173f6bb4-cdc7-3dd2-8d4c-efa1df9a0ca7 | -8.1876 | -54.7219 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 8e319f5f-a915-3df3-980a-747f21147406 | -7.4092 | -44.7885 | 2026-09-21 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 165.3 |
| ce3dfd10-6161-3b8f-a4af-5694e4b6744a | -6.0033 | -44.7247 | 2026-09-21 14:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5896ad10-203d-3602-951b-176317598f65 | -7.026 | -42.0924 | 2026-09-21 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 154f5874-a0ec-30d5-8d5f-3376b2db2218 | -5.8411 | -53.5002 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 893d9e71-4f30-3a7b-8218-d6653c76c6d9 | -6.0196 | -51.7893 | 2026-09-21 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 45e19091-18df-3a4f-a8df-ee63cd8c82eb | -12.3021 | -50.6988 | 2026-09-21 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6207b632-6f20-3fca-a139-a8cda373bb29 | -11.8359 | -50.046 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 999ec434-0024-3d4a-8d00-0ed4a53d6548 | -6.883 | -43.0771 | 2026-09-21 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ed83a356-3a95-3f11-9eed-b5e85679b9f7 | -12.2914 | -50.1633 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 4a8f014e-b7b5-3036-b8b0-6785ddeb4395 | -14.6487 | -45.6833 | 2026-09-21 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 931edce4-bee5-36e6-aa8a-f003a81217bb | -10.3921 | -50.2488 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 738b733e-3106-3425-acac-c17dc690af1d | -12.1853 | -50.8623 | 2026-09-21 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e77ec470-dd96-34b5-839c-22d2ac7ee0be | -6.9225 | -42.9088 | 2026-09-21 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| a2f9536d-91ca-32b3-b1f5-50dd1d7d5f28 | -5.8274 | -47.7898 | 2026-09-21 14:50:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 14adaa22-3542-37a7-98af-23a3b4a986d7 | -12.3018 | -50.7203 | 2026-09-21 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 880443f0-d21c-3bd8-909a-8900a84715eb | -3.4555 | -50.5927 | 2026-09-21 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 17f573cc-dbca-369c-b1f1-8f9a137aa850 | -9.5594 | -66.0359 | 2026-09-21 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 95c64167-9f42-317a-a1b6-58aef63e7c88 | -7.4124 | -49.853 | 2026-09-21 14:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e495c64b-4801-3147-86ac-4f8ab59de7f5 | -10.3543 | -50.2527 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 600476c7-7aa4-3371-ad00-6e79fed213ed | -8.6171 | -54.6126 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 009b8770-9046-39fa-8a01-771fe954145b | -4.5774 | -42.9512 | 2026-09-21 14:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 4e99410e-5dba-35d7-8572-942e581d86f4 | -10.4111 | -50.2469 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 97fc91d1-b1c1-3d87-9139-cdde6a3019c6 | -7.4283 | -44.7639 | 2026-09-21 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.5 |


[Clique aqui para ver as próximas entradas](README133.md)
