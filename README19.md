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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a189f19-eb87-3083-a84a-524b1d513412 | -3.16069 | -44.32872 | 2025-09-22 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbe608cd-0ac8-36e8-a198-f461631e0f52 | -12.43492 | -45.14272 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 814936a9-46a0-38d3-ac4e-73270063090b | -12.0759 | -44.79923 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 08f9fda9-c5d2-356a-a612-af4c7e19ef8f | -7.94027 | -44.09425 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c825ecc-9d47-311d-b08b-f63a56067447 | -12.71486 | -47.70091 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3dd4ea3a-e77d-3cd7-8158-248e43c2b2bf | -11.27058 | -47.47135 | 2025-09-22 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 78925807-2cd2-3365-a0db-feed06092f1f | -6.01026 | -44.33216 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5db41acf-f8b5-39dc-8d0b-b88033bd760b | -7.44371 | -40.10048 | 2025-09-22 04:17:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 03be9557-4712-33ac-8202-b51a0a1b1c73 | -8.00739 | -45.7241 | 2025-09-22 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5ad6b92-0834-338a-bbd1-9719b0127011 | -12.98292 | -46.37584 | 2025-09-22 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d072afd-ca03-3a31-88e4-ab4ef873d808 | -1.63246 | -48.67772 | 2025-09-22 04:17:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b541cc0-dc4a-3831-8aab-ec6eaf72d1c7 | -12.73241 | -46.82867 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b69179-a8b9-3987-8546-97fbfaff33aa | -4.87512 | -45.81048 | 2025-09-22 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d47d732d-a72c-3fe0-8d5d-82a772f7297c | -6.61374 | -44.5982 | 2025-09-22 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e059bf6d-9e64-3e77-8ead-0094d44a8808 | -11.74044 | -54.72561 | 2025-09-22 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2effe448-d92a-3326-8e62-189eaef52c6a | -11.32291 | -54.3474 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4979872-b9b9-338f-b090-4d5340bc04b8 | -11.52148 | -54.68406 | 2025-09-22 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29c1742e-781c-3919-b142-f888c40cbd8c | -11.32774 | -54.35262 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7edb57ee-bd1f-3238-b4b2-409d9f2a9a6d | -4.30761 | -48.09491 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c13d2d2-cc6b-3ec4-9782-a3372bd0addd | -3.94725 | -53.39185 | 2025-09-22 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faae5585-2e64-30ca-9c4e-8cb76da22a59 | -7.3671 | -43.8448 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0afb4f14-3813-3477-89ca-0cb5340aaceb | -8.80545 | -43.0243 | 2025-09-22 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3d32848-636e-3e2f-80c7-9158fe1b3e09 | -7.79773 | -46.19089 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c24b1e4-fd55-3892-9f15-9b6269fb484e | -12.08016 | -44.85816 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba3fb99b-3e49-3e56-ac30-3ee253c97859 | -14.35172 | -47.78868 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60cc13df-b220-3268-b6dd-2ec6d4a5901b | -4.8722 | -45.80572 | 2025-09-22 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df77cfdd-bc8b-3eca-b0cf-ffda72a643a3 | -13.31852 | -47.29526 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09f5e30e-33f3-37a0-b01c-39c0186a11e4 | -5.65679 | -51.46326 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b70f795b-3a95-34f0-a7fc-5297eaa4e583 | -15.09272 | -43.83799 | 2025-09-22 04:17:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6868afcb-894a-3bef-83cc-e95c467830c1 | -12.74309 | -47.75406 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dec07c10-b8b8-39c5-8fd2-703e86911c0a | -11.55523 | -48.58943 | 2025-09-22 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e52cbc5-e750-363a-88ee-55698afcc680 | -5.55892 | -46.27802 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c60bf6cd-488b-3bb6-8fac-409b5bea54a2 | -11.46087 | -46.93802 | 2025-09-22 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55c72ca6-75d7-3656-86c6-62f9beb18e1b | -8.806 | -43.02078 | 2025-09-22 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb894c91-1bd7-3474-ba8b-89d7416557c2 | -12.43435 | -45.14629 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1eeba43-62a8-32a1-97c3-7d22fbf9357e | -3.88352 | -38.39511 | 2025-09-22 04:17:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e90f1e6c-ce3d-3dfd-95c0-66cdec036fff | -8.0115 | -45.72081 | 2025-09-22 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76e3c3e1-c466-3376-802e-70e4b620ab8a | -11.28674 | -47.50895 | 2025-09-22 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a868032e-ff02-36d9-bf0f-9a57c5d90416 | -12.07477 | -44.80632 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7b0ebb5-20f0-399f-ba14-dcbc6086af74 | -5.65573 | -51.46929 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef64cc0b-070f-369a-84f5-52feb468f838 | -0.95269 | -47.36116 | 2025-09-22 04:17:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ea303f1-bec2-3b8c-9f00-e68874dc36af | -14.84337 | -45.47923 | 2025-09-22 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 278e2620-3016-3e1a-9476-853b81daf9fe | -3.86018 | -40.34294 | 2025-09-22 04:17:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb0cd63c-9674-339f-9ac3-7c0caaf65c58 | -7.93638 | -44.09723 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 183f2cbe-2c8c-38e5-8b61-6924d32bff21 | -5.57066 | -42.12984 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 79929733-0809-3816-a38e-a264100e8bd2 | -2.26323 | -47.84525 | 2025-09-22 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10e05331-0373-3c4d-95f4-7bf28d009bdd | -7.84893 | -45.14632 | 2025-09-22 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 378a3319-041b-33d0-a711-57af8cac77b0 | -12.06966 | -44.83824 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9d66c84-2ffe-34c6-b639-bffe978e4098 | -5.56258 | -46.27863 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14b77310-e4d9-3428-92cf-80537b798ccb | -7.93526 | -44.10425 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65f9152e-bf02-3091-8552-fb95ecaf61e4 | -5.03342 | -43.60708 | 2025-09-22 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c3e0c48-3635-3072-992f-a59fbbd1134c | -7.61387 | -44.48119 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4de9bd4e-e3ed-3744-9c28-43cf69fd62e2 | -6.04124 | -44.13917 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d072aa2-9b16-3f16-b1e9-75030d4a1271 | -7.17068 | -44.43601 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11e850dc-8d8a-3471-92be-c5234c023715 | -12.75032 | -47.75539 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18c614de-638b-370a-bd0e-4b7ef6542c4e | -14.44305 | -46.52765 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0a20128c-7270-3a5e-9c5e-4842d8c3bb17 | -12.74077 | -46.88565 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70469ef7-b510-37c6-b58f-34478bdd804e | -11.77681 | -43.76529 | 2025-09-22 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c06ea43c-6ce8-3fa9-96fc-34e78ca632c6 | -12.74011 | -46.88957 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c44864fa-f18f-3cd3-8803-57add8d51061 | -6.4434 | -45.69037 | 2025-09-22 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b560bc9b-85b1-3677-b071-99dd2d5ad443 | -6.08734 | -44.08801 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d2d7590-5dde-3a8a-aa1d-eb401a1e49dd | -11.63582 | -44.33663 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f92673c3-cba9-3d04-a9d0-af35f5c1b698 | -7.61066 | -44.43683 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8c16352-e290-3969-b154-f9a25940d8af | -5.65328 | -51.47113 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1971f405-9732-328d-960e-5e031602ff50 | -13.68211 | -47.70751 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0af7e68-b2cd-3e53-b661-566d392419cf | -7.80705 | -46.20097 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70d2e89-a896-3879-84d2-49a0c02518ec | -7.60481 | -45.49204 | 2025-09-22 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaff3e5b-ea58-3a1f-a2bb-87669d3654b0 | -14.98907 | -42.23971 | 2025-09-22 04:17:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1adc1a5a-106b-3fd9-b5cc-ea426fa4e38c | -13.31078 | -47.29809 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afa59c74-edea-3943-8529-160f4364ba91 | -14.33251 | -47.79386 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e781c866-e0ec-3a9f-b5ac-adf6b3b955cb | -14.44704 | -46.52463 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34f1fa6d-0091-3ef9-b2d1-c85d9e46c46b | -7.28996 | -39.93746 | 2025-09-22 04:17:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1cbfdf93-a2f2-3c35-92e0-935cff69a7d8 | -13.72682 | -43.90652 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0dac3f8-3294-3a31-a869-c1c1aef92a85 | -12.33327 | -44.09429 | 2025-09-22 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 388b42ad-57d3-30bd-a3cc-01e550b61275 | -0.79831 | -47.60266 | 2025-09-22 04:17:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a19e78a-9234-3a55-b67f-3375e118ddd1 | -13.7378 | -43.78244 | 2025-09-22 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 501cfde5-fde2-3dbb-b39b-5c8d61a1b81c | -20.18513 | -44.62808 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38421522-2b31-3f9c-b1ed-c0294c9807cd | -20.61241 | -46.07456 | 2025-09-22 04:19:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcc9eea5-d61e-3b8c-8c56-8ffafdd10f3a | -21.14174 | -46.33679 | 2025-09-22 04:19:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a8fbf8fd-ad6f-31ed-b900-dc30062ece7d | -22.41257 | -46.7958 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8ad9f185-6eae-36b1-934f-81d11e5efc4e | -19.90016 | -44.59873 | 2025-09-22 04:19:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 724dd6e1-de8b-38eb-9151-f02429d4c2de | -17.0527 | -44.90672 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 885d070d-6274-3a70-9657-21541674efe0 | -19.85087 | -57.30378 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 00a2a1da-0e6d-3a1a-807d-5c3054243bab | -20.99911 | -46.5134 | 2025-09-22 04:19:00 | NPP-375D | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 05b30e8b-105f-3cbd-a4c2-ecd7b8ebaf74 | -20.43957 | -43.67754 | 2025-09-22 04:19:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8a0be57d-c39f-3984-aa04-37cd84ccf88d | -20.12509 | -42.47565 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 14b9b6f6-9595-3c52-aa96-2be70b2cfa2f | -11.42133 | -43.52295 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46bf8201-9b6a-3611-9a00-f1bff2696943 | -19.84894 | -57.28545 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c28d7ef9-1a76-396e-addc-534e1d56ad8a | -8.85631 | -46.16112 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29003363-89ee-3daa-adb4-1205b0aae349 | -22.41101 | -46.78397 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d91ff47-807a-3a21-b0c8-cf3e278239da | -16.31318 | -43.03961 | 2025-09-22 04:19:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 116e8b57-5996-3643-8121-07e2dc860bc5 | -18.9877 | -44.22591 | 2025-09-22 04:19:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b570c4aa-8a1c-3cea-886b-27bb9fc55130 | -20.26116 | -55.49929 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 92e48ce6-8616-39a2-bbc6-cac6786bbccf | -10.34641 | -46.07415 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff61b8bf-2444-3437-a88f-3b3e0a29b890 | -10.37861 | -46.08259 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 844e24d7-e79d-3905-9f25-9aaa4d6ae359 | -20.50456 | -56.87941 | 2025-09-22 04:19:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8062a59-21f9-38f1-83c4-646b876055e3 | -20.26758 | -55.49427 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbb13f23-a64c-332b-b86c-fff6295d7dc8 | -15.77135 | -59.41075 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba19e772-b082-3210-82bf-ab528e0bc9cb | -15.15698 | -49.58302 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ff29078-9430-372a-a3b7-ca99bc523b4f | -7.70994 | -55.45379 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README20.md)
