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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ed9453f-62ff-3294-b9d4-530c46646ef8 | -7.88385 | -44.01818 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e802e8db-e69d-3ef4-b1aa-b3492cbc69d4 | -6.67156 | -42.04099 | 2025-09-23 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b620975-9e51-34b8-a3b0-31dd0ea3c5d3 | -8.52633 | -44.97267 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3eea11f-f6e1-3ace-a100-75439e6a768b | -12.06504 | -41.60826 | 2025-09-23 03:57:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91e6ea07-fdf7-3e70-a519-b7a7df713816 | -5.88573 | -42.82603 | 2025-09-23 03:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1492dce1-e546-30da-bfff-854518305ca6 | -7.49811 | -35.25072 | 2025-09-23 03:57:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4f81e270-b1b9-3c8c-bfba-1a5ab05f57f2 | -8.13796 | -44.4729 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f892120-f91a-348f-b77b-69deca1779e7 | -7.16593 | -44.43824 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae679ff6-fb91-3dba-b57e-8fc6b18b8190 | -8.13835 | -44.46807 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2303bf8-579e-3abb-868e-5b08d6234f08 | -5.23672 | -43.6945 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8672e27b-3ccc-3596-88aa-93adebcc97ad | -4.59836 | -46.59427 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e9149c-45a5-31b2-8f0c-5dc04b60e8f4 | -5.68136 | -46.364 | 2025-09-23 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c490debb-aee5-3079-8a16-2c1fd69de51d | -11.82226 | -43.16293 | 2025-09-23 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 94603ec4-4cba-35c9-b688-a67b4462beb9 | -9.99036 | -46.27938 | 2025-09-23 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 906c9788-63d5-3708-adbe-466dccd23acb | -11.52868 | -43.61521 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5ba9a09-14e4-3745-8069-61a021d4575a | -5.94697 | -45.39596 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 848d5d10-48f9-3d65-9ac4-cfed7e8d90f4 | -7.90091 | -44.01756 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af5a761-05fe-3b79-ba80-c86a7315ad3a | -11.02066 | -45.88982 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b346a53f-f584-342d-92ac-097380b1b3c8 | -11.89242 | -41.27479 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e63ee4f1-de79-37be-8a36-4df2f168543f | -7.36349 | -44.54491 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df167034-06e4-3e9c-88e2-2f403cd157ef | -4.3845 | -43.28524 | 2025-09-23 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c496250b-f6a7-3e30-86e8-9f7b14c9d92b | -8.01507 | -45.45473 | 2025-09-23 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a3f4e97-4e1f-36ce-8e6f-aeaa5e54dabe | -5.55548 | -42.73936 | 2025-09-23 03:57:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3f55f22-3481-3a94-9f37-966c079b0318 | -9.99325 | -46.2897 | 2025-09-23 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea173aa2-c418-36a6-ad46-9a17c8bb56fc | -11.45507 | -43.52709 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3687cd7a-3e14-3aa1-8b69-ce7694794aa9 | -4.8595 | -45.74527 | 2025-09-23 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c47bfd4-3202-39da-96cf-171fcbe81dc2 | -6.25806 | -45.33918 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d99c4fbd-faf3-35b8-be76-87de8236fb96 | -7.03597 | -34.91002 | 2025-09-23 03:57:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8067581-9c3a-36f0-9398-7424012d8da3 | -9.51 | -37.9655 | 2025-09-23 03:57:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 47fa9595-053e-3d94-bcea-db5435bd1f92 | -10.3149 | -45.22838 | 2025-09-23 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7541232-0220-3000-a684-cda716f23deb | -5.6207 | -43.46727 | 2025-09-23 03:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fce17c7a-b2b5-366e-91a8-5dd8b5006130 | -6.55546 | -39.89404 | 2025-09-23 03:57:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f5c9eaf-303a-3075-9ab1-82eba4161a40 | -4.79719 | -47.28078 | 2025-09-23 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc4911ce-4147-35f1-8f10-28db71db0606 | -11.5227 | -43.24725 | 2025-09-23 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa125b87-e416-3f63-bcc1-303a85dabea0 | -11.02183 | -45.89256 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a7fa07e-3182-36f8-b39f-81837244dc22 | -4.78507 | -47.25438 | 2025-09-23 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0bbceb5-d023-308c-b72b-f0dd6aadb037 | -6.20804 | -42.64471 | 2025-09-23 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 75a92b75-3ca7-38d0-9e99-72ab792e327c | -11.52944 | -43.61765 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 707cf043-03f3-30ff-af5a-5ffe4f9a86d4 | -9.19275 | -44.62234 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 124c23d2-4c99-3278-b6cf-80aa0248eba4 | -4.48101 | -47.67284 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47df5013-4646-30ea-b3e6-feb8d06e7547 | -6.77384 | -38.31113 | 2025-09-23 03:57:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8893ccf0-f4c1-3b21-ba65-ef00f8ad23b4 | -8.00803 | -45.71198 | 2025-09-23 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2495168c-c52c-32e1-8193-e621bd9c1759 | -6.59666 | -44.54895 | 2025-09-23 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21078879-909c-37f1-8225-90aa201e9d14 | -7.88257 | -44.02551 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ebb40994-642d-3b6d-957b-6f18956f2623 | -11.46641 | -43.52919 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 053ed50d-d45e-3132-98b7-56a28b8e8c74 | -11.46263 | -43.5285 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9565c063-a49f-33f5-b9dd-0d45f61a9970 | -11.4413 | -43.52264 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28307463-dfce-33ee-9018-0a8072eba497 | -11.53246 | -43.62299 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 259c0c60-e41c-33b5-a45d-aaa48b1ead7c | -6.09716 | -43.15374 | 2025-09-23 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4e969e3-2960-3778-ba8b-fd34875aa4bb | -7.26703 | -42.99511 | 2025-09-23 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8c02c3c9-7892-3be6-97d5-ea890b8533ad | -5.87698 | -47.20985 | 2025-09-23 03:57:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8dd634b-9338-37c2-a223-0948d6a3d755 | -8.8034 | -43.07397 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9481e732-57f4-35c1-baad-1816552b1a11 | -4.4935 | -48.11444 | 2025-09-23 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 001cb182-a4ba-3b3d-b965-e3517ddca8a8 | -11.92061 | -43.43068 | 2025-09-23 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3061fc35-5bc8-3777-99da-7041e00338c1 | -7.06075 | -45.05313 | 2025-09-23 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b224f502-af5d-3cf0-a856-fdc03ff8ae28 | -6.40752 | -43.76683 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fc3f2bc-3ade-390d-86df-12892d7f57e1 | -7.28546 | -41.86744 | 2025-09-23 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 968c46be-e202-3cf5-9a47-88c8b4596c8c | -8.13862 | -44.46902 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c45c1c6d-11c5-33a7-a1ab-85b953f17755 | -6.44455 | -45.66405 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c61a650-734f-3ebf-b5f5-af6589889a92 | -4.07663 | -48.04478 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 653926a6-3435-346f-901d-7677addeaabb | -7.04324 | -41.99784 | 2025-09-23 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0d83778-2002-3e9f-a9cf-b30d1ac625d8 | -6.3412 | -56.2009 | 2025-09-23 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| db16e3fa-f413-3461-8416-bd31dde77033 | -15.92825 | -38.94235 | 2025-09-23 04:00:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85c07729-ff67-3554-97d9-962f184b9587 | -13.41268 | -47.55939 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cbc32b00-7c2e-315a-aed9-ab4c30604cf5 | -12.76512 | -47.50058 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| efb78933-2e38-39dc-8e8b-f93a18b988ab | -12.76614 | -47.4953 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac43679f-baae-3be4-81e7-b13dfe07c4c4 | -15.59071 | -42.39202 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| eba7834d-9d19-3959-9ec1-fa98b2af1748 | -13.42118 | -47.54293 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05e81bb6-f16d-397d-a4b8-1d490f8556f5 | -13.42502 | -47.54848 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45d8a883-f920-3a2b-aee2-5799e10ec7db | -13.81105 | -41.82566 | 2025-09-23 04:00:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f5a72111-966e-3bd9-b99e-61723214707a | -12.83414 | -42.96498 | 2025-09-23 04:00:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2f3654b-69a5-35aa-b08b-c2b783dacb1d | -13.56076 | -42.56392 | 2025-09-23 04:00:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 02a3d1b3-e8ac-3c76-9b0c-cda716017eb1 | -12.78923 | -47.47799 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8f6ca97-0b5f-3e9a-8899-b20e0a794fd6 | -14.6449 | -42.49476 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d6924043-799d-30ac-a5dc-3f0ef6e50a24 | -14.55679 | -42.48736 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae9d3401-d744-32ce-8d9f-99cc744159d4 | -12.90513 | -43.18464 | 2025-09-23 04:00:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46824927-7bb5-36fa-94ec-e93b94bb22b0 | -13.41541 | -47.54742 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96a8f212-2f6d-3b26-ae49-84e548de7592 | -13.42315 | -47.55579 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faabf2bc-a1bc-3884-9e73-cfd83ac2006c | -14.38785 | -41.20476 | 2025-09-23 04:00:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 4e751428-8ff0-3959-b821-80dca92e28dc | -11.99947 | -47.75449 | 2025-09-23 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b2bfe8d8-a0cb-304a-90f5-0f5ae46fcdc5 | -13.56352 | -42.2252 | 2025-09-23 04:00:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 291104ce-96ee-360c-a130-2a25c82f3de3 | -14.08391 | -41.44337 | 2025-09-23 04:00:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c92cbe65-a316-3121-9c23-9bb2b2927160 | -15.58001 | -42.4138 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b9b447fb-762c-3bb6-a77b-8f41ffc65c65 | -12.7777 | -47.48663 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1fd7ed6a-d9b4-3d28-b45f-7176d6a73c43 | -13.41631 | -47.54275 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 736bf6bf-30fb-3f72-b0ea-ed241c3135fc | -13.40786 | -47.55893 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14d01a18-fe2f-326e-94d8-3d973484042c | -16.61476 | -40.58248 | 2025-09-23 04:00:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 89bbe31b-33d1-332a-97d4-6e4da770f27f | -13.65291 | -42.51019 | 2025-09-23 04:00:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c837fe45-d7a6-3499-9c79-2b44efa57890 | -15.92484 | -38.9418 | 2025-09-23 04:00:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 24ed0bef-8923-389f-8340-f8c4a0668a2a | -13.51414 | -42.3492 | 2025-09-23 04:00:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 15e442a3-fda0-38a0-b4d3-7110accbbfce | -12.96877 | -43.52715 | 2025-09-23 04:00:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d66bf9f-eddd-325e-b89d-46a809753b2b | -12.83355 | -42.96603 | 2025-09-23 04:00:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34d3c63e-4510-3cbc-8b19-291d00a7d08e | -15.58344 | -42.41443 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 9bfa5f2d-5bb8-328f-80bf-fc59199bc603 | -13.2686 | -39.88779 | 2025-09-23 04:00:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 850e2e85-ca09-3280-a3e4-a7cf0adcecbc | -14.38668 | -41.21199 | 2025-09-23 04:00:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 271bf96a-52fa-3317-9ad5-53b751dc2e00 | -14.64536 | -42.49779 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c545c6e-b822-3a15-b47a-72f9d3e6a5f0 | -12.13072 | -44.30146 | 2025-09-23 04:00:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be9496fd-b86b-3240-acf4-64db50d56677 | -13.40864 | -47.55704 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a951240d-ed32-3aa1-96e9-51c5c79bb1b4 | -12.75457 | -47.50723 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b982450d-3268-3371-a1d8-5a1856705636 | -15.58664 | -42.39526 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
