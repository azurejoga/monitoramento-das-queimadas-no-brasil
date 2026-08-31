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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf1b8cf0-ff76-39ab-af07-67442563b792 | -8.3919 | -44.98554 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2105fada-1972-365f-8e97-23524de709de | -11.25013 | -45.11659 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 4bf65cc5-ca3d-3d1e-bc0d-e8def3c8c68e | -9.19801 | -48.00291 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fa2f6906-0c49-3ced-b419-a02c3a86091b | -13.79752 | -41.12334 | 2026-08-31 16:30:00 | NPP-375 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a311a671-bb41-3e7a-bcd3-530a9e802664 | -11.67303 | -47.61118 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e24420e2-2c91-393d-9006-e80d2fedd085 | -15.24516 | -53.86192 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f77fbb4f-1b00-3c02-a280-9d69435ebd18 | -10.08378 | -46.24838 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 70ce0880-ce5c-31cf-9f9b-e004b927ae14 | -11.19833 | -45.04368 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b741c829-40c4-33bd-8eed-d9b39ed2f9fb | -10.08208 | -46.63041 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 68d8eae1-7657-31ae-b13b-0b168e8e43c3 | -8.8593 | -47.07401 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3571eea7-a974-329f-8a6b-231e10ed5b89 | -12.09705 | -47.25412 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 44074a1e-5ad1-3a70-999d-464a55278ad5 | -13.06474 | -45.18024 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f6df259f-21c7-3b72-91a6-6dc3d5de2b26 | -13.46335 | -51.40784 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 16d51b97-f31a-335c-a04d-3000f7c86f1f | -8.86913 | -47.0794 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 13fa52f0-d4b2-3c34-95e3-261c4cfe7e69 | -14.21219 | -48.64003 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6b94e9d1-d31a-395a-85b1-95283ac6dc8c | -9.47071 | -48.19188 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 92c8177e-905d-3f92-acd5-d09d1f5e6b04 | -10.58746 | -40.12831 | 2026-08-31 16:30:00 | NPP-375 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7461f8e8-3b04-3a26-a3ae-6619f121333a | -11.2156 | -45.11269 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 576e5307-4982-349a-b211-99fd7728f759 | -10.10291 | -50.30096 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fde7818-a5c8-3369-93dc-777e75004dc2 | -11.31913 | -45.194 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| c3107b47-6749-33f6-8ded-c34870941d52 | -8.86384 | -47.07696 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1e211ef5-b108-3ded-8033-b220c95e0b80 | -10.8162 | -50.63501 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e27872e3-06a0-3abe-b121-59e8b048f9d0 | -11.52308 | -45.49622 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a0f4cf93-7c57-39df-91b2-465ced0c1817 | -12.41814 | -42.88808 | 2026-08-31 16:30:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f7e7cf23-4ff7-34b5-a749-290a044b6729 | -10.15336 | -45.75999 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93de16cf-d297-3e4d-ad43-71df6dbf94c5 | -14.66448 | -53.57691 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 44d7711f-44ca-399f-bed8-26950f87c8ad | -14.20054 | -46.56915 | 2026-08-31 16:30:00 | NPP-375 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b1ebd3f9-f823-3a3d-838c-7801bc1c37fb | -10.15713 | -45.75936 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c67616b8-36a4-3a4d-a6b4-a75267132b2f | -11.25133 | -45.09862 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 50552889-521d-3285-abb9-07bed36a53a7 | -11.02951 | -49.69579 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3047f93d-50ff-3b80-9472-6edbde568600 | -8.40967 | -44.98277 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b2709dde-4eea-3016-b495-b549d28faeb7 | -11.08 | -51.53549 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 36049c0f-5dd2-331c-9c80-b84751f11406 | -8.75965 | -46.46696 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 37d622a9-95ca-371c-8db4-530085f19490 | -11.21277 | -46.11736 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e49ea6a3-75b8-3fdc-8eed-91c2aab253a8 | -11.24898 | -45.13501 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 03b8bcd4-a205-349d-9d56-4103bb8db855 | -12.09215 | -45.75128 | 2026-08-31 16:30:00 | NPP-375 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6c987b1b-9e88-3bd3-b8e2-a9cc0fbed4b2 | -10.02544 | -45.56359 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a36ed2e4-5fb7-38e2-9c00-0b435f4ccc67 | -10.5617 | -46.16438 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6907b11a-3371-3a08-b10a-82a78959ca1a | -9.96305 | -46.7781 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3760c14e-8ba6-3cc1-89e2-4929c2ce0ef3 | -10.15502 | -45.74463 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| dec2e0a7-33ce-3d17-b078-663313cc2795 | -11.37254 | -45.2226 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f7dafa8f-7bdd-3dd3-8acf-63a4ef7ab2fa | -11.2126 | -50.61827 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 227242a3-8f23-36f4-9895-598de5b92eb6 | -9.15853 | -49.95694 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dbf0ebfe-9d07-3056-94ca-f7cf7ebab66f | -10.35478 | -49.97312 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 17fcce61-88a9-34d7-9c94-dc841d175a2b | -10.10213 | -50.29494 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 756c50c0-ed5e-3c6b-88b0-0ef0c5379e3d | -10.3379 | -49.95984 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b5ae1418-f276-3248-90ce-6ae05cd19a75 | -10.12179 | -50.32616 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53c065c2-29cb-3e6f-8e55-2ce755e376d3 | -10.10763 | -50.29729 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e248e25-40dc-3c58-a5c9-502b6acec621 | -10.61983 | -48.68523 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4dd9a6f0-3e9d-3178-842b-e8726929ee73 | -10.51125 | -45.04334 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3a7fb76a-c028-366e-9ba3-2c224a447239 | -13.42407 | -51.69007 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 137dd4c8-756b-3c2a-8e34-fb32dc21209f | -10.73706 | -47.98571 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d70c1584-6294-32e3-b3ba-6e08b97c591f | -8.88021 | -46.02548 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| eaa469e2-4c23-3e87-ac8e-4cd9784fc9d3 | -11.19473 | -46.10704 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 47352329-185b-32aa-aeb0-b8d32d2d9cb1 | -12.63657 | -39.11974 | 2026-08-31 16:30:00 | NPP-375 | MURITIBA | BAHIA | Brasil | 2922300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0e24c2c7-da5e-3f02-ba7a-be78cadf7be8 | -8.85678 | -47.08509 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b549f48d-6b70-3577-a47f-d42b80621705 | -14.21993 | -48.65223 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b72a0805-d08d-379d-a578-f8e49318f0f7 | -11.19642 | -46.11476 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 06518527-5f88-30ec-8bab-5b86e97acffc | -10.08386 | -46.61438 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2379435e-6f0e-3147-9ad5-d7c99ba2b344 | -9.67048 | -47.95325 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| f58ad878-2b77-3664-bde1-1fc7bb344e9a | -11.16624 | -45.04733 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 325046df-c160-32c7-af03-f7f4ecee58c6 | -14.65896 | -53.55992 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 08bcfe8c-ca9a-3187-afb5-3629092c7c7b | -8.91316 | -44.17245 | 2026-08-31 16:30:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 753e7be4-609e-3102-aa55-eb2748f48747 | -11.17348 | -50.56322 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 99d9fe49-60e9-33ca-b315-25fe9dd236d8 | -9.6532 | -46.05124 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1e8aea7e-4517-3aca-ab38-a9e475dfe913 | -14.95481 | -54.57761 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1441c780-233a-3cf2-9b56-e1f9c1d88b8a | -9.65388 | -46.05598 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e08c27d2-bb6f-3da3-956c-e77468c0fe9c | -12.56734 | -45.08215 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| db218e7c-79db-31b8-9783-c068ca1f6ef8 | -9.67962 | -50.84898 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f848fd5a-fd52-366e-8228-645bbd45f8d6 | -14.4418 | -49.00343 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 912cb0d6-1be5-37b4-b45d-bd3ec1b2748b | -10.82524 | -47.23222 | 2026-08-31 16:30:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 48797f24-584d-3aea-9bd5-8c448222b3d9 | -10.0217 | -45.56414 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 272386ff-4f55-3c33-9030-3d0ed902f0e4 | -10.84319 | -45.30954 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1825061c-e6a8-3e7e-bdc8-8080b6636657 | -13.93811 | -54.41734 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3c3c0dec-1dc6-3e53-b758-2b662700e97e | -11.22431 | -45.14761 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e5ac8c57-e25e-3887-8152-e2c96576a10c | -11.24296 | -51.25992 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a8601d50-0bd5-3f9f-b4bf-30d3aa80883f | -10.33252 | -49.95844 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1b9a6990-0b8a-3b6e-96bc-34b294630f45 | -9.41861 | -45.67819 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 879be950-052d-3e36-a8d3-45ba950ee89a | -11.32598 | -45.18876 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3cb75f58-727c-3379-af92-78c2849874b8 | -13.01025 | -39.73493 | 2026-08-31 16:30:00 | NPP-375 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1b8f0e2b-fcb6-3d40-b164-750faec37f8e | -10.04289 | -48.68077 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6af95303-c9a3-38a0-957a-28d61559edd6 | -11.1957 | -46.10971 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 358200e2-e73c-3927-b3d4-abb34f8bb690 | -10.40886 | -45.08423 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2dba222e-c4d1-3082-8921-312b21e99365 | -13.46886 | -51.41319 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ddaefdaa-b277-38c6-893d-58d34e07395e | -11.19796 | -46.10138 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 218eb1e6-469c-3bbf-88af-0f3fba53cc26 | -8.37746 | -45.76281 | 2026-08-31 16:30:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ac644676-fa7e-37a3-82df-cad886c74697 | -14.79166 | -48.75047 | 2026-08-31 16:30:00 | NPP-375 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f134d5c1-c447-363d-aed4-41e48e48f08e | -8.93371 | -45.03028 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cfd759b4-8854-3004-8a94-8c97f68521d8 | -10.15655 | -45.70159 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 605d44d2-5a1f-3d1b-835d-b0afeeb28629 | -12.38248 | -48.1646 | 2026-08-31 16:30:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f8854182-94d7-3260-85e3-47114930a11d | -8.86962 | -47.08296 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0cd23bd4-88ee-3445-a51f-3e8470eb48a1 | -14.95134 | -54.58287 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1f5e5962-f485-383d-a96e-890a19d421b1 | -9.68479 | -47.89711 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 23694ee1-6fa7-33c9-89e8-6f37c35011a6 | -11.23696 | -51.25697 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41bc779a-673b-3994-ac5d-65be7e6071f7 | -11.32842 | -45.20613 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 592c9736-e272-3861-811f-ad64ef8d9e99 | -10.33826 | -49.96356 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 536076d0-5dbe-3805-aecb-6d64951af1e4 | -9.89743 | -46.62812 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 386892db-4796-3605-9e85-802200ee0e22 | -12.09681 | -47.18875 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 462eb773-6ee8-3f13-a445-33322d564560 | -10.05823 | -48.69425 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1778dc9b-138d-3dae-8fb1-994782f934af | -9.66394 | -47.93751 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README118.md)
