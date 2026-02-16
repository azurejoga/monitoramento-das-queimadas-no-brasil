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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2e9be46-5e7f-3e5b-bfee-ada0f66e3473 | 2.7634 | -60.315 | 2026-02-16 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 70fbe22c-ce2e-3eca-a4e4-1e7a4989c836 | -8.82233 | -35.67187 | 2026-02-16 04:33:00 | NOAA-21 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 59ccbc02-267d-3531-9604-057f4a5f743b | -9.40823 | -44.53571 | 2026-02-16 04:33:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05a10078-bbb4-3a1a-9943-e941fd9042f1 | -5.28509 | -56.01796 | 2026-02-16 04:33:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b30f9de-4f4a-3554-902f-e22af5596bba | -5.00647 | -37.46518 | 2026-02-16 04:33:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d044655f-666d-3259-aa0b-e818d92d0510 | -5.28457 | -56.02095 | 2026-02-16 04:33:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8368bbd3-102a-3640-81b1-1310a55c068d | -8.81903 | -35.67595 | 2026-02-16 04:33:00 | NOAA-21 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a93ca842-0617-359a-8eb4-a61556f8d02d | -8.1662 | -43.1674 | 2026-02-16 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e284c3d-de16-3a88-ab9b-cdd1fa513b16 | -11.17835 | -43.3048 | 2026-02-16 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e98b6891-ff31-3935-967c-11cb9aec1e51 | -5.0102 | -37.46788 | 2026-02-16 04:33:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5251e0da-00c9-349b-bb63-f0dccf5714c3 | -8.82583 | -35.67632 | 2026-02-16 04:33:00 | NOAA-21 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2efc5dd-06b6-3040-9cab-2ec959abdbdb | -13.50635 | -47.55013 | 2026-02-16 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 979461b3-d0b8-3c3e-97cd-d02e11749fe4 | -11.84874 | -49.22324 | 2026-02-16 04:36:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 737d7ded-ab0c-37a1-b807-580813fb9991 | -15.00796 | -45.14637 | 2026-02-16 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af1950a8-91b3-3978-bae7-e08cca0a9d8a | -12.53549 | -47.55286 | 2026-02-16 04:36:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fe9b231-e07f-352c-89b2-25d7ebc51931 | -15.42146 | -41.44228 | 2026-02-16 04:36:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ac70012f-f1c0-3a8a-8be3-b720dee3dbea | -15.0119 | -45.14695 | 2026-02-16 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb80ab57-9e44-393f-a8b4-b76cb567421b | -15.01262 | -45.14175 | 2026-02-16 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 027e9c83-2ffc-36ba-85c6-d0a261a4d6c5 | -11.84599 | -49.21922 | 2026-02-16 04:36:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b954fdff-497e-3547-afa6-6399ca896a54 | -20.7247 | -48.8728 | 2026-02-16 04:38:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8fffa9e-d5f5-3ee6-8de4-4d05f323a63e | -22.9642 | -52.8493 | 2026-02-16 04:38:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 523948db-6691-3c53-bc55-de86f3397e63 | -20.76037 | -44.03099 | 2026-02-16 04:38:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| afd92305-782a-3c2d-a41b-333d33749390 | -20.76105 | -44.02683 | 2026-02-16 04:38:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 86111c44-84d6-383a-9b01-02fba2acc600 | -17.53244 | -57.27703 | 2026-02-16 04:38:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 391d1078-2397-3edb-be63-96641495a814 | -23.41443 | -50.7695 | 2026-02-16 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1ef5089-9aca-3251-af3b-5dbea4681554 | -23.40718 | -46.35442 | 2026-02-16 04:38:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 524f3a2c-7f4e-38d1-a4d6-70f361ec6b51 | -22.24939 | -47.21347 | 2026-02-16 04:38:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7336dce1-8485-366b-81a3-5cdfea592faf | -19.40858 | -51.62609 | 2026-02-16 04:38:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 072618e0-58b9-309e-a6a7-2caceee1325c | -23.41126 | -46.35505 | 2026-02-16 04:38:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 73c9f671-3820-333b-9546-3af093720b4b | -17.5377 | -57.27346 | 2026-02-16 04:38:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8f3a01ee-6d17-3c69-9d51-5d425899d5df | -22.96482 | -52.84552 | 2026-02-16 04:38:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 176b7734-db7b-31a4-a031-79553cba3b05 | -23.41778 | -50.77008 | 2026-02-16 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc9e7344-af0d-329d-b27c-1e3322b6a383 | -21.2716 | -49.4039 | 2026-02-16 04:38:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70dc5683-efa8-3ab9-b463-203a52ee77dc | -23.41835 | -50.76624 | 2026-02-16 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba677d20-4ef2-3814-b03f-e6a1794095e0 | -23.415 | -50.76566 | 2026-02-16 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ffc03eac-d6e7-366f-8d2d-92f960e82020 | -18.97557 | -52.92739 | 2026-02-16 04:38:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 60f7e722-302a-349d-859b-a289098369a0 | -18.97492 | -52.93126 | 2026-02-16 04:38:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7f2e03a4-137a-31ed-9006-8fd75376512c | -17.53339 | -57.27312 | 2026-02-16 04:38:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 3308972d-57c4-356c-8b4d-f0fc06dca2d4 | -20.76097 | -44.02584 | 2026-02-16 04:38:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a248b80-3baf-3668-840d-5dc3117003ce | -22.96753 | -52.84992 | 2026-02-16 04:38:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 39c583dc-ed56-3d14-a26d-69c12249071e | -23.40763 | -46.35049 | 2026-02-16 04:38:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 83679324-ef2d-3524-b2cf-4542dc8509a8 | -20.08458 | -49.92168 | 2026-02-16 04:38:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 677cde6b-2873-3fa5-9c03-87b1e8cf3cc5 | -23.41172 | -46.35112 | 2026-02-16 04:38:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 3f48d54c-bf12-336c-a0d1-4b29f6c6b78b | -19.43793 | -57.08289 | 2026-02-16 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aae90a4e-268d-3883-9367-b2119ad93e3f | -19.75906 | -48.28959 | 2026-02-16 04:38:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e3e446-1aff-3a89-9492-02ca359cef99 | -19.76258 | -48.29016 | 2026-02-16 04:38:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c10aa8a5-33c3-3f66-9d96-257c90680ade | -17.53332 | -57.27256 | 2026-02-16 04:38:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f6dd33cd-10d6-3791-b924-f60dd29d743e | -21.15836 | -53.21672 | 2026-02-16 04:38:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 787f13e2-3bb7-3a8b-97f8-33240e0032e3 | -17.96698 | -44.93142 | 2026-02-16 04:38:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9861115-2d5a-3cff-ab92-d7d532c0cda2 | -21.15498 | -53.21607 | 2026-02-16 04:38:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89e788b6-21a0-3f84-ae72-a68b2114576a | -19.75965 | -48.28542 | 2026-02-16 04:38:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aa9ce43-18a6-3b27-8347-a4c0368c8df8 | 2.7634 | -60.315 | 2026-02-16 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8ebcd33e-c6fb-3b8d-97f5-57d957e522c9 | -27.45762 | -48.4528 | 2026-02-16 04:40:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45f61d88-23cc-319f-a1fe-db1cbbd380ec | 2.7634 | -60.315 | 2026-02-16 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7e26106d-8f92-3eda-98d3-639943f04fbc | 2.7634 | -60.315 | 2026-02-16 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 131aa3f3-ee73-3527-900d-aebecf74659e | 2.6548 | -60.17154 | 2026-02-16 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46989f44-bfd4-3030-bf25-57700869c301 | 0.93609 | -59.42053 | 2026-02-16 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b45202-55c4-3e11-8cf7-5077e1b88298 | 2.66555 | -60.17554 | 2026-02-16 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6cff363-52b7-3fc5-92e9-24de83480d81 | 2.66469 | -60.16996 | 2026-02-16 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63273756-bc22-3500-bbc6-a43f81883b78 | 3.84618 | -60.89737 | 2026-02-16 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6465e6f3-39d2-3723-ba85-7f81c1216cc4 | 2.76921 | -60.3203 | 2026-02-16 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 30820c71-17ed-3048-bec5-e80f833adccc | 2.66597 | -60.17481 | 2026-02-16 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e4da53e-3fd4-3a5e-8207-613b0dbe4de8 | 1.85196 | -60.3294 | 2026-02-16 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd564596-b2b8-3d10-970a-78a22329af47 | 3.84084 | -60.89789 | 2026-02-16 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86da4732-b48c-357f-a9aa-e5263dac84ac | 0.93682 | -59.42517 | 2026-02-16 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19fd9461-4f68-359a-8831-d1ae70740ff3 | 2.76834 | -60.31458 | 2026-02-16 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 45dc30f4-2316-391b-ba7f-ecb1ee485475 | -5.28576 | -56.01986 | 2026-02-16 05:03:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b3687bd-f50d-363a-bcf4-ea3fcb59cfb2 | -5.28231 | -56.01929 | 2026-02-16 05:03:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15052285-ed5b-3adf-9c53-a525a83212cc | -14.21442 | -58.14119 | 2026-02-16 05:05:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6baf9370-97ec-374f-9cdb-ef90c7cdbddf | -17.53572 | -57.27639 | 2026-02-16 05:08:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8ce6545b-4d32-39c3-b4d8-7c1033f1eba3 | -19.12236 | -56.23639 | 2026-02-16 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7522ba83-c530-3149-9246-2d068c451e5e | -21.15686 | -53.21907 | 2026-02-16 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dc18616-eb8b-374f-934e-319d05057dad | -19.43637 | -57.07998 | 2026-02-16 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 688d3d8d-ba67-3753-9d84-6fedf611f051 | -23.41677 | -50.7693 | 2026-02-16 05:08:00 | NPP-375D | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1d86eeac-bf92-3b9b-ac26-68e7aa5b07d3 | -22.24841 | -47.21724 | 2026-02-16 05:08:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dde8352c-7643-3340-827b-33df2e14dc0b | -22.96549 | -52.84711 | 2026-02-16 05:08:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f4dee321-4728-3f01-9a4e-deda08b83652 | -21.15754 | -53.21397 | 2026-02-16 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8edfd934-6696-361e-9a5c-77f764280f42 | -23.41136 | -46.35372 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| b1c37d02-0e7a-3d53-b491-6bfb988f3e55 | -23.412 | -46.34803 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 959ce521-edd6-3a16-bc4b-cc79da734f86 | -23.41157 | -46.35302 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| deedb712-8ecf-31ea-82b9-d0f367d71b34 | -23.40544 | -46.35229 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| da313faf-fdbb-3904-a9bc-2131b7ad7b0a | -17.53239 | -57.27581 | 2026-02-16 05:08:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f0917120-71bc-3f11-b1fc-84d4d61aecbc | -19.75909 | -48.2899 | 2026-02-16 05:08:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d9f9745-3b5e-337c-926a-d7cc6eaf3901 | -23.41176 | -46.34873 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 931e7896-8f1b-32b1-9f63-8684b5af8da5 | -19.13128 | -56.25227 | 2026-02-16 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 87fbb4c9-2920-3d6d-add0-492c74e34180 | -23.40523 | -46.35298 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 8f5bbb26-3950-303a-8643-56724fe0825f | -22.24881 | -47.21306 | 2026-02-16 05:08:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d17f95f-3eaa-334e-bcab-6fec086fd5ba | -23.40563 | -46.34801 | 2026-02-16 05:08:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0e581910-4271-3604-a2ff-512c3c28e4e9 | -19.13015 | -56.25301 | 2026-02-16 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 173af257-d08b-38d7-93db-e10420819655 | -19.75943 | -48.28666 | 2026-02-16 05:08:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 564d2f10-08d0-3774-a53b-13e98313ecc2 | -18.97398 | -52.93018 | 2026-02-16 05:08:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5f4aee35-942d-365d-a8f3-c39eb83b7cec | -18.97781 | -52.93073 | 2026-02-16 05:08:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa67c00-79cf-31a3-9104-da48ec65a496 | -21.15298 | -53.21853 | 2026-02-16 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb09f35c-63dd-3da1-9ea6-a53d79a98e37 | 2.7634 | -60.315 | 2026-02-16 05:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b218458b-3f30-3603-89c7-efd647d8b453 | 2.7634 | -60.315 | 2026-02-16 05:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1518a0ad-1189-3710-b553-c4e069ff10d3 | 3.70418 | -60.91133 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cccb10fb-6072-32fb-9ed5-12792dfe5dae | 2.77002 | -60.31545 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 87825723-29f7-39db-a417-ab325a129b89 | 3.90744 | -60.23967 | 2026-02-16 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd316eca-410b-3ddd-8743-ef1f97fef244 | 1.84969 | -60.3306 | 2026-02-16 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d48e95d-3579-3a45-8e65-59afe4611bed | 1.8525 | -60.32648 | 2026-02-16 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
