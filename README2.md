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
| d87fb403-3854-3e24-82f0-6acf9f4b6f03 | -2.766 | -52.5959 | 2024-11-19 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 68e74d53-9e80-3e7a-905c-845a87710077 | -4.1182 | -51.0486 | 2024-11-19 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 58e497c6-7012-3199-a8ca-f599c27df01c | -2.9982 | -45.1658 | 2024-11-19 00:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f99a855a-249d-3f41-b19a-d7ffdf97422e | -3.4847 | -48.2558 | 2024-11-19 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 00f6c62f-7834-3dc5-a61d-6a2580762402 | -2.9443 | -48.320099 | 2024-11-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ced3e16-7028-311b-ab46-0e7d4896e3b6 | -2.2527 | -51.8792 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e57ac2-fa98-3615-bbf6-0008849fa88c | -3.4641 | -48.248699 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef04c13-eb17-3a12-801d-d825ca5ba7aa | -4.3517 | -45.2878 | 2024-11-19 00:28:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09d567ef-f335-3847-a149-df9e938d7469 | -2.6925 | -51.682999 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7493c9e-327f-3e4a-92fb-bb0db10097d9 | -3.3526 | -50.8144 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db33ceca-f321-3459-9fee-560041fac29d | -1.3695 | -52.073601 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cbfb162-30c8-35f2-96d0-343205250055 | -9.2558 | -45.002899 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a386bf73-9e9c-3854-b1e7-e07ac270da34 | -10.3912 | -44.475101 | 2024-11-19 00:28:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5afe967b-d72a-3e54-bdf1-4cc27857bd29 | -2.5944 | -51.796299 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e22cca34-7c2c-3c69-b118-57a1b1fe1548 | -1.3856 | -52.419998 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd115074-20a4-394e-baa3-8506ba7d1555 | -3.3064 | -54.161598 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d09acac7-9bd3-326d-ab16-087644e6f8e3 | -7.9824 | -44.370899 | 2024-11-19 00:28:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf26e5b-78aa-3402-93a9-0d6eae4fdc79 | -2.946 | -48.327202 | 2024-11-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a0d469c-c894-3135-8414-52b130e3e0bf | -10.8072 | -44.3563 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5527083b-9eda-3eaa-98cb-1c66f889d688 | -10.7521 | -44.3414 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6c0bd0e-746d-3dbb-b93c-3ee4c03167e0 | -3.3542 | -50.8214 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 397a7062-366c-3bc7-ad99-272c1a68731a | -6.3032 | -45.214901 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce0a4fc-d6a4-368d-bfd7-615525e716c1 | -13.2406 | -56.788898 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c13e2255-cdfa-3576-aefe-07e87cda25b9 | -2.5912 | -51.7817 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7afcec64-9024-3436-a7bd-6ee09c7df0f4 | -3.3622 | -54.0891 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83707e3b-890e-3616-9524-a83a6a6c6256 | -2.7508 | -52.587502 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b3aa56-4111-3712-9957-0ddb8f88fd5a | -5.4461 | -49.677399 | 2024-11-19 00:28:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b59f233-8bc0-3b52-8a65-8b018066e840 | -2.3126 | -45.642799 | 2024-11-19 00:28:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0620166-e800-3986-8ee9-dfa18f9810b8 | -22.302799 | -49.757198 | 2024-11-19 00:28:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74df70ea-f4fa-3c49-994a-6da364b972d5 | -2.2984 | -45.625999 | 2024-11-19 00:28:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0f989cc-a67f-356e-b67f-30c0724e72bb | -1.9838 | -45.555 | 2024-11-19 00:28:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e79d044-54b9-39e7-9225-9da51f822588 | -2.928 | -48.066601 | 2024-11-19 00:28:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3817bc55-3599-3bfa-8c12-ad3de4366609 | -2.9247 | -48.324402 | 2024-11-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d6a2b6-2de3-3549-8147-cab2691e63c9 | -9.242 | -44.988098 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1926b105-0ef8-3c82-8a01-ea9881a4f133 | -1.3839 | -52.412498 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe38010-d7fe-3e05-9219-91c1957f1272 | -3.0992 | -53.736698 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c685279-a2c2-3982-a0b8-9aaa1fca59b5 | -7.3854 | -42.7714 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2e0674b-704d-3f35-8d4b-65b781b30fcf | -13.2444 | -56.809299 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c33dd5c-d798-383f-afb0-a2a05e8023db | -3.8758 | -46.935001 | 2024-11-19 00:28:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10ae64ae-50e2-3c17-8158-07af06702973 | -3.555 | -50.247501 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd96f43-761b-3328-8b03-310115ed12da | -13.1657 | -53.265099 | 2024-11-19 00:28:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34c1a3a7-9ae9-340e-915b-35b0e4aba04c | -3.1996 | -52.431702 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c31b7e8-2d22-3998-9193-7a5c45e6f839 | -3.5446 | -51.533901 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4c078e-84e3-3903-998d-e037723e6a7d | -2.6862 | -51.883999 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e083421-f3b8-3fde-ae41-f6745679a003 | -2.8925 | -53.038399 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7be9516-602f-30fc-9123-b48a93d94db6 | -4.8552 | -50.534199 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77da484-85aa-3a23-b109-9ade6a2eafce | -1.7242 | -52.689899 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8aaeeb-5d98-35d7-a4f5-358525f8ae32 | -12.263 | -43.526402 | 2024-11-19 00:28:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55afad05-8f45-3bfb-9286-66bfe2a0a194 | -3.768 | -52.398102 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5b1caf-5918-3d6c-85dd-9dd0c6a69bde | -10.8093 | -44.3652 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9427b15f-e94c-30e0-80ca-2a7267ef6e59 | -3.7533 | -51.915798 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05311b82-7382-3c4f-9e9d-aa0f3b666979 | -3.0292 | -49.4688 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a51da1b-f14e-311e-bfac-f33cb8439a44 | -9.6862 | -47.866699 | 2024-11-19 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be779142-d2c2-3dc3-9645-7fe1a41e7751 | -6.0378 | -46.607498 | 2024-11-19 00:28:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3efad3c-d4b8-3ec9-ac5f-56c8b8152ec4 | -3.0584 | -53.275398 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74dda89-45b2-3832-9083-4bdb3b88394f | -2.6582 | -51.713402 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a27a6359-0b8e-3c74-ba94-731f64c9e70e | -11.8759 | -43.809502 | 2024-11-19 00:28:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a26db6f6-6b23-3015-851e-64d8f0f48238 | -2.5748 | -51.7089 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81057eb7-e6d0-3fb0-9ef6-f5c17994ab94 | -7.5595 | -46.452702 | 2024-11-19 00:28:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1833631b-c786-3ba4-9986-c117ec0f78fa | -3.2661 | -50.520599 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6caf9c9e-eb7a-3da1-81e3-93270adc5c12 | -3.2927 | -45.3395 | 2024-11-19 00:28:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52d17679-c5cf-30d7-abbd-62f31d28c387 | -6.039 | -44.043098 | 2024-11-19 00:28:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7aefaf06-746d-3700-971e-8c9b01528a96 | -3.4305 | -50.2896 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce2d15c-095c-3a0f-a038-aa8f26d6cefc | -3.3286 | -50.477901 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 543ac33e-3d2e-3759-b25e-cb0f4325ce0c | -3.3968 | -50.368999 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37ea9e7b-01e6-3127-8406-eb1d0790a9bf | -3.3906 | -50.341499 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8c0b8e-cd7f-375e-973b-62fec51287b3 | -2.9597 | -51.4048 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af20eff-2dd1-3886-8c45-792311af6779 | -5.3742 | -40.659 | 2024-11-19 00:28:00 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 223f78f9-6206-3abe-b731-c2119c54ea2a | -12.2608 | -43.516899 | 2024-11-19 00:28:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b406b9b6-2b65-3286-96ac-2d927cd64127 | 2.5954 | -50.850899 | 2024-11-19 00:28:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 601e2e2b-31ca-395a-afb1-a12f76a4d7d7 | -5.9678 | -45.368301 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56217323-161c-36ec-af43-8486e44c0302 | -2.8383 | -53.995499 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38769659-e4aa-339c-b036-5d82c3e14282 | -2.9378 | -48.0644 | 2024-11-19 00:28:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b93e0c-df55-35a7-8a9e-50a6d9759223 | -2.2833 | -53.625801 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdbacab-e522-30af-9176-cc313e3a4577 | -2.9739 | -45.340698 | 2024-11-19 00:28:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1505cb-8024-3942-a634-ea2c14c8fe55 | -9.9694 | -48.857399 | 2024-11-19 00:28:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7adc7d2-00a3-346c-9bdf-1f7e3ba9e005 | -2.7624 | -52.5933 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d49e56-2cb6-3e04-8380-b2147b8213d1 | -1.2386 | -52.041302 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c11a61f7-4c86-3b05-b540-5103f54e91f0 | -5.6992 | -43.8251 | 2024-11-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4548790f-21d2-30e5-9cc8-fb05707ee276 | -2.4861 | -49.027 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e97221c1-b003-3ea4-b5cc-8af37c21e8e4 | -5.7374 | -47.909401 | 2024-11-19 00:28:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 41770ac2-c046-3f34-82a3-c23c204a547a | -4.0996 | -43.5877 | 2024-11-19 00:28:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e25d4625-44e6-30ae-92a2-cb40c879151f | -2.8265 | -46.672298 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aac4734-df28-3e30-a4ae-8ed46ff8f72e | -1.6261 | -52.574001 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e910b05b-478e-3d36-9893-9f0eab4c212d | -3.4739 | -48.246498 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a08d6ac-38be-393f-994d-ea4e537d6622 | -3.4723 | -48.239399 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58d00726-21d6-37ae-8687-dbe7e8a1176d | -7.3825 | -42.759102 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 164cf106-217b-30b0-95d8-4d64402dcf77 | -6.3873 | -44.736301 | 2024-11-19 00:28:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0d9ff2-e01d-3ad0-8886-0bcda5c951a2 | -3.5648 | -50.245399 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac88d44-67db-30c8-b67a-6d53ce8d94a9 | -2.6845 | -51.876701 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb6d2c1-744e-39a7-bb14-03fb26f93de9 | -3.0894 | -53.0914 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734b5309-13c3-3ac8-b5c8-3d8f0e4a42c5 | -13.1681 | -53.276901 | 2024-11-19 00:28:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90421a8c-a0cf-3da1-a3e2-f2da5c02cb4d | -1.9246 | -46.511398 | 2024-11-19 00:28:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff0ecac-5fbc-31e8-9daf-453322aa1f40 | -3.6835 | -51.556999 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a08c9f5e-8459-3d14-9c8a-a890a42d8ddc | -2.2735 | -53.627899 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb94d17b-934a-31e7-a119-7aa7fd3c0c89 | -4.1067 | -51.055 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74be7d7-404b-3065-a57a-1dbd00b3c738 | -3.0992 | -53.089199 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d355a04-da96-3ad3-bdbe-9f905cbf092b | -3.2465 | -50.387798 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc42ce3-dcfc-3f72-b3cd-d1ab3a0405da | -2.567 | -45.5853 | 2024-11-19 00:28:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf8df8bb-936a-3d13-b126-ae2e92e8e6f6 | -10.7001 | -48.810902 | 2024-11-19 00:28:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
