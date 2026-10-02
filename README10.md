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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51952e6f-885f-3456-874d-68daf5dfe201 | -3.0192 | -53.8668 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 1bf713bc-b492-3b7a-a60f-7080c55c69fa | -13.3476 | -43.8776 | 2026-10-02 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 5e13324b-4cdb-37b4-b292-a90cd7c9ea2e | -11.1424 | -44.6029 | 2026-10-02 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 3849edf5-5464-3b45-ab4d-23ffd54dc974 | -13.3282 | -43.881 | 2026-10-02 01:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 7ac55a3b-bd05-3c66-a048-5a4ceea9e055 | 1.7853 | -55.6449 | 2026-10-02 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1c76627d-9f5f-34a6-a8b4-5d40ffed3376 | 1.8037 | -55.6249 | 2026-10-02 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 50c54368-bb4a-3969-953e-f35b388d3e64 | -13.3486 | -43.8301 | 2026-10-02 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 00404c58-e75a-35e5-9d86-95a0a5558840 | -2.0394 | -56.8593 | 2026-10-02 01:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 490ed32a-ff83-37b8-96ef-7662b72be0b1 | -2.0576 | -56.8786 | 2026-10-02 01:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1205f59f-7cc2-3927-923f-37d87769ed9a | -3.2766 | -53.8602 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a03483e9-9979-3f23-8828-dd44f1dab847 | -3.1299 | -53.7431 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 204d63ea-7053-3439-a53b-6d5f77120f33 | -13.0378 | -51.2929 | 2026-10-02 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| fbebfe9c-2795-3f5f-bf38-cf2fb21ac5af | -3.0192 | -53.887 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b2a3cef1-daba-3569-837c-6c9bee4664fa | -3.2951 | -53.8395 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 9d5c35de-e795-37e4-802e-f9ff10c800af | -3.1483 | -53.7426 | 2026-10-02 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 1e61fa4f-2d1d-3f0b-9b2b-6d748aae3928 | -7.1827 | -52.6078 | 2026-10-02 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6bb0b038-f386-304e-a69e-5af70856c79a | -11.7738 | -43.5482 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 858da47a-1a81-38ea-a862-652d832b9934 | 1.8037 | -55.6051 | 2026-10-02 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fb1e3655-114a-3829-993c-64bc00900654 | -7.0478 | -55.6302 | 2026-10-02 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5f6eaa98-0700-3092-bdc6-2ea7ca0ae68e | -11.7926 | -43.5689 | 2026-10-02 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| b936ffd7-ca1f-3b8b-bbe6-5a5457b848c9 | -7.0464 | -55.648998 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 708ed368-14af-3f1a-b895-9feaa03cc28f | -8.3084 | -54.729301 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1000243-7575-3dd4-9b5d-df37e014b48e | 1.7985 | -55.613499 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988da6ea-936f-39bb-8254-30a680f63d0a | -6.5495 | -56.2658 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efaae04d-a779-36a4-87fe-563d721c81b2 | -7.6412 | -55.0555 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c7a1c8-b216-3156-abe4-ed337cb9d82a | -7.4006 | -55.218899 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5291dea8-4a12-33ce-ae6d-fe0e4076f5af | -8.2018 | -54.714901 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 812c48b2-89f0-38be-9320-22c7f3692d62 | -7.3519 | -55.5863 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc42965b-9373-3ba5-b4a7-ae0eb875f93f | -3.0412 | -53.873501 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 058c8ad0-f7ae-3529-99f9-63a299df9054 | -13.0621 | -51.305099 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ad4f774-f438-3a25-9d97-a9d5b5e09c66 | -7.2783 | -55.580799 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa1fbbd-bd35-3208-a8cc-4aa430605523 | -11.3355 | -51.3092 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a81469b8-01d6-36f7-bfc9-49e90b4bed8e | -7.4899 | -54.981899 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf27153d-f723-3a22-aba2-11af881a9a06 | -8.5465 | -54.555599 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f71239e6-93b4-3c20-9036-1409c2580275 | -8.4178 | -54.7117 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8868756c-a750-38f3-a11b-7e437f3e32c0 | -4.4497 | -54.9128 | 2026-10-02 01:12:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8122b9-7d89-377f-a72a-db9ae36b6711 | -7.0562 | -55.646801 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f26d92-b9d4-3dcf-a78e-2284b76fd2b6 | -8.23 | -55.278599 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69becfcb-a391-350e-b2db-e32ddde87fbc | -4.0661 | -51.115101 | 2026-10-02 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 090319a2-656f-377b-a2d7-86cce3c5060d | -8.5501 | -54.570702 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2598fa9-7442-33dd-8567-e7315b10d065 | -6.6677 | -55.085899 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5158670f-dcd5-3860-a2c0-ca8e21213429 | -3.1744 | -54.090401 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b361d0a9-3d45-31aa-96ba-6866b68c601b | -7.5766 | -55.132198 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd1c00ca-7a9d-3c3d-8ddc-e782c73d4e20 | -3.0314 | -53.875801 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac861a89-2050-3697-bb86-7173c49a1db1 | -5.7589 | -45.1661 | 2026-10-02 01:12:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb9bb23c-7747-3958-aeb8-582fff045a1f | -5.9989 | -53.558399 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f86547-8406-394c-bdfa-0e5b7573e35e | -8.2577 | -54.733299 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79fd325a-835d-32f5-879e-3cc70b9a5239 | -8.2093 | -55.100899 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f34413f-fbf2-32d1-844b-8e0a8099d74e | -7.8664 | -54.737701 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb630d06-8b1b-38ce-b5a6-df8e1e1edac3 | -7.4639 | -55.003502 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cc8b23a-3a7f-3edc-b27c-ba4c65c4f2c0 | -3.1368 | -53.754299 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f9f40a-4be1-39e5-a10f-5e81ecff7686 | -13.3257 | -43.843498 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5c5daed-611f-39ba-82c4-5fa361171f17 | -4.2963 | -50.788799 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2397d6b5-3689-3fa3-8e1e-5844459be760 | -12.7887 | -51.414501 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4c5f14-057f-308f-9cd7-bb7c60fca4ae | -8.2647 | -54.763 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c9d007e-eb2b-3021-ac2e-0b12a7a25e4b | -13.3433 | -43.869499 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14c04260-b340-3e68-b3fe-de3045a20f53 | -9.579 | -54.643398 | 2026-10-02 01:12:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4527ab3-2f81-3434-bcd3-7c34c336ee81 | -7.7184 | -54.811501 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243254f5-7c9d-3771-aafa-e1fd9c964b8b | -3.1444 | -53.742699 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac99f404-0b00-3663-a6c3-451d9c5371f8 | -4.4577 | -54.902699 | 2026-10-02 01:12:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7424a029-ce4b-32fa-952b-7a305332489c | -7.4737 | -55.001202 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef27a1d-69a1-35d3-9a64-416894eec607 | -7.414 | -55.587101 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff9359a7-2649-3852-bf28-b653dea0a7f9 | -12.9827 | -51.1497 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df6ccccd-70df-33ad-b255-e9fa6214beac | -11.7559 | -43.573399 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9844f46a-28e2-34e2-a488-843dd7ef0b1a | -8.2633 | -55.6898 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c41ebd6-b02d-32f7-8e91-91cb2412e01f | -8.1593 | -54.8423 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff91ef42-3f57-3b95-a927-ba950f1e8a9b | -0.3727 | -51.742401 | 2026-10-02 01:12:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fe931893-ff2d-312c-87f8-670d6f852740 | -3.0237 | -53.887199 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5072955c-4321-3b29-ab35-94c863894732 | -7.73 | -54.8167 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f6bb674-ce2a-37e1-81ac-153a8e1ee068 | -7.4058 | -55.596401 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9074c9-c2ba-3329-ae40-3affcdb0aeb0 | -7.5543 | -55.0369 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45e90769-4215-3989-9c16-aee4c0370a79 | -6.0818 | -57.8241 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 857caade-cb73-33f1-b4aa-3a48be4de723 | -5.7392 | -55.752499 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c29c0c11-2be5-366f-a75e-c5ddfdbe95f9 | -7.6395 | -55.048199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe7301f4-e8f0-3e19-bebb-38e59df6f2ec | -8.5385 | -54.565399 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b422730-fa6a-3608-ae8e-eede1fb00547 | -8.237 | -54.777302 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 254950e8-58f2-3327-8599-8369a1ae948a | -4.2634 | -50.737801 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 881694cf-6162-3be4-a26b-57794ceb43a8 | -3.0161 | -53.898602 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa43abf4-e3df-3bb1-88ae-b1267da63d33 | -7.7345 | -54.792099 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb4a0f84-ac96-3fb6-a88b-a5fd527228dc | -5.8752 | -50.172001 | 2026-10-02 01:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294ae64e-a47f-3c98-8a0c-5152d9c27871 | -8.1011 | -55.346199 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d75a47-f6bf-36f4-ab72-7a418151d28f | -12.8388 | -51.4925 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f43269ff-9518-3aff-8eaa-eec2f60f4c1d | -4.2866 | -50.7911 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0736e4-77e8-32a5-8c7f-be0269f1de89 | -6.7495 | -55.082699 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50dbdd8c-052a-3b08-8554-b2e3f5965d57 | -8.0781 | -54.8922 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5422aa1a-738a-32f7-a7d4-28cfc1981fbc | -8.1558 | -54.827499 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66f354b9-9421-3fc1-b983-8ec5de341ba8 | -6.8625 | -57.7216 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7552d36-247d-336f-8828-1c76f4e3fe71 | -2.0486 | -56.879601 | 2026-10-02 01:12:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc8cec6-ec3a-3e4d-b514-9896fd86b93c | -6.4055 | -55.200901 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5baef617-f9ef-33a3-86bf-faebfdca45e5 | -12.8365 | -51.483101 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15ba0ff5-11a7-3001-857a-64e45db15380 | -3.2845 | -53.856201 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce1de3e-f7ef-342b-bddb-d552da77bbc8 | -11.2543 | -50.978298 | 2026-10-02 01:12:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14e9b7b9-90fe-3761-80ca-1f4e48d592cf | -7.5705 | -55.017601 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e644b916-128b-3071-9846-8cef3cf3e3c9 | -7.7608 | -49.2164 | 2026-10-02 01:12:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 29d2297a-81a0-3b58-a5b7-1db6556a2f2f | -5.7375 | -55.7453 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175f2ce3-edae-31a7-80b0-f32601c9b8c5 | -7.4657 | -55.010799 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d63ee4-8418-33f1-91d2-7f10b3ad8c2e | -11.7838 | -43.599998 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3d831ce-0b84-3d36-b80f-c4f83947ea1a | -9.7918 | -53.834099 | 2026-10-02 01:12:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d390008b-3af9-3015-a0c7-7ca5a14d85d5 | -11.15 | -44.588799 | 2026-10-02 01:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d26ef31-e290-3aa8-99c7-c1fc61266b47 | -7.6297 | -55.0504 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
