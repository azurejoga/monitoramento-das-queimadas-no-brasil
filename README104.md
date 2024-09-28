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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 878f1931-c600-3970-a176-aec67ad81eeb | -15.79826 | -47.54153 | 2024-09-28 12:51:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 05606f9c-fb58-3e00-b1d0-4c48b2d79559 | -15.78998 | -47.52895 | 2024-09-28 12:51:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 73154917-8b25-35d6-b0e4-8458974859e6 | -15.6452 | -47.23122 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| abf6f365-e649-343e-9f88-a0bfe0ebce96 | -15.48702 | -48.02851 | 2024-09-28 12:51:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8cd98153-bcb0-3d9f-969f-b1f07792328f | -15.4856 | -48.03896 | 2024-09-28 12:51:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 81752105-c122-3dbd-bfeb-af29e2a7c163 | -15.44208 | -47.45796 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 90d04b90-f39f-39dc-aeeb-838c932ab004 | -15.43384 | -47.44503 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1c2d256c-6d73-34b9-b296-cf80097ea8cb | -15.43233 | -47.45658 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 455.5 |
| 8e8a746a-5f30-3c6a-a771-bb2d1269f7f6 | -15.43087 | -47.46771 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 23237f0d-397b-3037-9fe7-77e2d765149c | -15.42407 | -47.44384 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 42d93948-be73-310c-92fd-f6df8648f91b | -15.42258 | -47.45528 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 201.0 |
| c8354821-1dcf-3130-9223-7add819bd5a8 | -15.4143 | -47.44263 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e50b1444-2b83-3560-b781-221bdc770c44 | -15.40526 | -47.58762 | 2024-09-28 12:51:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1fec0937-6b65-33a2-ae8e-bbe83108808d | -15.40383 | -47.59854 | 2024-09-28 12:51:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 313badad-ea94-37f1-834a-7a0750109f21 | -15.36136 | -47.44995 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b70b7aa-1fdb-3ee9-9d39-5e8d301a2307 | -8.87424 | -47.99618 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d0098457-bb79-3639-9ba0-0be728dd6edd | -9.55691 | -47.92651 | 2024-09-28 12:51:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5b2751db-4477-3acf-bf3d-12fd09862109 | -9.7267 | -48.02874 | 2024-09-28 12:51:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6928d523-38a3-3fe5-8a29-b6bec3ca9f02 | -10.70081 | -48.5615 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f3406687-b503-3e96-85e3-3001afb5cb6a | -10.55108 | -48.05897 | 2024-09-28 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 33aca995-252f-3956-a733-3b79a4eb79e4 | -10.54978 | -48.06824 | 2024-09-28 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 90f0cc1c-57cf-34c4-ad7e-c2e7963cfd1d | -10.54331 | -48.04869 | 2024-09-28 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 55126340-a506-3595-ae15-eb6b88aca4bf | -10.43055 | -48.19671 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0284d999-b1d8-35c3-97d0-2b2ac3bd595c | -10.42929 | -48.20567 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9594e808-ae6d-3af8-80d6-0c0d72d6a18b | -10.42286 | -48.18616 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 7191698f-ef15-3af2-b609-ba614cd230bc | -10.42158 | -48.19521 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1e0f4b5f-0bbe-37fb-a432-5e97f76e49c8 | -10.4203 | -48.20433 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 876a99d1-1493-3c5b-bdb9-18cd831cb064 | -10.24948 | -47.78146 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 424ac146-b907-377e-8bd0-c45b39710ae0 | -10.23388 | -47.76028 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b34b7ddb-be70-3443-a332-12e4ef2f27ea | -10.23258 | -47.76963 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3511a563-3d30-3cc9-a113-305993a67668 | -10.22216 | -47.77774 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a976da80-3d1e-3af4-a5c5-20c81eb9bfc9 | -11.72564 | -47.82317 | 2024-09-28 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e009d47c-ee56-39e2-add4-fe166dc5cde6 | -11.72428 | -47.83291 | 2024-09-28 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 5b5b4580-1de8-36a1-8c7c-d15e667c4cbd | -11.71644 | -47.8219 | 2024-09-28 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d75bd4c6-f498-3571-beb4-135050c65c1c | -11.71509 | -47.83162 | 2024-09-28 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d4670eff-a66a-3ece-92c1-2965c866ba64 | -11.66778 | -47.83498 | 2024-09-28 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6caca912-0a5d-3f05-8c3b-b0f82e241c5c | -11.65979 | -47.83739 | 2024-09-28 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7bbc1c63-d0a2-3238-a759-c1d68d93c239 | -11.58529 | -48.43076 | 2024-09-28 12:51:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b7a48cf9-9815-3ff7-a731-9b3cc4655a0a | -13.45879 | -48.59196 | 2024-09-28 12:51:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2fc40491-4b81-3628-98f4-0628a4336d1e | -13.17515 | -48.5137 | 2024-09-28 12:51:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0221e852-db9d-3d80-9008-59cc357eddfa | -13.16606 | -48.51262 | 2024-09-28 12:51:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6e945065-a421-3abf-b9c7-0296d5f83082 | -13.03249 | -48.61226 | 2024-09-28 12:51:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3a354460-a8b0-3b61-a322-60fed6d8b43e | -13.02453 | -48.60447 | 2024-09-28 12:51:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b9f73783-cd94-3dd7-8ad1-885187bd3d0a | -12.47911 | -48.02349 | 2024-09-28 12:51:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5920b0b8-6e0b-3f31-87dc-9534f2715168 | -12.47778 | -48.03317 | 2024-09-28 12:51:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5a9b2df5-6625-3373-8131-bdd13366d211 | -13.94252 | -49.08049 | 2024-09-28 12:51:00 | TERRA_M-T | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7e890538-b18f-38bd-9115-199fa5eeee96 | -15.20385 | -48.68354 | 2024-09-28 12:51:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 65753276-a852-3c7d-a1d4-1361c3858afd | -8.61336 | -49.48643 | 2024-09-28 12:51:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 419d2a95-1309-3870-809a-24d119462b93 | -8.97846 | -49.82365 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f2991251-6941-3abd-acc3-ad3fd5d1788d | -8.9695 | -49.82234 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cad8f76e-d727-3921-8eb1-dec8cb5dc8cb | -8.9449 | -49.29651 | 2024-09-28 12:51:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 689cb054-1171-31c4-b169-4852e2dbd51a | -8.9436 | -49.30547 | 2024-09-28 12:51:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e05b6608-86bb-3b38-be49-2c719eea3737 | -8.75488 | -49.77854 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| efe49520-a0bc-39ad-803e-725899b33aaf | -8.72921 | -49.95259 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 98230d98-8960-3925-846c-66cbae82652f | -8.61468 | -49.47742 | 2024-09-28 12:51:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0d832217-465b-3e86-9eb9-75724e600e1e | -9.38355 | -50.01714 | 2024-09-28 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| df75c95b-123b-3319-9280-48b624f00f1f | -9.36693 | -50.00534 | 2024-09-28 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 89d55cf7-ed6d-32ef-9cf4-7a89d9689b48 | -10.76286 | -49.85713 | 2024-09-28 12:51:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7f33a87c-8811-34ff-8562-3e60eed37186 | -9.77199 | -50.071 | 2024-09-28 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 79d92aea-d1e9-3013-a687-accdd075e29f | -9.56943 | -50.13214 | 2024-09-28 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 2c16c6f1-3db5-37c5-a2a1-4a7d4d6067f0 | -9.39254 | -50.01846 | 2024-09-28 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 954dbba0-6c4e-372c-96ec-6af0ba3f71e9 | -9.36557 | -50.01451 | 2024-09-28 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 833925c7-5c76-3c46-b72e-f436062e75ae | -10.95419 | -50.12046 | 2024-09-28 12:51:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 2a0905fe-2e15-31fd-a382-01fb4eb86dd4 | -10.95285 | -50.12959 | 2024-09-28 12:51:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dbe62afa-365b-3053-a76f-ced531cdc145 | -12.81679 | -51.11721 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8231825c-2e9a-3868-b665-ef4ed03bf820 | -12.52999 | -50.62719 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5df9108d-2b58-35a7-b0bd-d7f62847de6e | -12.52863 | -50.63644 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 361fef43-52ba-31dd-94b8-33e34ac65166 | -12.30366 | -50.47716 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| ab2025e5-919b-3662-91db-9a8591feb11f | -12.30229 | -50.48636 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 6239d766-2ed7-349f-a48b-6627e002aa32 | -12.30092 | -50.49556 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 85844c00-e10e-3e58-bfdb-9c863f01de67 | -12.29489 | -50.46976 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f6aca26c-e9f8-3b3e-87e2-173a8ec420d8 | -12.29353 | -50.47896 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 2dca8de4-236d-3a2c-935c-27edcd824702 | -12.29218 | -50.48816 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| dfbef68a-b6a8-359c-b4ba-00da839b23c4 | -8.38789 | -50.81379 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7fd698c0-c0cd-3476-a3c6-5efb872a226a | -9.29957 | -50.77501 | 2024-09-28 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 579eb508-b109-3c4d-a2ae-089aac9be762 | -8.38939 | -50.80391 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0a92e5fc-4695-301b-a4c8-8301c71e5cdb | -10.8467 | -51.15033 | 2024-09-28 12:51:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1c022ee0-af65-34f0-9b18-495ef135cca1 | -10.60681 | -51.09496 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9dd9a28b-f698-364e-9609-8c4a8418ba7a | -10.49786 | -51.14245 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cdb0282f-c6d6-312e-8b19-b023c59315fa | -10.45673 | -50.80239 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 939dc728-5859-3e37-8966-e6116e9bbf45 | -13.2515 | -51.29339 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 068feb4e-5f26-3115-9aea-7dd9057ead63 | -13.25006 | -51.30297 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 268d7908-217f-304f-8f22-ec9a124aab3c | -13.22993 | -51.25096 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6c661acd-834a-3fdc-bbda-d775935e702d | -13.22849 | -51.2605 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7597ff0f-2f6f-339a-b58e-44b13fd0e5c2 | -13.21317 | -51.23864 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 27827644-b077-31d0-8875-2908b60a9132 | -13.20408 | -51.23724 | 2024-09-28 12:51:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 3434d567-8c28-379a-86f2-1acafc855a29 | -8.9937 | -52.14141 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8d5791e3-d417-3b41-83ab-e0062c7e6937 | -8.89862 | -53.01525 | 2024-09-28 12:51:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d5ed51c5-ec24-397b-9fa3-dbca70ff50f3 | -8.67592 | -53.18837 | 2024-09-28 12:51:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0805e899-52aa-39df-9fbf-15c496db176f | -10.03461 | -53.48249 | 2024-09-28 12:51:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4480679a-5036-34be-8e0a-cae1d2342868 | -10.02598 | -53.467 | 2024-09-28 12:51:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| b740afcc-88cd-384a-9194-3326655234da | -10.02381 | -53.48069 | 2024-09-28 12:51:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| e8004f95-9b14-3aaa-96a4-3c599ffe6c2c | -11.41112 | -52.87383 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b738c938-1636-3971-a735-2aff784b36ee | -11.21214 | -53.82462 | 2024-09-28 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| cdceb271-c28c-3411-a3b3-1481c41eee54 | -11.07261 | -52.48471 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e1c5fec4-0021-3a06-abd5-5d3455843a00 | -11.07092 | -52.48992 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 47404c7e-9f5a-3897-a519-4f0381a1343b | -11.0708 | -52.49615 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 25d0d95f-22c4-3bee-a79f-9ae018f9c3ea | -12.77611 | -54.0099 | 2024-09-28 12:51:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a31ecdf9-ed58-395e-bdd9-1ad2fd397c31 | -12.77324 | -54.00283 | 2024-09-28 12:51:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 09d69168-27d5-376a-b60a-310999a17f5c | -12.77111 | -54.0164 | 2024-09-28 12:51:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |


[Clique aqui para ver as próximas entradas](README105.md)
