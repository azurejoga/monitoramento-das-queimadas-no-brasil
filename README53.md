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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb7f3ea8-992b-3e69-bf26-9e09c44b7a70 | -12.81769 | -47.2248 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 37aac7e3-743f-357b-9377-f9ede674043a | -12.65923 | -47.7117 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a74489a7-c61d-3fb0-ad8b-61a21045caf1 | -8.93163 | -47.73429 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07e398f1-c126-3eb8-8941-156e4a9c6525 | -12.69556 | -43.46991 | 2025-09-16 04:29:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b8bca46-2258-3e03-b883-13b0039201cc | -7.72329 | -44.78268 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3e1f350-a590-3144-875a-70838218b0a9 | -13.21471 | -47.29963 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1daf9d1b-02c6-3cb1-b9d3-1cbb9b7de9d3 | -12.76524 | -47.96128 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddfe31b4-ac0c-380e-aa3d-ee57b14799c3 | -10.63906 | -48.73659 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 096dfd8c-b8a1-3723-aa62-22a759cb76e5 | -13.02509 | -47.96771 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 276ad92e-cfcf-3a65-9ddb-c6c1de1b8fae | -10.37098 | -61.25979 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af6fbbf9-c586-3d86-880c-d2ad34bbd11f | -8.08985 | -50.15518 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8531f19-bd39-39a9-963e-4e62b07be79d | -11.46672 | -48.69603 | 2025-09-16 04:29:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36c78d24-3bac-31ee-b330-9f15d915763d | -11.12601 | -45.34875 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d56aaabc-586e-307e-94a4-c29ed1c07f5d | -8.97427 | -47.05911 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88280a9f-c46e-3b0c-b67c-dd1c514fd60f | -12.98297 | -47.95351 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d64394c6-7f84-3a9e-8123-f10abd48de24 | -10.72194 | -44.75622 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f3a52209-6fb7-3ba4-8a1b-6007708eb995 | -8.11261 | -48.26905 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1d2b400-e4e0-30b5-89c7-e7dd83ee32a9 | -12.68762 | -47.98523 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72c54532-e0e4-3b8c-b33e-80883ab0c2ec | -10.94529 | -45.50261 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f57bebb3-f359-374b-90bb-912d8c7380dc | -10.79947 | -45.98143 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aa6d16a-dce0-3102-a348-9109f840ebfc | -9.05521 | -47.02185 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c423108d-3350-3a82-aa42-ddc09f10d95d | -15.78739 | -53.4469 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58774045-914b-38a0-b973-c1bbdef7491b | -14.42191 | -47.36116 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b0ef9ab-1e65-3018-a684-9e6342ce514c | -15.79664 | -53.45739 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af9f0d6d-bbfd-344e-a83f-28b479c332a5 | -13.70812 | -49.85396 | 2025-09-16 04:32:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a9af064-b046-3031-a0ac-71b38faab702 | -15.46874 | -47.31646 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8569f4eb-a957-3cca-bea6-46c4a15501f2 | -14.84991 | -45.51009 | 2025-09-16 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18d64265-ac9d-3729-8fc2-820bfb22d4a2 | -16.66079 | -49.75879 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f2ab18-1467-35f8-a569-872a0a3dec47 | -18.16106 | -49.20499 | 2025-09-16 04:32:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e99d3e66-a260-32d9-8669-55aa7d8b3671 | -15.8548 | -47.32544 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 594f369f-6223-34cc-b3be-19edbd1d4d1e | -15.84023 | -53.47427 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8545e12f-746c-3f35-81bb-b0c17e9aa6e4 | -18.30761 | -50.19391 | 2025-09-16 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a997251-bfc7-355b-b273-7e6f3965d80d | -19.89066 | -42.04317 | 2025-09-16 04:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0093c234-7b49-3221-be7c-19d571c72ede | -15.41277 | -47.34474 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2968135f-dc97-35b1-93e4-fce5aefc85e8 | -14.53145 | -47.37566 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5844276c-7fc1-320c-8a24-d84b577c82c6 | -21.22262 | -46.94954 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 105404de-1d8c-358d-839d-3631f6b0951e | -19.84366 | -46.45784 | 2025-09-16 04:32:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 16f1bcfd-a8a1-380f-a9ad-027b2a7e2067 | -15.80534 | -53.46161 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c78a983c-21b1-358c-b26c-391a11679e6b | -18.18613 | -47.87246 | 2025-09-16 04:32:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ead1a90-2b3d-39c6-bbd6-51fad9d43f01 | -17.8665 | -44.44781 | 2025-09-16 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 640e5f59-0335-39d4-a700-a5e7e9ff34de | -18.58368 | -48.14554 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f0a69f6-d072-3799-be57-ea5c2c9fc941 | -14.30043 | -49.5293 | 2025-09-16 04:32:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ccd4f46-7975-3c1a-9f18-1aeba74aae23 | -14.52142 | -47.39615 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73ed5c1c-2629-35e3-bbf5-8eac27dea7e5 | -15.83588 | -59.43033 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bff8c605-9c3e-336b-9785-6d14db45e05a | -14.80246 | -51.67591 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 68fb5d8c-afdc-3445-8976-687c0691755d | -21.15606 | -46.2823 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f47c72ce-7113-3731-90ba-2e63098d7e3b | -15.4051 | -41.70718 | 2025-09-16 04:32:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3896b786-5bec-395d-8ed3-d231823fd166 | -14.80321 | -51.67149 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ff8c4b0b-6b3c-3146-8228-136e13c6a775 | -18.58703 | -48.14614 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baa167e8-7384-3695-948a-4e48dbdf2075 | -14.6072 | -46.37988 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e7e11c8-8082-355b-8c09-63f2c0fa5971 | -15.83529 | -59.41483 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a1d6ac4-de44-3f97-bb6c-ceb430354886 | -15.40006 | -41.71105 | 2025-09-16 04:32:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e95087f8-3d43-3d5c-8f61-c9dc4656302d | -16.0139 | -59.2438 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a63b99d-a741-3b0d-82e2-4380218b4ce8 | -21.15542 | -44.30887 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5ff3c5c-c1e0-3dff-b942-985c97a2b844 | -19.38572 | -44.30334 | 2025-09-16 04:32:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cee7ba6-dbb7-32ed-bfd4-63844d5fcbc6 | -15.58842 | -47.94125 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6791b7e3-7eda-39e5-9a22-7635f261ced3 | -14.51206 | -47.32389 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96c203c4-3b62-384e-b0cc-cf866e8943df | -16.42797 | -45.6767 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f976efb-e64e-3183-a91b-e14e474a77a3 | -14.80905 | -51.67534 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e40cdf68-de3e-3e88-a263-20bc310f0f5d | -16.70141 | -54.96941 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2ba4961-9c52-3f78-bb12-ac9d7a47a01e | -17.07854 | -45.82443 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 240cbfde-b859-3b18-b522-2be8f69e1cba | -15.87414 | -59.39363 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b88a0b52-814e-3ff8-baac-37d0887a3e74 | -16.04422 | -59.44593 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f8ce07f-4985-347c-9518-c976729dab18 | -16.68863 | -49.77891 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fd5a00-6b50-3958-8085-28bac731fc94 | -14.551 | -47.37087 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37fd127a-2914-3f61-aae2-7e9dc5b0eff0 | -17.8658 | -44.44577 | 2025-09-16 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcb8646f-fbd6-397c-91db-df1487d819e7 | -19.38639 | -44.29806 | 2025-09-16 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 998f992d-d220-3275-9541-df5802eb8988 | -16.00251 | -59.44179 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4104e41-71fe-3289-b5f7-70fa14d049bf | -17.71971 | -47.9413 | 2025-09-16 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1ec4ce1-431c-3781-b091-cd334f6d0043 | -15.99206 | -47.95174 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90654e6d-07a2-3b26-8fcb-0601fab27453 | -14.61518 | -46.37341 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84c3ab57-cc92-3052-8d92-acc1922d39c4 | -20.2075 | -45.3662 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 1d8c9f46-6b4d-3933-a3d1-ef5e6558d745 | -16.66811 | -49.75632 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15f927a9-612c-378d-a1da-3af791ab5308 | -17.32719 | -46.80058 | 2025-09-16 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48881987-8487-38d4-8c24-c730c8d470de | -14.5343 | -47.35743 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4ec503f-4998-35da-b50d-9c002e9c5871 | -14.42039 | -53.36798 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e84fd19-e29f-39ed-b8f2-bd0ccd292da9 | -16.03741 | -59.44943 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f28ac746-2744-3fd6-8cbd-22f91909a66f | -15.82524 | -53.46579 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1745d205-a971-378b-bf9c-933ac3651eac | -16.43602 | -49.58801 | 2025-09-16 04:32:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f6b5e1-26b9-3018-bc69-d39a1d08a69a | -16.66753 | -49.75988 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a33a627-a793-3f2e-9f63-6ec40af9b5ec | -14.51194 | -47.39095 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27096bd4-963a-3f97-9da0-a58b59b94312 | -19.53309 | -45.38723 | 2025-09-16 04:32:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42491b3f-9511-39ec-9478-b15b84000b66 | -14.65705 | -52.07302 | 2025-09-16 04:32:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a45f6de-60bf-3f82-8ef3-f53968a62cb8 | -21.20222 | -44.36533 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0f79ba91-a44e-33dc-9d7b-c27d1992dba4 | -16.93521 | -44.06969 | 2025-09-16 04:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebe0c8a4-354f-3f5f-84c9-6b9362b9a456 | -14.81137 | -51.66214 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a2b9953-5379-3d96-b510-b58600b516ce | -14.41857 | -47.3606 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18efc735-480b-3d61-9138-ecd75ee1a25b | -21.21965 | -46.94489 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 03837b1f-81eb-3dc0-9779-8aca8a0629df | -18.58311 | -48.14928 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7da26448-ba13-3251-8c54-a9012388d567 | -16.65404 | -49.75773 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7cec63b-01b8-30be-9679-bf9430613f6c | -19.56179 | -49.44198 | 2025-09-16 04:32:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 402e9f3f-234d-3383-bcc0-292a4dab67a9 | -14.80613 | -51.67658 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 582c4efb-7afa-3f99-ba0e-39a029fcb13f | -16.71365 | -49.23089 | 2025-09-16 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8130681-c85e-3abd-9abb-dc2138e192c3 | -15.98929 | -47.94758 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fcbad13-8841-3210-bbf6-7b558016e79e | -16.43153 | -45.6773 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df33f340-9dea-3e70-afdc-8c78cb5b24ae | -17.07914 | -45.82025 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ce787c-a5a3-3e40-8655-797751f7636a | -16.01221 | -59.2518 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe8d18da-38a7-356f-bb29-ce8309739bd7 | -14.38457 | -52.90186 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70816077-7c36-3c98-bff9-9a57f5af2a9a | -15.78642 | -53.45215 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dae0bc70-8297-3ba3-a143-f1b8dd34afeb | -13.76061 | -48.76323 | 2025-09-16 04:32:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README54.md)
