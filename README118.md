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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20d343f1-9432-3579-a4bd-082bec3df241 | -13.01253 | -48.72396 | 2025-09-11 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df3c30ac-5327-3c05-846f-d6278fdec775 | -11.16058 | -52.0311 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6392f098-4cab-37eb-afd0-f0188fadcae9 | -9.97531 | -51.68629 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41f3cefb-7a63-355b-bf2d-3479dc2c2fa9 | -11.35927 | -46.56931 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 561f1d97-2a3d-36c2-b010-f90a89272ef7 | -12.10111 | -51.01844 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bdc2f81-e652-3f67-9a4a-99c2731e9dfe | -12.1278 | -44.87169 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be3a71f9-5b0f-36ef-b148-6a440460d979 | -18.60393 | -43.96904 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af093833-ee92-3044-99c6-0ba75d2be4e7 | -19.66601 | -57.00414 | 2025-09-11 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 188e0736-5c18-3de3-9289-5bae3fbcbbc4 | -20.53833 | -47.62155 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 917872ed-ac7d-35f4-b028-bfdfad10acb9 | -18.56233 | -46.56212 | 2025-09-11 04:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b173cdc-cde2-3c51-b6e2-a2433430a87a | -17.37813 | -52.92633 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 027f835f-07c8-3ee6-a3fe-797d0c16bbe1 | -20.00649 | -47.62371 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ffaac9b-5a8c-3d28-8c20-2a907d4a3f4a | -18.01245 | -47.99809 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b52d84d-f8ae-3a57-95e9-9c20630c2861 | -21.73041 | -50.10277 | 2025-09-11 04:49:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0cedbbbf-f922-3e1c-8c10-22c0b18b587e | -21.72723 | -50.09713 | 2025-09-11 04:49:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 2f8fe7b0-5bf7-3db6-9dde-c55b4181d2ca | -20.086 | -44.47952 | 2025-09-11 04:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fd114fd0-0e12-36e0-98a3-07da888cc50b | -20.24162 | -43.57352 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7b0975ef-98a5-3c79-a604-e8682cf205c5 | -17.73573 | -44.50132 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a35c109-ec3c-3a35-857a-6536ad4a25fd | -17.7056 | -44.43616 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a1bfd73-b12b-3bc1-a119-fd27f0b61766 | -18.60334 | -43.96718 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59848506-8ed5-33f0-87fe-95513b466fe5 | -19.01138 | -46.25375 | 2025-09-11 04:49:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c043fd9-7e9e-3b59-99ab-af11dcc73fc1 | -17.90672 | -44.59205 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81689ff9-f8ef-3909-88b9-d1631611b569 | -20.07178 | -47.5261 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d224ee4-de83-3a96-bd31-75ee1172f6c5 | -16.54386 | -55.177 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1531e39c-6699-3698-8619-b563c10f878f | -17.27119 | -49.21232 | 2025-09-11 04:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86a0b07a-849b-301b-8af9-a53c24b23119 | -16.55746 | -49.74471 | 2025-09-11 04:49:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b30c92-276b-31eb-aa02-279983871eb7 | -18.35326 | -49.33006 | 2025-09-11 04:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db9a5108-5782-3e01-81dc-1b1e4b4f3200 | -20.00022 | -47.63859 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f56d359f-ce5f-341c-8ea2-25dafebd45af | -20.14638 | -47.38113 | 2025-09-11 04:49:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c0e595-0eb8-320c-8c3a-ccc4a02007e1 | -18.01141 | -44.45698 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cb8fdd8-fefa-3330-b27f-9b3b542319e9 | -19.24127 | -48.00229 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d5d6d0c-e4f9-3464-a55b-a206750e83c4 | -17.24495 | -46.75574 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de005d8e-1676-3634-abd7-326d0e5eb9df | -16.18158 | -53.8644 | 2025-09-11 04:49:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02557636-16f9-3158-b404-a346177da33d | -21.56815 | -51.92801 | 2025-09-11 04:49:00 | NOAA-20 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 20fee335-8d63-31fb-960a-9e143327cc3c | -21.91335 | -47.9116 | 2025-09-11 04:49:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca316e93-a61c-311a-88bd-032c7e17e177 | -20.39601 | -46.27814 | 2025-09-11 04:49:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b53f4b5c-1031-3022-91c1-dd59b8079da3 | -20.90579 | -45.28575 | 2025-09-11 04:49:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cfcb8a53-5eab-3405-a1f4-2e45be404c6c | -15.60331 | -58.3054 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 136a499b-a0a0-35c9-9ff6-1a4e193a8283 | -18.76673 | -48.19376 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ccffc1-ccc9-3a79-b017-2dc5a7708ddb | -16.53643 | -55.17948 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9b850213-9aaa-3233-9364-1bf8f6a9be4d | -17.72711 | -44.4345 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8917b05a-1612-3531-bd64-bbd193cdf7c0 | -19.75188 | -45.19086 | 2025-09-11 04:49:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6881fcf-0dc1-3899-9ca8-29a7a2acd893 | -18.34557 | -49.32879 | 2025-09-11 04:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d00cf34-1f96-37f1-b1fa-7be059f8077a | -17.32282 | -46.68032 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32e1392c-0a98-35da-a08a-4097dc3ddd3a | -20.84898 | -54.98943 | 2025-09-11 04:49:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16f94ad8-8d25-3293-af0e-d9465de4d1d6 | -16.6328 | -49.76394 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d74e7412-4358-39b6-bad4-89f81e16e8bf | -22.83625 | -47.46809 | 2025-09-11 04:49:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d6b84115-68ce-3ae0-9c19-69a6c143958f | -20.00053 | -47.63651 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae600a42-64e4-3024-95a8-1f308345df4c | -19.65942 | -44.9012 | 2025-09-11 04:49:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7d6c386b-17e4-3a7f-9ae1-e18ac53b3121 | -17.34007 | -46.70342 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a3ffc94-3519-3daf-873e-6adec6b27972 | -16.61192 | -49.77891 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f08d4ad4-0b0e-3ba4-9543-e9f6add6c99e | -17.83734 | -46.74124 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b21c824-e3ac-3820-8f62-f906f47f98ee | -19.54983 | -46.94709 | 2025-09-11 04:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 049ee9c4-92f3-358e-84c8-a3d8804f21d7 | -16.51418 | -55.16502 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 492e9652-61ee-38fc-a275-29e9b21cc145 | -19.10641 | -43.22408 | 2025-09-11 04:49:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bb0ffe19-0d94-3e57-aed6-62132ae635e3 | -19.9844 | -47.62225 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3adf45d6-ce6c-3930-b065-341c00198fa2 | -20.89087 | -48.30394 | 2025-09-11 04:49:00 | NOAA-20 | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8b4fa5d-2776-35a8-9c70-feefffb99196 | -17.26661 | -46.08187 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 067f1e6f-2b6c-339e-9822-b10727a2e840 | -22.32054 | -48.82764 | 2025-09-11 04:49:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f5f45a6-57b5-338b-9696-5ed57eb2afdd | -17.83342 | -46.73584 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 486638d1-dd8a-3c5e-8512-65758ec338b7 | -17.79394 | -44.40956 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f9fe6b3-ed57-39b2-92c3-88709d22fa9f | -17.95025 | -44.48493 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9a9260c-8c6c-3a88-8e97-54731d082004 | -16.57896 | -49.31424 | 2025-09-11 04:49:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e73d3814-c92d-31b6-83e0-107822096b53 | -18.01221 | -47.12968 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8d5928b-71a4-3eac-89f9-77429f14221b | -20.07443 | -44.74724 | 2025-09-11 04:49:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc888f9-794a-39cd-a9a5-da4487000970 | -17.84773 | -46.74477 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a600f54-8d47-3cd8-845a-fcf4b96ffbd8 | -21.728 | -50.10468 | 2025-09-11 04:49:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 08ff7dde-18c3-3abf-b8f5-31c05835d640 | -16.56242 | -49.7362 | 2025-09-11 04:49:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b725bad3-3431-381e-952e-bced20a0bad0 | -16.61128 | -49.78354 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2a2cc64-1cfe-3572-ab89-e5c1ea3c401d | -17.8238 | -46.73932 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51ec19c5-679c-384c-83a9-79e3f08b2145 | -20.16176 | -41.03878 | 2025-09-11 04:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4392f5a2-93d8-380a-8540-16226a843286 | -18.01175 | -44.45379 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffb3bd95-8e73-35e9-bd6f-e3dba718b9a2 | -18.45154 | -49.57314 | 2025-09-11 04:49:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8834639d-7210-3c31-be25-90c8b6090721 | -17.3234 | -46.67573 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22cd9e71-1a95-306d-8ffb-6bf6fed27868 | -19.22755 | -48.0087 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8eb64f3a-f981-348b-b1c7-40479260a382 | -17.73583 | -44.45214 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73a70eb1-e347-3158-912a-fa8ff10b7618 | -18.05784 | -50.73092 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c0b02a0-0ff6-33f9-8692-a6a8e596ee31 | -18.62222 | -44.26766 | 2025-09-11 04:49:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b63bec2-2306-339b-8726-0381562e1176 | -17.50375 | -43.75481 | 2025-09-11 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b52aa4a-14c3-3725-91a5-07aeac6577fc | -21.34028 | -45.79574 | 2025-09-11 04:49:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e65e8aad-f718-392b-ae8a-be8255a49fcc | -19.98815 | -47.62799 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6fd77d8-2dad-3721-9dde-35cad22b4f53 | -18.34536 | -44.36422 | 2025-09-11 04:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba47f358-3424-3200-834e-75851445a6b5 | -22.79445 | -47.80483 | 2025-09-11 04:49:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b03828e9-8750-33e5-9442-0859d03d237b | -19.10686 | -43.2197 | 2025-09-11 04:49:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 708e4e70-193f-39b5-a08f-adb0a9862593 | -20.53778 | -47.62606 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb5c17dd-38d3-328d-99ab-6cf4b7680dd3 | -22.81927 | -47.0392 | 2025-09-11 04:49:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a0ee021-c3fb-3a93-9c53-6448aaf258eb | -17.79887 | -44.40667 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ace20eb8-d54e-3473-8c36-4b55d1104a7b | -19.99827 | -47.61765 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef42c52b-0482-333d-bba3-9449585fcd20 | -17.47009 | -45.10461 | 2025-09-11 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 405e4bf6-49b8-3209-898c-269465dd7374 | -16.34708 | -52.94491 | 2025-09-11 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1452bbf-8b58-396b-ac59-2a8731a80be1 | -15.34197 | -58.88144 | 2025-09-11 04:49:00 | NOAA-20 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142145b8-0316-392e-9a48-8d2668e0d792 | -17.98886 | -49.37279 | 2025-09-11 04:49:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9d889e9-8068-3fd3-ab64-d919db8ce7a7 | -20.40143 | -46.27329 | 2025-09-11 04:49:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2eb1999-f68c-3489-9975-15a17ec3535e | -19.34986 | -56.71089 | 2025-09-11 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9c0cc845-e5a8-32ca-b564-81c54d9f1650 | -18.07877 | -51.03616 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34801060-55c3-310a-a60f-b47ab05bbc64 | -21.3453 | -45.79658 | 2025-09-11 04:49:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 03353495-4354-326b-a61c-d82cdb9471fe | -16.51481 | -55.16123 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9eb85b1c-4e5b-30f0-8cbc-60a96bb34506 | -15.8757 | -54.93 | 2025-09-11 04:49:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ad837e7-6dc1-34f6-9326-6941c845b8e5 | -20.17173 | -44.62347 | 2025-09-11 04:49:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24d5f030-c909-3103-8884-088d8a0fbc49 | -17.24384 | -46.76476 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README119.md)
