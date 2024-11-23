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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afd934d4-abdb-3c64-b959-a81cfeefdfc8 | -4.66476 | -45.68064 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| defa480e-2d0e-3678-9c0b-12196bc59c92 | -4.10021 | -51.07407 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64774dcd-6963-37e4-855a-459611dd6aee | -3.23976 | -54.24383 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 065639fd-dafe-3573-8b36-2f47b8c558bd | -2.45306 | -53.70347 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 068ba6ca-9887-31f0-941c-fcaab30ac9c8 | -4.34586 | -45.8831 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 431761f6-828a-353a-be56-edd37dffcb45 | -5.93212 | -43.77973 | 2024-11-23 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9013d14-775a-3713-8bc0-c37f34996ca0 | -4.70128 | -45.85285 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cea27d7e-b6c6-39a2-a4fb-950f8b0a9388 | -6.56361 | -39.76685 | 2024-11-23 04:18:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0860dedc-9843-3959-b926-16591a1b44bd | -4.29099 | -46.5814 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 494ea941-68e2-3f57-b50e-fd86e4b7185b | -5.97183 | -46.30676 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d5d2d3f-53c5-368c-9e51-9738c025756f | -9.13249 | -43.11076 | 2024-11-23 04:18:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 12d1fc6d-6633-38e6-aa65-bd5a5db834e4 | -4.09202 | -47.03642 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a36e956f-694e-32e1-b310-f1b617c0fcbc | -2.91096 | -53.06504 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d2369ef-d242-3d35-b3d0-c61437ff628b | -4.69509 | -45.84819 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 25639987-9170-31a7-b6dc-c30af64eeee9 | -5.59834 | -43.74154 | 2024-11-23 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 402c5bb1-c0fc-3069-b9c2-fde23d09b88b | -3.23905 | -54.24806 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c5bc5b-05be-3717-8c1a-73f11204d3eb | -4.73165 | -44.43767 | 2024-11-23 04:18:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 162f765d-b249-3139-b6e1-41905e7cca12 | -4.00187 | -47.91931 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d320be62-4f9f-338c-93eb-771fd64eb30f | -5.3299 | -45.49006 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf30d9bd-efb1-39a8-833e-9fcc684e5c8c | -3.70624 | -47.61837 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d8ad6f-1683-382c-b754-7487af41bcfa | -5.8471 | -40.79982 | 2024-11-23 04:18:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0dafdf62-4465-3428-9145-1574b434b435 | -3.00662 | -51.31153 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0104ec0c-60d4-37fb-9f4a-71353a0a81ce | -4.25061 | -48.70602 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bac200e-219a-37a7-899e-c2603669b4a3 | -4.54578 | -45.88424 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3ea91c8d-e9b4-3727-be38-7b572db60da6 | -5.68048 | -46.48465 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f44ca9a7-c099-3acb-b3fd-71c83e7e838d | -4.67553 | -45.66769 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b995e5fe-8bb9-3f95-a1f1-7855a3adb547 | -7.30321 | -39.62115 | 2024-11-23 04:18:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a314bd30-1807-340d-bcae-930defc48363 | -6.15079 | -46.67677 | 2024-11-23 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33a0e498-169a-3a49-b225-caf3bb178685 | -3.84521 | -43.93809 | 2024-11-23 04:18:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b0e704a-c2fc-33a6-9c09-c8765b53bd9c | -3.67089 | -47.13785 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82c16799-edb2-32e8-a2c8-330b349fb8b2 | -4.11638 | -48.52073 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af095505-674c-399b-8094-a0f020bba51b | -4.53456 | -42.9219 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc2c140c-1a8a-368e-a26b-feba1cb74e72 | -6.3515 | -46.75842 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93d58bad-133f-3f1e-a32e-0e604ce1cde6 | -5.93157 | -43.78323 | 2024-11-23 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68636c5e-820c-32b7-8b41-0178f696d048 | -4.03335 | -46.19473 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68c75bdb-891b-31dc-a74b-0445b4165d07 | -2.82201 | -54.03312 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13fd13c7-61da-33b3-a6fd-4f0e7eaaef3f | -3.46836 | -47.68504 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a67600-0972-3810-b3e1-edd14582052a | -3.54858 | -51.53749 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 771b4b01-d7a9-30f1-b4bf-e38385e16e8e | -7.01572 | -39.22892 | 2024-11-23 04:18:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee898025-05b4-3f6e-bb73-db81053186ff | -5.26392 | -44.72623 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77f9489e-3928-3e9b-aa74-6bd6d64b42c2 | -5.9991 | -44.63034 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eae43123-1435-354f-91b1-4a86d594ec57 | -5.68108 | -46.48091 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0b98320-485c-3594-8f6b-278ac43f9b9c | -9.81658 | -39.1518 | 2024-11-23 04:18:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db2880c1-861e-3e0c-ba1e-67d278397ac3 | -3.00542 | -51.55602 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf6569a2-bcd0-3337-a109-263f2b20c4d6 | -5.44265 | -45.588 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 398c5f06-fd57-326b-b07b-128f4cb63696 | -4.44819 | -48.20219 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b590583f-95c6-3a14-bf7f-657fbf2cb257 | -3.22576 | -53.94308 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12acdc2c-cb62-3e2e-b573-2091bbd3174c | -3.96847 | -46.65104 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d70c16a0-b973-30e4-a784-43f6f6b4c1e1 | -3.89173 | -46.65867 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a0e7420-a4d4-356c-bbb8-e190bac7fd87 | -4.10718 | -48.50434 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10c647ec-4dd7-384b-b387-9fe0c37ce466 | -4.72419 | -45.49276 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2f1d6e6-5534-3ff4-a061-2d6c73afd595 | -3.58612 | -46.20733 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e67add07-669c-3602-b745-2747e74c52c4 | -6.49591 | -47.04337 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dbe61d35-629c-349c-925c-c8a4c35d592b | -3.25991 | -53.27212 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39bff4f9-1eb6-3919-8146-e1ab22b177e9 | -5.16382 | -47.03804 | 2024-11-23 04:18:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3059461e-05a7-35e5-b3c4-f979c6607fbb | -7.11086 | -45.37846 | 2024-11-23 04:18:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca31163d-c8fa-32b0-8cce-3c5b45ecd74c | -3.25354 | -54.2373 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 94a399fa-ce5c-3768-a905-6e8ce684daca | -3.70832 | -47.612 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72989c89-9466-3f77-acac-6c6fe93d7679 | -5.18823 | -46.14178 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d60c772-ff3f-39a1-9e29-fc18e9310428 | -5.74392 | -46.26314 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a413f4c-faf1-3b12-8a54-6d88874e413e | -5.1174 | -45.84031 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a36a05f-3e71-38ee-a9d3-4bd501374d01 | -5.46623 | -43.23977 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cba5f91-946d-3600-97f5-b8ee341a4096 | -4.10791 | -42.47079 | 2024-11-23 04:18:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 796f2541-890b-3de4-a4ed-a90746b6055c | -2.92936 | -54.28436 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a99a948-d843-31a9-bb6a-73bfd0221587 | -4.25613 | -48.69669 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 2ebfa9af-fcf4-3a25-b2a7-125a01acf32e | -6.61659 | -47.90403 | 2024-11-23 04:18:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f37462e-f5d4-307b-b2e4-5063d3967f80 | -4.6895 | -45.68824 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b63f4e9e-2990-3469-8c2d-da976cb036fc | -3.93733 | -48.14991 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7eda056-bb1f-3e23-a63a-e25424523d6d | -4.54298 | -45.88002 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cf8edcdc-87ce-3cc4-86c0-011380e8a087 | -2.82033 | -51.79997 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94330144-1233-3d06-9059-b833db86a3f0 | -3.63182 | -44.34567 | 2024-11-23 04:18:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4438b617-cdb6-3998-ace9-6e19ff544de8 | -4.69393 | -45.85546 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29f122a6-057e-3090-8b9c-df20e679acef | -3.93533 | -47.01621 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c380b38a-1f7c-3294-8601-8c64a9c54342 | -3.75395 | -50.008 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72210848-bdea-3c07-9412-94987dcc79ca | -3.25397 | -54.22945 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2f2a9a6-f243-3e49-80fa-eb8a16a6d6ec | -4.26237 | -44.69914 | 2024-11-23 04:18:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1437ac05-23ba-3a10-8888-f0fac538c9fb | -4.54519 | -45.88791 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ffa6b029-1528-3dda-87a9-57548b53d3f4 | -4.34809 | -45.89092 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a89b2cdd-dec4-39f7-995f-9e30f3f71619 | -4.72716 | -45.6685 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f370d7c-24d9-3053-a8de-922255671a41 | -4.48121 | -45.6523 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16352961-cd01-30eb-ac5b-3296f0c268cf | -3.0006 | -51.55519 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4da7a76-c421-34b2-b9fd-5f86c7ac80f4 | -4.29075 | -48.07524 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76bb8c88-5033-30b2-8b04-900f3d0b38b8 | -7.03716 | -46.99031 | 2024-11-23 04:18:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e12217d4-2477-3c47-9419-7473ba671146 | -6.15018 | -46.68051 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cdc41bb-5ee7-380c-954a-e8cd6af620cf | -3.23124 | -54.25944 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0cf81d8-edf2-3ad2-b20a-47b0e4211e31 | -3.25333 | -54.23337 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 70602db9-7a80-30b1-a81d-42f088569b1d | -6.29852 | -43.43277 | 2024-11-23 04:18:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38dec87f-b5e8-3d35-8ade-0072a1ed1018 | -5.7479 | -46.26002 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 187d4587-687f-3fba-a349-1e2e7ce5259f | -5.40354 | -45.13186 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0942dea0-c5c9-3827-bb21-37f790d3e563 | -7.19158 | -46.25289 | 2024-11-23 04:18:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 87b87859-c52c-3bd1-95b5-fc5cd5522dcc | -4.26277 | -46.29132 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc856712-5f4a-30ae-8413-1c0f62aa4314 | -7.63533 | -39.82397 | 2024-11-23 04:18:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e05a228a-8614-3759-85fd-ec11d4236362 | -4.51748 | -46.73406 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60aa2f12-315f-3431-a08d-8f3a6cead5d2 | -4.10735 | -42.47442 | 2024-11-23 04:18:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b22ec34a-fc85-3c62-b6e2-a0f7e6fc5d81 | -6.78054 | -44.08672 | 2024-11-23 04:18:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98522b36-ccf1-3d0a-8e2a-9c701ca53e42 | -3.75247 | -50.00703 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36ec5a20-7279-3548-a298-f01562106cc7 | -5.44656 | -45.58499 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22e7006b-e789-3e7f-b87f-0c70e5ffe9c5 | -3.96908 | -46.64719 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5e887507-2f5b-3b47-9b0b-ae502e85b7de | -8.71183 | -44.00452 | 2024-11-23 04:18:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e82d182-cb2f-30de-9311-5935edc232c2 | -2.7613 | -54.07317 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README39.md)
