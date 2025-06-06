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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb6ff5a9-d485-328f-b56e-8b716defb545 | -7.73243 | -44.17997 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64f30995-6c37-33b5-a64b-e2855a09564c | -7.71367 | -44.16986 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dec5e8d6-498b-3fb1-981f-faa0ffb19e74 | -6.05291 | -44.1671 | 2025-06-06 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62f535be-b1a1-3267-8277-300de55912e4 | -8.47196 | -46.48291 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e67766c-c032-3021-85ad-55dd7043e655 | -7.6772 | -41.97129 | 2025-06-06 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2a34d78d-9aec-3450-bd0f-aed5ab7e2097 | -7.01271 | -44.59927 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f40ac7e2-a78e-31a3-a91a-b2fc705f2d2e | -7.0138 | -44.61406 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fce198d4-e2bd-3155-b014-f4dc96b8fd05 | -10.65579 | -44.48705 | 2025-06-06 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a7e9c48-2285-3f95-8cd1-619f81a5e8de | -6.2048 | -43.33301 | 2025-06-06 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e022abb2-1cb2-31b3-b2bd-f1a38f01422b | -6.96542 | -42.90596 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e546e240-fcc9-3c5c-8d93-d74348a4b2b3 | -7.71477 | -44.16289 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5eaea5d5-bc4d-31a5-99d5-9601a8f9d6cb | -3.40732 | -47.5878 | 2025-06-06 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a5b159e-48f6-319b-9a57-e944c7ee89b7 | -11.02665 | -45.23747 | 2025-06-06 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ab0d20d-44a5-31ef-a64e-137a808cfd14 | -7.20245 | -43.13453 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59913d9f-5734-3842-80b9-b4c6fe6368b0 | -7.01045 | -44.61355 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33f3072f-207f-37e5-9c1f-2ef82a035bf7 | -9.6658 | -48.598 | 2025-06-06 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feb28487-1e61-301c-914e-02b5afb2dfde | -7.55796 | -45.82681 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6b5e924-430d-3a71-a2ee-2e53bbf7dd8b | -8.67184 | -44.2668 | 2025-06-06 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a45764bf-8415-36fa-a992-1aa804b57312 | -10.35028 | -43.30053 | 2025-06-06 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a43cf26-2e13-3341-8270-d268234b71d9 | -7.71422 | -44.16637 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ff75ff6-1123-3d43-b87f-343fcfeca40c | -9.54532 | -47.77341 | 2025-06-06 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b8bd17a-aaa0-308f-b2c5-f7b0fdb3bc24 | -7.90868 | -50.36431 | 2025-06-06 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f5d9084-a2f4-3879-b42f-3f14e327e062 | -9.2213 | -48.86359 | 2025-06-06 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92a13c14-55ce-38c6-8848-f9b881340545 | -4.97815 | -47.8157 | 2025-06-06 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45bd1a2a-82b8-3096-aac4-a79049e14c80 | -8.73153 | -47.99036 | 2025-06-06 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29231a53-50fa-3a59-9e29-d870a9145400 | -9.2259 | -48.86077 | 2025-06-06 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b132444-2ac4-319f-bbc1-335f827ad6a4 | -6.24544 | -43.81089 | 2025-06-06 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9adf92c-f23a-3dc7-ab04-3ef6e9924203 | -6.33245 | -47.48232 | 2025-06-06 04:14:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba1bdc20-7957-301e-b673-c2e11f9e74f9 | -4.00001 | -43.24219 | 2025-06-06 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8e6ac1e-70bc-32da-b5b4-26b0b885b286 | -10.58799 | -44.39752 | 2025-06-06 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 208763aa-aab1-324c-840c-8ce66fcb32e1 | -6.21666 | -55.65156 | 2025-06-06 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3708e858-d4dc-3ded-afc3-54b3a0f1536d | -6.66444 | -51.96372 | 2025-06-06 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97f02fc0-3f53-3bef-941c-de8700b9c21d | -9.37923 | -48.55205 | 2025-06-06 04:14:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e78806f8-0a55-3227-84d0-4b263c5692dc | -9.39268 | -48.42577 | 2025-06-06 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3998eac8-357f-3a62-9311-2bbc7bde423a | -6.18956 | -48.55648 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d17a737-ba5e-33c6-a815-534170407555 | -6.11445 | -46.18148 | 2025-06-06 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 018b685c-9336-3ad9-953d-a616a011da60 | -7.00823 | -44.60591 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3c75829f-c2e2-3d6a-85a8-d981c73e5fbe | -7.12851 | -43.29969 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 319376ed-c92a-3d81-a49c-356f87da0233 | -6.20426 | -43.33646 | 2025-06-06 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e851867-8087-31b6-8a00-5016733ae0f4 | -11.02332 | -45.23693 | 2025-06-06 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c830791-7c46-3d25-b101-c6a46fad7de7 | -7.71863 | -44.15992 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4653295-bbfa-37b3-b7fe-09c6f258bf46 | -7.20959 | -43.13211 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27b71a89-86e2-3556-af32-2f8df8d9023a | -8.47201 | -46.48208 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4336bcc2-13d6-3fbd-bbd1-433d3220e46c | -7.90336 | -50.36815 | 2025-06-06 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7bc0fd10-45cb-38ee-b0e5-45b2f74e0ded | -10.65084 | -44.49697 | 2025-06-06 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65ceec47-7e0b-317f-bb3d-4ba875222cb6 | -9.20552 | -49.69089 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8d04d5a-e6d5-3b61-b4d5-165003f79600 | -6.74672 | -44.99054 | 2025-06-06 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbb83cd8-7359-3e81-9d28-80f050963d50 | -4.42202 | -47.66693 | 2025-06-06 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b68104d-ac85-3ce0-8546-19d6d195294f | -6.46519 | -48.02716 | 2025-06-06 04:14:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3aa61cd-03da-3b8e-9212-5e57a3c02903 | -7.17614 | -43.15163 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb90f42b-f0c7-3b16-bb92-2d1880679270 | -7.01493 | -44.60693 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e3133da-3d25-3b56-a9a9-8806c09313aa | -7.28818 | -37.2639 | 2025-06-06 04:14:00 | NOAA-21 | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4f8482b6-31e3-332f-98be-a023b56dcdc2 | -8.96488 | -47.96696 | 2025-06-06 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 664e3056-1080-30c1-a5fb-8b228cacb22c | -9.33935 | -49.54438 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8be9d65b-a2f0-3fe4-9ddd-07026f63b13e | -6.20756 | -43.33697 | 2025-06-06 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2efc72-751a-3b29-b561-a9a59d9ddbc7 | -5.649 | -43.59881 | 2025-06-06 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f282ddb-f0f1-324e-890f-0c1f9ea9e790 | -6.12369 | -46.82568 | 2025-06-06 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e6aa254-e6e2-3237-8934-1d585ce68111 | -6.19303 | -48.56101 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f7d533b-4450-31e4-9c92-9f444b7d12c7 | -10.65139 | -44.49348 | 2025-06-06 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27e59fb1-2c20-3ab6-808a-50ca9b4ede2c | -7.21288 | -43.13262 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d793d46-7341-3925-b0e9-5708ddf207b9 | -7.00936 | -44.59878 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8996f1f5-60d6-36a4-9d0c-e6b354f7f5f2 | -6.19651 | -48.5655 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcc664a9-76e3-3083-bfbb-f2232b894387 | -6.94694 | -42.80738 | 2025-06-06 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 44237de4-fa2d-36c8-91bb-4717e3a9c9cf | -9.24267 | -49.80084 | 2025-06-06 04:14:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 541e40ca-6a58-394b-8ed0-3bfb98843264 | -9.07501 | -47.14209 | 2025-06-06 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afecf3da-b8a8-3a87-83ce-ca1ce9d7a738 | -8.94399 | -47.29853 | 2025-06-06 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c642dab7-35a2-32a2-9608-4fd751696a95 | -7.72912 | -44.17944 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fcad17c4-8340-34c2-a7e5-b8c55cffa1ea | -6.05624 | -44.16764 | 2025-06-06 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bb13cb6-9a7f-3971-818f-144bb7fd348e | -8.73233 | -47.98554 | 2025-06-06 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8705b096-6fb5-32bf-b42e-e490c445ea64 | -8.47656 | -49.60561 | 2025-06-06 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf72aebb-8f37-34fa-a3fe-ee88410bb743 | -5.64569 | -43.59829 | 2025-06-06 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b80c6629-3e1a-3284-97af-c17c7820d530 | -8.47549 | -46.48353 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f07204b-a8de-3aaa-adf5-130fce509609 | -6.21818 | -55.65025 | 2025-06-06 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e31a6dd6-1c40-3bb7-899b-af1e34262c13 | -7.71918 | -44.15644 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 860876ea-94da-3f0e-906c-e4fdc6a601fb | -7.20299 | -43.13108 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 193742e3-60a7-3a0b-bdc1-50bff3df43bf | -6.12439 | -46.82129 | 2025-06-06 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4161077-3427-391b-89af-8816cc80bd5d | -6.19997 | -48.5701 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ffa89bf-734f-3c88-adb6-7c967933d97e | -7.71808 | -44.16341 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799f0465-5ec9-3aa5-b859-a0aed8f1d5de | -7.71974 | -44.17439 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27e13c1c-3f2a-3109-b919-6754c52ee031 | -9.52599 | -54.77796 | 2025-06-06 04:14:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeb3bf3c-2a4b-3a21-9959-2c934cb7d120 | -6.19238 | -48.56486 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d22c352a-8f51-3448-adf4-75c6cc0b74c0 | -7.0155 | -44.60337 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 523e49aa-14d4-39ef-968a-0c41fede3c9c | -9.60991 | -49.0163 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73384c70-46c7-3873-9e11-5f961bc2afbb | -4.59059 | -47.88964 | 2025-06-06 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbc3605f-0064-3bc6-9015-763adb01edf8 | -8.46842 | -46.4823 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cab7111a-149c-35b7-9643-1ebbc6b93239 | -6.19434 | -48.55328 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c7f00e-fa6d-36d9-840b-1f6fc6346098 | -7.01884 | -44.60391 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44e7873b-a84b-31c7-86ae-4e98b16f0d2f | -9.37881 | -48.4133 | 2025-06-06 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80541c59-a6d6-3523-8e8d-a06af8a791ea | -6.95955 | -42.06684 | 2025-06-06 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ac90fdf2-0778-3b30-8aa0-72cc3e6fa25f | -4.42323 | -47.73536 | 2025-06-06 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 234baf6d-02f9-3bac-884a-a1adbc3ffa82 | -7.58836 | -45.85928 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8367e4e2-36f8-3668-ab01-2b27dea3ccdd | -7.28802 | -49.2822 | 2025-06-06 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8e2c561-67ea-36f9-8894-3ba82aa4c825 | -6.19369 | -48.55714 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34836805-6652-30d0-bfac-8dbea18c4096 | -7.02275 | -44.60089 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6a3981c-da20-3e94-bb32-436123f00aa7 | -7.12575 | -43.29573 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db2637f5-7911-334f-ab95-101342c496d6 | -6.51223 | -43.67179 | 2025-06-06 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac98cb31-60f0-3dad-acfe-aab05ca3f695 | -9.70583 | -49.48458 | 2025-06-06 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a49ef75-e6aa-3253-943b-16b4ebaa465e | -7.25378 | -44.77008 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89f1273e-1a1a-38e7-81b5-aeb2510fa3f2 | -9.2013 | -49.69012 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1cfd557-2145-37b8-a64e-970f5e3ecafa | -7.77593 | -43.05544 | 2025-06-06 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README4.md)
