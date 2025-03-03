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
| dd0057c5-3710-31b2-8549-31ae2a7dccdc | -14.01011 | -45.59949 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82c99304-16a4-3be3-9a85-c17fe3c65a0c | -14.45435 | -45.6472 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03c87a60-9e6f-3994-bee2-e5564a4c91a4 | -21.81537 | -44.20226 | 2025-03-03 03:57:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c94c912-5f4a-361b-958b-804b7f58356d | -13.9876 | -45.58362 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45b47328-9325-3178-9a19-182b86446062 | -13.99442 | -45.59266 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab2010e4-8511-3b48-b531-1729ad9da8cb | -14.00323 | -45.56717 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09552144-2036-3b56-8417-0f96fafe17be | -18.19745 | -46.80631 | 2025-03-03 03:57:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28297b8e-c863-3893-8d99-f011cb1f98ed | -13.98692 | -45.58738 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1990005f-d9bb-30c6-a3e0-8c098a1f7cd8 | -13.98829 | -45.60322 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 850ddf52-c031-3e72-807e-2680343cfe5c | -13.98828 | -45.57987 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a0e925c-1a53-38f5-8cd7-9ee3784bc1b7 | -13.98078 | -45.59794 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5f9d215-4aa6-3963-a4eb-f00d07487692 | -23.98705 | -48.9163 | 2025-03-03 03:59:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4941f939-3b4a-39fc-b816-03add3d83e76 | -22.68516 | -42.89064 | 2025-03-03 03:59:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 782a2741-82b7-3479-ad7e-57ffa362f98f | -23.59525 | -47.44047 | 2025-03-03 03:59:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f67e7e9-5ad5-36ef-b8dd-7f8d176315bc | -23.33779 | -46.77192 | 2025-03-03 03:59:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b4bae67b-29f5-36fa-b51e-1ba98ebb9d25 | -23.40549 | -46.55429 | 2025-03-03 03:59:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 51e814a1-2a70-3de8-ba22-b22ac5a55726 | -23.33702 | -46.77475 | 2025-03-03 03:59:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a3319d2e-db73-325b-acdf-8e597e4752c8 | -22.91769 | -43.59036 | 2025-03-03 03:59:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 182fa97c-f94e-3177-8dbe-93b82e27077a | -22.85782 | -42.98028 | 2025-03-03 03:59:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 26d73af0-9f9c-3bb5-a634-1e1d6a4846cb | -23.52183 | -47.61091 | 2025-03-03 03:59:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e59d02e-465d-3a9e-b1df-7e86631d77c1 | -23.4464 | -47.02653 | 2025-03-03 03:59:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5096a37-17d8-3967-b3f5-31bf7cbb1135 | -22.84702 | -42.55813 | 2025-03-03 03:59:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ea7cd11-c641-31ed-8a94-f9521ef7c11e | -28.58505 | -49.4413 | 2025-03-03 04:01:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 10b88f3a-e30a-3331-b546-dd25d1d12896 | -27.3811 | -53.93619 | 2025-03-03 04:01:00 | NOAA-21 | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fe6af5e3-43db-3b68-b63c-80216ae3a46e | -8.11262 | -43.14203 | 2025-03-03 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7110c169-a28e-3637-963d-ff5cdf25d02b | -8.10575 | -43.14097 | 2025-03-03 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 265df7b5-934a-3127-ba0c-aea6401b957a | -8.10231 | -43.14044 | 2025-03-03 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 535d1c4f-1cd6-3101-ba46-1afa5cd1c937 | -9.67591 | -36.87333 | 2025-03-03 04:21:00 | NPP-375D | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7062d1be-d296-3934-a2f5-e02ac35fa178 | -14.45495 | -45.64268 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4476e7ed-738b-31e7-8968-e0de16422353 | -13.98848 | -45.584 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7f8ea9b-0ab1-3798-9100-0426bbdafbf3 | -13.98235 | -45.57932 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8eb59b4-0a3b-32c9-b08a-34e2184fe2ea | -14.00743 | -45.57227 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 208de607-1418-36ec-bc96-e4c1ec6fed8a | -22.68324 | -42.89069 | 2025-03-03 04:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 29b1d0fa-8860-389c-9452-29a40882e7da | -14.00744 | -45.59445 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f965779-f07a-3734-a34a-21f01aca2221 | -20.71291 | -54.41832 | 2025-03-03 04:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f71dd9c-4d11-335e-8940-68e81ed1bfb2 | -21.82343 | -44.2084 | 2025-03-03 04:23:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b162733-51e4-31f7-8c64-5c29ac3a0960 | -13.96282 | -45.55028 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e08dd8-c1d9-363d-bac5-e3c01bc29ffb | -21.1959 | -44.93707 | 2025-03-03 04:23:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d1e89716-6ed5-3000-92ee-8472bf3e3436 | -13.95836 | -45.55695 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64e80bef-7bc5-38b4-ad53-1ceeed1daade | -14.00967 | -45.6022 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d96ba132-23f0-3a01-b740-b1d5bdd47c7c | -21.95904 | -45.40232 | 2025-03-03 04:23:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 37d6f95c-0aa9-3b98-9f82-27d2f18af150 | -13.97845 | -45.58238 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d139f1bb-90c3-3c3e-abcd-81b7f2154f68 | -10.5045 | -42.40123 | 2025-03-03 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0233275-f340-305a-bb48-1cb2dd1af75e | -14.00521 | -45.5867 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e2d43384-4527-37e8-a3f3-492ea974ea90 | -14.00688 | -45.59805 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce4d88a8-d7c4-3bef-9f12-06365b216f8b | -13.98626 | -45.59842 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31a526ba-43a7-3001-9e56-753b5aba80bf | -14.45775 | -45.64684 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcbca609-e5a5-32bd-a94c-810c8fcf3f23 | -21.23194 | -56.06013 | 2025-03-03 04:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74d1056d-48f4-3852-a04f-854999f8aad8 | -13.96339 | -45.56885 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 568c293b-8ca6-3daa-86cb-f830605e5072 | -14.01022 | -45.59859 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f16b9a9-131f-3b39-a987-ee7e7091f7ba | -13.98068 | -45.59013 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93907bd6-8727-35b6-8abd-8bb12fc6eda2 | -14.00799 | -45.59084 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c8bbaaa7-0d30-30c2-a027-fd7af3d2186d | -13.98291 | -45.57571 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac46b035-d9a1-3f8a-9e64-b0dd94a5cafa | -22.21095 | -42.84162 | 2025-03-03 04:23:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4e5ab757-6ab6-328f-8970-49ec48d26e15 | -13.95892 | -45.55334 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eada7c4a-a473-3d1f-999f-f73155f30b10 | -13.98347 | -45.59427 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e7d6363c-f7d4-3859-a4bc-39fc1176c26b | -14.43876 | -45.62586 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9488bc9f-51ce-3e77-8738-3f30b9c1002b | -14.00632 | -45.57948 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e7d249c2-f2c6-32c4-a814-df1873876e52 | -21.80897 | -44.20111 | 2025-03-03 04:23:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 13ab5ad5-a48a-31d8-b061-1631d668f824 | -13.98292 | -45.59787 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4edcd19-57fc-3176-ba68-7e25623ded59 | -13.98403 | -45.59067 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aec901fa-cb3d-32be-b368-1f4710df34f9 | -14.00632 | -45.60166 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 458d682b-ab77-3b35-8327-ad92d1118344 | -14.47003 | -45.65625 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a66acb91-3ef4-35f4-b14e-d2e0b0a463f1 | -13.95557 | -45.5528 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e2588e2-a60e-3e95-a043-7e5f336ccc87 | -14.00019 | -45.57479 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f579aa25-d055-3a9a-98c5-216d0d50fe78 | -13.96395 | -45.56525 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff719689-1dfd-3d54-8623-c90fcd2f2045 | -10.48314 | -42.41975 | 2025-03-03 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1397469b-7812-34e2-b923-2514c366582c | -16.06794 | -46.12787 | 2025-03-03 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d38f671d-22f9-33e8-b47d-fce21f3c8686 | -21.81275 | -44.20172 | 2025-03-03 04:23:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0a89e3f3-47ef-3974-8d7e-18b3d66e14cd | -14.00465 | -45.59031 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 762d9b97-60a2-3793-9029-0569a7b79f40 | -14.4544 | -45.6463 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 240ee477-baa0-3d5d-8246-adea46e940d8 | -14.00409 | -45.57173 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 18e29a8f-4116-399d-8820-f70cfd37e685 | -13.96226 | -45.55389 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82d1312e-324d-3c67-8392-a49efa95ff6d | -13.979 | -45.57877 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3924fda5-d276-3cd7-a261-fa3dbfd7f0a7 | -13.96505 | -45.55803 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4d84872-d045-341b-a4bb-2f2bf28d06d0 | -22.68737 | -42.89128 | 2025-03-03 04:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f0fd57e-abf4-3fbf-a9e9-c63b39686874 | -15.56799 | -47.8558 | 2025-03-03 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 249332a7-daf0-35ef-a9ec-b2f09bc7f7fb | -13.96561 | -45.55443 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aee4744f-4c6d-3256-9123-32a23a7d47f0 | -14.00688 | -45.57587 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92a6b807-7539-30fa-b9a8-75c122a20153 | -14.00074 | -45.57119 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 01597c73-961a-3cfb-b4cc-ec60d95021af | -13.95781 | -45.56055 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbadca39-e884-30e2-a1b0-4b5c360af6be | -13.98013 | -45.59373 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46615ccc-915f-37db-881d-9de4510abbc2 | -14.00353 | -45.57534 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5a8f5681-183f-3bbd-9d3e-eea1c40e54ad | -14.00186 | -45.58616 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db774b04-a88c-3f1d-9c7b-19a3f986b3ff | -14.00297 | -45.57895 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5467109-d534-3b5c-bbde-a90202d19585 | -13.9606 | -45.5647 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 373090dc-f3ff-369b-a288-6cd930f36deb | -14.46109 | -45.64738 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c1bc59a-89c4-379b-9f4d-3616f5fac046 | -13.96729 | -45.56579 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e8527ca-9271-3e62-8808-66c68ae86a23 | -14.00409 | -45.59391 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 610fb243-10fd-329e-8a29-e09dae694c1d | -14.00855 | -45.58723 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2504f1d8-c050-34ae-93a4-8119fae6d3ce | -13.98793 | -45.58761 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e4d105a-f327-3f41-b62d-58df6928c8c9 | -20.71716 | -54.41934 | 2025-03-03 04:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a022ce83-db93-31c0-979a-70091facde98 | -14.00576 | -45.58309 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f87dbc91-0cca-3315-ab64-77d7fd5f4203 | -13.98124 | -45.58652 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 025efe6b-b6dc-3ce8-a681-720e9c16fb82 | -13.96784 | -45.56218 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb178181-3037-3bbc-828d-eb5b660c81f8 | -13.98236 | -45.60147 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efd3de48-a91f-3ecc-b370-20d1b9a2f514 | -22.9192 | -43.58979 | 2025-03-03 04:23:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6b9dca09-c5ba-3c4b-b922-e39cddcfaef1 | -13.98682 | -45.59481 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1edceb1e-3655-35a0-b4b1-c8209ab35db6 | -13.98458 | -45.58707 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e4ec0519-9a3f-3599-9b77-2c01de5a37ac | -13.9645 | -45.56164 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
