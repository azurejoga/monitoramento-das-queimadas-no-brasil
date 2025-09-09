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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99d09a67-5e25-3978-bfa3-be414078b488 | -13.0465 | -48.02964 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20975ff1-fc61-3ee8-9d70-f0643b4569db | -15.53149 | -48.39645 | 2025-09-09 05:53:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 0b9a5f8f-dbcf-392e-a6ab-0c531ea9a220 | -13.79429 | -46.26836 | 2025-09-09 05:53:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3fb2453d-0935-3f82-a3ec-1e0b75a62343 | -15.77388 | -53.53518 | 2025-09-09 05:53:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 249093f5-6773-35ae-bd15-d76b70512cab | -13.94674 | -48.24602 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c1287e91-6c2a-347b-b044-e1d57e7f501e | -15.52253 | -48.39507 | 2025-09-09 05:53:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4323b5c5-eecf-39d6-9d2a-9c9908985321 | -13.95719 | -48.23825 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bfc1d6c4-abe2-3525-82c5-7ab200dd4f87 | -11.20193 | -55.00315 | 2025-09-09 05:53:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 5ebd14b7-d4af-33cc-bf79-e6ba98eddb6a | -14.35757 | -47.31844 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e61b71b4-ca78-3ab3-a3f4-c4f714df4a3f | -14.41213 | -48.46031 | 2025-09-09 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8cb46c50-2ee3-3c3d-9dee-bf3843d5f6cf | -13.93026 | -48.23322 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4c717fd8-5084-31ba-9480-82086d550453 | -13.9482 | -48.23668 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8c6312e0-41d1-3b9b-b225-f18a0f2ec74d | -11.98543 | -51.01344 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d65b5836-9915-3b3d-a1bd-0bcc95c4db38 | -11.93325 | -50.96947 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c86eac4b-758c-3732-ba98-960ea6b064de | -17.73252 | -44.49717 | 2025-09-09 05:53:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 19f2c0f4-a396-304e-806c-e7c79e108505 | -16.27977 | -45.67698 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f9d3dfb4-12d9-30c7-b699-58bf0338e837 | -13.80044 | -46.2877 | 2025-09-09 05:53:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f0531768-06e0-3a5e-a70a-ebbd0c8d3020 | -17.34194 | -43.58303 | 2025-09-09 05:53:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 92f004b4-1e6d-3282-8ec1-6e2225bff247 | -16.28748 | -45.68811 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33ee36a9-b26e-308b-b76c-405bb6910a74 | -11.97467 | -50.99131 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eb0919f5-bb78-3628-ba29-8a337366fd9f | -17.28622 | -46.69949 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a744b29e-74ad-3965-ba06-7cdfc01102a2 | -15.82455 | -48.94791 | 2025-09-09 05:53:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 6fe9eab2-d42f-3eda-930d-d4a8c91ae4e9 | -17.30262 | -46.71162 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9c335f3b-2d58-37ba-97eb-2818855fce49 | -17.15748 | -44.44835 | 2025-09-09 05:53:00 | AQUA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4f79615-12f4-3388-a80d-5ecfe0302075 | -11.97233 | -51.00566 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| b9c0defa-d3f3-3238-bb5d-6db19b42bd7b | -17.28757 | -46.69017 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 56c979c6-be24-3487-b7ab-df31de876f92 | -15.69952 | -49.8964 | 2025-09-09 05:53:00 | AQUA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bbeb0bba-1ef8-326d-855e-88c455fbd560 | -17.27056 | -46.74475 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b4af2e10-3b5e-3463-a1d4-bc12838c7ab5 | -12.82733 | -52.93077 | 2025-09-09 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| fa769fc9-bccf-3585-bce0-39ce9c88d3ea | -12.01971 | -51.07867 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a8a3e93a-7f3d-3f7b-a127-a20e1822c3bd | -14.3474 | -47.32608 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f3c625de-e52d-3c84-b0e0-ac2d3c7095cc | -15.11456 | -48.04795 | 2025-09-09 05:53:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d5f8536-1a6b-33b3-b7de-bf0a1198f7c9 | -16.43438 | -49.29771 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 48e47061-ca70-3c00-96e5-4352efd1da63 | -12.86058 | -47.97659 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c822520a-9219-3f83-b778-f82b89e9707e | -17.25776 | -46.75603 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a7425454-ede2-3625-b47e-d58162b4777c | -15.1759 | -47.95068 | 2025-09-09 05:53:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a8f3aab3-be9d-310a-851a-0810d3be47e7 | -18.03358 | -47.13296 | 2025-09-09 05:53:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| dc0de407-c657-3993-b997-f060c2ba1962 | -12.03072 | -51.08055 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 2ff5f4c0-51c5-3677-a967-a9cf9f3ed7e8 | -12.20981 | -53.87309 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c1548280-cb31-3eb5-90f6-5ae9221ba014 | -11.20675 | -54.99615 | 2025-09-09 05:53:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| ccf6cf31-e528-33cd-aa4a-9ac91a3c71ea | -15.83108 | -52.26196 | 2025-09-09 05:53:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8915e077-0a20-3fd9-a4c9-f6399cb7d4d3 | -12.20231 | -53.86671 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4235b1a3-d8a5-3120-a3b1-6a5de9b65d24 | -16.31723 | -52.92167 | 2025-09-09 05:53:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b7eab472-f1dd-3e97-9876-5318f8cabf88 | -18.82651 | -49.67733 | 2025-09-09 05:53:00 | AQUA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| f908ed7b-2c05-3a2b-9f5c-71d72a6a40d5 | -14.321 | -47.32188 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 26dd5dd6-a61a-3bb7-bdd8-b4627dabca0e | -11.9769 | -50.99724 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| bb51f4f9-f056-3f3d-a6a9-e854bcb5316b | -13.93922 | -48.23499 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c3482b2c-0e6a-3295-8cb7-d13d577903b3 | -18.82492 | -49.68737 | 2025-09-09 05:53:00 | AQUA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 135.7 |
| e0ddb269-c20a-30fb-93b9-31bdc0a6f3fb | -17.29719 | -46.74889 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 771f1c80-2cdf-3a87-be9e-91dbf342f08c | -12.03311 | -51.06607 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 750fbcef-d441-3745-a072-5f8bfdf05def | -21.45409 | -48.83977 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 6ad9673e-7d5f-3a1b-80f1-c9aeab24f874 | -23.12821 | -46.83149 | 2025-09-09 05:55:00 | AQUA_M-M | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 1ed0472d-b59a-35c5-af79-7538e432f816 | -23.22572 | -50.17801 | 2025-09-09 05:55:00 | AQUA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| fa28e6e0-f8d0-3ec9-b2d4-588cf476eb23 | -21.45122 | -48.85862 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 06cbffcb-2846-3b1c-859d-90bb4e38e832 | -22.36222 | -50.87632 | 2025-09-09 05:55:00 | AQUA_M-M | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d8f5fcbd-5df0-3469-954b-7a36ade14238 | -22.7616 | -47.08332 | 2025-09-09 05:55:00 | AQUA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3b562cf-f872-3820-8793-2850c768498c | -21.44527 | -48.83826 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 13e50c1a-9abb-349d-b545-bd4d3f1cc2e5 | -21.42908 | -48.82585 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d4861d90-d1d0-3a41-b91b-18cbf8565306 | -21.45265 | -48.84919 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 131.7 |
| eeee2c97-75c8-37d1-ad8b-47180deafb0b | -21.44384 | -48.84768 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 1b57342e-c359-3259-bc96-f65a153408b8 | -21.43503 | -48.84618 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b495288b-e8a9-37ad-9765-fc65b3a05f59 | -22.32686 | -48.81894 | 2025-09-09 05:55:00 | AQUA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c7306cf4-120f-3dc1-ac1b-cdb916035c56 | -22.76301 | -47.0731 | 2025-09-09 05:55:00 | AQUA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 490c1200-446d-396b-a800-c6437cfb0358 | -22.35231 | -50.89043 | 2025-09-09 05:55:00 | AQUA_M-M | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| df314409-a7e4-3f26-8414-6073943f6032 | -22.32828 | -48.80948 | 2025-09-09 05:55:00 | AQUA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| defce908-ac0b-37d9-b7c3-2ff4903c596f | -21.32483 | -46.69146 | 2025-09-09 05:55:00 | AQUA_M-M | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6b463156-6192-3016-b4fc-e62d55d50488 | -21.43646 | -48.83677 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 30a3eab4-dac4-3224-a6a3-ccb020955a23 | -21.63599 | -47.03186 | 2025-09-09 05:55:00 | AQUA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 8fbe11fc-a7df-379c-a929-4953d62aad3e | -23.43659 | -47.12904 | 2025-09-09 05:55:00 | AQUA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 7f9b3d37-b729-3232-9e56-980a10135bc9 | -21.46147 | -48.85071 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 29.9 |
| dd85db64-a024-387b-b8da-053f8435f738 | -22.3506 | -50.90102 | 2025-09-09 05:55:00 | AQUA_M-M | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 04fde4aa-3eea-3a05-a6a6-35cb08914407 | -21.6374 | -47.0219 | 2025-09-09 05:55:00 | AQUA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6c17f806-74d0-3a75-8d9b-82037e9e6ed6 | -21.64504 | -47.03333 | 2025-09-09 05:55:00 | AQUA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1ad72b9c-de2c-3e3d-9b70-58ea15b55863 | -21.46004 | -48.86014 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9fa2da8a-caa3-3d59-a7ba-9f2db60f2733 | -22.35696 | -50.90802 | 2025-09-09 05:55:00 | AQUA_M-M | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 794badd0-66f9-3918-ac59-9b890130a040 | -21.64647 | -47.02331 | 2025-09-09 05:55:00 | AQUA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9559d4b-cd9a-3b69-ab67-9e54f2361df6 | -22.35871 | -50.89745 | 2025-09-09 05:55:00 | AQUA_M-M | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6c365753-cc71-3579-b65f-a899d47cac7b | -21.43789 | -48.82735 | 2025-09-09 05:55:00 | AQUA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0bc88f39-77c9-3927-a637-f979dd9d2c17 | -22.92117 | -49.16047 | 2025-09-09 05:55:00 | AQUA_M-M | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bbf78fde-6520-37fb-ba02-194937aa632c | -22.3469 | -50.8888 | 2025-09-09 06:00:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 159d5768-83b0-3222-b957-13a3729348ab | -22.3671 | -50.9071 | 2025-09-09 06:00:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 237f82e9-0d50-36f7-8fe1-1c275a61ce1b | -22.3463 | -50.9117 | 2025-09-09 06:00:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 8ca7ce13-935c-3a08-b706-0a0446b26da3 | -21.4548 | -48.8687 | 2025-09-09 06:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 139.8 |
| a31a087f-7694-3cc2-a775-2f1528c47dfd | -21.4348 | -48.8503 | 2025-09-09 06:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f6351764-0215-3a3f-827c-bd8b26221b69 | -21.4762 | -48.8406 | 2025-09-09 06:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 56e2d87c-306c-3380-8a2c-a4e59482ac2d | -21.4755 | -48.8639 | 2025-09-09 06:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 138.2 |
| fdd62b1f-7650-3399-9339-311c2b7f49a3 | -12.1991 | -53.8817 | 2025-09-09 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4260472b-7ec0-3622-b27e-e02490b13a8f | -14.362 | -47.3107 | 2025-09-09 06:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 0b69c35a-a8a7-3f12-9d53-248ce59690ce | -14.3615 | -47.3333 | 2025-09-09 06:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| cfc9ca0d-4c9e-3f0c-a7ba-733b399019bc | -18.8174 | -49.6816 | 2025-09-09 06:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 139.2 |
| c44df656-2375-3da5-9365-706ff7944e83 | -12.1988 | -53.9024 | 2025-09-09 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 91d35f33-e40a-3c17-aa56-e46d6d3ff527 | -18.8375 | -49.6777 | 2025-09-09 06:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.8 |
| b9c4b3ff-c18a-3237-970e-85a4bc7a774f | -22.3678 | -50.8842 | 2025-09-09 06:00:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 126.1 |
| ec4a8851-f5ec-3af2-942b-cfb814f72cbe | -18.8168 | -49.7042 | 2025-09-09 06:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 95aa2605-fef9-3f23-bc3b-9f1a0ffc0712 | -18.8369 | -49.7003 | 2025-09-09 06:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 131.3 |
| eb78eb53-a8d7-3621-ab12-9d49ce0ca182 | -11.9735 | -51.0148 | 2025-09-09 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fe4ef137-82a3-3419-81f4-ad62fb5bae02 | -21.4555 | -48.8455 | 2025-09-09 06:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 253.6 |
| af87fc0f-1bc7-38ad-99ba-b3d5da8bba2b | -21.4755 | -48.8639 | 2025-09-09 06:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b82470f2-f96e-39ee-88fe-9e718db23f77 | -21.4548 | -48.8687 | 2025-09-09 06:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 4ffd53b5-d642-3405-af54-c71980bdb6d1 | -21.4555 | -48.8455 | 2025-09-09 06:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 198.6 |


[Clique aqui para ver as próximas entradas](README71.md)
