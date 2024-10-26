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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d0ced85-dac9-39fe-8930-4f5389880fa3 | -3.5812 | -54.66402 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 635c75d3-e888-3c40-9089-01632fabfdfe | -3.58063 | -54.63346 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5487cd65-e2fd-3f21-b8e3-35ba1c2cc531 | -3.57934 | -54.63308 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9201edb9-1b15-3c25-8da1-28d662d9a41a | -3.57891 | -54.63606 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4eb03b4c-3cd8-34eb-87a0-5b70de99991d | -3.57558 | -54.63257 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d027bea5-63bb-35b8-ba56-6ee32f165c83 | -3.57513 | -54.63554 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c3c7173f-fdff-3a88-a2ec-d00cff121b6b | -3.57204 | -54.58686 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00f5036a-56b2-3d1f-ab83-3bd7f45e853a | -3.5716 | -54.58984 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f03e4e6a-f26d-3e43-99d6-d360d81dc6e3 | -3.55378 | -53.99034 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a59b7b24-dff8-3207-b956-40ab06928799 | -3.55329 | -53.99361 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cab276a-aef8-3e38-9d06-1c22b2ecdfdf | -3.55284 | -54.43391 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c4c081e-3558-3942-8681-4c3f0239ff86 | -4.50026 | -54.96197 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f867bdb-36d8-3214-843a-4c313456df97 | -4.49982 | -54.96494 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c33c99-f0bb-3b25-afbe-05c79aaf8f80 | -4.4831 | -55.08021 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8312107e-d7d4-32a3-9b07-32135fd570b9 | -4.34596 | -55.36045 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7b7989da-1931-3123-979c-ab2f777b84e1 | -4.34309 | -55.35993 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 33f6005c-3abe-3916-ba80-dd8a9547cf0c | -4.30262 | -55.08723 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f58eb3-5043-34b0-857f-f099b72813d0 | -4.29764 | -55.08647 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 506dfc25-142b-30bb-8dc4-29b2b45882e2 | -4.29725 | -55.08919 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30646a9-df92-3b82-aaa2-ea0338dbf86b | -4.07414 | -54.43571 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2696e7cb-8a67-30ea-91fd-f3d6a8298a69 | -4.06896 | -54.43492 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d19e2a6d-e58c-331b-a673-0731ab496957 | -4.037 | -54.5475 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7327d4a5-3103-387f-81a5-0caa46215b0d | -4.03656 | -54.55061 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f33c2d7f-7ec0-3cd1-a1d2-15ce97d9d07d | -4.03611 | -54.55374 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92c3631e-777a-371e-bb3e-4756f4503295 | -4.03426 | -54.54937 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1141b0b3-d652-3702-9ee3-0aea62a27289 | -4.03379 | -54.55248 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0346d3f3-b93f-3f95-ae5e-c8dc88bbcc59 | -4.03244 | -54.61611 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05464a37-9a1a-3bbb-9538-80fc8488a7cd | -4.03199 | -54.61924 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a2936c3-b8cb-3e5b-b103-dee7c431286a | -4.03142 | -54.54979 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0199e784-2fc4-3a4e-818c-52fae327cff5 | -4.02502 | -54.61075 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd58b2c1-4349-355f-8d27-76c79cdc39af | -4.02308 | -54.6084 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da3ec79a-a71e-3304-80d1-2c6be8d6820f | -3.88534 | -54.1428 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 316b5426-370a-3ded-828d-c872451a41d4 | -3.73942 | -54.48368 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd2239d7-7dc2-3d5c-9ca5-59ab0a5680cb | -3.73895 | -54.48692 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18acbbcb-e39e-346e-a36e-12b4c43e4c72 | -3.68112 | -54.29244 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93980f6f-849e-3416-a54d-4f53c2f95b7d | -3.68067 | -54.29553 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec691257-c915-35c9-aa6d-a7bc800a1151 | -3.63953 | -54.68257 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6289fcd-3864-39c1-9658-2fa3ca1a3f1a | -2.03815 | -55.7599 | 2024-10-26 05:36:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83df02a8-e826-3b1c-a978-63afa52c6b30 | -1.96473 | -56.39803 | 2024-10-26 05:36:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bac2429-e7c8-35c1-97ec-7f1173701079 | -3.63407 | -55.51088 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 28888d1c-a8c6-3841-9e53-95f491a42909 | -3.63329 | -55.51612 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c61c66f3-adca-3272-9f44-70052bf81a2a | -3.62927 | -55.51027 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 023f369c-77aa-342a-8c38-ea653aad39e7 | -3.55959 | -55.45097 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 117b8af0-fb68-3162-91e3-5d3cd36f4baa | -3.55943 | -55.45404 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0e46082-f504-3fff-9d19-0ab2a985a808 | -3.55462 | -55.45344 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bd39fc6-6b6c-39b0-932e-50a74d096654 | -2.42832 | -55.63551 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8884a605-6d6d-3934-8bae-0e170eb20abd | -2.42757 | -55.64045 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53e7a61c-2edb-3cd6-943b-0a01054d5ac4 | -5.07605 | -56.22674 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 483e8151-aa80-3cb5-b9ee-f2c8bdfdc45b | -5.07499 | -56.22409 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e45d267-3e6c-3790-a16d-b930b902bb6d | -5.0743 | -56.22903 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1297158-0e7b-32f7-bfc5-d818f50df196 | -5.0714 | -56.22599 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d170ce7-b115-3e20-a0fc-e528ad41112e | -4.61556 | -55.90312 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1688b6ce-c61c-3d3d-b6b8-ec15581cf58d | -4.61085 | -55.76681 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2233f07d-53e9-35a8-aebd-cc3a4e739db9 | -4.61059 | -55.76575 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6112809b-48d9-3750-991f-0c163c2dfdf2 | -4.60607 | -55.76618 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fccd4a52-ce3f-37b8-bbbb-e67fe27e34dd | -4.60581 | -55.76512 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796e6eb0-dcd9-341c-9c2e-a02568f8677d | -4.58145 | -56.10619 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13adbe4e-a9bf-3bd7-aeee-8bc28ad34cf9 | -4.5296 | -56.01761 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69d6c2cd-5ab8-366c-a804-d352167db13c | -4.51444 | -55.82446 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a487e6d1-3155-3966-a71c-d70452857f15 | -4.5137 | -55.82959 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c58c5cd-d04e-39a7-bd87-516b4c92552f | -4.5078 | -56.00307 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ca1aed0-6c24-31d4-8a31-af11b04d6787 | -4.42457 | -55.70044 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7884515-ee93-3514-bc77-de8f3eac623f | -4.21553 | -55.72282 | 2024-10-26 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d37a646e-581c-3a75-b8bd-d086edb98e12 | -4.04065 | -56.27803 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f13e41d-2f18-3f2f-bde6-bd3d85bd7f8b | -4.03998 | -56.28256 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30e924bd-c599-37c1-ac77-998af2dc9e5b | -4.00619 | -56.25842 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bb267e4-de2a-3ce7-84fe-1d655c9f1917 | -4.00313 | -55.73417 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 901019fd-9e32-3bbd-bfd7-419f72572251 | -3.99834 | -55.73381 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 371ef1d1-2a93-36d7-9c82-7852ea1939b3 | -3.92239 | -55.92694 | 2024-10-26 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b3bc3be-1f83-3fc3-abff-9b312912fa35 | -3.91992 | -55.92517 | 2024-10-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be5ddf60-153a-3e17-b26f-720d3a56e435 | -5.30214 | -55.99456 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e726a59-3aea-363c-a3f6-bc2592059b64 | -5.25359 | -55.96132 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7f8b714-46dc-39d4-b873-33422b734cdf | -5.25286 | -55.96644 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e59be721-0047-3e52-9fbb-8d6fff9924c9 | -5.24811 | -55.96571 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5cea5ff-5708-3b3a-a6e3-f721bdbfd786 | -5.24336 | -55.96501 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac333e4-a4c5-3f71-874d-3978abfa18b6 | -5.24264 | -55.97008 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7385306-79cc-3695-b090-d7c70d8cd973 | -5.09848 | -56.19272 | 2024-10-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c50eabb6-2053-34e9-8fbb-4482b76cd88a | -2.10906 | -56.66903 | 2024-10-26 05:36:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9281622-40c3-36c0-88eb-d33f10f2d01a | -2.7316 | -57.46787 | 2024-10-26 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 149f19d2-8b4b-3da2-a7ae-b554eae709a1 | -2.73053 | -57.46669 | 2024-10-26 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b59ba33-01b6-3115-928b-3ce289f737e5 | -2.72805 | -57.46354 | 2024-10-26 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ddbff97-d4eb-3a23-b274-175122ce51a0 | -2.72748 | -57.46724 | 2024-10-26 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1a4c3e9-9944-311c-bb92-cd93a30ea1ad | -2.72336 | -57.4666 | 2024-10-26 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdafb4a8-3a0c-3a65-9463-a0de3b7314e4 | -2.72278 | -57.47031 | 2024-10-26 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48e9694b-ebf7-3cb1-9292-6f3ea49d3638 | -2.53418 | -57.31628 | 2024-10-26 05:36:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 612fb54f-0664-3a19-a0f7-830a9049ef75 | -2.5336 | -57.32003 | 2024-10-26 05:36:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eccb3f7f-7937-34fa-86f7-f154be1842f7 | -2.53184 | -57.31841 | 2024-10-26 05:36:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc4301d0-197a-3ed0-b75c-4dc9f6d12618 | -2.39874 | -57.89627 | 2024-10-26 05:36:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ea8d1e0-782f-3189-99b5-43fe91f8e9d1 | -6.3319 | -58.3119 | 2024-10-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf275ad-8a01-3bcb-a9ca-9340fa227767 | -6.33137 | -58.31559 | 2024-10-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17bfd94a-75e7-3072-91f9-6469074f0bfe | -1.88055 | -59.56201 | 2024-10-26 05:36:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e29f331f-937c-39f8-ac27-01207c9b60d6 | -3.08305 | -59.12102 | 2024-10-26 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d0bd3aa-bdb6-3f51-a889-62e7cfce40f2 | -3.42021 | -59.63346 | 2024-10-26 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02103948-17ad-3b10-ba92-7ef83b20fe20 | -3.38183 | -59.54199 | 2024-10-26 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78c9806c-f2d4-3e95-9823-4eaacbe8d31d | -3.37817 | -59.54143 | 2024-10-26 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 905a8bb6-d2c5-3eb9-8c37-3f66c815ea56 | -3.15867 | -59.82724 | 2024-10-26 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0e2d445-d8b5-306e-84f9-8101960b9bdc | -4.29606 | -59.98633 | 2024-10-26 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a98b4ca-2894-3dfc-89ea-df5a6c7330b9 | -4.15994 | -59.89111 | 2024-10-26 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a651a057-60df-3664-8ee3-120f2603b347 | -4.22719 | -59.94328 | 2024-10-26 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1cc91718-e079-33ad-8e6a-77d22f2b7d5d | -5.60082 | -60.24477 | 2024-10-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README96.md)
