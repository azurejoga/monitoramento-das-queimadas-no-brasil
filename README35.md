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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3f94a2e-9d05-32a8-a9f6-8519c0c0987c | -7.07137 | -44.34229 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552c35d7-7136-3f5c-ad17-b11dcec02101 | -6.63856 | -44.25109 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80a8b15d-87a7-3793-9453-2893e8725f20 | -11.37395 | -43.56929 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47599106-a958-37be-9634-c89117c10542 | -6.3102 | -43.62568 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d40a97b-0d36-38c8-8d0c-98d4f1471602 | -7.94998 | -46.45573 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e410ce-7269-3dac-a3b5-6941e7687a4f | -6.182 | -43.35335 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 352fdb78-87aa-3619-a194-3650eb4807a6 | -11.03551 | -47.05026 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462acbf3-4f42-3bc7-8d91-54004e384860 | -5.83669 | -46.13381 | 2025-09-01 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a59f654-83f9-36ae-b3b8-9a70c33c38d8 | -11.05077 | -46.91474 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba06b74b-65a6-3503-90bf-3951b8a2aca2 | -7.63188 | -44.02208 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77786310-6d79-3865-b799-3ae08bf72778 | -9.64063 | -47.81287 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe4a5709-0306-37b3-9dba-61d2c9995f82 | -10.60445 | -44.32479 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f9d1620-ab05-33bd-b675-2a701926872a | -6.49739 | -43.56533 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e89b11e1-ad99-3f27-a1cc-8aded2ca751a | -7.70883 | -50.30547 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38a185d7-e958-3bae-a1e7-6894b1e3794e | -5.6578 | -43.66683 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f57c52d-ba58-3776-a891-cd2b1c30677c | -5.36147 | -41.1479 | 2025-09-01 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 024aaa3d-4162-3334-b6c2-708a2b3c5428 | -6.74037 | -43.77665 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a84ac4be-0743-3aa9-9f50-6f92f5cf2349 | -11.05803 | -44.64508 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab50c314-bf13-3c13-9ada-0f19aac7ffd2 | -8.16132 | -42.31218 | 2025-09-01 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 029c897f-3330-3e8c-ab5b-92abf3782998 | -7.84827 | -46.95037 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9083bec-ce99-3bf9-a314-4bd96c79e75b | -11.04311 | -45.14628 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 16d04866-f24b-3107-b8ff-fdb8d30bd683 | -7.08297 | -44.36092 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2f13d86-529b-3d61-aff2-2ca353f14f0f | -6.81211 | -43.35082 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 27ec752a-25a1-34c2-9b97-c03f95ef1103 | -9.66652 | -47.81316 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d61819ef-035a-37f4-9e55-9a70956c3be5 | -6.15578 | -43.34988 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc065ddf-4be7-3681-81b9-fdc01975fdde | -6.24174 | -41.80596 | 2025-09-01 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c6c67a8-0be7-38b2-a9a8-252d78e5e1c3 | -6.14938 | -44.12537 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b071f93-caac-31d3-9058-19ef751da0ca | -7.70402 | -50.27373 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14cd5e91-db47-33c3-8bf5-d1447ea6fff4 | -7.95175 | -46.44538 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebc2fd08-04f3-399b-a1e6-573e29654fcd | -7.73361 | -50.25592 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 571a31e9-4e89-3d74-8f44-3191eab10ca6 | -6.3055 | -43.63274 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c174219-d312-3eda-8d76-e91200c9162d | -6.30325 | -43.62457 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7cd5cf46-a444-34b1-b221-b0362eb748b2 | -7.24605 | -44.24204 | 2025-09-01 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31eb034b-7d25-3575-9bdf-883a65204073 | -11.37152 | -43.60568 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbd27845-9647-34d0-b877-ece2ddd759e5 | -8.462 | -43.62346 | 2025-09-01 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 836efaa5-94d7-39ea-9e9d-4b815104d4cd | -8.70488 | -47.86954 | 2025-09-01 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17e0fae5-1853-313d-9953-d896204c1301 | -6.19912 | -45.38048 | 2025-09-01 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c355c156-1264-3b80-b6d0-73d16f773262 | -11.0313 | -46.86583 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58adb304-6f35-3bdf-b6a1-fc19075ebcfd | -6.56375 | -43.66861 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 786c5a4f-3e12-3164-9916-404cb2106a85 | -9.15631 | -47.93758 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d76301-c058-3cfc-bf2f-51b0480af73c | -5.54683 | -43.74976 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a19125cb-c62e-32d2-a8f0-1e0f1ee71e81 | -6.83723 | -44.24879 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab128f14-88bf-3509-843e-c1ac34e0ccd0 | -6.36966 | -44.46019 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 115fa9d9-83cb-3f26-9313-9384835ae086 | -11.89658 | -46.73924 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a941e516-6a45-3068-bb38-292f1b71a246 | -8.84951 | -45.73536 | 2025-09-01 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feec1907-203e-3860-92ad-e3c18c923383 | -6.0026 | -43.36398 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abbfff7b-51e8-32d5-ad0d-5aff9e7b50c9 | -7.69608 | -44.99638 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac47d881-4d85-360c-a002-bb13eff2bff8 | -6.24442 | -43.38261 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f824e662-1896-3e74-a608-8b17e0a6e654 | -7.41072 | -47.4299 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4824885a-804c-3820-88e0-8ad903db3617 | -6.48291 | -43.56696 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 068130b2-de0f-3d61-aed5-e685b570d8bf | -11.01846 | -46.84806 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e5de12-d425-32cb-adbe-cae00ff98ab7 | -11.37615 | -43.57701 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86497eb7-919c-3a42-a00a-151f48c13c42 | -11.80409 | -46.42228 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a72ba83b-114d-3e09-9def-3dc67ad9f8f7 | -6.16804 | -43.31733 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94751135-0ad8-3161-980d-87c9c264f15c | -9.63791 | -47.82813 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2bac7a0-155a-31f7-a48c-909935f1fd1c | -11.37242 | -43.6428 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ada950d-6e72-3fe5-afda-3cd750a0031e | -9.27753 | -47.10915 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03558ee0-5a8a-393b-9d3a-2d9ba0e0b3f1 | -5.86059 | -42.98846 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a147d5e-f811-32ac-863a-7d07db3283c1 | -6.94445 | -44.34344 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cf7615a-eebc-3b87-a422-728b87f10210 | -8.83449 | -47.49298 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a96281-6d22-3e04-bc28-86028e2b0368 | -6.139 | -44.12825 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4d8fc5b-8e61-3b10-bbf5-5769ffe13d7f | -7.4592 | -44.8265 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b14e463d-1677-31ba-a4ce-52fecad3c646 | -10.24135 | -51.12091 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b1effe4-9509-352b-9991-383cb1b14ecd | -6.41513 | -43.6229 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed3269dc-55f3-34c6-a875-e7cfd69d9273 | -7.11006 | -44.76981 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb2e75d4-4c30-3158-95e7-d453b49feb52 | -5.31411 | -45.4512 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75ce2b11-3377-3bb8-bc52-67202b51e7e0 | -7.40579 | -47.43322 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e759deb-b9e9-34dc-b292-d374eec7690a | -7.88689 | -46.99471 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6d6aa3d-58a7-3a2e-8609-af7c274f9b49 | -9.67243 | -47.04242 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fbca239-8ca9-3ee7-9152-a89ebdd022e5 | -6.36199 | -43.55569 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c49f50e-bdaa-3a3c-9fca-729cc32824d9 | -6.81598 | -43.34303 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 605409d2-5387-3bc2-b212-0d26ec840710 | -10.27989 | -54.25547 | 2025-09-01 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e88b8f-6697-3866-864e-3018b8004703 | -5.35182 | -45.77667 | 2025-09-01 04:10:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18e25b26-3f98-33c6-a5f5-4649e2e29b76 | -6.18949 | -43.35073 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5b58e8a-41ba-3819-a345-d1838e393f50 | -6.78608 | -44.62966 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5939f24-81a5-3434-83c6-a11943f94c0c | -7.08493 | -44.34875 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 815b3f18-4805-3294-8924-f3e33bd6b992 | -6.56848 | -43.70506 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4fded4d-d55e-35a0-93dc-263ff5cb2705 | -8.83796 | -47.50484 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 823059b8-ccfb-3a8b-8ff1-647bcf778cfb | -11.91774 | -46.68495 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d38548b8-565f-3b50-ac8b-651b6cbf2a9a | -11.80037 | -46.42157 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b2e0cc99-d28a-369d-8edc-90015adb186f | -7.10793 | -44.55593 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c385bdc4-55e2-3003-87a8-ccd8e765cd12 | -11.32306 | -43.64941 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f2f91f6-db25-3fbe-a5e9-6afb4a33030e | -6.92548 | -45.56655 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b62fcb27-2f88-38ba-9a91-90aeb1436f7b | -11.38031 | -43.63671 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d42671d0-91b9-3aa2-beec-ae4d51980cde | -9.15684 | -45.21715 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3210fbd9-c82c-36c1-861d-d865501ac1bf | -6.29053 | -43.30968 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 082b1fd7-5ca5-3f04-8e07-d85ba23c9408 | -6.52989 | -42.95189 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c812615-cc37-372f-b668-24e2ea8ebe8c | -11.3728 | -43.57646 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad7355c9-d8a0-3940-8edd-9ebc3207c448 | -6.93121 | -42.0232 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8ca8510d-9775-35c2-b3d9-b8cb67436349 | -7.08558 | -44.34471 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 243d9a3c-ee7c-3155-b53e-9f334df194a4 | -8.83661 | -47.51253 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6949c779-bbbc-3ef0-a92c-4ed4d7f341a6 | -5.81916 | -43.2246 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f230b0d-b0d9-3696-81ab-fa8e46b2e0b0 | -6.83456 | -52.83355 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51efa59b-ba8b-3cf8-a206-1692e027eee1 | -6.8133 | -43.34337 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 24132bf0-1c23-3b6a-90bb-6ccb3e707d28 | -7.24993 | -44.06506 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b462ce0c-df51-32a9-8127-4695ad819f38 | -5.8519 | -43.21838 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e39b826-2d77-3ffe-8585-e31175aa8d53 | -8.00986 | -44.05361 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39ded88e-0d7f-39e0-a445-8337cccaed42 | -6.28899 | -43.82434 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3bb1650-d14b-37da-9676-afbc8fc06c2a | -9.385 | -48.01786 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 582f127c-2fb1-3969-adf4-ef7f9b8d9ff7 | -6.71213 | -42.25329 | 2025-09-01 04:10:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |


[Clique aqui para ver as próximas entradas](README36.md)
