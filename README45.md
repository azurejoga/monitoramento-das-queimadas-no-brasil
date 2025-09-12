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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1cbdcb1-eb7d-317d-90b7-a717a47ecc93 | -11.98231 | -51.15181 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bb90bcd-81c4-35bc-a834-a64cb9f0169e | -11.2247 | -54.90276 | 2025-09-12 04:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| febdcfda-ee2b-3af6-887b-981a7f08b35e | -11.53479 | -50.41423 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2698e0ca-b70f-36a2-8ce9-17359d62a851 | -12.58314 | -45.68594 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c36b176-9482-32e7-8576-85b5d2a33e53 | -16.49622 | -51.97738 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37994005-0952-34d6-9cac-a4a37ac1a739 | -16.65664 | -47.62859 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac2cc2e5-6b02-349c-a1e0-f37971ec2304 | -17.281 | -46.0858 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7500a9f-2098-3f77-b739-a4fba80e0370 | -18.05366 | -45.43847 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eaec6f15-14d1-37d7-8984-8aa6c09ac61d | -16.5982 | -49.81351 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36bfb0d2-c148-32f3-ad00-02b540700866 | -12.14181 | -44.86676 | 2025-09-12 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13259bfa-b63d-37d6-a556-d69b42d67eef | -18.11431 | -45.33326 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3a4924f-25f0-3f5e-b59d-ada6f446e1f0 | -16.49136 | -51.97364 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4109b03-5b27-334d-aa7c-701f914151e8 | -14.40126 | -52.93348 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87c5aaca-d905-372d-9725-5255f71e5676 | -16.81204 | -47.82771 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f7c6269-9fe4-36c0-aa10-bd1862544c41 | -11.53076 | -50.40636 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 766e0512-3ade-3dde-bc08-0a923595998b | -13.91239 | -48.2661 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0716875c-59cf-377a-9091-c20a4214f752 | -17.43382 | -49.22922 | 2025-09-12 04:06:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7778f98-f2d8-372d-8777-4ab4d3fd41e0 | -14.41852 | -46.4044 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 864c3bca-0977-3e86-99ca-3b21aa33649d | -11.99791 | -47.56711 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb9de7f5-7285-3c4a-a9dd-095818576580 | -11.52176 | -50.59766 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d4a227a-09b9-3412-89e8-4d05a603f6f4 | -17.5879 | -42.17109 | 2025-09-12 04:06:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 96d94bab-e791-39d7-bc2d-cb9579120d76 | -14.28701 | -45.08372 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47f95581-5103-38ef-a85e-e9cc7496d343 | -12.92937 | -48.0018 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa9eeb8b-b0c1-30a9-9d5a-9ee778d1c0df | -14.18297 | -46.19688 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b36f2b40-1193-3c2c-b81d-e22bb1f48c50 | -11.69771 | -50.59969 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b8f0b5b-2b8e-3bbb-a72f-e3ccf89358b4 | -12.56178 | -44.68024 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8479ac70-dc95-30e7-8102-ca19db4a8fac | -12.83079 | -52.96523 | 2025-09-12 04:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70b864ff-591a-3fcd-9b1b-2efdcac71782 | -12.15189 | -48.68898 | 2025-09-12 04:06:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aa0cd38-faf3-3819-a6df-87a32cdda173 | -15.07927 | -48.00632 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 090d9fb0-147f-3cfe-b2be-d3cebd9d26e3 | -11.73271 | -50.62122 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f873d77-5dc5-3291-9b82-36852438acb1 | -12.47017 | -47.49637 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a92d34dc-ca63-3414-bbe5-d2e639f0dbba | -12.84841 | -52.9766 | 2025-09-12 04:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e75173-5795-3797-a4aa-0efd18775650 | -17.20601 | -50.15228 | 2025-09-12 04:06:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1fccb1bb-f87d-3931-b619-5f2ead6eee38 | -14.18344 | -46.17153 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f99d10f2-514b-3eee-9124-b841e6c5a019 | -17.34765 | -46.69602 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66c325f7-c3f2-3f71-b681-26b6e6f5eba8 | -11.9591 | -51.18214 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d83dc0b-277d-33a6-ad31-7399dff91bac | -14.131 | -45.38503 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78d4d441-1d29-3977-9c99-f22db70923e7 | -13.19919 | -51.75444 | 2025-09-12 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57b9cb14-3bd1-3b24-ad83-29cb27e6079d | -15.78894 | -52.24102 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1de8ae70-54b4-3879-92ac-bd718263c7af | -12.85508 | -47.95609 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75d8f54d-958a-3ae2-95d5-25083ac2b43e | -17.77207 | -43.45379 | 2025-09-12 04:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d886ea5c-5cbd-3234-8632-e3258987a1ca | -15.6866 | -47.0435 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e43a7796-4a33-34c4-848a-2529dc8b4428 | -18.05222 | -45.4469 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07930a84-c472-3719-bb44-5d1dbb63a2f9 | -11.64381 | -50.58243 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64246141-f4c0-375a-90f3-6bb88bf76973 | -12.24628 | -47.33865 | 2025-09-12 04:06:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 060df464-438c-358f-82d8-0a65e4478d78 | -11.19035 | -55.06831 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e377177-a121-318b-8992-bf01f30a215f | -18.02105 | -46.8625 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a92a4d83-531b-3809-bd43-2916aaad9f95 | -16.49748 | -51.97115 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e14c1ec-1073-32c8-9593-47601f5f91a4 | -18.05509 | -45.43003 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 89998013-0931-306a-9979-54c667eb6523 | -15.7888 | -52.23666 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0f40b305-b2c9-30a7-9199-b2c989ef1db8 | -14.1744 | -46.2 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ed09463-d17a-38eb-8ca2-044bf7a37204 | -16.40145 | -44.04913 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0673f01b-4af6-309e-8ece-c3ad18a087d0 | -12.827 | -47.95893 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c38153e4-a874-3649-93d9-6adf3f252b18 | -18.30918 | -45.01501 | 2025-09-12 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 636185d0-6bc9-3931-a6f5-0962f7242784 | -16.25206 | -52.65573 | 2025-09-12 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ad697b6-b308-3db3-9776-9e56d768effe | -15.56183 | -41.79054 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22a2461d-b497-32b8-8704-96532386d48a | -12.09395 | -47.58252 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 215dfb2a-532c-376a-906a-8b21f134b5fe | -16.28717 | -45.68481 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61eaf703-2a31-3e8f-bdf3-2f360c32de84 | -11.69751 | -49.02101 | 2025-09-12 04:06:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20875b24-2b0c-3885-a936-75301b5e168f | -12.92846 | -48.00688 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a3067e3-ac97-33de-a83a-098c917482d3 | -18.05255 | -45.43657 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28a162c3-5e77-383e-80ae-15995d5f81a3 | -13.36286 | -41.92198 | 2025-09-12 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed9ae3fe-5190-33cd-a900-bc28efcb074d | -11.5274 | -50.39514 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c25ca50c-4288-3b44-aec2-438c021a1841 | -17.80214 | -42.57159 | 2025-09-12 04:06:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e341758-2e87-38ee-81a7-262bbd94b084 | -15.0829 | -52.44937 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b76f380-b9d9-3b32-84a8-bcfe1b7724db | -11.79006 | -50.56633 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de40bcb5-f4d1-3998-ad15-ec299e1536ba | -12.98538 | -48.01187 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3977440f-840f-3f81-93b0-dc9269fd05f2 | -13.25616 | -43.76676 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5de18285-e03b-376f-a4f7-285acdbbf1e0 | -13.00572 | -48.00105 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 241bcd6a-848f-31e6-b4fb-b83dfd5d6bf6 | -12.90242 | -47.97313 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7aada750-d601-30c0-8cb0-f5d08e667c13 | -15.78954 | -52.23311 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c0964cff-956c-3013-9d99-55a4d4e109cf | -15.74204 | -48.38006 | 2025-09-12 04:06:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fac444a3-3bce-351a-aed9-f707463cbdc3 | -18.05964 | -45.43791 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5777ff09-fd1b-30d7-abde-0dc85945715a | -12.56819 | -44.73048 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c20c91-00f3-3a23-9bb3-8964f5da3b40 | -15.53428 | -48.54517 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d958885d-8520-3232-9d1f-80286d5acefd | -13.33669 | -40.34397 | 2025-09-12 04:06:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5dee61e9-d016-302c-92f8-2de20d2eafb5 | -11.97546 | -46.64598 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27ac3f28-d6cb-31c3-9f49-10a92cf04530 | -11.52543 | -50.4053 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1a4f7b19-1df2-319c-992a-1d4e7c0d613d | -15.69126 | -47.01746 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3401170-0822-332b-9ba0-39f7d457d926 | -17.93696 | -46.92485 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 630dac03-5931-3439-8fc1-4f4083742db7 | -16.193 | -47.86362 | 2025-09-12 04:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6d92597-afa3-3c72-8e93-c7810e5a88b3 | -16.59352 | -49.81253 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 142e2e9f-e5fe-355b-ba8b-023857feba1c | -14.12806 | -45.37984 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a388e0e0-3701-3c5f-970c-ee4f1778200b | -17.56478 | -44.55343 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94210831-8e34-376b-82d6-ef81a2d8a4cc | -13.17303 | -47.26364 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43afafba-0e5d-37fb-bb03-815efa7b7b0a | -14.74384 | -46.29167 | 2025-09-12 04:06:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e79ac413-0315-3d7d-8195-e17fd3834228 | -15.78974 | -52.23703 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e0b4a253-ea37-3af9-8816-ba77b98848ea | -18.05757 | -45.4288 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc826b0-f3dd-3fbd-a5c7-0981f4c99e2b | -17.8173 | -46.7368 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4baa2b2f-3ec0-3280-87a9-c8a0889b3072 | -12.93377 | -48.00289 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ac8aed0b-67a2-3686-9d89-f9a756d7abbe | -12.82978 | -52.97006 | 2025-09-12 04:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c97bf6-17f9-3017-bb16-a1ea8e0708f8 | -12.80333 | -44.75496 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b6785f0-840a-34ed-8465-1e043277e1e0 | -14.12436 | -45.37916 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 794322d6-06c3-39df-8b7b-52cd801a4de3 | -11.51977 | -50.39421 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 073ece88-c1d3-3b8e-82b7-111a3aa82b80 | -12.98931 | -46.74736 | 2025-09-12 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae427642-25b8-3061-a7f2-68063e53c92a | -14.13177 | -45.38054 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b9f110b-cf4b-332e-9b5d-3829e151a67d | -15.22969 | -44.03551 | 2025-09-12 04:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a94706a1-f3e6-3875-b5fb-96f01be94edf | -16.44299 | -49.04369 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c1089da-e310-3eab-8887-f801b62f1022 | -17.35907 | -46.69829 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e20e0085-ce63-3882-aa37-2afba5bbf67c | -13.58495 | -47.69225 | 2025-09-12 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README46.md)
