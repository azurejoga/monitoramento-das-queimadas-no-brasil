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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 658080c8-b250-3210-9498-c02836d5bd68 | -5.77719 | -57.58927 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d857aed1-c02b-3b49-9aeb-c018d04847ef | -11.03667 | -57.24812 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b68eee0f-9d57-3191-b99c-ced87aecf9c5 | -9.39889 | -51.6451 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496c3108-d3cc-303f-84d8-36636262c2c1 | -7.58089 | -61.34129 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5e2b5b5-b8f9-331d-a02f-59b42615f7d2 | -11.35816 | -45.15961 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 88eb0abb-e989-36c4-9d6e-df53c7d21784 | -11.22604 | -53.98409 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4378d051-5ce6-3e08-b402-418083c1ec70 | -6.77273 | -55.66114 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 05ddc891-1e09-37f3-bca8-d9f9be630e38 | -8.97924 | -50.79078 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf16de2-bb0d-3647-bce3-f4fe075bcf24 | -8.08774 | -51.66729 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c899c2fd-aa8f-3216-a7b8-4f8c58d198d0 | -10.50667 | -59.62469 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 139182c8-2da2-3c10-bddd-77fc2ebb6dd0 | -7.51159 | -55.30308 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5828e292-9a8c-376e-8d67-f070ead1e0d2 | -11.20581 | -55.09915 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 342bbff1-05cb-3b81-bc0d-f3a257613579 | -5.87774 | -57.7695 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 19b7c1cf-f005-3c77-95ff-827c5aa73542 | -11.2378 | -53.99747 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d5ae4ae-aa34-3160-98a4-174644fc2b35 | -6.78736 | -55.66841 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 850dbebe-4aa6-3f8f-bf53-36eb00509fd8 | -8.55791 | -54.71455 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3baa5544-ce13-3961-9ee0-0cd12aa8dce7 | -6.37406 | -54.95496 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbe4b97e-7ca4-3c67-a56b-d8da306b3635 | -19.28878 | -49.51656 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6d2f6fd-2529-3ed8-b675-c07867a7d37d | -9.42594 | -51.68872 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628cf8e4-f345-3f10-b295-816a0e269d32 | -6.68763 | -50.61597 | 2026-08-29 04:53:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36d28c38-e073-30f2-9f28-1331ac115486 | -8.01811 | -48.01286 | 2026-08-29 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e6644655-a8ba-33a6-a7e4-9491b2100a0f | -12.2176 | -50.54012 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e55cd8f7-00a7-331f-924f-940de39623d4 | -11.49038 | -46.95021 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81695270-248e-30c2-aba0-b8dd13160491 | -9.01039 | -57.54148 | 2026-08-29 04:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e75ebaa5-35f4-343a-9a34-7a3de5613f26 | -9.93791 | -60.4351 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dcc61a0-c387-389d-9305-c9c9b3cba7ce | -6.78432 | -55.66291 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8507ef54-0624-381d-9970-a906135354d3 | -11.62812 | -54.59086 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3608798b-0429-3d65-ae3c-3fa1ccf1a497 | -17.82292 | -50.95201 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b23f5ce9-6594-309f-82d3-3a8b39ea57e1 | -5.8692 | -52.09449 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c28834d-6625-31d8-9de9-138f8799f5f0 | -7.00074 | -59.64082 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f5a8f54-c788-3760-8899-ce58ed895e20 | -12.43569 | -42.89223 | 2026-08-29 04:53:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2153ab24-ce10-37ea-becd-017d597c6473 | -17.82232 | -50.95623 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c828471d-4b9e-36ec-bfc9-b38c94de3a75 | -6.94902 | -45.2315 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe392365-c1a3-3d0c-8010-fbe231247fab | -6.75484 | -55.67323 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 55c5c5f5-3010-31fa-b2f1-a320b299693f | -5.98287 | -57.68023 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93e43646-5601-3a31-a16d-d4b093cb72ae | -7.26514 | -45.35502 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff038ab3-05ce-3885-b398-2f6ed9f250d8 | -7.99888 | -61.41326 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 339e898d-86f1-329d-8700-d934350ad1b1 | -6.93746 | -58.95631 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f75716f0-f04d-3686-84b8-8eb958ace21c | -11.1965 | -53.99427 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb7411e2-07dd-389b-8a88-6db2a86a3931 | -11.29542 | -54.03369 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f071ad6b-3b48-350e-8315-39d5c60041c9 | -5.87623 | -57.77833 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 497e3f87-4dc9-33ea-825c-c84be96eac21 | -12.19927 | -50.54506 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0210130a-0642-333b-912f-b4aaffb6132d | -10.40667 | -61.19788 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f8556e0-e3f6-311d-9527-1fa33cc2ea24 | -6.50344 | -53.2559 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f843b6a0-ba01-38f1-93e7-2299d5734fc7 | -10.90797 | -46.61056 | 2026-08-29 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd7ff140-02d6-35fc-b233-44a4590e4d55 | -16.61048 | -49.40675 | 2026-08-29 04:53:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0ead55b-6a4c-330c-a087-26dd041a4420 | -7.85772 | -56.68097 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513868fb-6b08-3f4b-85c4-f052e50fe6bd | -7.03594 | -45.54247 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0d0fe1a-a5f8-3901-af54-598ce804fa9d | -14.07967 | -44.06075 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2c5000c-2c73-3314-8f2c-330cebe532ab | -6.91382 | -44.95241 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a34de56-e97a-3f6c-92c8-a43174a87404 | -11.49086 | -46.94675 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d795944d-2950-3637-8442-afb92388d1e2 | -6.15375 | -57.7997 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ba329af-eb22-3c3c-abb9-09216170fe3e | -6.27612 | -53.14368 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab9a21dc-02d0-3176-afe4-a541a359b786 | -8.59626 | -54.77178 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92a098e3-8140-3929-a637-2ef53f5ee1de | -7.12433 | -42.7675 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bf2bc84-0cb0-3e5e-a88e-b55b827a538c | -11.22243 | -54.00623 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6165716e-4dc4-3662-b03b-423546e8bf9d | -7.27913 | -45.85596 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4de8527f-db77-3752-abf0-d4083a882a02 | -10.87918 | -50.50397 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c74d225-e9b7-3703-8dd5-9e4fa77b8cb6 | -7.35005 | -55.16222 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95cc9973-2e49-3e5b-a498-753071ce0bd6 | -11.16512 | -54.01551 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4da4e79e-ea39-3246-8116-23c63c08367a | -10.53725 | -50.4752 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c8547e0-bc59-3661-806c-2aaa39cd2dfb | -8.95467 | -63.27838 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1063701-5c35-3145-9402-5d9664940369 | -6.25347 | -55.42457 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 064b876e-a02e-3a35-8a5d-d38bed96243e | -16.57902 | -49.18357 | 2026-08-29 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ddb69d2-aab6-3f41-9ba7-f5be428a5844 | -7.58644 | -61.34233 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b214a8e-8833-3fae-9ab7-d849db944713 | -9.26734 | -45.63794 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dcafb25f-62a8-380e-9f9f-d28da718a466 | -14.07845 | -44.06517 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c421ade-edf0-3459-923c-015fe90ba60d | -11.62531 | -54.58643 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 230dc908-2734-3c99-9427-27747a201447 | -8.94976 | -50.80432 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eef3eb9-e387-3027-9150-c9440c68c6f7 | -9.92793 | -60.43299 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84d7d1cb-f092-3cc6-bb45-1a000f44feae | -19.00277 | -47.44868 | 2026-08-29 04:53:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 274bb887-92fc-3694-bd20-0fa9beb04823 | -7.04019 | -45.54307 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9bba6937-59e7-32ea-9b59-77ef8bb1fd8c | -11.73008 | -54.52512 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f914266-f6a9-3d93-ac71-525011a2396c | -9.93292 | -60.43407 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a1b6e2-2a66-39b8-9480-2aa3a1ae5b3f | -11.23222 | -53.98892 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53e60471-a7a7-33e6-b847-05235c8d1ab0 | -6.16928 | -57.7763 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddc2dcb8-e7bb-38d3-b030-36b3426fcbed | -12.26299 | -50.53909 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22c1a71b-7f64-3e2c-9b26-32965dcf7953 | -10.82475 | -50.51828 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c43894b-6e25-3c6a-894d-ffe233b4fef1 | -10.75954 | -54.04832 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad5bb56f-e240-3032-92d1-396be90b289c | -13.39503 | -51.79228 | 2026-08-29 04:53:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3dadb07-82b3-3372-83f2-27cfe2b7919c | -10.75054 | -54.03917 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72537fbf-e337-352f-9b2b-eac96649b0de | -6.51151 | -53.59953 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d27c9f79-a4b1-3d2f-80ce-cd3d304fa631 | -13.31871 | -48.19469 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c96ba14-0b28-34a5-8063-7d165a61394a | -7.19858 | -42.73708 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e19b583c-77d7-3cef-a1e6-5ec47bc004e0 | -14.11913 | -44.21487 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2553c3b3-b69b-3502-90f8-d0e1c41e235f | -11.72258 | -54.52772 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c46d4dcd-5cdd-3117-aefa-e4483764e0e3 | -8.33043 | -47.6323 | 2026-08-29 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e0d395e-3f8b-33c9-b9c6-8de078c6fe11 | -9.30782 | -56.7995 | 2026-08-29 04:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f2484b7-4059-35cd-a4bd-55e42419335c | -13.39559 | -51.78866 | 2026-08-29 04:53:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e27542b-4d89-3bc7-b243-cd8274018b6d | -7.50862 | -55.29785 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b71362e-cdc0-30b1-ace1-09b50525807f | -9.40165 | -51.64912 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19ba3e9b-e5cf-31a9-ace4-178c0df199ed | -12.42607 | -43.4149 | 2026-08-29 04:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbaf4022-dff2-32f3-a255-7853e7fb851a | -17.30715 | -54.93507 | 2026-08-29 04:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60d17b60-f8fa-3db0-99a2-7c8aa07434eb | -10.38816 | -61.23972 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3883dd89-a7ee-3acd-b59a-5d4f46a1c0c4 | -6.17298 | -57.78145 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4b06ad8-e57f-3817-a02b-caf0fd9b9fbe | -9.63092 | -48.33338 | 2026-08-29 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d45887ab-eeb8-3cd3-89d6-f806e8480146 | -7.49817 | -55.29146 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 485d4a8e-723b-3e7a-b050-b1399b2d7c2e | -9.96494 | -53.93042 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f0584da4-506c-37ff-90f0-7cb3b957e47c | -6.91824 | -44.95304 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14414287-9dd5-3d73-a872-6bec6d252fb9 | -8.98637 | -52.38319 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
