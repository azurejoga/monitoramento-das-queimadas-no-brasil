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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de8b4042-ffe6-36f2-9225-33c15a4ad23b | -5.04154 | -49.76874 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73a3a716-e723-3a5a-b6eb-fcdf4b9780a8 | -3.03998 | -54.2572 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| baaf8bf9-896c-3b62-8422-b47bafbfb3f0 | -3.54451 | -54.66758 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38bc7834-a502-34ec-aa1d-23adb25cf17e | -7.21861 | -55.10557 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbf0940e-b16c-3131-a3a7-70f4c43c2059 | -5.68045 | -53.48612 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27eaa5e6-218e-382f-a6e9-deda6f7afaf3 | -3.17553 | -53.83448 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08e2a1bd-77cb-3c85-8b2f-6cb0851b56d7 | -7.38693 | -55.22134 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a462c95-2f3e-3ee1-a7bd-9c889b0427ed | -9.83655 | -47.47592 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8999382e-976b-349b-8ff3-05b2e540a14a | -7.871 | -54.97226 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b188af5e-b88e-33e0-aca6-29b83635b405 | -10.43749 | -47.27227 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 493b34e4-a1a9-3aff-b8cf-6063255f461e | -2.99088 | -54.05242 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19761c11-102c-3c65-9c6e-ef75cee94a3c | -3.84001 | -55.98869 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7d3ee1b-c113-325b-862f-80531f71a96b | -6.8855 | -43.69608 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 0247600f-efee-3baf-94a7-66efe3c583b3 | -2.5085 | -56.17886 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac020fbe-e3a4-3cf2-988e-c6d865f09cf9 | -4.11525 | -51.08642 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25c9940c-bb07-34a7-a762-de0783d9f2e0 | -2.99305 | -54.13345 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57c25349-e515-3b8a-a727-a3a23c88c1e1 | -10.96665 | -45.39386 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7b50e18-d839-3859-b097-76a029d062fe | -11.26592 | -45.18429 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c219149d-ef52-3fee-9cf7-6a00ed1be06a | -3.27361 | -54.04514 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce019677-0ee0-3958-bbc3-78247e79a158 | -4.92139 | -55.85989 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79f44722-d687-3980-8dd9-5b6f57189c3b | -9.51855 | -54.75547 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3790ecce-8393-39ac-b304-86b104aa1054 | -3.34999 | -50.47364 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19191009-f023-3534-a6eb-206eb6a53b40 | -2.94833 | -54.19886 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e191a927-ab6a-35c0-ba47-12d76ce199d6 | -3.0455 | -53.94576 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa37a182-7b49-3edd-9a45-a452d862e5ca | -4.14261 | -54.02712 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5dbccce3-764a-3c24-a36a-6e53aeebe532 | -5.96684 | -55.37231 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a266fbfe-8132-31ba-b929-cf5bfc5256d9 | -4.92483 | -55.86401 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f21ebb25-9cba-31e7-941f-49b6b58c44e5 | -3.84495 | -55.97895 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc69eae2-a7ac-3769-b66d-786250feb82f | -3.478 | -54.62164 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e86e3f5-3ed2-394d-8f25-6034a5df5a13 | -2.7936 | -54.09149 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e5f6dd9-000b-3631-82b2-5f9333caabc3 | -3.08169 | -54.2589 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe9a38a-b3af-3985-9ea0-b4496422b621 | -3.03359 | -53.92635 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34aab2db-b912-3df0-b40f-950cd014a914 | -3.2796 | -54.0549 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38c2dc4-cda1-3e3b-a393-6a5165e083a3 | -3.74505 | -51.21185 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 796bf2e4-2636-3e0c-885d-1fab79d24ee9 | -5.23495 | -48.40446 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c28016c3-94fc-31cf-95b2-c7e193b6d5bc | -2.88148 | -54.12685 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4de365b5-88ca-3028-b216-35fd6ea9b5a9 | -5.75037 | -42.07067 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be11c4c6-e080-3888-bb98-de232d7b8d3d | -3.47831 | -55.42799 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b33dc1a-b4fe-3511-b83b-d492da491d40 | -2.60823 | -57.58268 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df9ff4a7-53da-35dd-a6be-8d5323abb1f8 | -6.22012 | -55.67378 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a1631c-afa2-3528-aa46-66369b08e5bb | -3.69006 | -55.95791 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd4eefd3-e259-3eca-8755-8d067a31035f | -9.26688 | -45.64141 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71a15743-b115-31d6-b7b3-1b326f70fee1 | -3.35827 | -50.48545 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83103f8e-d51a-3e83-ab38-eb76200967bc | -9.90384 | -44.80382 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ec4612d-22e7-3f2a-b2ef-d7f1eb0a81e0 | -2.50412 | -56.15352 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| edc5ad7b-c441-30ef-ae88-55fb063aef74 | -2.99815 | -54.12522 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 548728e4-79d2-3cd7-b158-9de5205ac915 | -4.07141 | -51.03735 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5368a7a0-4a3b-3ae2-950c-46fe8421201e | -2.78599 | -54.06781 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6b9029c-c607-31b9-82e5-c5b320398125 | -10.42484 | -47.27578 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 928c5bb9-dfd9-3685-868a-0c3c2ac9c1e3 | -7.23154 | -55.16653 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64888e57-2af2-3659-8a3e-fe604f0798ce | -2.8458 | -57.47495 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20627fd7-24c4-35dd-9e6c-d541f1b1068d | -3.05688 | -53.92118 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35e144d7-9fb0-35a8-8344-be6cef2fd8c3 | -3.00485 | -54.13076 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 494d8d86-a7a0-3d86-9afc-90c504d3eadb | -11.39716 | -46.69631 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2031d7b2-53d9-3fd4-a760-9b0610f20bcc | -3.44239 | -50.62205 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f8a7f5-5c39-38a4-8ee8-762c932f637c | -5.0122 | -50.94307 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9926f444-07f7-33b6-94dc-9b47d37903fb | -3.15334 | -54.09416 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2df989a2-04b5-3eae-a767-97f6e0857f4f | -3.27034 | -54.01812 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29c026ce-6361-3a44-b6db-d17213e5d073 | -3.09906 | -53.77149 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7bc7cbe0-538b-3796-8863-f32b2a420c5b | -3.25044 | -56.8034 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6440ce50-bb86-3766-bfb4-39d35ce0aa59 | -3.0375 | -53.94894 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7f300ab-ccb8-3e23-8919-9bf7f0b26763 | -2.61066 | -57.58645 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce5ffde-f92e-3c66-bced-204dcdbd1b88 | -6.09506 | -49.41052 | 2026-10-08 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 44b592ec-11e6-3cfb-90cb-b1fdc4208031 | -2.9883 | -54.76853 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 775f5eab-82ab-3a8e-8200-d0a37ab3fdb7 | -3.52785 | -54.33259 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b580ae-f67b-362c-8a8f-33c31ea45339 | -6.07446 | -53.76573 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50cdd0e-c9b6-3750-bd22-111a98cb23b8 | -3.29429 | -54.07797 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19ad2541-7b7d-3e97-8c26-40bea5fdd320 | -3.80379 | -48.90507 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80efc076-46f7-3826-b286-1783a9c626a5 | -3.28394 | -54.05115 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15d191fe-6dc0-3c37-87d9-b9dc45b65000 | -3.17487 | -53.83865 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 453b11af-29bd-3859-a81c-f089b4c05a29 | -5.83403 | -47.40059 | 2026-10-08 04:46:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d079d35-91df-3910-a7e3-018e8ed2c5f4 | -2.47288 | -56.10448 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff343de3-d177-3383-b4da-a2cf0560de79 | -4.12703 | -50.83853 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46782c3-eed8-3701-9594-26de2679d329 | -2.9487 | -54.06098 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| addd01c8-ed00-3c9a-9a71-6147eb1186e3 | -3.1097 | -54.1548 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d390f618-0698-30ee-9a6a-0a7767d07a08 | -3.16663 | -54.74371 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cea9269-b158-36de-9fd9-7aaabbd66df0 | -3.02424 | -54.152 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e85acaf-134c-308f-9e5e-55cccab5b549 | -3.49934 | -59.27541 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cf9b3d0-a40f-3be6-963c-7c90e6ef7508 | -3.84557 | -55.97522 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7593ffe-668a-37a8-bb81-96cf5ea9181d | -3.28798 | -54.02533 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62280972-cdd0-333b-a2ab-38429ea49313 | -5.69603 | -53.50006 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fff6b405-f5c3-35ab-9ada-5ad658eb4579 | -3.73149 | -55.98286 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37e269f7-53b8-37a1-86e0-37921962e3f9 | -2.84738 | -57.46544 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1989c84-316b-3863-aa23-f4cae3b55a2a | -3.04668 | -54.26296 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfa059d0-9e91-3cfb-bcba-65f2d05d49fb | -5.34188 | -50.98804 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cf54ca4-d681-3e8b-81ab-54e1e5f282df | -3.84706 | -55.91573 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13f9d636-3368-38e5-86aa-d81d3bd210fc | -6.68751 | -55.09616 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56b60c06-4993-3fd2-845b-462ac499df8c | -3.02583 | -53.95155 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4a6e8c4-94b5-33e9-82c0-a69647a68f56 | -3.58091 | -54.68287 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 74e771cd-d438-389b-9ea8-f561a96ddd13 | -2.86768 | -54.16558 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ab12d09c-d084-3cfe-8c8f-c24f762bf518 | -4.26793 | -54.87714 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 418ff4ac-5890-3ccc-a533-77745073f9a4 | -9.79688 | -47.81671 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 250f5a11-e3a1-3f41-b408-1aa72d3bb9e9 | -2.75674 | -54.10836 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98f41a89-4b13-3bdd-85c1-750444d350d7 | -5.72953 | -45.15942 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 131b39fa-1cb3-3aee-aef0-27298b3f6592 | -3.01551 | -54.08751 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c495e08f-d23c-3c02-8cc2-9e3c65fd5475 | -4.00748 | -56.25734 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f6ff4f9-30ba-3093-8b45-d34ecfdf7829 | -7.53512 | -55.83184 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39ee9264-6a73-3bba-b2d5-757434756804 | -3.57859 | -54.67303 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6326bad1-4dc1-3a1d-bcf0-d654c06ada62 | -3.03579 | -54.52158 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71c19d23-c0e7-320a-90a9-57477c660d52 | -8.98305 | -45.91508 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README94.md)
