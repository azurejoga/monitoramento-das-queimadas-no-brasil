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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27a73480-6e5d-31fe-bafa-b58349df0401 | -3.49418 | -48.03563 | 2026-06-08 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2a1d64be-a05b-3b14-8c21-48e4df4c93ef | -2.73645 | -58.18936 | 2026-06-08 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c16cd35-46eb-3ba2-bdef-4f0b1499500d | -3.49267 | -48.03359 | 2026-06-08 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37627dc5-0359-3dca-8e50-d2a8e46cdbfc | -10.85982 | -53.73803 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f0b8773-055d-39e7-8c7a-b155cf4ca434 | -10.84499 | -53.75134 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d0f3cb-72c2-3dc4-a050-1aeee465257c | -11.54196 | -56.33434 | 2026-06-08 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ae1eee2-c1c3-3f0f-a10b-e6a96a0f1814 | -9.09228 | -50.60807 | 2026-06-08 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fef66323-1758-30b9-99f7-09176457d612 | -10.92276 | -54.11333 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f585a9e-46e7-3b93-8e41-226ed58c13b5 | -14.73574 | -52.68082 | 2026-06-08 05:27:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eff4268-623e-3aff-905d-632d44813447 | -10.11875 | -57.76087 | 2026-06-08 05:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0cca3f3-dfd3-30c9-a005-9eb61ea3d3a0 | -14.73533 | -52.68443 | 2026-06-08 05:27:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2438b71a-4455-3d53-89df-881144eca9ac | -11.54249 | -56.33063 | 2026-06-08 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f978820a-da32-359f-831c-c9e5cb771bb4 | -10.84866 | -53.74771 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f4a1559-81d8-30a2-8613-afcdea907d1d | -11.51151 | -56.1287 | 2026-06-08 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a409f0f6-bb8f-314a-8499-c1e053166dc6 | -10.40366 | -64.44968 | 2026-06-08 05:27:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e1aaccc-a1b6-3ef0-acf0-0541d9912ff9 | -14.33147 | -58.46665 | 2026-06-08 05:27:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 20323082-fb10-3ab2-a65a-e1a3013f9d2c | -11.74281 | -57.83246 | 2026-06-08 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b349b1cb-7635-37bc-bc22-2ca451cc5425 | -10.85423 | -53.7429 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49f193aa-ea67-39c6-93e5-1d68aa538a5b | -14.33211 | -58.46207 | 2026-06-08 05:27:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55bf6554-a2b8-3799-9656-309ce2bbe627 | -14.33341 | -58.45285 | 2026-06-08 05:27:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 528d1003-fc60-3be6-b807-f4cf5780f11b | -10.12245 | -57.76143 | 2026-06-08 05:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96603537-9ec2-3d56-953d-be4c80cbd83e | -11.89679 | -57.78187 | 2026-06-08 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cea79cc4-90af-35bb-adb0-f10bac50ec08 | -14.33276 | -58.45747 | 2026-06-08 05:27:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c3fb02d-f28a-3537-a6aa-834aa28e79ce | -10.82727 | -56.60305 | 2026-06-08 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdb10a6e-78a8-386f-add2-5ffa4f8f8f7b | -10.84937 | -53.7422 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02159b25-18f5-3b03-a468-8055a7eee3e5 | -11.89917 | -57.76579 | 2026-06-08 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76a0f47-6e75-367a-82c2-6f5df22e33d6 | -12.07002 | -48.42378 | 2026-06-08 05:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0057e5d-ddd2-3409-be49-076b1749637c | -11.58805 | -58.50959 | 2026-06-08 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 207c88ff-da03-3d61-9174-16abab0eb55d | -11.89654 | -57.78452 | 2026-06-08 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9e1293e-fa7a-33d6-a14c-a28c12c0f883 | -11.89955 | -57.76311 | 2026-06-08 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b008684-f415-3403-981d-640332b6c211 | -11.30064 | -54.88251 | 2026-06-08 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 811d7a01-730d-3d49-9ab8-82947a89db13 | -10.85495 | -53.73736 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d564fe0-9cd6-382b-a632-005bf79f7c01 | -10.84575 | -53.74583 | 2026-06-08 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 077d6323-3426-38ac-a914-530447887921 | -12.06931 | -48.4302 | 2026-06-08 05:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b2e7434-8395-3f9d-b3e2-a7676b34c273 | -11.84567 | -52.51205 | 2026-06-08 05:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e0208db-6e01-3548-8804-bdcfae060421 | -10.40434 | -64.44559 | 2026-06-08 05:27:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6534a51-bcce-38d8-a6c0-17e98ce81699 | -21.9888 | -57.60789 | 2026-06-08 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edb50cbd-5457-3b76-b1e3-8b95c0e9d2dd | -16.26814 | -60.00096 | 2026-06-08 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc73349f-97e7-345b-b73a-8226c7231b15 | -21.98823 | -57.61273 | 2026-06-08 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57e211aa-9b6e-3751-8475-4b48bb53b6e0 | -21.99261 | -57.61328 | 2026-06-08 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 069968bf-6090-3224-9941-763044bf5611 | -21.99319 | -57.60843 | 2026-06-08 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cd7b929-595a-3e6a-82b0-01a0f5fbb617 | -18.46589 | -54.70439 | 2026-06-08 05:29:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3567923-16f2-3d7e-8084-d63a425e9fff | -18.46083 | -54.70375 | 2026-06-08 05:29:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4cb9c06f-5ca9-34c2-bc64-877b192ed45e | -16.26754 | -60.0051 | 2026-06-08 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef638235-a554-3d32-9959-c165f5f81da5 | -21.98384 | -57.61226 | 2026-06-08 05:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf28e72e-561d-3da7-a74f-81052a6b0982 | -6.98301 | -42.87783 | 2026-06-08 05:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e5984b5f-5943-311c-8b6c-6a0008629a6a | -7.5991 | -72.78816 | 2026-06-08 06:14:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66233e51-78d1-36e4-ad95-3ef52dc8b768 | -5.89505 | -42.66484 | 2026-06-08 11:32:00 | TERRA_M-M | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3b83ae1d-2a1e-3c84-87fc-65fd822aeb57 | -6.78339 | -39.18986 | 2026-06-08 11:32:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 13f4f28e-13c6-3ac3-ad44-add24f125e03 | -6.76435 | -45.00742 | 2026-06-08 11:32:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5f2bd6b0-e3fd-3646-aa6b-03f031eddde6 | -6.98091 | -42.88201 | 2026-06-08 11:32:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ad8551c5-bbd7-3006-9340-3867a9679528 | -17.56607 | -46.55354 | 2026-06-08 11:34:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1ea645f9-3b67-353f-80c3-7da99a9feb0c | -17.15696 | -45.05128 | 2026-06-08 11:34:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78b7f6d0-7299-3436-92f5-6f815a8b0b1d | -12.05366 | -45.57044 | 2026-06-08 11:34:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8513e122-7a93-334d-aecc-849ceb42dc99 | -12.14882 | -43.58683 | 2026-06-08 11:34:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f682c790-4761-384a-9a8f-12b2f950bd64 | -7.9043 | -47.09288 | 2026-06-08 11:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9a77533b-25d8-3945-a649-63e51e2d01a0 | -12.13994 | -43.58553 | 2026-06-08 11:34:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 81431fef-c042-34ef-b588-d691a032f670 | -18.46079 | -40.3827 | 2026-06-08 11:34:00 | TERRA_M-M | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e10770ac-a2b6-3bd0-ae56-952c521f7fab | -17.16592 | -45.05272 | 2026-06-08 11:34:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d858a319-54e2-3fd6-8242-91a863cfe6b2 | -11.02457 | -44.31677 | 2026-06-08 11:34:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ec8c41e7-2139-321b-80fa-37106cd73cb9 | -7.90512 | -47.10334 | 2026-06-08 11:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2a820aa6-28a9-3c3b-b3c2-0e3885f9a127 | -11.72347 | -44.58171 | 2026-06-08 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 721f77a3-74e2-33b3-b889-6929214ee347 | -19.00437 | -40.26609 | 2026-06-08 11:34:00 | TERRA_M-M | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 7b48e404-d0c3-3e04-ae3d-e776dba6c804 | -17.16451 | -45.0622 | 2026-06-08 11:34:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 9ba1c2af-434b-3298-8c50-d6f9dea9452c | -19.12419 | -40.17177 | 2026-06-08 11:34:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| dff078e7-f6ce-3f93-b4d5-61c48c1da95f | -8.99654 | -40.3796 | 2026-06-08 11:34:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| c0d85a68-4af7-3fac-bc4f-be14ed81c4ab | -16.30926 | -43.71704 | 2026-06-08 11:34:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20e5ac8b-8659-35cd-bbee-dc26f72ff789 | -9.07941 | -40.25304 | 2026-06-08 11:34:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 038f0efc-4d3a-35fb-9dba-f1317c375b8d | -7.90754 | -47.08743 | 2026-06-08 11:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 513bf7df-fac4-3895-b3b5-0f62d408e0e2 | -17.15556 | -45.06076 | 2026-06-08 11:34:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 610e0138-fba3-3130-a714-16da02de46d4 | -20.98118 | -44.3876 | 2026-06-08 11:36:00 | TERRA_M-M | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 73c2ee89-eb38-371f-9c10-6879e61c340d | -20.9825 | -44.3782 | 2026-06-08 11:36:00 | TERRA_M-M | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 179ecf0e-494b-33b4-87a0-0a6467027292 | -22.91806 | -48.67792 | 2026-06-08 11:36:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| afdbbb71-b3d4-3fa0-b3af-6f32d5953940 | -22.91598 | -48.69037 | 2026-06-08 11:36:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 40fb65c1-e237-383b-9089-686413c2c26c | -19.33333 | -40.57182 | 2026-06-08 11:36:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f2e2b854-b2de-3e6f-8667-8ad7df0e53e8 | -19.33176 | -40.58457 | 2026-06-08 11:36:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f74c0ad7-47b1-3737-83aa-e1ee5dfb7a05 | -14.287 | -57.5434 | 2026-06-08 12:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2a9076ac-120e-3891-ac25-9b16d9b70145 | -14.287 | -57.5434 | 2026-06-08 12:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 5511b7c1-f4e6-38d0-bf7e-77ef3c23ed67 | -14.287 | -57.5434 | 2026-06-08 12:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3bcbb510-a5a7-3519-9509-6a2e8371671c | -14.287 | -57.5434 | 2026-06-08 12:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 1ae67a58-437c-3a34-a92d-18652db72c7c | -14.287 | -57.5434 | 2026-06-08 13:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ac32fa8b-41bc-3ce6-8fa9-b287a29cd90a | -11.451 | -46.6846 | 2026-06-08 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6d3cb10f-1865-325a-890a-ab950f4ee0c1 | -11.451 | -46.6846 | 2026-06-08 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 84d66010-3696-3aa8-8874-e344c1badb6b | -11.8734 | -61.0479 | 2026-06-08 13:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| e27789d0-7377-32ee-98bd-9bf6140dc727 | -12.50621 | -57.19706 | 2026-06-08 13:12:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 839ce715-3601-3537-ac2c-0c030636df37 | -11.8782 | -61.03859 | 2026-06-08 13:12:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 07788a88-0e90-34d5-a27f-3dff2447751d | -12.50844 | -57.20434 | 2026-06-08 13:12:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 63833c61-05bd-3f84-b985-d9c7b68bb435 | -14.2914 | -57.54421 | 2026-06-08 13:12:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 78983445-0eeb-39e7-b0f1-0f56e733445f | -11.88052 | -61.01916 | 2026-06-08 13:12:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| de3ccde0-7983-3672-824b-5169e51e22ff | -14.29407 | -57.55104 | 2026-06-08 13:12:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d400377b-6f73-3304-bc62-c662b69190bd | -11.86554 | -61.03696 | 2026-06-08 13:12:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5d61c789-1cd7-306a-ac40-518fad9c0358 | -14.29789 | -57.51063 | 2026-06-08 13:12:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e7cbdb80-63c0-3203-96bb-c58f4031726f | -8.943 | -45.6573 | 2026-06-08 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c6071193-8ca2-38a8-9b72-81b74bc0ffde | -11.8734 | -61.0479 | 2026-06-08 13:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2655cb3d-622e-3164-ab46-ff659e601b57 | -11.451 | -46.6846 | 2026-06-08 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 641a99e2-89d7-31b8-bbd9-abaeab9a2b10 | -8.943 | -45.6573 | 2026-06-08 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| e8118b48-b5ad-323d-829b-71a2bd4745f8 | -11.4319 | -46.6871 | 2026-06-08 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 3993c39a-ea36-3f52-87e6-eecc7b5c39d4 | -8.943 | -45.6573 | 2026-06-08 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| b628eff7-d750-3142-928d-904fc3063c13 | -8.9433 | -45.6346 | 2026-06-08 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8fcf6cb3-90bf-3d23-a052-60a92706a683 | -6.7686 | -45.0051 | 2026-06-08 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |


[Clique aqui para ver as próximas entradas](README6.md)
