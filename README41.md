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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e9e76e-da72-32c6-bff9-7c48f9674bbe | -7.41193 | -44.35334 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5811512-2ae3-36bb-b246-80a4fccdb4ac | -1.97742 | -47.97868 | 2025-09-13 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0a3b5f3d-1b5e-3c19-9f69-36dc084fa413 | -6.38976 | -43.53164 | 2025-09-13 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cecc893-9376-3c9c-8cbc-eadcebd2076a | -5.90347 | -42.65071 | 2025-09-13 04:06:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ad63c482-54e6-3e94-aa90-df36634a168d | -6.18079 | -43.47926 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7017b467-fc0c-3b23-88eb-70294e66c666 | -3.48232 | -48.43853 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e8ced20-5c5e-3a35-9114-eb1c3e443bd4 | -6.46781 | -46.03604 | 2025-09-13 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03526be5-6178-3396-bca7-73d5e03de735 | -6.8334 | -47.86515 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23bbc113-f805-3876-b18b-178a99e65d30 | -6.69279 | -44.12061 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f531b043-7939-333b-a5b9-16021f136674 | -7.31901 | -43.92161 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fc252b6-4d7c-3ab1-ad69-9e195d2b9fb0 | -7.55291 | -43.95128 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 081dea5f-c4a9-3cdc-85ae-10157a305ae2 | -6.83269 | -47.8694 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 533c3a81-486f-3978-a307-acd1a08aad3d | -6.28885 | -44.24047 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 359540d1-6358-3e91-a5f3-e0714c8a6c92 | -6.26392 | -43.48458 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f1aafee-f652-37c1-93c7-d3bc69cf091f | -8.00976 | -43.81523 | 2025-09-13 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 348b82c8-75ff-33b0-9f7c-585084fb193e | -6.13075 | -43.28909 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cbd2f2a9-555e-3c3c-8279-9956dce1dfa9 | -7.41259 | -44.34935 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f064b332-5b70-39a4-aa94-38072454b18b | -7.50223 | -44.68479 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da5a9ce-2aff-3ceb-8dbe-bdc68a4e7c99 | -6.71933 | -44.02485 | 2025-09-13 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6cc6ab07-235a-3339-93b2-3bb99058ea87 | -6.11778 | -43.91137 | 2025-09-13 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74d515cb-3e5b-3dbf-8b4e-93b0a957f8d8 | -6.39183 | -45.64508 | 2025-09-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e737fa8-d506-3cdd-8634-e4b4454e4ea8 | -5.24826 | -45.57795 | 2025-09-13 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 891831ac-152e-3762-9ae8-9e4df85422c5 | -6.87749 | -45.64071 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bae66cc5-36a8-36ce-bbec-47f39178f02d | -6.25182 | -43.47552 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c2acbd5-1f99-3547-8873-51c9f8765ccf | -6.685 | -44.16399 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcdf9abf-3863-35fa-b002-1bc738ca4b0e | -6.15023 | -43.36442 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d3a0ac0-c120-3f2b-b4f3-05e7590a7587 | -7.52854 | -44.3719 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d34a0dbc-dde1-3f43-9618-5b8da99cb80c | -7.54262 | -42.66132 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ad0f277-4b3d-3a1d-be6e-7f11822edd2f | -6.88379 | -42.83195 | 2025-09-13 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 69a7b672-bc6b-3d91-8084-74993033344b | -6.61928 | -44.08079 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e82ad83-5730-3ddf-808a-0c458fd91b7a | -6.56054 | -44.77713 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd19e432-900a-391a-8df3-0799b7dd133c | -3.43618 | -42.46597 | 2025-09-13 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 03c489ea-bc30-3b70-90fb-1044ef5bd89b | -5.58732 | -35.71959 | 2025-09-13 04:06:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50b60bb8-9279-3e2e-bb0c-6cd1e062e829 | -6.24705 | -43.13394 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96d9eb01-c9e2-374d-9b5c-1afba3ce66c7 | -3.79195 | -48.6385 | 2025-09-13 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d221c477-d8ff-3203-86d5-4619e4767b45 | -3.24031 | -46.7911 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3c532fcf-6cef-311c-a596-707d9bda251f | -8.18015 | -42.41168 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 071ea038-7cc8-39a8-996b-206d25a468aa | -6.50779 | -43.80231 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0172cd8b-596d-3bc3-ab61-c50267c821b9 | -8.02899 | -39.59299 | 2025-09-13 04:06:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ede9dde9-806b-3038-a2d0-618100eceac2 | -4.08511 | -48.04358 | 2025-09-13 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c625e732-2e0d-3fc2-8c7e-f085d65b469f | -6.2145 | -43.33595 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2d0982d-f520-3c42-949a-91e62e97813e | -3.22993 | -47.12669 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3d732096-7d79-354e-bda8-ab6e84726444 | -3.95031 | -40.74082 | 2025-09-13 04:06:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4c5d7fa2-69bd-3ebb-92bc-16dfb7883f08 | -3.22757 | -47.63236 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 1066944f-a930-3de4-9f8e-fc5fad67657d | -5.65219 | -42.60394 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6d67f1a9-5e72-3f35-b85d-fbe308d41042 | -6.19995 | -43.44789 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d7d8360-20ed-3c6a-9bc3-749102a0f6c4 | -8.08845 | -42.56184 | 2025-09-13 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79b51b88-9cb2-372d-b98d-6c7a85ff31e4 | -5.72228 | -43.19037 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05f2064b-066f-3d8b-bf48-5072c66081f1 | -6.21365 | -43.45018 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e980f25a-8306-3d0c-982f-13c696ec267f | -8.32584 | -38.09454 | 2025-09-13 04:06:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c1d3f09-c2c2-3266-90a0-17686fff3162 | -6.13594 | -43.36601 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f8f3bc3d-aa31-349c-aba5-3b1d66cfe109 | -4.95938 | -48.18869 | 2025-09-13 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16013ffd-2dfc-3a04-9247-fc305de94fb8 | -1.97658 | -47.98382 | 2025-09-13 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d774f9df-b444-3b1a-b5af-59a48c2b0546 | -6.78557 | -43.40361 | 2025-09-13 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dbaab742-b2d0-3e19-b8b9-c951a394d29a | -5.34643 | -47.28811 | 2025-09-13 04:06:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65673098-a0dc-393b-b466-8c8d948d0c58 | -6.80029 | -45.63755 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54067299-bb4c-3059-adae-7a4cf691e5ee | -6.17818 | -41.13061 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f78f2d06-a74f-38d1-9f82-d90c75b9171a | -7.98207 | -43.66184 | 2025-09-13 04:06:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd79f078-2646-3254-b2d7-4db3ff44a161 | -6.24019 | -43.41626 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc2b2e2f-4ce0-3fc9-accf-a6203412d78b | -7.56875 | -42.64745 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87eace20-53ae-38ab-a6c5-3e4a07af91d9 | -6.1683 | -41.15033 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3158a572-582e-324c-8023-6f64b84f8909 | -5.71722 | -43.17827 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 69403d3e-cd68-3b18-8e07-213d39384ddf | -7.05952 | -34.97067 | 2025-09-13 04:06:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4cb6a658-561b-35ea-b9e3-8a4cdc6e8e20 | -5.72169 | -43.19403 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3130263-a84e-3bd2-8647-6c0a876941a6 | -5.41092 | -42.83821 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de940491-668c-384e-b847-5c93c22fc9a7 | -5.3507 | -47.28904 | 2025-09-13 04:06:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc4a8af4-71d5-35eb-ad69-a8dbf4ccf09f | -6.18019 | -43.48301 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49ab2d3e-8dc9-360f-ae2c-1cedc0254074 | -8.08513 | -42.5613 | 2025-09-13 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c63186d-df92-36f0-8a9b-1f957f05f071 | -3.43279 | -42.46542 | 2025-09-13 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2eaac03e-1d63-37d6-9324-e76c0a30fa0d | -7.54819 | -42.64777 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8db7436e-c195-34c2-9209-04e276019b86 | -6.19211 | -45.28262 | 2025-09-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50554199-c75f-36cc-936d-90e2e0f151c9 | -7.56819 | -42.65097 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7354c6b2-0d9b-3883-a34b-1d3c9ecd281d | -6.44634 | -41.75734 | 2025-09-13 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48251090-3ea0-3f4d-9776-c37ce9cb0770 | -7.44685 | -44.44859 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f36cffb7-f193-30d0-8ae4-9e75849c871d | -5.96819 | -45.84598 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd9b7197-8054-3283-9785-5f739fdd4d45 | -6.25081 | -43.4786 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70342724-6b6d-3ad5-a755-4ec86702b5fe | -6.80484 | -45.63363 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f07ab3-edee-3229-a264-4bfc4fc3698a | -6.28532 | -44.23984 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee7fb973-9c68-371e-b5ff-307578664cce | -7.43157 | -44.40941 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1d5f5ac-29ba-3214-9590-5aedd51ae805 | -6.32661 | -43.44502 | 2025-09-13 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 781f29df-b275-3e54-b3fa-729eca3321ae | -7.43466 | -44.86021 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fcc5338-9aea-36b5-b1c1-e6a5650c9721 | -5.91967 | -47.4305 | 2025-09-13 04:06:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 184f2b66-e29b-3263-aa45-9bc71fa50a63 | -5.40337 | -45.93542 | 2025-09-13 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 505a8b12-9544-3f75-9736-837f2749c847 | -6.99871 | -41.63581 | 2025-09-13 04:06:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33c08baa-b005-3a83-91dd-a2fc909897bb | -5.49215 | -43.99298 | 2025-09-13 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c998c2a-b8e7-3cdc-a9e4-2fa24f80db3c | -6.90728 | -49.40934 | 2025-09-13 04:06:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b8f135c-030d-3ca2-9760-955a40cef40f | -7.41128 | -44.35727 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3406e218-a3ef-3a8a-acf6-9735de9c0b2c | -5.07014 | -43.08089 | 2025-09-13 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b3c8704-84a1-3154-94e9-0e711313ced2 | -6.67915 | -41.68119 | 2025-09-13 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43d2694a-70cf-3e07-8874-ec3821110ae1 | -7.27123 | -47.00663 | 2025-09-13 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a99395d3-1537-3926-ba9a-007b06aeee5d | -6.2062 | -43.45278 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e324a657-e806-3827-be59-1fee7b2d62ac | -5.66112 | -42.61269 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2928e27-7f1c-397a-8834-602d00cbf198 | -7.50292 | -44.68062 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92e9882c-cbc5-344b-99dd-ba19b0b057cd | -7.51072 | -44.67768 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac78ffcf-fc37-3493-a8ab-433b1958a9fc | -5.64253 | -45.94547 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79a8dc92-740c-34aa-b42a-44d6a3dcff24 | -7.39929 | -44.34005 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afb27a26-96dc-359c-b37f-f37ff6882d00 | -6.35983 | -42.5374 | 2025-09-13 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3d268b96-fcb4-3ed9-b677-5398a4d79005 | -3.42825 | -42.47215 | 2025-09-13 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 89bc8af8-7c6e-3d13-9210-f53c15824951 | -7.15018 | -44.35763 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47a385ff-92d0-38db-b153-c375b611c337 | -5.72345 | -43.18306 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README42.md)
