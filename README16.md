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
| 8ba959c5-3b4f-3557-b462-4ac4ee6cbb92 | -6.93528 | -43.54457 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9080eff4-52e6-3f02-b8d5-63c1c8bf21a3 | -7.56093 | -43.08653 | 2024-12-12 04:16:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54ed181c-800b-3d34-955f-71a3385328dc | -9.794 | -36.22546 | 2024-12-12 04:16:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| c455aecf-0f60-39d4-89a9-4f9f9c421bbe | -11.20284 | -53.81977 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1b2de5e-9066-39ae-97c1-9be6d03cbd68 | -7.79365 | -35.13023 | 2024-12-12 04:16:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f75b8475-0285-362d-8877-a1d83c3979c1 | -9.11314 | -49.4672 | 2024-12-12 04:16:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 036df411-3129-3fdf-baf5-f4d5bc45dffe | -7.79406 | -35.12718 | 2024-12-12 04:16:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8dd14e35-da99-3571-9e5e-9b5aa8716d23 | -10.01987 | -47.56091 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b97f1cb-c30c-333c-965e-64a65a6e2e8e | -9.435 | -43.21226 | 2024-12-12 04:16:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c02ac2c4-6cea-3379-b7df-f9af6ecf0b1c | -6.92692 | -43.51139 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 144266b4-595a-3639-a12f-04ead2f0707a | -6.91539 | -43.52021 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee1b5dec-8ee8-39de-95d4-eb057f36f905 | -7.67159 | -40.84917 | 2024-12-12 04:16:00 | NOAA-21 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 908b662a-35f7-30af-9047-381905cc5bb8 | -12.65877 | -46.5806 | 2024-12-12 04:16:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50dd0ca0-6795-3a36-a6fc-305427760e41 | -7.56785 | -49.40322 | 2024-12-12 04:16:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c2d38b7-2a32-315a-aade-25db5a392f5a | -6.97298 | -42.99775 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93346b53-3369-36f6-8700-7e3c761c8c52 | -7.4347 | -39.76938 | 2024-12-12 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a6edf24-8f6c-33eb-92af-b2a183f89f24 | -7.94723 | -49.75024 | 2024-12-12 04:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b0267bc-0eb9-31c6-a965-bd2983f07c17 | -11.20219 | -53.82314 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a1fc106b-a899-3296-acf6-3b40cfa2d139 | -7.30243 | -44.52025 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cdd4b9d-3e21-3d7f-b0eb-e63ba1b944d0 | -7.79447 | -35.12409 | 2024-12-12 04:16:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 387d2459-6dab-332a-b00f-344f7a63eb59 | -9.37336 | -43.28148 | 2024-12-12 04:16:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7c99214f-fa3d-31bb-b9e4-1475ddf98793 | -6.7462 | -44.18684 | 2024-12-12 04:16:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b5c3dfe-f650-3157-9358-5032377ccb1b | -10.53959 | -44.68055 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 43af499e-9a88-37ca-9162-c3e5c23b28ae | -5.93068 | -48.05842 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1151c9a-db7d-3b1f-b91c-43b6504d3457 | -7.4745 | -44.74335 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5914e62a-5642-30d3-9abc-95c7ec68aa18 | -10.00329 | -47.56865 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 831836cb-37d6-3f39-ba7a-bf1180f98986 | -11.20268 | -53.83313 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 227fb2f0-84cb-312f-a72d-6b5df419cd4e | -6.92645 | -43.5361 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9518e81-4529-31e9-b99b-031d62cd094e | -6.93137 | -43.52625 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 413c4122-5717-3a14-a33d-0e7ec8152c84 | -6.96636 | -42.99671 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecae97d1-91a2-3c77-ba5b-b17da612b437 | -7.86648 | -35.1529 | 2024-12-12 04:16:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1255012a-0ecc-3e6a-aa84-74fb787707f3 | -7.80097 | -46.2091 | 2024-12-12 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f317943b-3ee6-3ffc-8a78-32f127af9003 | -11.2069 | -53.82739 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b329d83-db38-3a9e-bbc7-fc181fc1be2b | -10.87467 | -44.34412 | 2024-12-12 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97dd7a63-0e39-30cd-8b75-b6e89f236700 | -6.91977 | -43.51382 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f48d0fb9-557c-382c-9124-2283d5ef3ac2 | -6.94351 | -43.53522 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f43a0606-b90f-3158-b6ca-23b85ff4c164 | -11.11778 | -54.64895 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0b37d6c-1e8e-3687-bab4-b8b13a8cde3a | -6.96305 | -42.99619 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b27abfd-e325-357e-89cb-1f5167bbc4c9 | -6.86116 | -44.77359 | 2024-12-12 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 893959e0-20bd-3f05-8f69-6144f6a58bce | -8.36611 | -44.48484 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87b29a2b-e3bf-3ec8-8321-8bfab365f1e9 | -11.20331 | -53.82973 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4efc4f69-0625-3e8f-ba50-2ed0ae4d6ba1 | -11.87541 | -43.71811 | 2024-12-12 04:16:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4133f57a-40ed-3438-8d7b-f73a6cbea764 | -6.92753 | -43.52919 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 871c5768-db60-3b9e-b692-888ddfff7470 | -6.91593 | -43.51676 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fac3b1b4-b5a8-3fd7-86ca-3e6b62289272 | -7.79958 | -35.12481 | 2024-12-12 04:16:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d555edc7-68cd-3c3e-9d0f-72778a89bc93 | -6.93636 | -43.53765 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5bf544c-5cb5-3c4a-a226-e6cb462197bc | -6.93252 | -43.54059 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89cf9cf3-190d-3341-98c4-3c9512af3d5e | -14.05076 | -43.3044 | 2024-12-12 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0d199243-f489-302a-98d0-93a4bb625318 | -11.68681 | -48.07772 | 2024-12-12 04:16:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e448287f-0da4-3020-b968-4feabe292b22 | -8.86323 | -35.72847 | 2024-12-12 04:16:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 95a5bcd0-e6e0-375c-b22f-2c6caa6ff330 | -7.86332 | -43.08783 | 2024-12-12 04:16:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8434f31e-cdbb-36c9-8923-14f915e99c34 | -13.86872 | -43.06879 | 2024-12-12 04:16:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba8f1ecb-251c-34bc-82b6-e5133c290647 | -7.71347 | -45.66365 | 2024-12-12 04:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18f11269-da04-3647-987c-618ed22311db | -9.12775 | -43.1102 | 2024-12-12 04:16:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ea814772-d088-3215-9403-b06239a83c8d | -10.28976 | -53.69824 | 2024-12-12 04:16:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a264f2c-2781-320e-98ba-6385d6e37066 | -11.68336 | -48.07806 | 2024-12-12 04:16:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ffb83f8-c4dd-34e7-9f59-03d8dded7b2b | -12.67145 | -43.44072 | 2024-12-12 04:16:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00174332-ecbb-3cc3-8b2e-2df7b1584be7 | -6.9669 | -42.99324 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 258d8233-77e9-3413-bf2a-c5fa393fdba5 | -11.20089 | -53.82987 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a73a8a2d-4f83-3045-b044-955be2cba079 | -12.35405 | -44.71275 | 2024-12-12 04:16:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43508726-a3cd-3393-b310-0754fd18d433 | -6.9253 | -43.52176 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f77d60ec-4320-3a29-84f4-4b0fb5923178 | -10.02295 | -47.56303 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fa082a8-3315-3719-b914-664e0d6a193f | -8.907 | -44.22454 | 2024-12-12 04:16:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b8cd1c1-3d02-3ee7-b81b-d3d53753956d | -9.38987 | -38.87694 | 2024-12-12 04:16:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6386c6c5-2d23-3b12-80e8-9fa8d7ccbb8c | -6.93967 | -43.53817 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f9e7396-65ab-3e5d-8696-9c43a4314ac7 | -6.9369 | -43.53419 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 338db095-0788-3f0d-9e21-16bca797b8be | -11.69413 | -48.07901 | 2024-12-12 04:16:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cf6ee18-b69e-30c4-a663-873a748487de | -12.42799 | -46.63874 | 2024-12-12 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ba27d5f-a8d3-3162-9d4e-3543b8ed7324 | -11.19894 | -53.83998 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e5aa65c-7d29-3614-b96f-75d627420ed9 | -6.93299 | -43.51588 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 34c2f55b-949d-3684-9df5-d00f261fbc10 | -12.36477 | -41.18333 | 2024-12-12 04:16:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e72cda6f-a5e8-320a-a463-e987a66a8dc9 | -10.5429 | -44.68108 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64a30d86-3c29-37bc-b58c-81940f1d3158 | -13.18447 | -43.57262 | 2024-12-12 04:16:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61c4bc52-ba6d-316d-942d-c6ac4ece5286 | -7.2991 | -44.51973 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe689a0c-3d87-3109-82c0-c665b12f3534 | -12.50366 | -43.87558 | 2024-12-12 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7349168a-bf04-33c5-b17c-344f4fffbae3 | -6.92699 | -43.53265 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d3fc224-1955-3f92-910b-3409c283c69d | -10.55556 | -44.57906 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a4dbec0-1207-3e60-9681-d425e1fe1caf | -6.92422 | -43.52867 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cbb0a57f-d7ed-3917-a8b3-7786f26534e5 | -8.62399 | -50.01899 | 2024-12-12 04:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0cd86ae8-62ee-342b-a1b5-e34599c0cb2c | -12.19735 | -46.71729 | 2024-12-12 04:16:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8195c927-7669-3176-8bad-ad7d03b4189d | -6.93414 | -43.53022 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b5ea5321-2183-3ab5-9e5a-104c2a3fe5ed | -6.93245 | -43.51934 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 50210570-99ad-320b-901a-0fbd2f7d80d7 | -11.21225 | -53.82831 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbfe4b5b-631c-36a7-9519-adc360b27bc1 | -11.20494 | -53.83758 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26ee088f-b2d3-3fb6-aa28-d2bf643f6054 | -7.43348 | -39.76678 | 2024-12-12 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0779af2c-998c-3975-af1e-662a5c6ec3be | -8.6986 | -50.19587 | 2024-12-12 04:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7489e8c8-aa00-3929-a9ee-c8b91ee78d8c | -8.6936 | -50.19535 | 2024-12-12 04:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a81622-ab96-351e-a859-3985edc770f3 | -10.76979 | -45.03152 | 2024-12-12 04:16:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a8fff9a-dc23-3d27-9ab6-056bbba15c9e | -8.37331 | -44.48239 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af10d9fa-02e3-3cfa-b33f-dd4fe97bb28b | -10.00258 | -47.57296 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53f73016-39b1-35bc-bcb2-beb4116a93ec | -6.93913 | -43.54162 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 425e5b53-e44a-3703-9f76-a11b8a71a6db | -9.78504 | -37.10738 | 2024-12-12 04:16:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3577a8c3-6887-3011-aeb2-e5ed92bb4076 | -10.53904 | -44.68406 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d722ffb-4e3f-395d-a16e-8e846c2b49fa | -10.0206 | -47.55658 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 508d179e-c775-32a3-af18-c12a4985fb85 | -6.93083 | -43.52971 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 85bed0a7-9759-3226-8c93-43234aff8825 | -13.18111 | -43.57209 | 2024-12-12 04:16:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ba3d7f8-183e-325f-b8c2-c067dcdc6af7 | -11.80171 | -43.80117 | 2024-12-12 04:16:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87e1640-0f9d-38d3-9be2-87532288f264 | -6.85724 | -41.06556 | 2024-12-12 04:16:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2f2fb340-7207-3434-8aab-4040a6de05a8 | -12.46875 | -43.88102 | 2024-12-12 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d653fd2-8757-3b18-9ab1-e843816cb6bb | -9.66545 | -36.34943 | 2024-12-12 04:16:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README17.md)
