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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d32981c4-de39-35ab-b371-84e76d022930 | -3.9596 | -43.1038 | 2026-09-14 18:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 55d2fb90-3f97-3b33-afc8-02afa6cfcd7c | -6.3436 | -55.8243 | 2026-09-14 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 966857b0-6ad1-3dfa-a989-0d6d623311a5 | -2.9395 | -50.3994 | 2026-09-14 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 38753798-6baf-3b10-bb90-5024a31a6027 | -1.861 | -54.4315 | 2026-09-14 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5bff1bda-09be-3685-b12f-ca9b2c9ffb9b | -9.1708 | -50.0049 | 2026-09-14 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| dc6c24dc-3c85-3ada-ae99-8be0f2566046 | -6.0925 | -57.6847 | 2026-09-14 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 74b7b848-34fd-37c6-ab24-c2909010dee4 | -3.7462 | -61.7552 | 2026-09-14 18:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 37f08797-ccf9-3ce0-9912-98a4d32871fb | -16.8665 | -41.9063 | 2026-09-14 18:40:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| ab67a9ba-ce47-338c-b02c-b0297f92d2dd | -10.6824 | -54.1884 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 865.8 |
| ed034933-ddc2-3b36-93a9-116cba2e2ccf | -10.6455 | -54.1303 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c8d59d02-7b4e-37a6-9068-57d19a396501 | -3.7645 | -61.7548 | 2026-09-14 18:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 324812a1-5d91-3c6f-8ab1-09f971cfb068 | -5.3635 | -50.1742 | 2026-09-14 18:40:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| a75c8327-8e54-3942-9346-6225be6b3907 | -9.4513 | -50.1282 | 2026-09-14 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4de447ce-e031-3bd9-9ff5-a4680d609d77 | -11.2391 | -43.4413 | 2026-09-14 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 625d66e0-47a9-337d-85e2-f12f63827aa2 | -5.8021 | -53.8061 | 2026-09-14 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| eded69c5-8847-344f-8c61-9ff8b148bfd9 | -10.6452 | -54.1508 | 2026-09-14 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0c96ee20-2ac6-30b0-875b-4a966eb647e0 | -13.5719 | -51.4605 | 2026-09-14 18:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| b90e320a-4083-3c00-812f-52891edfa105 | -1.7133 | -54.9521 | 2026-09-14 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d85a9bad-d5db-3e32-93f0-8bc3041b0980 | -6.2959 | -41.6824 | 2026-09-14 18:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 72d091ff-2c2b-3383-9b1b-457dc1cf46a8 | -3.382 | -61.3279 | 2026-09-14 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| e8e3ed98-8708-38e6-a53a-1ecb87206a8b | -6.0537 | -52.2006 | 2026-09-14 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1ba9b1f7-a397-38bf-b005-69b78cbcf7e9 | -8.2582 | -51.2032 | 2026-09-14 18:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3a2c29a2-8c2e-321d-9ca1-4ade1ce05749 | -3.5336 | -53.9939 | 2026-09-14 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a37ffb7c-2f8f-36d2-b761-6348f2edb466 | -2.9025 | -50.4004 | 2026-09-14 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| b2bf0439-3c4c-3ba3-9d25-c08d1ec0716e | -5.569 | -47.5006 | 2026-09-14 18:40:00 | GOES-19 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 88e964c9-4a72-3c41-9b40-be084d4754ec | -7.2067 | -46.1411 | 2026-09-14 18:40:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b4b7adce-05cc-3b43-bc66-69d5ea9ed9fb | -6.6021 | -58.849 | 2026-09-14 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 84739bca-9824-3fd8-ae57-83c9f8f9cbc8 | -6.8067 | -43.1779 | 2026-09-14 18:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| a0589895-435d-35cb-a6dc-c6f06fb03753 | -11.8362 | -50.0244 | 2026-09-14 18:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 00c02531-2ccf-307c-b424-0823d1f32897 | -9.1742 | -56.9358 | 2026-09-14 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 094aec98-885c-3edc-9dfa-1b0efa553832 | -3.382 | -61.309 | 2026-09-14 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 73351001-0e84-3dc6-a6f0-8ae16f3f6f5b | -9.8649 | -46.0051 | 2026-09-14 18:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |


