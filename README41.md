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
| a41f0216-f9cc-3fa2-9eca-889b61f64a08 | -6.25149 | -60.02023 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb9192df-24f2-3ee4-8617-01915d518fac | -8.89368 | -60.76166 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87112db1-7ee3-3ad5-9d12-601502676051 | -11.14159 | -46.34034 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b96bc86-e9c4-31be-9066-18018c4d830d | -8.45423 | -43.66964 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0f3c8e5-ccf0-353b-91b8-aa05383daada | -8.26618 | -45.0616 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15959369-1beb-3aa2-9a53-d6f4bc30b5a1 | -8.2458 | -45.14834 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98f1498a-717e-3a78-8046-5f35108f832d | -7.12077 | -43.69213 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67792bb9-40a1-33b5-adfb-f27dab412c8f | -9.1599 | -59.56478 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2ac71d02-4837-33ee-b0e5-b74242eef88c | -4.49545 | -46.37062 | 2025-08-27 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d964ebf-28e6-3918-8e11-af4f0308c97f | -7.4033 | -44.06824 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 597cbc98-a257-3f75-9444-b96c63f2c2a9 | -10.63423 | -47.48291 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96e50e9e-53d5-3c6d-9525-e37ffb1aee77 | -8.48559 | -43.65736 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73f28de5-1fb8-3633-b1d6-a33a9ea026a9 | -6.57354 | -47.38376 | 2025-08-27 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a7de8848-22b7-3f81-9658-8a30d422fbde | -7.7353 | -50.28353 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c5d46d9-3011-3507-81d9-9c6a94d139fc | -8.32668 | -44.80453 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aefddb88-b08f-35a5-8b9c-c17683269460 | -8.67918 | -47.98627 | 2025-08-27 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 977d59b8-60f9-3df9-a1c8-283be465bdfa | -7.59433 | -43.95408 | 2025-08-27 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee42f59b-001c-3f51-bfe7-965e30026e42 | -9.78542 | -46.02665 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e93a73e9-c8d2-3610-aac4-9d8650e63f0a | -7.76548 | -43.63255 | 2025-08-27 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70401e99-4b44-3710-b0c4-cbf9792fb5c5 | -6.5702 | -47.38322 | 2025-08-27 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 77443308-2d47-3a9a-9f4d-1630445ffbcb | -9.97259 | -46.37525 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d148de9b-67c2-3732-b9d8-713d5a9abfa8 | -9.06076 | -49.55775 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ce7f25f-f2dc-3660-8d4d-bf180cc1fc86 | -4.49822 | -46.3746 | 2025-08-27 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a25a510-b816-3082-8db8-697f0928b8b1 | -11.57972 | -44.65067 | 2025-08-27 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7496988e-ccbd-3ba0-b2c2-50449930714d | -6.29864 | -45.57377 | 2025-08-27 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48597b6e-a04e-3b29-be14-dcbd29a2a926 | -6.80042 | -44.34804 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd6b705e-96a5-3a00-9661-98bf10ee7ea0 | -6.68767 | -58.54781 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1c85ffa-50fc-3b33-8465-7826efa79cd3 | -7.56559 | -47.48735 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc86b0ec-fdc7-35bb-922b-f8028e2a60d4 | -11.15464 | -44.78795 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1c5db38-fb02-3608-ab88-fe101bf82705 | -5.7408 | -46.14248 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d7a969a-5fed-342b-89cc-7919a25e0d06 | -7.63875 | -42.68588 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bbb189b6-4c03-3439-8521-6acccd1570bb | -10.12521 | -47.43641 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8c2bc65-2796-3ad2-966b-4c52b9479dc4 | -8.468 | -43.67601 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5052f527-ba96-3ddc-963c-424227c058da | -8.08477 | -45.01464 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 134b2348-f63a-35cd-9528-75c961559a3d | -9.50323 | -46.70716 | 2025-08-27 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c42d19-4784-3763-bbda-77a4d1feeac3 | -9.18352 | -60.80549 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bd4ca813-491f-3df7-aec9-f8af0dc1a104 | -9.17418 | -59.45752 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4be15392-6625-31bb-9a8a-eef2e013b6fb | -10.76495 | -46.38756 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7274b7d7-919c-344e-aab6-3e82b93268e8 | -5.63563 | -45.25165 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afef0342-44af-37a1-b534-bc3fa4d13ac0 | -5.83093 | -43.21658 | 2025-08-27 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40d0bc2a-812a-33b7-bade-62738e4b6ce0 | -8.29632 | -46.32619 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 435f2a17-3e79-3ce5-91b6-3acf1a1262f2 | -11.1349 | -46.33929 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1b3d2505-31de-3f3f-b5cb-82c823a85e39 | -8.25374 | -45.11951 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f44eec5-cc7d-339b-983a-661328856b19 | -7.56835 | -47.49142 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05d782c0-783e-344a-a77b-73a93061bdfc | -11.25787 | -44.99253 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d37fd5a6-fc89-383a-86e9-331b33f099e8 | -3.98341 | -47.88278 | 2025-08-27 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7109adbf-1a22-3fcf-b377-d9ec0d435403 | -8.49113 | -44.73754 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 937f701f-60db-3fab-a641-bfd39378dcd3 | -7.35675 | -57.62732 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9158d145-f0ec-3f72-b725-6edb90cfadd7 | -5.69012 | -40.98137 | 2025-08-27 04:25:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b897fb1-e9f3-3c1a-9e39-077c8af02bd9 | -6.25001 | -60.01451 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ccc543a-5ff2-3bc5-8da9-801a3bb64b4e | -11.45498 | -47.31691 | 2025-08-27 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a81a292d-5255-3292-9308-c80d2bed35a7 | -7.39282 | -44.06654 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6d6fa95-bba2-37ce-b5f8-53e0f56bf6d8 | -6.95818 | -44.09476 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1e6f21e-91a8-38a0-aab3-8061b6e00a25 | -6.52252 | -42.97522 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c36cc812-1d95-39cb-826b-905ef28137b9 | -9.5114 | -45.41166 | 2025-08-27 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09112448-8b18-3bee-b331-34d40de8efdb | -9.14539 | -60.79099 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f0fb7c-47dc-3cbf-8d70-636d2a2ac5b1 | -4.8216 | -46.00465 | 2025-08-27 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bad4d11-dc0b-3a1d-8f1c-772be6df189f | -5.21979 | -42.71831 | 2025-08-27 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6445f05-6961-3d62-83bf-e10f573cc9b8 | -6.78288 | -59.6412 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dab3fb2c-99af-32d2-bc28-f1a7e6ae052d | -9.14109 | -45.24934 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f1055b-e573-3d62-9111-c84caf4a8ff3 | -10.30866 | -46.8107 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9015a2fc-3582-3d21-83f0-c338db664ad8 | -3.79816 | -51.1915 | 2025-08-27 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cb242bae-9889-30b7-936c-a835700a3e62 | -8.49457 | -44.73807 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 110b31ee-405f-31ef-84da-fb95dd20650e | -6.3897 | -45.31447 | 2025-08-27 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e597cd5-d705-33ec-acb1-4a04b9127cee | -9.07417 | -49.56408 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26c98828-6959-3700-8469-67e7591e1026 | -6.7637 | -59.67179 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d014f69-dfd0-38e1-a603-2be7cdd00ada | -9.94784 | -46.4906 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 299fefd6-dfef-30be-851f-3b89134b2714 | -6.83017 | -58.97039 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9cff535d-e4fa-32df-aee4-bc6253c21c67 | -8.9043 | -45.71455 | 2025-08-27 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 559679bf-db2e-3db7-989b-85bcfd488fa4 | -8.27212 | -45.1183 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 466a308c-da78-3934-a4ce-9b72d9ca3cda | -6.38581 | -45.31749 | 2025-08-27 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad4d1ec8-cb01-3a68-8528-fd1383025ed6 | -7.65354 | -42.66448 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 66a14e46-59e4-37da-82dc-9ce867793bd2 | -8.25825 | -45.11279 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8a2f6e8-8733-301f-86ce-18afe0280849 | -6.81933 | -42.81544 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 540f429b-a3d4-3672-875a-ab8e9256eda9 | -6.84333 | -58.97271 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a11d633-c243-3297-8624-58a63009f0d0 | -7.59844 | -43.95071 | 2025-08-27 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e19d5812-dcf6-35cb-93d2-4d8cf7581f3c | -8.25769 | -45.11642 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27bee796-aa87-34bc-b9c1-264f383eeb61 | -8.07223 | -44.98272 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19e7d65a-9432-316e-aee8-372001eff303 | -7.08006 | -43.64883 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d06458b-a13c-36d2-9e04-c0457d8415fc | -9.25063 | -56.90767 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1b91f0a-ddd6-3d34-92d9-9cb3c8d27e3f | -8.91996 | -51.04972 | 2025-08-27 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35915aa0-cb5f-3ee9-aa39-d59cd0367f51 | -10.77273 | -46.38146 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e647246-4651-34e8-b481-09565a13e35d | -9.0779 | -49.60858 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bff8afb5-7dfd-393e-a038-a5c8c45007c9 | -6.80922 | -44.99621 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d916168a-7226-394e-91cc-75c933864502 | -9.08494 | -49.60976 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75a4df03-b015-36d6-b496-870a58506a77 | -6.23469 | -60.01842 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c33c696-4cc9-34be-8035-6265b79514e2 | -9.50654 | -46.70768 | 2025-08-27 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7ebb0a4-4fee-3514-9c1c-c84577e60f5c | -9.5834 | -55.3822 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54bbe7c7-0ce0-3197-aaa8-acb6a3d330d0 | -7.25286 | -57.67415 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28fe77a9-55fa-339c-827e-9f41612946e1 | -9.19144 | -59.54239 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9fcf295d-f0d8-3d81-8e13-b913e31b4e57 | -10.47274 | -46.88997 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be1ea46f-352a-30a4-bffe-8dcf75389691 | -10.76106 | -46.39059 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb81589-7c7e-3330-a9c9-aaf181cd4662 | -10.31853 | -46.76925 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96b00396-96a7-3b86-8e8b-03472fb160cf | -7.16804 | -44.4634 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81374ed8-2e76-3e92-bf8f-c3fda48b5d35 | -8.88247 | -60.78096 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63b00e26-1bd8-3ac9-bd10-ae7e1ba22e07 | -4.09975 | -47.72532 | 2025-08-27 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5e0615b-a029-3501-b533-67fa5b4f3c39 | -9.17042 | -60.77519 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 887cba5a-9864-3047-b6fa-9b8a3c576f10 | -3.84745 | -55.81408 | 2025-08-27 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b765973-5980-310f-8eb2-6d61bb605940 | -6.5209 | -42.98685 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8a0507e-801c-33d6-8c86-cb1800052067 | -6.8312 | -51.39008 | 2025-08-27 04:25:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README42.md)
