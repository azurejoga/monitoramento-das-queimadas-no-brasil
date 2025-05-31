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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16b0c4cc-6a51-3fcc-bdc2-5caaf302439f | -7.8784 | -46.48669 | 2025-05-31 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8018f9a3-e987-3a3d-a3d5-42c5ff07f747 | -5.85133 | -43.63599 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caa67e31-1f51-321d-99e7-b6f782f8cc8f | -5.33204 | -44.96187 | 2025-05-31 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d0a13b-925e-3907-93e4-4f27409c7166 | -7.58247 | -45.87146 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed5c835d-615f-3638-a96a-1380da9e53d9 | -7.01249 | -44.62507 | 2025-05-31 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3382f855-6f91-3d8a-93a5-4fb60a233888 | -6.18313 | -48.06571 | 2025-05-31 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8fd630f-47d9-3dcc-89d5-4d54623fa26c | -7.5797 | -45.86745 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e632f483-4add-3682-a595-64f0ae863e4f | -6.33868 | -43.38431 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 112e8d80-39be-3fc9-84f7-466eedfd5523 | -7.47959 | -47.05381 | 2025-05-31 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f880ef0d-4f2b-3e4c-a4d3-8030d2cf6abb | -6.82872 | -44.65394 | 2025-05-31 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 120b2852-5f94-38ba-8e29-9b5290a6eccf | -6.54722 | -47.80687 | 2025-05-31 04:25:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62a1e80a-6f7a-3726-9ba2-6c2f0ec0f4ae | -7.4312 | -45.41948 | 2025-05-31 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81dab5e4-205b-3286-91f3-399329b5a726 | -8.08938 | -46.28627 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e04d80f5-2abe-3c87-ace9-0d5f86dcfda1 | -6.20518 | -43.33225 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bbd728b0-eb73-3bb0-96ca-d021e59cc91a | -7.61603 | -49.93233 | 2025-05-31 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5593ff6b-03fb-3cc3-bdd8-0ebcf474f620 | -6.15475 | -42.61279 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 8e353a6d-aa5d-37fb-98be-d20c3bd5121b | -4.82248 | -44.35748 | 2025-05-31 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6336e4be-a377-34ec-bdcf-05d451f0ad36 | -5.85365 | -43.64431 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02081617-b2ba-3fda-bb57-74ff14d52dfd | -7.22738 | -43.12931 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb55500c-6db2-3b6d-a582-8520d0a80bfc | -7.58355 | -45.86449 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3bf5a6cd-1809-3663-9b43-369cd4548383 | -8.79186 | -48.80634 | 2025-05-31 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27ac37fa-e7f2-39e5-affe-32cde39e2878 | -7.23439 | -43.25602 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9d1ebcdb-b0ee-38eb-a208-e02317ff59d0 | -7.01079 | -44.61345 | 2025-05-31 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ceacc740-21ea-3ec9-b8f7-153b5d288f3d | -6.69194 | -43.68351 | 2025-05-31 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1df97284-5123-3990-9c64-a9b6c79374fa | -8.47481 | -49.6041 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ac6d012-68d0-3015-ae84-4001e0b8be86 | -6.21109 | -43.34146 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddcb7c49-cc29-3e9b-b2d7-581ff26adb56 | -7.31062 | -55.3097 | 2025-05-31 04:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e034610-9a48-34a7-bcaa-43b28210613c | -7.24406 | -43.0924 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff88b19e-9fe4-3c45-85be-a82c13d527c7 | -4.50458 | -46.07951 | 2025-05-31 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72c578c4-2a31-3f4e-bf0c-8a8d427001c4 | -7.58633 | -45.86849 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93b5e6fc-ec31-3376-8159-f6728bdea52f | -3.14603 | -49.49006 | 2025-05-31 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 046a899e-6913-3beb-8345-4760fcaeb078 | -8.20559 | -49.80364 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd70e86b-a2ce-3d6c-93bd-19b816e52614 | -7.98175 | -49.68977 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 788d190f-acb8-3d52-b724-a3e53db0ba07 | -7.22374 | -43.12876 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f3efbea-d49e-3aec-9c55-fb564538e1d4 | -7.00739 | -44.61285 | 2025-05-31 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 26f12e23-809a-3fb0-8fee-9ddbb44d7b89 | -7.08384 | -46.03896 | 2025-05-31 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23db7314-322d-3dfd-a571-b71520d1db16 | -6.18255 | -48.06937 | 2025-05-31 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 994f1c3e-e8ef-3587-a770-ea264823c868 | -7.21709 | -43.12336 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 997d8811-4d67-3c15-87b8-72f6500c9914 | -8.47128 | -49.60352 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 10f96a9d-aff4-329b-a70a-68e7d93a6999 | -7.21946 | -43.13247 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 07ee4e16-ddfa-3b0e-aa15-3c100e2a4f73 | -7.67316 | -48.37758 | 2025-05-31 04:25:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 961ea410-9135-3db2-b468-36effb9be271 | -7.29686 | -46.7448 | 2025-05-31 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 254561a2-c56f-36a5-b27d-7bf0feff7707 | -8.67539 | -48.28808 | 2025-05-31 04:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b73e7926-f5ea-3c0f-841a-c1b7f0acb692 | -7.24707 | -43.09725 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6aefaab8-7674-3cfe-a7ad-90057b9fab4f | -5.43169 | -47.53839 | 2025-05-31 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e407b2f-e5e4-300b-b55c-051f0586d2fb | -8.09269 | -46.28679 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97341a3b-7030-3d96-a5bb-77a71f253652 | -6.61779 | -42.84962 | 2025-05-31 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 551d086c-6c34-3632-848e-494d9f19e382 | -6.82996 | -44.65352 | 2025-05-31 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f215417c-a46a-361e-a45e-4fc2e91a011b | -6.15411 | -42.61716 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a642d7ed-425b-3bfc-b5e2-88718e6c9a4e | -2.44871 | -47.49268 | 2025-05-31 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95b93d08-ee6d-3943-adc1-79d80b08fcfa | -8.19586 | -49.80321 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d20964e5-1fc1-3f68-881e-58fd84773274 | -4.81965 | -44.35334 | 2025-05-31 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d87978cd-39f9-3c7f-afe7-cf4fe8c11c38 | -8.47901 | -49.60066 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e776eba-5861-38ab-b052-722b2925dc2b | -5.41645 | -47.56911 | 2025-05-31 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bc1cbfa-cba4-3095-a263-1ae97ff320bc | -3.04567 | -49.4384 | 2025-05-31 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad259685-fdfc-3548-9f5c-297177f74206 | -6.82929 | -44.65024 | 2025-05-31 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cba1410e-32b4-3052-a211-c17e9d10be49 | -6.33513 | -43.38375 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e7715e8-2a85-3a66-99ec-8503725ad367 | -5.85074 | -43.63988 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72e4f7ed-4b8d-35a6-a7f6-9f8a15fc948a | -4.42412 | -47.66528 | 2025-05-31 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e889053d-55f0-3651-ab4e-b2deee9903d0 | -7.43453 | -45.41999 | 2025-05-31 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31fa1534-a4ff-38dc-9519-2f8e609e4be3 | -4.87484 | -47.4063 | 2025-05-31 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba5f4d8-54eb-3b0a-89e9-b3ae04dee49c | -5.21555 | -43.31475 | 2025-05-31 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 576e3bf8-e6ca-3080-8c03-7e924dbc256e | -7.31276 | -47.03091 | 2025-05-31 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c42a403f-48c7-339c-ba94-acc70b4a2188 | -4.48771 | -47.79182 | 2025-05-31 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f1c50de-c6cf-32d8-8f95-f46907e80e29 | -7.25247 | -43.2588 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b85bb9af-5733-3ab8-a021-ac0355b03dad | -7.99149 | -50.68408 | 2025-05-31 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cfe5e9a-eb7c-3ea2-a618-f4ebba8bc308 | -7.22073 | -43.12392 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8939361c-4b94-3702-af3d-e36b69d00625 | -6.15538 | -42.60842 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9653020f-74c8-3e0c-97be-be0cf104f24b | -8.31953 | -47.91822 | 2025-05-31 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9f97b26-5523-3633-b40a-2a5867e456a4 | -7.2231 | -43.13303 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 04926908-10b1-3df9-b04f-656a45f7bd11 | -7.87993 | -45.99321 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88448b9e-84a3-3e77-85e0-24396367d1ca | -7.95542 | -46.16526 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd533bb6-d495-3fd3-97ff-cfc9a4faad34 | -6.1532 | -42.60575 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43ce0357-e2b6-3e1a-933a-406e6e6cbf77 | -7.25345 | -43.26147 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0be68e0-f26a-350f-94d3-e92017f85912 | -8.47062 | -49.60754 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b06a36c2-5907-3fa6-bc9e-1b59510774a6 | -6.55991 | -44.48894 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 11152f0b-3fe5-3a34-bedf-9701114d0cea | -7.23102 | -43.12988 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 239a9ed6-3262-3349-a767-887c2b0db93d | -8.47548 | -49.60008 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ce083397-f2f9-3163-9086-1d1d0a7d0bca | -7.08553 | -46.04985 | 2025-05-31 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc708f1-e129-313b-a8ca-a5d392a7683e | -7.58024 | -45.86397 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 390ee00b-5077-3aa8-80d6-ef1f3c894623 | -7.22865 | -43.12078 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a4b9629e-7779-33d2-90f9-636b2c9e9c9c | -6.43206 | -43.53312 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 085dcb1f-d858-3d99-878f-e6c42ed070b7 | -3.04941 | -49.439 | 2025-05-31 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 938b30d2-8baa-3c22-98a2-67b7fa8d97f0 | -9.04666 | -47.02081 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bac0388-0635-314e-802e-081e722aee2f | -4.48823 | -47.7922 | 2025-05-31 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e581f641-772f-323a-bab6-f36ea6735ea0 | -6.2123 | -43.33339 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29a78120-0608-3ada-a47a-2c5757e7297f | -4.41089 | -42.13834 | 2025-05-31 04:25:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac5aa602-9b63-3532-9039-3825ec320366 | -7.95596 | -46.16177 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e01ac00-c6bd-3d30-9d4c-6f6a61540476 | -6.21615 | -48.52195 | 2025-05-31 04:25:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c492d4-7cda-3e82-b716-66538c2abcfa | -6.34224 | -43.38487 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9ede5f5-59eb-34f7-b70e-bb6232f66647 | -6.15624 | -42.61065 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5e827004-67e1-32cd-8465-04b06bb09709 | -8.65963 | -47.81331 | 2025-05-31 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff1b5e6a-eb14-32c6-b70b-822d965c12aa | -6.83051 | -44.6498 | 2025-05-31 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87936a39-2176-321c-9acb-5247c7ca542e | -6.15188 | -42.61449 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| bd551504-f7b6-395d-b66b-b5207b637a01 | -8.79128 | -48.80674 | 2025-05-31 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3014941-55e6-32c0-9c0f-708c1e1ff06f | -7.93664 | -45.42515 | 2025-05-31 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39c16e9e-1d6f-367e-8d0d-aa10e9032a09 | -6.82591 | -44.64967 | 2025-05-31 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 721c5c39-bafe-3559-b957-cc36dbb6e5b4 | -7.25406 | -43.25723 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5deada86-a774-3999-bc5c-50c5a6f8dfc4 | -4.87698 | -47.40707 | 2025-05-31 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f67267c-ca84-3500-8f2a-d23cc59121ae | -6.56047 | -44.48526 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README8.md)
