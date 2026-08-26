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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 150aebf6-2c65-3c31-bdef-5f3ce587b372 | -6.30578 | -53.57312 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b921807-dfaf-3b86-8a5f-5ab5badac8f2 | -8.59822 | -54.75436 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c255265-59be-35cc-8f82-031ef3a0bb38 | -6.74906 | -56.33425 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63487a6d-11e0-3b91-ab3b-b89c130fbba9 | -7.01769 | -59.23337 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47f0f9c3-400c-300b-9728-70d3b58c4ef8 | -6.68871 | -58.72561 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3276939-ca18-33b5-9d9a-7d5317d494e8 | -7.25508 | -49.85112 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6836e159-d7a1-3197-9cf3-a98d3ee70623 | -6.88946 | -59.95232 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74647208-1b7c-35a4-b33b-f016d1908f07 | -7.37496 | -55.18959 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cda9021-5921-31ed-b0dd-92b25b1f71a6 | -7.51644 | -55.58914 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b339678-645f-3543-858e-3099e428ccda | -3.22275 | -61.24385 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd77b7be-81d3-3dda-9707-f95968a57afb | -6.13985 | -57.84497 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f51ac2b1-98ee-30cd-89d3-567a99670174 | -8.86298 | -49.71902 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c1052a7-7c72-3fb8-8aac-e4f5f2ed7f2a | -7.38263 | -55.19051 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5613f88c-bf2f-32e6-835f-9f0f3828aea5 | -6.80713 | -58.66273 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d93407-85c6-361a-b57c-662fff26225e | -8.11223 | -51.66817 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6524a5c-9b98-32ad-b63b-c5f6c17b9a90 | -7.51824 | -61.37974 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| dfab906c-0d23-3d5b-a892-2f89db5f7b10 | -6.14231 | -59.92717 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f18f9ad8-6d71-342c-91e7-5ff03bb55b33 | -6.74619 | -59.64272 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb48cffb-f8f4-30aa-be33-e4dcc3f1b094 | -6.80708 | -59.68468 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dde90014-4b00-3844-ab4b-58cc22eb3c67 | -6.26563 | -53.37658 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9248af1a-8d38-3c15-89e8-07c580da9806 | -6.22881 | -55.61937 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a61577c1-4218-3bf0-b7de-0cd37d7a1532 | -6.54297 | -55.08822 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66b8cbb3-30d9-3936-976a-cd384b90eca4 | -5.56587 | -50.49238 | 2026-08-26 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5aec4c2-a8ed-36ef-8c3d-7d3c7d1b9b84 | -7.062 | -59.23038 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c646f8-002b-3c9b-b9a3-453f2cd294c2 | -7.39894 | -55.15937 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8abfc10c-d7a2-39a8-9860-060e4aae7895 | -7.09419 | -56.54652 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62329aa7-7dc5-3039-b7aa-7b5cc09741b4 | -6.64013 | -58.51437 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef92b761-b467-3595-bc27-96d0a8d3178c | -6.14418 | -57.70658 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8c470ee-60dd-3ab9-a139-ec3367c2fa12 | -7.38716 | -55.18626 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94e8361a-3135-3369-98cd-64db2fdd435a | -6.22945 | -55.61509 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30afbe76-4278-3368-a770-2c0d94f4c733 | -6.61723 | -58.38544 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9359b741-c284-3b72-bda2-001012567844 | -6.95248 | -59.09163 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e1a65cd-4cda-323a-9554-0133b39fea61 | -6.25353 | -53.3708 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fa70ec3-c80c-3421-ba36-91906823dd9f | -6.26198 | -53.37204 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad354c2c-c5d9-3ecc-a42d-f8798cae3205 | -7.2812 | -59.62113 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c834929a-fee9-35c3-a8e2-ff95593e3502 | -6.30995 | -53.57376 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46f69c0e-cdd7-3431-83b6-ee97171e9a0a | -7.03816 | -59.23306 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 570c95c6-f0c8-3b6b-91cb-9b25849de04e | -7.25891 | -49.86408 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 910b4096-3cd3-31f2-9c8d-255d2c4ec826 | -6.1094 | -53.8475 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a3afe72-743a-3944-9fb2-dd315235c829 | -7.03484 | -59.23253 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc080c3e-fe77-319b-8267-fe092f32d76c | -6.65008 | -58.49445 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 698335f5-6469-30a1-ad5e-5694e6658122 | -7.02382 | -59.30194 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97340f1b-939c-3306-83f9-754cd5c9a7f9 | -7.11006 | -56.56119 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83b2bd5a-3fbb-392d-ae4e-aeecf28d6c81 | -6.11831 | -57.6952 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53ea0ebb-7c96-39a7-a972-9467e20bf81e | -8.95374 | -50.77296 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b47a694-a2ec-3c6e-976c-c2dd1afa0d5e | -8.8202 | -49.60799 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a44da6c7-ddcb-3e4e-ad7f-3c8d9bfa8415 | -8.08114 | -47.50376 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86b8895f-5526-3841-9abe-9789aef214a5 | -6.1172 | -57.70237 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fdfbc2a-647d-31d4-9555-e72d3f252d71 | -7.39063 | -55.16272 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03d833b4-8d2d-3aad-9fb9-8bcca4af0db0 | -6.27407 | -53.37784 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67371b55-14be-3d14-a282-2bbf3fbd1cee | -6.4234 | -54.94172 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 824fa63c-cc7c-32e6-b459-981ae789619f | -6.64455 | -58.50791 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2437d374-df22-3c33-af99-ebe019560728 | -5.94741 | -57.73523 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e337712a-d3e7-3069-a8cf-d3f56b134631 | -7.11359 | -56.56174 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c854ac1-f303-3ad0-b5ba-6607cc81d95b | -6.80652 | -59.68816 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a799d08-c90a-3170-bed7-880208e8ffd3 | -6.1453 | -57.6994 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb345289-a49e-3b31-88a9-19e5e1327688 | -6.149 | -59.92826 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 018ff5fa-baea-3ec3-8f1e-76dd3a12d54b | -8.20596 | -54.96402 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29a33c05-6080-352e-af5f-d0b1f98a46ef | -3.2156 | -61.2427 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ae19eab-5be7-3904-bf0e-a26dead35ebb | -7.49506 | -55.37049 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a729c4e-93a4-3457-9fe1-5a12a24ef944 | -6.51046 | -55.22873 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46e84ab0-12be-36bf-a4c2-ff60494aa76f | -3.11007 | -61.2272 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ca5b3a4-a304-3a84-b3f4-952677c3dd08 | -7.52765 | -55.59081 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76f55336-a7cd-3e22-a2f8-33a1bf59214b | -6.30162 | -53.57247 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f916241-112e-3173-9742-b199b4fe0d1e | -6.65067 | -58.51246 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7a724caf-e719-31f2-bf3d-1c5700de14a6 | -6.00359 | -57.84954 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60745716-e5e2-3078-a4f6-260f8c99ae78 | -6.75264 | -56.33468 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e2bfdf-e7be-3541-9448-082d2fe6dc31 | -7.38822 | -55.15253 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cee7e5f-b1a5-3567-8da0-3153dd2fddac | -7.11066 | -56.55722 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4799fe58-2fea-3dcf-9184-57e16407345b | -6.77498 | -59.4404 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c7c022f-cc62-303f-8831-85b81b355919 | -6.9978 | -59.27289 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b35ea77-111b-3c23-930b-b260399b395d | -6.77831 | -59.44094 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a792dbe-c33e-3995-b940-38670e5b650a | -6.9834 | -59.25638 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931410c5-a315-3a28-a6f5-bfb9f0692f0f | -6.17768 | -53.47469 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6007cf3-bb0c-3f00-9235-1bdcbb54ab33 | -8.14152 | -47.5023 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec42b104-8ea8-305f-b2bd-0655077518d4 | -8.59894 | -54.74926 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1a97888-ff5f-322a-a97d-96a42673869d | -6.62791 | -58.49109 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 486766a2-96c1-3626-92b3-bee98cace242 | -7.03207 | -59.22853 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad206d3e-d8e7-3f76-bf4e-e9598257dca5 | -8.71454 | -49.60768 | 2026-08-26 05:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 440b221f-abca-3cb1-86dd-119b45ee2b90 | -6.64788 | -58.50845 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34c66e7e-4827-3ff9-a170-2757ff6dce33 | -6.15866 | -53.68668 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c383ea7a-2c39-38b5-b645-958da3974a1d | -6.73075 | -59.14547 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a700522-870a-3101-8128-be04d20dbb52 | -6.82541 | -58.65489 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 067819bf-8273-3c5c-8677-390a8c553fed | -7.54386 | -61.35292 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65310153-b46b-3179-a072-4a567fe2d464 | -6.11347 | -53.84816 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13244931-3da6-3d50-999d-abecd6bc50b3 | -6.13006 | -59.91797 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5104109-6789-327d-b737-03d1e5d0252d | -9.18305 | -49.9953 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdc10e3c-e5fa-3d9a-ab0d-a45e001ce542 | -6.7711 | -59.44342 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec365a15-9f5a-30d8-aea3-30fe052d8b1d | -6.61834 | -58.37843 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 197de447-beeb-3e6c-b8a3-e2c8930d8f84 | -5.79224 | -57.60846 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb8c70a-ed1b-3f9f-a0e5-cec9dbbaf534 | -6.68132 | -56.34839 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba62d691-449d-3913-8516-91bc35ff18c3 | -6.30059 | -53.57355 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45e52560-ed4f-3c60-8443-33b615753b56 | -3.1351 | -61.18555 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04d37ce1-c4db-3373-8ead-fd1556dddfb5 | -6.71516 | -56.34138 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f93d9b7-3947-3bcf-833c-5fe69c39bfa6 | -6.54021 | -58.31598 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e77c0c91-7d9f-338c-99d6-0ec24a479c1b | -6.62904 | -58.50558 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1939136d-162c-302f-be62-b0030076e706 | -3.59652 | -54.04531 | 2026-08-26 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 524c3118-a4ff-355b-8fa6-3d79319388cc | -6.27635 | -53.36229 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d28e354c-b5e5-3eb7-bf45-4c720e1a05c8 | -6.99558 | -59.26543 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97869320-b015-39ef-b785-3e193757bc81 | -6.96354 | -59.08627 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
