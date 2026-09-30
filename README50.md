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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6976d71-5df2-32e7-bbc5-6994e53efa79 | -5.09563 | -46.04613 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bf8e44e-cddb-3c57-ad27-0fd9ce239037 | -5.16149 | -56.01238 | 2026-09-30 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21fb7ae6-fa37-35b2-8cdf-d0ddff535878 | -5.76206 | -45.17711 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e92b0de3-1f0c-3375-aca9-774fa98d9892 | -3.96536 | -53.43942 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5b5ffe9-8483-307d-a0f8-2d6046850efb | -12.12764 | -61.15566 | 2026-09-30 04:53:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d2bda84-857b-3eec-abea-a712247a99c2 | -10.53329 | -51.42668 | 2026-09-30 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8da33dd-fdd0-36c3-b6f9-ce64a9872ded | -5.75893 | -45.16854 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01f56b3-c3af-3a6d-908b-c7b9f4860226 | -10.68438 | -50.29186 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 803c07f7-9549-3008-b099-de94a2cd6407 | -7.42705 | -55.18161 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43d6ce96-5e8a-3284-9b4e-47e62790831c | -8.97099 | -44.17683 | 2026-09-30 04:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14479716-0700-3c3a-aa0a-1840ea34e6be | -6.32968 | -51.16232 | 2026-09-30 04:53:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca0848bd-4277-3911-9646-308b3215b6b5 | -11.17432 | -44.83076 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2f2d479a-c813-3402-98f5-70246ba1c7e1 | -11.16226 | -44.77675 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20f48bc7-06fa-3e72-ba40-05344859d9f3 | -6.33947 | -55.32855 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0e7a9f3-a606-31b7-83a4-d5ad3247422a | -7.49432 | -55.59258 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60d964de-fd0c-37c2-be12-d9a20e14c7ab | -3.1566 | -54.08498 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b45b5cdb-20ab-366b-9c56-aae3e3467584 | -17.1307 | -52.13312 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d9a814f-3d04-3986-a4f2-a58296b0de80 | -4.32667 | -48.62802 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b679e245-8d30-3acf-9923-c6c7631bdde9 | -10.41391 | -53.78205 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fcc9af3-a2b8-3aa5-bc08-50992f38975d | -7.83511 | -45.82271 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fcfb6b99-ad54-305d-a0ac-00d5fa5ff2e5 | -15.19849 | -46.1449 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ab53dad-5e75-3a86-8100-9837593d2b87 | -3.5714 | -50.25917 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfbd6635-8235-3f14-94d1-3e6fc96cf67a | -8.30009 | -54.71272 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c6a7bea-2b2c-3329-83b6-651cbfdd479a | -6.16362 | -52.90572 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 860f9dcd-526a-3467-9ea0-3c510f544223 | -3.26977 | -50.70501 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9694c791-5fa4-3125-83d0-0194b0f622b8 | -8.27943 | -50.26767 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f07260da-e5ea-395c-8040-d1f04a50f4d5 | -8.06095 | -55.33723 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6edb6a54-6641-3fa1-9498-8645274f403a | -5.16552 | -56.01311 | 2026-09-30 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80685bfc-a268-35bf-be43-c07b3ce82f79 | -6.70408 | -45.98963 | 2026-09-30 04:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60ffd53d-f759-345d-9b96-12bf21a269dc | -3.37686 | -50.95174 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18d7ac0b-85ab-305e-a034-cb2fce4a9e0e | -5.75452 | -45.17667 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c595be77-a57b-32b3-b0ef-c058eb27c9e1 | -3.38017 | -50.95227 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 077a0f03-f02b-3982-868f-0ce4cbbf2a9d | -11.25529 | -43.54413 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c7a239e-9aaf-34b4-996e-11252d926579 | -4.29118 | -48.56065 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a47b0a6-5424-3082-bf6b-23de7facc04f | -3.18436 | -51.24403 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 784f49e3-8c51-338c-b773-ab5bdf943244 | -10.74673 | -50.50258 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6404aee1-ff11-3158-be3d-c731de97723a | -10.08588 | -50.31549 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43c01746-5567-3876-93fd-2f1e05d625b8 | -11.63697 | -43.53017 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eb8139e-6838-3013-9056-2f5d6355bbdf | -10.70918 | -50.83813 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 119f7a56-d4e1-3250-8e34-038b5e9b3fd8 | -4.26748 | -48.56143 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb04df0-c83f-3108-82e4-78e77d155ff7 | -6.66839 | -59.93056 | 2026-09-30 04:53:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57c688d7-77eb-32e0-9f79-32fc514c6eb0 | -10.08756 | -50.30436 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b65a734f-9b52-3124-b65d-faef817bdf76 | -5.81628 | -46.22099 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f48bae3-233e-30dc-b44d-f8b4094c4bb0 | -7.1933 | -46.50882 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9682e191-6306-3fce-a5aa-7d2db479d577 | -8.9475 | -49.79321 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b64dd99-6e2d-3da6-9aa7-f9f5b92c4ccb | -11.19471 | -45.12243 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 507eae36-98b6-3e24-aa97-39a894c3ff3a | -8.22243 | -54.74794 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82e3e566-1981-303c-a269-6d3893c7dcef | -11.03334 | -50.71288 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bddc65ca-89d1-33a2-9396-971d6d0fd837 | -9.93166 | -50.15514 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11173436-7056-303d-bb13-e784608f3f5a | -7.1016 | -46.45325 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7ce10d9-6da6-3cf8-876f-d6804c040c84 | -3.77244 | -53.42325 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 533a3879-8184-31d6-a5a8-361c7b0a6e1a | -8.94464 | -49.78892 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39d7f19b-a2b1-3021-8b20-3cb210fbf715 | -8.33831 | -44.16438 | 2026-09-30 04:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b02c296-cd75-375b-b563-2e134dce89c1 | -6.34706 | -55.32985 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1301edb3-ac90-3244-aaad-4d24e9f4fba1 | -7.48327 | -47.59323 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12c788b5-ec7e-38fd-80d2-98d3f6e752cf | -4.45835 | -47.92106 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9cd930d0-7774-3403-a5c1-b4a627ed074b | -11.17363 | -44.8358 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a37d433-59c2-3178-9a8b-ff138d579281 | -7.82268 | -45.81718 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7984ea86-fff8-3dca-858b-1b40eae4c090 | -6.39763 | -55.23769 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e297ab5-3f01-330b-8024-22f6c0411ddd | -15.97998 | -48.13786 | 2026-09-30 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae835a8a-9c4b-3b50-916b-1bd0f9bd7e3e | -5.12624 | -56.02091 | 2026-09-30 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad47ea4c-2ba5-3e92-a832-686a853b5b5f | -11.71034 | -43.45627 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eaf240ca-efe3-37f3-b7d1-2d2129c356cb | -7.1898 | -46.50481 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ca9a6c-9473-3bdf-be2d-67c80ba32398 | -10.51834 | -50.8463 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 535a9350-aa61-3496-9b62-788321f25b07 | -8.26489 | -54.75935 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16c368dd-27a0-3bd8-ae37-7ed33a335de0 | -11.43137 | -43.42622 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 553cae19-72f7-3f9a-9b6c-0ee6bdc1955f | -6.71811 | -50.94025 | 2026-09-30 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc327af-b373-31ff-babe-e69c17a81fd4 | -10.8378 | -48.71648 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e624200-4275-32b8-a83b-af034867efdc | -3.38348 | -50.95279 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f0b11bc-a782-3b10-b4e6-e1d3a19973e6 | -11.71115 | -43.44976 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bdded19-bc91-369b-9e95-975297570293 | -9.81053 | -48.21556 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bb1a111-916d-3517-8231-ad249bdf5882 | -6.30236 | -46.06364 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5900c15b-f60f-3d18-939a-dd0a603b5195 | -7.50264 | -55.03835 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4c5d080-ac55-389a-b1aa-201db1bcc7c6 | -10.71691 | -44.42072 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| abbca384-c413-3006-9fa1-6a777379e5e7 | -5.98484 | -53.54842 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed53f94-82af-385e-8c65-90e56e6807bb | -6.10536 | -55.71026 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70896152-8554-3735-81a6-10fe766c2026 | -6.06796 | -53.60989 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6848c8ad-7b2f-3599-bf77-aead0857db66 | -9.09513 | -47.16694 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50bbe107-7a11-33db-a956-9d46a639564a | -15.77583 | -46.03358 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2e0242b-dfce-34fb-bd91-5d8cc5fb445f | -6.70547 | -45.6357 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 114bdd9b-ad4b-3811-8dec-07736b57b311 | -15.12652 | -43.62243 | 2026-09-30 04:53:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8a344f4-a6cf-346c-9333-4ed1023db48c | -4.02812 | -54.20705 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 500018db-002a-36ad-9efa-91aec2c86e54 | -10.7711 | -50.47982 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e73b4d7-5e9d-3691-a7f0-84306edc19bd | -4.5389 | -50.77912 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d42704a2-033f-3faf-864d-424cd6d21c77 | -6.19779 | -55.54547 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebe8fbe9-a21b-3a1c-850b-d0366ee51e77 | -4.53944 | -50.77567 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86494c3a-9b10-3021-b551-543c581afef4 | -3.82766 | -55.9043 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 206606c5-54e1-3c18-b26a-98968d90b9c6 | -5.75778 | -45.1765 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abc2ec72-7301-3f6d-aa88-57c7c6ca1687 | -16.57022 | -51.62537 | 2026-09-30 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d000a46a-67f7-3abc-9aa7-24c3f3f20fa8 | -3.14712 | -54.09679 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31c178fc-6d03-3e1e-9895-dbc17c95a814 | -6.2249 | -55.62051 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5615441d-488a-373f-93b1-b2a8e55eabe8 | -11.35007 | -43.35142 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ba1b61b-442f-3fce-812f-cdf28d735be9 | -3.43217 | -50.66749 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d72827cc-d888-3c2d-b094-c9261319157f | -4.94708 | -49.41404 | 2026-09-30 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f19846ca-ec7e-3ca5-aab9-217300857f22 | -3.99272 | -49.04193 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef10f773-0bae-3d9c-96da-5778f17594ac | -16.35452 | -42.58398 | 2026-09-30 04:53:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01bdcc99-cbcb-370f-adef-b6f16af5413a | -10.82857 | -48.70265 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a569ea9e-136a-3b8c-af67-85ef885f8841 | -5.75084 | -45.17214 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ccec195-cb8f-3769-a073-a7e5fd7a95ff | -10.19646 | -49.97932 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45b76766-4497-3909-9743-0a31ddc6ab2b | -6.24748 | -46.65456 | 2026-09-30 04:53:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
