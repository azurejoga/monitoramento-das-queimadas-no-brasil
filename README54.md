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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45c949dd-7298-3f86-a60c-0f419b908aa9 | -12.24346 | -47.85022 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14c249ef-6b3e-3d85-8e3d-1495ed3b8695 | -12.45463 | -45.52114 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 95df52c2-7054-3b38-be65-c61d32bbf740 | -13.62694 | -48.68439 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16dffa0a-459d-3099-b798-ace9a8ee0f99 | -14.65276 | -48.34033 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4df255f6-4bc1-36d6-9445-e494582f6567 | -13.30293 | -48.12186 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f8df92a-2de1-3da9-984a-b6adf4dde591 | -12.40481 | -51.10068 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9506dc61-edd3-34c9-85ae-5733840bbc52 | -13.3161 | -48.07569 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13a85595-ab6e-32b2-9a8f-0c0d98347a91 | -14.92846 | -46.8394 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 382377e5-0745-356e-9b3c-1d1bdea3214a | -10.6215 | -48.67378 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45a469b6-574b-33f3-bcce-3ea1819f37d6 | -13.3801 | -47.54465 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eea65f77-4402-3ea1-8558-418c96d6e7d1 | -12.26847 | -49.19887 | 2025-10-05 03:55:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cc9d450-43b0-35ab-bfd7-7b986e704035 | -12.20558 | -47.77917 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 506c065e-83da-3bb9-8c3c-c27d07452a60 | -14.68464 | -48.29592 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eef6a5d6-a6ff-30ad-bc18-266caa5c3a18 | -13.09565 | -47.85044 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c432313-31d8-34e1-bf90-6e33237c31a9 | -10.74357 | -47.89027 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 189b373d-ae97-37c8-a023-e7e3f593d498 | -13.31909 | -47.78972 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd8aedae-fbcb-3175-847e-b77760880a52 | -11.88218 | -44.97337 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ea78cce-2bbb-339e-9808-de36b53f4fc0 | -13.44094 | -47.27018 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02d7cb4d-b78a-3835-b196-bbe0ac0c3fc1 | -13.72694 | -51.31297 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ababa0f8-0717-3f1e-9662-74c16a94b4f6 | -13.81623 | -48.05625 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec2b01e2-68fd-34dd-a60b-99349e4b7de0 | -11.09183 | -47.74629 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 027dfcc1-2e19-3872-9150-331a861e035b | -16.26558 | -47.10698 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6da1f5b6-a48c-3e6a-b572-19217b656342 | -12.69852 | -45.85611 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caf766dc-06b3-331d-bf00-6b5f06281c6d | -13.11462 | -47.83019 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03502c36-7e55-3474-aed3-a4e1807169b7 | -12.45884 | -45.522 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695d95e4-889e-378e-ac7f-c00227c92e37 | -14.68478 | -48.33273 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f7f44e0-ee11-3b9a-9072-50b0d74e2f2e | -14.33518 | -47.68826 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2fdb884-4a05-35d7-a40e-6fe1f3535f74 | -16.33752 | -51.47626 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ab75cbfb-dc14-35c3-8945-b604392ed843 | -13.35671 | -47.59026 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5afaf8a-6d0a-3fec-8a82-2dab1c76175e | -11.87873 | -44.96883 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 037b38de-ecbc-398c-9521-80219e2dea78 | -14.75226 | -54.66572 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d20d0627-9a88-31b7-ae87-279d9863b9e5 | -11.83227 | -45.08616 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ea61d995-1fd7-37d1-a4b5-5337be3ef150 | -15.69375 | -46.27546 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0221d79-e6e9-3fa3-8c84-ac7cf970125f | -16.38847 | -52.15715 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42b2d43e-76a1-3bcb-bffa-3a04596a2524 | -13.31524 | -47.78357 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d3fa92-5f92-38cf-b92a-623dfceb46e0 | -12.09925 | -45.17677 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a43b79a-2351-3845-b964-43ec463d1145 | -13.58916 | -48.16257 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| be507517-1434-3905-974f-b8f6d532c9c6 | -11.23682 | -47.79579 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cae8c27-c020-34a0-9e41-6a9da16b8885 | -11.53333 | -47.67188 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f602d4a8-cbf7-3a77-b838-89f1ca6b300f | -13.7395 | -48.07644 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c103779f-2e74-3235-a9b9-27320a881aa6 | -13.10978 | -47.82904 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfc3348d-250c-3264-9842-83bad17cdcc7 | -10.4507 | -48.37643 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a306b1d-1573-3d3b-8d89-cfcd16ecccf2 | -12.88986 | -47.31511 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef7f67e3-6555-33a5-930f-8c9689bed65a | -14.41476 | -46.17948 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4878dd41-0c88-3679-98ce-08526265dba7 | -12.81351 | -50.53967 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2805f818-46bb-3a0b-8354-525bb7545bc2 | -11.67419 | -43.90051 | 2025-10-05 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 409727db-d640-3d70-9688-8a7619fd948f | -17.25468 | -46.80428 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e07052ea-93c3-3bdd-a976-3be5cd1e31ee | -13.09685 | -47.84404 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc107359-bbda-341b-b3e9-9b938d4731ae | -11.06884 | -47.90082 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eed177c9-e8cf-3aef-9465-a88d4c7b8ca2 | -11.0952 | -47.75175 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b201446-5434-328a-95e0-58208b3344bb | -12.22592 | -47.83424 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a50efc9-a439-343b-978f-fbe19ac38368 | -15.51631 | -46.84657 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d18a4e7b-d199-36af-bfae-66dcf5391d8b | -12.58847 | -48.12892 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5c8d410-37f1-3a38-859f-61bd4669a82c | -13.24718 | -48.48771 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 760d788a-5492-3f00-b5ca-82484da49882 | -15.12204 | -45.73402 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3cf8a7-4f89-355f-a00a-34da2e79c28c | -14.65124 | -48.33819 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a677de9d-69f2-3bf1-a80c-a80ecbdc0809 | -12.08535 | -45.15108 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e11e4c3a-e1f5-359d-ba90-3f1f0eaa6aa0 | -10.98817 | -46.66605 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a588d5fa-78f7-339b-a4e2-b0d80c2de30e | -10.74136 | -47.90192 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 185210f0-d7ff-3ecb-9874-dc2edc60d6db | -12.13 | -50.92375 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 188dd735-a647-3058-8d8d-303274cd36ab | -12.9814 | -51.01567 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0116f0a0-d22e-3388-98cb-843fb88a3982 | -13.11476 | -44.0769 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbb89ed4-e404-3a5c-b681-79b76872b080 | -10.86881 | -45.41227 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bea1580b-45fb-371b-a7fc-6b2052a96ea5 | -12.46097 | -45.51001 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64546ee6-c762-3708-b5de-098ac51616e5 | -14.68516 | -48.35667 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8c0df2b0-30a0-3783-9b8c-7056e4733505 | -11.23226 | -47.7923 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3eda39d6-c528-31ff-bd54-58486385e205 | -11.00116 | -46.52785 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94934719-43c4-3a5d-b754-476c7b30fae1 | -16.57193 | -46.35901 | 2025-10-05 03:55:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccd88f07-b310-39ac-9ac0-96136e4b0fe6 | -13.26305 | -47.20101 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a99aef6-9920-3677-ba16-990f2abf3ade | -14.66341 | -48.31227 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5d0bab4-a7f9-32ee-9f19-9037ffcbbd97 | -12.41622 | -51.10906 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ddf62a3-ad71-3326-a5a0-4a6790e8abf4 | -15.51928 | -46.87875 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57650eda-0bad-3b98-892f-b5a7df823a29 | -12.97227 | -50.99946 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0f88ad9-c2e1-3eb3-8d9b-bf488a3e4871 | -14.89084 | -48.26271 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 622af4a9-466d-3b49-9f95-ce0a8e05c3eb | -10.45457 | -47.812 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01c6621f-692c-38ed-8d1b-7703ab41c9d2 | -13.35594 | -47.20867 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1e27215-3f89-399f-8f07-23af6046dab7 | -13.81541 | -43.17014 | 2025-10-05 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1217447-da00-316c-805c-69a2a3859ae5 | -11.11935 | -47.2089 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 386e81b5-3cc3-3d9e-8c09-3d51bdc9b81b | -14.6854 | -48.30375 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cba0c63-a30a-372f-a44c-0efa2c0f3485 | -14.27135 | -45.86698 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f60c22d2-2307-3f78-b804-4df79c0d8989 | -14.33299 | -47.69991 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 836464e6-27e3-3de4-a78e-bb861ff89a42 | -17.54966 | -46.76694 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1640a754-3b43-3fde-9e90-fd8b75024631 | -13.30644 | -47.7771 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2423e474-7bab-3ba4-b38d-37f67784db50 | -16.33849 | -51.47174 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb783408-7c46-3d8d-bd39-a6db08375d19 | -15.91294 | -48.82383 | 2025-10-05 03:55:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56dc85cf-91c1-39a3-8c75-d059f4c7e655 | -14.28885 | -45.86621 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a1427ca-d2c2-3379-ab47-c7d25e2c19e6 | -11.81844 | -45.0915 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d34318-c9bd-3110-8825-65209c449dc5 | -15.74596 | -46.27658 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 559cdf64-5156-377d-8199-2b550afcdf59 | -14.27973 | -45.86863 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb57e86f-70ce-3be2-9c71-fdad00ef7620 | -17.99917 | -45.00457 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cedd6f2-28c2-327f-92a6-65b503b7e06b | -15.29771 | -47.9507 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b302c8c2-e81c-36a2-9949-a2c14aac2732 | -10.78822 | -51.00217 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 25988538-a763-3637-bc65-e91db1e23681 | -14.97135 | -49.97486 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65bce6f3-1d49-3bb0-93d4-1c7c6441b26d | -10.93982 | -47.08815 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fc66492-8e35-3695-b102-93b8f8e74dac | -14.32668 | -47.68142 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 811586dc-bf1a-3a67-97a2-5cc2ada00190 | -12.99597 | -43.99812 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd14634c-10ad-374b-911c-05c36623ca34 | -16.97405 | -47.27048 | 2025-10-05 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b529600b-63e7-3b5f-8d5a-9730c380ee7f | -14.32279 | -47.67613 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 53b36c37-8bba-31a6-bf6f-0be45c2a3cfb | -11.00168 | -46.51487 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c1a869f-bdeb-3b6b-ada3-e15d08565308 | -13.45314 | -47.26832 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README55.md)
