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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ebdf6cc-e0cc-3e67-a827-85dceeeb0f9d | -3.8618 | -47.0438 | 2025-11-28 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 28934c5f-fce9-35e5-831d-c17508bc0b19 | -2.5135 | -45.5644 | 2025-11-28 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 228.0 |
| c44a8ce8-7be4-33cc-96ca-98fbfb610e38 | 0.4648 | -60.4494 | 2025-11-28 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ad4db8df-7bb5-3d9a-a646-860b41075d80 | -9.4 | -40.3722 | 2025-11-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.1 |
| fe454f97-b0db-3c67-a338-aa95d75fc570 | -5.5398 | -46.4893 | 2025-11-28 00:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bc2f219a-bdc5-3f56-851b-6abd5a7a15ff | -6.7199 | -40.8188 | 2025-11-28 00:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 775022f4-b916-360f-937d-78244c5b348c | -2.42 | -45.7462 | 2025-11-28 00:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 3010238c-387e-38a2-a435-373da63345cc | 0.4648 | -60.4494 | 2025-11-28 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e9714dd0-b9d8-35fc-b087-e095f14d4693 | -3.8618 | -47.0438 | 2025-11-28 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 244ffd16-4fd4-3ff6-8561-82f0df7f8280 | -5.5396 | -46.5115 | 2025-11-28 00:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 5c05d97c-0a1b-3345-afb3-bf2b7a5cbfe5 | -2.5135 | -45.5644 | 2025-11-28 00:40:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 633b2a2f-4e24-3d0a-b7c6-16d79d882ec6 | -6.7388 | -40.8169 | 2025-11-28 00:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| bbc38efa-8fc9-3080-8684-e3ef414c2cfb | -9.3813 | -40.3501 | 2025-11-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 270.1 |
| 67a9575c-e685-30e8-9fe2-018dfad75356 | -3.8432 | -47.0446 | 2025-11-28 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 09a7c749-a0dc-3fa5-94d9-48c62e8a573c | -3.8431 | -47.0666 | 2025-11-28 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 200.6 |
| ad365e9b-b54c-345e-8a38-f1dfd03f1c21 | -3.8978 | -47.2395 | 2025-11-28 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 87ece73c-66a3-399d-999e-f3f644548552 | -3.8617 | -47.0657 | 2025-11-28 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 5e99ef12-b72b-33aa-8c38-0165250dddd2 | -1.8245 | -54.332 | 2025-11-28 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b8aa585d-3915-308a-a7bd-45b20d827cbb | -9.3809 | -40.375 | 2025-11-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 373.6 |
| 7803a9bd-9ea0-3349-b71b-936de4785661 | -5.5584 | -46.488 | 2025-11-28 00:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 826b0649-424a-3314-95b6-00c034c91c58 | -5.5582 | -46.5102 | 2025-11-28 00:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 160c0b7f-51bd-3b57-b1f2-329043eacb3f | -9.4004 | -40.3474 | 2025-11-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 5458e806-e24a-3a71-8a54-9775c4095892 | -20.4715 | -47.4711 | 2025-11-28 00:40:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6cd1eb14-4fe3-33f5-b16f-e2b65670ff2b | -22.978001 | -48.670101 | 2025-11-28 00:45:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bbcbeb5a-bc6e-3c14-96b5-7af7a7e4ceb3 | -19.9795 | -49.9776 | 2025-11-28 00:45:00 | METOP-C | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91bd3844-3b71-3ba8-943a-9c000e4cbd14 | -4.0683 | -48.868301 | 2025-11-28 00:45:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd04ed3f-63e4-3cdb-9878-815586f4fafd | -14.3067 | -49.879101 | 2025-11-28 00:45:00 | METOP-C | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 78347672-e328-3c56-8915-635d4bc79525 | -19.990999 | -49.983799 | 2025-11-28 00:45:00 | METOP-C | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2bfe33ed-aeb5-3778-8eb9-d9111eeec013 | -21.749399 | -49.022301 | 2025-11-28 00:45:00 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c96555c6-5d15-30d8-8c40-358cd0099a2b | -17.587601 | -46.6665 | 2025-11-28 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3dd858b-4bd8-3283-abc4-c0e0af3e2f9b | -2.9626 | -48.592899 | 2025-11-28 00:45:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3d6ff1e-7596-3faa-96dd-ba548e8bc0c3 | -21.530899 | -47.682499 | 2025-11-28 00:45:00 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5b2a55e7-8135-375f-86bc-182c3ce8ff5f | -6.7275 | -40.8097 | 2025-11-28 00:45:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5537eda4-8e48-3bd0-a64c-3850a4de19dc | -2.9561 | -45.563599 | 2025-11-28 00:45:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48f40f39-f5a5-3b14-b4ea-fd3795271e97 | -9.3963 | -40.383999 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1cd27ba1-eb19-3d8d-882e-1f434e4e21e0 | -21.653999 | -48.608898 | 2025-11-28 00:45:00 | METOP-C | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4d4d4937-1f97-371f-9f24-d9fb4d27476d | -20.4576 | -47.473801 | 2025-11-28 00:45:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 76f5ceff-062b-3ab4-97d6-d29d11430d8e | -3.0776 | -50.3437 | 2025-11-28 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c0a378-a1d6-3e2d-8dfa-be1efc11f6bd | -21.657301 | -48.624699 | 2025-11-28 00:45:00 | METOP-C | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9c54fae1-9321-3527-a5bb-f66f59199e43 | -21.751101 | -49.030399 | 2025-11-28 00:45:00 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ed525b9-8b2a-3b7e-9e99-ab4470356a14 | -22.976299 | -48.6619 | 2025-11-28 00:45:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8b39505c-3e32-36f3-857a-390a0ff108dd | -9.4009 | -40.361698 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3c032572-0890-3f45-a461-167107ce0c77 | -17.589199 | -46.673801 | 2025-11-28 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 39675d3b-af7b-30c7-a75e-29132e30a762 | -20.4674 | -47.4715 | 2025-11-28 00:45:00 | METOP-C | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3b63b65a-bc32-32d6-add4-3443b1d4a606 | -19.981199 | -49.986 | 2025-11-28 00:45:00 | METOP-C | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3cd29626-2284-3e6a-ae83-2351b189734e | -3.3825 | -51.494801 | 2025-11-28 00:45:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1edb01dd-70ac-3d24-92a7-7ab150e01257 | -6.7223 | -40.7892 | 2025-11-28 00:45:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddae7b04-b1e7-3e2b-8f71-eb74a478b4b2 | -17.576099 | -46.661598 | 2025-11-28 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 336df96a-a278-31c4-be43-5018c31ccf59 | -21.5228 | -47.692299 | 2025-11-28 00:45:00 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 68e03405-50ec-3002-b98e-53fbbe5cf054 | -24.967699 | -49.274799 | 2025-11-28 00:45:00 | METOP-C | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 687f8e7e-2adc-3d52-b732-94a6dc6010d0 | -2.7081 | -45.209702 | 2025-11-28 00:45:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3440ce0e-3453-3ac0-a12a-d30431b80e9b | -3.0792 | -50.350498 | 2025-11-28 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2ab357b-d107-3cde-b8f8-794b6de37e39 | -9.3912 | -40.364201 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0f80990d-e6b2-364d-aad9-d80f49605a52 | -21.645901 | -48.619099 | 2025-11-28 00:45:00 | METOP-C | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 50005cc5-1884-3caf-b32a-9f2b8eaa3c17 | -21.655701 | -48.616798 | 2025-11-28 00:45:00 | METOP-C | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7de8c692-9f97-3d68-955b-d579db758a4c | -9.3861 | -40.344398 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f77cbc1a-2690-3797-b0dd-b4c39f7f4d80 | -21.259501 | -50.294201 | 2025-11-28 00:45:00 | METOP-C | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c6f93f8-9b6a-3797-9888-b48d361aaf52 | -3.8265 | -49.295101 | 2025-11-28 00:45:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a58a90b-b9ec-36cf-99ca-fffbcf728171 | -2.4409 | -46.351398 | 2025-11-28 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7aaeef4c-8118-3e30-9769-56e93e658fb9 | -21.5341 | -47.697498 | 2025-11-28 00:45:00 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f5c69cd9-7a2a-3c37-a088-16e1de2b434a | -2.9609 | -48.5853 | 2025-11-28 00:45:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda542bf-c0eb-38d5-9774-9dd3f0704a4a | -5.1388 | -49.931198 | 2025-11-28 00:45:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8c2c33-b91f-3b73-8b11-e7647fafb830 | -17.577801 | -46.6689 | 2025-11-28 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 412ed90d-a88e-3634-8a7d-e8fefe88a7bc | -20.465799 | -47.464199 | 2025-11-28 00:45:00 | METOP-C | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7150eadd-0a45-30f8-9834-9350ca5efa49 | -9.3816 | -40.366699 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ade7cbf5-31eb-3c69-836c-6f579c3e3442 | -2.7109 | -45.2215 | 2025-11-28 00:45:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a404ee0c-db5a-3242-8f2c-b467550669ce | -3.2263 | -50.317501 | 2025-11-28 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53bbf770-5f45-38a7-b52d-2003f471bc82 | -20.455999 | -47.466499 | 2025-11-28 00:45:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ffe97004-cb23-39dc-af86-006b4c8acbec | -2.7053 | -45.197899 | 2025-11-28 00:45:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7f33b8-0848-31ae-b385-05a82ade1c3b | -21.532499 | -47.689999 | 2025-11-28 00:45:00 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 085679eb-814a-3a4a-b27f-fe06961dbdde | -17.579399 | -46.676201 | 2025-11-28 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53501592-2331-38db-9b7f-a299f5d3d742 | -17.585899 | -46.659199 | 2025-11-28 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 580ab293-6db3-3628-ae9a-e3e805ba7be3 | -9.3765 | -40.346901 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9c95f1a5-70d0-3ed4-9c45-ee3687fe906b | -3.2247 | -50.310699 | 2025-11-28 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f568df9d-d731-3c3f-947a-dabc13dd33a3 | -9.381 | -40.324501 | 2025-11-28 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 82351f23-0f56-3937-95e4-030a4577a693 | -21.524401 | -47.699799 | 2025-11-28 00:45:00 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dce8d0c5-ff2f-36e8-b6fb-057ae7f83a15 | -3.8249 | -49.287899 | 2025-11-28 00:45:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8d5647-32b1-3d59-981c-7a53e3ece46f | -20.469 | -47.478901 | 2025-11-28 00:45:00 | METOP-C | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec2743c8-6731-321a-b2c2-d605d6fcc83f | -3.3556 | -45.424301 | 2025-11-28 00:45:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a722a262-6642-32d8-adb3-35a613476ec6 | -2.9535 | -45.552502 | 2025-11-28 00:45:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48ae23a6-4b92-3132-8bb4-6b8903eb5713 | -3.8618 | -47.0438 | 2025-11-28 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 0a1e5f25-74eb-3a22-818d-c3124cbf0efc | -1.8245 | -54.332 | 2025-11-28 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| ecb9a977-5826-312f-bee5-fe98533249a5 | -3.8617 | -47.0657 | 2025-11-28 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 202.2 |
| 75dc64b4-d754-3d26-857c-89efdd5c3b5a | -5.5398 | -46.4893 | 2025-11-28 00:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7109f631-a0f7-3527-95b5-b114a7ec3099 | -2.42 | -45.7462 | 2025-11-28 00:50:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 03194057-54d6-36aa-9448-f789254d7a4c | -20.4715 | -47.4711 | 2025-11-28 00:50:00 | GOES-19 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 101.0 |
| cccaaac1-7f99-3140-99b0-3fc00b6e6519 | -5.5584 | -46.488 | 2025-11-28 00:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 70a12c0d-b728-3da4-9e1b-b489dcb43b4a | -3.8431 | -47.0666 | 2025-11-28 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 8bf29ec2-a449-3b13-a6c1-ec9533586ef1 | -3.8978 | -47.2395 | 2025-11-28 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 65f9306e-65fb-3d37-b59b-eff35a89f9d3 | 0.4648 | -60.4494 | 2025-11-28 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f59b04fd-b290-3a6c-8e7f-44e7c9fd24ef | -5.5582 | -46.5102 | 2025-11-28 00:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 27702fd4-f629-3cf8-86e8-69e665687def | -3.8432 | -47.0446 | 2025-11-28 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f6e9cc79-9346-3bce-8cf3-768cba32c2e7 | -9.3809 | -40.375 | 2025-11-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 305.0 |
| 9ace45ff-42f5-3b67-ba84-8a3f35f2ebc2 | -5.5396 | -46.5115 | 2025-11-28 00:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0a92c661-c992-3a83-929a-233b882129a2 | -9.4 | -40.3722 | 2025-11-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 152.8 |
| d846b6cd-d0f6-3ef1-8ac2-da0b0a53850f | -9.4004 | -40.3474 | 2025-11-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 128.6 |
| da529efe-d9e4-3141-9214-9e1c90f79af7 | -9.3813 | -40.3501 | 2025-11-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 253.1 |
| 6d144622-c562-346d-bf0b-06fe0f093735 | -2.267 | -47.0994 | 2025-11-28 01:00:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9ab5fec2-0d04-3f1e-ba51-923dbcf9dcec | -5.5582 | -46.5102 | 2025-11-28 01:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 35b25f80-1e9e-308c-9faa-0fb6afb02376 | -5.5398 | -46.4893 | 2025-11-28 01:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |


[Clique aqui para ver as próximas entradas](README3.md)
