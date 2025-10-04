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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f9136b5-ae54-360a-875e-d91bbeb5857a | -3.45505 | -43.3346 | 2025-10-04 12:17:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 07a060f2-c2e3-32a2-9759-da187582f26b | -7.04839 | -45.80034 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3fab7402-6e13-3862-97c1-1ea43bca4d52 | -8.56302 | -47.65211 | 2025-10-04 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f151f64d-b4dd-3c55-bd16-f7b9e36a9944 | -6.39169 | -44.77797 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 098a70f7-2e4f-30be-9b73-2a11c0bd6b52 | -5.66004 | -42.74004 | 2025-10-04 12:17:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| ebcb4d83-1399-3174-a3cd-d5fc1fa6da4e | -8.23348 | -46.8101 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b51c822c-33e4-332e-9bc0-b45bd52e59c8 | -8.84934 | -46.81462 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7b03b99b-e9bb-3509-b606-108201bc86ac | -6.30867 | -43.46766 | 2025-10-04 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f5d8de61-a271-38cb-be0f-712ba570aa3c | -7.05492 | -42.76812 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 677423a3-1c13-3b96-917e-9bdc48b6f900 | -4.99131 | -45.42144 | 2025-10-04 12:17:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d9630d71-a7ca-3a23-9bcb-70629a153794 | -8.45211 | -47.65709 | 2025-10-04 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 095f15da-baf1-3b2e-b417-9180f8492149 | -7.01187 | -42.31086 | 2025-10-04 12:17:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 878a608d-84ef-3ebe-b434-479c3b292576 | -3.44355 | -43.34452 | 2025-10-04 12:17:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 411430a7-026d-34e7-9a1d-9e58f8bf637d | -9.11474 | -44.39875 | 2025-10-04 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 312ecb4f-4492-322f-b1c3-5615a030606b | -6.72908 | -45.97315 | 2025-10-04 12:17:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 71cdad0d-4a25-3c11-9be6-e4c48a740c1d | -7.77404 | -46.27578 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 9c557e2c-9bf3-303b-959f-ed0c08bd64c1 | -6.46263 | -44.58502 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f2eb7661-202d-355a-91d9-d13eacc97f74 | -5.82927 | -42.88885 | 2025-10-04 12:17:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| f1c6cf00-6360-3098-97f7-42313dd4a048 | -7.05103 | -45.78163 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| db197778-0b2d-314b-bfb1-783e4046e047 | -5.48691 | -44.10497 | 2025-10-04 12:17:00 | TERRA_M-T | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 24b52693-1b2f-30eb-978e-6a877175f50b | -6.37393 | -44.62997 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bade9b94-152f-3029-8c9b-97367a65ab44 | -6.71529 | -42.81065 | 2025-10-04 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 476264ea-8f09-3846-ad2f-1f4688c2f0d5 | -7.91993 | -49.64177 | 2025-10-04 12:17:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b7a64a88-3be8-3184-9b70-19dcf667edb8 | -6.24607 | -44.22508 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fa6797b2-c1d9-368f-9982-58168631bc37 | -7.26956 | -45.26915 | 2025-10-04 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cfa12c99-79b2-3e75-a9aa-5f372583670f | -4.95897 | -45.06704 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 83dfb88a-04c9-3858-ab0a-755343470287 | -6.34101 | -43.45963 | 2025-10-04 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f8e68a37-67e4-3f52-a81d-3ba540f3f1eb | -7.80736 | -42.53638 | 2025-10-04 12:17:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 4955f3b7-8268-371f-b011-5977d772780e | -7.85665 | -48.20674 | 2025-10-04 12:17:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ba623932-5282-3f07-990b-e6830dbf6b09 | -6.1542 | -44.60826 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0f97c373-66c8-3372-8992-6f54979a24f2 | -8.8455 | -46.84164 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c6998aea-f405-3602-a274-14c18ab055bf | -5.4725 | -42.7696 | 2025-10-04 12:17:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 2707cce3-cffb-3be5-af96-4e578f43d61f | -6.499 | -45.18838 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 875e0c61-a1ae-3586-9770-2746fdd014fa | -6.4423 | -44.80083 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d1a19f5f-8032-3191-b0ff-7ff0e9113feb | -8.14579 | -44.08386 | 2025-10-04 12:17:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 02f8fdb6-cdf4-3931-bad9-f03c8001e499 | -8.52469 | -47.21482 | 2025-10-04 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| dfcb8438-9dcc-32a0-8492-c61bf148e2fe | -5.95831 | -43.49328 | 2025-10-04 12:17:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fa109338-4576-32d1-862e-6658e71c7d26 | -8.00991 | -47.33734 | 2025-10-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 35a43252-4141-3726-af48-a81927fad8d5 | -8.10031 | -47.98818 | 2025-10-04 12:17:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b7ef2e2d-4553-3dad-b2fa-b0937ca7c47d | -6.06791 | -42.51436 | 2025-10-04 12:17:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 969511ec-987d-3283-bccf-97f694f65d52 | -4.71691 | -47.20829 | 2025-10-04 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9a891806-96a7-38c7-9fb0-3469218a747b | -8.85833 | -46.75139 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 2a570ecf-d016-3f4d-9808-77df5825ec5f | -6.35531 | -41.62448 | 2025-10-04 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 997f5230-b271-32bf-bb44-692b7a273ba4 | -8.82905 | -46.76575 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34e883a1-0b87-3ca7-affd-c6a90f482467 | -5.76603 | -43.47927 | 2025-10-04 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8b1ef284-d846-39f9-8ca5-478b14c93814 | -6.06437 | -42.5215 | 2025-10-04 12:17:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 4fd3af48-28ec-3a58-a91e-13ec8fd8fc35 | -8.4473 | -45.67953 | 2025-10-04 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da0a6485-4b12-3709-8a44-ca7aef0c7031 | -4.83629 | -45.15 | 2025-10-04 12:17:00 | TERRA_M-T | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 52eedb50-e54d-356e-bb59-39e1c5e0bfe4 | -7.77021 | -46.23796 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ecacd8ef-bd56-3636-a6b2-c645d6e708ae | -7.11093 | -45.08411 | 2025-10-04 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3fc619af-4165-3715-a39d-3f6c5dbb98f8 | -7.36999 | -45.54571 | 2025-10-04 12:17:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 112cdfa4-38f9-3e51-8486-94b1de0f9c7e | -6.66522 | -42.82594 | 2025-10-04 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 8fd3311c-b3bd-3907-ab75-65737f570886 | -6.16226 | -44.61988 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c08f9418-215d-30e1-a246-2b0a7f869beb | -6.28163 | -44.04035 | 2025-10-04 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0cc68729-741b-3ca1-b47e-e34c29a49cbd | -7.05745 | -45.80153 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 445b41d1-26fd-3762-944f-4f5451fc81c8 | -7.77552 | -42.60125 | 2025-10-04 12:17:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| aac37ce9-798e-3f92-9b7e-d0adf599e37d | -5.95671 | -43.50511 | 2025-10-04 12:17:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ec3f7461-747c-397b-829c-e1ebbb4e4578 | -8.46763 | -47.424 | 2025-10-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 32f92454-2cef-3afa-a4ce-cdf16f3584ef | -7.47671 | -43.04954 | 2025-10-04 12:17:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| eda6cafe-75ff-325b-8e38-068392959b92 | -7.04039 | -42.79439 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 0e670e51-50e0-321c-b173-74cc636fbc1f | -8.19584 | -46.99854 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 78157336-3385-38b9-b538-d3fab2751fe5 | -7.15238 | -48.28761 | 2025-10-04 12:17:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| acf6b56a-e78a-32a5-80d5-a9bd736ead03 | -8.27861 | -50.25214 | 2025-10-04 12:17:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 5bb5c696-bd72-3436-b548-28e02e401ad2 | -6.80683 | -43.78848 | 2025-10-04 12:17:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b3f73903-2a2b-3063-9b48-a27b10b138f7 | -7.86689 | -48.19895 | 2025-10-04 12:17:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 03b3ef87-3bdd-32d1-8789-b4dacb8b43be | -8.17687 | -47.00495 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| ee8e6f13-40ab-379b-a7a9-0d6e48793330 | -8.11851 | -47.28642 | 2025-10-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 03a0a4ca-5614-33ed-9cf7-ed206bda5b52 | -5.84768 | -42.79168 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 0260513e-1370-3bce-a1a5-1a3691dbcfea | -8.53353 | -47.21607 | 2025-10-04 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0c99e767-089e-3d39-993c-dfc7339a313a | -8.8976 | -45.01759 | 2025-10-04 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3519ddc8-8984-3320-bdca-343e2598286b | -3.6872 | -43.14008 | 2025-10-04 12:17:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a810131d-04c2-3de1-8dab-08a55e73feb1 | -6.85815 | -43.93669 | 2025-10-04 12:17:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 29c6071f-de0a-39d6-bb14-fafde30f0f1a | -6.24314 | -44.24624 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 38916bd7-6deb-3bc8-a58e-ae51f72cfcb2 | -6.34267 | -43.44745 | 2025-10-04 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 453d7bb2-2b07-3e66-84c0-66e1909da939 | -8.58885 | -46.24798 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 016f9238-5e26-3906-9d08-c5825ffb8b34 | -7.04186 | -42.7605 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 40a4d251-42c2-3d8b-ac54-b87533b43219 | -7.77532 | -46.26663 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1a2dcce9-5b16-3043-a849-8e1ed565acda | -8.16657 | -47.20277 | 2025-10-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6fd1d83b-d478-3fa6-b38d-a88585b44450 | -5.99249 | -44.34484 | 2025-10-04 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4d6fdbf5-bd0b-337e-9b16-b8dc02870869 | -8.22265 | -46.81119 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 65ff3d81-0a44-3c36-adc6-4b86d757c340 | -6.31891 | -43.46891 | 2025-10-04 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| ed900613-61dc-308e-91c0-2fa8010d52a6 | -6.16367 | -44.60963 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c6000c15-f50e-3f6d-b9f1-c50afd135016 | -8.59013 | -46.23872 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 87101718-a1e0-3342-9a70-8ff5f8557ecc | -13.13198 | -47.8117 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e007b5ad-40ca-355b-a80e-dd1ae34e63bf | -13.19074 | -50.98212 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 265.1 |
| 79287bc2-a10c-3c30-b401-5469149d8591 | -13.16219 | -50.97765 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b4bddd11-9232-33bb-8b1a-3bfacd90f508 | -11.64006 | -45.06107 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a14651f0-a4ee-3f9e-97b3-a4d5f89293d9 | -9.91788 | -45.9571 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 0a18a40b-f2ee-303a-92df-107b531a83fa | -14.69491 | -48.10287 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 88984cfa-c69c-39a2-bf94-a617db5f6339 | -15.94298 | -48.98651 | 2025-10-04 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| dc1ac906-03c2-3bdf-b64b-0c740a00c481 | -11.50382 | -45.00645 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4952e2cf-4543-3a3b-b181-70960a7ac482 | -9.32039 | -45.75222 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 54356a5c-e65e-33a3-8870-0ca8a4e645ae | -18.68104 | -45.014 | 2025-10-04 12:19:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4a956da7-0768-3c6f-aef0-53d51a75c9dd | -9.29107 | -45.96545 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| aac4f79c-8b36-3137-8fa3-9efc6b2cc02a | -13.14004 | -47.9584 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d4c795fc-b734-3ea4-bfc8-f8b8a1e1f71a | -9.96983 | -45.78375 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cca850fe-7f1a-3a97-8301-687e6f8157f4 | -12.03978 | -45.19629 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 05408e7b-2c54-3965-b657-c8eb6d60a5e8 | -13.97265 | -48.19062 | 2025-10-04 12:19:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 789dacd6-aca3-3614-83e7-f4a5e83eee4e | -15.56151 | -46.95988 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c1297de-2b30-3c91-8014-71cc05d03f15 | -8.98147 | -50.26865 | 2025-10-04 12:19:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |


[Clique aqui para ver as próximas entradas](README139.md)
