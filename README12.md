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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c714330f-7a2a-3e49-b499-16e924c4adca | -11.11862 | -54.6661 | 2025-05-22 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74c9fa86-8441-3a88-9ab0-30a63ad3c981 | -8.78569 | -49.0769 | 2025-05-22 04:21:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37784926-96f2-3450-a9ba-9454f9353135 | -9.67533 | -50.95603 | 2025-05-22 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7170119a-dbd6-37ec-a8d0-da308edc5128 | -10.54838 | -42.43081 | 2025-05-22 04:21:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d3a577c7-faeb-3120-a4e1-61f8c6386a67 | -11.57331 | -54.57089 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0d5f16a-2ac1-3d06-bca0-379ee117b130 | -11.29829 | -53.98306 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec6bbc16-ebb2-3df5-b7dd-30a663ccbd74 | -10.93833 | -55.31894 | 2025-05-22 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 653593e6-1982-313c-a2a3-5439916d0c55 | -10.36096 | -47.97081 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6861636f-8b33-3ad7-900d-ce7cd4baef81 | -9.02156 | -47.75319 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ed3aee1-2738-3365-93e9-3336a7562daa | -11.08039 | -54.78299 | 2025-05-22 04:21:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e7f0f96-2649-3cdb-96fe-9d4ea7f861e8 | -8.73827 | -47.98471 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3586bfbf-a684-3c0a-a307-a2f3ea8bcc55 | -12.10819 | -49.29766 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c8422b0-d3ac-3301-82f9-376ccfebf15d | -9.04492 | -47.02375 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf5f056b-abc7-31f1-a791-958c53a8cc13 | -7.1048 | -44.36848 | 2025-05-22 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e577a88-2353-3a92-a419-bf753ffbab8c | -7.58024 | -45.8581 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e745c46-9eeb-3be1-87b7-15ec12767ec3 | -12.08077 | -47.34627 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ddb67fd-af8a-3f0c-8441-6a158f2ea562 | -13.89664 | -41.30117 | 2025-05-22 04:21:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ef165e9-c85c-330e-acc2-74519c192851 | -11.57446 | -54.56481 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 430fcf76-282d-3af6-81c2-6fbf6aedbe30 | -7.80377 | -46.21038 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64f3372a-a824-30ad-877e-75c4cb90375a | -7.39331 | -45.94022 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74bfb70e-e072-309b-86c1-52e6fedd13db | -7.23691 | -44.71493 | 2025-05-22 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 784fac97-b9ee-3b5a-9551-0c187d56c057 | -11.56149 | -47.44532 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8a9fb721-4514-3fc7-8eaa-2acaf10165d3 | -9.60418 | -49.01804 | 2025-05-22 04:21:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 232d4c1c-a6f5-3b9c-8150-01c013997b32 | -11.07696 | -54.77254 | 2025-05-22 04:21:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e873a6fa-7f71-35c5-a8ab-0b7069bb1386 | -7.24356 | -44.71598 | 2025-05-22 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bfb1dea-468b-33e9-8619-0f7b04766b1c | -8.48149 | -49.60421 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80d1916c-eac1-3c59-8a60-8e411d55799c | -13.67109 | -53.94172 | 2025-05-22 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 715c46db-b115-30ba-9d6a-18ae37a672f9 | -12.13368 | -54.65665 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2d3cea-f860-3f19-924f-2f823a3c186d | -12.29575 | -52.4874 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bbff294-960d-390c-8a63-79cd03b26343 | -13.47518 | -52.27796 | 2025-05-22 04:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62e4d9fd-fbe8-3fce-b2f1-dbc3aad6362c | -12.66739 | -58.21537 | 2025-05-22 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95b2eb24-b68c-3ba1-8cde-b4670130c255 | -15.69541 | -43.41932 | 2025-05-22 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9e925cd-c40b-3ca2-a653-e5bc3c9aa515 | -14.03294 | -53.38246 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4807e0dc-7ccb-387b-9ca8-3fb9959eadde | -12.2978 | -52.50122 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 80d17924-513a-3934-822a-4ee80a7da6bd | -15.07842 | -48.94292 | 2025-05-22 04:23:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96e92a8a-ac1b-3d8a-9f19-4725a002d105 | -13.66995 | -53.94372 | 2025-05-22 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6852d36-11ce-3ab4-a531-a06d53e3ae78 | -12.27336 | -57.26886 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 345798b5-a4a8-3c92-babd-f48da71f0c5a | -12.42051 | -54.35821 | 2025-05-22 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e53c850-68aa-39ca-8287-4d1cbf29b06b | -12.50544 | -57.21609 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d744d976-0c40-359d-bd64-a79246d25f01 | -13.58784 | -47.36045 | 2025-05-22 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 480193c1-725c-3727-8c4d-54da2e3756cd | -13.38764 | -48.45131 | 2025-05-22 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38934c48-f7a8-3880-ac61-4bd50b5d987e | -12.67258 | -58.22201 | 2025-05-22 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e347da0c-0bfd-3d72-bac4-f8880d61f623 | -12.49949 | -57.21493 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cb10859-e34b-3b6b-ad95-ccfc39af9f88 | -12.29341 | -52.50039 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 39c99681-7279-3733-9949-9f577b94645d | -12.2862 | -52.49006 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66a497eb-e2b4-361f-b704-bf3c17e7e81c | -12.28119 | -57.26107 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21c979f1-86c9-3aca-876e-2a76a6012edd | -13.06692 | -52.02351 | 2025-05-22 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64d7a005-a1c8-3e81-aa99-526b0ed23f2b | -12.49047 | -57.18775 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42dddf1b-c832-3b45-9fa8-4e7feb877e13 | -12.69135 | -58.13089 | 2025-05-22 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd08fee7-c8b9-3ea1-a290-6ef2d8a8eefa | -12.28463 | -52.49873 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c951f2f6-10a9-3dcf-ac63-f9b604948f35 | -12.29059 | -52.49088 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90b152cb-ece5-381e-b872-fd80360a7ef3 | -12.13201 | -54.66558 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf9bf2cd-4e10-31e1-8301-3a44a9ddaa99 | -12.64328 | -57.19091 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96b98cc-7906-34c4-ace5-badc1d103f78 | -12.27939 | -57.26365 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c7fb7b01-6009-3edb-88f2-ea142fe6e717 | -13.69669 | -45.27098 | 2025-05-22 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bc7328f-22ba-3771-83bf-0a52d8a5264e | -13.66244 | -53.93156 | 2025-05-22 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67d986ed-c4ea-3b88-8306-796717c7921c | -12.13506 | -54.6617 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909ff139-c3c6-3840-bd7a-dd860123f124 | -12.13312 | -54.65961 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87ae6a46-1687-3766-ba6d-256b2a4858b8 | -12.13448 | -54.66467 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b57a3e1c-f655-385b-946e-348c59e41dd6 | -14.05152 | -45.53143 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| accad188-9fcd-360d-a751-6e73f1aba054 | -14.02931 | -53.37692 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d0ba1b5-cff7-3c3c-8238-ea75f622e34a | -14.01885 | -55.14042 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc15c790-d7bc-3f33-b183-d3f37af0f86d | -15.74451 | -43.48759 | 2025-05-22 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cc95710-5846-31be-ad12-212983fe00c0 | -14.03921 | -53.37405 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98af82d8-c076-3f38-9dfa-b94b9558f143 | -12.72116 | -54.97509 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5eccca46-a062-3616-a72f-75c7ea2f0ec2 | -14.05429 | -45.51327 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9832d7b4-ddcc-3eed-b1c3-ef584c56a753 | -14.01613 | -55.12746 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3baedfef-c16c-3cde-b379-552187f98032 | -14.01496 | -55.1334 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a751255-d64b-3522-a48b-82b328e29d3c | -13.06324 | -52.0231 | 2025-05-22 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c41bec-88b2-3145-b716-cad0b4904a49 | -13.80367 | -52.89482 | 2025-05-22 04:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01b1e406-d411-31c8-afb8-382f3fcd5e27 | -12.64414 | -57.18665 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7a125e-de6d-320a-a0c5-f683b92cbe3b | -14.02002 | -55.13446 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7563c35e-ea8d-3d67-a427-5d4d3056128f | -12.28698 | -52.48574 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d33566e9-4c18-3b84-a88c-4b5059e09160 | -14.04871 | -45.52726 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 439b349f-ef8f-3463-bd11-02ab53d14e90 | -14.03833 | -53.37869 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aeb9ee15-1808-31ac-8ee9-d2a8c17b2873 | -12.72332 | -54.96942 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e9f0317-88a6-3f54-9dea-913ce10fbb6e | -15.69478 | -43.42373 | 2025-05-22 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8607dd1-9189-370a-8ec8-8161212518dc | -12.27849 | -57.26818 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7923c5c3-0fb9-3d2e-ae29-2e3fbf647ae7 | -12.28027 | -57.26558 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b60eeb0-a4a0-3b96-9581-0d6b715085dc | -14.05765 | -45.51381 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fc902a4-8ce2-3f4f-96d6-a590664fbefa | -12.72232 | -54.96894 | 2025-05-22 04:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c036da0-4ca0-3fda-bb01-a8b2b382a484 | -12.41943 | -54.36381 | 2025-05-22 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8592dbe-1060-3a37-8a87-02419b99a6f5 | -14.86586 | -45.12038 | 2025-05-22 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8d31b63-acba-3bb4-852b-707277d7d5c2 | -14.2319 | -45.8307 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5a8ab9ac-7406-3515-9e5e-71a7ad70962d | -14.02957 | -55.13945 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d23ba4f-7e3b-34e7-be87-6a5b3e5dce87 | -12.29498 | -52.49171 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b92ee8a1-c0ae-37b6-b611-bed31b7b6ab9 | -14.01437 | -55.13639 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3346411-e6a5-3317-9d09-238ef146bb5f | -14.02392 | -55.14141 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a23205fd-1194-3d75-af1f-2102ff2cad1b | -14.07092 | -50.4277 | 2025-05-22 04:23:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d091f402-c2f2-3fc3-9609-aeaec0b74c59 | -12.30091 | -52.48392 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 453985fd-8988-3e58-92c9-0b1c4c3688c5 | -14.03016 | -55.13645 | 2025-05-22 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c860fc6-34b7-38fa-b5c1-b9f1a97958f7 | -12.30014 | -52.48823 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 070f8817-dbf8-3805-b665-8c9d38dd86be | -12.30219 | -52.50207 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dff83e11-edbf-3be6-bd40-6c5d08e7d32f | -12.29936 | -52.49255 | 2025-05-22 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcf4dcaf-2d32-3bce-a547-1e737ede534c | -12.50383 | -57.21384 | 2025-05-22 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef8fb93-d706-3695-a4fe-1f614c6029aa | -13.78279 | -54.30854 | 2025-05-22 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1a6b4f8-51c4-3c58-bbf8-6c8df63225ed | -14.05709 | -45.51744 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e052a650-596e-3eec-bac5-c07413410351 | -14.03867 | -45.51477 | 2025-05-22 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3a7c3c6-9e32-36e1-8b3e-d1991a084f41 | -12.41967 | -54.3635 | 2025-05-22 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3f3e504-70ae-3619-8d07-27b2cb2a31da | -13.19626 | -47.27304 | 2025-05-22 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
