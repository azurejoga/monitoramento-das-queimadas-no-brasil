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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bf4db2b-c3e6-3161-841a-903898ee97cc | -17.75945 | -52.42965 | 2025-05-09 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fdae4b8-f81b-3e3b-9701-58c4d875b093 | -19.0554 | -53.45527 | 2025-05-09 04:42:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 294f02ef-e806-3a7e-a66f-1f2310dd5557 | -21.35914 | -48.73767 | 2025-05-09 04:42:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d54e3e3-e01f-3df9-8632-e3b2d8531827 | -15.3676 | -60.17519 | 2025-05-09 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8111d91e-0456-3274-a586-d6303328c520 | -20.76482 | -46.76848 | 2025-05-09 04:42:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1aa5a5c6-5c58-3387-ad18-b26c65ed4f7a | -19.84645 | -54.22521 | 2025-05-09 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fad4adeb-ba30-3297-bf41-0f3007255ed3 | -21.241 | -54.6015 | 2025-05-09 04:42:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc59d84b-41a7-3a3e-9a67-68966926d924 | -20.27415 | -54.63732 | 2025-05-09 04:42:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 050b0f2b-773d-322b-8a27-66ad797a5726 | -21.0565 | -55.99791 | 2025-05-09 04:42:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f6a913c-d78f-3ca7-9d20-ea5491518c6f | -15.36315 | -60.17118 | 2025-05-09 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0bd52a-9ecf-3f50-b351-82f45400d1b5 | -17.52985 | -52.11652 | 2025-05-09 04:42:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b68fa9c9-9990-341d-99a6-bcb3900bbbea | -20.06107 | -49.36245 | 2025-05-09 04:42:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fcae897b-b871-32fd-a9b6-5f319b66219e | -19.8437 | -54.22078 | 2025-05-09 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d940488d-c01e-3dc5-8b78-eb2925730021 | -17.57955 | -47.48803 | 2025-05-09 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41b7775d-db37-378c-8d04-67440459f4c2 | -23.98573 | -48.91806 | 2025-05-09 04:44:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d4ecd49-686b-345e-a724-51bbfb1d1bfd | -21.78466 | -52.74632 | 2025-05-09 04:44:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5632b0d7-3c89-3a67-b94d-77409a5e97eb | -26.1965 | -51.5864 | 2025-05-09 04:44:00 | NOAA-21 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 264bdd0b-b1bb-3b52-b39d-6ce9b5cde423 | -25.19451 | -49.32819 | 2025-05-09 04:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4435fbd-15ea-3024-b90f-6d00b55d74c4 | -21.77837 | -55.31635 | 2025-05-09 04:44:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80cb6af-3d02-31b7-9c7c-354f14612b78 | -22.99992 | -52.44201 | 2025-05-09 04:44:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2e2768b2-c94b-31fe-a306-4b53aac4b5b4 | -21.78739 | -52.7506 | 2025-05-09 04:44:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ca6839f-c14b-39ec-be95-f0adbe8352c9 | -22.31743 | -55.16947 | 2025-05-09 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fccdde78-6148-3719-863e-0d09e4ce16dc | -24.28109 | -48.55259 | 2025-05-09 04:44:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88e64317-dda5-30f5-9baa-8cb479071724 | -23.33293 | -46.95942 | 2025-05-09 04:44:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 31f61e41-19cc-3576-b706-66d828b95574 | -21.78796 | -52.7469 | 2025-05-09 04:44:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bdafba5-601b-31a7-9b35-305bbc4220b1 | -24.53779 | -49.06357 | 2025-05-09 04:44:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8bbb1646-134e-3ef8-8881-a77e2675cdcd | -24.28042 | -48.5581 | 2025-05-09 04:44:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6de264d-bdb1-395b-a256-80ac9530ff3f | -26.09944 | -50.17265 | 2025-05-09 04:44:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d48b370d-ebca-32c8-9df4-42658f8eb23b | -22.54062 | -48.81193 | 2025-05-09 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e874e3a1-5d44-39b7-88e4-de7eeed8f2bb | -23.34088 | -46.77517 | 2025-05-09 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14b9d7f1-2681-3748-96bf-4c727e58b556 | -21.78408 | -52.75001 | 2025-05-09 04:44:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94a7337d-8f9d-3ebc-9943-27b677716405 | -22.67155 | -49.82734 | 2025-05-09 04:44:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a23b1cd4-e8cf-3658-951e-bfc4786552a0 | -25.1907 | -49.32749 | 2025-05-09 04:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ee4bf54-0421-3c99-a299-38f77c6b5292 | -26.09778 | -50.1741 | 2025-05-09 04:44:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| acd50e8a-d6de-3a58-90f6-fa18b6aefec2 | -24.93314 | -51.91621 | 2025-05-09 04:44:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| cf0ba950-0aa6-3a1e-97aa-6abbdfc2bc3d | -23.40541 | -46.55806 | 2025-05-09 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 46b9d532-a58b-3594-977e-134d6a7b600c | -25.21215 | -50.71001 | 2025-05-09 04:44:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e288caee-9de5-31b9-803d-6a10cb7fecd4 | -24.93257 | -51.92021 | 2025-05-09 04:44:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| fb21995b-c5c4-3112-b34e-57cd5dbca9d7 | -21.54143 | -55.52909 | 2025-05-09 04:44:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c71ea65e-6e4a-3368-a1a1-092f93efc431 | -24.09488 | -48.96984 | 2025-05-09 04:44:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c49c2306-1be0-3c0f-bff4-88aa191315eb | -25.4949 | -50.74944 | 2025-05-09 04:44:00 | NOAA-21 | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6391ec7e-8f02-3933-9070-1dfde942ae6f | -23.59472 | -47.44006 | 2025-05-09 04:44:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 934baf08-5d69-3c40-ba5a-c978a3d8fd80 | -10.67027 | -44.35946 | 2025-05-09 04:49:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 7e6c4c5a-4a55-3305-92b2-152800378a8b | -8.07077 | -43.10507 | 2025-05-09 04:49:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| cbe30eb6-c1a1-314f-a3fe-42169d20072a | -6.69731 | -42.13646 | 2025-05-09 04:49:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 1e04daea-2464-3040-a14f-6bed365083fd | -8.07713 | -43.10138 | 2025-05-09 04:49:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| febf757a-393b-3498-b408-b10340bc09b6 | -8.07143 | -43.13474 | 2025-05-09 04:49:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| bf44ba7d-a550-3a3a-9225-04825c94c309 | -8.06476 | -43.13869 | 2025-05-09 04:49:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.7 |
| fec58768-985b-368c-ae59-6b7af1658b64 | -8.07 | -43.1216 | 2025-05-09 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 0109139e-8e23-309d-8b34-c2fe2e27128c | -8.0889 | -43.1196 | 2025-05-09 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| fc9a74d0-eee5-367d-8d5b-f092a99699b0 | -8.07 | -43.1216 | 2025-05-09 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 1bcd27f4-95a8-37b1-a8f6-cdfdc21844a4 | -6.96256 | -42.78296 | 2025-05-09 05:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e60272b-7cfc-32d5-9a18-f361aebd4ce2 | -6.70178 | -42.1352 | 2025-05-09 05:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 28f4cb2f-e905-3cdb-8eef-6ed91ced98e9 | -6.61826 | -48.01016 | 2025-05-09 05:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8db5bf2a-94ce-3d3e-8300-4286a74ef4e4 | -5.16478 | -45.10398 | 2025-05-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08665c79-049c-32f0-bc79-33c6c4206c29 | -5.17065 | -45.10472 | 2025-05-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc5e73fa-fcb4-3deb-9fb7-fb18dba98c15 | -6.69735 | -42.13926 | 2025-05-09 05:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 97eeb228-fb93-359b-b21c-d8412942c0eb | -6.69826 | -42.13227 | 2025-05-09 05:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 919e94c8-8d9e-3e43-80b7-f60e88a156b8 | -6.96948 | -42.78394 | 2025-05-09 05:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3bceea24-6f07-3fa6-b888-d76c63ca8b1a | -2.5852 | -51.92314 | 2025-05-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61d3b594-1c80-3046-aa85-3ff517766c65 | -6.69365 | -42.14132 | 2025-05-09 05:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 476e6aad-64fa-31d5-b8a9-673fb9f32444 | -6.70084 | -42.14204 | 2025-05-09 05:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 14fcc38b-b06f-3b15-a932-3985e327ed21 | -4.00641 | -56.10964 | 2025-05-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 722bdafb-7948-33f0-ab68-9f17c30b4ea5 | -7.07995 | -44.37317 | 2025-05-09 05:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef676763-2f41-3603-b0b4-8ba1b6c4abe6 | -3.46369 | -49.17757 | 2025-05-09 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71860812-70aa-36b1-8470-12864b6b4dd5 | -5.16419 | -45.1081 | 2025-05-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 021956f6-f568-30e1-83d3-23e68b224fef | -7.21341 | -43.11763 | 2025-05-09 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5afb402-5c4e-3248-830b-cda812e16d25 | -4.13033 | -54.89925 | 2025-05-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4ea40d3-4899-3249-840b-784b842eae25 | -4.00164 | -43.24547 | 2025-05-09 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93700170-349b-3a02-8b69-b4ebd31b14ab | -6.6194 | -48.01121 | 2025-05-09 05:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16c9d763-538d-33b4-8158-b6a100d13054 | -5.16538 | -45.09977 | 2025-05-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f3fcbfa-f0c5-39c7-b685-f7df3f631953 | -3.99517 | -43.24445 | 2025-05-09 05:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c98c69b-7213-3613-9fb4-b411c1eddc6a | -7.08628 | -44.37375 | 2025-05-09 05:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e1b2a48-0b66-386c-afb4-a5e4315ee90f | -12.12005 | -47.98723 | 2025-05-09 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d878b0f-5f67-3073-9f06-09364849ff30 | -7.89165 | -61.46398 | 2025-05-09 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4765f8b1-8619-37a0-9a89-df76617cb887 | -11.35871 | -55.12772 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2f4de56-33bd-319d-8eca-efcd65409101 | -11.56233 | -47.6154 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b31b8b1c-af3f-3819-94c9-bbd61fa3b7e8 | -10.23384 | -59.24078 | 2025-05-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d79d19-36be-399f-935e-f21f8d2444fa | -12.11473 | -47.98645 | 2025-05-09 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a89160f-d60e-390e-95f1-ab3e2dbb1fe2 | -11.55761 | -47.61722 | 2025-05-09 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b8d65b4-4182-378f-9482-eb712f72a339 | -12.35061 | -52.48631 | 2025-05-09 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f49dd3b-9eb3-3ad8-8315-3329fc91403d | -11.38819 | -52.94001 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5bf5a16a-56ff-34a7-8ba4-498896c10487 | -11.91491 | -54.39939 | 2025-05-09 05:06:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 733ab0c3-9e84-3509-a0cb-b519e8f4c014 | -11.38749 | -52.9447 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 247372a3-42b5-3aa1-95da-3076fec4d0da | -11.38406 | -55.11546 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15baf632-f19d-3e15-b26a-9bdff32f835f | -10.96978 | -44.43457 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed99814d-255b-3b5d-a447-641b9342e2f1 | -11.62961 | -54.93904 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6095d62-5390-316b-a853-da5e9c43278c | -10.97494 | -44.43524 | 2025-05-09 05:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd01a7bf-3c61-33d8-9db1-e3f364a90ce6 | -11.62615 | -54.9385 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9d80e6a-438c-3664-952c-54d4d712c9e6 | -11.47374 | -58.67045 | 2025-05-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4b15d49-45d0-3646-8225-734068d4397e | -11.62124 | -54.93805 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f171c9c0-c622-301f-af21-b731e5ca2a4f | -10.07874 | -54.33043 | 2025-05-09 05:06:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0619dd3-b9fe-35ad-821d-440ce4f76e73 | -11.39112 | -52.94235 | 2025-05-09 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 62f3c885-b95a-3928-aa1f-5f662ddc2dca | -7.94291 | -50.59412 | 2025-05-09 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6526870-56dd-3287-bc19-53ae8e214f23 | -9.42332 | -62.11464 | 2025-05-09 05:06:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39338d31-754f-3343-8601-ba5d9c25b07d | -10.23032 | -59.24021 | 2025-05-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 077eb728-dd83-3d0b-b249-657833a41a0b | -11.47388 | -58.67164 | 2025-05-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c46415b6-2c4f-3cb1-8ba7-fce97702b318 | -11.62816 | -54.93914 | 2025-05-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24fc3a96-5de5-3a2e-be98-f15758dac769 | -9.61853 | -62.06541 | 2025-05-09 05:06:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9693543e-493c-3d6c-9cd9-21a2783d51c9 | -11.91137 | -54.39884 | 2025-05-09 05:06:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
