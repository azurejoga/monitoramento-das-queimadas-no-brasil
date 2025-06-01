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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c70b23d-0650-394e-bdb7-f871e0789f64 | -14.7006 | -45.092 | 2025-06-01 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1e8ada27-cb36-3a1a-892a-6d102579cc89 | -6.2705 | -44.1996 | 2025-06-01 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a4fcf94c-5cdc-39cc-b7ea-a93e7d0ff1b9 | -7.2211 | -43.1388 | 2025-06-01 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 5fb1d466-588c-3f9c-aa4c-c5627eb4c973 | -6.2705 | -44.1996 | 2025-06-01 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b0186bd8-6534-3759-bcba-8e9c16a2a3fa | -7.2211 | -43.1388 | 2025-06-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 6969e38f-4807-35b3-88f4-c7e76a4aabe8 | -14.7006 | -45.092 | 2025-06-01 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 185312ff-4573-3102-a8b8-561c6011eaa1 | -6.2705 | -44.1996 | 2025-06-01 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8bdb6f08-0f72-30d8-9322-cfd5f5e55f12 | -14.6899 | -45.113098 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35c770b4-8079-3161-9f62-6f505202c4a7 | -8.6754 | -46.645401 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c89a138d-acc6-3119-bbfc-3f6af181a193 | -6.2146 | -48.5163 | 2025-06-01 00:20:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b317ca8-29c7-373c-bdac-86fa08362e04 | -10.6702 | -44.399899 | 2025-06-01 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06a4fd02-b685-3b79-9de2-22e77ff84570 | -8.6851 | -46.643101 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea521a0-241a-3cb4-98cb-2d1e02c960b7 | -6.2713 | -44.205101 | 2025-06-01 00:20:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21fa3d78-2238-322c-8104-229fd3102a14 | -10.2178 | -47.166698 | 2025-06-01 00:20:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4734759f-27dd-3bb2-b063-94d5b1d938e7 | -7.8725 | -45.982498 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a4aea07-ae78-3042-914e-6d0bf666453c | -14.0298 | -55.1157 | 2025-06-01 00:20:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0ed890a-92a1-3abf-b1f4-eb21cc81a8ad | -9.3274 | -48.934399 | 2025-06-01 00:20:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c302bd1e-32be-3075-a70a-e998323cea29 | -9.9292 | -59.850498 | 2025-06-01 00:20:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81da839d-df81-3e86-9523-1e1c81bf483c | -8.7313 | -47.977001 | 2025-06-01 00:20:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7627eb8e-30e5-3603-9cfc-99516e19f064 | -11.144 | -53.929401 | 2025-06-01 00:20:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7535d753-694d-324f-97fe-cb9dd56e9c69 | -10.226 | -47.157299 | 2025-06-01 00:20:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8736fb06-153d-3e17-9e98-8e09a1a689b3 | -10.4652 | -47.942101 | 2025-06-01 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9821c509-f934-3bd9-964b-73f10e20c7af | -10.7311 | -49.2775 | 2025-06-01 00:20:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18b93606-441c-3f05-9e9d-bd5b4ae1d7d0 | -9.4006 | -48.939701 | 2025-06-01 00:20:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0cc59a4-b465-35e0-a21e-275500e1d1f2 | -13.1036 | -45.264198 | 2025-06-01 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7032fe51-b56a-3d22-9826-566ee4fb6568 | -8.6736 | -46.637699 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af280a3f-aaa2-377d-8639-c840bf6793ce | -14.6941 | -45.0872 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27c86095-ab1a-3e72-9620-f8fd086f9d7f | -10.2293 | -47.1717 | 2025-06-01 00:20:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4632d0fa-9178-3ad4-8339-0c75ef43ca82 | -12.7207 | -54.947701 | 2025-06-01 00:20:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c790a78a-7c95-33cf-9049-d03adbe55f74 | -7.8706 | -45.974201 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46e3dc96-471e-355d-929a-88088ee4b614 | -6.2662 | -44.183399 | 2025-06-01 00:20:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40ae8ad7-1d5f-36b9-97b6-e69a97a15049 | -4.6445 | -47.956402 | 2025-06-01 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6636e0c6-4f5a-3251-995a-f2d49094afcd | -7.6607 | -49.126999 | 2025-06-01 00:20:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4434bf72-d0e7-3e56-99a5-1919c4772ab2 | -11.0779 | -54.757 | 2025-06-01 00:20:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1774e1b-d6c3-3afc-8f9e-28c00111de59 | -7.2106 | -43.127602 | 2025-06-01 00:20:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ddfee66-3f33-330b-b45d-5679a1288fe0 | -10.1434 | -52.1189 | 2025-06-01 00:20:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd5bb795-f6f9-3404-b7a0-7570138cebde | -9.3289 | -48.941299 | 2025-06-01 00:20:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 663aa2e1-2f07-3ab2-9ec8-ca03e51fab7b | -10.1453 | -52.127602 | 2025-06-01 00:20:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b11d69cd-0093-3439-bd88-4bf5d532e737 | -6.2162 | -48.5233 | 2025-06-01 00:20:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0369916b-3c4a-3c6d-bb84-a2e2837823c8 | -8.6816 | -46.627899 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaf699c1-698d-3f94-889a-d1b2dfcf3eed | -11.1417 | -53.9179 | 2025-06-01 00:20:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27dc70bb-844d-3662-a5e4-f9173b990cc1 | -7.0089 | -44.624199 | 2025-06-01 00:20:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 578e06f2-b56c-3af0-b0de-90d39612d36b | -22.766001 | -48.574699 | 2025-06-01 00:20:00 | METOP-B | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e82de117-e15e-32ef-9739-351aee1f6263 | -14.6913 | -52.674599 | 2025-06-01 00:20:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4625741f-0bb1-3c75-8005-086b4fbfc2cb | -10.6609 | -49.426201 | 2025-06-01 00:20:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db345e59-32b0-302b-832a-b22263ef5255 | -9.9195 | -59.852299 | 2025-06-01 00:20:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4972fc0-f442-33c4-8f87-1950f824b849 | -9.4937 | -40.292301 | 2025-06-01 00:20:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 31ebd0aa-ab10-383e-9e90-1f2ce0587456 | -11.5811 | -47.4506 | 2025-06-01 00:20:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03ea5ab0-77ad-393a-96c2-f36f336cb173 | -7.2173 | -43.112801 | 2025-06-01 00:20:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2ecea1c4-e14b-3fba-8340-e17165d88e34 | -6.2177 | -48.530201 | 2025-06-01 00:20:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32f22fcb-385b-32c1-a156-047f7327517b | -11.4396 | -54.9884 | 2025-06-01 00:20:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7cb348-42c6-3ed7-b4d4-689aff288b44 | -9.4072 | -48.415901 | 2025-06-01 00:20:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be88f3bc-676d-342c-92b3-f6f2d68f5556 | -10.6783 | -47.196301 | 2025-06-01 00:20:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b172cb9-81ef-3449-90e6-30b99b989965 | -10.475 | -47.939899 | 2025-06-01 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2014371f-31b5-35c8-8b3f-d66abe1ee4dc | -10.6724 | -44.4091 | 2025-06-01 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a349fc51-e69f-3e00-ad02-b765d64854c9 | -10.4637 | -47.9352 | 2025-06-01 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c393c5a2-4c11-3cdb-bff3-4dadda59b95c | -10.6594 | -49.419201 | 2025-06-01 00:20:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39e947b1-cf8e-3964-a1b6-ffde7b76a4b0 | -11.0753 | -54.743999 | 2025-06-01 00:20:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7426e4c-e4e5-3d23-a4fe-94f37662f530 | -10.2276 | -47.164501 | 2025-06-01 00:20:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3db2d87-ad45-3df8-a5c1-05d5d73e87fc | -14.6959 | -45.095001 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03aab360-39b8-36f6-888e-72b9f6f181ed | -14.6996 | -45.110699 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1c6141b-25fe-3a82-a2bb-fbeccc88efef | -13.1017 | -45.256199 | 2025-06-01 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca62f146-72eb-3cc1-a336-7ecbdf7b2d9f | -9.4981 | -40.309898 | 2025-06-01 00:20:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 023dbc5c-0381-38f2-af75-771d710bca08 | -7.2203 | -43.125198 | 2025-06-01 00:20:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e22814c-e69d-3e17-81d7-d06f2fe62e28 | -8.1115 | -45.900799 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e836227-8bb1-303b-89ec-442f4d486655 | -13.1022 | -52.278801 | 2025-06-01 00:20:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 739122e5-27cf-3359-8c73-163dd53b32ea | -11.0805 | -54.77 | 2025-06-01 00:20:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b08f0f8-3f48-3ebb-ab43-988e52b1f4f7 | -11.5713 | -47.4529 | 2025-06-01 00:20:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9d6957d-684c-3583-bf14-47eb1cc1d4c7 | -11.0877 | -54.755001 | 2025-06-01 00:20:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5904804f-968d-3b71-a438-26a0ddab88ff | -8.6834 | -46.635502 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbad999-2866-328b-b94d-dc98d8cee2f2 | -14.6703 | -45.117802 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d732417-4440-327e-9c5e-bd51ac58d038 | -14.6801 | -45.115501 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41426888-cb90-3bf4-80d1-84cc8aa1e218 | -10.6766 | -47.189098 | 2025-06-01 00:20:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c27fa7f-ca40-3c1e-b019-296f2c9130d5 | -11.792 | -41.192402 | 2025-06-01 00:20:00 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3d779295-d58c-3dc3-832f-c98fb38b8f71 | -10.2374 | -47.162201 | 2025-06-01 00:20:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45b64714-6bfb-3ca9-9139-9aef16f4c5bd | -9.3485 | -48.936901 | 2025-06-01 00:20:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3235af75-dc90-386e-9adc-09c3a7cf1834 | -14.6978 | -45.102901 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70b6ef64-0ba5-3f50-8aec-b99eec672329 | -10.4766 | -47.946899 | 2025-06-01 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fc64eee-8cec-3310-bbee-772236df3114 | -10.1471 | -52.136299 | 2025-06-01 00:20:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2923ba18-efc6-380f-8125-f8c17595bdf4 | -11.7885 | -41.178299 | 2025-06-01 00:20:00 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b042f645-b8a7-3a49-903b-f1eb9d8815a3 | -12.131 | -54.583801 | 2025-06-01 00:20:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b52bfa12-d20c-3925-b9a8-9658cc3d79b1 | -7.5171 | -46.8563 | 2025-06-01 00:20:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38f6e8b9-2a4e-34cb-8431-d3bf5a69fdcc | -11.5795 | -47.443501 | 2025-06-01 00:20:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae945562-cb68-3ad5-bde3-56ce7816fe26 | -11.4368 | -54.974701 | 2025-06-01 00:20:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15608662-5b60-3dc0-a4d5-23130fcc3b71 | -8.1096 | -45.892502 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5b61eae-29c4-330f-b92e-81bb9b845cb2 | -7.0066 | -44.614201 | 2025-06-01 00:20:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db879e34-10a3-3c92-b83e-c4f6c3ede716 | -8.6719 | -46.6301 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84fcf86f-4f54-308e-b986-077a3e72f1ff | -7.2301 | -43.122898 | 2025-06-01 00:20:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8e687a3-3521-3e79-a431-91743903e3fa | -8.1321 | -49.578602 | 2025-06-01 00:20:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9661671-d157-3380-85bb-544fcb6aa3f3 | -6.2688 | -44.194302 | 2025-06-01 00:20:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cca21dd-3838-3fc4-88cc-8a834199fed0 | -8.1415 | -46.477001 | 2025-06-01 00:20:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25f05d59-487e-32e6-b002-84649233f8c1 | -9.35 | -48.943802 | 2025-06-01 00:20:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42044a49-3100-31b3-8698-a4ffb0400491 | -11.7982 | -41.1758 | 2025-06-01 00:20:00 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cb04da12-8e32-3e4a-bb2b-2f1b7fb655e8 | -11.9089 | -47.4417 | 2025-06-01 00:20:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd025ca-e4b6-3c85-893b-d6eefa4f9692 | -13.6406 | -52.165501 | 2025-06-01 00:20:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6803d03-2020-34dc-a69a-a190674cec2e | -6.6385 | -47.342201 | 2025-06-01 00:20:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4eeecaa8-1512-3277-8d03-ad9c49cdf05a | -7.2232 | -43.137501 | 2025-06-01 00:20:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a8f2166-7963-317d-8b60-5e32a8a66cf8 | -11.8361 | -51.258099 | 2025-06-01 00:20:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c1545eb-df78-392e-83ee-134c0263db50 | -13.0919 | -45.258499 | 2025-06-01 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b087b5d-1c30-3879-b9f9-8bebc7153f05 | -11.4494 | -54.986401 | 2025-06-01 00:20:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
