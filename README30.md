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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41de4d08-0d07-3394-aee6-77deddb22c89 | -6.62117 | -43.88386 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33cf6dd9-7176-30c0-8d45-4d9382cfa1df | -10.71801 | -48.23554 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ed6ae4f-43e8-3d29-964b-dac8804f9c41 | -13.02327 | -45.16145 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5123ff67-011d-3c1b-a1f2-b323ff0b7592 | -7.49223 | -44.94189 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4ef0549-ee8b-3948-bbec-f04af7b3d1a5 | -7.12199 | -44.66117 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75720355-f3d0-3635-8ec5-73a3ef40f3c1 | -9.10991 | -45.18191 | 2025-08-21 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43794e6d-8931-3574-bb7e-2a803f212128 | -7.59305 | -44.38478 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b472159-6374-323a-b665-3d8a3d0fd8fc | -5.79062 | -45.07491 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae6292f8-7f4d-34fa-b68f-13e6abcc660f | -6.43217 | -44.6719 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f17ac62-761d-36a7-839f-701b739753cc | -13.01545 | -45.16748 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47c41235-0e1a-33f1-9adb-f80fb158b0a2 | -12.22256 | -45.40178 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 698728b7-fd6d-3287-901b-ba260941060c | -7.02196 | -44.61109 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad57e3d6-0990-37f9-a519-f3e942422452 | -12.08681 | -47.91542 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d134f3b-2962-3344-8966-fafeb7d4ff24 | -8.77948 | -45.4526 | 2025-08-21 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41bc0b58-3aee-3581-a488-1a2b934a07cd | -7.3035 | -43.68009 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bea756b1-6ad0-3aca-bf1c-3f0a4f5dae62 | -8.83463 | -52.06503 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 656eed50-6add-35ee-9be4-c8818874ace3 | -6.27793 | -43.72128 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4cccffd-6706-32e9-8c3b-f06b8dbf1c0f | -7.64948 | -45.25004 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e123271-ed47-3024-bbd6-8d73c0671a36 | -6.5555 | -42.99795 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1717291a-3e65-3822-bcd4-700a17d94465 | -6.01885 | -44.35218 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aad61e2-fe46-3e10-bd19-067248075abb | -6.58455 | -44.46424 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c38ce41f-c3cc-364f-b2b8-823da2707732 | -6.71523 | -44.32536 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9135b7d5-6fcd-3c2f-9171-762e8fda0388 | -6.41992 | -41.85966 | 2025-08-21 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 123a9021-d7a1-336e-be06-040e90232379 | -5.66552 | -43.50891 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b69e2e8-2468-37eb-86c4-ca936024c486 | -9.29473 | -48.42464 | 2025-08-21 04:17:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77bb2e70-756f-3ba8-9978-13c1673d6a93 | -11.28845 | -46.27941 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2047a235-65ff-39bb-a360-4844a2d905a6 | -8.34631 | -47.50414 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1929135-f7a9-3fac-94c5-c75b4af07c2d | -7.25044 | -50.16371 | 2025-08-21 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85c3ffdc-f376-344a-bf63-def51019d39b | -12.18591 | -47.22256 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7a358b-498e-3290-a239-8a9b22da7dde | -6.08211 | -44.12959 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c572a8a3-9600-3cbc-8953-2f31e77bf0a6 | -7.7381 | -45.73184 | 2025-08-21 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a666aa38-63f0-3fef-bb38-2eac41964378 | -6.53562 | -45.46751 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c24f122c-df1c-3546-aa3c-5633b5d72b81 | -12.97851 | -45.20535 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9312fc97-f040-3d49-a6cf-46af0aebe58d | -6.61838 | -43.8798 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3dd0c02b-9685-3689-94eb-10023288bd9a | -8.16188 | -47.35781 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e891d0bc-41a5-3841-8858-61b333affc22 | -6.01243 | -42.81629 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fccce41-a770-3071-afc8-5c00b70e8360 | -10.22816 | -48.9329 | 2025-08-21 04:17:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97bcd8e5-9d33-379a-a45f-0b37ea0c370d | -6.01487 | -44.35527 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f6891e1-ba0d-38db-a0b6-ac0ac44f8026 | -5.87764 | -48.1173 | 2025-08-21 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fb5f36e-3866-31a8-9429-93cf1576a833 | -6.96665 | -44.15298 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8720780f-b883-3161-aeb7-87a541b22071 | -6.43052 | -44.66035 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 816ec893-9b38-3ac8-a91f-9e9d3d045009 | -11.29191 | -46.28003 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 002c2027-f5af-3c28-a0ad-e10607e3c0ba | -5.74182 | -42.75201 | 2025-08-21 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 897b49b7-fc3f-3b92-9fce-0c14341c66a2 | -6.2644 | -52.81918 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 143d2037-daf7-3feb-bb6e-67c9a3d36263 | -6.0703 | -44.13869 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 697ae48f-7b12-3574-97fe-4e1118304f08 | -6.82005 | -39.89222 | 2025-08-21 04:17:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e2147348-7580-3b6f-83a4-766996b60f02 | -6.94841 | -44.17244 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcf03e34-4407-3b6e-a763-93626d81db0d | -6.4981 | -43.10265 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0633ea9-ff75-3fc2-a911-f58aa119c92a | -9.1065 | -45.18136 | 2025-08-21 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ebe002f-83d3-30d9-bca5-577e44e3c0d0 | -9.52034 | -45.17237 | 2025-08-21 04:17:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca67d914-4169-3ddb-b403-dd31c73eab95 | -12.66621 | -44.96355 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdd8bbca-54db-3e86-a1dd-cad76c4fdac0 | -7.39109 | -43.08399 | 2025-08-21 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4889039d-678a-3567-8253-6845d4749464 | -13.01592 | -45.18591 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c3af9308-f323-3931-af8d-1b846223e85b | -9.29584 | -48.42719 | 2025-08-21 04:17:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30f97ddd-9aab-3976-b080-bec2e8643aec | -7.56842 | -44.40253 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e4ec0c8-fc5b-3283-a911-9820050d91e3 | -12.63727 | -46.87511 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0e6bf14-85a5-31bb-95a3-9f31b3a9100e | -6.77649 | -44.33176 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66c82ad0-4b19-39ae-a466-a5ed78498004 | -12.08561 | -47.91261 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6afc1c-c623-3d02-940f-237e07eb706d | -8.07075 | -43.6878 | 2025-08-21 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51570e07-c978-3a49-beb5-462b7012d96d | -6.09483 | -44.3787 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f7aa937-e2e0-391c-9019-7eaacb11152c | -7.0202 | -44.62193 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d64076d8-30c5-3cba-9f18-a5285934da69 | -11.32576 | -47.83389 | 2025-08-21 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82b42f2c-a625-3fe7-aad3-e239dbef7e53 | -6.20125 | -43.56496 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e0bead1-b6c4-3589-9930-118823abb2b7 | -6.07882 | -43.4456 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31931e96-1ae2-33fa-b643-3b226e65c2b1 | -13.01603 | -45.16391 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01641175-f294-3bac-94be-08f999ab1547 | -7.63913 | -45.24842 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7cbaf0d-7991-300c-83f2-dd8cfc90feac | -5.96217 | -44.13631 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1dec73f-0a5f-38e4-8236-e9f34eea14eb | -6.4979 | -42.97464 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f59bf253-2d53-3ba7-b885-918494e375de | -13.02604 | -45.16558 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 96909537-a402-3b50-aa26-9bbd4b98069d | -6.36575 | -43.25595 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b80d4acc-d123-3375-8a3f-c35b91d78bdb | -7.63181 | -46.26743 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdf38be0-91b6-3fd2-bb71-9c5b56cc8222 | -5.90651 | -46.31546 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccc0c866-bdfa-38d4-b194-fa311daf898b | -10.72865 | -48.2427 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a9f2c17-2b31-3f32-8b6d-2a8f1e55261f | -6.09764 | -44.38284 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f0aa0a4-c871-3fc0-838e-ae1100f23fce | -12.97633 | -45.19764 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a445ed78-caa4-380d-b494-b4dce8d22c42 | -6.3609 | -43.65171 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6536cbcb-a651-3f42-8369-4e894ab0c561 | -6.32595 | -42.90796 | 2025-08-21 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46de5803-2f01-31e6-9a0d-b027b05110c3 | -6.19736 | -43.56794 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d909e677-bd73-3460-bbfc-f57cc251a3a3 | -8.36233 | -47.50209 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aeb62f6-aa65-3846-8221-56855269ac8d | -12.08439 | -40.31374 | 2025-08-21 04:17:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50d82a70-2eb9-3f62-9b81-d04a7c3d9b8e | -11.43694 | -47.32483 | 2025-08-21 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8a88af0-92fe-3bf5-9df7-818e13289f10 | -6.10103 | -44.38338 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985c7ad1-9bc0-3912-89f0-a71e4078b376 | -6.17817 | -44.73056 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1777fd28-e13f-375e-84c7-e542f597efab | -6.9511 | -42.8685 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7963623b-2607-383c-8b9c-e0ece797a4f1 | -5.87867 | -50.15234 | 2025-08-21 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9db1d9ec-904c-3554-8019-595908a9ba98 | -6.26961 | -43.71588 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86f6e795-45ae-3794-a7df-7ba8b5cd032c | -6.6615 | -51.57534 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7587cbe-73fb-3378-9ebc-7a7b44cc7195 | -7.99089 | -47.33527 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 041b5f2a-281c-32ea-959f-09fa20192663 | -6.01313 | -44.36613 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e2e52b9-a6e3-3fbf-8a7e-65adca1ee64d | -5.96949 | -44.13381 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26e76a49-cc26-3221-bc2f-33d75b8cb7e3 | -6.06636 | -44.14171 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56a3d9e8-9eaa-3c91-8c3c-cc067bbc5188 | -9.82836 | -45.95635 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 883949d7-bf73-3c52-94ea-ae31aa6350d9 | -7.03153 | -44.61646 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d84b3243-da43-38af-bd4e-f7e2c980b472 | -7.01798 | -44.61414 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 0e975949-36aa-3232-8255-6d9785118181 | -6.53211 | -45.46698 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13d02c1c-689f-3cf1-8267-6cb90ae0a0b1 | -9.55926 | -48.11153 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f58914a-59d6-398b-868e-4b9fd9250de5 | -10.54195 | -42.54936 | 2025-08-21 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0736aacb-5a60-36fe-affe-18b36ac06b19 | -10.98611 | -55.243 | 2025-08-21 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae42fdc3-efe3-3b35-b57d-dd3bf235b5a1 | -8.83409 | -52.03867 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68741b26-8cb4-3b0d-9327-6c56fedc0cad | -7.02931 | -44.60867 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README31.md)
