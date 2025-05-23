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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f61db2df-006d-3e17-888f-0d4ffead0401 | -9.04068 | -47.75001 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb2a6aea-2f2e-304f-8655-1205c5c4ee34 | -12.26596 | -47.00239 | 2025-05-23 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac67eba5-dbef-3820-aaf5-6856ad847dc7 | -11.79183 | -44.28189 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a92db8bc-876c-3536-a721-e537d437a58b | -9.96462 | -49.80761 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f110789e-5a0d-354f-b747-c6afd2b32630 | -12.38699 | -49.97737 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e85f3a30-3876-3ca1-826e-edac70c95c8c | -7.71345 | -45.65661 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c538d36c-4fc2-355a-9dc2-4cbc7ddc1b39 | -12.41022 | -42.52913 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d4d4ebd-274e-3bab-9ea1-c0a503200fde | -11.79423 | -44.29089 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2291ae77-78e6-393b-acb0-ab6d5fe29cfe | -12.08285 | -47.34877 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45087180-268d-343b-87f9-f8f2b031d194 | -12.42408 | -49.97925 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3285e378-a0f0-3eac-81f3-9e1e5ce86c61 | -11.93444 | -43.93549 | 2025-05-23 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89107e4d-8c10-305a-aeb2-ca1570301b1f | -12.38982 | -49.98187 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d83cd46c-cf22-338b-a4b6-0384c1c76f99 | -12.84715 | -47.38953 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4db11bce-a43d-37a6-974a-4d249baab0c6 | -9.02344 | -47.75085 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b611221b-f48b-3a90-ae81-8aba9b241654 | -11.75502 | -47.2528 | 2025-05-23 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1298b638-f521-326a-b74f-ab4317b53bb6 | -13.15524 | -56.81582 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4df488e6-3aa6-3886-a92a-2c3c041607e7 | -11.79243 | -42.63687 | 2025-05-23 04:25:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9d94c06-28e9-3e76-bb80-6153a1187730 | -12.83997 | -47.39198 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04d5bea8-9e90-31a1-96d1-8d0b84391ce4 | -12.33637 | -49.98076 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ae058d1-a112-3a4e-bf75-ed0b1ee760e9 | -11.78822 | -44.28133 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0f6e17d5-7d62-38d0-aab8-cf6e2b9b7d4f | -14.04481 | -53.37334 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa82faf3-7b0e-3b65-b16a-fa91f0d8eaca | -12.42061 | -49.97865 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dadc947f-29a4-32b9-8724-dfb925ce8db1 | -12.41648 | -49.98197 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a22cc73-8344-35dc-ab27-4506eacef282 | -11.55916 | -47.4624 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f71f067-650b-3499-8084-cc8fc2c28442 | -11.74773 | -54.72375 | 2025-05-23 04:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fe5a47d-273e-3bb0-90a3-a73389bab2c2 | -11.57165 | -47.8969 | 2025-05-23 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdc5560a-f2e8-32cd-b252-cf1c8679514b | -10.7163 | -48.82407 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74980470-14d8-39cc-a76d-7498eed41053 | -13.49222 | -55.6633 | 2025-05-23 04:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a82ed695-cd03-39a2-bd76-fe594986b2b7 | -10.70953 | -48.82295 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db3267bc-3179-3a55-9774-db1b1443e8f6 | -13.18175 | -53.57331 | 2025-05-23 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef63fb35-eb68-3ae8-ad7f-bc6d5df95c3d | -12.06751 | -47.33915 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6681f7e-56f2-3fa3-a9a5-fcbcb8b869a0 | -15.1177 | -43.95532 | 2025-05-23 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71b2e105-cc3f-3755-9c57-2bbfd1504057 | -12.84328 | -47.39252 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09d4c174-0549-38b3-8baa-a7790576c8de | -13.94075 | -54.48768 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f30dfb2-8fc8-344b-86f9-b8d7a222afab | -12.82456 | -47.38206 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98ade226-cb64-364a-aedd-ad94feeb4280 | -8.89952 | -50.02885 | 2025-05-23 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 176501b3-d6be-3975-ace9-760a5f87cd9f | -14.0428 | -53.38452 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c6c1583-13b0-3cfe-91f3-53399752b991 | -12.39047 | -49.97796 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e52a8f3-d2de-3991-8787-c384ff8ca238 | -11.79122 | -44.28611 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 72f2889b-dcee-3bcf-91bf-5de8a72fa0f7 | -11.089 | -57.27098 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a972bfa0-f540-3db9-a033-3b51dc89aa38 | -13.18245 | -53.56935 | 2025-05-23 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6585f732-f9d0-32e4-a63f-4266fa230e4a | -11.79483 | -44.28666 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60e050cf-f8be-309c-beb1-4b4569c96a62 | -9.96815 | -49.8082 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a27538e-a4da-387b-b56b-2e73da30b059 | -11.56413 | -47.45241 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88b2cf42-5742-3a4e-b967-a0264c82eb8d | -9.04124 | -47.74648 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f14d6fe-8991-3f1a-b028-a8e111286fc4 | -12.297 | -52.49117 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd1427f5-0202-3ac1-8e41-21641320a2dd | -14.03734 | -53.36807 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 095ef339-c847-3b71-9da5-1afc73bb2194 | -11.56468 | -47.4489 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0292fa3f-f456-3c62-a2e1-c8c868afb2b6 | -12.32397 | -49.99074 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38d2fd6a-7c05-3140-abd5-f9e573fc83e9 | -14.06792 | -53.38543 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53e1bb9f-cfcb-3cda-9839-8d359cce5ec2 | -14.67858 | -45.10548 | 2025-05-23 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4749e0c2-d874-3607-a50e-c120cc4dff7d | -9.21493 | -49.67249 | 2025-05-23 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdfb6d17-6535-325b-9d67-748945cd47d1 | -7.70957 | -45.65961 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8611c847-c529-31ba-b060-25cdcad03314 | -11.97394 | -44.15513 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4cd9fa9-31b8-36fe-b94b-fa19190b772b | -12.28727 | -52.50015 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1036a01-f71c-3ee0-8cf9-f69a8fc35c15 | -10.98569 | -59.1518 | 2025-05-23 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88d6517c-3391-328f-81fd-3af2a90d65aa | -10.64331 | -49.48017 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb77a84c-751d-3ce0-b3bb-5f3838eab878 | -10.71291 | -48.82352 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc67eee3-2fe3-36c9-a1eb-9e8da45fd9c3 | -10.67954 | -57.59966 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2567caab-5fd2-33cb-bce6-714c5c6dc4b9 | -12.31984 | -49.99406 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69fe7c40-98f9-39e6-af9f-5b7af9f2bf39 | -12.301 | -52.50437 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc74b4ef-75da-362a-80f7-8c0c0b1c2f4a | -11.03573 | -50.77637 | 2025-05-23 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7c4b4cd-a939-38ea-979d-7e0c97de8cf6 | -15.42638 | -41.40655 | 2025-05-23 04:25:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b483c700-8deb-3ab6-b964-6a55e43dc72f | -10.66601 | -49.4721 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe51182-d90b-39fe-9a7d-6fc16cf3e893 | -15.02936 | -43.84112 | 2025-05-23 04:25:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72ea6b7e-da3c-30a4-ba6e-01228580e6b0 | -11.93875 | -43.93165 | 2025-05-23 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f87c3cbc-1f7a-3bc5-86e0-29b79af11758 | -9.0418 | -47.74295 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 84e0fd31-9d9f-369a-9fdb-4ce35876a655 | -10.81845 | -56.95738 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b678e7c-8ae7-3e3a-a493-f68a588b562d | -12.294 | -52.49769 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 530a752e-5ee4-3ea0-bc10-b75d3ba335d1 | -7.96869 | -49.69621 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a705ae6f-9b70-3937-9639-e6b11dbfe9b8 | -10.49213 | -42.41457 | 2025-05-23 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5e2c44f0-1015-38b8-9cdb-816e76211c64 | -10.36901 | -57.49921 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ed06d73-2a18-3c32-b75e-f536383f9749 | -11.56916 | -54.56508 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c5e51a8-84ba-308b-8d36-2529b0208152 | -10.98468 | -59.15687 | 2025-05-23 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c462c11-d369-3683-a9dd-a9b72eaadfdf | -12.39394 | -49.97854 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61f9dc99-3c08-3a70-bab9-3e388c79afff | -11.30844 | -54.02722 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd830adb-adb0-3c31-b0a6-b30f1d92a914 | -10.61486 | -49.55582 | 2025-05-23 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1eddc7d0-3875-3148-83fa-f423f4ecc6bd | -9.2178 | -49.67713 | 2025-05-23 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0a6c9e6-0347-3cb5-bdf2-1aa9455a57f9 | -7.71236 | -45.66365 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b71ee13-aee2-3c98-8ad2-03151b2a370f | -12.85046 | -47.39006 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b72d68c8-f5a2-3161-9496-a9af4c7f3881 | -10.71571 | -48.82774 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f468047-a665-3b7c-a5a8-181168aa28ea | -10.721 | -52.47149 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 569c143c-89d5-3aca-b703-b606699286c1 | -14.68154 | -45.11022 | 2025-05-23 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28366df3-207a-32b8-a9cf-86fc06158712 | -11.74864 | -54.7188 | 2025-05-23 04:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40f21a0d-ccc8-304e-bdb0-790ff7259eab | -12.32876 | -49.9835 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdeda4d5-e7af-3bba-a0bd-943baa0899f4 | -11.93956 | -43.93372 | 2025-05-23 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8722e908-e0af-3ed6-a3a9-842a70d42b1c | -12.2952 | -52.50161 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56a99463-babf-3f4e-8f2c-e531a7580a2e | -7.65745 | -46.10267 | 2025-05-23 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 269c47e0-6967-397d-bdf8-aed5c11e2b08 | -14.07199 | -53.38621 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 157d02b8-8369-30e5-9e71-16c8e359aa57 | -11.65513 | -58.26023 | 2025-05-23 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 835a2c69-2828-3e52-be5c-c89e02602172 | -14.05296 | -53.37489 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b27edcc-b453-327a-9f16-bacaec8e3e7f | -12.41995 | -49.98257 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 49d99443-653f-322e-8577-1be0ac5bb373 | -9.04345 | -47.75409 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59ad6b96-fc64-387c-b3b5-5d1fed0c8e0b | -8.47918 | -49.60617 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a05187fe-ae2d-3242-8f03-ff418f0d9ba9 | -12.33507 | -49.98858 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4038fe22-bf52-3018-a093-1e34607271f7 | -11.32472 | -58.62642 | 2025-05-23 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e24a4531-d515-3f42-84fc-c2e3a5e5581c | -10.82325 | -56.96193 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9aa0a5d2-31eb-3019-810c-28e49c506222 | -11.26844 | -52.47209 | 2025-05-23 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a433af9-8007-3404-b933-04be4ae443ba | -8.7234 | -50.25621 | 2025-05-23 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f30719-0908-3407-a35c-e29fb146f1fb | -13.78352 | -54.30811 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README14.md)
