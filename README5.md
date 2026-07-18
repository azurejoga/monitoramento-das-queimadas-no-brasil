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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3168da3-315b-347f-b188-039013ae2737 | -11.47427 | -47.34506 | 2026-07-18 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4116f053-e324-3032-adc5-776658c3be8f | -13.55497 | -47.7804 | 2026-07-18 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 933e2a3f-5bf5-383b-a7cf-413d652a4edf | -9.53301 | -47.11856 | 2026-07-18 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d5b891f-2544-32d1-ae64-795811d2d54e | -11.47354 | -47.34882 | 2026-07-18 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ac59d88-ff6b-3d5f-aac3-445cb39c1a2c | -12.95053 | -44.73288 | 2026-07-18 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c87febdf-4b84-3b71-af3c-aaa613c2acd9 | -8.94708 | -47.61081 | 2026-07-18 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a2de6a0-3c78-351c-903a-9bfff75fc579 | -13.31189 | -45.15688 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eafa7a48-6621-321d-865c-6886ca14b56c | -13.31907 | -45.14641 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0b2e0b7a-74f2-33b8-841d-d70e82959d99 | -7.29279 | -46.25537 | 2026-07-18 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2751abd-f31a-398b-af22-ba9abaa93042 | -7.91276 | -48.26357 | 2026-07-18 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fec66677-fc4f-315d-a6c8-a783b8609417 | -11.79825 | -45.94191 | 2026-07-18 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca90f2a2-c53a-3464-a0b9-f57086500e0a | -13.55832 | -47.79381 | 2026-07-18 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47b42caa-05e0-3b62-8e47-5164e87f43bc | -12.45586 | -49.58927 | 2026-07-18 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e852a1da-4701-3138-b95c-4268220e944c | -13.313 | -45.15111 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| eaac6d4d-55ac-3039-8a1d-e1ae162687aa | -11.79287 | -45.94083 | 2026-07-18 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebb1244b-4ef7-3284-b90f-94ca59006793 | -11.79355 | -45.93731 | 2026-07-18 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0341186-5b91-339e-9157-6e994caa98b3 | -12.45462 | -49.59521 | 2026-07-18 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ab367e5f-a253-34d1-852b-597ccc370282 | -7.47757 | -46.66691 | 2026-07-18 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74f929aa-828c-31a1-9d42-34657d0cc712 | -22.47351 | -43.08562 | 2026-07-18 03:47:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4b30c76e-2c03-3af5-98c7-1ae41ccd42cb | -22.77242 | -43.72926 | 2026-07-18 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a9cb7e2c-8cc6-38a3-9db6-e5cfb370e4d2 | -22.47259 | -43.09069 | 2026-07-18 03:47:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9284cc7e-a14b-3082-b435-a9995deddd4e | -20.35257 | -48.31744 | 2026-07-18 03:47:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 531340dd-c724-3610-bbab-a374d4765587 | -19.93335 | -44.07165 | 2026-07-18 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8e4cebee-3182-39ec-98b9-0754a30fbd4a | -21.14939 | -40.89899 | 2026-07-18 03:47:00 | NOAA-21 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1021b8d2-7395-30e8-ad94-a53f606337d4 | -20.07203 | -43.70884 | 2026-07-18 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b5b6a91-6c4c-3d5a-a4df-d0810a7e3f89 | -22.46876 | -43.09047 | 2026-07-18 03:47:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2e3af698-c9cc-31a4-9aed-bd0c5226bc24 | -22.46682 | -43.10109 | 2026-07-18 03:47:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0321843c-9ed3-3cfe-9fef-7526fdab9f9d | -19.93154 | -44.07167 | 2026-07-18 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 86a5177c-dce4-373d-9610-67002bb568a8 | -21.27379 | -49.1559 | 2026-07-18 03:47:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 17733d50-4827-3db1-8d1d-c677fd7d4ca7 | -19.7845 | -48.26505 | 2026-07-18 03:47:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c1b8ed2-ca52-3fdd-922e-bb0b607ad0b2 | -21.85542 | -48.76397 | 2026-07-18 03:47:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cd6eedb-2571-3de4-a40c-8ec946a85697 | -21.85621 | -48.76038 | 2026-07-18 03:47:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ed7322a-63b9-33a8-bb69-fccfef63c483 | -19.71834 | -50.21044 | 2026-07-18 03:47:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 8fda06a4-146e-34c8-b65f-31f569bda222 | -22.81929 | -43.56275 | 2026-07-18 03:47:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e0ebf146-8e86-377b-a539-bf1dfd450da0 | -22.46969 | -43.08537 | 2026-07-18 03:47:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| fd663504-9e7b-3037-a7dd-859b49e17857 | -22.81545 | -43.56211 | 2026-07-18 03:47:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6dcf2594-b50f-33cc-8475-49a63fb5ac7a | -15.24376 | -48.57843 | 2026-07-18 03:47:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 296c0b6a-fa07-38ab-a62e-77334d11970b | -20.07335 | -44.62608 | 2026-07-18 03:47:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cbb86a1-78c6-39fe-a9a4-0440ef3fc1e3 | -15.24469 | -48.57409 | 2026-07-18 03:47:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cce17cb-11a1-3304-a47f-de5a7f3cdc86 | -21.85701 | -48.75675 | 2026-07-18 03:47:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a377477-e6a9-3e52-8bd7-e10a1cbaea2e | -20.07278 | -43.70475 | 2026-07-18 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bcbccd9a-8ae2-3990-b203-a71c27383714 | -20.3246 | -41.51137 | 2026-07-18 03:47:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6d01c699-d4cd-33ff-bb62-ff8f2c28e719 | -19.35473 | -44.71025 | 2026-07-18 03:47:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0df0c12e-1249-3b49-b30b-b65d2d96be62 | -22.72043 | -43.59255 | 2026-07-18 03:47:00 | NOAA-21 | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 45526d42-f71d-37b9-916b-24d7fd3c30d7 | -19.78526 | -48.26151 | 2026-07-18 03:47:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd4580b9-daf2-38e2-b7cc-c31d8afe5cab | -20.35788 | -48.31867 | 2026-07-18 03:47:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c30ad450-7251-3a70-9729-37395531cf02 | -19.8913 | -44.02274 | 2026-07-18 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 29b0fa15-46be-3241-8c21-a695e445e0d0 | -20.07362 | -43.70028 | 2026-07-18 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04894cd3-b9e8-39eb-a476-eaa58bd1767f | -17.32159 | -42.38675 | 2026-07-18 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a3712c-44ba-3ad4-8991-6172f7cb0fae | -20.91061 | -43.94373 | 2026-07-18 03:47:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| caeb8502-f900-3772-a89c-2aeaa25a4882 | -17.91711 | -45.28013 | 2026-07-18 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bc66e99-6c6d-3beb-9cec-ea64d5da5987 | -20.32816 | -41.51205 | 2026-07-18 03:47:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 725e2d8c-1dc2-3708-bb23-f9bfb32aeee7 | -22.80109 | -43.4484 | 2026-07-18 03:47:00 | NOAA-21 | MESQUITA | RIO DE JANEIRO | Brasil | 3302858 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e390a2a0-6c10-3cf4-9db0-13b22ae15d43 | -22.52159 | -43.54972 | 2026-07-18 03:47:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b58aed94-edb6-3b5d-ba93-0786c3f67669 | -17.16237 | -39.3028 | 2026-07-18 03:47:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 179902d2-5820-3275-9f47-ad62df05ffbb | -20.91462 | -43.94453 | 2026-07-18 03:47:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 90b1d8de-8f30-3404-b4fc-2f26c9dff486 | -18.41472 | -43.72079 | 2026-07-18 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed73ecac-202d-3d6e-9c1a-c89b37f0de98 | -22.57271 | -47.31117 | 2026-07-18 03:49:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e7c2f79-9262-3679-b47d-ef87d7a98786 | -22.25353 | -52.86769 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c2435753-cc78-3883-902b-6eb256ceea60 | -22.25514 | -52.87691 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| da9e4729-9e20-350d-ac0f-cb022dee68c3 | -22.25045 | -52.87981 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6a85f112-64b7-35b9-a990-6caa31074f5b | -30.208 | -53.99603 | 2026-07-18 03:49:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| c09457c5-806e-379c-94b6-40a8bf587090 | -23.16093 | -46.57484 | 2026-07-18 03:49:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f22059b-f772-3831-ac8b-4fb3321e0661 | -28.09415 | -50.60066 | 2026-07-18 03:49:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 794cde4b-82d9-3cf8-85a9-d62175748f22 | -28.09484 | -50.59729 | 2026-07-18 03:49:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0e240315-8c84-32ef-a21b-999aac0e934e | -23.16416 | -46.57842 | 2026-07-18 03:49:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7607c3c-6d5c-3b8a-b376-69824860e0b9 | -28.88795 | -50.73959 | 2026-07-18 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a446f89-717c-3657-bff8-e166dba0bc89 | -29.27861 | -50.34761 | 2026-07-18 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de5b6ce9-3701-3f2d-ac04-bce11f11b0a1 | -22.79892 | -49.33911 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4ab14d2-5539-3053-ad07-8d30946e8bfb | -22.57261 | -47.30814 | 2026-07-18 03:49:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fce027b5-7e07-3c9f-bf0e-2afb87975c6c | -22.57386 | -47.30558 | 2026-07-18 03:49:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0844ead0-d7e8-31b7-ba06-ac7d294436c3 | -28.75433 | -50.00431 | 2026-07-18 03:49:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1ff2c147-1784-35b1-a3cf-da975852f753 | -30.1217 | -52.0824 | 2026-07-18 03:49:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 84aff676-bddf-39b0-89c8-51ae1a7e3c95 | -22.24696 | -52.86575 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d33e5025-e95b-3f71-908e-44d8777ffe6c | -22.25009 | -52.8688 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1d5aebbb-d39d-30b5-9b38-21c757078e56 | -22.24859 | -52.87485 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 49c8be08-35c0-30d3-b27d-aa6abb9eb9dd | -28.09499 | -50.59703 | 2026-07-18 03:49:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bfa4096e-bceb-3542-9c9a-ad2bfe609a79 | -22.79193 | -49.34491 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1b56c79-af03-3b38-9bad-9e574521dcc3 | -28.99555 | -50.58971 | 2026-07-18 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2eae324c-88be-3790-992c-6a6c99b4104d | -22.79727 | -49.3464 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f02efd6-201c-3e70-8aa3-927e83d9b9a3 | -28.09398 | -50.60089 | 2026-07-18 03:49:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 263ba90d-b05a-336b-9e88-b54c078f8275 | -22.25856 | -52.87569 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 627a0aaa-46bf-3ed3-8dbb-85a6337f3a09 | -28.08991 | -50.59517 | 2026-07-18 03:49:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4fcf887c-65dd-3d22-b1dc-f1ab8391580b | -28.08977 | -50.59544 | 2026-07-18 03:49:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d94cfb96-0af5-3938-aedc-44d9c979aba1 | -22.92243 | -49.20247 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1251e139-6492-3601-b06c-5e6311c55f4f | -29.27364 | -50.34622 | 2026-07-18 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 393fb826-2950-330c-a41a-01768b460585 | -28.8551 | -52.58944 | 2026-07-18 03:49:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ba3f033-7ba2-345b-ad97-1ffae62aa552 | -22.79811 | -49.34271 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 967865b8-5820-394d-975f-361373354691 | -22.92159 | -49.20619 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10a4293-acbe-3ca0-aa39-56d80a2e237f | -29.07409 | -50.72438 | 2026-07-18 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e35f671-dd46-3bf8-be09-d6d502353453 | -28.7536 | -50.00748 | 2026-07-18 03:49:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2cbdf1c5-583b-36f3-b045-f9f3d051a343 | -23.82932 | -47.51105 | 2026-07-18 03:49:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8850db7a-82c2-3fc0-8526-0f6695dcab61 | -28.86078 | -52.5911 | 2026-07-18 03:49:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81269a40-15d9-35c9-91d4-d87bf9da3c61 | -22.92449 | -49.20676 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d0dea89-406a-389e-9953-deca0ea2e3da | -22.92531 | -49.20305 | 2026-07-18 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1989471-df73-31dc-81fa-fddae5a221b5 | -29.07323 | -50.72798 | 2026-07-18 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1db77597-4840-396f-9092-6dbae2a11dae | -22.25201 | -52.87368 | 2026-07-18 03:49:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 1a02a0a4-640a-30c9-8124-7c6ff5774dd1 | -30.1207 | -52.08648 | 2026-07-18 03:49:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 267f1806-f46f-3e57-9df4-44ca0872a9c3 | -13.3217 | -45.1479 | 2026-07-18 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e6f23ee6-eca9-3ea5-bee4-954cc1377efc | -20.0252 | -57.9468 | 2026-07-18 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |


[Clique aqui para ver as próximas entradas](README6.md)
