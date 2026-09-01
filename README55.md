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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2974e8c0-ec0b-3b32-8613-ee3cfe055942 | -6.65538 | -59.43245 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee9a1abb-b758-3695-b878-e089bc9b1fc3 | -6.3754 | -51.76316 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbe5b57-6fec-31af-9416-4f17390e2a99 | -7.02717 | -55.64594 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1bd2fd2c-969e-3bd1-abe5-d5af5e77983e | -7.53511 | -61.38272 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ccae3d2-5fb6-329b-8d80-f4784ae70fa9 | -6.7379 | -56.34077 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ff18a56-ae08-366b-ae50-a8dbe2f481ca | -6.88036 | -56.50613 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e835518c-87d5-3cdb-a273-84e46433492d | -8.59623 | -54.75747 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8eaed43-1cce-32ab-ace6-8bf9aef8e68c | -7.52561 | -55.33743 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1311519-a9c0-3f7f-aee5-457fc1562d49 | -9.482 | -57.02494 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebc2a313-6fde-31d6-aa69-0fc1a0b7fc05 | -6.92036 | -55.70045 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0261665-bd01-3114-a7bc-2c87c48e755a | -6.15614 | -57.78601 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ce6e451-1db8-373b-b0e6-430eb64dae36 | -5.25359 | -55.9047 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e0faa9b-9159-3460-8663-e56d9dfc7480 | -5.88465 | -57.76266 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 397447a6-dbe3-3a4d-871e-c67f26a149a8 | -7.31722 | -61.14554 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa86afb-45bd-3d5a-b372-65604f9e4580 | -9.15292 | -60.93888 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 659886a3-f10f-3c83-9dfa-5090d14ef52a | -6.82896 | -56.44793 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39b83156-bb10-3b8e-8993-273f34814312 | -6.36569 | -56.00026 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d56924-c14a-3c8d-aca2-e665a8283d27 | -6.69866 | -55.41565 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e3c64ae-24d5-3e1b-8024-ff21b794bbde | -9.47923 | -57.02089 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 372270d6-5d47-33d2-a49d-d87023c318b3 | -7.56498 | -61.20599 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02722fe6-b2a5-3d8a-bdc4-34c2f636cf0b | -6.24896 | -55.43408 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50bc8162-d508-3b54-a386-03e1b5b03ce5 | -4.37375 | -55.41433 | 2026-09-01 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18750e32-ffb0-3046-a362-54d845472a35 | -6.20531 | -42.5191 | 2026-09-01 05:16:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3c5769d-f29f-360c-b2bc-37936bf22ecc | -6.27797 | -53.33818 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b602aa1e-0a50-3e99-a614-746b971b9a75 | -6.80395 | -59.77225 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 420277c6-4e93-3f8f-a2a9-fd4f2a836117 | -3.12072 | -61.22912 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e59ac134-45a7-311d-971c-2a764f3bbcde | -7.52754 | -61.37768 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 588c6386-1518-355d-9d87-87bcc778d0fb | -10.68927 | -46.25458 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20700f4d-7c98-3300-b63d-f3df1ebe0272 | -9.15475 | -59.53539 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03b6c1dc-10f9-39f7-a4ee-c3946db65297 | -8.78845 | -62.48648 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df4b667f-554d-3551-8a7e-3586c647e15b | -8.21689 | -54.93432 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73c434c4-8823-3cbc-8abb-213f6a458845 | -9.05359 | -60.44503 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e73a0401-0de0-3771-acb7-36353bbfd710 | -10.32407 | -49.95186 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eaf2f6f-63c2-324e-bcd6-42a62d071150 | -7.53859 | -61.38708 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bbf9617-732f-328b-84be-1ae41a0912b6 | -4.9687 | -55.84557 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 096a9782-7cf8-3d5f-a705-5f06ac9334ba | -11.15217 | -45.05075 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82e09dff-a363-392f-977f-7972459d0ce5 | -9.06427 | -60.42802 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09ccbff5-2c2e-318a-8d4c-07a9ff4760be | -3.62719 | -60.5667 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6818d429-5583-3aec-aaee-6a073c174871 | -6.94244 | -55.64691 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0289f8f9-407c-39de-bcdb-98e2eda1d71a | -7.57029 | -61.37389 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41827c29-6b77-3b69-8c72-c81e7d9e3bb2 | -7.61945 | -57.61885 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f1d6bd-9b1e-3b35-98c3-97dcb865394a | -11.00773 | -48.37904 | 2026-09-01 05:16:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 897e68d4-647f-3fc5-ac35-f7b04fc0f134 | -8.13755 | -54.96994 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a52c0ce9-e4b2-3895-805c-de7f8ec5d25c | -7.52345 | -61.37698 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ed981bd-d693-3675-b2b7-53e1497116e0 | -6.34677 | -55.88353 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3fb1fa0-fad9-3164-8439-7e0a54ceae29 | -7.41338 | -55.16465 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 553f7ef5-280e-33c7-ab0c-b9b98c880e8a | -7.41247 | -49.73938 | 2026-09-01 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f96be1-d36c-3ee4-a5a1-8729b8b3df46 | -7.28663 | -49.83775 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 866ca8de-3861-3615-82e5-b1324611b105 | -9.96645 | -53.93973 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7564e95e-342c-3a07-8621-30f1983d5a2a | -5.25524 | -55.89431 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cf88708-b163-3fd3-8bf1-106373938d62 | -6.18806 | -57.58938 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 918ca0e4-ce83-3440-a517-4a2d091bd7e5 | -8.80498 | -62.49366 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b0a181c-a079-3546-b7b1-ea0bea4380c3 | -6.25179 | -55.48081 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509dc265-dc8d-3686-959d-f35bd8ca788a | -7.57758 | -61.33017 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c45b5d16-5841-3f01-a077-3bc219b1459b | -8.19667 | -54.95325 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06ceb1f9-ae42-343d-8c07-99bacbe77c7f | -6.60369 | -58.60751 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25115570-60bc-3d05-a839-9c6cc052e846 | -7.1906 | -60.69046 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 871793d0-fa83-31fa-80b7-cb48c02fd407 | -11.26737 | -45.1146 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3eed907-69df-36b6-be9b-5d50b8652178 | -7.0369 | -59.22335 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5241bc-f90c-3cde-850a-7856506db9c6 | -6.15903 | -52.64054 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fef601aa-3efa-3058-833b-38217e360419 | -5.88529 | -52.07159 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4b00e7b-4a64-3bd6-8064-89921afb9894 | -7.53102 | -61.38201 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec1ab7bf-421b-347f-a6df-6c26ef4c71fe | -6.60563 | -58.59557 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e947f04-a2d6-3296-a770-c4144513170a | -7.94623 | -52.45997 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19b9562e-1ef2-307f-9dd9-0bc97780b3e9 | -3.34441 | -59.4354 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d151d1d-7a85-3b3a-84b6-fc10b1c874a7 | -5.57587 | -60.19004 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bcd6c08-e4ce-3a61-8e14-518ef15251d2 | -6.85998 | -59.48132 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d2d566-b96f-30b6-8e80-aef99f6ca6c8 | -4.36592 | -47.77752 | 2026-09-01 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| efb2740e-f598-3580-ae6d-98d741796f9d | -3.61201 | -59.06532 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7737c66d-87e8-3ac3-b33b-1c3fbaa98698 | -7.29047 | -49.84219 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73517af7-f3bf-35c5-b972-a6edc51663db | -6.73982 | -55.4504 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f5307a9-8a03-3eaf-98c8-24f5ebe2a4a0 | -4.97093 | -55.85302 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d92e3696-71a8-3c7e-8942-570bbcf7bdef | -4.85609 | -55.83152 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a1c4307-57d0-3a19-a637-6ce0624aeefa | -3.096 | -61.21651 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 957a5649-3bca-344f-ae73-26150c5e0985 | -6.56002 | -58.56349 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48c5107e-e133-361a-a1dd-ce06f51a4979 | -8.62173 | -54.79526 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbda4d1a-b5cb-39dd-b3a4-68e1139f1bcf | -6.55649 | -58.56291 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d3461c-c711-33ed-b606-d6b5d6a36f46 | -6.75618 | -56.33302 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07d25970-a50e-3d4e-bdec-b5a5f0829e02 | -6.12891 | -57.69361 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a76a5e1b-5906-3c29-8d9e-286265ea827b | -10.82827 | -50.71597 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4ec1d4c-5149-3842-b849-c84a3aa08b05 | -6.12178 | -53.55311 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91a17423-56ed-3587-8971-676381b892d9 | -9.46812 | -57.02631 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70a5e2cd-8db1-34be-8808-e49515aaf3b2 | -7.61982 | -55.29417 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a71c687-ce9e-3c7b-9799-6b047c8ff8e3 | -6.88461 | -59.40097 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbe4d862-d196-3006-b497-b9fd1cf6e267 | -6.93798 | -55.63194 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59ad418-d865-339c-a8f6-f1dafe4e4017 | -8.03798 | -61.73211 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6edc2011-9c50-3bcb-96d9-d6cf1f8b39e0 | -5.25579 | -55.89084 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dffc5032-aee6-3456-bc2b-398030cbb50e | -8.61094 | -54.81992 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a93317f-0ead-31ce-87fb-d7573856df6c | -10.58462 | -50.38084 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ef3796e-1047-38d4-a1fc-fd129a046a49 | -8.80856 | -62.49857 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c2f415a-50c2-356d-80db-867c1490140f | -7.73273 | -55.22111 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1de7dc0-f55a-3014-9578-4351af995d97 | -7.52404 | -47.33548 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15f1d366-d4f6-387c-b936-d41b564b9836 | -7.39956 | -48.01017 | 2026-09-01 05:16:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e04d65d-ddac-3b9f-a4b3-9d7e2856d489 | -8.14092 | -54.97048 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08ca3549-cbbc-3728-8ef4-0c4311657586 | -2.94176 | -54.15522 | 2026-09-01 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df8afb98-7f09-386d-b003-cccb0cbaa781 | -7.57818 | -61.32655 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0efd6592-7e59-354b-aa20-68810edae0bf | -9.14978 | -61.09863 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68b8c416-3269-3043-afac-c942c19c9aa5 | -6.02627 | -57.68156 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29c3ffc9-3726-3038-a427-221b4d1ec410 | -8.48812 | -44.75027 | 2026-09-01 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b77090b-81ae-34dd-b75a-8874a4ed167c | -3.79459 | -59.34872 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README56.md)
