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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d7226cf-a0ef-3e61-9996-4e9dd11b0e26 | -8.6904 | -50.40165 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ced82c42-9502-3124-aa20-f67014925d00 | -9.94104 | -44.02118 | 2025-08-30 04:49:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c98fee8-bc1c-3f17-b2f8-ff7d646b6aa8 | -11.3035 | -43.58115 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c1cb6ed-cf25-31dc-b8f4-2c22fa68689a | -11.31962 | -43.65627 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d79ee65-1d55-32b5-8453-ca18c174cda2 | -11.84148 | -46.7904 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecaa0787-3bde-35e4-96db-2a4e788df34b | -8.43209 | -47.36895 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a0d37f3-513c-3a7a-8ebf-d1822a76cb21 | -11.5725 | -46.3471 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ed43b9f-87ea-3024-9cc3-a98706ab9684 | -9.43644 | -60.54887 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5f2eb30-ab02-3fb7-9ba0-f733e515c8f7 | -8.4571 | -43.64087 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c78c4c38-c8a4-3fcb-adbe-316a9a6b4aee | -7.3968 | -45.92603 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 435a5cbc-a582-30f8-8cd5-737daab85104 | -10.64734 | -48.65468 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff13c2b6-cf1c-3b27-9901-ff05374da85c | -6.77811 | -44.82772 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5123b3c-60ec-333a-a955-d517fed93a98 | -11.82205 | -46.46796 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| bf2f0c15-351b-3d01-ac69-5680ece6e127 | -7.11782 | -44.58497 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1b88c0b-3d35-3faa-b3a3-e95fffaa9b68 | -7.62379 | -60.85087 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a072ff6-96a0-35d8-b975-3c350764f8ab | -11.02345 | -52.47623 | 2025-08-30 04:49:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4b042f8-1092-3f1e-85cd-b8e4556b8daa | -11.8331 | -46.44508 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fdc44d1f-8c8e-3da6-bf4d-9359425aaa79 | -11.36041 | -43.58257 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 682ec6b0-5d47-37c3-855d-e2a9f59af87e | -7.77922 | -45.47655 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b5370063-7dce-3835-8200-6ff86e1cb206 | -7.62553 | -42.66255 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 736a3f98-8351-35e1-aa77-f73659cd064b | -11.83639 | -46.45785 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c9f8be2b-6acd-3cb8-bce0-05c8090e12f5 | -8.05476 | -45.4105 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9de0fdc-763b-3b08-8917-23e7aae06fe1 | -9.62718 | -47.79999 | 2025-08-30 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10662a16-5104-3515-a5f9-141f3d74054a | -10.66921 | -47.07183 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cec0d216-0c88-39ab-badc-896eb228391b | -9.43673 | -62.32971 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0ed885b-251a-3d21-aac9-cb2c874133b7 | -8.87646 | -60.7364 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58610f0b-8a9c-3c93-a6e6-bad05ef29968 | -7.72991 | -50.27492 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 836829d5-ae23-3af4-9d89-699dcb6ed366 | -7.08851 | -44.30041 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98f68696-b76b-3101-9803-0d2466451c91 | -9.4311 | -62.33969 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c79eb740-9dc1-3cb2-a81d-6813c3f68ce9 | -11.41267 | -46.90483 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0cd46da-886d-3583-9a1b-c31a3c317d9c | -8.45438 | -43.63959 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82d2b2c6-eb75-3f3c-8083-74feeb01517e | -11.30554 | -43.60555 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b9a5449-7e30-3557-9db2-9909aeee4af6 | -10.53704 | -56.38596 | 2025-08-30 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8602d680-7845-3e88-931a-a6e7f2bfa15b | -8.88548 | -60.73011 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beb9fb74-c268-3ad2-8b96-e1429bdbfb8f | -7.64187 | -42.65839 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8770922b-4d62-3fb2-a7c7-20b9b9b8afd7 | -8.10441 | -44.99788 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 376c67e5-e4d0-3a9d-8ca7-b039b2de2c9a | -8.55184 | -63.02501 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5ca4028-04fd-3f42-86ac-6c77abc10bb0 | -6.98835 | -44.41683 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e83af47-c52b-3c45-8670-00ca224904c0 | -11.30589 | -43.56261 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 730e498b-4d97-3703-aa30-2b7fa8d834f1 | -7.60632 | -44.94713 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 610e8081-20e5-379f-acb9-46c2bde011f7 | -11.34266 | -43.59902 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55c0d6a6-7572-339f-890d-26980313c77f | -7.96005 | -46.38083 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f7570f-b225-32b0-be01-07b2298771cb | -11.83748 | -46.45012 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1dc55b0c-f72b-3f31-b578-3116a4a4ddd6 | -8.55606 | -51.30656 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bdd1349b-85d4-3f98-bc86-5aebf332d26d | -7.90619 | -44.78577 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9913e390-d01f-3b40-8401-da3f2c896474 | -7.16469 | -44.16122 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33cc6be6-b1db-3b6c-af14-d349bfc41568 | -10.67886 | -48.36725 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5544e48-768e-3278-b018-7c33e836786e | -7.73443 | -50.29005 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34fd443e-713e-39db-abf7-f7e2c4caabd9 | -7.60112 | -42.72452 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23af0629-a63b-36f8-9811-a6565e8b79ef | -9.45286 | -62.37234 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afaaa731-ff49-3737-b2cf-f9b14667df69 | -7.5836 | -42.70004 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b6154b8e-1343-32d4-bec8-f763e6f991ac | -10.93945 | -47.43078 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f351c48-5ca9-3cf8-bbb0-4da3a51877f9 | -11.34684 | -43.52779 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 397cf56e-10a7-32b3-b04d-fb4379946e32 | -9.44201 | -62.34637 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7999212a-fd89-3e3e-adcc-8c059bc71d3d | -11.33838 | -43.59216 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71ceb829-df23-3d9b-8947-fd2225712af5 | -8.52708 | -64.01557 | 2025-08-30 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2020d19e-da11-3611-a23f-11c0d2e6c167 | -11.41572 | -46.91271 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6885edec-86d9-326b-a448-90eb832ee759 | -9.44048 | -60.55616 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 108333f0-eb02-3825-a810-47bfe0bb8793 | -7.72375 | -50.27036 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8bb3ef77-65e3-3f44-a917-206a93fe3480 | -7.40341 | -44.286 | 2025-08-30 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 230af1e8-a110-35b5-9fb5-cb65107a19a7 | -9.45492 | -60.56573 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc97c81d-6d9b-3f4c-95eb-a3072686951f | -10.07601 | -54.931 | 2025-08-30 04:49:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a45db255-c871-344c-b10c-9214360e80aa | -11.0805 | -52.03052 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ff8645d-7ff0-3d8b-b6e0-687d65137725 | -7.73046 | -50.27139 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b00933c-a5cc-378e-8515-e16dfa2cf4ca | -7.90529 | -45.17122 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32796753-2073-38ae-a0ac-6d47d91ab240 | -11.41177 | -44.68142 | 2025-08-30 04:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb33636f-27a5-3981-980c-84a7eeba2a62 | -11.83628 | -46.85818 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4856dcc2-a451-375b-99d2-8c6dee1f8423 | -10.77655 | -48.8134 | 2025-08-30 04:49:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 343aa55f-f8b8-3078-9619-ba72ebcbb077 | -7.76382 | -45.46311 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 301bbff7-b550-3397-a406-d8d75e4b8e5d | -8.67719 | -62.43798 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd2c5b4-0631-33d3-ba54-9d9ca683d307 | -8.17228 | -61.37634 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e30ffd60-ac3f-3cd1-9889-56d77235d39a | -7.11596 | -44.59791 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 144b5440-719b-3d59-bcae-5bc801803c70 | -9.45674 | -60.55592 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e8cf025-24cf-3a3c-b524-38338e5c44a8 | -7.78786 | -50.96684 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1713d89-c439-3a21-9734-31012bbf069b | -9.43867 | -60.5658 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 327479e9-3dc8-35c8-a4d5-52abfbba5660 | -11.0709 | -44.61367 | 2025-08-30 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b2a259b-6ddb-32db-a403-c775e2e26e3c | -11.07156 | -44.60868 | 2025-08-30 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f60c168-0c8a-3c0a-8521-165e5d0d2699 | -7.77978 | -45.47277 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3474dbcb-2435-3770-9f22-8cb58e25470e | -12.40409 | -46.47546 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b85ef646-d05a-3e2e-bcf8-74db2ce98dd9 | -10.99915 | -46.96337 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 47653f41-df18-385c-b64f-416073407188 | -8.8484 | -47.81033 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff1304c6-1dd2-3520-a988-3fbb9b755875 | -11.36 | -43.58563 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5306794-48ab-364d-a271-809b7c83e6e0 | -9.24922 | -56.89529 | 2025-08-30 04:49:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1584fc4d-c9a2-3a7c-9d2d-6f20015c5c63 | -8.84493 | -52.02271 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57d530ac-53f5-33bb-bdbe-2fa42f80e364 | -11.93365 | -46.68702 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26c17171-23c9-3efb-bb69-4808c0e2ad9a | -11.91079 | -46.69916 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 757b321c-43c8-329c-b850-f0867eeb2cf9 | -11.57304 | -46.34311 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23425c07-b7ce-3734-882b-dbfa76fa46c8 | -9.44849 | -60.57114 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b38bd253-100f-3398-bb21-1aa68cefcf02 | -7.39218 | -45.92904 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6750583c-f825-3865-b784-74c59ed56c8b | -10.37546 | -57.82066 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91e53f90-a570-3d56-817e-1dbd3b96cf48 | -8.51416 | -54.71352 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a571fd64-3159-3611-a4b6-b96f863002a9 | -8.55551 | -51.31005 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2160d32-2b06-38a8-aefe-dd2a04a4d644 | -7.61009 | -42.73513 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c1c9496b-aef1-3dcb-b09d-b089caf7ca67 | -7.76866 | -45.45975 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 850d7046-2ac8-36d9-a9d2-2b1faf5e1c91 | -10.48627 | -57.95357 | 2025-08-30 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e8023f6b-d58b-3d9c-a32a-7a96a761043f | -8.55474 | -63.02069 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c75730f-a9bf-30d0-b905-228a19d3baf1 | -9.44628 | -47.64202 | 2025-08-30 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2444696-f694-3d88-92b4-79373859aa73 | -11.86802 | -46.4417 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa8279a6-b2ad-39be-ab3e-921574cc9bf0 | -11.30089 | -43.6414 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1763f50f-f084-38be-bf51-4f991a090d0c | -10.36732 | -59.21366 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README49.md)
