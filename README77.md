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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1aeba988-0551-305f-bfd4-6315954c4543 | -5.14081 | -37.34325 | 2026-10-04 15:18:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ac5c30c8-9c47-3bf8-91d5-29905c50e9eb | -5.14138 | -37.34718 | 2026-10-04 15:18:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6a3066ee-4b6e-380b-a543-f17278ef1f1e | -3.93514 | -40.73257 | 2026-10-04 15:18:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 153d0d4f-5f6f-39c2-9152-034c8f12d94e | -5.13785 | -37.3471 | 2026-10-04 15:18:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 63059c57-8d76-3aa9-b253-441fc526a814 | -5.13881 | -37.70211 | 2026-10-04 15:18:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 46d5a983-a0d6-3c34-be77-5f8d3384288d | -3.71087 | -40.34929 | 2026-10-04 15:18:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 6bb285b0-8f02-32c1-a10c-6eca74f69168 | -5.21427 | -36.75402 | 2026-10-04 15:18:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| cbc3cb56-e2f1-3cd8-b9e9-12429995134c | -12.1969 | -57.0903 | 2026-10-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e2506dae-9fdf-3aea-8650-acc4b693470d | 3.434 | -51.3015 | 2026-10-04 15:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 3ce28707-471f-391c-8e6f-5c95cd0137a2 | -2.2113 | -53.7029 | 2026-10-04 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 672d531d-ee26-3af8-ad52-0d0bad7be803 | 3.9157 | -60.0461 | 2026-10-04 15:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| be1691f5-67ab-34e2-82c3-63568cdf24f7 | -9.4432 | -67.1751 | 2026-10-04 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7368d3b5-bc9e-362a-9270-9c765f975118 | -12.1964 | -57.1303 | 2026-10-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 03e58d0d-ede0-3147-a214-b4d4fe3531ad | -0.84 | -48.618 | 2026-10-04 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3fababdf-099f-3617-9cb5-c9a070a4c8a5 | 2.1879 | -55.8758 | 2026-10-04 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 11744f70-4f74-3169-82f0-e57b0f275d30 | -1.1991 | -55.6909 | 2026-10-04 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| bfd2e3ed-6c51-3348-8260-1f803439dd44 | -2.7713 | -57.0229 | 2026-10-04 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ba6141f9-f30d-31ab-8d90-87fda3eb4b3d | -2.8899 | -54.0711 | 2026-10-04 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5def5b97-5c0c-3aa2-b1ed-3d352ae26090 | -1.0911 | -54.1202 | 2026-10-04 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 552eb4ad-09c4-3a84-aff1-de85a910c209 | 1.7583 | -50.8232 | 2026-10-04 15:20:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7f768829-d7dc-31da-ac8b-7d47e50da70a | 4.2249 | -60.6671 | 2026-10-04 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 1ba2d7cb-e4bd-3de0-91b1-1bbd453ad747 | -1.4488 | -48.9099 | 2026-10-04 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f6693429-6010-390d-9df5-e76c06bc45b6 | -2.7897 | -57.0031 | 2026-10-04 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3b875402-9ec4-3573-b221-ea245e9b35e1 | -1.0911 | -54.1001 | 2026-10-04 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6899233d-bdd9-3b31-a762-72dcec8320fe | -1.4662 | -49.4413 | 2026-10-04 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5bbf9bcf-d297-360e-851b-edf19f1e41eb | -12.1777 | -57.1119 | 2026-10-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c19520e1-5939-35e9-8d45-30ede07d24b2 | -2.7714 | -57.0034 | 2026-10-04 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 3d67792c-89a8-3682-87fb-facb87e73034 | -12.1779 | -57.0919 | 2026-10-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bfa2b1be-20fd-3b11-ad67-6aba09ac442a | -12.1967 | -57.1103 | 2026-10-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 288.5 |
| a8a8040e-f545-387c-a6cc-1049175441ae | -1.4672 | -48.9097 | 2026-10-04 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f1fd7688-73bd-3353-b4fa-a2699cdffdf5 | -2.2297 | -53.7026 | 2026-10-04 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| a73bc528-faf4-339d-b58b-a785483e94eb | -1.5031 | -49.462 | 2026-10-04 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 292bea5b-645f-3a41-8b6c-39e57c9d7148 | -1.1351 | -48.8501 | 2026-10-04 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ad4e5026-08e7-3a7e-a306-b05c7215434a | 2.2794 | -55.9137 | 2026-10-04 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 29823ca1-b03b-391f-b6a1-25c266e0e1a3 | 1.7487 | -55.6454 | 2026-10-04 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c86d814e-8fd8-3f98-b532-41b39a3b5042 | -12.2154 | -57.1287 | 2026-10-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| d33163b8-9445-3f16-8407-e3e97d13521e | -2.1127 | -49.2384 | 2026-10-04 15:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ef647df9-29a6-3814-a8d1-877d5149c924 | -9.1334 | -65.9 | 2026-10-04 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4923df66-e624-3635-af41-74e7b4b88876 | -10.8377 | -57.1979 | 2026-10-04 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 687b4ebc-bf2d-38af-852f-294ed1ef114f | -1.4846 | -49.4623 | 2026-10-04 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fb630fe7-38bf-3534-8413-27a54176c4c5 | 3.4155 | -51.3021 | 2026-10-04 15:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 5b18e92f-1fb1-35d3-9f89-b413758732ca | -1.0911 | -54.1202 | 2026-10-04 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f60ccb66-962f-3af1-9862-c3a20024d37c | 3.434 | -51.3015 | 2026-10-04 15:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6065a30a-7063-366c-b9b4-57296ff5a22e | -2.4806 | -56.0875 | 2026-10-04 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 83c8e215-fb18-3221-a303-8ca44b7ecc48 | -12.2154 | -57.1287 | 2026-10-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 31a32f46-8682-3895-a253-dbfe6c3d0744 | -1.1991 | -55.6909 | 2026-10-04 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 32b5f715-8ba0-3c08-a0aa-4cb1d0d04e0c | -9.3929 | -65.9105 | 2026-10-04 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c69b134a-a50e-387b-97d5-2b13f0966e1a | -12.1779 | -57.0919 | 2026-10-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| fba1d8cc-c837-3ce9-9957-5902e1ed3fc4 | -1.1094 | -54.12 | 2026-10-04 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 23bd4eed-b5f4-390d-ad03-61717f4743d7 | -12.1967 | -57.1103 | 2026-10-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 4ac9b709-27f4-3df0-b62e-74b951d503fd | -1.4672 | -48.9097 | 2026-10-04 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ff17dde2-eb90-30bc-9159-bf1adbbde82e | 3.9157 | -60.0461 | 2026-10-04 15:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f50ceeb2-f5c0-3bc4-bae4-960c2d1a8b3e | -12.1777 | -57.1119 | 2026-10-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 689af1ff-335d-365e-965d-00a9f1634df5 | -12.1964 | -57.1303 | 2026-10-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 5fd760ea-d78a-38ab-b236-ed9362c5a78b | -12.1969 | -57.0903 | 2026-10-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5d6ff6b6-9a70-3b22-a332-1523a7a753f9 | -10.8375 | -57.2178 | 2026-10-04 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d88f7a3b-272c-3648-ac62-fc46eedcc693 | -1.0911 | -54.1001 | 2026-10-04 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6879e51a-8714-325f-bc4f-0b38c5fc58da | 1.7583 | -50.8232 | 2026-10-04 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b906a7cc-7370-34ed-8cdb-7c43bbe7176b | -0.4687 | -52.0354 | 2026-10-04 15:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 18c394df-ca14-33d1-b71d-8300b10a1c16 | -13.5197 | -61.1319 | 2026-10-04 15:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 93c18969-5e83-3263-9fd3-7fd5479c50fe | -1.1095 | -54.1 | 2026-10-04 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 0a7dbd0b-5fa4-3ecb-8846-fc11687f047a | -1.8693 | -50.6127 | 2026-10-04 15:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 046e54c3-1ad3-3e17-9d52-192d406de1ab | -8.3526 | -62.8302 | 2026-10-04 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e40b7e2c-f31c-38ef-9f9d-1c963eedeaa7 | -0.3584 | -52.0153 | 2026-10-04 15:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fefab6f8-fd33-3da6-af98-502d9822d04c | -1.2271 | -49.0197 | 2026-10-04 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4143bd63-9729-3790-9173-726e460b9016 | -0.34 | -52.0154 | 2026-10-04 15:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8bb5a79c-5958-340e-a105-1f910bcdeccc | -1.4672 | -48.9097 | 2026-10-04 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 730f67de-4843-354c-ae1e-5e1de367f120 | 1.822 | -55.6247 | 2026-10-04 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5348b71c-d0bb-3650-9989-b6ccd4a3d3c4 | -0.3584 | -52.0359 | 2026-10-04 15:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4b707142-ab41-348e-8669-46b7599c1352 | 1.7487 | -55.6454 | 2026-10-04 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 79750363-f486-3d69-803d-3b22c31d4818 | -8.9195 | -64.1473 | 2026-10-04 15:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3eeb92bf-0ae5-379c-b581-6f1370dc19e8 | -1.8693 | -50.6127 | 2026-10-04 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 56209742-ce83-3646-90f8-e7716ef7b75a | 1.9424 | -50.8616 | 2026-10-04 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7d659823-5de6-3209-802e-80678a678227 | -8.3526 | -62.8302 | 2026-10-04 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b85f4b0a-4f59-3a42-8ed4-6d338a5f8466 | -0.34 | -52.0359 | 2026-10-04 15:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3fa16e5e-28ab-3851-aa10-f213019dfccf | -9.1257 | -67.8322 | 2026-10-04 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 62836cce-2cac-3310-8e03-3f3dff3955c8 | -12.1779 | -57.0919 | 2026-10-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 3cde9d19-ad86-386a-94ac-adc7c0010dc4 | -8.3341 | -62.8309 | 2026-10-04 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| dd8e7e94-0dc9-3643-aa55-7f41c8e1a27e | 1.9793 | -50.8609 | 2026-10-04 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7b8ccc3c-04ba-3bca-b1f6-da11c7b50eee | 2.8909 | -60.465 | 2026-10-04 15:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 0169f840-18eb-3c8d-b09d-4d2a886c5f7c | -1.4672 | -48.9097 | 2026-10-04 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| db0778a3-cc69-380c-a0d4-8495bf10c49d | -0.3584 | -51.9948 | 2026-10-04 15:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 43.7 |
| d1e1ee13-c118-3e30-a0d3-5a27502eab10 | 1.7487 | -55.6256 | 2026-10-04 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9246a617-3b1d-3516-b75f-32b5ff8651bf | -8.3526 | -62.8302 | 2026-10-04 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d935b122-ba2b-3faf-8a84-eaeb0527873a | 1.9239 | -50.9035 | 2026-10-04 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ac208e0a-7a44-3029-9bb5-219a79befd87 | -0.3584 | -52.0153 | 2026-10-04 15:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 086d16f6-42e9-36b4-9f3d-b346fa2726d1 | -1.4857 | -48.9094 | 2026-10-04 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a108e8de-f4ac-3100-bc43-81bf2362bf51 | -0.3584 | -52.0359 | 2026-10-04 15:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c38a90d3-e4e9-345b-a0ba-2c1f5ae58768 | -1.4662 | -49.4625 | 2026-10-04 15:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| eb4d86d4-d1ed-3097-9246-25c29a2bc464 | -8.9195 | -64.1473 | 2026-10-04 15:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 193a6f18-694f-3d09-a69b-30f459fb8113 | -1.8693 | -50.6127 | 2026-10-04 15:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d12756fa-25e6-3c62-949a-9a549c6bfb1a | 1.9424 | -50.8824 | 2026-10-04 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b4fa0645-962e-3d96-a02f-576ac4898240 | -8.334 | -62.8498 | 2026-10-04 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| fd700a55-6e0c-32bb-8a9b-22ef06ce30b8 | -8.3341 | -62.8309 | 2026-10-04 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| aaf5055f-8f06-3135-9049-8b1bb3e56844 | -1.8693 | -50.6127 | 2026-10-04 16:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 55b17860-eafa-3e7d-a55c-38bdaddccbcd | -11.8814 | -64.9323 | 2026-10-04 16:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fc3a36d8-6f24-313e-a080-ce0c243b7747 | -1.4857 | -48.9094 | 2026-10-04 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 67a98fea-41c2-3416-b5da-999885d74bf1 | -8.3526 | -62.8302 | 2026-10-04 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e96e0683-f9f4-3668-a061-9e036bbe80b6 | -1.4672 | -48.9097 | 2026-10-04 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 374fb2fb-35fc-38e2-a7c1-f1c41e4389ac | 1.9424 | -50.8824 | 2026-10-04 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |


[Clique aqui para ver as próximas entradas](README78.md)
