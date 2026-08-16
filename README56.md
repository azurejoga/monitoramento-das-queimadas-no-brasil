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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 194c4138-33cd-309e-8ea5-78f191070bf5 | -8.96 | -60.5358 | 2026-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 1c59aa86-dfaa-3880-a54c-8de6dce7c656 | -8.9787 | -60.5156 | 2026-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6de0c747-f7aa-3747-b547-deac9218b6c8 | -8.9601 | -60.5165 | 2026-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| afc3542b-bd5f-3cfb-9bc9-c4360d2a4ff8 | -12.0087 | -46.4725 | 2026-08-16 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 904ee307-084c-33ac-982a-0dbcfcb9b160 | -6.7123 | -58.9412 | 2026-08-16 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4b958539-0f03-3cf6-a390-5afbb662fe7e | -8.9785 | -60.5349 | 2026-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e8244f8e-5ae1-3586-b600-7d3d21279180 | -14.9005 | -46.6512 | 2026-08-16 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 46d6b8cc-2284-3b3a-8dfa-865ce274b016 | -8.41129 | -62.66167 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51f0443c-0ed1-39e3-80c3-223a212ca711 | -9.13811 | -68.1955 | 2026-08-16 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7dc5742-db4e-341f-aefe-1a64806f174f | -8.4391 | -62.68831 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0a092a44-34bc-3161-9ca8-2c31a64682aa | -7.76392 | -69.92847 | 2026-08-16 06:22:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0a3b6af-21b6-3910-8738-cf52b6775089 | -8.43531 | -62.66384 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e76539e3-d218-3976-9153-de0d6f5536cc | -10.00371 | -67.4941 | 2026-08-16 06:22:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fd1d5b5-f55a-3026-9062-9be0c65ef343 | -8.43982 | -62.6824 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| af65a531-7361-3dad-9ea0-f1d5274b889a | -9.39952 | -65.96346 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a215a9-d722-36de-8cac-4edd725792f6 | -9.3559 | -62.37154 | 2026-08-16 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5171b52d-e8f0-36c7-92b9-33ddafe58fc6 | -9.50804 | -68.50079 | 2026-08-16 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63f2a6af-526f-39a7-9ee3-bbc495befaaf | -8.42901 | -62.68229 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b627d61e-bc0c-3193-9bf1-154442d8ac4b | -9.39997 | -65.95985 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cabba5ea-2bd1-38fb-93b8-8544424353c6 | -9.12897 | -66.97259 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a7a731d-e8f0-3e53-994e-6f16dce52e4a | -9.13211 | -66.97241 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d8cb7e8-ed8e-3446-b415-54f770371151 | -8.4153 | -62.66086 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3270c5b1-e64d-3681-bf2f-69b830e262ab | -9.13409 | -66.97322 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d56334ce-ba25-3227-a8ad-8c6fd0f34f71 | -9.37726 | -62.36803 | 2026-08-16 06:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 034e9ee2-9550-3871-b18b-88ae94c6ac53 | -8.43387 | -62.6756 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0d5de449-8859-3d62-9e00-40b8b2d95c26 | -8.43315 | -62.68147 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 035ee07d-fd3f-3bee-af2b-3ce7561d1075 | -9.1345 | -66.9702 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49aae514-139d-30d3-a673-04f6186528e2 | -8.4272 | -62.67468 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cff009d0-c035-3e3c-bd07-805ea4c81c77 | -8.80909 | -66.76684 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7950d542-4313-3079-acd3-0ff13eda500c | -9.13368 | -66.97623 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caa56e97-adf6-34e1-9aca-27b03e78088d | -7.60366 | -70.35889 | 2026-08-16 06:22:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca54917c-2747-34cb-a8ce-05ca8a0c0c0b | -9.13172 | -66.97543 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fa443a3-fa65-33be-ad83-47fbce2bef8c | -9.14213 | -68.20119 | 2026-08-16 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43572c06-81dc-3154-8403-355ebe4bbb46 | -8.81426 | -66.76754 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48376397-515b-3ff7-952a-6be742662227 | -9.13743 | -68.20052 | 2026-08-16 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96feac0e-fac4-3837-bd95-12c58255a300 | -9.34904 | -62.37048 | 2026-08-16 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 317f0a6a-31c9-3a7f-ac6b-3504a4eb36e0 | -8.56957 | -69.90503 | 2026-08-16 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 681331b7-9cd0-3752-b432-e83aababec59 | -8.44199 | -62.66476 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f40fa379-deee-36c2-a850-774e890c1943 | -8.44054 | -62.67652 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 61d719d7-66ab-3717-a356-42286bcbf69d | -8.56904 | -69.9088 | 2026-08-16 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0912b94f-88e5-35fa-82f4-9a7addd04972 | -9.37807 | -62.36135 | 2026-08-16 06:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc0cd212-cd3d-3c05-9b8b-b21cd1aa989d | -8.85904 | -71.47583 | 2026-08-16 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31d16d1-2349-3824-8746-18d9b387ce38 | -9.1325 | -66.96936 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a610d3-f5f7-327c-a690-8059911be9be | -8.43459 | -62.66974 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e3f74e4b-b96d-32a4-9e8e-151fdb73bf63 | -8.42977 | -62.67643 | 2026-08-16 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d3caf12-44ee-30cc-8976-b5c1b6dd378a | -8.81467 | -66.76445 | 2026-08-16 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88a21cd-8cca-3be4-a027-b34bab28b82a | -8.9787 | -60.5156 | 2026-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9710eafc-4513-3e45-97fe-5e6b268b6de6 | -15.0682 | -47.0098 | 2026-08-16 06:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c3638338-2ba5-321a-be2b-3b7c809e7550 | -14.9005 | -46.6512 | 2026-08-16 06:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 286ca45e-1a36-39e7-92a2-0c7f5250a9d4 | -11.0609 | -47.2503 | 2026-08-16 06:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 934239a2-ec54-3d56-8f5e-4cdc83ca0b56 | -12.0091 | -46.4498 | 2026-08-16 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 219.8 |
| 82070eef-0733-3c5c-9682-4ac25f73f693 | -8.96 | -60.5358 | 2026-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f675cb75-f21e-3173-8b37-eb8e6c84a6e8 | -8.9785 | -60.5349 | 2026-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c435ce5a-e775-36ed-964d-67763f345ac5 | -12.0282 | -46.4471 | 2026-08-16 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| ac0b293e-5379-3e01-b8c6-8ba2eec25841 | -12.0095 | -46.4271 | 2026-08-16 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| daa509b0-a297-3eef-b671-c89aaa8f2e91 | -12.0279 | -46.4698 | 2026-08-16 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a3734db7-3555-3137-9eb2-4cf178f4673a | -12.0087 | -46.4725 | 2026-08-16 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 52bace1a-e9de-3458-a9f7-43d44c1fcaa1 | -14.901 | -46.6283 | 2026-08-16 06:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 167.6 |
| abca5fba-124e-30e8-adf1-68f3b96390ac | -8.9601 | -60.5165 | 2026-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b155b725-0fe1-31f6-8f1f-5a23f71355be | -6.7123 | -58.9412 | 2026-08-16 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 27949777-1b29-3f10-a95a-7ce40bcfa522 | -14.881 | -46.6546 | 2026-08-16 06:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 9dc9e93c-692b-3877-aa8d-7f49682a00c7 | -6.3137 | -43.6178 | 2026-08-16 06:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 478ccd4e-1536-33d8-992e-142fd61a35f5 | -12.0286 | -46.4244 | 2026-08-16 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| da732113-8609-39a2-aa59-b8d63c5fc53c | -15.0682 | -47.0098 | 2026-08-16 06:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 932406fa-1553-3047-a2d4-61caadfad907 | -12.0286 | -46.4244 | 2026-08-16 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d9e3c42f-af90-3355-9821-713b520ebb82 | -8.9785 | -60.5349 | 2026-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b591aff6-f53c-3d60-bd83-5589c8f14a1c | -8.96 | -60.5358 | 2026-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4d956af8-08f2-3928-9d0e-b02cdd5845de | -12.0095 | -46.4271 | 2026-08-16 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 60348abb-6c14-3679-a09f-a54fd6a27fd5 | -12.0091 | -46.4498 | 2026-08-16 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| d2d4c483-1c1f-3680-aea3-e990d9b839c8 | -6.3137 | -43.6178 | 2026-08-16 06:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b8d04e2a-d4ae-3287-9953-68799fcc6f6c | -6.7123 | -58.9412 | 2026-08-16 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 350500f5-4239-3772-b142-79ae2248bfd1 | -14.9005 | -46.6512 | 2026-08-16 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 20e6ff4e-9f01-39ab-a5bb-83256badb576 | -8.9787 | -60.5156 | 2026-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f5e0cd9f-87fb-31bf-804c-274aee37f59b | -12.0282 | -46.4471 | 2026-08-16 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| f55f8916-eff6-3bdb-9c01-6b42982fca4c | -14.901 | -46.6283 | 2026-08-16 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| eb38faee-cd4f-387c-b0f4-e58d6eaef030 | -8.9601 | -60.5165 | 2026-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 963801c1-faf2-335f-9abb-65a084ac34bf | -12.0286 | -46.4244 | 2026-08-16 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 62e679c5-e11b-3297-8d5c-e0dabadd6205 | -14.9005 | -46.6512 | 2026-08-16 06:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ea6847d8-f1a2-3526-b201-96355fce82f7 | -14.901 | -46.6283 | 2026-08-16 06:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f007aa20-f7bc-3b34-bd02-65b0e9195921 | -12.0091 | -46.4498 | 2026-08-16 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 3da0aa1d-b91a-3748-bd58-6d1ef509809d | -6.1107 | -57.723 | 2026-08-16 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| bac22b9d-9668-37c7-9ac4-0822af14c956 | -6.7123 | -58.9412 | 2026-08-16 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9aaa69b1-0a30-3036-ad15-085065d8a591 | -8.9787 | -60.5156 | 2026-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6c263c57-7ee3-35ce-b907-51b5a8e65491 | -8.9785 | -60.5349 | 2026-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fe0fe160-7ce8-397d-ac5d-e9953c2698c6 | -12.0095 | -46.4271 | 2026-08-16 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 7b8c53e7-3f8e-3122-9f87-1ccad8a8c018 | -12.0282 | -46.4471 | 2026-08-16 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 07bce7d3-0041-34a5-8f88-3f00af6802c1 | -8.96 | -60.5358 | 2026-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e26640e2-799d-3f76-910a-ef1edc83af4f | -8.9601 | -60.5165 | 2026-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 67db9cc1-5033-3402-9032-df934c7dd309 | -14.9005 | -46.6512 | 2026-08-16 07:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 165.4 |
| f8525e51-48a2-3f5e-baeb-92bffb3e2f0d | -12.0091 | -46.4498 | 2026-08-16 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 248.2 |
| c066e061-be94-355a-8ac4-3fd14d93548a | -12.0282 | -46.4471 | 2026-08-16 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 41fdbfb5-efdb-376a-bcc7-d9b6b4aee7d4 | -8.9601 | -60.5165 | 2026-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 90e3fea2-3c12-3151-bb4f-4607c46d26ac | -8.96 | -60.5358 | 2026-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3d96c656-35c1-3bd4-87aa-5de5b3e8b6de | -12.0286 | -46.4244 | 2026-08-16 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0e6cda4a-b14c-32cb-8276-ed0a4a8e3c15 | -6.3137 | -43.6178 | 2026-08-16 07:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c97ad42d-963e-39db-aa71-4241e9609ff3 | -12.0087 | -46.4725 | 2026-08-16 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a9025140-a47d-3398-88d1-4991e65675df | -6.1107 | -57.723 | 2026-08-16 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9e83348b-e4dd-3e8a-bd5a-61f5fffa1987 | -12.7017 | -48.4753 | 2026-08-16 07:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d6318cc4-ea7d-35e8-a8a8-f0f3731fe316 | -6.7123 | -58.9412 | 2026-08-16 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9db9c6d2-b5d5-3140-9eb4-7fb62ccac624 | -14.901 | -46.6283 | 2026-08-16 07:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |


[Clique aqui para ver as próximas entradas](README57.md)
