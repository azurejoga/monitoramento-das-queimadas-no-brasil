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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e8a41d6-6d5f-32b6-b133-a44fc22bfa1c | -4.29356 | -48.60782 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0c1e74de-eea0-3993-94e8-8705bfcf538d | -4.29303 | -48.61126 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e2b2d0b-904a-31e1-8aba-81d981979f50 | -4.29195 | -48.61814 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771e52b6-3001-3c0b-8f8e-1d4684320a40 | -4.2875 | -48.60335 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 836cc718-7f38-375a-954a-e4bccee69b29 | -4.2514 | -48.54848 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f3ed56-dc50-354f-aa29-c545d05c951d | -4.2481 | -48.54797 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c021e06-e9d0-3081-b6d2-ca689d19551e | -4.24702 | -48.55486 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0813c5e-fa35-3b1d-927d-ac8f7f1e88f1 | -4.23819 | -48.54642 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 697e89d1-d159-3f33-80d5-64cfe59f8de6 | -4.23657 | -48.55676 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 196126b4-00e6-3cda-a27a-5227960fee61 | -4.23603 | -48.5602 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50bca8a2-9222-3686-8bbb-d0dadee9f5c4 | -4.23327 | -48.55625 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47d30ede-f77c-3a71-993d-6e5a04606391 | -4.60109 | -48.07455 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca9629d6-a747-3f89-9318-c76dd8a9b23c | -4.59776 | -48.07405 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f099d0aa-f91d-394d-9910-d48e517380a9 | -4.57169 | -48.02304 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 921dc0f5-6b74-3a9a-abbe-1d4ca17522c9 | -4.35468 | -48.15009 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 553fe119-570e-3be0-a086-fdac75fa5d09 | -4.35114 | -48.14973 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b6ec406-7b66-3e49-b860-a4319c9fcea2 | -4.3506 | -48.1532 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc816aee-c43e-3092-a4cb-f5475dac62a7 | -4.34782 | -48.14922 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0728431e-a83f-3123-8769-430778089760 | -4.29313 | -48.15133 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b44da679-d15e-30e0-9274-bba32079d742 | -4.37118 | -48.63045 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a08e4f05-bf13-31b9-937f-da73873a6533 | -4.36788 | -48.62994 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9394e459-cdca-3943-ba75-531095e15a9c | -4.36404 | -48.63287 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2dda2dc-ac8f-39e3-9ec4-ffe74c746b9b | -4.3635 | -48.63631 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00d602ea-d418-3cde-844b-bae5edc63aa2 | -4.3602 | -48.6358 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 832c47af-c64c-3493-a253-ad35f5b56f01 | -4.34423 | -48.6298 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ccdb5e6-48cc-39cb-9c46-206cad63be2f | -4.32941 | -48.63806 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88cd57e3-d609-34b6-81a2-87146c93ab82 | -4.32887 | -48.6415 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16c5e791-5814-3456-96ad-bd84a0a87dbb | -4.32611 | -48.63755 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcbfb36b-1a2b-33b7-9e0f-11b646b58999 | -4.32557 | -48.64098 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02081522-a05f-3d68-bcad-8f1a71c0b10a | -4.30139 | -48.64427 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f19e9d0c-bbe2-3035-9185-54eaaf06a3ee | -4.30085 | -48.64771 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 162febae-cb52-3fe5-98f5-b589d035bbb1 | -4.30031 | -48.65114 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59f59ff3-e693-3a1f-b817-a4144797e0fe | -4.29809 | -48.64376 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be571edb-4f5a-3b2d-8c87-de80b74a1d42 | -4.29701 | -48.65063 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48c1d38e-2faa-3174-8bbc-7acced8563ef | -4.29694 | -48.62949 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ac9c60c-3917-3345-ae94-546f42f6c9ca | -4.29479 | -48.64325 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d864ba-beff-3b20-a8fe-a1405bc52dac | -4.29425 | -48.64668 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bdc47f0-3a90-36ef-be6e-32f9151797b8 | -4.29371 | -48.65012 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b0773f9-f4db-38e1-8d1c-715d67b53f78 | -4.2931 | -48.63242 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d13c81a0-4bf5-32a9-a969-da79ebd71e04 | -4.29149 | -48.64273 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2e5aaaf-85fe-3207-8971-59b417a6301a | -4.29095 | -48.64616 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a507a0-fc89-3601-9d29-e2928965afa4 | -4.29041 | -48.6496 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a155782e-dd7e-3864-9a0b-ff1c542dcaa6 | -6.39228 | -49.58591 | 2024-10-29 04:40:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c373e979-9ae7-38f2-bae8-1707734bf468 | -5.99608 | -49.59725 | 2024-10-29 04:40:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c8da4b8-1a39-36ab-9dac-0aced0d3fd6a | -5.97894 | -49.29383 | 2024-10-29 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d76fd78d-62ac-3ba6-a6ba-42c879ed3c19 | -5.88143 | -48.30582 | 2024-10-29 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f09c4861-a335-3fed-9947-dadbf05d7435 | -5.70451 | -48.98204 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3bcd4e4-103b-383d-8502-9a8dde92054e | -5.51598 | -49.21005 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56904590-3bc7-33bf-a0d1-e4d1d9b4adc6 | -5.29388 | -49.49546 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d58782b0-0940-3b66-8b39-42d91faaee16 | -5.20966 | -48.22962 | 2024-10-29 04:40:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36a2e27c-c97f-3fc6-b82f-5338b1257fca | -5.20301 | -48.22859 | 2024-10-29 04:40:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7c53865-94ad-321b-a833-802a12969a6f | -5.19432 | -48.30589 | 2024-10-29 04:40:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57f39740-dceb-317c-bc50-4ef80114b6ad | -5.12271 | -48.39463 | 2024-10-29 04:40:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a65eb189-9124-3688-b511-8d93c80901f4 | -5.26634 | -48.93417 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6f41b65-6246-3b0f-90f7-1c12de5b43b2 | -6.39283 | -49.58247 | 2024-10-29 04:40:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48f93329-4afc-3034-9c2f-6fb9c81ec8d6 | -5.70505 | -48.97859 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37e76070-f30d-32c4-92cd-086cdf7ed93b | -5.51652 | -49.20661 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4598b79-f7e1-31ac-a164-cf5db9e1b03c | -5.41308 | -49.23621 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7043c06-fed6-3146-9a31-25f709ae699f | -5.79293 | -48.50301 | 2024-10-29 04:40:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e14626b2-f103-31f8-bd9b-18651a0eda47 | -5.78961 | -48.50251 | 2024-10-29 04:40:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd05d708-8ca6-3b77-bb59-88ec31c9293a | -7.85947 | -48.75071 | 2024-10-29 04:40:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01e20ee1-4254-3e16-a37c-8959f8396bd2 | -7.72574 | -49.54366 | 2024-10-29 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bde95ae8-0414-36e3-b5eb-013dfdec187e | -7.10055 | -48.38283 | 2024-10-29 04:40:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 230aa8a7-c7e6-378e-a2b8-c2680e0acc9b | -9.02275 | -48.77154 | 2024-10-29 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 196d5748-2c4b-3048-aa5c-3e56919153a5 | -8.84321 | -49.86029 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b123c1b-48bb-3ea3-889b-0deeffa14352 | -8.84046 | -49.85631 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a6635b54-cd55-3d1c-88d1-0d37c90b0d6d | -8.81368 | -49.6814 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4448678-e915-3728-a694-7ab84212d91e | -8.7501 | -49.78155 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba41510f-69d4-35ac-9e9e-5696d8aa0e26 | -8.74956 | -49.78502 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f4c66d60-d5f7-3d0d-ad9f-00a19fef7386 | -8.53985 | -49.71222 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbe360a7-15c1-3679-894a-96b933299167 | -8.53654 | -49.7117 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a7d0b3-4bda-3c28-b996-eb9c700ec777 | -8.48636 | -49.44425 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6414d233-1aaf-3871-a612-417efb9df096 | -8.04898 | -49.65552 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad3692cc-b941-3e40-800c-d78d96979fdf | -8.04844 | -49.65898 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf232b03-1fb1-3510-84a1-50009734fd8c | -8.02417 | -49.68001 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71337a19-471d-3e6b-b3fa-6a2764a15bad | -8.02087 | -49.67949 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5b27bf5-f12d-3536-b6c3-59a2e72a8f47 | -8.83991 | -49.85978 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| be91f413-b035-34f5-892f-7b6ae6d8a76c | -8.45128 | -49.51705 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4792d19-f14b-32ee-9688-b43ae52e4b92 | -8.3055 | -50.01184 | 2024-10-29 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6317cea4-0a39-3eef-8092-9c5acbf9f6e1 | -8.16908 | -49.7561 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e606292-7938-3989-8125-6118ff9e290c | -8.02951 | -49.60281 | 2024-10-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8149906e-4cd9-3076-bbfd-c46b27347372 | -9.8657 | -49.69546 | 2024-10-29 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4484616e-2073-3e11-bf4e-13d5ed667824 | -10.87678 | -49.53493 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5f63e1b-4bb0-364a-a591-f9886bbc9862 | -10.8729 | -49.53795 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d860f81-62ee-3816-bbac-007f64bf7cdf | -10.40742 | -49.20269 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34c07084-7c07-3025-8a9e-4eeeac24799a | -10.36596 | -49.91167 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a44bda45-11af-3834-ba47-8dbb11fa7b41 | -10.23742 | -49.68986 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a17bc0e-e369-3660-9103-9c77ced47042 | -10.23411 | -49.68933 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1f72045-710a-3aaa-849b-8791e90042d1 | -10.23134 | -49.6853 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4da816c8-c400-395f-9468-f898672245dd | -10.23079 | -49.68881 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc63658f-8eec-311b-9583-1516b756920e | -10.22694 | -49.6918 | 2024-10-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 756558f8-9074-3aec-bcff-bfd7d5b6636e | -9.86956 | -49.69248 | 2024-10-29 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8f671ab-b96d-351c-beff-137c2ab5247a | -9.86901 | -49.69598 | 2024-10-29 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ad7eaae-1a9b-3b4b-9e81-8e2f559c0a24 | -9.57664 | -49.08006 | 2024-10-29 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 364f9884-0c2e-34ba-befb-8481befec4c1 | -11.30058 | -49.96043 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c022a4e0-6570-3a87-bb98-8f638dfb9a30 | -11.25224 | -49.87667 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255ce071-e68b-3096-b9f1-8d1743b52885 | -11.18262 | -49.8656 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43bbb445-27b2-3aae-b374-3c3bb22fc23c | -10.97709 | -49.30212 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20f47530-6368-3654-8bc4-df1c992ae9af | -10.97375 | -49.30158 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79d84ab8-a713-343f-b6ec-62aa18a30708 | -4.7692 | -49.45492 | 2024-10-29 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README62.md)
