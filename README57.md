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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da4741cf-39f4-3ebf-b8f5-b3aad2f3c593 | -13.3537 | -54.4213 | 2025-08-19 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2684b92e-cd8e-371c-9ef8-b2555e6bd281 | -13.8748 | -45.5411 | 2025-08-19 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 34f76c9e-fa63-3efc-b70d-9e7717325290 | -13.1555 | -54.9357 | 2025-08-19 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 888203b7-0633-398c-8a3a-2d69e1b126ae | -13.256 | -50.8377 | 2025-08-19 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 115341ac-3fe3-3259-973e-a8f2cce34bc9 | -13.8752 | -45.5179 | 2025-08-19 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| bf362316-0a47-370d-9645-bd4b7fbdb3d4 | -13.0119 | -45.1988 | 2025-08-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 284.0 |
| 0bce8bc3-df3d-3ff5-b583-a58a4e701b67 | -13.2563 | -50.8162 | 2025-08-19 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 234.4 |
| ebf9e9a3-6732-3f6b-b236-3843ffb90839 | -12.6536 | -45.8082 | 2025-08-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9cdcc8eb-f07d-3deb-b518-9949bb27722b | -6.9339 | -43.5868 | 2025-08-19 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 383c1abe-9a7f-38b0-aeeb-71c313508fac | -7.1606 | -43.4956 | 2025-08-19 12:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 510c29f8-cbd6-3413-9e88-5d9a3509358a | -12.993 | -45.1787 | 2025-08-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 9188f297-6430-38e9-bca7-e7ed925785b8 | -12.8984 | -46.0906 | 2025-08-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 263.6 |
| 7d3bcada-77f3-3652-ad64-2d35852cb98a | -13.2752 | -50.8352 | 2025-08-19 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 60e7de52-e9fd-34d1-a5f4-38d1ef8e463a | -15.0386 | -54.8297 | 2025-08-19 12:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5d71275c-6904-3abc-ac61-8af11a45240a | -13.0119 | -45.1988 | 2025-08-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 79f8fe7f-5d38-35fd-ad57-b2c7cce21d36 | -13.1555 | -54.9357 | 2025-08-19 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 77454b12-6892-3827-9c63-5d0d15d45eb6 | -5.7887 | -43.6134 | 2025-08-19 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5bcf0e4c-5033-34fb-9b12-719b0318c6e3 | -13.3537 | -54.4213 | 2025-08-19 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| ef4ecf16-0e4f-394b-9726-cc8a71bd3eaa | -13.2755 | -50.8137 | 2025-08-19 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1b90dd12-b01f-37bb-b9a2-eb6021d63130 | -6.9527 | -43.585 | 2025-08-19 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a012e15c-e42f-34dd-bd67-fc22a579a0a5 | -14.1707 | -45.3042 | 2025-08-19 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 59f91c41-4a68-3082-9cd9-7f6b1c74ccbd | -6.5201 | -45.5013 | 2025-08-19 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d059aa0c-8771-3c4f-9f5e-a1a7c600ad7d | -6.9715 | -43.5833 | 2025-08-19 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| b4760a21-9a80-3eaf-b808-b71c306b5518 | -13.2567 | -50.7947 | 2025-08-19 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 5309f3ab-8879-3a41-bec1-c2b02d0b3618 | -13.2563 | -50.8162 | 2025-08-19 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 979eaf66-2840-3a5a-acc9-50cbbaa6d990 | -13.8748 | -45.5411 | 2025-08-19 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| ddb40e55-052a-32d7-adc2-2b99b3b36ed0 | -13.8752 | -45.5179 | 2025-08-19 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bb7867e9-001a-3a66-a7cd-98304b08d527 | -12.9925 | -45.202 | 2025-08-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 4557aba6-5593-3e17-8340-8c0e6da472c6 | -12.8791 | -46.0936 | 2025-08-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| a44f0431-8c84-3afa-931c-60d48ca50413 | -13.1555 | -54.9357 | 2025-08-19 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0dd255a7-1402-3b9c-8a6f-220dba206ce1 | -6.9715 | -43.5833 | 2025-08-19 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 68020256-04ff-3534-8629-0877c081e438 | -11.6048 | -46.6188 | 2025-08-19 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 34a3129c-28d3-3026-8d73-5b386d18eaca | -13.8752 | -45.5179 | 2025-08-19 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a5ad4f1e-c685-382d-9c08-7855054c6920 | -6.9527 | -43.585 | 2025-08-19 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 06a75cd4-47b6-3cf0-9f6f-cbf6a76fc80d | -15.0196 | -54.8112 | 2025-08-19 12:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 53f14e6a-9f95-350c-b847-472e236a3f6f | -13.2755 | -50.8137 | 2025-08-19 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8533fe05-65de-3932-b112-7bbb6bffdfd4 | -7.1606 | -43.4956 | 2025-08-19 12:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 078f8a7f-253a-3795-b2ae-9ab0c0770a9c | -13.1746 | -54.9337 | 2025-08-19 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| cee2294c-726b-3a9c-a40e-4a6895d2afa6 | -12.9925 | -45.202 | 2025-08-19 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a9093893-b47b-3dd4-b89d-2aab4b4e7c17 | -13.8748 | -45.5411 | 2025-08-19 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ef9ce488-4a6c-334c-b9cc-413c3481534f | -12.993 | -45.1787 | 2025-08-19 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| d8f7fed1-18e8-3034-8b8e-4f314ef7dd4b | -6.9339 | -43.5868 | 2025-08-19 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 25463f69-c014-36cc-8f37-7852dd3a75c1 | -6.5201 | -45.5013 | 2025-08-19 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 836c6b3b-a053-3617-b95f-29b30d0c6403 | -5.7887 | -43.6134 | 2025-08-19 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4e1598d4-3caf-3970-b245-ee287fce96ee | -13.2563 | -50.8162 | 2025-08-19 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 84266d53-2e39-3e94-bc55-4bbe4408ca31 | -13.3537 | -54.4213 | 2025-08-19 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 8ad66d14-1436-3893-ac90-0bf0febd0533 | -14.1707 | -45.3042 | 2025-08-19 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 05a662a6-764a-3510-b965-05dbc5aab63d | -13.2567 | -50.7947 | 2025-08-19 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c14bd859-059a-3cb5-a171-fd836df82e51 | -13.0119 | -45.1988 | 2025-08-19 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 259.5 |
| 36c99ee3-64f8-3dd1-a545-d774d2439944 | -6.9715 | -43.5833 | 2025-08-19 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| cda72297-060a-3a59-9576-9c760ac7c103 | -5.7887 | -43.6134 | 2025-08-19 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| da708601-a5de-3d8f-b828-b1e2673a46d3 | -13.1555 | -54.9357 | 2025-08-19 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.9 |
| f9c2d184-e84e-3fec-918a-53f1854921d0 | -6.9527 | -43.585 | 2025-08-19 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 90af01b1-f82f-3818-9eb7-eb11df60dae5 | -6.5013 | -45.5028 | 2025-08-19 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 23ccd715-9559-365c-bbc9-6e5279ab758b | -15.0196 | -54.8112 | 2025-08-19 12:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cd60cc6a-9d3d-3b65-910f-0280e35253d6 | -13.3537 | -54.4213 | 2025-08-19 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| b6177eab-97d3-3301-9612-78054aaa6326 | -6.9339 | -43.5868 | 2025-08-19 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 32679ae8-2daa-3672-a282-75e3299d1a32 | -13.3534 | -54.4419 | 2025-08-19 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 3bb9d915-0cdb-31f4-bf0a-933480cdfacc | -13.2755 | -50.8137 | 2025-08-19 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 32ecf728-8161-35b5-8b3b-5f90efd230ef | -13.354 | -54.4006 | 2025-08-19 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 28eb87e0-80da-35dc-9f9f-39dafc7f3fab | -12.9925 | -45.202 | 2025-08-19 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 7687c3ec-a78a-3a0b-8528-4043d38ed4a1 | -14.1707 | -45.3042 | 2025-08-19 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7b8a1e81-3433-397c-a502-4b0ae1d5316a | -13.0119 | -45.1988 | 2025-08-19 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| b31d6ffc-3f6f-33b6-a66c-120f7df1d4c2 | -15.0389 | -54.8089 | 2025-08-19 12:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d09f06c5-86fe-34d6-a0c1-93a7fbaadab4 | -13.8553 | -45.5444 | 2025-08-19 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c3311e79-2aa1-3f99-b5da-162428e49f5e | -7.1606 | -43.4956 | 2025-08-19 12:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| efd95a8f-e1a2-3d6b-84d9-96aa41aa9075 | -15.0386 | -54.8297 | 2025-08-19 12:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 69811af3-ff02-3319-9da3-35df51d36318 | -13.8752 | -45.5179 | 2025-08-19 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b2605ba8-024c-3d10-85bb-91ac7c2ecd75 | -12.9739 | -46.1703 | 2025-08-19 12:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7323c355-c42b-3a9a-bba4-79ff8db17377 | -12.993 | -45.1787 | 2025-08-19 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| dc52a61d-72bd-314b-a07e-f459323e1abc | -13.8748 | -45.5411 | 2025-08-19 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| cc0935b9-21a8-33d0-9052-7933c1578344 | -6.5201 | -45.5013 | 2025-08-19 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| d0fe98da-3128-38c5-b183-46498fb50cf5 | -13.2563 | -50.8162 | 2025-08-19 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 6d8ab7d0-ecb8-3e75-945f-bde8d39f6f24 | -6.5203 | -45.4787 | 2025-08-19 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7fad5728-5615-31ee-be70-22256ac83fc3 | -13.1746 | -54.9337 | 2025-08-19 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 648cb763-5406-334b-a42b-be57caca6ab7 | -13.2567 | -50.7947 | 2025-08-19 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 9a846aa4-5c37-3eac-a6e2-4b8eac346ba7 | -6.9527 | -43.585 | 2025-08-19 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 2a0720ed-ef1d-36e1-8a00-1cc3ea8d4176 | -14.1707 | -45.3042 | 2025-08-19 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 40e56169-04e2-35ab-a712-e4c1034c26d3 | -13.1558 | -54.9151 | 2025-08-19 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e51f3164-aa37-3bc8-a65c-58c439afe8df | -15.0389 | -54.8089 | 2025-08-19 12:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8052cc80-7fa6-34c1-b0a1-c95477dfed29 | -13.0119 | -45.1988 | 2025-08-19 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 8ae4567f-7495-3935-a860-bf919076698d | -6.9712 | -43.6066 | 2025-08-19 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| cf4f3cb6-b699-3520-b3cf-6958b3055995 | -15.0196 | -54.8112 | 2025-08-19 12:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| fbc34c98-10f3-3576-9a9c-62c33c138655 | -12.9925 | -45.202 | 2025-08-19 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 1af7c061-8ae3-381a-8d38-26136403961d | -7.1606 | -43.4956 | 2025-08-19 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| a5f2d5ea-7b48-3e4d-9c30-1f8b35a7236e | -6.5201 | -45.5013 | 2025-08-19 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e709a3e3-253a-32f9-82d6-229a4dd1a011 | -13.3537 | -54.4213 | 2025-08-19 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 248.2 |
| 571db6ff-1df3-3fc0-b449-d9437a43dcac | -13.8748 | -45.5411 | 2025-08-19 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 39f9c9ac-ab27-3e92-9f8c-2b2344b46417 | -15.0386 | -54.8297 | 2025-08-19 12:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 77e25195-3892-349f-bdd9-97c32398f1a0 | -12.4729 | -43.1967 | 2025-08-19 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b1a40ee4-1871-38ae-bf11-ed0f5720f7b8 | -12.993 | -45.1787 | 2025-08-19 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 97602d97-ac18-31de-a002-908b098e9f67 | -13.3534 | -54.4419 | 2025-08-19 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 3f0d44fb-3208-320f-bfce-7b6ce8bc7c77 | -7.5899 | -45.4315 | 2025-08-19 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 65754058-38ab-3705-87fa-9654e5874a9d | -13.2567 | -50.7947 | 2025-08-19 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c827d0ab-9241-3e4c-a6a8-d96e417c9e35 | -13.1746 | -54.9337 | 2025-08-19 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.8 |
| f7c151d1-f0c0-35de-aa05-b09e029f24ac | -13.1555 | -54.9357 | 2025-08-19 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 193.2 |
| a1479717-ca04-3bd0-a45f-96ecea8dd3b5 | -11.6044 | -46.6414 | 2025-08-19 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| dbddce54-5a42-3e5b-9121-55d935bab614 | -11.6048 | -46.6188 | 2025-08-19 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 3f222bd5-007d-3a5f-97c5-7ccab5724db5 | -12.8984 | -46.0906 | 2025-08-19 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1a029c3c-32f0-3a8f-981d-fbc008de9404 | -13.2563 | -50.8162 | 2025-08-19 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |


[Clique aqui para ver as próximas entradas](README58.md)
