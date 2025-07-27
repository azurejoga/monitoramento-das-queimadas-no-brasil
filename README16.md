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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 116f3709-975b-34e9-aa65-4e114effcea0 | -6.6671 | -58.8473 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b9380cf-c8ec-32f4-af4c-dcfdfc4be8d4 | -3.57093 | -49.50431 | 2025-07-27 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9f2c8c00-1b62-3ee2-9457-dbf6b95822fa | -7.56827 | -61.40634 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23061c07-12ac-3c57-b6df-6f3e73464cbc | -6.6329 | -58.86178 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ad62d202-4d52-3dcf-b8ef-a990eea56530 | -4.13069 | -47.64761 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9593dc07-9804-381b-b966-b4d591bbe82a | -3.27836 | -48.8173 | 2025-07-27 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a36da79-0d77-31c3-b9e2-585c6a17dbf5 | -6.55258 | -56.19965 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e53994aa-3402-3c9c-bba3-1971adee0fa3 | -6.49294 | -56.20146 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4cb8324b-bba3-3225-b918-c4921352011f | -6.22777 | -44.52337 | 2025-07-27 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cedc51a-94b4-3534-b536-54db005c6e82 | -7.75957 | -51.12313 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77893eb3-6799-38d5-915f-c20f275bc862 | -6.89228 | -44.80629 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d204d2e-f806-321a-844c-bfd09a23dd7f | -6.56337 | -56.1976 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 875b5896-118a-3d12-9905-753e9894c654 | -5.77814 | -43.60728 | 2025-07-27 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f3c9d6e7-a988-3815-96d6-49f3c642b9c0 | -3.06761 | -49.50248 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16b78e21-10e0-3745-9771-674b3bcf39a3 | -6.89099 | -52.8686 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c775017f-b805-3246-a79e-4936b526dd57 | -6.01407 | -44.05648 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ee7ee7f-b4bd-3afa-acac-c861e1cdc0de | -7.8046 | -46.5685 | 2025-07-27 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 724b013c-8fd0-3ed7-8f33-01bc86432452 | -6.6315 | -58.84636 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c9a335a-54a7-35c8-983e-15311aed284f | -6.66404 | -58.84181 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a8d3813-3e9c-3c08-94a6-9e9c5d6727d3 | -3.37234 | -52.80179 | 2025-07-27 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8694299-7a4b-3bdc-8589-7b2d5c9dedba | -2.90735 | -48.24857 | 2025-07-27 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e84087ee-089b-34d3-a190-89501ec3cc08 | -6.66243 | -58.85154 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 38b6c4fb-f566-317b-b3a5-7a4f58268d0a | -6.54015 | -56.19009 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8c44ee2-6d2a-304b-a1ef-cc258ba3fe68 | -3.74857 | -49.04782 | 2025-07-27 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bcc6c26-bd77-3c9b-bc67-59cab1a35d23 | -3.13492 | -47.0112 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4441414b-150a-386c-b672-e8415091a219 | -9.43477 | -51.75616 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df608736-d200-38f0-9346-ca32c1753318 | -6.01273 | -44.05472 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec789782-a80c-3de0-b4f2-16004048b006 | -6.63537 | -58.84701 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0782371c-bde8-3375-8ce5-db81feb7053f | -3.39235 | -47.49633 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e8034d7-5bf0-3d69-9742-bde9dc1c91bc | -6.67097 | -58.84794 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3eb82488-c297-384b-a231-d0b73acbe89b | -6.54637 | -56.19485 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ea8aec2-352c-38c2-b144-21d293a27676 | -6.6563 | -58.84056 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06fa2b6a-5341-3b27-953d-7d5cb1952c72 | -6.01219 | -44.05851 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7debfb96-a699-3f1f-b7e3-f3205f6c22ab | -3.04864 | -47.38098 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36399451-6c46-36ce-8359-0a6595885877 | -6.66017 | -58.84119 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca51cd41-b9f8-37a3-bd58-6aee624424d4 | -2.91146 | -48.24921 | 2025-07-27 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2525c985-f27b-3c27-a9b8-89406f035606 | -6.55892 | -56.1818 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d19c89a-f92b-3443-a48b-905d2505a667 | -6.89043 | -43.10834 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89dba285-8cd5-3f34-ac45-a6e1e341899b | -6.53515 | -56.26493 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d951485-eca5-3df2-8fd7-261e7c4c5a03 | -6.53574 | -56.26124 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63fa668f-a4de-30df-8142-4d5db01bf38c | -4.59231 | -47.97625 | 2025-07-27 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d8cbae8-529c-3782-8954-1108710c5505 | -8.28819 | -45.00848 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b884b1e-5a5a-3b55-98bf-e103ac2a8041 | -9.43902 | -51.75253 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55237599-3a03-3d7c-a516-7c75820a3cb5 | -7.24537 | -49.62144 | 2025-07-27 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8aea414-439b-33d2-85d1-1ef6e96151c6 | -6.62598 | -58.85558 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 538181ce-d00a-32e0-8dd6-36e1a6c519b9 | -4.13447 | -47.65228 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 742d4fdb-bdeb-3375-a958-82eace1e9f24 | -6.64937 | -58.83448 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bf6f9e3-6b04-37cb-b42b-68734200cc10 | -7.10432 | -59.76427 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f72674-d369-3785-8aa7-0e6b5de0608f | -5.18728 | -44.9545 | 2025-07-27 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9aafb76-4ba9-3dba-9526-a541a6c3d691 | -6.53633 | -56.25756 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 260fcf45-db39-3316-b2c1-9eeee1beb904 | -4.11256 | -48.12572 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0419fcf8-1bea-3dd4-9b2b-6bdf3bb71f9d | -6.63759 | -58.85752 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 42d30596-60fe-3d23-9e41-0c0591a9bc15 | -5.68168 | -43.6651 | 2025-07-27 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfffa0a0-fc91-340c-9557-868e967e74e1 | -6.54296 | -56.1943 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64b001b7-87d2-3e23-88b2-cec77fc140f9 | -8.29476 | -45.00164 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f346f56-7fcc-338f-a44d-84dd78d26769 | -3.36536 | -49.16741 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c6b0bef-85aa-326f-9c45-80955002811c | -6.6819 | -58.82975 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fe97a25-2279-337f-ba5e-f5530f383f8e | -6.66324 | -58.84666 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f109f74e-24d0-3b97-ba40-e8976679aaf2 | -4.96086 | -43.72916 | 2025-07-27 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98de9c37-e880-3287-9846-45f3bdad3173 | -6.65163 | -58.84478 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8b8139e-61eb-38d6-ad72-fa278a4a4f5e | -6.66257 | -58.82664 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48677927-9d8c-3667-90dc-78d4f907ddda | -6.65484 | -58.82541 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e24fefe2-a982-3ed4-b968-a12fd8f77714 | -6.62293 | -58.85004 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70d5cb85-b18a-3bdf-93f0-bec1a3993ecb | -6.02024 | -44.05412 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c520b2d-319f-3423-9f6a-68e653eab01a | -6.54754 | -56.18752 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4b2f16b-3ca3-31b2-807a-7d1452bd2897 | -3.14402 | -53.13189 | 2025-07-27 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 701a5758-1502-3c7e-8bbb-cffebefcd2e7 | -3.48391 | -51.18777 | 2025-07-27 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14724734-7ca3-3984-8597-b25c95637a9f | -3.06366 | -49.49975 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54a736c2-21c1-31ef-b30d-0ea7e1b4de70 | -8.87627 | -49.00859 | 2025-07-27 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8df9c6d2-74c9-30c3-b295-cd93292214d2 | -7.08655 | -44.90859 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d66ad8ff-6476-3a60-a49b-85c438411936 | -6.6803 | -58.83944 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76c2b79e-264d-3e58-8a74-46504a648301 | -6.64776 | -58.84415 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a8902cf-6a41-3a39-9c82-fe49a4b3f276 | -8.44043 | -47.51503 | 2025-07-27 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fb875da-6a15-3b8a-9055-9b5d8dc6e9ef | -6.65001 | -58.85453 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f1948a4-9292-36f4-8c9b-9a77a4511586 | -6.39638 | -53.33851 | 2025-07-27 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afcff861-0404-336d-8c57-a5bcc42b5969 | -6.64856 | -58.83932 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85b934af-c8df-3d71-a3d2-7791a472fb8f | -3.07058 | -49.50559 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f48c4b0-5a61-33a9-b3ab-468a59d80480 | -7.4997 | -63.5047 | 2025-07-27 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95001f1d-ac67-3263-8161-6946f05fbc52 | -6.8918 | -44.80988 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd5231d7-c835-3083-a524-28b0507da6ef | -6.64228 | -58.85326 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 205f69d5-a451-347d-bc03-fe2e818f0d10 | -6.65082 | -58.84965 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1afcaf86-44df-3530-bd6a-f5b08ecaa92f | -6.66484 | -58.83697 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c9ee8bf-9d0e-36ac-8717-a0aae74865ef | -6.67257 | -58.83819 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aee460f4-fb9f-3aaa-9690-9dfaea175dbb | -8.17331 | -43.19506 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d6f128a-a0f3-3468-b6ec-fdb5536945ed | -6.6447 | -58.83869 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c72bb36-7602-339a-b0bb-be369f0f313b | -3.40481 | -47.50245 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef80a23c-2ca6-38a3-b351-cb764f552f38 | -8.01244 | -48.17204 | 2025-07-27 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bd7aa70-6dd8-3389-9ebc-ea5100ebabea | -8.04557 | -50.67733 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 712241bc-f5a8-325c-b792-0c48e9b893d2 | -6.67177 | -58.84307 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b8b177a-9958-39f2-b08f-b7d97f8172df | -6.55317 | -56.19595 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f06bfc-cf91-315b-8350-2f938daf0906 | -6.63231 | -58.84151 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04c8e131-af69-319f-b53a-9ba1f8f41d8d | -7.28817 | -60.18426 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd9e204a-6a1a-3be0-83f9-717e2d38b641 | -6.67417 | -58.8285 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a27b3d5-f6eb-34c1-854f-5e0311e2daee | -7.293 | -60.18108 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| defbc0db-640a-3076-abac-dc02c9f3b08c | -6.89592 | -43.11413 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ad9518c-30a9-38fa-a605-6477e27113ca | -6.63006 | -58.83123 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0f1975e-68d3-3dbe-afc2-2dd87a84e2a3 | -9.43237 | -51.7473 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 043a6d39-558b-341d-8abd-2cec0552aac4 | -3.0669 | -49.50708 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f454855-34e8-3c79-ac84-5e10ec3e4349 | -6.89658 | -43.10928 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18a22a00-cf14-360d-9186-46bfacc837e6 | -7.74909 | -51.11765 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
