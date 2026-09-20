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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e9fdde8-ecc4-3ae6-964c-fe89ac2281ca | -5.66983 | -43.40477 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3a6d667-e8ff-35be-81eb-bc43cd39c837 | -4.22356 | -47.54523 | 2026-09-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9926adfb-6434-3352-aa9f-8c37d96da175 | -5.58538 | -45.55842 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6c61b6f-254f-3b6b-a30f-a3283a0f9965 | -3.70823 | -39.4364 | 2026-09-20 04:38:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1cfe4c00-ff25-3442-85c4-4c8259d2a5f6 | -2.45286 | -49.2095 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eacb990c-d242-31b9-803e-3d222e3f93de | -5.34754 | -44.8295 | 2026-09-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a7e489a-dc5e-388d-8cc4-82be1d3ea566 | -3.69094 | -60.60381 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7f7a177-c423-3e57-a5c7-62ea08f736e4 | -6.30314 | -47.6051 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d043327d-26ac-309f-92dc-12e7d0bedf88 | -1.21689 | -55.72408 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc5c20b2-88fe-37f6-b2a2-f561df7409dc | -3.85733 | -58.89769 | 2026-09-20 04:38:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60f5efc4-7144-3f6a-896f-ad02f1c2e7fe | -3.38487 | -50.44436 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ddcd085-c244-3c59-b675-53d3a20b1ed8 | -5.76851 | -47.28936 | 2026-09-20 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9a4230e-26a4-3ddc-bd67-7e1dacd7d5c6 | -3.04424 | -46.9249 | 2026-09-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c4bed4b-2dca-3241-bc34-ef54b5b0995f | -6.28933 | -47.60651 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1991d186-9b86-30eb-8d6a-0258eb54a71b | -6.59558 | -45.88364 | 2026-09-20 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb33ef83-a751-3929-a5cf-94bf21a9614c | -3.52878 | -49.82109 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b398c495-5ae7-3e36-a89f-889920fe0f73 | -6.91598 | -42.91373 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29dac5e6-c3fa-3101-87b2-ef537cf545a5 | -5.75743 | -43.69556 | 2026-09-20 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cf1f248-d8ad-32ed-90ca-d8a35fe057c4 | -6.31588 | -47.63199 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ed7363a9-712b-35c8-82bc-d4241357dbcd | -4.48333 | -55.49114 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 693086e2-1408-32c1-84bb-009da0c83c20 | -1.22211 | -55.72503 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be759ca8-6aa7-36ee-b0af-17578fe7485d | -6.98886 | -43.37389 | 2026-09-20 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a31f1e52-36cc-34c9-b1eb-7a3cabbeb259 | -3.23198 | -51.35107 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bc32001-5895-3ab1-82f2-fbd3d2c46af6 | -5.31565 | -45.34488 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7fbd336-5620-37db-8726-655155c09ad9 | -3.1289 | -52.71696 | 2026-09-20 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95b513ee-7b7b-3639-be2a-e1e36c7efa9e | -6.00157 | -45.25565 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d71457ef-fc95-36e0-8fe1-964441e900da | -5.35112 | -44.83005 | 2026-09-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a45bc1c-30e0-3dd0-88ce-0bd650305b90 | -4.42477 | -55.50995 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b5e863f-d121-3ca6-8640-4a0a8b761441 | -4.51625 | -55.47443 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c6a52e0-fc68-398e-aebb-5ed721bb1d4d | -3.37835 | -50.43901 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a74c7e8-5fce-3f35-8495-fae8a82e10ed | -5.22086 | -47.57584 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c485e7ac-3361-3d8f-a48a-4ee1d666d37d | -2.88079 | -57.7985 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81b7b88a-35b4-3465-8a10-a7cd60d89b6c | -3.48103 | -49.51001 | 2026-09-20 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84a6e0e2-8a61-3fb5-b7a6-65dfd2d1a2a1 | -4.77487 | -48.0532 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a058f9da-d839-3f12-932d-d6fd008c6c35 | -6.20346 | -45.35419 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ed1d0ad-3a10-37cf-8b05-2e48f1dafe2d | -6.6865 | -43.62769 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47388a21-859e-3d96-9464-6f4e5cfa076d | 1.22342 | -50.98619 | 2026-09-20 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cb4c5fa-a423-32b0-85b2-17d94df4afd5 | -5.22526 | -47.56946 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab4e7fc8-a036-395e-b8eb-67658eaa0bba | -5.7891 | -51.86476 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1225936f-e4f1-3cf1-b80f-d2803cd379c4 | -6.24847 | -47.64943 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fecb143b-a01f-364b-8647-dc94a5271072 | -4.26104 | -48.63169 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac246d4-1af7-3906-9825-ad8c8fc7ac07 | -2.71518 | -57.96216 | 2026-09-20 04:38:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 024e1baa-b03c-323a-9ed3-5d0f82462d5e | -2.8838 | -57.81617 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 411e2a47-b8de-3829-8f87-a69d4dcbe34e | -6.92274 | -42.8962 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03a91f79-81f6-3e46-a0c1-60bd0973f6eb | -2.8241 | -50.46338 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dacde2b-48a1-378a-95fd-544d9aef916d | -6.29541 | -47.61101 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 531f3bbf-3420-3783-9191-6304106b6c4d | -3.82608 | -48.99802 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b04a68-8fe1-32c9-937b-b71e95704904 | -3.50325 | -43.35735 | 2026-09-20 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 94efb516-85b6-38a4-8e5e-9cf99b0632a0 | -3.6852 | -60.59627 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d99939d-7581-3696-81e4-eaa0eab7d9b1 | -5.60341 | -44.37972 | 2026-09-20 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79fca0bc-9215-3418-b8e0-47fb9154620f | -3.0121 | -54.16982 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd916300-d9b2-379d-8035-134f1403a20a | -3.84596 | -51.34303 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40b63791-a5ad-3ccb-b7e5-d26a4957fd2b | -5.76573 | -47.28536 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a06e6a0e-a6f8-3f5c-849d-15bc7b8a450a | -6.9263 | -42.90046 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81db1e78-a954-3183-ba7e-c5017e8935db | -2.71704 | -57.96704 | 2026-09-20 04:38:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52854d7f-3828-36dd-b18f-4c08f8da13ee | -6.17096 | -47.51639 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3866db6c-77c2-34ac-b184-337c07bf4f8f | -4.53296 | -55.62716 | 2026-09-20 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e828074d-7347-3d5d-a218-5f0523f08b55 | -3.53399 | -58.69363 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b0c6a9e-8c55-3631-b226-fd31014b6c94 | -4.20541 | -56.33937 | 2026-09-20 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 091fb378-ba6d-3b49-a1d5-c55995861cde | -3.69537 | -60.57864 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82c3010e-1eee-336f-a75e-c09fc9ade734 | -3.40283 | -50.40104 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 219036e0-ef7d-3565-998d-1c2c1c753cc7 | -4.26381 | -48.63575 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc8a5391-dfc1-3ccb-925b-2820383c1376 | -5.64233 | -43.3755 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20207538-1c40-3b64-976f-f00fb2bb0f05 | -5.89107 | -46.59033 | 2026-09-20 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a1a2b2-7a5f-3943-8d6a-7b16ecf89cba | -3.07419 | -51.19821 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd05b164-373b-3d1e-bd19-0f33308fd7af | -3.68409 | -60.60257 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbd3531d-3ab3-3ff3-af9b-838bc2ecf90d | -3.00771 | -54.16633 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 713f3ac9-0ebf-3027-ab3e-ed1ddb3fef74 | -6.68578 | -43.63262 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4eeea194-7253-3bdc-8154-78fcea9de742 | -6.96908 | -42.17361 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71ce695b-f18b-3ece-96ab-61a45c7beb6a | -3.89238 | -49.09015 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e84e252-011a-3849-ac67-40e596d999af | -5.27802 | -49.34881 | 2026-09-20 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2a0d02d-f157-337a-b93e-0c1d7f7bd0a9 | -7.02875 | -42.08006 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20cb8487-6f98-3391-b16b-368a619ff416 | -6.06731 | -47.87244 | 2026-09-20 04:38:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed09b6eb-9807-3e8f-a7b5-5e23330cee42 | -5.61261 | -52.16125 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96dcb1e3-a9f1-3dd6-b1c4-42c571cdf54d | -6.7196 | -46.07582 | 2026-09-20 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18d5fa4e-156b-3da1-944d-f42b8fb00843 | -6.19649 | -45.32879 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3611b3fe-5b11-378a-a517-06ac00d73bbb | -5.78442 | -50.20925 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d5840a-3891-3f43-94c7-55f9b575b6c0 | -5.22623 | -49.32579 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f395e07-beda-369d-bc72-4fb7b666a591 | -5.8313 | -52.03168 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d0489cf-e266-364a-962d-374e176378fc | -7.12084 | -43.10263 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a73f7ffc-0278-35dc-81f7-0575afca40ab | -3.36264 | -50.44495 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf96795e-2b09-36f8-ae24-485bf52b883b | -5.22141 | -47.57239 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47c002e6-31f7-3536-a385-a72662cfb0ff | -2.61389 | -54.75246 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f720ff69-12f7-300e-91af-be83c6845a42 | -6.32636 | -47.63009 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 75b9ff77-91cf-385f-bea1-d7a90e4ab5f3 | -5.78456 | -47.29545 | 2026-09-20 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 226d7040-49cb-3e0e-861d-6c93b22e7e60 | -3.50776 | -43.35332 | 2026-09-20 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2694e8b-f8b3-3184-8c2c-005e09ad4231 | -4.4627 | -42.90834 | 2026-09-20 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f86b757-7e6d-3181-9143-eb820aabf418 | -4.61864 | -46.30288 | 2026-09-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 013e39d4-2128-3a43-88d1-e9cfd05afec0 | -3.37702 | -50.44727 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb56369b-c2b9-3881-8577-77d92054a77d | -2.14411 | -50.90616 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c95b2a72-5c4b-34e8-b722-fbbe28eb70b1 | -3.44185 | -50.60501 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 922c8859-3107-3248-b5ee-6ebef25907ef | -3.35479 | -50.44787 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff4bcc72-5146-3f84-a57a-a56e74ec959e | -2.4557 | -49.21378 | 2026-09-20 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 139d11fd-4c9a-39fd-8b66-e63de02ba231 | -6.98713 | -43.73437 | 2026-09-20 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4181bf7e-3d63-36b4-baa0-44d65bbae5b5 | -6.26152 | -42.72915 | 2026-09-20 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce104469-bf79-371a-8ce2-d88ad2aeb244 | -6.21226 | -45.34377 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 308c16ee-551a-30d0-b60d-7b144ee7ca9d | -6.30317 | -47.62645 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d01fe8c-d196-3845-b008-525d5abc9dfe | -5.8114 | -49.09202 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6371bc9-e027-3e35-8718-7830a97c482d | -4.49002 | -55.48124 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da26f546-2fdd-3659-a8d0-4ede76994506 | -6.41396 | -43.8747 | 2026-09-20 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README53.md)
