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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 039db61c-3f44-352b-8c42-711390fa8415 | -15.29928 | -47.32337 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7587cfdf-8782-3079-a587-997d0f562c37 | -15.3445 | -47.99193 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8af252e6-9b96-3292-9b5e-994e41f05533 | -17.09151 | -39.44321 | 2025-10-06 03:38:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fd109561-ab50-3fb0-a982-4364fdb9aed0 | -21.44258 | -44.03154 | 2025-10-06 03:38:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3bae618b-3736-32e0-b74a-5b8f36d78e02 | -14.67519 | -48.39169 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b456ba9b-52aa-38ae-8938-35d0c5454961 | -15.32631 | -47.31654 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97c2a60d-5213-3c4e-833a-0efc2b4d9e7e | -19.66249 | -45.92002 | 2025-10-06 03:38:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96e5ea1e-a9c5-3d40-8f0f-2110f31f6818 | -14.67643 | -48.39616 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 438d8a61-15e1-336e-99ec-cc223b5f40f9 | -18.39071 | -45.22509 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8954a57-a4cc-3c49-a5fd-6b055f58c7e0 | -15.34463 | -47.34834 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c506f0e-012f-3796-8022-39a73313e1b6 | -19.90018 | -46.79912 | 2025-10-06 03:38:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84f9a3bb-077c-3ae1-9cfe-f59d8b3825ec | -17.07539 | -43.38607 | 2025-10-06 03:38:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e02d0786-4258-3c3a-84b1-359db344b43c | -15.74768 | -46.25754 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0996562-1466-3a61-a5b0-286f11b7902a | -15.84432 | -43.30678 | 2025-10-06 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd998551-bd51-3ea0-b3ea-ea38fecd77a8 | -19.1109 | -43.6132 | 2025-10-06 03:38:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccd9058f-f5a7-376f-b73d-ebc80f3c6993 | -14.55421 | -46.63655 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deae0797-bab0-3689-990a-7a5e37c7035d | -18.39569 | -45.22664 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e8467b5-f99a-3a2e-83fa-798765c20732 | -19.62377 | -45.92382 | 2025-10-06 03:38:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00725fb8-04cd-3f6c-aa08-b8e3ed2b0387 | -13.35571 | -47.57563 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99ddbf44-8d53-3d0d-8179-7b7540890965 | -16.32685 | -41.95121 | 2025-10-06 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 52072c1e-0dba-3c4f-ad49-416158cf6730 | -17.58863 | -44.45461 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7819e537-beba-37cc-8596-93d107df6ca2 | -21.21637 | -44.2346 | 2025-10-06 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 53289021-d472-3343-8de5-7e5563493a27 | -17.26014 | -46.91499 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de25a0bd-07d1-3f64-9b96-7090da7f59ff | -19.5054 | -44.17467 | 2025-10-06 03:38:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a6f4fb2-21ba-37fc-bd4f-7bb21fe1720c | -14.48763 | -47.54961 | 2025-10-06 03:38:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bd18607-5aca-324c-9cbe-ceb2d288cb1f | -14.69754 | -48.29823 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7f9fda8-dad9-3bcd-b862-a45a51b6685a | -14.54085 | -46.96957 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8778195-8e4a-3a46-bc2d-ba02dfd4ca1c | -14.69132 | -48.29531 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bea2f465-6f37-37cb-817a-08cc5cabb5e2 | -14.91104 | -46.8488 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d754270-fac4-3c76-ae6f-ab121aa86977 | -16.35025 | -47.05545 | 2025-10-06 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2f1ace-ca5d-35a8-b1af-1fd59b0421af | -21.3607 | -44.50845 | 2025-10-06 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d46ebf80-79d8-3fd8-9755-7a00def07f28 | -13.72128 | -48.07176 | 2025-10-06 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea29a8c6-ed54-36b4-89fd-6d794fecbb27 | -14.4676 | -46.33791 | 2025-10-06 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa716d37-e5db-346b-83b3-8f740ec317fe | -15.3279 | -47.30906 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bedb5a9-a519-36f8-949c-6d0d23fe7545 | -13.63113 | -48.7184 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b26dbb18-94d8-3418-8764-ddc2d1ec0209 | -17.07635 | -43.38114 | 2025-10-06 03:38:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eda1c184-c2a0-3a4e-b524-bd0d429542f6 | -14.46164 | -46.33721 | 2025-10-06 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23074e56-5be3-33b7-bb53-26fd0e3bf19d | -20.26469 | -43.63843 | 2025-10-06 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56ba8481-29ef-34c4-b689-d536a3057c4a | -15.51628 | -47.35046 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ca9ada1-26d1-3896-8ce8-a8db6d1d8c45 | -14.94602 | -46.83143 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0138049-fa9c-3632-a4ee-e40ad9ae9fcb | -14.34206 | -47.72429 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 402f7f54-2bcf-375f-b96a-862282d4809a | -13.68656 | -47.31569 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4008745f-5ef5-3d47-8350-8a112e4911f5 | -18.28538 | -45.42435 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 960f4aaa-4dd6-3040-bee2-48999601b2b6 | -13.49896 | -47.24384 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8415e496-5e1e-32ab-9561-b11750cc5da5 | -13.25973 | -48.47719 | 2025-10-06 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ff7cccd-8a80-3d50-b0bd-9b9ce5f6c0ee | -18.397 | -45.22019 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f7c9b803-fe76-3707-9c46-4bfb19863012 | -18.87422 | -48.60955 | 2025-10-06 03:38:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 677f70b1-292d-3920-81a8-5353dd220f63 | -15.28716 | -46.32888 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1005459b-c173-3a43-b490-a77dbeb6622f | -14.67811 | -48.37857 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7692ec20-85ba-3cde-b546-f9d1b4a25230 | -16.10256 | -43.62827 | 2025-10-06 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a1cc842-1ed6-3070-83d5-1ea6920a6e7d | -13.55299 | -47.23622 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1f04bf9-d6d7-3f6d-91d1-e5180a9c1321 | -15.74832 | -46.25446 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7ac2226-7be2-35a4-9b31-3b9a9734f021 | -16.29397 | -45.24444 | 2025-10-06 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 007e913e-c332-32f2-b0fb-06e46c615ea1 | -14.66716 | -48.28043 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7c99330-389b-3294-b597-a37f0a1fd079 | -19.59205 | -44.64759 | 2025-10-06 03:38:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bccec805-9880-3360-95ce-8caa421e8dc6 | -16.23503 | -49.66753 | 2025-10-06 03:38:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 430ec211-4b1e-3db3-8bdc-67ffa02853c1 | -20.20258 | -46.15001 | 2025-10-06 03:38:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55dff8b4-fe40-3f09-955e-59f4976f498f | -15.91409 | -48.83389 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c092d076-200c-3fb2-83d5-ff4b48ada015 | -17.38979 | -46.64865 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f40d910-2817-3bca-8039-f319e9a08b76 | -18.27656 | -45.4151 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a9ea067-39b8-3564-994d-325dc4c7c733 | -15.33162 | -47.32158 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c73ded2a-94df-316f-aa37-6c188874f215 | -15.92099 | -48.62616 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3ae2fa9-2289-383b-a96f-06cd1cf13dca | -15.57715 | -47.27585 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf3f1a7e-5eda-32fa-b3f2-2289696f8b19 | -14.71193 | -48.35891 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1e833a6-9e87-314e-82a6-8291be4a0d00 | -14.65527 | -48.36673 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 587c952c-6f91-3ca7-a859-a3bf5157cd71 | -15.15372 | -45.7598 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 631cc5a9-189d-307a-be02-156b57baff78 | -14.68298 | -48.39772 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6b0b4d3-b719-35b6-bced-af846991ba67 | -15.33249 | -47.3175 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 913848db-085c-33ec-a272-d7f13d058438 | -14.68312 | -48.38703 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ef56a5c-5f89-3c9d-8961-5c3d19f91bbd | -13.30482 | -48.0683 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a60e01b2-f045-30be-ac7c-fe6b76b57b77 | -17.60349 | -44.45008 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13a84d09-29fc-35fb-973d-ce833bc6775d | -14.5378 | -46.95381 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d291cac6-71b6-35c6-a2e7-9b878319f596 | -17.65445 | -44.43239 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473f2367-d2f2-3981-8561-31d0866fb46a | -14.9267 | -47.13099 | 2025-10-06 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56662b26-c116-39af-8939-125fee51966a | -14.26908 | -45.87001 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2161755-ef74-365b-8667-e6de07aa09e2 | -13.49104 | -47.25028 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 971765f9-d6fb-35a6-9653-065ac910fe91 | -15.84731 | -43.31114 | 2025-10-06 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17547cb5-5a76-3429-8e8b-6beaff39664f | -15.34335 | -47.99048 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fac3aa3c-d7e0-3bfb-a11d-6b3bc6e4e7ef | -14.69228 | -48.2909 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 583ef925-a938-383f-a075-b56d7331934e | -20.19818 | -46.14518 | 2025-10-06 03:38:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b743b4b5-9c2d-3ada-a624-02d8704d4f5a | -18.87591 | -43.7463 | 2025-10-06 03:38:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0b44bb3-53dc-34a6-9945-d0b515e37002 | -14.68569 | -48.37546 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56e4e9b4-859c-3ea7-91fa-2a1ead85efe4 | -20.20331 | -46.14663 | 2025-10-06 03:38:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fa1a17f-4be0-35a8-9311-f8befa3cbc6d | -15.45662 | -44.3094 | 2025-10-06 03:38:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba6aac03-8ccf-3dbd-9957-84696d605341 | -14.91933 | -46.83057 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb9cdbcb-1f26-3e6a-a1b1-a76fa1696705 | -13.26165 | -48.47396 | 2025-10-06 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 987d96d9-8d5f-3967-8910-07c2a697ffaa | -13.34732 | -48.04988 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 932af2f8-f6c4-3eaa-9ab9-1769d71fbcd8 | -19.94036 | -44.64056 | 2025-10-06 03:38:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 449c3d8a-bcc2-39ae-82f7-b1ee79a3aaba | -20.26579 | -43.64054 | 2025-10-06 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a6f3ecd-b6aa-327d-900f-c5e5aeb2fb6b | -14.54944 | -46.65916 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c31b028a-51fb-32ae-aaa0-6778740d9a4b | -17.60349 | -44.45702 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d87ad8b6-eaee-31ca-b08e-e2599b7a0ab1 | -21.43836 | -41.24669 | 2025-10-06 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 92cbec31-50df-378c-9775-9356f9a46a9d | -14.46252 | -46.33291 | 2025-10-06 03:38:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8ca6a39-6a0b-324a-ab98-8da7c7a05875 | -14.69645 | -48.30329 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09295465-3450-3783-997f-fdd280dd9998 | -14.93257 | -46.82692 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c0e6ab5-92f6-3a36-8d08-f23c57adeb5b | -14.94504 | -46.83604 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0779b8b-ccab-3bc1-9be6-709ea0e3e0ed | -15.84902 | -43.30774 | 2025-10-06 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22ae55d6-05f2-3521-8bf8-2d1c534822fc | -14.68608 | -48.28789 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56cfad52-f3d9-3f0b-a5c2-330fd19ec6a2 | -14.55442 | -46.66506 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f9d9a35-f2bc-320b-945a-cd1a2cfc1097 | -15.87414 | -46.257 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
