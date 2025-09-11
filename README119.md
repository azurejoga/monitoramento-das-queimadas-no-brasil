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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc0266e5-d65d-3e8c-b838-337f5571f8d2 | -17.32481 | -46.67805 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd75fa46-8f05-3b4f-a570-b6aa74139b4a | -17.38886 | -44.92735 | 2025-09-11 04:49:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39bb5e7d-20df-384c-aa73-9614b724206b | -16.58718 | -50.09045 | 2025-09-11 04:49:00 | NOAA-20 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3db60600-5afc-3263-bb25-9e89f463b858 | -18.6226 | -44.2641 | 2025-09-11 04:49:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3872ca64-005b-3767-b8ed-472214ac638b | -20.84839 | -54.99313 | 2025-09-11 04:49:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6f490f8-9c98-3286-87e8-2fd27bfe0d5b | -20.02033 | -47.76925 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9bd9c46-07e7-304a-85b0-f879fe13ff85 | -21.72656 | -50.10217 | 2025-09-11 04:49:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| f5357bcb-7826-3a4d-a48c-86a0a7bfbee0 | -18.54253 | -46.69022 | 2025-09-11 04:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 002e2da9-853a-3386-8966-d7e294301d66 | -17.9398 | -44.48302 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c14d624-a1c1-3605-adff-5a0c803aebf3 | -19.96707 | -46.87822 | 2025-09-11 04:49:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0244ad59-765c-31f8-ac0e-d6ab16332923 | -20.16634 | -44.62316 | 2025-09-11 04:49:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e5933b0-0229-3dab-b1f3-ac9bbcef3a07 | -22.84142 | -47.4636 | 2025-09-11 04:49:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 563f5645-f846-32c5-b201-0b58a646ba71 | -17.3282 | -46.68796 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ebde443-fb05-3c94-b28c-3a78efc38ebb | -17.50998 | -43.74858 | 2025-09-11 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d974db-32d8-3f2f-b8c0-b5580088350d | -18.45088 | -49.57793 | 2025-09-11 04:49:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01518b32-edae-3374-a724-a4ab666f3e0a | -18.00729 | -44.45193 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb30336-b5aa-3bc1-b112-ccd513921211 | -19.254 | -48.00395 | 2025-09-11 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69fdae02-db87-32cd-9f4e-4fe6c4e6d822 | -16.60888 | -49.77373 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0a75ef-ae79-3f7d-bf73-fd8a13bdf2c0 | -18.05905 | -50.72243 | 2025-09-11 04:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8707910-83d5-36a3-9cd1-734c2ffa17ef | -18.5706 | -47.42002 | 2025-09-11 04:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25dccca5-dc24-35cf-a50d-b35f0256dbf4 | -18.60358 | -43.97245 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 420dfb87-a0aa-3353-a901-012cecb9f2c2 | -18.29009 | -47.67136 | 2025-09-11 04:49:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 20e0a865-d0fc-3a1b-98b6-eea2788d2456 | -21.4333 | -48.91703 | 2025-09-11 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 46ada41b-d77a-30a8-92cb-cfe140156951 | -17.99683 | -47.10909 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f03844bd-982b-3e69-92d6-f81bd88bbeb5 | -17.33183 | -46.68151 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4172d0ca-5e49-373d-8786-7ac199d69750 | -17.55385 | -44.55542 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 150ae758-5b00-36f1-b8bc-4c674f5f5fe2 | -17.37313 | -52.93665 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6743490b-61df-3d99-a6ae-00ce92bcb166 | -19.99635 | -47.6338 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa8415f1-cc0b-3256-b582-a7b85cb092d3 | -17.8283 | -46.74009 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9518597d-d87a-33e5-add5-22c20dac588e | -16.53304 | -55.17884 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ae353747-aa80-31a9-b88b-63275b726918 | -20.70053 | -46.078 | 2025-09-11 04:49:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c159075b-82d1-3011-abd2-8c8a6aafc2ad | -21.72865 | -50.09962 | 2025-09-11 04:49:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 07ac6460-2266-3f00-8726-602e68239167 | -20.54183 | -47.62497 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17ef18e2-c1a3-3337-9bfa-2a8fc9abe99c | -18.01223 | -44.45553 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d80e341c-897f-3ba3-912b-d99580f45f65 | -19.99178 | -47.63511 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9350b584-b6a4-3cfb-9131-85f6997d5598 | -17.20421 | -50.15545 | 2025-09-11 04:49:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f63792d-157f-385a-be9c-e23576adcc45 | -18.60989 | -43.96501 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af464cd5-e2b0-3f5e-a11f-ee1ce8fa5f46 | -18.19536 | -43.87166 | 2025-09-11 04:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddf14c79-2516-3117-bf03-4572e5f3f198 | -18.00882 | -47.99336 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51475bfb-af3e-34fc-9b62-89a9f07974c3 | -17.47076 | -45.09882 | 2025-09-11 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3481bc2-0a59-38c3-8ead-df3c9a87b59e | -19.66095 | -45.85755 | 2025-09-11 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cb0e0c33-39d4-3be4-b9fa-9dd5b0dcc412 | -17.84595 | -44.21715 | 2025-09-11 04:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a653ca80-2fb8-3cad-9455-4c66bc47f06d | -16.54746 | -55.13452 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3b9614f8-26cd-3119-be20-37d30823c67a | -17.06932 | -49.67595 | 2025-09-11 04:49:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87cd8b49-f295-3b62-9a47-dc5a2768bcc2 | -17.83224 | -46.74532 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 275ce7c4-a9b8-3d5c-8f84-ed54b1e12d0b | -20.48008 | -49.73193 | 2025-09-11 04:49:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff8674f8-7118-32ec-8950-e19e6be6e5be | -20.24055 | -43.5848 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 4a218428-a13c-334e-adb5-df5dbbdfca06 | -18.01259 | -44.4524 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9d8e183-568d-3b15-9a43-87f4c834b383 | -20.1581 | -41.03493 | 2025-09-11 04:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fd58d119-27cc-3f0f-8b66-84026710c954 | -16.18331 | -53.85355 | 2025-09-11 04:49:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| effb18fe-ea70-3eae-bbf8-a5dfd4994317 | -20.23664 | -42.74891 | 2025-09-11 04:49:00 | NOAA-20 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24067407-0c8e-38fc-ad67-03921c806df1 | -17.57838 | -47.49348 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16a8e95e-3676-3b13-85b9-69e25a16c6fa | -16.63346 | -49.75919 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72e6dc47-46ff-39f8-b999-c85f6ea2d818 | -19.23178 | -48.00932 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 2327f617-731b-3d7c-9580-b9d16f8ab425 | -16.6155 | -49.41154 | 2025-09-11 04:49:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33bfbf85-1cc8-3a5f-bdb2-b42ca06198b2 | -17.55454 | -44.54931 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93689c2c-632c-319f-ad57-770b420945df | -17.06992 | -49.67157 | 2025-09-11 04:49:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f05d3e2-5854-398e-a79c-5e9122b974f6 | -17.7109 | -44.43646 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa4b7530-efcc-387f-ae51-412a2025657f | -17.37925 | -52.91908 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e77b107-b124-3293-82eb-0f8c754daef6 | -17.3074 | -49.31727 | 2025-09-11 04:49:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53314ecb-6dae-3b74-bf60-cb9576d6aa40 | -19.22838 | -47.9667 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a727b74a-8eec-35dc-a87a-27d86667dceb | -19.25348 | -48.00806 | 2025-09-11 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c7306ab-5430-3426-9806-f3a9061c3d73 | -16.49109 | -51.9781 | 2025-09-11 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 269e7165-8309-3f70-994e-2c45ad3f07f0 | -20.03942 | -42.73438 | 2025-09-11 04:49:00 | NOAA-20 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 56eab378-daea-3a85-b53f-315d90450c5b | -18.00413 | -47.99675 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 711144da-76f0-3c89-abe1-3bfe774036a2 | -20.11199 | -44.94342 | 2025-09-11 04:49:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8222db5d-04fa-36bf-bae9-276975baf24b | -20.54234 | -47.62054 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a34e6b7-7c29-3184-a5ca-8468fdec39c1 | -17.5594 | -44.55307 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 991325dc-0401-34e8-b418-962a520071ec | -16.7132 | -49.37578 | 2025-09-11 04:49:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65ee74a5-c533-3bf5-bc07-8bd65b10a049 | -17.72749 | -44.431 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 746ce8c3-1a60-32c6-872d-d5df4a50c738 | -16.51543 | -55.15747 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8c8860cd-2b79-35df-b8e1-d1aa5c73fbf2 | -20.70261 | -46.07998 | 2025-09-11 04:49:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7f8769f-91e6-3742-a151-a228ceacf9d7 | -19.98877 | -47.62301 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aefef654-19ee-3566-b243-b9279072737a | -18.83629 | -50.11649 | 2025-09-11 04:49:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04db079c-fcd9-3999-a221-47b352f45163 | -20.49038 | -54.91428 | 2025-09-11 04:49:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d5d7a5e-bc41-36ff-9b27-73ff1dced434 | -16.55809 | -49.74018 | 2025-09-11 04:49:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfb528e7-7668-3d24-afab-68d5f613fb57 | -17.31538 | -46.75704 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b677d8-59ed-39c5-8610-76919b81a75e | -22.31776 | -50.8687 | 2025-09-11 04:49:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e60802c2-825f-3194-88b8-defed5ed2e69 | -17.96076 | -44.48631 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 895e7341-5731-3b40-af1f-c73422773c97 | -19.79812 | -47.16621 | 2025-09-11 04:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22f44a3e-13f1-32c8-8323-6fda0924df65 | -17.93603 | -50.54273 | 2025-09-11 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc32a4e8-13f9-33d8-b496-8737d9cc9542 | -19.95724 | -46.8822 | 2025-09-11 04:49:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bf0cf3d-d3b9-3216-9780-ce5e372a7091 | -20.07048 | -45.29274 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9b7c73c-9a93-31b9-844d-0dbcae870b3e | -17.2614 | -46.08558 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be3baf0f-efc5-3785-adcc-a9e015ece5b0 | -17.73549 | -44.45522 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0be0380-070f-3f8f-a342-b38de0c0ac74 | -20.00989 | -47.63274 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4afbab25-06aa-3e6c-96a5-c766222d509e | -17.82774 | -46.7446 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3358095e-6bf3-3abe-a23d-5bb0da5ec140 | -17.93917 | -44.48878 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eba6db1-16f3-346b-9e0d-b75a3c522fbf | -16.55042 | -55.15871 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4ce4f801-b0c6-3b86-9db8-8f7825f12b29 | -17.47509 | -45.1054 | 2025-09-11 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f273c2f-9ff9-3be7-a495-9ce1b49fbf87 | -20.70115 | -46.07248 | 2025-09-11 04:49:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dd56ccd1-15d3-3753-a7e6-b8c71311a35c | -21.29819 | -45.95336 | 2025-09-11 04:49:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b200a2ea-f2fd-3b3f-a6b7-5cb34b529eb5 | -22.84029 | -47.47388 | 2025-09-11 04:49:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 19d0aad0-8a4b-3ce4-8d51-e0754dd6b64e | -16.62548 | -49.76249 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45dedc92-3784-37ac-8d34-a7f5f657d208 | -20.00074 | -47.63439 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4317032-abfc-3bc4-a115-6447ed9e1116 | -18.28956 | -47.67565 | 2025-09-11 04:49:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3287d91a-21db-3b8f-9eac-b274a935edb6 | -16.71254 | -49.3805 | 2025-09-11 04:49:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab247441-6409-3c53-a859-797c091c622b | -16.5498 | -55.16245 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 83d9169b-0538-33f3-9375-9d51eeb7e1b7 | -18.29383 | -47.6763 | 2025-09-11 04:49:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2836e3-c76b-3aa6-9d2f-3afd029bb212 | -17.31791 | -46.75508 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README120.md)
