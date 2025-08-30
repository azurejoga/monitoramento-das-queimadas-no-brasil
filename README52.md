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
| b6c493dc-62ee-3b88-a6d1-80b6c2fbd7ae | -10.7948 | -49.58701 | 2025-08-30 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09be9688-f8d9-3c4f-b8b3-d5b52b5cbac7 | -11.83577 | -46.45731 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 0cfd6402-f359-3a02-9261-7b1ba0ebcdde | -8.28978 | -61.41789 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e10e48c2-e9ea-37a3-8ed2-5566ab7b6495 | -11.29545 | -43.64357 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab8bf868-36e9-31f6-a600-48ca8ffb1877 | -11.86737 | -46.38281 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8ecb8aa-f4c9-3383-b088-351a6e60a3b0 | -8.28909 | -61.42173 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91cefbe4-eba2-3b75-8210-b8d77c7c6c4a | -7.77716 | -45.46103 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c76820c-57f7-393e-974e-ff391b36fa25 | -7.73326 | -50.27544 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54cd7c0b-6800-3b83-84b8-91ba421ba551 | -11.85883 | -46.38194 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 882d4d53-c42a-365b-ab37-d2330aba94ec | -7.7204 | -50.26985 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36f98044-2aac-3384-ac8f-079a33aa5403 | -9.44357 | -60.54 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ffdfce7-9042-3018-8442-cf17eef81795 | -7.75961 | -50.30473 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27320858-ea8a-34c2-84a2-d9b113934217 | -9.46281 | -62.35213 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba4734ff-438a-3ed9-9175-86bf4fd323a8 | -6.89796 | -44.39785 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e56a662-10ed-3415-bda9-9a0dcf0334a5 | -11.8368 | -46.44956 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c914ab3e-8a99-35a1-9907-25860554235d | -11.07939 | -52.03755 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cec9625b-3606-37b7-8a23-2b04148888ef | -8.68649 | -50.4047 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17de230e-dd33-3749-a827-329759cb0f9c | -11.93783 | -46.68755 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa0e2781-4985-3214-8caa-eee5ae0c25ec | -11.82518 | -46.47623 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 7b57d6eb-67ff-3534-b4e4-8d955e3609b1 | -9.69489 | -47.0539 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1650e4a-ffeb-3c8e-a1fd-04bd1d531640 | -11.29802 | -43.58344 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d181f19-95ed-318d-b438-7382681a94c4 | -9.45155 | -60.55481 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e574c4f5-63ad-30fe-8802-f3aacb55f08c | -7.33893 | -59.64108 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18e943a1-e6ec-328f-bca8-00b0eeb2242c | -9.49026 | -45.40598 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc3bcd31-7718-3e3d-8d4a-33ad90925d43 | -9.10946 | -65.74249 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b45237c-a7bc-3328-9782-b677ce71ed39 | -11.82941 | -46.47679 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| a67df1bd-e28d-3124-a16e-456e15e6fc91 | -8.07527 | -48.41051 | 2025-08-30 04:49:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23570be1-dbea-346e-b462-87463e905000 | -7.63583 | -42.66395 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 99af69a3-2db5-3e9d-bb21-b892a07bb04b | -11.8342 | -46.46901 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57ef8981-4622-3080-930e-a0e078b5986a | -8.56216 | -51.31112 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2cf54577-c979-3cf2-9f36-b8e2be3ffac9 | -9.4403 | -62.37431 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00798813-de8f-3a9c-a612-ee30f8b57fc0 | -9.43593 | -62.33385 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17e71acc-598a-3a3b-bd6d-467c3c044be4 | -9.1077 | -65.7425 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d03a0dbb-9469-371d-a8f6-60f21f62aa76 | -8.87951 | -60.73249 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 297ed1ce-21c9-339a-8b04-547c57268607 | -10.36541 | -59.19755 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 140bebdf-357b-3772-ba1c-8908efc862a5 | -8.28347 | -61.42052 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05bfe3f2-58ab-3930-9062-bcc2af6162a7 | -10.0206 | -48.05852 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 224a4828-4664-3988-9379-c1d954359ccb | -7.68511 | -44.9918 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bbbe2ad-d429-3284-b1eb-7eeffc331083 | -9.78534 | -64.23914 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7dadad4-f975-3a9f-8366-b7e3f3cb89c1 | -8.56612 | -63.01769 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 722d22e7-244a-3354-b155-6d1665cfe908 | -11.35758 | -43.58239 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82f11e41-26bf-3095-ac7c-51a23198bd17 | -12.66131 | -45.30294 | 2025-08-30 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f209cfb-a679-37c1-9fcf-6745a5fec502 | -11.00591 | -46.85859 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1595705f-269f-32f9-aa41-7c91fbfa7afd | -11.83325 | -46.44952 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f31d985e-fdc2-33cf-9de5-8a5bca35fe4c | -6.63717 | -55.27065 | 2025-08-30 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4b17bd1-6203-3662-9a71-a20c8e80e6fe | -8.82952 | -47.7779 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 677f5164-c925-3b31-b559-4cc815e1b007 | -11.85833 | -46.38564 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b84d331-a922-36c2-ade9-bb09cfca9a60 | -9.43689 | -62.3604 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ac8ab3d-9008-3e17-bf35-a6a574455a76 | -12.06334 | -46.64541 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 465ad432-c360-389b-a9f6-ef8f2c8e93da | -11.73535 | -51.75635 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02cab1af-1e28-3c2d-944f-b523a9bbb54a | -11.00488 | -46.8658 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6f011e59-f3c6-3e0d-a2d5-036155496db4 | -10.36357 | -59.2076 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5ff6e0d-a401-3252-b83e-9351c29c76bd | -11.34212 | -43.52401 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b02ab74-35d4-3ec4-9e25-6a00eeb69b63 | -11.83271 | -46.4534 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 74b6cd73-bd66-33e5-b49f-0c37dd63d0fc | -11.84155 | -46.44629 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ffbd591d-4fa3-3e1c-979a-2f90be78b451 | -9.08809 | -59.48671 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88268933-7202-3dd7-9402-ada6abcae895 | -6.77315 | -44.83106 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538efd75-afc9-3f31-878b-d6090b86ba7a | -7.96057 | -46.37735 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b6a1e70-6421-34a8-9334-a038999966ad | -7.73101 | -50.26787 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b42a79c0-e127-3066-a158-6432747f577a | -7.78087 | -45.46538 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05effffa-29de-38f0-a3f8-c355c46c8b0c | -11.74257 | -51.75389 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a96d41a-dbd6-3b96-b6a6-c9be7a65d3dc | -9.96239 | -46.49376 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca42a03e-c66f-3668-be36-2b84b77b8e7f | -11.84778 | -46.37707 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eed9c046-524a-348d-8d58-385fe3828881 | -9.4444 | -62.33345 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9a5b81c0-8101-3e6f-9700-3f3461adf8cc | -9.44937 | -60.53776 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc49eac0-4dd9-3961-bd31-48e8d5192744 | -11.22584 | -45.01788 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52844d7d-8579-301d-accd-18ae860b6c5b | -9.45851 | -60.54648 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94a5c814-b298-3d1e-972d-792ec9200620 | -10.07574 | -58.35923 | 2025-08-30 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62edfdff-f3d9-3ce1-b33b-f80586e637ea | -11.85052 | -46.44365 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 23de2561-9f04-32c3-a104-2228bbc7c068 | -9.10919 | -65.7731 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f8cffdf7-2e7b-363f-8544-c5c8ba826ba3 | -11.88978 | -46.71688 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d5dba26-4e16-34e4-9e01-95985fa2534f | -7.24983 | -45.4472 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad5e8ab0-73c5-3c71-8f85-bb6a8cb577a9 | -7.16769 | -44.46932 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4351f728-449f-37a3-b619-4125ad2a7f09 | -9.57506 | -54.48524 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab0e3f6-40a0-3a6a-92a5-4d9047e92833 | -9.44011 | -60.55918 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77c6140b-0ece-3397-a4ac-84cde1ffc5f5 | -7.60368 | -42.70618 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8fc5af9c-99b8-32ed-bb4b-0415377abee8 | -11.31256 | -43.63115 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32cbfe7a-6787-36f2-b82d-189b074fe5b5 | -7.61072 | -44.94774 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e11c01e7-c6cf-30aa-910c-bc66a184fd2d | -9.11935 | -65.76767 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39af93e2-a43b-3c09-b9eb-95547c5a3ce1 | -7.16238 | -45.16763 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9976580e-89f4-3d12-86cf-9aae080392e5 | -9.44572 | -60.55706 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6dfc02e3-3041-36f9-ae6b-05287645c7f3 | -9.24184 | -59.77391 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fb87512-2c8d-3e16-bb79-32d2d4e76638 | -11.73924 | -51.75335 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbc40492-e237-3839-b3c6-a0b55ce6b3bb | -11.66138 | -46.87254 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a2ada70-cdc4-393b-999f-2f05d06c252d | -7.71766 | -50.28755 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 685f5b4b-44e4-3c47-8219-e55080b99b2c | -8.69371 | -50.38023 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 582e3e12-a865-3439-b93a-96047059f4da | -11.0054 | -46.86215 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c929438c-6f03-3725-8c92-2ac098c5f9cf | -11.86112 | -46.39701 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ae8337a-17be-3c08-8eed-34b32a4b0e13 | -9.43808 | -62.36759 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09ddeac6-324e-3c28-be68-7b68263e4627 | -8.54673 | -63.02914 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48c17742-4d0e-36e8-8102-1f3caca8298d | -7.68073 | -44.99111 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd04c7eb-d09a-3f1b-8f12-a238b0a84153 | -9.16958 | -59.57608 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04ccc77d-7901-3b9a-a54c-3656e725f55b | -7.61051 | -42.73211 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 55d78ca7-18f4-32bd-b760-e173640b4d1e | -9.45614 | -62.35519 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1aab6ed-215b-31d1-b4f5-5f916668ee27 | -9.43851 | -62.33246 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c952f39-f7e6-3366-abfe-af881c0d4789 | -11.84189 | -46.38816 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ead01f14-4fa6-39b1-9598-90c6233ba353 | -8.10882 | -44.99853 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c48ca7d5-35c9-32d8-830e-d1a647340476 | -9.44781 | -62.36692 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 043a6d6f-22c4-304e-b41d-672242776f30 | -8.5135 | -54.71612 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3d1312-6d51-3dab-9b86-243dd85cd5b9 | -9.1755 | -65.56245 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README53.md)
