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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0262161-bebd-3394-933f-a55bfff8f1aa | -5.8159 | -57.7346 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 220.9 |
| f4f605c3-d3a2-3b6c-b3de-d3318ee68087 | -10.1813 | -68.4361 | 2026-09-21 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 29f18164-97b8-3fd4-8b40-70419677b54a | -1.4302 | -48.9529 | 2026-09-21 18:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 23461915-021b-3491-8bd6-d4c2b947745e | -10.2711 | -45.4787 | 2026-09-21 18:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 093ea5e8-c53d-3c14-825c-51c4446943a1 | -3.5136 | -59.9401 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 83ed81d2-2f4f-3b5a-bef1-480b047a0194 | -1.3792 | -57.9747 | 2026-09-21 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| dc87bfb8-d94c-3b20-9c4f-cef98c9e512a | -6.2766 | -57.7358 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 48149c49-07f7-3d0b-9529-4af6f8c2e80d | -11.9507 | -46.5033 | 2026-09-21 18:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a10e1404-fbde-3b4e-91c2-80883c523467 | -11.8559 | -49.979 | 2026-09-21 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d4f6b32b-85f4-39a8-86f8-4c5313e3fa70 | -3.6449 | -58.8647 | 2026-09-21 18:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c5c9d864-cf5c-3ff9-914c-083a5bb24f3a | -7.6942 | -61.5473 | 2026-09-21 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 02a60fd0-e2fd-3c83-b97c-fc86e1abcc8f | -11.6802 | -43.4209 | 2026-09-21 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| fffcbfaf-e9bf-3202-aff7-4648d6c4195c | -5.7975 | -57.7353 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 93a9e740-9bba-386f-99f6-84bb9e54126e | -10.2517 | -45.5039 | 2026-09-21 18:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 272.9 |
| 6d3e2d22-2aeb-3944-aa76-4c809eb08a19 | -5.9335 | -53.5159 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a9db2756-79f8-30db-a9a3-cd648f4c5ee1 | -9.0227 | -49.8262 | 2026-09-21 18:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e9d713c8-379e-3d9d-9c59-e62018c3659f | -10.1791 | -69.0659 | 2026-09-21 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 343e654c-00bf-3b18-b9e8-12df97d3deef | -2.8608 | -57.8188 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 5a10c9e4-c642-387c-9b7e-60dd6603c0c2 | -6.325 | -55.8451 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 360f98b0-1773-39bb-8bbe-38717e85559f | -8.5984 | -54.6139 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 05f6ebf8-7531-3e8a-a6b0-2a3da26553eb | -10.8282 | -50.1601 | 2026-09-21 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a718f8cc-0e71-39cd-ac71-41beb945bb82 | -2.9525 | -57.7394 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 4365b11f-2dc9-3b14-ab7d-bafafb5081d6 | -10.236 | -68.7498 | 2026-09-21 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 186bc321-bf3b-360f-b075-fa9a100c6c8b | -0.7471 | -49.2161 | 2026-09-21 18:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 4c633c75-fbc6-34a3-a1b5-0b0060138c62 | -10.3725 | -48.9153 | 2026-09-21 18:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ccc45e6d-a2c7-39ef-97d9-96202052b5b3 | -6.6761 | -50.9381 | 2026-09-21 18:20:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 093c5a4b-7052-3e55-bc9d-8eb559b1b489 | -10.2154 | -53.9011 | 2026-09-21 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 1e2f1b1a-27cd-31a2-905f-0b573baa06b9 | -2.8791 | -57.799 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 7acaa654-e310-3b7b-b881-346b4dba2bf2 | -9.977 | -50.248 | 2026-09-21 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| cb4017e6-ac24-3a65-8b0c-1a72eaf06253 | -6.3657 | -58.2771 | 2026-09-21 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 4a6faa02-6ae7-3726-8e89-da20a6dded4b | -6.3436 | -55.8243 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e80f09a3-3f13-31c7-aa99-b92a6e7d08a7 | -5.977 | -55.3639 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ad563625-b2ae-3e9c-9f56-4e5d6371f893 | -8.7911 | -60.7935 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 892840a6-445a-3fd9-bd38-5ae04eb9e345 | -5.3906 | -48.9612 | 2026-09-21 18:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| f56ba966-50c0-3862-83dc-e88a9eed73b4 | -6.3015 | -59.9387 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4a73659c-8a99-3b0e-8db6-019cf98b5f20 | -8.0894 | -55.331 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 66fedd7b-7306-3fae-9e93-4ecb99bede7a | -3.3505 | -59.4082 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| bb3e701a-5873-334f-954f-272804ba6265 | -10.8475 | -50.1366 | 2026-09-21 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 211eb4f8-0511-353e-b89e-f079b1622001 | -7.566 | -61.343 | 2026-09-21 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4ee447de-4ddf-3adf-86af-fa76a746d8b8 | -9.1813 | -60.7747 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 1a22042c-1a46-3c2c-b42a-3026b60794c7 | -7.5477 | -61.3247 | 2026-09-21 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| d7c4aff4-4afe-3221-80ce-d6dda755c19d | -3.1698 | -58.5859 | 2026-09-21 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e842f83f-96bd-3898-a009-fa7b8cb4897f | -3.3138 | -59.4472 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 11484b72-a1b9-3d1a-bb45-7caecb3559d4 | -11.8171 | -50.0267 | 2026-09-21 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| ff6479f4-174b-33f9-8f2e-73c0df85badd | -10.8093 | -50.1621 | 2026-09-21 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6a61fc4e-9d95-30db-b6d6-889c373a1598 | -10.8472 | -50.1581 | 2026-09-21 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 43201d24-880c-3da7-b69d-0ebf8413b31f | -6.513 | -58.3099 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 83b846df-402d-35c8-90f9-8aaa056ab1b6 | -12.0645 | -50.0401 | 2026-09-21 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a5a9b271-ba3f-35fd-9bb8-1e3556dd17c4 | -9.5353 | -47.9569 | 2026-09-21 18:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1206e168-1ad8-3e28-80e0-e7577f72c155 | -8.8644 | -68.5034 | 2026-09-21 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cbfe44ea-eb75-395c-9124-2a238a96eea2 | -7.5476 | -61.3437 | 2026-09-21 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 15a07da2-881f-3a85-8b25-90c41812615e | -8.7916 | -44.2778 | 2026-09-21 18:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 851.2 |
| a0580a62-feac-310a-9272-a68762ddb69e | -8.7729 | -44.2568 | 2026-09-21 18:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9a8059d4-32c1-3317-b112-0cc54161f049 | -4.5774 | -42.9512 | 2026-09-21 18:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 83fa9edb-e9cc-3ee3-bdd2-6cfc102eb3e9 | -6.9297 | -59.6267 | 2026-09-21 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a99fbfba-2583-370a-8a72-71fb7a2ebd85 | -3.3138 | -59.4281 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d10f0560-1ab5-30ea-a96a-eb24ddfdad4c | -7.822 | -61.8084 | 2026-09-21 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| f3be2b04-9058-3107-a8c7-7924b2dc8647 | -3.2955 | -59.4284 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2b69d6e7-cd15-3536-be12-51f7496ff9fb | -2.8608 | -57.7994 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 7bd8bf83-0b97-3e4a-966d-2b78361557f9 | -3.6264 | -58.9228 | 2026-09-21 18:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 966eaa7f-247c-377d-8feb-2074849d7f83 | -10.4725 | -51.3231 | 2026-09-21 18:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c9d98fc9-d366-371a-9200-1ce41c53a304 | -3.6264 | -58.9036 | 2026-09-21 18:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 39d549c5-bdd5-3bd8-b6f1-e0b95b9c36a5 | -10.7223 | -54.0008 | 2026-09-21 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 890779e2-9f6b-3066-87a4-bb315c71e6ad | -9.0866 | -61.0287 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 341e0945-d444-3c89-b9fe-8f40772469b7 | -6.9839 | -49.799 | 2026-09-21 18:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d9b0c690-cd73-3951-951a-e0b3a16aef55 | -6.3434 | -55.8442 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6f968dee-9585-35eb-86a8-e3226a5edfbd | -5.8408 | -53.5408 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fc391dcc-18fc-3f6f-8112-3686a8072e67 | -11.0529 | -46.5569 | 2026-09-21 18:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 972593b9-c02e-3e78-95db-1cb1e5d74fba | -3.8957 | -60.5984 | 2026-09-21 18:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 882f5584-8c41-39dd-bf81-ab198894b332 | -8.4177 | -43.9718 | 2026-09-21 18:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 00e09b5d-fed5-375d-be14-19bd1ca3053c | -12.0448 | -50.0856 | 2026-09-21 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 3a9c92bc-27bc-37ca-800e-0c07548a3042 | -5.9334 | -59.9707 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 172.3 |
| d7834f29-69cc-32e4-b8bc-6311ed88f2c8 | -6.3286 | -55.2877 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 74867b09-88d5-3d14-b37d-7c22ae611bc2 | -8.754 | -44.2589 | 2026-09-21 18:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| bbd4a708-43c0-3177-ba60-be73324abcce | -8.1874 | -54.742 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 0a911b55-aea1-383b-a555-6cfa57e2773d | -10.6878 | -50.751 | 2026-09-21 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 690aeaf1-2f68-3ae6-a7c0-8b2f3c26439e | -12.0451 | -50.064 | 2026-09-21 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e3da49c1-0399-30fd-a0a8-17336ad06b05 | -2.9525 | -57.72 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 2bbfa9f4-7f5c-3b1c-930a-89fdc1293c73 | -6.0743 | -57.6465 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 8f80dabd-8e84-3a70-af97-c1827be1ecbb | -3.2955 | -59.4476 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f743b654-b253-34e6-9df9-4cb1afc0e7ba | -12.382 | -47.0283 | 2026-09-21 18:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 604af83f-1c24-3f66-a649-b63a2b162863 | -5.1838 | -49.3358 | 2026-09-21 18:20:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1edce0b9-4af5-3eaa-b030-b41accba0e3a | -8.1871 | -54.7824 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 002017d8-7030-381e-ad35-6d80a4f87a99 | -3.1881 | -58.5855 | 2026-09-21 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a41a8aa9-5860-3784-9d44-8e27fa60f0b7 | -8.3061 | -46.8662 | 2026-09-21 18:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e6791cdf-460f-3af1-ae3c-0228eb571cfc | -2.9157 | -57.7983 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1b5e2758-8947-32df-b4f6-2b66bff3d775 | -9.0287 | -69.2191 | 2026-09-21 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 28aceaa7-ff1e-32e8-b0bf-fc5a486b4a6f | -8.7378 | -45.4753 | 2026-09-21 18:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| df061360-7ca8-3ac6-b96e-6b84d7cc0450 | -10.252 | -45.4811 | 2026-09-21 18:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 67a0bda2-ae5a-316d-a1d4-9dfb05606e28 | -6.2832 | -59.9202 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| eddffed6-d4d9-3bf6-b7db-3665ab9436be | -10.2174 | -68.7503 | 2026-09-21 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 824d3ff4-08c0-3569-9308-88eeb42fca57 | -10.7061 | -50.7915 | 2026-09-21 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e1f7aacc-c2c0-3396-996d-53091f0302d3 | -5.7317 | -43.7105 | 2026-09-21 18:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 21d3b524-e607-390e-ab43-2d8db5175c58 | -10.4764 | -69.2073 | 2026-09-21 18:20:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1afb8e6b-52e9-35c1-a169-2b1520ff469f | -10.6875 | -50.7722 | 2026-09-21 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f1350f9c-1ea0-3bed-a4b5-1a565d739728 | -8.1495 | -54.8251 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 57099f50-ceaf-3e82-b1e1-6725a4737795 | -3.2817 | -57.8685 | 2026-09-21 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2b3f5892-e579-3f82-8e14-82567a9565fe | -3.6448 | -58.9031 | 2026-09-21 18:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7966e5c6-945b-3b76-86ce-8d44228a313e | -6.5708 | -44.1747 | 2026-09-21 18:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| dc7959ba-8269-3c74-ab7a-077312d47516 | -8.1681 | -54.8239 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |


[Clique aqui para ver as próximas entradas](README187.md)
