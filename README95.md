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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c23ae4b9-c0d6-376e-8755-c7f2c5edac65 | -11.0055 | -45.9527 | 2025-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 006b6cdf-8681-3359-b5ef-8f6320682713 | -6.1944 | -53.2585 | 2025-09-06 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| f06a06de-190f-3b6a-a89b-b3a341b9547c | -10.2187 | -50.5223 | 2025-09-06 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d709a28f-e614-37bc-8e14-4a6f3103f846 | -6.1945 | -53.2381 | 2025-09-06 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4ad5ed33-ca1a-30fc-84aa-f8047449e346 | -8.4415 | -45.0515 | 2025-09-06 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f11a20cd-bcd1-3911-ab49-8080dcf5b3a2 | -6.2038 | -43.3475 | 2025-09-06 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 32ef5b6e-d465-3080-849b-1cbdb2f9a8ce | -15.7186 | -53.5743 | 2025-09-06 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 219.8 |
| fccb0053-ffae-397e-a138-5a7c4c56b1a8 | -15.719 | -53.5532 | 2025-09-06 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7f198922-3ea9-3189-aa0b-3371aeff5ccf | -9.0596 | -62.3466 | 2025-09-06 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 2454977e-25da-3a52-9956-4935e1a7372f | -11.2302 | -46.1949 | 2025-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 373.5 |
| 7b4730c9-c295-3433-bf70-198ea82311f6 | -16.3345 | -52.9387 | 2025-09-06 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c9e9e79c-a4f7-3cd6-84ee-cbdfaa648cce | -9.6843 | -51.0819 | 2025-09-06 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 239e6a2e-480b-3e99-9c90-649a6b602b08 | -6.1944 | -53.2585 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| d63bb581-e240-3c39-814e-7f5ba5199abc | -10.314 | -46.4022 | 2025-09-06 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| bd4f0f86-91e0-309e-834e-faec40ac5786 | -5.753 | -45.5362 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| db54cdcc-c441-3f54-8adb-0eb8359d97fe | -15.7381 | -53.5717 | 2025-09-06 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4d26f3ff-f2ac-3ea5-a40f-40e80ad4473e | -13.0044 | -54.8282 | 2025-09-06 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| ab5e2e4e-9d06-3c23-a3d2-663fba49c619 | -10.3327 | -46.4225 | 2025-09-06 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9012795d-5bf6-31c7-a0d3-4efd63729e1e | -9.4497 | -62.3485 | 2025-09-06 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 80db2719-3d9e-35ae-8894-b9f0106f4aa3 | -8.1179 | -45.3125 | 2025-09-06 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 96b716fa-9479-328f-b0f6-7459ca9c93e9 | -9.9785 | -51.6436 | 2025-09-06 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 577429d4-1d6a-34e0-8cda-e9fd8f10e0bf | -9.0781 | -62.3458 | 2025-09-06 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 38be37b4-7859-343d-a920-79a2d1b9f779 | -10.6128 | -44.3284 | 2025-09-06 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 227f71b1-cbe4-36e1-ba84-9e8d66c5309d | -15.3064 | -52.7208 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 207.5 |
| a4bc41f9-b5d3-3c4e-ab7f-2b4a45e3250a | -6.2418 | -43.2976 | 2025-09-06 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| bf8d6d77-502c-30f3-8622-8562d9716d90 | -15.2873 | -52.7022 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 8def469c-eb11-38aa-b8ae-b17d783a2d31 | -8.0223 | -45.4354 | 2025-09-06 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 400.2 |
| a4889be5-e9e3-3565-8595-82748e456ec0 | -6.2127 | -42.4532 | 2025-09-06 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 36ecf9b5-6675-30ce-81df-289b1d05b33f | -15.0639 | -50.087 | 2025-09-06 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 4424f92c-05ac-3304-8875-298a7e2c8596 | -6.2672 | -53.4379 | 2025-09-06 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 75b84a3b-02f0-3e03-b2c1-4d076e2d5a29 | -12.8636 | -47.9877 | 2025-09-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d5c2ae8e-1ae3-375c-83ad-c4a228b11551 | -6.267 | -53.4582 | 2025-09-06 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d52c1121-75e1-32d3-b1db-5488052039af | -15.3067 | -52.6995 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 88d69b07-8e66-3040-9feb-c96b2fd74391 | -9.7031 | -51.0802 | 2025-09-06 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a409bbf7-efa5-306b-8821-85949a5c6381 | -5.7504 | -43.7091 | 2025-09-06 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f9b6f559-9087-3ed4-ada6-93dd3492ce43 | -7.8593 | -44.9053 | 2025-09-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| efe6154f-c4c5-32ef-b6ac-c0a56a4bb621 | -11.0242 | -45.9729 | 2025-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 523c4d36-be2b-3df7-9a17-89a00df895b6 | -15.6991 | -53.5769 | 2025-09-06 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e8d85e14-d692-31e0-812e-fd417824403c | -5.7183 | -45.2226 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8ca34afd-3058-3679-bec6-a5de821cc679 | -6.8841 | -44.7215 | 2025-09-06 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| abaf7a5a-69db-32fb-a2aa-7c2d74fd2ba2 | -6.2857 | -53.4369 | 2025-09-06 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f1f75c41-e2d1-3981-8411-4d3626b39421 | -7.0129 | -44.9613 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 180bf976-eafa-3b0b-8103-0e71d613d708 | -13.8006 | -52.7454 | 2025-09-06 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 367c4a4d-308b-3a33-9690-25d1ace5a7e6 | -6.5141 | -42.4028 | 2025-09-06 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 2cbb46f1-a7dd-318d-bec6-e7f5308f92c9 | -11.0245 | -45.9502 | 2025-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5006d7a3-6924-3653-a8dc-3f6cfda155e0 | -5.4579 | -42.8911 | 2025-09-06 14:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| fc015619-ffe6-3fb8-9a5b-94fe35ee630b | -4.4568 | -44.1413 | 2025-09-06 14:10:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 311.5 |
| 7e37737b-5dbf-3fbc-adc2-7b2486d40142 | -6.2421 | -43.2743 | 2025-09-06 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8cabbf92-69ef-3f5d-89f5-5aaa7dc066ef | -6.2296 | -42.641 | 2025-09-06 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| e9ec9151-1005-3df8-93de-361cd46718ba | -15.3258 | -52.7182 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0b7a7287-4aaa-39a3-989d-03129842d05d | -6.8281 | -52.8143 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c522a0f5-6f3f-38e5-beef-62ee61a4d248 | -7.6881 | -50.2991 | 2025-09-06 14:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d0d79168-c1ec-384a-9a97-3dc40df80978 | -9.4495 | -62.3675 | 2025-09-06 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8e707d35-f237-3076-9dbd-f03af45e8067 | -6.7419 | -51.975 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 17bff6a4-aa00-3e7a-bb4c-741f171d8e82 | -6.1679 | -43.1869 | 2025-09-06 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 68.5 |
| cdc13d28-3cbe-34a4-a506-72be7cb4e902 | -9.0951 | -47.0093 | 2025-09-06 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f7d4ddc9-5a26-3e96-97f7-37c705053edb | -6.1491 | -43.1885 | 2025-09-06 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 4274ace1-1d35-3093-a723-295f27858451 | -5.7298 | -43.9189 | 2025-09-06 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| bc448849-716e-3251-bb23-76c3b198e7bc | -10.2187 | -50.5223 | 2025-09-06 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| fec798bd-afc4-3718-925b-9588463bb756 | -15.7182 | -53.5954 | 2025-09-06 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 96e478a9-49ac-31fa-9cf5-b91f533bba1e | -16.924 | -45.7552 | 2025-09-06 14:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0947070d-bf7b-3d12-ad3d-c41fcb3d80fd | -13.0353 | -48.0521 | 2025-09-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6040e84c-2852-3dde-8463-1142f885f4a1 | -6.1945 | -53.2381 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ad33fc05-70bf-31a8-8fef-2c3dd60c9b33 | -11.2651 | -46.3938 | 2025-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2c7038bd-2199-3f41-9ce7-eb761647208d | -13.8407 | -46.2598 | 2025-09-06 14:10:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4664bf7f-2bfc-3834-8e5d-f2f8aef34752 | -7.3838 | -50.9116 | 2025-09-06 14:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 8f544f1e-a2c3-3471-a526-699f1d434fb4 | -6.6954 | -44.829 | 2025-09-06 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3df9c647-7a81-36f9-891f-1d2e5748d268 | -5.5695 | -45.1425 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6695485d-4056-36a8-9381-6ee91a5bb311 | -11.3567 | -50.3161 | 2025-09-06 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d4932c32-011c-3398-96d7-d14634c28998 | -8.099 | -45.3144 | 2025-09-06 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 1504b67b-1dad-3307-81a9-00dfbfc12bb9 | -16.307 | -58.1055 | 2025-09-06 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 236.4 |
| a306098d-7cb6-3bda-8513-416d5dac2080 | -6.8095 | -52.8154 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5cf20fa1-53d6-334b-9fba-e244ee515092 | -5.73 | -43.8958 | 2025-09-06 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 1ec42bd5-cb99-3363-8f71-f93e54bc2d15 | -8.0226 | -45.4127 | 2025-09-06 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 0509ed70-8a8c-3da6-ad4e-a4c5ded09732 | -15.7186 | -53.5743 | 2025-09-06 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 2ca84a36-9d75-3288-bfd0-2bc1539056bf | -6.8844 | -44.6987 | 2025-09-06 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6c09cf12-c276-3535-9721-291158c6ad38 | -6.4021 | -46.0944 | 2025-09-06 14:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 17094060-ee9a-34b5-8af5-b2e7103e6123 | -5.5697 | -45.1198 | 2025-09-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d39e3fc3-23ad-3267-9a54-dbc18533628b | -10.7872 | -47.7501 | 2025-09-06 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 03153048-43ec-3d36-9749-c3fcc31089bd | -6.8465 | -52.8337 | 2025-09-06 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b889255c-1e14-3816-b0a3-d0cdff695049 | -11.2306 | -46.1722 | 2025-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7e556446-b5ed-3d20-a0f7-c122e0268d70 | -5.8877 | -45.0972 | 2025-09-06 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a6d191c9-8652-3018-9547-372503df3334 | -6.5138 | -42.4266 | 2025-09-06 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 5a2941a3-2f5f-304e-82bb-0a043233eab6 | -6.8281 | -52.8143 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ea76032a-8a9f-3659-9518-9ae811c9a6a2 | -6.1502 | -45.0322 | 2025-09-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c4f04007-efab-380c-aeb7-28672dc1a86e | -9.0951 | -47.0093 | 2025-09-06 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 472a72cb-7d58-3577-96d6-73f58a88f44e | -11.319 | -50.2989 | 2025-09-06 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 3b7b188c-0010-3326-a3a9-5e9b885d51c0 | -11.3 | -50.301 | 2025-09-06 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 0862007c-ee21-3219-90f2-655e1fd6a54a | -11.0242 | -45.9729 | 2025-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 57fd2a19-947e-3250-a0bb-5ac73c1f9a8b | -7.9252 | -63.2608 | 2025-09-06 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 81627945-9e4d-368c-8548-72d4d6c3eb12 | -6.9942 | -44.9629 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a812b863-45a9-3e36-8139-8cf865bb8db6 | -11.3193 | -50.2775 | 2025-09-06 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0944ea42-21cf-3ae3-937e-1d4586ee3684 | -5.8485 | -45.3038 | 2025-09-06 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 72774212-990e-3c8f-927b-c04aa08aa36e | -15.7377 | -53.5928 | 2025-09-06 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 43484897-b5e9-3002-a859-f1d5cc288260 | -6.8095 | -52.8154 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d7dc109c-82bc-30ec-85f3-de9df7176165 | -15.6991 | -53.5769 | 2025-09-06 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| dbce8ea4-0b71-3676-b46a-21bddd90c10d | -7.6505 | -46.7268 | 2025-09-06 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a9f4c990-26f6-3f52-abbe-4e1a199e5a39 | -9.0596 | -62.3466 | 2025-09-06 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 7226585b-9330-3aa7-afc7-1463339b7304 | -15.3064 | -52.7208 | 2025-09-06 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 294fa419-58ee-3296-b59f-09ff40b63894 | -15.7186 | -53.5743 | 2025-09-06 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 349.9 |


[Clique aqui para ver as próximas entradas](README96.md)
