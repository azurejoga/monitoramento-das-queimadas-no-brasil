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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c20dc94-f83e-34af-a391-bdf19b02c1a7 | -16.23241 | -52.65493 | 2026-09-14 05:40:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e241a569-7d7f-3662-9dc2-882bc4f121cc | -16.23299 | -52.64849 | 2026-09-14 05:40:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c005113-e559-3e9a-b2cf-d62f4bb99b15 | -4.81511 | -42.87421 | 2026-09-14 05:53:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 32a8191e-4832-3930-a948-95cd76402d1a | -4.94603 | -37.3656 | 2026-09-14 05:53:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 43.3 |
| c066d98d-fc27-3e49-b1bd-be6c28d639de | -6.33588 | -43.34573 | 2026-09-14 05:53:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| e746967e-348b-38fc-8788-4928dd30b070 | -4.94414 | -37.37792 | 2026-09-14 05:53:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5caf0503-7718-354f-b4c5-25d7fc721f97 | -4.9436 | -37.37088 | 2026-09-14 05:53:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 5841c016-b246-320f-a555-a0746b0d6a53 | -4.80528 | -42.86768 | 2026-09-14 05:53:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 1848311e-f355-39fd-82f6-c27d7ecb93e5 | -4.94557 | -37.3586 | 2026-09-14 05:53:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 14.3 |
| ceddf734-2e82-3945-b1d0-4248da68d043 | -15.5572 | -48.7953 | 2026-09-14 06:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 51c06d11-2079-352d-b7ad-4509d42a8356 | -15.5572 | -48.7953 | 2026-09-14 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e79909a8-3f28-3e37-bd90-7432ba7c2eef | 2.58152 | -60.30453 | 2026-09-14 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 279ec835-1ea0-3b48-941e-e4f1204027c0 | -5.08544 | -56.25376 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 219f6c80-b833-3e41-b818-9b5ed707b075 | -3.16572 | -58.64313 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b321964b-d9a8-32a7-b4b4-9840c579945b | -2.67627 | -57.55484 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6efd4511-cea5-390c-b06b-31a0fadd5215 | -6.02259 | -59.93782 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf41cbc-ba8e-3432-94b8-5627ecb6f1cb | -5.12657 | -55.96486 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e68207b-101a-3d1b-b1bc-bc455253b86d | -5.58973 | -60.18821 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69f13f34-6f13-355e-9e33-5c57c5d4fe93 | -4.12849 | -60.68895 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f7b23c8-b95d-3a41-8769-97231329cd21 | -2.67641 | -57.56585 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b9b9345-f6d3-383a-80f1-6bb1be2d62dd | -5.13584 | -55.95135 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7750ae22-017b-3f8d-8dad-7588209ee4b3 | -5.08233 | -56.25597 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa075ac9-54ae-32d5-8bdb-40d2211c46e9 | -2.67472 | -57.56496 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 024d3ca9-686e-3bc8-b1b4-fa1a2d9a65ba | -3.41368 | -58.20523 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac678373-f3f6-36b2-9a8f-ab34f6f7a6f0 | -2.70321 | -57.54846 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4ed9b0b9-45f4-3106-98f6-306623c53e2d | -3.14766 | -60.63303 | 2026-09-14 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b323926e-f1ed-3ee0-9a49-ef5569a7048a | -6.10841 | -57.67184 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d30f339-f237-3204-b100-519e1524a58d | -3.1434 | -60.62587 | 2026-09-14 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0232aa-15b3-3238-85f6-d0e62c1967b7 | -5.73502 | -60.22215 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d5dd8b-b138-338e-91e7-fa744936f261 | -2.69356 | -57.53732 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e4dd1c7-f65f-3e51-b277-37106487a574 | -3.41297 | -58.20996 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41ffdd26-9ee9-3f0a-9b53-50542d21ebd0 | -2.69991 | -57.53829 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9238051e-36b4-3f83-92a3-df4e92ec6c23 | -6.1086 | -57.86387 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72572266-07b2-3543-a183-ad9aa94f8fd8 | -6.076 | -57.85934 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b91ddd4-614a-3874-a382-603ffc38971a | -5.12866 | -55.95015 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce12e611-3f1a-3947-9645-50775c39f86e | -5.59532 | -60.18896 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e97093d5-2e5d-3738-a1ef-a80bda7a2bd3 | -6.10765 | -57.67741 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 378a3966-2eae-3949-acb8-18f6f6ee761d | -4.1189 | -60.68092 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6964377b-6e6a-3620-9faa-c8dc807938ad | -3.41823 | -58.20871 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b584c4c0-c173-34b3-b2a7-9ed940791baa | -6.02148 | -59.94561 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a2b76de-7f49-3118-b324-2994780cac24 | -3.17102 | -58.64832 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c8d80e4-0fbf-3d66-a0f0-a5958d5914b9 | -4.12369 | -60.68494 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5c8a6703-a508-34b9-9e23-ad9d3d72abda | -3.14292 | -60.62901 | 2026-09-14 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e152903-8fab-377f-ac7b-8df2985d7247 | -6.06875 | -57.86378 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 572428b3-0253-3647-bfc0-52da833126a0 | -4.11841 | -60.68415 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a7f45838-3bf9-379f-bb47-c05904b82407 | -5.12969 | -55.96071 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 89029b5f-9a7c-367a-9a36-4a07530eddc1 | -5.59027 | -60.18452 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3e4fe2-cc3c-37ce-a78b-87593a46def5 | -3.16841 | -58.64043 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8246d88d-9b1c-3390-aa81-364a768d5571 | -3.16778 | -58.64476 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 385cb011-eacb-332a-b48e-f3e4d3fe5c37 | -5.58846 | -60.187 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e9e25cb-fd07-3347-be80-0f3c233cba82 | -6.01524 | -59.94852 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 389cb9f9-867c-37ab-9d27-51a7fa3dc9da | -5.59456 | -60.1841 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fa3543b-c99a-3c0f-86cc-ba658c51192f | -6.01579 | -59.94466 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c3947e6-425c-37ae-ba3c-e3b5b472392b | -2.69286 | -57.53135 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3889782b-493b-3988-b30d-766418583257 | -6.11585 | -57.66662 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 070bb987-246c-390c-aacb-f217e1fdd906 | -2.69431 | -57.53223 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0baa9aa-0f03-3801-9aec-5744dbea0fce | -2.68027 | -57.57102 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a89730b3-2c24-35ec-a0d3-5b0d1add88c2 | -2.69916 | -57.54337 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fc55ded-47e3-37b4-bef8-6ac780efc801 | -3.18142 | -61.11765 | 2026-09-14 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ca0646c-8b3e-35f8-acc0-d3990fd6a39a | -4.12321 | -60.68816 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7cb27c9f-9bf6-35c6-8c71-fca5e36cafbd | -4.12418 | -60.68169 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 444d16cc-ad16-3abe-90e7-8157ddc9d4b4 | -5.13481 | -55.95858 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a48158f-1e52-3ecc-b17d-5078cd75816d | -3.16716 | -58.64904 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c93a836-ffe1-3337-92a8-fde17f3a96bb | -2.68535 | -57.50475 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c9da9fb-d5e3-341d-8394-febddd779aa4 | -2.67156 | -57.5547 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13813994-9228-38c8-aafd-d3ae9b29be72 | -5.72943 | -60.22136 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6e0b7ca-f7d1-3634-a122-1c432e3ad273 | -4.12946 | -60.68248 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35bec6fd-075a-3fa0-a693-07850291cbed | -5.59586 | -60.18528 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c83db4-2990-30da-89c3-c4912f87eb5f | -2.67973 | -57.49866 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f91598a1-a2b1-3af9-8955-15a2541bb224 | -6.02203 | -59.94173 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a116b8d-d271-34c5-9003-eada42b6c9e6 | -2.70478 | -57.53834 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df494c22-7ff3-38a6-96a5-2c85e838dc20 | -5.12361 | -55.95144 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e9066299-12d5-39ac-9417-96c43477322a | -5.59405 | -60.18778 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c271962-19fc-3e72-b4af-e1a404c771a3 | -5.12053 | -55.95565 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef5a6485-0160-3385-b203-07691cd29d8e | -6.07525 | -57.86485 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5b21850-a287-397e-924c-406651e87765 | -3.59672 | -59.06865 | 2026-09-14 06:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dce4751-f64a-3d98-9481-438cac65cacf | -5.07838 | -56.25263 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d989878-aa8f-3b49-b100-43f8993a9e7f | -2.70399 | -57.5434 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 266d64b7-1295-332b-b956-91d0fb79988f | -3.41226 | -58.21465 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a4d3468-7879-3f28-bf20-6d755f6330be | -5.13791 | -55.95426 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5decbdb3-6fae-3d7d-88af-a6132c7ff421 | -2.48797 | -58.0051 | 2026-09-14 06:12:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a2d1fc6-57d9-3eeb-abf4-1908d5b1ecb8 | -3.35607 | -59.62188 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07310938-6a13-3a45-ae4f-ef07bc849f24 | -5.12259 | -55.95897 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dd7a1350-0469-3ffc-9157-3fcb92ba72e9 | -3.16506 | -58.64743 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2e6dd6c-f710-3bf0-b832-e91595735911 | -6.1092 | -57.66605 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8976229-530e-350b-a536-bd8589d94295 | -3.18186 | -61.11473 | 2026-09-14 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef42915e-c260-35ac-8696-19e1ce05c28a | -2.23209 | -60.04248 | 2026-09-14 06:12:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0464010d-1f73-3e46-80da-0aa4d24b5585 | -6.02092 | -59.94953 | 2026-09-14 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3761b759-13d9-30a8-8980-994ca35ed2f7 | -3.60195 | -59.0736 | 2026-09-14 06:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa73a0dd-c426-3c9d-ac32-fbcfc574ff57 | -3.16182 | -58.64385 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b6bd428-752e-3379-8fcd-d3d725e816f5 | -3.15977 | -58.6422 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3aecc40-684e-32b3-93fb-233053be4743 | -2.70551 | -57.54433 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2f72731d-3023-36e0-80de-b570a29751e9 | -4.12752 | -60.68488 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 651876ec-5caa-33fa-b188-65245c414304 | -3.16245 | -58.63951 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50e95ea8-203b-33fe-aff2-e9f7fd8ba1e1 | -2.69843 | -57.53738 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06e15b70-f3f4-3c29-a357-b79f478bf80a | -2.69208 | -57.53644 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99943b8f-10e2-3273-aef3-85e0134c0628 | -2.69764 | -57.54246 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 96e61669-e6f4-30db-9a85-905ff41b6533 | -5.13071 | -55.9532 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e3f4a38-0e52-3ac6-9aea-8c350c28026c | -2.67549 | -57.55989 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5224304-1b1f-369c-a3ff-63dd1fb59c6a | -3.72088 | -58.87074 | 2026-09-14 06:12:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README62.md)
