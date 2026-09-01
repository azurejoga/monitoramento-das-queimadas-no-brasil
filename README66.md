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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52e5852d-d6bc-312d-b344-fa960f1c5bc7 | -14.50731 | -52.23366 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99f54944-3ed0-32f8-8c64-f209b7b7af67 | -11.20704 | -55.10684 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaa3c1ae-d251-3041-b0ba-a2c8f8aa324f | -15.64516 | -50.10814 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99b4fb38-7f2f-3c78-b7bf-784d2b5368ea | -14.97283 | -48.14502 | 2026-09-01 05:18:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62f047cd-a456-3856-b4ce-2ef5a11a3718 | -16.04554 | -54.39166 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ec1e2ee2-e290-3997-86e6-8959bd880b8f | -10.84108 | -54.03413 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75a09d8d-9af1-3e3e-8666-28e85edc3ce8 | -14.66502 | -53.55007 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fdfc5ac-fff9-3a3c-91fe-9d83fcf215c5 | -15.20706 | -46.21707 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4aab7a5-8619-3468-814c-5c15b22913b7 | -11.29805 | -50.57248 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 08679fd6-7245-33e2-a425-20445ccd3527 | -14.43083 | -52.50735 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57f1521e-d5a8-350e-a66b-b665f5dec989 | -15.23894 | -53.84705 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f85599ae-ad4f-38a5-8a6d-7009e82dccd7 | -14.00926 | -54.08552 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bcf34ef-6bb0-30d7-84ad-58584150fb04 | -10.75148 | -54.05878 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ff59d54-7081-3d72-a7a9-cb2154211cbd | -14.26636 | -52.86162 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9709e847-78fa-3a91-bad9-0865c893ea85 | -9.00633 | -67.79809 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c924ee7-0286-341a-87b9-70b876954cc6 | -13.27893 | -48.5517 | 2026-09-01 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70de6026-81d4-3b62-b76b-4a185634d0bd | -10.13149 | -68.58318 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e45da6f-ddfe-3a22-826f-ef5060078ce1 | -15.62585 | -56.42232 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53129cc9-aacc-3fa6-bb25-7584f6bc9ff4 | -9.03235 | -65.39938 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c80ec0a3-a255-34c1-9d3c-81c24386e08d | -10.75939 | -54.00571 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ac5841-8215-3003-8fab-38f1fdd7b279 | -15.66797 | -45.95481 | 2026-09-01 05:18:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70d8dfb5-f2e1-3cdc-a1ac-e40f2cda1425 | -14.39069 | -52.52793 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6f10a57-d5be-3c8e-b792-c9c74bb425f9 | -11.29051 | -50.57248 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 83ef4e90-812a-3e07-9346-db534d04ed3a | -14.73366 | -53.59032 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa25217a-0509-35cc-8c8f-e1c4cfc88c0a | -16.04116 | -54.39571 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d0cab7d-b6cb-3e1f-b479-769b6c794b79 | -15.24491 | -53.88655 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c65242-4512-379e-a7f9-6c2efd90d9cb | -10.4139 | -64.45641 | 2026-09-01 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d7bfb60d-3fba-351e-97de-0f55329116bd | -11.29936 | -50.57373 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 1de89096-8643-3d85-921e-b46b50238d5e | -11.7913 | -47.67376 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7313f5c-7981-324d-b259-b6da4fdd690f | -15.64305 | -50.10571 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51081d0f-5fdc-3607-a062-95cf938ef026 | -13.47627 | -57.03335 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c983aeb4-e70f-363f-aec0-a11cac711fa2 | -9.06459 | -65.48886 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d7044ef-6fb7-3ecd-828b-5f3f79fd3424 | -16.37078 | -54.5197 | 2026-09-01 05:18:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0f0f6fc-9787-3443-a3dc-ce609001ecc9 | -15.76996 | -56.09013 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| e2e6d5cf-662f-31b4-8544-ae2e12136a83 | -13.38246 | -51.76096 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e7bb35e-8e28-3b07-8985-96e4c4b464ee | -15.39292 | -53.75639 | 2026-09-01 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bd8daa8-9250-302b-9cb0-4b304e63f977 | -10.49364 | -59.60456 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b757d1b5-2544-32ce-8c31-a413a9d79fcc | -13.44827 | -51.87736 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db31b55-e6ae-3055-b348-236d1a25ac4c | -16.04316 | -54.38183 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 35b10ea8-d302-3486-81b5-801bf3943679 | -10.50005 | -59.60987 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c12eeba-dc4e-3e00-baed-453840536f7c | -14.25557 | -52.88115 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d9f98ff-63b8-32b8-b3bf-c362cbf3e5b2 | -15.60829 | -56.40022 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b3c7ce1-2e72-3958-ab36-6d19429d1712 | -14.4012 | -52.48064 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a0596fa-d9ae-3a31-a955-a792164ee3e8 | -10.7433 | -54.01574 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d92b5da-0a54-38f3-a9bf-cc0a5c5dedce | -11.30822 | -50.57497 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cb99882b-9a51-3c33-8b44-153a509ecf92 | -14.27502 | -52.85767 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7306f61-80f0-380f-8aec-cdbc263df4bf | -14.45118 | -52.51043 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a22bc571-e789-30a9-a015-1235388165c7 | -15.65004 | -50.1087 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4efb7cd3-db3c-3318-9b9d-1c3e15232792 | -16.54581 | -49.56784 | 2026-09-01 05:18:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37308e5a-5cba-32b3-b1a7-6aae1ea698ac | -11.19893 | -55.04391 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9258275e-9988-3607-a6a8-7a74c30e1ee2 | -11.90574 | -45.07447 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c601959b-2196-3179-b79f-7f7068edb67f | -10.73966 | -54.04022 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25537ad5-91c4-383a-94ba-b7af70c7ca40 | -12.78792 | -46.46415 | 2026-09-01 05:18:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a861122a-7c22-39ec-ab52-964ebd701fc2 | -8.5071 | -67.13217 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36d82369-66ce-3533-bbb3-1c8408daccfe | -15.85288 | -47.69197 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 473131fc-46f5-3f37-8738-162cf9a4c57a | -14.57861 | -54.07894 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55740dc9-af00-3fa5-8c0c-268053f5ad5f | -11.48429 | -58.51965 | 2026-09-01 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d2673d8-9245-3b55-bba3-eb9e0c5882b4 | -12.78499 | -46.4605 | 2026-09-01 05:18:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cb86dd5-5026-36ba-9b70-b57970d7d270 | -9.79758 | -59.43829 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d44ba5e-b419-3d71-9644-882d831cf0cb | -14.39427 | -52.5322 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 507e1a4c-5fd5-3d43-bae1-11b9ef010be8 | -9.05993 | -65.48463 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83a19edb-bf5e-3dd7-b517-004440af43b6 | -8.51299 | -67.1333 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1e92fb7-9a34-335b-ae68-94d828c89e08 | -11.29747 | -50.57687 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 012c3e0a-2215-3e6a-b60c-9a698610b514 | -15.25183 | -53.88963 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a2db01-406f-355d-af31-48a9742df288 | -12.95067 | -45.96384 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3b8ffe6f-303f-3bcf-8228-a8548bef42a4 | -11.2583 | -50.57682 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ccd726ea-4223-3f92-97c5-9434ef4b92be | -11.68359 | -47.1552 | 2026-09-01 05:18:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fbc6471-b954-3b28-9005-936fc28ce0ff | -11.29842 | -50.6037 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 499ff210-2b8c-3752-a6ee-890d48df3a2c | -11.3019 | -50.5775 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7de629d5-7eb7-3d1f-97b5-a1d33cd9ba9f | -15.63214 | -56.38097 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae15cb0c-e01a-3295-9247-2efbbe744aa1 | -11.66038 | -47.61022 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 64ce15ae-adac-3ca9-a0aa-33721ecc9472 | -11.06699 | -51.52803 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2e6958e-c19c-30d6-ba1e-9e321ab2504d | -15.25414 | -53.84916 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ea3c0f-1afd-34be-a5b3-bb1dec42a1f4 | -15.88438 | -56.48553 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1b80470-f44f-354a-bf49-cf9ef59d9932 | -11.19904 | -55.11328 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a80a5ce-de3c-3290-9f7e-7ea76aa598d1 | -11.29875 | -50.5781 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 825ef6e7-db9e-3b56-ae70-a72654bd260d | -16.4485 | -51.40631 | 2026-09-01 05:18:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ca3bcc7-1beb-3f25-b362-ed09f2edc1e8 | -14.7211 | -53.56859 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d802f38-b664-31df-a417-c2ebc981c79c | -15.61795 | -56.38253 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1afd997-8271-308f-8755-678a98216b31 | -14.41092 | -52.50106 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f645efd3-4815-367b-a045-f927caa3b596 | -8.99976 | -65.42843 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8981c0ed-6771-368f-8c2e-b86ad373523b | -13.27373 | -48.55071 | 2026-09-01 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60bb1931-938f-379a-8c62-fa73ce98eb91 | -16.59706 | -50.24612 | 2026-09-01 05:18:00 | NPP-375D | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b817808e-2b65-37c2-b6a0-3abcefbda487 | -11.30318 | -50.57872 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 23321017-3042-3aff-8c4c-b01519ea6da3 | -15.24805 | -53.88906 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3b81a1e-f704-3a36-9c4d-276bdab6332f | -15.01004 | -52.76983 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9bf6fd1-0668-3860-bed6-8d7ae1b7a885 | -8.58581 | -66.97204 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6c3232e-2ced-3ac1-8690-0f93fbab2ef8 | -15.84676 | -47.69495 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e400406-ff9b-31fa-b29a-a095cd603574 | -14.45988 | -52.50766 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aac1bf81-c7e5-32dc-bf89-22a693f01652 | -11.06816 | -60.69788 | 2026-09-01 05:18:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d3e6f0b-b775-3e40-9b83-2a3bfc0b376e | -11.52252 | -46.92954 | 2026-09-01 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3efaaa-1cd5-3b4a-ab4d-ce8aedd17235 | -14.58967 | -54.11965 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f3bc7c1-40b6-3197-8a5e-e4624bfcad61 | -15.40341 | -52.7295 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 189bdbf2-5587-3eb0-a63d-faa352dc2aa1 | -14.26239 | -52.861 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74fb2268-70ba-3499-8f32-2cc7a696850c | -14.7305 | -53.5851 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beadedaf-0474-3f50-b719-38b3ff53951a | -16.18237 | -49.32482 | 2026-09-01 05:18:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ba1eea7-cede-3285-bd25-9244c66e7089 | -11.79175 | -47.67029 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fee80e73-50e4-3085-aeab-69d558163318 | -15.83089 | -47.68082 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a146c83-3e1c-3315-b51b-70a988c65541 | -10.4809 | -59.61501 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d991a7c-6995-3b08-8f04-77dd1aaa91bb | -11.66715 | -47.60061 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README67.md)
