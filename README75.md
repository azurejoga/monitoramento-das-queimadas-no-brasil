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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff3f3e37-ab60-3777-8f90-3a074db107d0 | -3.57319 | -49.43674 | 2025-10-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1482372f-467c-3e55-9849-0bfe43dedc41 | -3.08328 | -51.28362 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e715ab2-9913-3bc6-a418-01f54cbd1c18 | -4.88413 | -45.74607 | 2025-10-28 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 918520d1-8cee-32f3-ba9f-d4d4e6f65582 | -3.23832 | -50.65393 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a311e24-05b9-3c80-b7f5-cdda1519d603 | -2.89363 | -52.58709 | 2025-10-28 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc5e931a-183f-3975-8a8e-969e10b542b9 | -6.48564 | -42.23625 | 2025-10-28 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b9fd69b3-3b76-3311-b48e-a8a8bc81c2b9 | 1.05621 | -50.9734 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4277256-1eb7-352d-a357-e695fb911b69 | -10.9347 | -48.03202 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 665beb45-5164-32ee-942d-9a5df6f166d2 | -7.59634 | -55.49441 | 2025-10-28 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e56cca5f-cdaf-32ce-a57b-decbeb46cdeb | -13.42211 | -47.38044 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f8af5f7-cd00-382c-941a-e9c7166c8bed | -7.96772 | -46.29926 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3e832dd-0c35-3c63-ac89-6c6e2b0058c7 | -7.61259 | -46.47662 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 426141ff-71ff-38f8-b4d3-31d5a444842f | -13.67124 | -46.51908 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88b59d2b-0edf-308a-bdd1-a6a7592dedbe | -9.95816 | -47.08646 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18d70fdd-5081-3c3b-9b50-d60f7e11fd49 | -7.45211 | -47.0292 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e51b9442-149f-3a77-a3b4-7fe94c048733 | -8.64522 | -45.28905 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 106f2630-fb6a-3e84-90e2-ebeede9a42ff | -7.85939 | -46.39583 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a69d1955-eb9b-3074-81f6-c303c7015797 | -10.92618 | -50.27458 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5395f970-1568-3bc4-8562-fd6bcdcc3f46 | -10.92982 | -47.61247 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7600190-373d-3b07-8140-a6d6bedcda0f | -10.28889 | -47.2352 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ac5a9a2-bbd1-3c9a-aea6-30b3eaea26e1 | -10.97144 | -47.82691 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18ce8c02-090a-39d7-9627-6722189e89c7 | -8.13845 | -47.75347 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4568b174-f6a0-3816-ab48-8b99194e1299 | -7.97817 | -46.7321 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e5d22c4-96c4-377b-ba6d-517a2b6bbcfc | -9.97053 | -47.17725 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19d2a960-efa4-34c4-a899-ea72ba14b755 | -7.94361 | -45.50381 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6128c5ff-9e7d-32fd-9b21-f81abb564c95 | -9.57159 | -47.9027 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14be311e-e9d3-31d3-9800-853cc830c4de | -9.46386 | -46.87174 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f10fccfa-74dd-310e-b9d7-647ef0cb0242 | -13.53661 | -47.17159 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d07a3686-8263-3488-9a57-a00e22f8e53d | -7.97729 | -46.73878 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55175036-0279-3570-a8a3-920ea445f558 | -7.89405 | -45.69248 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0351a856-7d79-325f-9478-e141ca9ed9b1 | -8.10812 | -45.95987 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ff3452-2241-3289-8a20-18ec3948081d | -7.35724 | -47.64038 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a55d5b48-85c4-336a-9c3d-ea3ef25543b7 | -9.95722 | -47.09355 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44139a8a-03e9-3545-8ad1-a98e30a81f83 | -10.31602 | -48.78962 | 2025-10-28 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 739ef922-29a6-3130-94d1-ea87ab60882e | -8.1512 | -47.00674 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ef6693c-8572-391c-9ff6-12c95a209818 | -12.61709 | -44.2576 | 2025-10-28 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15fb736d-4925-3f68-af42-89a0ed86405a | -11.03763 | -47.85529 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bef472c0-d9c4-3ccd-a0e1-18053718a854 | -10.92118 | -50.27834 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bee63bef-eadf-3ce6-ab5c-8b518581ea20 | -7.26676 | -45.00957 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| feb5cd2b-de76-3811-aaed-cd30dfc972bd | -10.76122 | -44.75103 | 2025-10-28 05:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ad64e4a-e1c8-323b-aad1-02617007778a | -11.04261 | -47.85791 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bde7fa63-2097-318e-b39d-a5dd050a7b82 | -7.4095 | -47.77589 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4edd8a9-6e2f-3d87-8c0f-3dd117edb119 | -10.28306 | -47.23798 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 071c6980-194d-3259-9541-43484956bd11 | -7.62179 | -46.69287 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 953a4942-65c8-38d7-8793-06b06e795be4 | -9.5428 | -46.9563 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c86312f3-af26-3028-963e-b4d8b4348640 | -12.53307 | -47.54638 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0466022-e718-3d7d-9b02-a859c2edb5fc | -7.61354 | -46.46951 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a5e1ee0-3091-3913-ac1b-0a5eb6a31894 | -7.12931 | -55.11385 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e820d657-9f0d-3c23-ac8d-2d82d1b985af | -7.29784 | -45.07025 | 2025-10-28 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 10dbd853-4d28-3eff-8f85-d2dfd193ee5b | -11.03234 | -47.85521 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fba08b5d-98ac-38bb-9da3-67f21f1d05be | -10.56095 | -47.89919 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8988ccb5-d27c-3751-93e6-c9ddfefd3599 | -10.55994 | -49.82823 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| feef7584-6a55-3518-b6c7-1ff7e5826bd6 | -8.87351 | -50.33326 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebe70c24-21c2-38d2-90d5-c148f2ff089a | -7.47231 | -47.15187 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8c9e038-c112-3ab1-89f4-308f6648a87a | -7.31438 | -44.10687 | 2025-10-28 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0abf132b-17e5-30b7-9f15-fc7adedb2fc8 | -7.99345 | -46.19183 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fbdd614-9d5b-3b2f-837b-03cfd87061fd | -12.23797 | -46.52904 | 2025-10-28 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 202f10fa-f893-3ce8-9b95-aba5db72d195 | -7.00163 | -46.9977 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5687d3ff-afcb-3111-b1cb-522a1a3d0a35 | -7.9827 | -46.73938 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3da723d-a3e6-3df7-8e6b-18cad7f0d020 | -6.74108 | -48.17439 | 2025-10-28 05:04:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74952bb3-8a1b-3ef3-bf6b-2dc8674cc170 | -7.46104 | -47.15658 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c51268f5-dc57-34f0-863a-4f685039b544 | -6.60476 | -44.64656 | 2025-10-28 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf752bfe-bb84-3535-a989-9af0e7e64771 | -10.99047 | -50.36326 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe50400c-dcb7-350c-97a7-d4a0a2e3506b | -13.39476 | -48.51068 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7259e21-81bc-3ba5-9320-d8323cc223f1 | -7.87036 | -46.39762 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f86c25e4-76d9-3d91-8dc3-3d685ed48548 | -9.95531 | -47.08083 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3730eca5-a76d-361d-a44b-b046d615e94a | -7.35652 | -47.64556 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 245cd4e6-7dd5-36fb-a0dd-b189fa7216ec | -11.33482 | -55.06118 | 2025-10-28 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d6fd486-8691-35d5-aba9-43c4cb51f6a3 | -10.55996 | -49.81712 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f75715-3c97-371a-869f-8b91efb3c309 | -10.92306 | -50.26658 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b0ba63d-83e3-3169-af3b-c3d3ef36d91c | -10.92734 | -50.26583 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f40b7c8c-72ce-30bc-8688-75ff78311352 | -8.08432 | -45.96489 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c4f510d-3f93-3f83-8b58-3a85666a60fb | -9.95982 | -47.11517 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c13ca6e8-792b-3963-b116-8ec2b1116426 | -7.89292 | -45.70071 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9645c61e-2a8e-3828-ac28-9169841e4c9f | -10.68928 | -48.01625 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a4e5927-260a-3a5e-9ab9-0ea1571c9db1 | -13.36716 | -47.41572 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8148c936-a3e4-3789-8606-32823d3fccbf | -7.80766 | -46.49012 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be31c519-94b8-31cd-b374-7acfc5235011 | -9.91548 | -47.68699 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d923d61-c70e-3a0a-a31e-5d0f8b0e4422 | -8.63917 | -45.2888 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| da7dc3e2-e0b6-3dee-9964-56e07d1deb73 | -9.01791 | -43.97739 | 2025-10-28 05:04:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8a6e75-e162-3286-b9fc-866b226a9788 | -4.96591 | -56.26978 | 2025-10-28 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d45dc82d-ebdd-359e-96ff-eac3c4bd6e69 | -7.96738 | -46.75081 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f63bf31-d2fb-3164-8d0b-151085e67f36 | -10.56152 | -49.78122 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13320244-2270-3895-97ed-82d85e5f4736 | -12.53352 | -47.54278 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c9f7475-75fe-3b37-a369-3ea2e8ecf1ed | -9.21969 | -48.60586 | 2025-10-28 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c776f35-1e3f-3c3e-ad72-b5b5a0f05073 | -11.92595 | -47.66023 | 2025-10-28 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 226351f8-8780-3e48-b76d-2c689b0b6984 | -7.35615 | -47.64819 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76fe5aa9-7f30-34e9-a896-23b6b1d3faa2 | -7.06826 | -47.36889 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86786eef-a2b9-3deb-ada3-bc51019083d2 | -10.29649 | -47.21859 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f2bf4cb-c8e6-3e21-8311-839e34da72d2 | -7.97774 | -46.73543 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45975790-e995-3c64-acf2-fa6ad3e60744 | -9.9701 | -47.18063 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381a96c4-5197-3315-b728-5757e03b1a6d | -9.53677 | -46.97303 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7f8abdb-ce50-3d8a-8d33-c62735a61adc | -7.95384 | -45.51317 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 709af3a4-9758-3789-91bd-92d36c7c8345 | -7.81609 | -46.42653 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c10a1ff5-8d18-34a3-a816-37cf2c9cceef | -7.97962 | -46.7417 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36731e42-ebc1-339b-8537-55daa16c0064 | -7.97008 | -46.75192 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 685c2fe7-4c05-383d-9d1c-affb18a9ba49 | -7.13128 | -47.06626 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6106b21a-5eb7-380a-9f25-3a8f608d9dd3 | -7.81137 | -46.46212 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8a4543b-ffb6-36a9-8701-ac382a8e3b33 | -10.92625 | -50.27592 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae8e66b9-f1ba-36b5-95db-1f75ac03cc27 | -8.15101 | -47.00061 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README76.md)
