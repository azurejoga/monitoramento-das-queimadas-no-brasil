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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29c12332-aab3-3a3f-b18a-d76e32934a81 | -5.88431 | -57.76925 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e2fe80-4b30-364c-95c9-9608e74577dc | -6.67838 | -58.74981 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1940d0c9-878b-37d3-bad7-faac658a7c8d | -7.69567 | -63.32703 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cbfb790-0dc1-34c4-948a-8f1e17d4e4d4 | -1.60624 | -54.41233 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10a97423-8d22-382f-bfa5-49bfbf3e0380 | -5.88522 | -57.76282 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b11d4b8-7776-38b6-b211-d63c73b99536 | -7.58331 | -61.35033 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc162951-d8ee-3100-92eb-6188ea03f11c | -5.48269 | -57.1456 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7836752-4f4f-37a6-b9da-2724bcf5a9fc | -7.40243 | -60.58439 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6692ecf8-db42-3e3d-b500-d39b59b9c75c | -5.85774 | -57.55367 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67b92142-e338-3774-aee2-701bfe995a63 | -5.48877 | -57.14269 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c822b04c-2a0e-377d-a41f-b7907a98fb60 | 0.98981 | -59.87691 | 2026-08-31 05:53:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0595bf00-8cef-3388-8ce9-9f6664e210f6 | -7.69257 | -63.32182 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f140d7f8-2991-3a77-bced-7023db61bc0a | -1.59994 | -54.41155 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d048552-3354-34b8-9eb2-5ea15e78d8c6 | -6.77539 | -55.64682 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccbbb14b-cfc8-3acc-a37a-9e2ed7da1568 | -1.62536 | -55.17043 | 2026-08-31 05:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fa01ad9-2117-30fa-a8cc-7418449c9283 | -5.87167 | -57.78122 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5a87b2a-1959-3a74-9708-2b61a366ab7b | -6.90762 | -59.486 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0525e02c-9fa9-3032-ac2a-183250e2da03 | -5.88568 | -57.75957 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df2e9451-a3c3-396f-a32b-17bbba83fda6 | -5.24727 | -55.89037 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 395b727d-83dd-3368-ab44-ed962c2dfdf7 | -7.60919 | -61.36948 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 75f7c168-5d43-3541-ba67-5e4e86e49c0c | -7.58311 | -61.3365 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f9bbb94-8306-3939-bc3a-56c23a69465e | -6.41849 | -58.23116 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d3dfee1-11dd-30fe-8349-0708d896a6ea | -7.61289 | -61.37423 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b61f2681-d915-38c1-a347-a915c3a30b04 | -5.24665 | -55.8949 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13bf6cbe-7e6f-3f78-9717-25915c40dcc5 | -7.3347 | -60.59458 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7fcbe8e5-87e4-3363-93ad-ef551372f4e2 | -5.57456 | -60.23343 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbcdc562-d9dd-35c2-97ac-67354b21e1e1 | -5.95376 | -57.68289 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d94c0f1-4b00-390d-a544-0de9d21a3509 | -5.24603 | -55.89939 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 014e32db-ee2a-3d36-885c-ef3de178c2bf | -5.49491 | -57.1453 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e07a2d68-2d28-3e85-821f-831306304c35 | -5.25358 | -55.91542 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 88601875-a4fc-3b7b-8798-dd23a2725e52 | -5.24484 | -55.89126 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ed8c21e-b265-3b9c-9929-c88e787106e6 | -7.314 | -60.57823 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd05e526-12ec-3f0d-a97e-b9b7907df107 | -6.15133 | -57.78236 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb8d1718-2e77-32b2-a319-3b7ad1aec08d | -6.92625 | -55.72504 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fec6af91-83f2-33ae-aacd-8ca3a3ad3ad3 | -6.12201 | -57.67957 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 82fa257b-2b05-395e-b57e-93856b65c6f3 | -5.31942 | -55.85806 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7011e1f6-d0ad-36a5-ad7a-047304d6c32b | -7.29468 | -60.58437 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa525347-f8e6-30cf-b24a-d7eed9abe393 | -7.44266 | -61.42276 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5633ad1-0cfa-394c-b6e3-8cb400ece950 | -7.5623 | -61.31379 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbc252ad-3e64-3f63-8d6b-02b5ccc18386 | -7.33986 | -60.59077 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6548c46-076a-3efd-8b31-fdec1878364d | -5.94198 | -57.68842 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48c5dba4-db9d-3dd2-82ec-6ab747a7bed8 | -5.25141 | -55.90477 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cf7887b3-5df2-3e3a-83cf-a5b1f62a7aa9 | -6.90614 | -59.49658 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e9c5ba4-ace7-36dc-bf05-aac7bc8f18ea | -6.91581 | -55.70846 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 683c1552-07dc-3f97-a29d-cc254e9b5008 | -6.12792 | -57.67683 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7ccf863-2e71-3807-9414-2fe2816b2049 | -7.31211 | -60.59143 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3184a172-82f4-3d54-a355-d777f58afc2f | -7.84227 | -62.31683 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3986647e-791a-3cbf-81cf-d1835c60de74 | -5.94554 | -57.68716 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| baed8810-0241-3f57-bc28-756f55c1b328 | -6.1592 | -57.78325 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18907dfb-20ae-36c4-9dcc-5c732db87df8 | -5.48319 | -57.14196 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 649ba816-7a9d-31f6-8770-b01f55eeb5c7 | -6.92694 | -55.71994 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f90f68e1-fa76-3b89-8563-f0d7d67a123f | -6.75439 | -56.33933 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7858710a-1280-3492-b844-18bb38d930ca | -6.60693 | -58.60675 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| aac5344a-a25f-31de-ba7d-1cdef8a07698 | -6.86405 | -59.47955 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 886776df-5e83-3eae-ace9-2f3d53df981b | -5.49483 | -57.1399 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2057b1d3-aab9-3af3-97cb-ba5ea9b02ad8 | -6.86552 | -59.47758 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab21a0b2-cd8f-324d-8522-67580b330531 | -8.02971 | -61.25533 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab9a8279-18ce-3caa-9134-cd209cea4aee | -5.93865 | -57.69669 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c44965c-005f-3728-95d1-a121cf348174 | -7.52144 | -55.33947 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a6b4618-65c1-3fa6-b7dc-6bb4382daae3 | -6.56392 | -58.55906 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 819476bc-199e-3f01-bd84-529d9f6fa06e | -5.94151 | -57.69184 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33162f9a-3ab3-313f-9a05-8c2b6c8f1497 | -5.30731 | -55.85662 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f048259-8492-36cc-846a-ff846ef734ba | -6.94767 | -55.70739 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cca947d9-8367-3026-a478-2f5b300b8f0f | -5.25621 | -55.89742 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee8266b4-0dc4-301d-9ee1-2251aaac22f1 | -6.86525 | -58.94782 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06c0eddb-ad1c-3051-8c71-447e13c48719 | -7.4372 | -61.43022 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3efcf663-552e-3d76-ad71-fbc5807e5ca4 | 0.01326 | -60.59604 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 766c6ed0-595e-3aee-9b53-312665a3b139 | -6.60267 | -58.59987 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 473f737b-0d13-3802-861b-cdbd3868dc73 | 0.01382 | -60.59955 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7e4f68-9165-3b53-a314-9568e447e155 | -6.79224 | -58.99644 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f2ab3cb-d0da-3a6d-8513-f25e0afbb4a5 | -7.27994 | -60.65579 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 896b9d76-5235-3a35-b800-cdd3ad9b5820 | -5.94454 | -57.69405 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 568a7bd7-b917-3f24-b583-686c08663eee | -7.24225 | -60.01031 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 660d1f94-2d33-368f-a32b-6f643435bdf3 | -7.61348 | -61.37012 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| afc59684-3fa7-339c-8b20-ed04c972ec36 | -7.32953 | -60.59846 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b194a5cb-020e-3bc7-8ba2-087657fdb3ba | -4.84858 | -55.8287 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3af3d219-3e24-3149-8121-d2af9d04f43f | -2.97934 | -60.9264 | 2026-08-31 05:55:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b00bd2e9-43bb-3df8-8f12-06d973330705 | -8.4347 | -70.41908 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0f45b33-b013-3ad7-a312-83cfdffbd0a9 | -8.9685 | -62.3959 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fbf9ff1-f6fd-36bf-be4e-5ba881fe8284 | -8.86812 | -66.7795 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12698adf-526c-313a-93c7-9a010a17f915 | -9.16181 | -59.50639 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53a8b79f-2801-34fe-a961-0aed1f467c8d | -3.11129 | -61.229 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abcb6437-8d89-363a-8817-92889ea698cb | -9.84432 | -64.98195 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01b74d09-b8f9-31a2-a4cd-c9807d28baf1 | -4.96497 | -55.84397 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57a233d5-590b-3f74-85f0-878399a5ad8d | -9.84015 | -64.98548 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e736a2-6403-3454-b01d-90715d986f69 | -9.88746 | -60.27279 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91b702b8-098b-34a3-bb74-7ca51a70e6c7 | -3.18963 | -60.15425 | 2026-08-31 05:55:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8efe95d0-85ad-3e12-87e2-e4666ffd17a3 | -9.71898 | -64.99702 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d91ae1a-969c-31ff-a41b-29e6a3063f57 | -9.20085 | -64.44591 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d7921f9-c3ac-3147-bd5b-858806aa8579 | -8.87327 | -66.89944 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0502c5-edef-3f16-9a84-d070dd899e08 | -9.05728 | -65.40973 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 736e1bc3-7af0-3e12-a298-14725a7c597b | -9.84371 | -64.98602 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d456dca5-d0fe-3520-beb5-297ec95ab0b4 | -2.97876 | -60.93011 | 2026-08-31 05:55:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 527b8501-f36d-3848-899c-b2ff33d4c23a | -9.90937 | -60.15132 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6d2e0d7-a1e6-3718-8fd9-d905cfdeac2e | -9.93717 | -60.51178 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75e2fa93-7111-3853-948d-51d5a5e3b913 | -15.55053 | -56.28083 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99388b1e-818b-327c-a735-2187ddfa42c9 | -8.14709 | -63.9988 | 2026-08-31 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad51318a-1e24-330e-a148-274ea38ffb66 | -9.15049 | -61.09622 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27bc66a9-ce23-3878-92b1-9776d74d8d69 | -8.93013 | -70.69009 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4097a37b-89ba-397f-a359-bcc9a3b015d6 | -2.74903 | -60.23772 | 2026-08-31 05:55:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README74.md)
