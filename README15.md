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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22ae060b-04b2-393e-a13c-cb36526bd421 | -3.1029 | -61.229698 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38d95c08-8e53-3d9a-9a67-690cd498ce44 | -9.1158 | -60.391201 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c661142f-636d-30c9-b4ef-9bbcfae00d04 | -6.0402 | -57.803699 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01120fa-51e4-3fee-84e3-8897ddffaaed | -19.7637 | -57.9636 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7e6b87c8-ef47-36fc-96aa-28c5dc3ffc93 | -8.9549 | -60.546299 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 469f1ad9-8600-34bc-974d-5e30157955bd | -8.5641 | -54.718102 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2cca0ac-0d72-3ae4-9e2e-70d6f747422c | -3.0998 | -61.2159 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47e1f2e7-d004-3056-9564-4fef90fbfc30 | -7.4728 | -60.047298 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf304927-298b-3223-8760-2599a453a065 | -8.5567 | -54.730301 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe417351-f2bb-3b10-a9db-8fb19015014d | -6.0195 | -57.847599 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b0c07b-d389-3f3d-930f-a520108ad582 | -7.0573 | -59.851601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 994bdc67-dc40-3b88-b35d-501dd1230ca9 | -19.7605 | -57.9487 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 805c91c1-d8b1-30c4-b651-bbfb130b2ce0 | -19.0784 | -57.361698 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0bea0e6f-e205-3191-b753-8b970513b152 | -6.8401 | -58.9902 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff1c31f-5e72-30d4-a3e2-27646ebf291d | -10.879 | -57.1273 | 2026-08-19 01:23:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d682ab0-9fb1-36ef-9fce-6c1b43c7c8b7 | -10.3115 | -50.439602 | 2026-08-19 01:23:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 249814a5-c4cb-3262-ba2d-49e0d9d3ed87 | -9.4174 | -60.451099 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f53a962d-5a61-3ed1-afbe-ae97300d324c | -6.8118 | -59.4529 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3a4db7e-47ae-39b4-9992-737eeb9c0757 | -9.2117 | -60.821701 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 662f053c-49d9-3204-91d1-72720960c4ab | -12.9462 | -56.646801 | 2026-08-19 01:23:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 055286d8-71b5-3052-bebc-0e23a9d54edd | -11.2315 | -55.0704 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c86eab51-f72b-35f2-8014-be7e49575f02 | -9.3989 | -60.552799 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 689c35f3-84fb-3797-bb17-706470bba5a1 | -6.7628 | -59.463902 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4517e4ac-838c-3d40-a888-93a3fd32f889 | -15.283 | -56.4818 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bfa9bdaf-69a7-3926-bf1c-80293c25b62a | -15.2101 | -48.237598 | 2026-08-19 01:23:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91213034-96a2-3603-a7dd-56331540cb85 | -6.8714 | -58.9468 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2de21f-0628-35ac-96c3-b25296654630 | -8.5886 | -54.691101 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af755b6e-d6b4-3716-a286-00cee63c0d5d | -5.9981 | -57.8447 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f179235-ef1e-3ebd-a17e-f6b50b3943b9 | -6.771 | -59.4548 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9920f94c-83a7-3d51-b98f-5bfc9265b680 | -19.737801 | -57.9384 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7e03dc4b-2fc6-378d-ba16-aea8109cf13f | -6.848 | -59.024799 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc908bec-c537-3ad8-aa12-e1599afae7ad | -6.7065 | -58.947601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 124567f5-a3de-3f31-abaf-9bbb676be8bf | -6.8806 | -59.032101 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e157547b-c47e-3f89-adb4-11fe9c6a1cb0 | -6.8626 | -59.0434 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7c07c60-f24e-342f-bb7a-f5bf8ba70aba | -6.0937 | -57.901001 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e862b9e-931e-3309-aa96-98804b4f9db7 | -9.3971 | -60.591 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f377250-170f-3d9f-bfb0-1c43f9a2e1f7 | -29.1518 | -50.402 | 2026-08-19 01:23:00 | METOP-C | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c032e451-26c6-31ac-a4be-3da5623a61b2 | -9.2215 | -60.8195 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43b359d0-fa19-3d88-a5b2-5583f5cae883 | -6.1376 | -57.867599 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4200da-09fe-3cca-a34c-e99c8abdce5b | -6.7049 | -58.940601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26eedab1-dc34-3469-a6b5-82f0af678210 | -6.0912 | -57.9187 | 2026-08-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 46bba697-5fde-3a7a-bb7b-91c50b3b9276 | -6.6938 | -58.942 | 2026-08-19 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| a0d9139a-e73b-3bd6-a1cd-9477fcadddd3 | -6.0913 | -57.8992 | 2026-08-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ec73c298-d340-320f-9672-e7122a50d1e2 | -9.4257 | -60.416 | 2026-08-19 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 433b7eac-d90c-358e-8a49-bb7f4c6108f0 | -6.8778 | -59.031 | 2026-08-19 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3a807b34-2ac8-3a0c-9358-3e302f00b1a2 | -6.0728 | -57.9194 | 2026-08-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c24f3825-bc89-30c9-847f-2fc69f8eaed6 | -15.5945 | -49.8292 | 2026-08-19 01:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| cbf0ad9a-b8d8-3e60-b50b-b53b68c83654 | -19.7639 | -57.9607 | 2026-08-19 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 140aad06-f95c-3608-8872-9afe1e0c1e49 | -9.4061 | -60.5518 | 2026-08-19 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1ad5b534-511e-38c6-965c-45a2fff45ebb | -5.9994 | -57.8639 | 2026-08-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 92b7ea18-6b0f-3517-a838-490318355315 | -9.4256 | -60.4353 | 2026-08-19 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 5bbb2580-e919-3519-a8f2-a0f29222ca46 | -9.3875 | -60.5528 | 2026-08-19 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| a0551898-a42d-3cc3-b07f-88a8bccaeb71 | -6.0178 | -57.8631 | 2026-08-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c1645154-89ba-3ec5-89b8-69a71098dc37 | -19.7442 | -57.9425 | 2026-08-19 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| d28aa043-41ea-3e82-9414-9e411eb65242 | -7.5301 | -55.5839 | 2026-08-19 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3ea779c8-5cc4-333e-9a7f-7b4881598efd | -5.9995 | -57.8444 | 2026-08-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2e8988f3-00d5-3840-a970-34ca0c5969f4 | -15.5749 | -49.8323 | 2026-08-19 01:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| feb708c1-7a75-32f5-b9f1-aec11612f51b | -5.4317 | -48.4212 | 2026-08-19 01:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 9244ce87-094c-324c-89ce-e77d428f20f7 | -5.4319 | -48.3996 | 2026-08-19 01:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9866a784-170f-3ae8-8d5f-28812004b5da | -6.7123 | -58.9412 | 2026-08-19 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b72721c7-f3cb-381c-9786-8ddd513d09be | -9.406 | -60.5711 | 2026-08-19 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| cc5f9b9b-d106-327f-bdff-32edf25564cb | -5.9198 | -43.6264 | 2026-08-19 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 5e119947-e299-3614-9480-adbe81b6d92b | -6.8593 | -59.0318 | 2026-08-19 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 01be73b2-dec6-36f7-9561-b4c82f052a06 | -9.3873 | -60.5721 | 2026-08-19 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 6eb19131-c826-38c7-a1ee-3089e01e2fe1 | -5.9011 | -43.6279 | 2026-08-19 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ff21a201-0362-32a9-a62d-c5b691a7d09d | -6.3496 | -54.9068 | 2026-08-19 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 14fdd724-5432-3da8-ae7d-934dd727dfb5 | -5.92 | -43.6032 | 2026-08-19 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f841444c-9c09-3237-ae6d-c8769c85a020 | -5.9994 | -57.8639 | 2026-08-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 965dc630-0b5e-3e5c-bd2a-8697e7503586 | -9.4257 | -60.416 | 2026-08-19 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f8809dcf-eb4c-3c74-8618-518b5e1a4bca | -5.4503 | -48.4201 | 2026-08-19 01:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 352df800-a52e-3fe5-9c00-b6fd708d6e2f | -16.345 | -49.4851 | 2026-08-19 01:40:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6d50840f-e169-38ba-90f6-c6f04fa7a103 | -9.406 | -60.5711 | 2026-08-19 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f15b3fba-c055-32d1-b3fa-455c5ed99567 | -6.0178 | -57.8631 | 2026-08-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c7d23f5b-77b3-39ee-b9e0-dc92088b1b56 | -5.92 | -43.6032 | 2026-08-19 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b7e8515b-ec0a-3df4-b050-56d99472a8f0 | -9.3873 | -60.5721 | 2026-08-19 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b9bc8872-a278-379f-a747-e38879b747e5 | -6.0912 | -57.9187 | 2026-08-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 27b2c669-6c40-3de4-b1db-4adf9b292395 | -6.7123 | -58.9412 | 2026-08-19 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ee04e911-6328-3287-accf-143267181e21 | -6.0179 | -57.8437 | 2026-08-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 58743e2c-f5d6-3863-8fec-cfde945351c1 | -9.4061 | -60.5518 | 2026-08-19 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b1674622-dde7-3d10-9200-2ded1e404db1 | -19.7639 | -57.9607 | 2026-08-19 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 6fec7065-c6d5-3a2c-95dd-97bbd15052e8 | -6.0913 | -57.8992 | 2026-08-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ace42937-7935-304a-9b10-d545baa88ad1 | -9.3875 | -60.5528 | 2026-08-19 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f833aab1-3881-389c-970c-3b3ca9894929 | -5.9198 | -43.6264 | 2026-08-19 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 5e3e6802-edea-35b0-8992-28690ca689ea | -5.9011 | -43.6279 | 2026-08-19 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| e3c2ac4a-2e51-3073-8211-9f883a99f5e0 | -5.9995 | -57.8444 | 2026-08-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 317aea82-d864-35a0-b693-be08585a50bf | -6.6938 | -58.942 | 2026-08-19 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| aecb554b-b16c-35e7-8d68-841d16ba402e | -5.4317 | -48.4212 | 2026-08-19 01:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| bb2598cf-e4f4-3535-8099-df75d5378dba | -19.7643 | -57.9399 | 2026-08-19 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 6c703737-b453-366f-a3c3-4b08460ead24 | -9.4256 | -60.4353 | 2026-08-19 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 650e9e10-c792-313b-9f5f-7dc442443eaa | -7.5487 | -55.5829 | 2026-08-19 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a9bd188e-7a8d-3098-902a-0793664c0648 | -5.4319 | -48.3996 | 2026-08-19 01:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fcc1fe64-ee51-33fe-b70d-e24ed76590b0 | -19.7442 | -57.9425 | 2026-08-19 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 79c581ff-7fb7-3d71-82aa-b96e934743c1 | -6.8593 | -59.0318 | 2026-08-19 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c73d49f2-4a56-3b90-846b-0d6c3afc1d52 | -7.71589 | -72.82872 | 2026-08-19 01:49:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| db0f5494-e920-31a2-9037-e302cb6dc392 | -5.9011 | -43.6279 | 2026-08-19 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 181e6ee0-9192-3626-844d-de5f0b721ab3 | -5.4319 | -48.3996 | 2026-08-19 01:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e0a37614-d63b-3a8f-baf3-1f46364762f0 | -5.92 | -43.6032 | 2026-08-19 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6c9501aa-3584-3a54-9399-64b990394ff7 | -6.7123 | -58.9412 | 2026-08-19 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 690ba19e-d669-31b7-a7b7-a79f7dd7e640 | -5.9994 | -57.8639 | 2026-08-19 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 97f8e5d7-d4d4-38de-b906-bf5795f2e46e | -6.0728 | -57.9194 | 2026-08-19 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |


[Clique aqui para ver as próximas entradas](README16.md)
