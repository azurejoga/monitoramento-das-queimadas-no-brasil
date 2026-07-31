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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64eefd53-e298-3f2d-a2a2-c6ffcdacd1d4 | -7.61368 | -45.18746 | 2026-07-31 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b1b0db-6723-31c2-86f7-8a515f42621f | -6.29323 | -43.82574 | 2026-07-31 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a19ed9a9-04e2-3c6b-a9f9-476a1b62fab0 | -8.90228 | -37.97101 | 2026-07-31 03:53:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d546056b-d9f1-3019-8efa-02fd8b75c0e1 | -10.85777 | -40.46407 | 2026-07-31 03:53:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03f9eae8-1572-3245-9f85-f9799739a40a | -11.2521 | -40.34458 | 2026-07-31 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| abbe1b98-4ba3-3ca2-9ea7-859e734f46ae | -5.7192 | -48.12455 | 2026-07-31 03:53:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e539bc8-bed1-38f9-bb89-7ace86dab39a | -9.63491 | -40.60234 | 2026-07-31 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c129db22-7420-3497-90fb-c500f188941b | -5.04558 | -43.26758 | 2026-07-31 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a80ac454-7d9b-3a2f-a5b1-027ef2aa0336 | -5.75371 | -43.2661 | 2026-07-31 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9397df78-e26c-3d55-b095-5a795492cb82 | -4.90259 | -43.47636 | 2026-07-31 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d46bffd-c6ef-38ba-82f6-79aa155c37d9 | -10.84767 | -44.55647 | 2026-07-31 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee92e09d-7763-3b52-8773-dcdb1107eddb | -7.61863 | -45.18807 | 2026-07-31 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9636469-dcec-36ec-b88c-e4650609f721 | -9.63135 | -40.60173 | 2026-07-31 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| baeb81ca-ce7b-38f2-a17e-36302435787d | -5.66814 | -43.56727 | 2026-07-31 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e44259b4-53c3-3a97-a0e7-c67c2fea9b54 | -4.90873 | -43.4677 | 2026-07-31 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6d4d9141-9db6-3103-b5fb-49c536e49dab | -9.07908 | -46.0644 | 2026-07-31 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 669d2897-a7e6-3cd8-b2ce-dfe83d02ef48 | -4.91329 | -43.46845 | 2026-07-31 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 072d65f2-33d4-3365-8787-5d7e42456e50 | -4.36884 | -47.77436 | 2026-07-31 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3faf928-e2df-368a-8d71-db62750ac35d | -7.87478 | -45.23223 | 2026-07-31 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a531834-6e1b-397d-8bdf-4d88edce0270 | -7.01061 | -45.84781 | 2026-07-31 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2793d118-0876-3298-90cf-63e4ab7e433e | -4.27602 | -48.19509 | 2026-07-31 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5db67ea-b1fc-3afd-8616-194efda212d5 | -9.00231 | -45.18302 | 2026-07-31 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93471c95-f843-3bcf-8aa2-05a5d167f0d4 | -7.00929 | -45.8478 | 2026-07-31 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 012a6e44-aff1-3ff7-86df-a68b10bd2ecc | -6.12494 | -43.76321 | 2026-07-31 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b581b4ad-4611-31ad-9b29-e4ed955de9ba | -5.04109 | -43.26686 | 2026-07-31 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04fb3214-831e-39b1-a771-72c25f34559f | -7.17872 | -40.17471 | 2026-07-31 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9efcb740-b453-3bff-bad2-5764989a7038 | -6.97465 | -42.88027 | 2026-07-31 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b68d6448-40af-3566-b9a6-287986328eb4 | -8.46079 | -38.43671 | 2026-07-31 03:53:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b8c6b717-3dc5-3abc-a1bf-8d23357629fc | -6.76764 | -38.69244 | 2026-07-31 03:53:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d99a5259-7236-3702-9170-cfd45e7c6aee | -9.42509 | -38.10249 | 2026-07-31 03:53:00 | NOAA-20 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b6715e3b-f7fe-35e4-97c0-ce5be9983cf4 | -9.39894 | -40.60313 | 2026-07-31 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 632dbd48-5ccc-35be-bfcf-00e9a87e1f40 | -11.82892 | -38.2641 | 2026-07-31 03:53:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49fa0a95-8885-3cb9-9211-d346c2fa4e15 | -5.48907 | -42.17344 | 2026-07-31 03:53:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 13f5d88f-eec2-366b-8dc0-448be0178f2c | -11.25619 | -40.3414 | 2026-07-31 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fae3b830-8c28-3555-b107-640726b747c9 | -4.36354 | -47.76859 | 2026-07-31 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 806846ec-1a87-3b39-8c78-28350a50af8a | -9.56155 | -47.11716 | 2026-07-31 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e7546b4-c193-330a-9993-e9913145636a | -5.80711 | -43.63923 | 2026-07-31 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5082831f-75c8-3b94-ac3a-f40b2b61a17e | -4.26974 | -48.1939 | 2026-07-31 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93958053-0e3e-3ce4-9aab-b7b9dbb9d8cf | -5.60561 | -44.02813 | 2026-07-31 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13b6853d-5540-33d5-9d6e-0717de534093 | -9.63558 | -40.59824 | 2026-07-31 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0d41f681-56f4-3bfa-8aa5-a9440a3129cd | -7.62397 | -38.79922 | 2026-07-31 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85a8b7f9-e058-3770-a0ab-06c3394f1007 | -4.36967 | -47.76963 | 2026-07-31 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7e981c9-bf91-37bb-9ffc-d05ad0ace1a1 | -4.26886 | -48.19893 | 2026-07-31 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e51b43e3-153a-3e78-8dcf-1c66110a8ba8 | -9.16746 | -45.83352 | 2026-07-31 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c36556e4-d3b1-3747-b827-8a00ab46dd73 | -9.07966 | -46.06123 | 2026-07-31 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f399a56-94ea-311b-b36b-af415edf34a9 | -5.71837 | -48.12927 | 2026-07-31 03:53:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e6c05d8-1632-3dab-ba33-56b3b8b87ac1 | -8.99756 | -45.18201 | 2026-07-31 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8236f584-fcdd-365f-a9d1-b2f4b1938955 | -11.25273 | -40.34081 | 2026-07-31 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b8dcd8e-db1a-3ccd-b808-8d1210f32e8e | -6.29402 | -43.82123 | 2026-07-31 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcf38c0a-4fb8-33a5-a264-752122838638 | -6.29889 | -43.65091 | 2026-07-31 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca01b9c6-fbc2-3b03-af8f-de34dfef2634 | -7.21648 | -34.95591 | 2026-07-31 03:53:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 104e476e-b646-335f-bb1d-521add9142fd | -5.92966 | -46.35098 | 2026-07-31 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1eab9e-b126-3c26-9878-d83571154d1d | -10.4735 | -46.36269 | 2026-07-31 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5cd035d5-5765-3b89-8462-779ab7a6828c | -6.54852 | -41.86079 | 2026-07-31 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 513bb4d2-8906-3516-99c7-0a88fc8b098c | -8.7227 | -36.91545 | 2026-07-31 03:53:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71a8b597-533c-3702-a0ae-ac7700d80a4e | -6.12576 | -43.75847 | 2026-07-31 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2efde08c-f0fc-3f78-8d26-aba240035d7e | -6.29341 | -43.823 | 2026-07-31 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96e777ec-8c05-3741-9d37-716fd1eaa63f | -14.39295 | -48.06099 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 20a989c7-64ba-3131-b5ee-b84df8fd0a70 | -17.58997 | -44.11438 | 2026-07-31 03:55:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4170617f-967b-3ce1-9dbc-c5b9a128f7bd | -12.62374 | -44.59928 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 961b3c4b-6a30-39f1-8a43-ee420087f2f0 | -12.67359 | -43.0944 | 2026-07-31 03:55:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a131e988-ebde-33f8-aa72-50f40ad61c1c | -14.38707 | -48.05992 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e004f15-f358-3fd5-8e6d-d7dadb140c60 | -14.39602 | -48.07331 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a5833b60-e115-3467-8280-96946510a248 | -15.84129 | -41.89913 | 2026-07-31 03:55:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4ba58a6-c573-396c-8e6c-6c1667fdb87b | -14.39228 | -48.06443 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 676d32fc-b08c-3dfd-bcbe-6361aad705d3 | -15.50818 | -47.82451 | 2026-07-31 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff2aeae8-e1c8-3827-a39c-9963c0b2f4ce | -11.90581 | -43.44172 | 2026-07-31 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3394f3a-8cbe-3a18-996b-54a5b5c1eda8 | -14.20488 | -44.11094 | 2026-07-31 03:55:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68a55ff6-41a2-3c45-b097-5eb28c77a996 | -14.37998 | -48.06793 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 642f1029-8a0b-315c-bb5f-f2e8167d89a9 | -12.61408 | -44.62804 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d91a653d-b1c6-3382-bff7-69f7cc904b63 | -17.52577 | -45.30693 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31f0a910-3d15-3dc7-a395-60b207787237 | -14.2103 | -44.10431 | 2026-07-31 03:55:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a5ba0ee-af0a-3cf3-882a-27d2c5569ebe | -17.53478 | -45.30468 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9927a0c0-bd46-39d0-aa54-136ec4a40cf2 | -13.95828 | -49.1489 | 2026-07-31 03:55:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ab2ae4f-31e3-3a78-847e-74ed16bacbfa | -14.40512 | -48.05172 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecb74d66-7b8c-3150-968b-d412721a21b6 | -14.37823 | -48.05246 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f63caf-a060-36c6-a771-6e81bdb51927 | -12.60498 | -44.60431 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3eb6d62-47d5-3ac4-ad0f-7288d67eb4d7 | -12.45543 | -43.52792 | 2026-07-31 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63779b57-0145-3a89-8ad7-006486e1b040 | -14.3936 | -48.05763 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82deb57e-f23a-323c-a078-5fd58784e421 | -14.35772 | -48.0457 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14a32d66-850a-3c0d-a028-a3a8c8d3a5d8 | -14.37935 | -48.07464 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 552883f9-b931-3d28-83be-3110b2443a66 | -14.4058 | -48.04836 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeea93ed-395c-31f7-b6e9-990ad1f49775 | -14.83291 | -48.52453 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e29fa52-1972-3ce9-8706-7d9f47d54dd2 | -14.40192 | -48.04057 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fc04fa2-b5fb-30e1-9aff-ff71cc468b88 | -14.38069 | -48.06444 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 208b3d60-adbc-322b-afd2-70c90bf71ba2 | -14.37639 | -48.06184 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 07484574-b0a9-38d5-8498-b41cba09e0f9 | -14.39145 | -48.06528 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7111eab5-5b6d-38e5-890f-2154afaacc59 | -12.60929 | -44.60515 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef3c21c-8ad6-357d-baf0-05ab341ae0a3 | -14.37052 | -48.06391 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6fc4b516-5f96-32b2-8d31-493f18e91afd | -14.82975 | -48.5237 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35a859ff-4472-3d20-850e-9444469e740d | -14.77575 | -46.8103 | 2026-07-31 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 593ddb2e-9b33-38eb-b59a-ce261c952945 | -12.09938 | -44.12867 | 2026-07-31 03:55:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6231a131-e46f-3d26-a730-01ccf945eedb | -14.39725 | -48.06366 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c98f4464-313f-394c-aaa7-060c1a1fea28 | -18.92804 | -40.34332 | 2026-07-31 03:55:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6d3d9da-10f7-35a0-b1be-f03890cb1600 | -14.40386 | -48.03296 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25ffa57e-348f-36d4-883e-8e1a39038d67 | -14.377 | -48.05874 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ab1d1f6-5759-3837-a074-0a1ce23a877b | -14.3864 | -48.06324 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 875f0e0e-3d51-3da2-bf26-cc606078f325 | -13.95744 | -49.15297 | 2026-07-31 03:55:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 885bcc19-69ef-345d-8f00-3af3157f3581 | -12.84727 | -44.3951 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fc906bf-d924-391e-8bf7-e7ae1fb4d4c0 | -18.0235 | -44.3711 | 2026-07-31 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README5.md)
