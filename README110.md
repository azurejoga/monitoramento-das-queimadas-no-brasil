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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b05b9b06-93f1-3278-8bf3-99c550de86cf | -10.61956 | -65.21214 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fb5cac5-7474-307b-8d35-a22e6dcc6c70 | -10.61894 | -65.21597 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e39e230-7bf2-34d7-a1c0-4037b890e482 | -11.52596 | -65.11962 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 712a632f-7ee5-3b95-86e2-e1c5337e17a7 | -11.51914 | -65.11846 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e9afc28-c8a4-3396-86e4-3452804e6848 | -11.51574 | -65.11789 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd6fed4c-2daf-36fd-9fa5-f9817da6b70b | -11.51538 | -65.11802 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 572918fc-d025-3d19-8eea-6c857e9f4dfa | -11.50553 | -65.13561 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6f80390-30a3-3fa3-bebe-5add366db67c | -11.50516 | -65.11629 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89201455-af23-3380-971f-f064d9038828 | -11.50236 | -65.11197 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d0ff33-84d2-32a4-832e-bdd6317792ab | -11.50175 | -65.11571 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 097e64c5-5c48-3244-8674-47d52f6faa92 | -11.49895 | -65.1114 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9267e880-00ee-3806-8bef-18bca530609e | -11.49736 | -65.0996 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f28b1b8e-9bca-310a-9ed0-4fa4d325ba6d | -11.49675 | -65.10335 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c344e159-04bc-3487-8723-d8c424fcb88b | -11.49615 | -65.10709 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 683b3188-bd83-3d6c-9f9e-4ad9d1970d36 | -11.49554 | -65.11082 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1d357f5-a2de-3ea3-88c4-dfeb9ee87300 | -11.49335 | -65.10278 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3cb451f-0fc5-3b4f-8d0c-5fc1d51eee55 | -11.49274 | -65.10651 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 956a85b0-3131-30be-a82f-713b9940ef0b | -11.49213 | -65.11024 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c272e49-4949-32e2-9b47-e446ec53e2ec | -11.30039 | -64.99436 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cba6d7ab-347f-3ea6-9afe-07e41da09265 | -11.29979 | -64.99808 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c12319-8d30-30e9-8019-515c65b12c61 | -11.29759 | -64.99007 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc80ea42-0452-30b6-85ba-ccd2ff596cc4 | -11.29699 | -64.99378 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf85722f-961a-3d5a-a0c8-3b6a292616ef | -11.2966 | -64.97462 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62908f00-488b-3dc6-8a84-61c0871c3748 | -11.29639 | -64.99751 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b9f17e-6d61-3979-8b22-b4ded29e64cf | -10.90053 | -65.10188 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2844e201-fa87-3815-b02b-af23ad4d3863 | -10.89991 | -65.10568 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86188851-2064-398f-adfb-1de1be2bf63e | -10.89772 | -65.09758 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe2e7970-7827-3f6b-a4cc-f1d21ed02e52 | -10.89585 | -65.10894 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44af40f6-f84f-332b-b135-1da0f60b8413 | -10.89306 | -65.10452 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 586c740a-70f2-3a13-ac5f-ef8df7074727 | -10.89085 | -65.09659 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f65ae377-b0ae-336e-988d-946160b7fb60 | -11.92553 | -65.01329 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19ece379-ad7c-34a5-8fc0-03bb781e95f5 | -11.90449 | -64.97167 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 716021fc-61a0-3384-ba9a-9a74b12b9bd6 | -11.89698 | -64.93259 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07de14b1-04d3-36f6-bd28-b008eec65516 | -11.8948 | -64.92467 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76b386c0-c719-39ae-b7f9-3284103a829f | -11.8942 | -64.92834 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 002535b3-898e-3c3c-93ec-8fc5e8eb984f | -11.87596 | -64.99725 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7babc2f-cd18-39c0-b2c0-e51092f7d1ef | -11.87197 | -65.00038 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5094bde0-b571-3f1e-b85a-14081352bb83 | -11.87136 | -65.0041 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8517021-5d74-3262-840b-a484c7c1254b | -11.8136 | -64.86238 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41f8fae8-e124-387d-97f1-4b44b3ab9c6b | -11.80032 | -64.83756 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b16c9b7f-5527-3954-be5f-ea86fe7f664e | -11.73937 | -64.81981 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d266db-508e-3474-b24d-e1eda64c8380 | -11.73659 | -64.81558 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b4b44b-8672-3869-8277-ab707b4548bc | -11.72843 | -64.97303 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 248741ee-b8d3-3662-855d-9d37f8a4cff4 | -11.72723 | -64.98044 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 024cff19-8b19-3d08-85d0-f441587bd068 | -11.72564 | -64.96877 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd5c4c3a-2e51-31c0-9adb-5176aa80a9a8 | -11.72504 | -64.97247 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e705171c-5155-3db2-aa1a-3c2edf98b5ef | -11.72444 | -64.97617 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cc55648e-8491-3454-8d3b-782d306c1f1e | -11.72384 | -64.97987 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39423929-e499-3bfc-a25e-eb52f0f02a7e | -11.72324 | -64.98358 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38d2a004-45bb-38a6-921b-5a72cff1d173 | -11.72225 | -64.96822 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acae03da-ef19-34ef-9575-91f170359c19 | -11.72165 | -64.97192 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28b7fb8d-3e26-37d1-9a01-a902266725cd | -11.72105 | -64.9756 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 891e2c64-7083-36c3-a93e-5821e0b11db8 | -11.72045 | -64.9793 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83354cb7-5229-346a-b527-734504d6b34c | -11.64374 | -65.19228 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b208c563-ecbb-3661-a579-5a6c94867bc5 | -11.64313 | -65.19604 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1a32d92-b244-32ec-8267-c796613beb5a | -11.61147 | -65.21774 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ca04b84-2674-38ae-a07f-fcc537f6405e | -11.60858 | -65.21465 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0192d8b8-89a7-34e6-938e-8c4bff6186b4 | -11.60806 | -65.21716 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d90eb392-a4ac-3f08-8b84-151fd28ccf95 | -10.49113 | -69.69521 | 2024-10-13 05:29:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a69c1e0-4d31-3d73-a2a6-eb20b931ea45 | -10.49035 | -69.69971 | 2024-10-13 05:29:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c805cf5a-69b0-3e8b-91f3-038016c58820 | -10.48588 | -69.69891 | 2024-10-13 05:29:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 907042df-3747-39b6-99fc-6847d86f206e | -10.45832 | -69.69862 | 2024-10-13 05:29:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d72f288e-36db-347d-bfb2-fec1a84a2d09 | -10.45427 | -69.72134 | 2024-10-13 05:29:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be54d2ac-c51b-398b-824b-b676a3553dad | -10.42708 | -69.69304 | 2024-10-13 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1294ca9f-8a7b-36bd-a91e-59a156729512 | -10.42628 | -69.6975 | 2024-10-13 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e43473f-beca-381b-b393-7ce8f95e39a6 | -10.40412 | -69.1425 | 2024-10-13 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9707df67-619a-3df4-95e7-6970a675e4b5 | -10.40239 | -69.13985 | 2024-10-13 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89d7c5fa-2a31-33ad-9c31-c38a4962d3b2 | -10.40168 | -69.14401 | 2024-10-13 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fd3a8f4-fcbd-3900-9f37-9a4864604cc9 | -10.39982 | -69.14175 | 2024-10-13 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 116bb58a-ecf2-37fb-aa4e-709cf83f64f5 | 3.52387 | -51.77081 | 2024-10-13 05:31:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8200211d-41c0-31e8-a217-7936dfe3ded3 | 3.51906 | -51.76577 | 2024-10-13 05:31:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d9c03c6a-fe6d-3744-a1d6-99f3bca715f4 | -18.19412 | -56.85658 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 44fa8bba-4cd7-327d-b0e8-20ef45c7dbb5 | -18.19335 | -56.85213 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f7fd86f5-8ef6-3136-9914-ecfef5ea9866 | -18.19274 | -56.85766 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0b487143-85b8-3fd9-a57f-5cb50540726c | -18.2351 | -56.51767 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cf262da7-db15-3881-8bf0-878954b95d6a | -18.23474 | -56.5108 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3ac25662-3a2d-3379-a3b8-7fe851bf9f21 | -18.23406 | -56.51662 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1e849b6c-a616-3073-a276-9d342e096332 | -18.23078 | -56.5112 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 65f3aae7-068b-3a45-b916-f8813e96b71f | -18.23014 | -56.51704 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3a664607-c79b-3f19-8fb1-434b07ab137c | -18.22979 | -56.51018 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6095fd17-dc26-394c-af85-82361a5aa8a5 | -18.22911 | -56.516 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7042f659-695a-385f-bf1b-3d1b7a655a91 | -18.22754 | -56.48624 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b237c635-ddf8-33c5-84e7-ed50f6939ea7 | -18.22619 | -56.49792 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 70d20e5d-7d57-31ea-8186-85e1be054722 | -18.22267 | -56.53969 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a30eb8ca-c5c8-3188-9225-14917ab66e72 | -18.22258 | -56.48563 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6eedbfd0-5d51-3b3f-a7a5-f6d51c773a98 | -18.22204 | -56.54549 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c4f97b00-ec21-39e1-82c9-7915b7ca4a02 | -18.2219 | -56.49148 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3801423d-a275-3e91-bcf2-65696715e2db | -18.22141 | -56.5513 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 63551da2-9958-3802-b79d-6ff7005175ea | -18.22123 | -56.49731 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 959a4258-6a09-3435-aba1-79eecab2fe2f | -18.2208 | -56.54441 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cef5413f-134c-3ae7-8cbe-655daaaa3d09 | -18.22012 | -56.55021 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 98656048-6023-3cbc-8fa9-3000d4cf142b | -18.21952 | -56.56868 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 52616f72-0546-3ec2-96a9-b4ace2baea15 | -18.21945 | -56.55599 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e652c7c3-9b29-3294-951b-9e01f009b2f1 | -18.21878 | -56.56177 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 25ec6a1f-8c7f-3c41-ad94-db443f35068c | -18.21811 | -56.56755 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a23b5fb2-0322-37c6-b789-becf2ec4e423 | -18.21762 | -56.48501 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ffc46fde-cc04-3ac4-a555-f320b9c1fe30 | -18.21695 | -56.49084 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 105a59aa-fcfb-3101-ae11-b898ff536944 | -18.21677 | -56.57908 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 70b3c2df-8050-3186-b99d-8cab9832c2ce | -18.21586 | -56.5438 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3ee62251-db6e-3f05-bc80-4b6835c8706a | -18.21519 | -56.54959 | 2024-10-13 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README111.md)
