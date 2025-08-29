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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02b5768c-d32f-346d-a0bb-3cd70150340d | -12.88674 | -48.13715 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 971068b9-14e7-3890-b8f4-ef6cc2605b9c | -7.96466 | -46.37457 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ea0d177-b5c2-3c24-b82c-1e5fa1c50e03 | -6.0198 | -44.48678 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eded2100-84e3-3350-b874-209f0a20258b | -5.33144 | -51.3261 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e15fb32-e890-328e-ac7b-0df841a327e1 | -12.9141 | -48.12413 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3254616b-60a3-35e9-879b-98f54d7cc73d | -8.45247 | -43.65436 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcec79a1-49f0-38ca-9b6a-90b3a84a99dd | -10.45748 | -57.95086 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 811f8b8f-4267-368e-91a1-511375159f9c | -12.8494 | -48.09966 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f3b59b8e-ef68-349a-a2a4-f2cb7d7c4fea | -7.047 | -44.37743 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3bfe543-e2f7-3ba7-bba1-b64dd30db303 | -12.88375 | -48.1326 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fa41da3-e4b0-3bff-a96b-3155354fc8e9 | -11.61025 | -46.20376 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50fff4ed-7ffe-3acf-aa3d-15c4dd7cccb7 | -10.98628 | -46.8554 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1a4b7704-373f-355d-b881-2bcfbc6000c4 | -7.0759 | -44.29333 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7926ec15-0718-309d-a40b-58aee082d6c2 | -11.45813 | -47.30885 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebcaa044-716c-3ee7-b5d8-a04f0bc731ec | -10.94835 | -46.85458 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a97cf798-9264-3ba4-8262-5f2d1a18c567 | -8.69448 | -62.47142 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fdf994e-8863-318e-b11d-a10f3bdc0b0f | -9.53901 | -45.86575 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d820cbf-127c-3d58-90e4-862c1f2cfa36 | -9.48387 | -45.40369 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9710139e-b4df-375f-89bc-e1be98eb24dd | -8.17242 | -61.36889 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b890c261-cd36-30f0-9f95-a4c38a814f27 | -6.7105 | -49.45128 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bc8db51-10f0-3532-b0b3-8fd74c43079d | -11.95572 | -44.84134 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee3703b1-549f-3302-8a09-129328998bb2 | -11.55746 | -46.35246 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d26f34c-81bf-3d39-b7cc-b5aafe6f0be4 | -11.22294 | -55.06683 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cac8bcb-f8df-3e68-8186-0176601e5459 | -7.05019 | -44.35505 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e5ffdf18-5712-3b9d-b9eb-0c4a3ad8e532 | -6.5408 | -43.92645 | 2025-08-29 04:40:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00f85508-9973-330e-b74d-50e78f180b96 | -6.54556 | -43.9232 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30f989ce-1f87-3878-b388-69c11b5ae9a4 | -8.90597 | -47.32241 | 2025-08-29 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09a48e38-6fa6-3f34-8de5-687c363de421 | -7.6224 | -60.8539 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c14f461d-9b6a-3e32-a838-16d84d6fcd72 | -12.83389 | -48.10602 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 837fc476-42ae-3a5e-b41e-a5f1761d5306 | -6.81761 | -44.35227 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f817bc2d-057b-345b-91f6-ec41cb25d030 | -5.75574 | -49.98633 | 2025-08-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89740ae9-12cd-3972-b361-2020703c1929 | -7.7757 | -45.46964 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9ad9c14-83d2-3091-84fe-8c8c96149f50 | -9.43429 | -47.63837 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63af2362-cf1a-3f0b-8a6c-95c85c676685 | -11.22265 | -55.05921 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f58c52cb-79f7-3d1a-a3ec-f427f4804c63 | -7.02813 | -44.68222 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0db9d9c-74b9-3170-b763-4b300e9d1700 | -6.70834 | -49.4651 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 734d1824-6732-312d-a61d-b1a50896d46d | -6.88379 | -44.44483 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 210d310d-1888-3891-8407-8ed61d89f1bb | -11.57707 | -46.26957 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ace537d-a288-3732-85d7-5bd44a23c264 | -6.51394 | -44.851 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05e73e09-1241-3621-81bf-2f71e001e5ec | -12.69204 | -48.16015 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 735c11c8-7095-34f4-9211-99cdf818d630 | -6.20004 | -44.13533 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69362b6a-6f2f-3bdd-86d2-0292a8025a76 | -7.15555 | -48.1748 | 2025-08-29 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 696b716a-5c10-3cb5-a3a0-37f60b84ee8f | -12.83212 | -48.16802 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59aa9747-b3fe-3054-8a81-f618a7ca3f91 | -12.81853 | -48.18647 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fcfca72-f569-385f-9ac6-05e7417cb90b | -12.79246 | -48.16586 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 142d01c0-5725-3e3f-909e-e7e8fa97f02d | -9.43369 | -47.64238 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 02f2b5aa-52a9-37e8-82b9-4f1c34ca60b4 | -6.49235 | -43.53412 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4826b627-50b1-32b2-91f9-174ea9cd2019 | -12.06702 | -46.62963 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39b536f9-7e13-36b9-8014-c03f4fe9cfae | -12.84226 | -48.09868 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3fd2b28-70e8-3988-abe4-6fb806538fd2 | -9.29959 | -56.81891 | 2025-08-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4645b221-e35a-3885-9df5-d083fabb9fa1 | -11.41361 | -46.90816 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 404c82e3-964b-36d6-9f08-5eccabdda211 | -9.67486 | -48.32176 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd4bda19-0ba4-36b7-8f5b-6e9a6e4e3db1 | -9.78082 | -64.24167 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d6dd1635-9515-3d8b-b09a-8a63d925245f | -9.69309 | -48.31654 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2cf8e73-d1c3-313c-b4c4-c8d7bd5d0c9e | -6.02137 | -44.47636 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85894950-04f3-31cf-b8f9-8c61e5679387 | -9.49331 | -45.39436 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 515ed77d-fa5b-3235-89cc-11dbc2cd3b03 | -9.69604 | -47.06293 | 2025-08-29 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ba957e26-b356-34bc-a916-625085d7dd82 | -9.48435 | -45.40023 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 424d9224-662f-3c54-88e9-5932c506cc47 | -11.06491 | -44.76339 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 758be495-8460-342e-8a1d-3f8aa94b4f9c | -12.41304 | -46.47789 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd9f8ad4-ea23-3ed4-a26d-6a9b6ac98de2 | -10.65332 | -48.6669 | 2025-08-29 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f7c5028-ee60-3206-9dfe-9182e74f94a4 | -6.38584 | -45.57927 | 2025-08-29 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e19b8da-a9a6-3ac4-9715-9737da3d1823 | -8.1042 | -45.00539 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584570b5-21d0-3436-af47-6a6c1f09b455 | -7.0506 | -44.38167 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4085b809-04bb-328e-be1b-fbf9e501026e | -6.16976 | -47.27728 | 2025-08-29 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 82cbcfbc-81ca-3de2-8575-7d695dfa45ea | -13.18166 | -45.28237 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa526fa2-c638-3a45-9377-3e6e33b31593 | -6.26704 | -43.81613 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f19137f-cbb6-3afd-8125-6f04daba22e3 | -6.35117 | -44.47479 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 481c5d7e-f813-33c1-a97a-f53ecc0e0c3c | -12.88259 | -48.14066 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 075c6b2f-4fb9-351d-bba4-f5be0ee63e02 | -10.08094 | -48.86128 | 2025-08-29 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80b8b89e-cc8b-31cd-a989-da627283e038 | -6.13769 | -44.42201 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3eedb4e-d5f1-3a26-8907-f7ed02b56677 | -13.1933 | -45.29223 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a69bcc1b-26be-3e45-b965-e484ef689eba | -6.28064 | -44.47176 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 712d54d3-fba2-3870-830e-f65560e6bb77 | -12.92515 | -46.33486 | 2025-08-29 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc5c9c6-845f-390a-aa47-885109b2dae0 | -10.60855 | -52.32738 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff390867-5faf-3d6b-9611-5991cb2e4dca | -9.69241 | -47.06239 | 2025-08-29 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d153c45f-d3e3-341b-9b4f-31be51ec4e90 | -11.87846 | -46.40454 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6710e847-e7ca-3166-8461-1aa522de2f7e | -9.16193 | -59.53748 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6662a44a-f243-3bc3-9fd9-c3936061b2cc | -7.72647 | -50.28222 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3b1b8bee-67d6-364c-beb7-12e5e12e1bdc | -8.27942 | -47.20533 | 2025-08-29 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abcc9fc9-ecd3-38fe-9af5-0f284910fc7b | -12.91173 | -48.11528 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a76fc41c-4467-3cb4-96a0-9e49a81bc0f7 | -12.87959 | -48.13619 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1491d160-0f09-35c8-ae97-e04d9f6606de | -7.74187 | -50.27045 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3da3fe46-9eda-346b-9b9b-03b5c54099e2 | -11.8349 | -46.79393 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec795c42-8508-3b0d-90bb-6c827555248d | -8.25175 | -61.45131 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bcfa28c-0628-3e3a-8cc5-a533130cf49b | -8.08511 | -45.02398 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04c9a182-df22-371f-827e-54f831f08d45 | -6.71057 | -49.47253 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2bf529f-9eba-36d8-8773-88355f51fa59 | -8.17763 | -61.37466 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e6f3c275-e2ad-3220-8a43-5163dde1c576 | -7.04753 | -44.37368 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75885530-f551-3995-969c-7c454fbe0b01 | -7.05381 | -44.35923 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b948ce3b-c777-371f-94e0-dd85352a274a | -9.68966 | -48.316 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33e35333-522a-311b-871f-1901ca3d8aaf | -10.3192 | -62.62016 | 2025-08-29 04:40:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3454067e-6943-3936-a01a-af047bc0c5c2 | -11.59338 | -46.37707 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4ba39fa-1f2d-3c48-b2ab-5f8d2d6619df | -8.88302 | -60.74283 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5984e46d-579e-39a3-b80b-e1f9924136b5 | -7.22233 | -45.44241 | 2025-08-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 876b83e6-fbc3-3803-a844-07c0c5cf6855 | -8.70072 | -50.38138 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e68e1050-f851-32aa-84c4-e1eed07b8d06 | -10.02377 | -48.07637 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c2e62d4-e50d-3a9d-8350-a9a1959b78d2 | -7.39847 | -45.93152 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05830172-e6fc-39a1-b573-976dd0183b28 | -9.67769 | -48.32626 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ff9faa5-4e15-322f-b044-aa6080ac1883 | -7.42944 | -42.06146 | 2025-08-29 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README46.md)
