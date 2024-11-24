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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 589f92c8-b116-338d-b1d2-2bae366f6f78 | -3.5083 | -50.539001 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13feeb4e-b5a0-3910-9126-2eb928a5aec6 | -2.9992 | -52.5005 | 2024-11-24 00:25:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f104cf-4398-330c-a80b-7e41f5713f15 | -1.3619 | -53.8181 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babdff6c-2cf6-37ce-af7d-c16d082aef4f | -4.0883 | -47.031101 | 2024-11-24 00:25:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07425e18-a753-3b75-9984-d0ceb4e870c7 | -3.8445 | -46.007999 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4cc2f70-e0ad-347a-b445-e3e461247af1 | -2.5411 | -46.391899 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f89e5f9-323e-325d-ba85-f767a26d888a | -5.9488 | -48.055801 | 2024-11-24 00:25:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40bdd06d-58a5-3954-a11e-45b262db6b90 | -3.0515 | -45.065701 | 2024-11-24 00:25:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d522dca-d1aa-34f7-ae5f-dbc933b7e9af | -0.1887 | -51.484699 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc0edce-4caf-3ea6-9433-7a67eae63865 | -4.6258 | -46.043701 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffa18e2c-68c5-3df6-b70e-a7b11a26a43a | -1.6356 | -53.297199 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2a4fdbc-2c8f-396d-9fff-dd7586e44491 | -3.1912 | -48.576698 | 2024-11-24 00:25:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 249b708e-9bb6-31df-9a34-9dc31040c01a | -4.4098 | -44.0797 | 2024-11-24 00:25:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09b570f7-2450-3756-802b-e8775f357acd | -3.5931 | -49.354698 | 2024-11-24 00:25:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65bad50a-5938-30e9-8306-45d98ab37c03 | -5.1185 | -43.1497 | 2024-11-24 00:30:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| feabdbae-4575-3c20-8a13-703e76bca0a5 | -3.2604 | -53.2746 | 2024-11-24 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 287da423-2331-3c19-831e-da59279ecbf3 | -2.7596 | -49.1157 | 2024-11-24 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 966cc30d-ac0b-3eab-923f-790e7b8c941e | -0.8907 | -52.7685 | 2024-11-24 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 15f4b7dc-05dc-31fa-b8d8-ecbc28e908f0 | -3.8304 | -46.0057 | 2024-11-24 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 8f0aa335-dfe5-3a0a-bfc6-a6b3840a0ac2 | -5.0998 | -43.151 | 2024-11-24 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8b2796ef-ddbf-3f38-b039-7774f9bead86 | -2.6963 | -46.2719 | 2024-11-24 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b4d6366a-2acb-3ff8-9d38-2f9fea78663d | -1.4732 | -46.0357 | 2024-11-24 00:30:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7452a8d2-9c3f-30e2-9a30-45f5cfaf0caa | -1.6042 | -54.415 | 2024-11-24 00:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 90c3000f-4425-3877-b84e-578ae1f7d677 | -1.8053 | -46.649 | 2024-11-24 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| f1b160cf-b516-393c-bc0f-5bfa11352d14 | -2.9229 | -45.3712 | 2024-11-24 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 190.1 |
| cd520fce-6e62-39fb-a4eb-a54409c926e3 | -5.9557 | -48.0425 | 2024-11-24 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0826531b-f1f4-3bfe-b573-9f94ea215adc | -3.242 | -53.2751 | 2024-11-24 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7ee9a944-0ccc-3f63-9f71-1c5a9dd814e7 | -3.2569 | -54.2226 | 2024-11-24 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2f0358d2-95d5-3fd0-b64b-f071391e3138 | -3.0582 | -53.2192 | 2024-11-24 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a43db477-9288-350e-8a27-60084057cbec | -2.8606 | -51.8143 | 2024-11-24 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e290279c-c6c5-3d14-94cf-d39da18b45cb | -2.9043 | -45.3719 | 2024-11-24 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 39c203c1-1c76-39ce-a0b1-38ebe408bd16 | -2.741 | -49.1375 | 2024-11-24 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d39b482b-1fb3-3357-a63e-e210202745dc | -2.7149 | -46.2713 | 2024-11-24 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| cf52e9ad-7188-3122-984f-03f8640d7dcf | -1.8053 | -46.6269 | 2024-11-24 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 218.3 |
| 5d1f09a4-10bb-3a38-a0fe-eee5b3711fbd | -3.8489 | -46.0271 | 2024-11-24 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c2960cf6-3903-3b47-9cfc-8f6434862f0f | -1.8238 | -46.6486 | 2024-11-24 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 288.3 |
| 397f0c9d-8a5d-3698-bfa4-0810042bbbbc | -2.7411 | -49.1162 | 2024-11-24 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 6fbde482-16db-3563-a412-146f6cdce7ad | -2.923 | -45.3487 | 2024-11-24 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 9a7cd3f6-356f-3047-a53c-e078ea48721c | -0.8724 | -52.7483 | 2024-11-24 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c1204c13-ef70-3c63-a641-747c15d68a83 | -1.5129 | -54.1759 | 2024-11-24 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 35e5732e-f5ad-3181-a27b-2b4de489bcdc | -4.5403 | -42.9066 | 2024-11-24 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f0ff40ea-3e78-3dd6-b1cb-c943bfc7ff00 | -1.8424 | -46.6261 | 2024-11-24 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 7d208e7d-c396-3f6b-b410-a5d28c391490 | -3.2386 | -54.223 | 2024-11-24 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6a7478cd-6151-33f4-9eb4-fa278e994f00 | -3.8303 | -46.028 | 2024-11-24 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 22ed37fd-8f9c-38af-9fed-ca353e900645 | -4.242 | -48.6978 | 2024-11-24 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 033d1bd6-210d-3ae0-bb94-5401b484eeee | -1.3667 | -53.8161 | 2024-11-24 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bc83df18-15c0-3452-9905-815a87b3b62f | -1.3666 | -53.8362 | 2024-11-24 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| ab973e9b-27a3-3dc9-9e42-ef51dd7533f4 | -0.8907 | -52.7481 | 2024-11-24 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5c201e56-766b-3c7c-8730-7916b9466246 | -2.4456 | -49.0816 | 2024-11-24 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e607d536-d290-369f-9fde-96d5609ccb8e | -1.385 | -53.836 | 2024-11-24 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| dd5de9b0-f791-37cf-8fd5-de1678ffbee0 | -3.849 | -46.0048 | 2024-11-24 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 9ad204a3-37ab-3867-b7f6-94d5b1d4b952 | -5.9556 | -48.0642 | 2024-11-24 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 00031910-ba06-36f8-aca9-3449a79ade0c | -2.9044 | -45.3494 | 2024-11-24 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b645388d-ea24-377f-897d-ac7e66d6e6af | -3.2212 | -53.922 | 2024-11-24 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f6b8d433-acc7-3c60-834f-194ff9771a13 | -2.7148 | -46.2935 | 2024-11-24 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1e5fc365-52ee-3800-bc98-8742868dc1b3 | -1.8239 | -46.6265 | 2024-11-24 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 301.4 |
| 80b2a4f3-4e35-33d7-85a4-b3602fef753e | -2.464 | -49.0811 | 2024-11-24 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4855bc54-a49a-3969-bbd9-7898b76e036a | -1.8423 | -46.6482 | 2024-11-24 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 538575e9-d9f2-365e-9b2f-217680878712 | -3.1068 | -45.7903 | 2024-11-24 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 1ee36ef7-9100-3ab3-b8b5-ab78c327deb8 | -0.8723 | -52.7686 | 2024-11-24 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 8ab86bde-1089-3d34-bf07-ca6c730182dc | -3.5995 | -47.5142 | 2024-11-24 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1c86ec61-7a8d-365f-a03e-2495f30624e7 | -1.5129 | -54.1959 | 2024-11-24 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 5e276cda-c3cf-33c6-84ad-f0d91cd6650d | -5.9557 | -48.0425 | 2024-11-24 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6c4727fd-0253-34c2-924d-47447bb73972 | -3.8303 | -46.028 | 2024-11-24 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| cccf2644-42a8-3db1-afca-114dac15d4c5 | -2.9044 | -45.3494 | 2024-11-24 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 144.0 |
| a9a13f0e-816d-33b5-8f52-a5533a4cf9fb | -1.5129 | -54.1759 | 2024-11-24 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5fc2f838-b9b3-3711-b4c2-7b4f14ea0cc1 | -0.8723 | -52.7686 | 2024-11-24 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 45dd57d7-346f-38d7-a85d-c12a26b49a5f | -3.849 | -46.0048 | 2024-11-24 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 3954b1fc-177d-36bc-98c3-4ef66c010618 | -5.1185 | -43.1497 | 2024-11-24 00:40:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e706e288-18ac-3a58-97ba-4cf90d93a535 | -3.1068 | -45.7903 | 2024-11-24 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ac5b1a33-590a-3796-a38a-8e84f6911240 | -4.5403 | -42.9066 | 2024-11-24 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2aa6e069-020f-3b35-aff7-cead8ff94e90 | -3.2386 | -54.223 | 2024-11-24 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1b1e7153-782e-3083-b9b3-517d1c1dfcd9 | -2.9229 | -45.3712 | 2024-11-24 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 342.7 |
| 05fe6fe9-6a15-379b-b9b5-f880e1b57f33 | -1.4732 | -46.0357 | 2024-11-24 00:40:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 06797d9e-e083-3fd7-90d2-a5a655f34475 | -2.923 | -45.3487 | 2024-11-24 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 58eeff2e-0904-31ea-9c7f-b484a2ec88f2 | -3.8489 | -46.0271 | 2024-11-24 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| bfeea4a6-6466-3c82-af3b-04ba5f40522d | -2.8606 | -51.8143 | 2024-11-24 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 95769453-c70f-3b27-94b4-045f03f39603 | -1.6042 | -54.415 | 2024-11-24 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b3fd7953-a8f9-34ea-845c-db8fad08e222 | -3.1069 | -45.768 | 2024-11-24 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 101ee0ef-b699-39a8-8047-3da6cf273a04 | -1.5129 | -54.1959 | 2024-11-24 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a2dc93d4-11c6-375f-9527-62aec9d235c1 | -2.4456 | -49.0816 | 2024-11-24 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5aaa1563-44dc-3fc2-8c26-58452ba47b0a | -3.8304 | -46.0057 | 2024-11-24 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 65dcf65c-62c1-3603-bbc0-d32e62d3a57d | -1.8423 | -46.6482 | 2024-11-24 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4feacad0-4296-31ff-8084-7e60c3dfa055 | -1.8053 | -46.649 | 2024-11-24 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 7fdbce49-eac7-3351-a4bc-ff672ebe89e1 | -3.5995 | -47.5142 | 2024-11-24 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 61f0ad7f-5d1b-34bf-9337-0d47ccddef81 | -2.9043 | -45.3719 | 2024-11-24 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 250.5 |
| 7dc9712b-6516-3b5f-a10c-c5552fe4e722 | -4.2605 | -48.697 | 2024-11-24 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ad3087e7-9086-3d7d-a526-f78f76738624 | -0.8724 | -52.7483 | 2024-11-24 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| aac6f699-ee25-3418-839f-ed139b9fe86f | -5.9556 | -48.0642 | 2024-11-24 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| cc687c9b-dbfa-3491-8c0e-afdac47eae6c | -2.9582 | -45.7957 | 2024-11-24 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e77edc16-2673-318c-856a-dde8c6c3398d | -3.242 | -53.2751 | 2024-11-24 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a771dfad-3804-37ac-91e8-84b6cea0c466 | -1.8239 | -46.6265 | 2024-11-24 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 226.1 |
| e2304f8e-d171-382e-b656-f60589ad3c2d | -4.2419 | -48.7193 | 2024-11-24 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f2d38636-c6ea-3ab5-b4e5-bc6a166aea4f | -2.5842 | -51.8829 | 2024-11-24 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| adfa7cc8-92e0-3f74-a1fb-c5db576eda73 | -1.8238 | -46.6486 | 2024-11-24 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| af562875-30a3-3fb2-8a83-f8e47f471b15 | -1.8053 | -46.6269 | 2024-11-24 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| bef75827-27be-3683-b36c-da0c28605214 | -2.741 | -49.1375 | 2024-11-24 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 78f88b20-bde9-3ab2-9b5e-3ce54afab3d0 | -3.2569 | -54.2226 | 2024-11-24 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2f2bb7e5-4825-3c94-ac84-0a0f24f48106 | -0.8907 | -52.7685 | 2024-11-24 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| ecc5d332-1440-3663-b4eb-fdaff21819f7 | -2.7596 | -49.1157 | 2024-11-24 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |


[Clique aqui para ver as próximas entradas](README13.md)
