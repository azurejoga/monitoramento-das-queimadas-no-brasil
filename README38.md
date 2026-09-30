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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0089656a-0884-3f07-922e-be63f837ef08 | -21.061 | -47.03845 | 2026-09-30 04:36:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63a920e3-64db-3a3c-a7b1-7ddbd5df4e18 | -22.50568 | -47.6027 | 2026-09-30 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5deca75-252c-3edc-af05-ceb2d9792ac4 | -20.54672 | -49.59555 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 841f76d4-ae7a-3e45-882a-7ffe7017b5b1 | -20.54268 | -49.59877 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f893eda-8376-31ca-95a9-4ec2a926c32f | -21.59176 | -49.8078 | 2026-09-30 04:36:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1cc925fc-ddd7-3728-a154-3347437699ba | -22.31754 | -45.13674 | 2026-09-30 04:36:00 | NPP-375D | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 71fa7475-1532-30f7-a722-26a10a11712d | -20.45616 | -46.22027 | 2026-09-30 04:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d933effa-bf7e-3279-b5d8-2c29f2abc894 | -22.53205 | -47.58795 | 2026-09-30 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85dd3bb6-d2fd-3613-8651-0c7060446b57 | -21.09669 | -43.9035 | 2026-09-30 04:36:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c95ffa96-ff88-34e5-95fd-e3ce63e03ae3 | -20.54608 | -49.59941 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 404adc6c-f485-313d-a36f-0ce73e17e466 | -21.09986 | -43.90896 | 2026-09-30 04:36:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 456bd261-76db-382b-8bc2-3372fe642cc9 | -21.04394 | -47.35852 | 2026-09-30 04:36:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3a482f6-b383-38b7-b262-419368381369 | -20.50622 | -49.6278 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 49.0 |
| f8911a45-f1a8-329d-bac9-f13a4be50d0b | -20.99481 | -47.04247 | 2026-09-30 04:36:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b0cc321c-15fa-3f54-a39f-9ebc8308e8dd | -20.8082 | -47.16548 | 2026-09-30 04:36:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f80982fa-460d-3ffd-a64a-f1077f36e199 | -20.82011 | -47.13283 | 2026-09-30 04:36:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58adb0b6-e2cb-35f7-aead-931fa59d36ee | -20.99424 | -47.04623 | 2026-09-30 04:36:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ab0ea28-6788-3c34-a4e6-ba2e895747f5 | -22.50397 | -47.60727 | 2026-09-30 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb84baee-f698-32eb-b4c5-2f1807dd047e | -22.92657 | -44.85364 | 2026-09-30 04:36:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 162b46a0-32fe-3af9-94ca-c19c99552041 | -20.49941 | -49.62647 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61ad623e-ae8c-36bd-a65e-e721b6eec83c | -20.74233 | -46.38228 | 2026-09-30 04:36:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e3f5c78-c593-314d-8e09-bab833adcf0b | -20.50282 | -49.62713 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 65f25112-8d81-3c41-89b0-b488031b741d | -20.01788 | -45.40075 | 2026-09-30 04:36:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30aa612f-36be-30a2-bd52-6ddace246e22 | -19.62676 | -46.91456 | 2026-09-30 04:36:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e4f35e-39e0-3968-b660-a0037d02b29f | -20.54543 | -49.60326 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| decc05f1-c3c8-3834-baa0-e38a4c54ab7a | -20.74783 | -47.03246 | 2026-09-30 04:36:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62b2914e-1043-3555-8898-c658e2e9be9f | -21.09391 | -43.90646 | 2026-09-30 04:36:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8d5f919-79b7-3551-9951-4719eaa0d489 | -22.53263 | -47.58415 | 2026-09-30 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7586a2c0-ea3c-3e3b-b411-469697433ecd | -20.85097 | -44.58558 | 2026-09-30 04:36:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8c5f79ce-11d5-33ae-a024-227d3f962cf7 | -20.07767 | -45.35912 | 2026-09-30 04:36:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cb6bab5-3294-3bfe-9282-a939b5757837 | -20.47996 | -47.36639 | 2026-09-30 04:36:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 948c1c6c-73fa-3c5b-ae23-1e4cc223963e | -20.49601 | -49.62581 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3092379-b8b4-3026-b808-7524154f8351 | -21.09605 | -43.90843 | 2026-09-30 04:36:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 89541b4f-5a79-3207-8ef9-2eb53cb18f6e | -20.39881 | -47.12752 | 2026-09-30 04:36:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 702f3ccf-5a95-3fc2-a864-d5226c38ea60 | -22.50456 | -47.60349 | 2026-09-30 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33fa6d50-1bb0-3b00-a01b-6be9dd95e625 | -20.54332 | -49.59491 | 2026-09-30 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0650127-e403-328e-ac47-76af04d652e9 | -21.09771 | -43.90702 | 2026-09-30 04:36:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 68a93270-3a3b-390d-97da-64af6b69673e | -18.50273 | -45.14465 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2aefae97-42f5-3d6f-ad74-eb59acf394f5 | -17.77567 | -43.0076 | 2026-09-30 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac673ba3-fbe9-3b93-a518-37d5ecfbee5f | -18.89394 | -43.80144 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 0022cd39-e8f7-3884-bb0d-7d71c39ba1fa | -18.24856 | -53.03592 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f1ef60c-e1a3-3f85-a9cb-ef0f1d22cf60 | -18.50331 | -45.14067 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61deac9a-cbbd-3e97-b480-9666fcb94d7a | -17.12663 | -52.1368 | 2026-09-30 04:36:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9f116bd-cb20-3060-af63-7c84d4f47014 | -19.93521 | -41.8342 | 2026-09-30 04:36:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 968c149e-efab-3dd0-9bde-602f350250db | -18.90086 | -43.80628 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40fb7e1d-0bbc-3f96-b1b9-3c34d66bd67b | -19.5311 | -42.93137 | 2026-09-30 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bd152911-be99-3e37-9995-7a01703b5bb3 | -18.49283 | -45.13907 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89e64425-b945-3b47-8371-199bdfcb95bf | -18.89769 | -43.80173 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e17c52ae-5056-30a2-93bd-5ae35756af23 | -18.26284 | -53.05098 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9352b5c0-9042-399a-a4af-bfa776a31f4e | -18.10362 | -44.40653 | 2026-09-30 04:36:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1edad102-11bf-302a-af35-33dbb669ff2f | -18.27447 | -53.05741 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 858789b7-f12b-39c6-ac32-efcce6109bb5 | -18.30291 | -43.32412 | 2026-09-30 04:36:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 29678129-b568-3b7e-aef1-f56f0cb61c24 | -18.68703 | -48.62777 | 2026-09-30 04:36:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 491e4977-fec8-37be-aaa0-6d34b52abce6 | -19.53367 | -42.94254 | 2026-09-30 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44cc5caf-8a5c-31be-8b04-82435572def5 | -17.9196 | -44.40475 | 2026-09-30 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 78f4d50f-1927-335b-b3a6-fe22a7240bb5 | -18.27108 | -53.05271 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| eb564a65-08af-3728-b932-1193efe1d141 | -18.88396 | -43.81876 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 243af4c9-175c-31dc-a801-e0fac70f1786 | -18.23505 | -53.01697 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13b04aa4-9d92-3608-9abf-ec4319efcfc2 | -18.30223 | -43.32916 | 2026-09-30 04:36:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f6731ce9-f072-3d6e-8ef5-cdc8bc7cbb11 | -19.86952 | -42.64004 | 2026-09-30 04:36:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f9bfba4b-952e-3fe8-9499-9cd806e48bbf | -18.33292 | -53.07223 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efa184e2-7874-37e3-bb0a-00df4b76c296 | -18.27035 | -53.05657 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3b9e4295-ab7d-3ff3-b23e-1b94f2441ca2 | -18.49516 | -45.14762 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f11c868e-9128-3a8a-94b8-325d4c4efe78 | -18.23768 | -53.02562 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5077348b-9d93-3aa9-8ce5-5d0c2a279377 | -18.48935 | -45.13851 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b689e9-427a-3202-87dd-e713ad80aa3e | -18.50795 | -45.13335 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71a5a510-8d60-38ae-a1d3-db0627e14583 | -18.7879 | -47.35448 | 2026-09-30 04:36:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2383f586-3024-3d73-bf0b-dfbcf843647a | -18.49981 | -45.14015 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a466325-2eb2-301d-96f5-d66960768869 | -18.90146 | -43.80194 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9c04645-9cf6-3433-affb-a121706230df | -18.28149 | -53.04281 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30c11b38-35ad-386c-9160-1b06d2f48675 | -18.88832 | -43.81471 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08da8d17-4ceb-380e-adad-7740213398d4 | -18.25872 | -53.05009 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cf5883c7-e35c-350b-a218-e170a5208301 | -18.27398 | -53.03722 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bcc2b8c-303b-3255-95d9-280712fac367 | -18.28222 | -53.03894 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 842d0596-1f62-3417-b274-18a35c9b831d | -18.24783 | -53.03976 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b336fd36-0061-32e0-aadf-c5194784c456 | -17.91603 | -44.40417 | 2026-09-30 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e60494ce-033f-3b04-9120-1304bafdf85f | -18.2222 | -42.31502 | 2026-09-30 04:36:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d74eebb-f720-385d-840d-bad02a4067a2 | -18.5157 | -46.27314 | 2026-09-30 04:36:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d5ec823-0728-3cf2-a5f9-aab9d0222462 | -19.21643 | -44.75708 | 2026-09-30 04:36:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8287b27-492c-37a6-b3f0-c94fbeb7b4ab | -17.33976 | -47.06449 | 2026-09-30 04:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7960e98-585b-3188-b498-ef00661e6fd5 | -18.51085 | -45.13791 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caba5f91-354c-3e1f-99c8-1524a4cd86ca | -18.25533 | -53.04536 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1755d806-cc15-37ed-94b0-ca41ec7d5e09 | -18.2781 | -53.03808 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47249d65-3697-38d9-b29b-b3a5e0fefad0 | -18.28345 | -53.05524 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ca5b57f-d644-397e-862a-d697495f5260 | -19.38828 | -44.70256 | 2026-09-30 04:36:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 823122d6-d702-35cb-baed-3f262fd3e254 | -18.26696 | -53.05184 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1fe7a2f7-35a6-393f-a94c-6ac821961f3e | -18.28489 | -53.04753 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd41df5f-19d2-3bec-98fa-37183a97bfa0 | -18.25122 | -53.04447 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 25c8249c-ab9b-361c-9740-548856a7e430 | -18.88894 | -43.81017 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 726955fe-ddcd-378a-95ac-02d7287f2316 | -18.28255 | -43.6957 | 2026-09-30 04:36:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7c2afe6-255c-3e0b-ab15-a9b3258f511c | -18.28901 | -53.04837 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17e975dd-ffb5-33bd-aee4-5dbf65b49b21 | -18.89331 | -43.80597 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e73278a3-85b9-3759-968e-722b4941aed2 | -18.1066 | -44.41119 | 2026-09-30 04:36:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3f9218c-61ef-3056-814f-ae99b3d2a3fb | -17.91661 | -44.40005 | 2026-09-30 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde7f110-cd0c-397d-8196-c71af74d93ca | -17.78982 | -47.17056 | 2026-09-30 04:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5aa1c86-67e2-344e-82c6-fe88bf025c1b | -18.88519 | -43.80981 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5713f474-34ad-3d93-a6e2-2316a87531eb | -17.12265 | -52.13602 | 2026-09-30 04:36:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85a730e9-72f2-3816-8afe-4bb00f1d61b5 | -18.25945 | -53.04624 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e55b26d-325d-3438-983f-4f005b7dd1a5 | -19.35841 | -41.49377 | 2026-09-30 04:36:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df97b2f2-aacb-3d2b-8072-fe73e04b79a5 | -18.48993 | -45.13453 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README39.md)
