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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3d3b419-5254-30b3-a74b-f6db0748ab66 | -3.5996 | -54.560799 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91656bf4-378b-3d96-988c-525f8fcf6358 | -3.002 | -54.120499 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd2ccda5-5176-3adb-8f7b-f00798ed013e | -6.7849 | -56.2463 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08501d2c-d868-396e-b854-d9bdb4fe8dfe | -3.0972 | -54.174801 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a268fc-b760-3bd9-a1e2-352fcbfcf3a6 | -3.0654 | -54.215599 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fcd4bae-8398-3a2f-a6fb-c767ce60e6f3 | -3.0249 | -54.1744 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2d7d674-7285-3b82-b5ee-391cd824e34d | -8.914 | -49.968102 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5a60c70-287e-3e9a-90a1-5b52d1fd47c9 | -3.1772 | -50.575802 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50a6369-01f4-3b9a-bc2a-204f8a18646a | -2.9004 | -54.126701 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a485a5a-2d66-37e0-9bdd-de861bd8c100 | -3.3866 | -59.514 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1c69329-c2b9-3834-b2eb-5dddeba77884 | -2.3752 | -56.133301 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e6b1581-b985-3c2a-a662-47e060185f01 | -12.4835 | -51.297401 | 2026-10-07 01:09:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b25c748-892f-3f97-99ae-daa9f2f4cf58 | -2.7618 | -54.107101 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25004155-09ae-3063-bad1-32ca4d892480 | -3.4463 | -56.932301 | 2026-10-07 01:09:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49753a19-16b2-33eb-8fa1-8fd0204ebd26 | -3.5077 | -54.6535 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e6fb0d2-4231-346c-ab1a-deeb2c2e171d | -7.1837 | -55.1101 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d8505ad-05d9-3cb1-8dd2-8fcb8768f71a | -3.0329 | -53.8992 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3548230-85c5-3be1-bc8c-7b1ed56af154 | -3.3871 | -58.204201 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fda7cdf6-edfc-308f-8f09-ce96294aa186 | -3.2687 | -54.025799 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7375e069-e1af-35b5-9d8a-85ded1c63725 | -3.4842 | -54.730301 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86386e41-e30d-389c-a7ff-83ddf02876e8 | -8.2865 | -50.2731 | 2026-10-07 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 2363a78c-7416-332a-b1c5-6768ba49835e | -2.7796 | -54.0937 | 2026-10-07 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 232.6 |
| dd54eff0-adb1-3d4e-bbc5-2f3075b57e2c | -11.0137 | -45.4501 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| a5968149-a1c9-3c5b-92fc-b52f74f386a1 | -8.7225 | -45.204 | 2026-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| cd789298-0720-338a-afd4-a172d3e86dfa | -11.065 | -45.8084 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 678a2933-4abc-329d-8abf-d776c70d5709 | -9.4621 | -67.0817 | 2026-10-07 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| cc9454be-736c-3247-acab-68ab1b93f4c6 | -3.0 | -54.1287 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 268e26c8-fbaf-3438-b046-e49e360d27ee | -3.1787 | -50.5807 | 2026-10-07 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 78bb5de3-5e30-3ca1-a0c8-85da4e4ededa | -8.7033 | -45.2289 | 2026-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 27a88309-973c-337f-9ad4-29b8d37acd19 | -12.1746 | -44.7051 | 2026-10-07 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9828d903-99f6-377f-9d69-46ea60e4913a | -5.7187 | -45.1773 | 2026-10-07 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1424eb4b-73fa-3248-9973-8bb9276d7aed | -12.1939 | -44.7021 | 2026-10-07 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| faee0b3e-8e23-3474-b45e-50e94e1c4ee7 | -3.0373 | -53.9469 | 2026-10-07 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b92d9368-7175-32c7-a2e1-a8c487d7c251 | 3.1463 | -60.5937 | 2026-10-07 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9c3d7a58-d83b-3a23-a912-99146e44482b | -2.7796 | -54.1138 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| b3c95c46-5e2b-3e3b-80f1-dc59ff0ec99c | -2.9448 | -54.1501 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 7e9270a6-a00b-3ad2-9acd-f9fc2bf01706 | -3.5126 | -54.6762 | 2026-10-07 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 94f47c4c-33a2-3ede-8986-57276756db67 | -3.6579 | -60.6412 | 2026-10-07 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c8c8d669-3651-3a29-8e42-ff79e779ddfe | -3.5127 | -54.6562 | 2026-10-07 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 26bf074f-6a67-3f26-ad78-e132a108f67f | -3.0374 | -53.9268 | 2026-10-07 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1eea43fb-9d0d-33e8-b430-675a6dcf1052 | -11.1043 | -45.7347 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| be1dda44-257c-3e1a-97be-41c8b1b63f72 | -3.0184 | -54.1282 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c316828d-9901-32b0-be06-037c96594079 | -1.801 | -57.1161 | 2026-10-07 01:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9139ec34-b47f-38bf-aeb7-01486e8b8624 | -4.7589 | -55.6516 | 2026-10-07 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c4321347-e6cb-3a2e-9172-3ab8492e6339 | -3.055 | -54.1474 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f87f8ad4-6491-3c54-afde-cbd1c8496381 | -3.4577 | -50.089 | 2026-10-07 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ac0cf4c9-cc46-3e05-b88b-aacbab5fa494 | -8.7228 | -45.1812 | 2026-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| f084efd4-11bc-3e64-b3f2-e297b787bdb2 | -3.1114 | -53.7839 | 2026-10-07 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 4ec45399-ce46-3506-b48c-eeafb3b46ac1 | -5.9838 | -40.9123 | 2026-10-07 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 477c8afb-4f8f-32e6-80cf-a00ef3063779 | -2.7613 | -54.0941 | 2026-10-07 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 4d15ba43-affc-349d-8b94-58771bcf1ae1 | -11.0646 | -45.8312 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fccdf062-1010-3c6a-b063-70e2e90b5c63 | -6.0075 | -53.5122 | 2026-10-07 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8791f708-e92c-37cf-9bb5-f830276239d7 | -8.7039 | -45.1832 | 2026-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f402a171-1bfa-33c1-be1a-42c17d31a3e6 | -14.2531 | -41.6256 | 2026-10-07 01:10:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 128.4 |
| ce2167a1-d386-33dc-8fdb-46a95d3ff7b9 | -7.7551 | -49.2067 | 2026-10-07 01:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6895fcd8-aa75-3627-88fd-44d652740839 | -2.7797 | -54.0736 | 2026-10-07 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ff1d1f01-915e-39ee-be5d-7d36123e81b4 | -3.0001 | -54.1086 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 71cf014c-adff-3aac-ad5c-5f5c80172566 | -5.7374 | -45.176 | 2026-10-07 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1ab79d61-99c9-3ee9-b955-22316d627910 | -3.0375 | -53.9066 | 2026-10-07 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 0dba96d0-6b34-3e9b-b0e2-19782445db24 | -5.9647 | -40.9383 | 2026-10-07 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| d45e1c93-75a9-3717-bfb6-6d86e998395a | -5.9835 | -40.9367 | 2026-10-07 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 197.4 |
| f6871ee7-2838-33d9-847d-55c4828b9c77 | -11.7528 | -43.646 | 2026-10-07 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 447d8ba5-d1be-3310-aa3e-a12fd22435f3 | -11.7143 | -43.652 | 2026-10-07 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b00019a4-cf80-3019-aaf4-d207ed66cb3d | -11.014 | -45.4272 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3326d084-9a1a-38ae-94fb-2db336a39134 | -3.531 | -54.6757 | 2026-10-07 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 58e0622a-4d6f-37ec-b8c7-7c228ca805b7 | -1.8011 | -57.0967 | 2026-10-07 01:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| efa6fdf9-4703-35e3-9be9-02eb4d6bcd99 | -3.1787 | -50.5597 | 2026-10-07 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 6c9fbcad-8a73-3e32-adaf-8304e4d0d2c2 | -5.7189 | -45.1547 | 2026-10-07 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 61f1869c-7a84-32d6-828e-c954ef098182 | -3.1972 | -50.5592 | 2026-10-07 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 613d343d-8892-3bf9-8a88-2386ac7026e9 | -2.9447 | -54.1702 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1eb67f62-b95c-3375-ab6d-9c10a124d099 | -11.7335 | -43.649 | 2026-10-07 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 674380b7-08f3-37cf-ac05-9f25257211e6 | -3.5311 | -54.6357 | 2026-10-07 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f4e2cf85-ac4b-3324-91b3-4862e4b01625 | -2.7612 | -54.1142 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 7464c002-07b4-3d03-9fb1-990a64813d65 | -3.1115 | -53.7637 | 2026-10-07 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| cc40517e-7548-346e-90b5-b0800fa539a2 | -3.1101 | -54.1661 | 2026-10-07 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4c2efc84-9be8-382a-a486-0518ea8f0cb2 | -3.5515 | -59.4807 | 2026-10-07 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c96351ec-4f98-32bc-b8c4-f78e1d5a82fc | -11.1047 | -45.7119 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c0fda2dd-48db-33bb-90c0-9a64bda78bc5 | -2.7874 | -51.6719 | 2026-10-07 01:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e792b5db-3183-3b13-b685-20fa9ad984d8 | -3.8567 | -55.9769 | 2026-10-07 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| e7e6a92c-2aec-3066-b984-397495e3584a | -13.5117 | -44.368 | 2026-10-07 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5a121e17-7a55-36b7-97f1-5d9ebe658d67 | -3.658 | -60.6222 | 2026-10-07 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 79bd3bb6-468d-3974-8023-1729a46c4d22 | -3.531 | -54.6557 | 2026-10-07 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| f426559f-51f9-34ba-b7b5-6d55b60dc2fa | -12.1742 | -44.7284 | 2026-10-07 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b844f98f-9bbc-38d6-a0ca-68271020da61 | -3.8566 | -55.9967 | 2026-10-07 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| ea4d187e-c25e-32b0-9ee7-e12c7d1fade4 | -3.5127 | -54.6362 | 2026-10-07 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 592e0336-dfa8-3ab8-b5cc-64c0af64f7e4 | -3.6762 | -60.6219 | 2026-10-07 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2504206c-dbf1-399b-b9dd-9ce1a5e5fccb | -3.8997 | -59.3198 | 2026-10-07 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e7549766-6f3a-36c0-a174-0e29549c7ae6 | -8.7036 | -45.2061 | 2026-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 189.2 |
| c100dcca-51dd-3a6a-a18e-79083641e033 | -3.4763 | -50.0673 | 2026-10-07 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7bf67e37-e09b-353b-9883-391c198da308 | -5.7376 | -45.1533 | 2026-10-07 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8e80d3ec-dd08-33e8-b546-42d02ab3535a | -2.7613 | -54.074 | 2026-10-07 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1b11ce3f-c612-3e85-8e38-3ba42d05daf5 | -10.9949 | -45.4298 | 2026-10-07 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 3f8646fd-2418-34e1-989e-e8a627660f97 | -3.0558 | -53.9263 | 2026-10-07 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 98d31a20-e572-3df7-b35b-5162238e038e | -3.4762 | -50.0883 | 2026-10-07 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| fec1286e-0b12-348e-86ac-0254cd848ad0 | -8.6847 | -45.2081 | 2026-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 12dcbdb5-66a3-3264-b37c-9d5361e06c24 | -3.29 | -54.07 | 2026-10-07 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e9cb9c-2e49-30f6-aefa-d2d7478aa286 | -12.16 | -44.73 | 2026-10-07 01:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb8eb0d-dd3b-306e-8e8d-9759cc282d54 | -8.7 | -45.24 | 2026-10-07 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8427ef-4302-3ce4-806b-2236d76ca3c7 | -12.19 | -44.73 | 2026-10-07 01:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10d6457a-4aab-3a71-bc33-8e924827cd43 | -11.72 | -43.64 | 2026-10-07 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README24.md)
