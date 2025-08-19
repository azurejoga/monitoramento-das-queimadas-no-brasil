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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e7bc108-a320-3c5e-b77a-34190639b0d7 | -6.93865 | -43.62396 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e63d6dd2-7b85-3c1f-a404-11781008ce9f | -4.92223 | -43.24894 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bb8ff0f-280c-33d6-bbed-0eddffae16ac | -3.13253 | -48.98661 | 2025-08-19 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 26fbe74a-2d75-3612-9634-64e03188a4c3 | -6.06414 | -44.12901 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c28affbe-a00f-3bdc-b681-c22afd18e741 | -6.86303 | -43.12142 | 2025-08-19 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d591356-3434-3580-8f75-4bd1083fc310 | -5.97191 | -44.13271 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a763f8cb-bb46-39f5-a936-bdfc61263937 | -6.55916 | -43.00884 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4b56979-5c94-3feb-adf8-8b7a9391e34c | -6.96581 | -43.58448 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6e195308-4da6-33ee-885e-2ee70159d38a | -6.94001 | -43.61413 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5453a643-0644-348a-9fe8-7a246e51625a | -5.97655 | -44.13638 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c99989d8-11fc-3001-9455-250fdbffc474 | -3.98684 | -42.5248 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1277553d-b34c-32b2-b84e-0f880070c128 | -6.94622 | -43.60841 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f84af763-0263-3fb3-9dec-28ba8b4130e7 | -5.64324 | -43.40034 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6f85c7e-2eee-317a-b96b-0c9cd1ab9c07 | -5.75128 | -46.67902 | 2025-08-19 04:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ae81e5a-554b-32a3-8080-4af908c8c5dd | -3.74207 | -48.92953 | 2025-08-19 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 225c6371-da13-31db-94d1-dce5bfeef224 | -5.66139 | -43.37618 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d411544c-aed0-3f49-8df1-2c1050b34e9d | -5.87924 | -48.1214 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0555f8a9-ee72-327f-b2da-1b02ad8304e9 | -5.98143 | -44.10154 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0497c29d-e0bf-370c-a2d1-b5527ce08f16 | -4.91741 | -43.24496 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c7d6188-c4dc-316a-8300-bf8e5443257a | -4.13145 | -50.24067 | 2025-08-19 04:51:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b15b5c21-17b3-3081-8776-28f0e9eee714 | -6.95244 | -43.60257 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db5e6136-770d-3885-b13f-69937853162b | -5.64679 | -43.40349 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ed62af1-7b2f-3157-aae2-a324167d3b18 | -6.94227 | -43.59791 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 924638c3-a98a-3f24-93a6-488dd73159c0 | -6.93472 | -43.61333 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63c0f6af-e236-33c8-a441-2cfe3426bd9c | -5.88237 | -48.12672 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5699bce-bacf-3efd-a6bf-a07afda605be | -6.93256 | -43.58979 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5159f4d6-6587-3776-9001-7ed460f0cab9 | -3.46824 | -47.68655 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fd3e416-b5eb-3125-b5bf-82916b7ac7bc | -4.91798 | -43.24508 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7f862c6-f149-3622-9c7d-bb2be589f97c | -5.87157 | -48.12011 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3edbe5f6-0196-3311-86f3-344fdba1fc46 | -6.45153 | -44.56328 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f5bcd5c-993c-3397-81b8-174aaf91ea9f | -6.94668 | -43.60506 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9f9eb04-6b59-397a-bb21-11bb1e8d5d1d | -6.95059 | -43.61584 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28943dbf-de02-3c6d-be4b-99b59ebf8700 | -6.16295 | -47.27828 | 2025-08-19 04:51:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4be572f-ee7d-35f1-bf99-8aec5f7520da | -6.74939 | -41.54256 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10239830-ca9a-331d-8ffe-d8a4eeae06a1 | -6.05709 | -43.74897 | 2025-08-19 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbde2d04-bf0b-3916-a54d-501d65698e1f | -3.12897 | -48.98608 | 2025-08-19 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af41a3fe-7e61-30fd-9c56-ef803758aa69 | -6.96628 | -43.5811 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 521961b2-21af-36d4-a94a-8630b05ec991 | -5.98152 | -44.28263 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96e40564-357f-3a2f-9f01-c99bb45d7750 | -6.37426 | -43.3208 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b928cdfd-3176-30bb-b4cb-583fc23d96ca | -6.75028 | -41.53945 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17d8881f-cd11-3461-9a5c-d7cd5d62b3c3 | -3.89829 | -53.48959 | 2025-08-19 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 393177d1-fef3-3808-a0a7-c25a4c6431c1 | -6.9388 | -43.58386 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe25fcab-6075-30c7-8649-8a291a408b84 | -3.25663 | -43.27657 | 2025-08-19 04:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5d47196-346f-3d98-9ab8-4e9d31868d68 | -3.47134 | -47.69184 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a99a996-0c49-32e9-ba88-d43d1184715d | -3.48182 | -48.43941 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7bd214fb-3267-3379-8ae8-94c9c35d055b | -6.93382 | -43.61985 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69053a48-a83c-364e-a232-b02f3888376c | -4.59273 | -43.31157 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df10c4bf-fdfb-3eef-b873-486c05061200 | -6.97018 | -43.59192 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f3c9735c-750f-3f63-b205-76b814595576 | -6.54777 | -43.98336 | 2025-08-19 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbd9eb28-4666-30f9-89c9-e60e04c0cf08 | -6.67544 | -43.67442 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 897ffcf2-abdb-34d3-b2b6-5da591f163a2 | -4.39099 | -47.77013 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bf59816-1066-3983-ad79-a957215459c3 | -3.58612 | -49.43388 | 2025-08-19 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ef65735-6453-3867-aab0-f5cfe294298f | -6.63297 | -55.27336 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c77f9984-03d6-377e-aedd-28ab61331f78 | -8.97333 | -60.49787 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea846701-0ba3-3e43-8893-0623ff15cd89 | -9.52824 | -63.58004 | 2025-08-19 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70c539ed-02a4-3cfe-8199-730549e88e63 | -11.85278 | -51.57912 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1fc37e3-cfc7-3067-8986-75891c802ed9 | -12.04178 | -44.01665 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 575aac71-4694-36df-9790-ba374c07e016 | -6.49122 | -53.39309 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df388b62-c98b-317c-92fe-bd5cd6be8f37 | -6.41875 | -53.37429 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 619b2b77-278c-348b-88ed-f1840c00f8d7 | -10.58225 | -49.13751 | 2025-08-19 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 885ae10f-bd58-3069-8125-e4c0518cc54f | -11.85509 | -51.58729 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10d3d8d7-b1e8-355a-9e7c-04607965cd7e | -10.82926 | -45.04073 | 2025-08-19 04:53:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29de21c9-60f0-3800-bd08-c1546e139852 | -10.49945 | -54.63068 | 2025-08-19 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 491699b3-f8a6-3c12-af67-f005fff47535 | -9.8548 | -44.68587 | 2025-08-19 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d06fb00-9e46-37b2-af00-b256d415d77b | -11.77571 | -51.73893 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2185a9a1-a81a-314b-9bbe-d57db306839f | -10.10935 | -57.76622 | 2025-08-19 04:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1041a21-5219-3eb6-b55b-504ececaa4f2 | -8.23188 | -47.30332 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8137326c-cde4-36ac-a9e2-394d02fb9f85 | -7.27068 | -50.16687 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb274861-569a-3bfa-8cfc-be1ef5765b36 | -7.15336 | -44.19595 | 2025-08-19 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2c5e08d-73bb-3669-b554-fe1f3da5e7b8 | -12.50106 | -45.56851 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 935dacbf-5eee-38fc-a6c1-1c1a73013afc | -11.57828 | -44.85635 | 2025-08-19 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d1a71cc-91a0-3851-aba2-d22ede0d060b | -12.63138 | -46.88574 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f7ad04d-5f57-3f43-8007-337ce990989a | -9.8188 | -49.22642 | 2025-08-19 04:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37d6a08d-2503-304e-9295-3d78add87c8c | -12.50236 | -45.56233 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 351268d7-e5b0-34a2-99a9-8c3ea7185dbe | -9.3403 | -48.51764 | 2025-08-19 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b08d59b4-17f8-3adf-92f7-d1e90559da98 | -12.99211 | -45.20501 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 483cdd9b-0f1f-31d3-91fd-18a85bb910f8 | -10.5034 | -54.62762 | 2025-08-19 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 689b5316-d57c-3cd1-aab2-b452a387f7d2 | -8.23848 | -47.86043 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbb3e22a-c97b-3cba-847b-c44fbcb54b7d | -8.81923 | -52.03356 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47541262-4d10-34d3-ae7e-ff9786b525e2 | -8.62218 | -62.623 | 2025-08-19 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ab30508-07ff-3ce5-98ac-bfa2060d7ffa | -7.76107 | -49.85267 | 2025-08-19 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91129e3a-2ead-38d6-af8c-acfaa36e70cf | -12.651 | -45.82367 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb741fbe-ef63-37ec-83e2-17d82659ae28 | -7.28846 | -43.68263 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6b11e8a-896f-359c-9c2e-97930f72344c | -8.81868 | -52.03717 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ac3744a-2611-3109-bf98-9f088d5a410c | -9.51563 | -60.51715 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0ee964e-82f1-34c5-bbb7-fb77eae4679d | -9.17543 | -59.64213 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 337b3a78-4cea-398b-8ee5-f1366f147083 | -9.17489 | -59.6193 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9459028c-4063-30df-93b3-70a798162c08 | -9.89015 | -64.26591 | 2025-08-19 04:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96513cf8-4405-3695-9fa7-bbe2ff6b1231 | -12.50178 | -45.56273 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 80eeb33f-6151-392d-8886-ae37619cfd14 | -12.99289 | -45.1987 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d56b0d73-b030-38e3-bdb8-8cb78476dcdb | -10.45748 | -48.81059 | 2025-08-19 04:53:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2767de2d-d180-3632-838b-20d370fd96d2 | -9.17044 | -59.61854 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f483e947-0790-3507-b642-7b4a8b2ececf | -9.05146 | -50.17943 | 2025-08-19 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15efb4e9-1b18-3eb1-a6b5-2aac63825b51 | -8.82483 | -52.04179 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce57954e-1b5a-383a-8e9f-988fd1b1f857 | -7.58365 | -45.43483 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20a16fb7-8192-31cf-8a6f-1d26e18f9d59 | -9.18807 | -59.64858 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32854782-85b7-3b8e-8ac5-7386d6c3ae8b | -12.73262 | -45.06254 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a22f06d-bae8-3249-a68e-6f52f425c6d5 | -9.20006 | -59.63262 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0abffdc5-d869-3f65-8bb8-0fd7c539bc08 | -7.21779 | -49.60871 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d798b6c-287a-32ce-b9b1-5b5224bd391c | -12.92947 | -46.10889 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
