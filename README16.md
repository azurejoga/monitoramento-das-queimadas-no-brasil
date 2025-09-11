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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 415e6b76-d821-3468-99d6-65825366d2db | -12.55734 | -46.93525 | 2025-09-11 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2197cd2d-326d-396f-ba3f-b988dc8c9b90 | -9.00188 | -46.07633 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1e287b9-f87f-3b18-b39e-e70e9356300d | -8.48974 | -47.31419 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db016ee3-f888-3183-b40e-61236ee03ef7 | -11.10497 | -48.40443 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0382d93-c2ca-39b5-b320-d1d73d69eb08 | -8.73042 | -47.08978 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 60166372-d3b8-396e-b993-316c46e30afb | -5.60148 | -45.78655 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ead24e8-1eae-35c6-92ac-474f823eda33 | -10.41163 | -50.52594 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 247d975c-6d85-3e6c-b96b-d71f005d9706 | -8.47863 | -47.28928 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6811f37-f590-3920-bf49-913a23994d31 | -6.32237 | -42.21216 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 03b61be0-4ffb-38bf-8d97-31a71d10ef6e | -7.50043 | -48.25672 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d40283b9-b946-3fd7-8549-646995fe82e7 | -8.19419 | -47.14662 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09e13390-4176-39dc-802f-206233bc12aa | -6.79669 | -43.41875 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b28681b6-b142-3189-8dca-678f3b05ccbf | -6.94024 | -44.64702 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acf94bb5-6602-3779-9c0c-b3997c2d3b91 | -7.24259 | -44.42666 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8e316fc-4640-3377-827d-48e18768701b | -11.47218 | -43.62285 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b840d96-5446-37f4-a95f-855e84f37d13 | -11.1044 | -48.40756 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01c052a1-17c5-3829-b323-a3ae4b4c105a | -13.15706 | -45.28554 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 96751d97-1781-32d4-98d0-667bf8213860 | -5.7286 | -45.41793 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51b4f3a6-395b-396a-ab3f-d8a0e515742d | -6.29183 | -42.20005 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 69df34c3-4e2a-3716-ae03-b84db74a4148 | -7.79563 | -47.94001 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f5db19a-7bf9-333b-bfbd-06cfe1a2d8df | -7.39305 | -44.36344 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29e6d13d-7777-338a-b1fc-ccbb6e27ad06 | -11.36408 | -46.53164 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0ea8a5b3-fd79-31f1-8c08-e8c4b58f49b0 | -7.65693 | -49.50063 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 110796e1-d830-3354-a673-70504ac8e29a | -11.46784 | -43.60306 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a88a0f68-e511-3741-8084-7e453edb9098 | -12.13392 | -44.86103 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e449895b-8669-3562-ba0a-818b3832bb51 | -8.44201 | -49.11241 | 2025-09-11 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 73b45674-b74d-3496-83fb-ff87527f6017 | -11.1615 | -52.03997 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58ae2e83-6efd-3e1e-ad49-0ccb0dc94fba | -6.38791 | -43.50687 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7ff24b-1bf6-316a-b9c3-b94ba94fa4d1 | -11.02219 | -44.65053 | 2025-09-11 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec5c2a0a-0e0e-3328-91df-0c4d57edefce | -6.76166 | -39.26348 | 2025-09-11 03:55:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d3b856f4-830d-3c7c-8f34-69b90de16a59 | -6.49563 | -45.2626 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74fd3513-e973-3a88-8a38-2497bc868897 | -5.57502 | -47.60458 | 2025-09-11 03:55:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42bd6b97-0fa5-368b-862a-fafe696e6c44 | -8.16312 | -46.09198 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71fcc733-2f6a-3146-a0c3-2423d6118b71 | -9.30905 | -46.77006 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b88646cf-7218-388a-a8e7-7499f46db38e | -11.15591 | -52.03167 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a417e49c-fd39-353b-bec7-eb30ec27e4e5 | -6.73344 | -43.39057 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7d4a75a-c00c-306f-8a31-b029946018c0 | -10.3915 | -50.51923 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1747694-d82a-32c7-8eb5-7de5cd7f9e46 | -6.42227 | -44.39452 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15e24dcc-048a-32c6-b351-bab2a834e5b1 | -6.91284 | -44.5561 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3943f957-b721-3092-a0c4-c3f01f6711b3 | -8.50813 | -45.66118 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62a1f812-a414-3869-9830-d26eb37e76cb | -7.64079 | -49.81665 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e800d5f3-95d3-395e-a925-c3188dca4bfc | -9.01943 | -49.78318 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2a66401-6ef2-324d-8d97-aa4fce5697eb | -9.53145 | -48.3026 | 2025-09-11 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c43465c1-d736-39f0-a2df-ae7a3527add9 | -9.34417 | -48.93846 | 2025-09-11 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7a68aca-e701-31d1-9a55-b21c70848634 | -9.67961 | -46.76434 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 265f01cd-03df-3c46-800b-87bb40fb2d34 | -11.80562 | -46.75327 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beb2c7dd-2915-30ec-b911-0bd07f481ca1 | -11.96721 | -46.65079 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51aa18da-6f90-33a1-92a5-388c5492709e | -11.0907 | -48.45302 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 226428b5-a787-38dc-950b-956950dd21a5 | -7.38799 | -47.36768 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83a79570-a0f8-3a55-a13b-f97c748e9c32 | -6.63677 | -44.07369 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c516a1d4-95e2-3ce7-977b-9f7ee42a1bdd | -11.47476 | -43.67587 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e09b0f33-b8c3-3941-99e9-e75ef749d417 | -6.17467 | -43.50695 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d43a437-8540-3640-96d7-95d0a2090b26 | -11.4807 | -43.68649 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7aaf2db3-da76-38e6-99d5-0219cbc20a32 | -8.58867 | -45.58546 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7dfc3ad2-5d98-3cd8-b862-176dc52229af | -10.93895 | -46.81681 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be2e7bf3-0c5b-334a-92d8-91a03f00d18e | -12.13789 | -44.86187 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be278270-76f5-3b61-af4a-be4800ea8aaa | -8.58429 | -50.79863 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11cc4b45-7938-3dbd-8f21-c5e57fcc32e6 | -6.6773 | -44.12292 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a02cc95e-6091-3aad-8a94-8896f61c3a16 | -10.32073 | -48.8051 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbc0710d-7829-3a50-be49-2ce638afd5dd | -11.7205 | -48.25451 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1899e0c4-09db-3f2b-823f-a80df06ae002 | -7.39022 | -47.36926 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 520cc9d1-66e4-3185-886f-123c866a38ae | -11.47494 | -43.65202 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73637f88-f963-35d3-a0f8-1ebef690a971 | -13.26929 | -43.74936 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7aa237b6-2c7f-3d3e-a69e-770177c6fb2e | -6.21778 | -43.36995 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 353353b4-42a8-33cf-ac8a-4b56522aa12e | -10.55338 | -49.88835 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f55423a4-f0bc-3500-aead-6fc4ab77ab11 | -12.13057 | -44.8566 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c77af3fc-cf51-323e-97a0-8f1509c2ee4e | -9.29265 | -48.42226 | 2025-09-11 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa403bdb-d50a-3b94-9f7f-fd257a6c2abd | -7.20454 | -40.24258 | 2025-09-11 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab28281d-ca72-3ebc-adbd-d2d67a46d1e2 | -12.00316 | -47.59108 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce23fa77-432a-3c16-b6b3-e90017710c05 | -5.77179 | -45.52962 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec3e10d6-3772-3b14-b0b8-8af14785b36e | -6.76853 | -43.46441 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8394c5c8-a86b-317d-9074-5ff483d961ca | -5.82691 | -44.8365 | 2025-09-11 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b960a35-871d-3400-bf1a-bed4a28a65c0 | -6.25203 | -43.4232 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfb9cdc5-beca-366a-ad14-55f208af3821 | -11.41874 | -43.56775 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc3a859a-5d8d-3868-a3e2-827e46e32f72 | -11.35884 | -46.56018 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| edbaa8e9-8108-36c8-9f73-559a817adace | -11.47672 | -43.61891 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7a433cf-3543-3477-b1c3-dc91cca0a68d | -9.09016 | -49.85384 | 2025-09-11 03:55:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a81f1bdb-176c-3b95-97e9-227c5d02d1b2 | -6.32829 | -47.74523 | 2025-09-11 03:55:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8c17599-ed19-3676-b33d-0d7590a68aaf | -13.23279 | -40.94867 | 2025-09-11 03:55:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 435cda15-f86e-3f5b-8ec6-cf6fe64a614e | -8.16775 | -46.09286 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1750300-992f-31f4-89f7-70dcd34b3300 | -10.7464 | -48.18342 | 2025-09-11 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cdf0871-1f4a-3b85-ae9d-c8e8bd952e7c | -9.7533 | -47.86023 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65f54b46-348e-3e50-bd76-23ffb5c1362f | -11.47277 | -43.64206 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d6858f25-04de-3240-9952-44f1a419ff88 | -9.05435 | -47.06744 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 72acabe6-e780-3480-8a66-5e04c34ad700 | -6.32288 | -43.41707 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c811f0e8-0385-3a61-b943-f386c6e008b0 | -8.74522 | -47.12109 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b338aea4-8711-3db9-99aa-3b4ea3c62981 | -11.36298 | -46.51219 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 157cb766-48cf-3462-93b2-745ebc55dca5 | -12.09873 | -51.01953 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ff9890f-fc43-3e8c-9a8c-4381efb0c8d1 | -11.71343 | -46.50754 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fca08bf8-153b-34b4-84b4-f5221e270e62 | -9.12307 | -46.98152 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3afd1fc-e169-3f08-82b0-743794dedf2f | -12.09962 | -51.01502 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 531d7994-35c2-38d8-9c36-5c3adba6e61a | -11.49372 | -43.65529 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e5bdfff-0202-3766-9c92-d920a7833335 | -10.37702 | -50.53035 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9648d6ed-35dd-37c0-b767-ea83aee716fa | -7.54783 | -42.52812 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df1f1004-4165-3052-80a1-5425cc04d11c | -9.14718 | -46.21588 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d191d83d-f227-34e4-86bf-a4229dc25600 | -9.08194 | -47.06972 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 736d807c-e386-30a1-8b05-0319f89caa49 | -8.48952 | -47.31404 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da9d02ff-e8ec-358d-a3e9-45fc810508fa | -7.85979 | -44.88445 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb826667-095a-30ba-9aac-032d2510ab20 | -11.34371 | -46.49034 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 036b93da-831f-36aa-ba1b-8bfc2d4199b3 | -11.16261 | -52.03455 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
