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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21937c14-6440-394f-a3e3-1f219be6e8d3 | -4.3988 | -44.4424 | 2025-12-10 00:00:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 814501a6-0972-30d2-8a40-989b78c92198 | -2.514 | -45.4298 | 2025-12-10 00:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| be4a25c9-8639-3db8-a440-0fdfc9abf84e | -5.1749 | -43.1224 | 2025-12-10 00:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 229.8 |
| deef9e07-0250-3a97-bc19-d6249d914b93 | -2.2169 | -45.4159 | 2025-12-10 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 0f19f422-df0c-37f6-bee1-fa217c03b973 | -5.1751 | -43.099 | 2025-12-10 00:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| c226d166-4405-35f7-992d-ea035357dcb6 | -5.1562 | -43.1237 | 2025-12-10 00:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f2cdc111-4efb-3402-a9f8-1537e71493df | 3.3788 | -51.2618 | 2025-12-10 00:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 63b4de0b-a598-3177-9625-7301be33b49d | -4.381 | -44.3061 | 2025-12-10 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d5064778-77cf-3d7d-a9f3-a9055b458e7d | -4.3624 | -44.3072 | 2025-12-10 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0b5b9d39-2d42-3d2a-be4e-1defbf975214 | -5.1562 | -43.1237 | 2025-12-10 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 29587d0e-a5e6-3691-b3d7-8ba02aa7edc5 | -1.7316 | -46.4961 | 2025-12-10 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e7b672c8-0697-3e33-abe7-b2159a0b69fc | -5.1751 | -43.099 | 2025-12-10 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5f5c10da-d9f8-36ba-b174-023e4f346217 | -1.7315 | -46.5182 | 2025-12-10 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5efecf30-e7cd-3bcd-a042-4690004babfc | -5.1749 | -43.1224 | 2025-12-10 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 190.0 |
| e78d93ed-5123-3920-b959-217af8170534 | -2.2169 | -45.4159 | 2025-12-10 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 78f28713-b51b-30a9-bdb6-9056f70b57bc | -2.5155 | -45.0243 | 2025-12-10 00:10:00 | GOES-19 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a3de504b-a2da-31ae-b40f-5532af9cc77b | -2.1984 | -45.4164 | 2025-12-10 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 76bf9e9c-524b-3662-b50c-7cbdd41c2702 | -5.1564 | -43.1003 | 2025-12-10 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ee8acfdc-65c1-3f0c-86fc-c50e3d2ef8d8 | -2.2169 | -45.4159 | 2025-12-10 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 2ce12400-e6c4-32dc-aa5b-452f00d0fe66 | -5.1562 | -43.1237 | 2025-12-10 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 56063c9b-750e-3f78-8689-8a8ae3278972 | -5.1564 | -43.1003 | 2025-12-10 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 11c5bc12-be7f-3226-a9d0-d87a3b41928d | -3.694 | -43.8134 | 2025-12-10 00:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c23bb38d-2453-39e5-b8e3-124c26ff9e99 | -3.6754 | -43.8143 | 2025-12-10 00:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 257f679d-3180-3cd2-b9dc-da26805fc37c | -5.1751 | -43.099 | 2025-12-10 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 7d0c155c-db26-3e8f-a9a2-ff0027ba3e39 | -2.1984 | -45.4164 | 2025-12-10 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 63cafec1-36ec-3f37-831d-ef5229b702d5 | -5.1749 | -43.1224 | 2025-12-10 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 61d0243b-b55e-335b-978a-5adaa4ff4849 | 3.3788 | -51.2618 | 2025-12-10 00:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2e2e49ae-9ecf-3dd3-a36c-83c8c012d3f8 | -3.6939 | -43.8365 | 2025-12-10 00:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b69e0faf-e80c-356e-962c-034070935901 | -3.694 | -43.8134 | 2025-12-10 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 242.1 |
| ce58de03-80db-374e-8758-0dd06894cbd5 | 3.3788 | -51.2618 | 2025-12-10 00:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2564dc51-ce64-3dd4-81d1-94b33fad9084 | -3.6754 | -43.8143 | 2025-12-10 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 955ce612-8851-3366-bfc6-2f813aa67de7 | 3.3787 | -51.2826 | 2025-12-10 00:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1974247f-c499-3d36-ab62-574b7763418b | -3.7127 | -43.8125 | 2025-12-10 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b3e3fd1d-7676-3b92-b074-6e1ef7a77cea | -1.7315 | -46.5182 | 2025-12-10 00:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e4cf7aac-6052-3a3e-a097-f6c6a2885a93 | -3.7125 | -43.8356 | 2025-12-10 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 6a06534a-f17c-3546-b4fe-c0ca01e485ab | -3.6939 | -43.8365 | 2025-12-10 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 202.5 |
| a1e726e4-ea7d-38e7-be24-7ff105816de5 | -3.6752 | -43.8374 | 2025-12-10 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| ba56005a-bff8-35bc-a495-30c379d7e1f4 | -2.1984 | -45.4164 | 2025-12-10 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 48fcf988-bc1c-356a-9672-fbc8aaeb06ed | -2.2169 | -45.4159 | 2025-12-10 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 463e568e-daed-3eaa-9de4-e5c2a5bd3a34 | -3.6939 | -43.8365 | 2025-12-10 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| acc3ee3e-3c6a-37cd-ba29-1e2f96f2f885 | -2.2169 | -45.4159 | 2025-12-10 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7f0ab988-6c5d-3a2e-b9e6-79ad47629275 | -3.6752 | -43.8374 | 2025-12-10 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 298ee22b-599c-3206-b43c-cd81dbcda53b | 3.3787 | -51.2826 | 2025-12-10 00:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 48.8 |
| fee0b35f-c2e7-3393-b624-49bb623b023f | -3.7127 | -43.8125 | 2025-12-10 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 12238760-9057-3132-a30f-53bd32cec84d | -3.6754 | -43.8143 | 2025-12-10 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 194.8 |
| f16f8708-dd81-3e6e-86f8-d204eb67d449 | 3.3788 | -51.2618 | 2025-12-10 00:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 68e92264-e33e-32ce-b789-66d520204dd4 | -3.694 | -43.8134 | 2025-12-10 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 278.9 |
| e942de30-cd56-328d-8589-ee8fe04e76d4 | -5.1562 | -43.1237 | 2025-12-10 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 09dbb773-a3cb-3dfa-934c-234a179296e0 | -5.1749 | -43.1224 | 2025-12-10 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 99fc26eb-5c62-3619-9f64-4e77f28d144f | -2.4869 | -47.7909 | 2025-12-10 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 8cd401ee-334c-3869-8195-798fa5fb6568 | -5.1751 | -43.099 | 2025-12-10 00:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| eddbf5d7-a0ec-3e46-a952-930abf0a4f12 | -3.694 | -43.8134 | 2025-12-10 00:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 286.7 |
| fcf0333d-faac-354e-8a23-918026e35495 | -3.6939 | -43.8365 | 2025-12-10 00:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 7f12ccd3-5400-3f58-bef0-635741f907de | -2.2169 | -45.4159 | 2025-12-10 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d13b8e7f-e060-3b96-be2c-d731f3f3c11f | -3.6754 | -43.8143 | 2025-12-10 00:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 2629e97f-1812-32ee-aa44-07add6c9c378 | -2.487 | -47.7692 | 2025-12-10 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 1732f69d-8899-39b1-aec3-a10f16fbc2da | -3.6752 | -43.8374 | 2025-12-10 00:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 43600327-814e-327d-8b7a-2e8007f2bf7d | 3.399 | -51.2509 | 2025-12-10 00:58:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bb8f7b58-d7d6-3cff-b791-a48d54c59a72 | 0.4574 | -60.411701 | 2025-12-10 00:58:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6e1128-92dc-3e74-934e-ee3c401c9848 | -3.6939 | -43.8365 | 2025-12-10 01:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 9e9b6904-a918-3742-9c00-ce93ac74d1ae | -2.2646 | -47.8617 | 2025-12-10 01:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| f78d45db-7541-325a-a246-5ac8443c1a28 | -3.6752 | -43.8374 | 2025-12-10 01:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 65f172b8-e6ac-363b-8e34-a39bec99411a | -2.487 | -47.7692 | 2025-12-10 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3f495789-b820-38b3-b48d-20ce50afecc7 | -2.4869 | -47.7909 | 2025-12-10 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a0bf079d-e77b-3198-ba62-a43a625f9610 | -3.6754 | -43.8143 | 2025-12-10 01:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 16e3e514-c971-3194-bc77-76c459deb82e | -3.694 | -43.8134 | 2025-12-10 01:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 45f334b3-9528-35db-91b1-f581d3aed7ea | 3.3788 | -51.2618 | 2025-12-10 01:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a5066cb0-c611-34db-9d94-7e91c72ad167 | -21.97557 | -56.78849 | 2025-12-10 01:06:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 011afde9-9ddb-3ca6-9037-6f1f3d885eca | -21.9769 | -56.798 | 2025-12-10 01:06:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65dfd9b7-1f7c-3f01-9040-3ead4326ad88 | -2.487 | -47.7692 | 2025-12-10 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 7751bea7-28da-3b1b-8c0d-1ff8c472f27b | -3.6939 | -43.8365 | 2025-12-10 01:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 48a8f344-138f-39af-b1ef-449b5d53fcbe | -5.1749 | -43.1224 | 2025-12-10 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e50300ca-3566-35b4-bd52-19b146fe469f | -5.1751 | -43.099 | 2025-12-10 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5735421d-49ff-3001-a775-6949856dab67 | -3.6754 | -43.8143 | 2025-12-10 01:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 09b65b56-9db8-3cfc-ae6e-deb26277011f | -3.694 | -43.8134 | 2025-12-10 01:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| e7239c30-e31e-3b5a-8ead-1f67b6d08673 | 3.3788 | -51.2618 | 2025-12-10 01:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5d97d983-d7c4-3d23-8ddd-dfafd25c98b4 | -3.6752 | -43.8374 | 2025-12-10 01:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0b72f219-4f9f-3fb6-8aba-5d3e20d00a8d | -2.4869 | -47.7909 | 2025-12-10 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 195059af-d3ae-330d-9aeb-82a0c33b6b2f | -5.1562 | -43.1237 | 2025-12-10 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0edbe2b8-d80a-3218-9a70-244b57a70486 | -1.8757 | -54.68737 | 2025-12-10 01:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 7ff72df0-9f53-3043-9ea9-e68578d65afd | -1.48092 | -53.54582 | 2025-12-10 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a393eb5d-3be0-3e1f-945a-391be2ff8443 | -1.58323 | -54.12232 | 2025-12-10 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8fb16058-d1ec-30d5-b2b2-c322bd9eeedf | -1.48322 | -53.53903 | 2025-12-10 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b4a82c7b-4501-3b5b-b8b0-036b9a5dfb80 | 3.3418 | -60.88282 | 2025-12-10 01:13:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2b6ae269-afc7-3707-b237-7405e7c6fdf6 | -1.47716 | -54.21492 | 2025-12-10 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f361b6ce-5c01-326a-97ca-c47f07496c7f | -1.47377 | -54.19202 | 2025-12-10 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fb11463b-48a0-352c-bbf5-3ff268732a15 | 1.97761 | -60.68671 | 2025-12-10 01:13:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5cfd155e-5232-354d-8c9f-e89a71ef18e9 | 0.45614 | -60.42678 | 2025-12-10 01:13:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ef5ff18b-45b5-3ca4-833f-901b188150bb | 2.01994 | -55.65905 | 2025-12-10 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6874efcb-e85c-3979-b75e-60df58550f76 | 3.34308 | -60.87348 | 2025-12-10 01:13:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 687c18a5-bef4-3e02-9842-d14c4f8b6c6e | -1.48072 | -54.19675 | 2025-12-10 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ef7d4057-cc6d-398d-95fc-d5ef9b2e0085 | -2.4869 | -47.7909 | 2025-12-10 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bc284f92-0ae1-3e8f-a6ec-938692c80151 | -3.6754 | -43.8143 | 2025-12-10 01:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 4b29f56f-4cbe-3e8d-9b6f-a038dfc5a842 | -2.487 | -47.7692 | 2025-12-10 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 22af8b65-fa8f-3993-a050-cc09bbbb0805 | -3.6939 | -43.8365 | 2025-12-10 01:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 4435d50f-9aaf-3eaa-94b2-927494ab14c0 | -5.1562 | -43.1237 | 2025-12-10 01:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 87416cbd-4a31-3e5e-8056-bc565b00e09c | -5.1749 | -43.1224 | 2025-12-10 01:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9e881692-e532-347b-a51f-dadc2e0a1cfc | -3.6752 | -43.8374 | 2025-12-10 01:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2eefa020-6e9a-3f5b-a50f-a067d5c83e81 | -3.694 | -43.8134 | 2025-12-10 01:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| a0b56989-49e0-3f8f-8a61-c17c27a78c89 | -2.2646 | -47.8617 | 2025-12-10 01:20:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |


[Clique aqui para ver as próximas entradas](README2.md)
