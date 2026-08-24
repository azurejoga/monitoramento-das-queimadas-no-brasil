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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865b1e91-ca9d-346a-9c24-d086dda2ce9c | -15.34478 | -52.79678 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6ea7458-c9b8-39cb-afc9-4caf1cbfe278 | -14.41654 | -51.78534 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| afee77dd-5e09-3924-856f-26ef4e408a7b | -12.11262 | -50.6209 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| fa611334-26fb-37e3-9a41-b0449459b020 | -16.04764 | -50.43002 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a18daf94-d11c-3c72-90fd-295e0fcda811 | -18.5244 | -47.16909 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50730bd4-a87f-397a-950b-f9d0392276fe | -12.07207 | -50.57484 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9511d2e-02b2-3056-9e7b-5622f8d8dc45 | -15.30504 | -52.82586 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a024f726-c8a1-3b5f-9f73-70915ef07cc1 | -18.33702 | -43.91228 | 2026-08-24 04:27:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cafc9637-2fea-387e-bedf-f1a259ada8e3 | -16.0526 | -50.4255 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2240ca6-9aff-35f9-b71b-81c13d66aae8 | -12.75197 | -46.44322 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8c2b643-1a10-30ce-9e6b-84890a80d5a7 | -17.74607 | -47.03279 | 2026-08-24 04:27:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed820d87-34b9-3af3-96ab-83f45dd4ee7c | -12.85499 | -48.49165 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f271a966-45b1-3925-8959-52a2a80fe649 | -13.09647 | -43.35725 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0fb766c-cbe1-3ab8-8a5c-919dd4cbfeaf | -12.73732 | -46.46786 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba134757-c26d-3e18-9df7-142377bad196 | -12.85872 | -48.49234 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc661a71-6d1a-3b38-8e70-97454afd7a5a | -13.69006 | -51.8371 | 2026-08-24 04:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8cf48f0-82d1-3948-b0bd-4bd2ed653495 | -17.42155 | -48.84013 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caded7e1-1c6d-3976-b3ee-88d9845b6e7a | -16.06052 | -50.44938 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2c16e162-0641-3486-9c7d-73cc4ce8a9bb | -19.07797 | -47.13738 | 2026-08-24 04:27:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a388160-3584-305a-85cc-00b9ae2de90a | -16.05468 | -50.42928 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e0ad4e5-f8c2-3443-8359-66e8221897aa | -19.9344 | -45.07013 | 2026-08-24 04:27:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21a204f2-7cea-3be1-9bd9-861d1339a70c | -15.29194 | -52.818 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4c4e41f-9fd9-3941-97eb-316bdd36decf | -15.26704 | -52.86535 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b49f46a-dc19-360c-80e4-344253117b76 | -12.8665 | -48.46968 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5438afe5-4bd4-388e-853b-e39b5039b066 | -18.08668 | -47.2772 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4891712-59e9-3c2e-9177-37c7badea5e1 | -18.44893 | -48.41309 | 2026-08-24 04:27:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9c34301-2b4c-38d4-bbfd-31dd5d8a303f | -15.33294 | -52.75754 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 444bad36-c532-375a-9b66-ccb1a22692fe | -11.84647 | -51.67868 | 2026-08-24 04:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2efc371-c6be-3e99-8ae7-f92505624283 | -12.06424 | -50.56913 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbf3835d-e05e-363d-8562-6dc76a38b2f0 | -15.26634 | -52.84326 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d20bdf5e-4ff1-379a-af70-57354f9c66ea | -19.0096 | -42.12551 | 2026-08-24 04:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b44d0b6-ed89-374d-8415-882835d33a4a | -16.41905 | -49.91806 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b631f67-0270-377c-bd81-dd903b0cfd29 | -11.20436 | -55.04478 | 2026-08-24 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dcc92df-3331-389b-8dae-ff8586667035 | -15.27551 | -52.87227 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2873e06c-5f75-3efe-81a4-489399bf7325 | -15.27344 | -52.8129 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75b8d887-3e4e-3955-8f01-ecd393cac876 | -11.15826 | -54.00756 | 2026-08-24 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2150117b-fcbe-3f31-9330-11b9548a2344 | -15.78712 | -56.06695 | 2026-08-24 04:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| decdf7d3-a7bb-3ba4-8d2e-37fcd977fcb4 | -12.10329 | -50.62341 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 3f99fe18-8bdb-3f18-b1c2-09610af5085c | -17.42218 | -48.84278 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4104358f-1e38-3401-a381-b7a6d821a4b5 | -17.43018 | -48.8329 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 981bd314-4124-3a7d-9321-13dacb30c673 | -15.35241 | -52.7824 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81278084-d424-316e-95ce-c117d45b553d | -15.26803 | -52.86013 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e91ede9e-7d1b-31ae-aa43-b14302024397 | -14.39874 | -51.78178 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 182a8017-7163-3880-8ad1-8fc3b0ab1585 | -12.85829 | -48.47272 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5c6a959-9fdb-3e78-af8e-31012ca73d50 | -18.60568 | -47.1223 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceae39c6-9c97-3765-bbbf-fd147823da5f | -16.41054 | -49.92124 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6740e4b-421f-3a60-97d5-2202cf857489 | -12.86502 | -48.47821 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cd8d863-1f02-3836-ba2c-6aad74f0e158 | -16.38485 | -51.82285 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 097e00c0-ed08-3ecd-9a91-889efe8cc5bf | -16.40925 | -51.8358 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb99e1f0-2237-33ee-b4ac-148fd963bd9f | -12.10906 | -50.61595 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7a3a2934-be2c-3b75-9151-9032b2bc61b9 | -16.0625 | -50.43871 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3da5eb52-04c3-3bda-b3b0-cbc15865c393 | -17.83312 | -44.46974 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a390e35-8f30-3a8a-8d07-6764fe6d3db8 | -14.98211 | -52.68292 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6799496-391f-3636-a8e8-358c770b2da0 | -14.31698 | -51.76158 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b968716-3cf7-3757-bf60-2fba53f35f9c | -16.85619 | -49.44536 | 2026-08-24 04:27:00 | NPP-375D | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31137831-693b-332b-8509-5473b3e8408d | -14.78468 | -48.77425 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9596a9a6-9902-3639-9c87-463a5e032c0d | -17.09606 | -49.40205 | 2026-08-24 04:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3aadc5b-06c4-3fed-b25a-0a8aaabbf107 | -13.15537 | -51.3903 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d302edab-54b2-3940-b250-09e849e164af | -19.15671 | -44.40131 | 2026-08-24 04:27:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2c3669d-0c0c-3d56-a935-ecb9755ab560 | -17.41945 | -48.83088 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9ecf06fc-50a2-3f5b-bb6b-ec2b932fdc7b | -13.26528 | -51.44438 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6061cd3b-a847-3469-8aca-c7d3ae989681 | -18.31937 | -47.20239 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7918b69-3d9a-3823-bc3c-687037fc1691 | -11.1578 | -54.01064 | 2026-08-24 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d0a62a-83ae-3f99-9d61-fc38a220decd | -12.09839 | -50.60111 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15f2253c-50cb-3ad8-bf2b-f4a433e3da05 | -17.42871 | -48.84148 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28842474-7c48-36f9-b89d-54cd91674cee | -15.26475 | -52.82593 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 854e2b3b-31d5-3dac-81e3-7b6d454867d6 | -15.2668 | -52.81518 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cbdb6446-32dd-346f-b5f9-429b9d6f4bdb | -15.12209 | -42.91983 | 2026-08-24 04:27:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95e55667-4fd9-37a0-99a0-a581d59193e8 | -14.33564 | -51.76059 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a0a40b1-cc43-371a-8ba0-37c6be7d3a95 | -16.09126 | -52.34585 | 2026-08-24 04:27:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45351e87-6814-33c4-bdb7-49e294c17d49 | -18.07407 | -47.29043 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e3e74f6-0166-3913-b25d-4437d1f4f433 | -16.06278 | -50.45312 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27a46a2d-db6b-3c8a-a81c-15d1f1ad6d52 | -15.25702 | -52.84092 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfd54dbf-c8e0-3711-bb9e-e12c7843e57d | -12.75134 | -46.44694 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88603583-c244-381d-b162-e9b4444478ae | -15.26658 | -52.8723 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bed95361-1d7c-3b19-a55c-970391b1d584 | -15.35345 | -52.77699 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98815469-9abb-35fd-8e98-5fc3ca807934 | -18.5305 | -47.17403 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7781f46-c8f9-33c1-87c5-f5a497ddda37 | -12.05921 | -50.57243 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b309e0af-067b-3408-a201-cf6bd39ff940 | -17.7041 | -46.38361 | 2026-08-24 04:27:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c8ba337-b244-36df-8f79-f7b1c3255cc3 | -12.8628 | -48.46887 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3bb5973-e16d-3440-a800-74cbcb9ea4bb | -16.06648 | -50.43945 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5695042a-a4e5-3899-8069-040e2178ac29 | -16.06468 | -50.4424 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 03d641cd-d2e3-37b2-aea9-9e32e3debc4f | -19.89363 | -43.88352 | 2026-08-24 04:27:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 27abdd89-b1bb-37a4-9857-6c50fd7da815 | -18.5482 | -47.15034 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95082314-d29d-35a7-883a-c0d017bfd0ee | -11.86407 | -51.68718 | 2026-08-24 04:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcbc1260-9c7d-3447-bd64-ca78ae7612cb | -11.91204 | -55.89989 | 2026-08-24 04:27:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7af5024-04a3-3cbb-bac4-f4e7ba74cb8c | -14.44601 | -51.80062 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb3525b8-6748-3013-9a0e-b9e70e745223 | -13.44693 | -43.84496 | 2026-08-24 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5621f768-b89a-3215-a718-cf866595bf7e | -12.86576 | -48.47391 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a56070d-b32d-384e-bcb1-aa7634b98771 | -16.04864 | -50.42466 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e06bb617-7609-3588-b241-7ac767cbb343 | -12.10624 | -50.60686 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fbe219d7-0544-35d7-827a-b99ab5e79375 | -15.28731 | -52.81676 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e35c124d-eacd-35d7-8815-c5629de143c1 | -15.2707 | -52.85146 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a4380429-7412-3c48-8e61-52ee6342baa6 | -15.27004 | -52.84953 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71266d3f-b120-3b24-852d-c19440c64b99 | -17.69019 | -46.38491 | 2026-08-24 04:27:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e1c47af-2c6f-3479-979a-32f2fc9ab308 | -16.05975 | -50.447 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 57f2b1bc-b693-3964-8be9-6d96b8374074 | -17.4244 | -48.84505 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2faa52-006f-3352-9929-db1d6f1c162d | -12.7467 | -46.45374 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dca083a-2dce-389e-b753-9d7e59cebf98 | -15.26982 | -52.87645 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d81a7ab-f850-3f92-8810-48f34af90c51 | -12.58663 | -47.94707 | 2026-08-24 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
