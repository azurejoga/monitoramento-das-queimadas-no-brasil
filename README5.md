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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af952e0d-b100-3550-83e6-b888d76e2973 | -3.60048 | -43.63131 | 2024-11-21 00:26:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c50268e4-8fc7-3cf5-8663-cbe23670e375 | -3.57531 | -46.07274 | 2024-11-21 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 7b0f9ae4-abe7-3825-9ee2-3b86eaa60280 | -4.51836 | -45.2686 | 2024-11-21 00:26:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e1f401b2-83e5-3050-b452-9d6128aba86e | -3.47765 | -44.39837 | 2024-11-21 00:26:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9d93e7c0-3b75-3ff1-a634-7f87f0ca40c3 | -4.57517 | -43.96056 | 2024-11-21 00:26:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c67b860f-d900-3191-ba8e-8f56e947a47d | -4.40352 | -47.64519 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| db96c532-5226-320d-a81e-c4cad14f5f3a | -1.23479 | -46.74253 | 2024-11-21 00:26:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 963a99a5-c0bf-3f33-aa60-7f9f3ebb0312 | -6.93939 | -41.20227 | 2024-11-21 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9bca4867-4123-3184-8154-0fdf1291e237 | -3.00493 | -40.22591 | 2024-11-21 00:26:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 15a1be50-e954-3e77-a140-cf9e8b9edb63 | -3.39958 | -50.10191 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 2f700464-23c9-3778-a74e-e6122b9132ff | -6.65918 | -39.23362 | 2024-11-21 00:26:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8808bafa-3312-3678-b040-b2b6a9b5cfa6 | -3.53698 | -50.44602 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 45e0e4cc-feae-36bc-94d4-7a8c95744e07 | -7.501 | -42.87466 | 2024-11-21 00:26:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 39599d53-c062-37b9-b7b0-003c80d378d5 | -4.2456 | -46.11404 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ec87a26c-a861-3659-a92e-93be99c6f8f2 | -3.3689 | -52.45053 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| dc4db112-069a-3a55-9da9-16c134fdcea4 | -3.12162 | -45.07331 | 2024-11-21 00:26:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 06a667ef-db04-3df2-9aa3-196434b20418 | -1.78862 | -48.44181 | 2024-11-21 00:26:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d2a795af-fa10-31ad-a575-6a459646c67b | -4.39188 | -45.60715 | 2024-11-21 00:26:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 623fbd00-cb45-39e0-8540-e5deb2111307 | -3.0086 | -51.0169 | 2024-11-21 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 60aa8abe-8c35-39d1-a62e-bceb8abbd2d6 | -3.36079 | -43.82907 | 2024-11-21 00:26:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| fb6d371d-2278-310b-b778-6128c01de61d | -3.47908 | -44.4086 | 2024-11-21 00:26:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 43cefda5-39a6-3f88-8d42-87da2bcdedab | -4.5682 | -48.00964 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 60807ffa-0f08-3d53-a594-1341e990cc14 | -3.28683 | -45.59539 | 2024-11-21 00:26:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 864e7bc7-aa3c-30aa-8d2a-f1aa3e9c641d | -3.74886 | -47.35814 | 2024-11-21 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 118bded5-cda4-3b26-98d6-a5418d205fdc | -3.1559 | -44.34712 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ae3bc81f-d2e1-30ae-81cf-f1585e893828 | -4.14197 | -43.87964 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4408a917-0fc0-3c98-871d-68dc3b9c91f8 | -3.37482 | -52.4874 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 087fdd46-9c13-32f0-a727-478aad313556 | -1.44548 | -47.11947 | 2024-11-21 00:26:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 223cf543-a486-39fe-b7b2-26c21008d5af | -3.36263 | -50.16867 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 27c943bc-cf32-3dcb-801f-f794373f4f00 | -4.08337 | -49.28871 | 2024-11-21 00:26:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 11161cb4-fdd3-3dc0-a297-a811c5b72b9c | -3.35131 | -50.19126 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 62887a24-9285-31f7-ab90-3366b4428cdb | -4.37015 | -46.08448 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1dfcdc41-c4f3-3eec-af50-29d494402033 | -5.14 | -39.80759 | 2024-11-21 00:26:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a24fb444-27be-3212-a7a1-05a9f7cf8395 | -5.2402 | -42.63537 | 2024-11-21 00:26:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 3e305d5b-6964-3e49-8f10-b6dbefb0bbaf | -5.71379 | -39.06941 | 2024-11-21 00:26:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d11948c0-d2e4-3290-b72b-b98838381196 | -4.14333 | -43.88942 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ae47d110-5dcb-3d79-8408-cad288a9c869 | -2.89142 | -46.70653 | 2024-11-21 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d13d7bf1-cf01-3d55-8d89-a84ccbd55131 | -3.81062 | -52.35732 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1519d2b6-a92e-3769-bea6-b4cddbb6b9d9 | -3.29975 | -45.55077 | 2024-11-21 00:26:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dbc46e5d-615c-3d0c-8b09-dd512e6ab998 | -5.42654 | -45.34285 | 2024-11-21 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4aacc1c4-8f82-30b1-a3a8-fbf9f168af39 | -2.23167 | -46.48325 | 2024-11-21 00:26:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 25559c92-88ff-344f-8199-2b61ee1f67de | -2.08616 | -46.2885 | 2024-11-21 00:26:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ef0e427c-4a7c-3e5b-bd82-cf4a80a41bdd | -7.39586 | -42.77879 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 9c22e51d-1940-3b45-b944-242487cf2143 | -3.56641 | -46.08725 | 2024-11-21 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 844b446a-232b-37dd-8ca5-4910be2a3c74 | -3.3745 | -52.49205 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 659bd3c3-23bb-37ee-b75c-ec6997d9880d | -3.81103 | -42.55204 | 2024-11-21 00:26:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce66651f-1252-39c3-8274-7a55d998c260 | -4.06239 | -50.89581 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 0406e35d-ee0a-3fc7-9c02-de0937b83267 | -5.95117 | -44.46656 | 2024-11-21 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 85044aa3-b5ec-329a-aa37-55a6a69c7b13 | -4.57078 | -48.02909 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2ef94568-2a80-300a-97c9-6f19e2b80946 | -3.57649 | -50.40461 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 13456bef-096d-3678-bea2-443fb966c936 | -5.10252 | -43.17413 | 2024-11-21 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 367548ad-4804-3f73-99a2-933f395b0dc8 | -4.15073 | -42.01939 | 2024-11-21 00:26:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| eb77c354-0061-3164-823a-c3d6abd2875e | -3.68801 | -50.21291 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 3d158a52-a90b-3498-8aef-faa38c6d126e | -3.28852 | -45.60739 | 2024-11-21 00:26:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 014c4726-4e47-3dcd-bbe5-ee345073752d | -6.18538 | -43.41532 | 2024-11-21 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 6ae5fc4c-0740-3629-b8f9-8010a89bc727 | -2.52289 | -45.61642 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 818a0afd-caf5-33c9-8408-01f738a574eb | -5.95069 | -44.24461 | 2024-11-21 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d1fa0211-58fb-3962-89ca-c9104b25ec1e | -3.15452 | -44.33705 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 96c7d752-cb93-3d17-a535-3bba9bcc34c4 | -4.49054 | -45.36982 | 2024-11-21 00:26:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 462ad693-bd7b-3134-baad-d4065a84a599 | -0.92554 | -47.85115 | 2024-11-21 00:26:00 | TERRA_M-M | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7a87b1d1-3857-3a03-82c4-d9e2d140605b | -3.79755 | -41.00471 | 2024-11-21 00:26:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 26d92534-53ea-3bfa-8a62-dcc33bc23b2f | -2.09009 | -46.39353 | 2024-11-21 00:26:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b3f53e60-e0f4-3d5b-bfe1-b0f5876c00f0 | -1.05018 | -51.75169 | 2024-11-21 00:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 71cc254f-d2a4-3cc4-ab1e-a6c6956c6d0d | -0.77997 | -51.77309 | 2024-11-21 00:28:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 24.9 |
| af107909-efbd-3169-8d60-c9e5a76ba3f1 | 0.40757 | -50.82584 | 2024-11-21 00:28:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 37.4 |
| c3c4f7d3-200f-34f3-92b7-509208e43118 | -0.78819 | -51.76681 | 2024-11-21 00:28:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 0401cb70-721b-3372-b796-39f4deba86a7 | 0.40848 | -50.83251 | 2024-11-21 00:28:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c4641a6d-dbe5-3046-ad49-2144052ad2ca | -3.1831 | -54.3247 | 2024-11-21 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d1059872-64f6-39b2-9f8f-6e552241e73c | -2.0075 | -54.5292 | 2024-11-21 00:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a1e80e2c-38f5-3dd8-b9df-57ed39225c3e | -4.5799 | -48.0349 | 2024-11-21 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 6f65bae6-245b-33fa-8bd3-66a58a6bbe88 | -4.16 | -43.8818 | 2024-11-21 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a3ec8eee-9ef9-39ac-bded-cf0707358a65 | -10.1223 | -65.0237 | 2024-11-21 00:30:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b23e33b0-6fc0-37ac-bcac-09d40cce8001 | -17.6111 | -50.1737 | 2024-11-21 00:30:00 | GOES-16 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 425fdedd-e671-3cfb-924e-51756f79d764 | -5.0996 | -43.1744 | 2024-11-21 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 3df3d53f-1f71-3955-b0d6-7c707c6bbc63 | -3.3924 | -52.4563 | 2024-11-21 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 9376c29a-61a8-312d-975b-f0c4e1628d5e | -4.1413 | -43.8828 | 2024-11-21 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d8edb5f9-5644-36a8-a7ac-a97dbdf6e92c | -4.5986 | -48.0123 | 2024-11-21 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 0fbb89d6-251e-3e26-bf4c-5a726524e8f4 | -6.8258 | -46.7737 | 2024-11-21 00:30:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e3ae5110-c857-3752-8909-7c91c215399e | -2.7491 | -52.105 | 2024-11-21 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5c2a6364-00cb-3efe-8fa1-33061a13914f | -17.5907 | -50.1995 | 2024-11-21 00:30:00 | GOES-16 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 39a0da60-2f64-3022-9e51-f783a39bb19e | -4.5614 | -48.0141 | 2024-11-21 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 01c84cce-7cbc-36b2-b0d3-a305d1307e70 | -17.5912 | -50.1772 | 2024-11-21 00:30:00 | GOES-16 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 07fcb937-3bbf-34c7-bb00-966bc2a5b3aa | -1.7556 | -52.0636 | 2024-11-21 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 752dbdc1-46a0-3284-ad34-ec23eb8933b8 | -3.295 | -53.8597 | 2024-11-21 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| da6df547-2a81-3652-8271-c118f7086727 | -3.374 | -52.4364 | 2024-11-21 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 98b153d4-dfec-3d5b-a5cd-18d5dce2d7cc | -3.2767 | -53.84 | 2024-11-21 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 42f4cb23-292c-3cbc-b89b-ab06f6de9022 | -3.4724 | -43.4306 | 2024-11-21 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 54265af6-a566-39c4-a5ac-af5406c2ab39 | -3.2952 | -53.8194 | 2024-11-21 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 72b4fa29-616e-3f16-820a-54236a5d845b | -3.374 | -52.4568 | 2024-11-21 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 214.1 |
| 1434088d-02e4-3474-a69a-6c375b66a210 | -2.7675 | -52.1251 | 2024-11-21 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| c09c1547-f1b1-395d-ae3d-793949d98979 | -3.6018 | -43.6331 | 2024-11-21 00:30:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5d66650c-3886-340f-82ea-98f38d5ac7c4 | -2.0259 | -54.5289 | 2024-11-21 00:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 227ad339-6bfc-31a1-9e05-d350c58df7f4 | -3.5698 | -46.084 | 2024-11-21 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 37631064-4767-345a-bc3c-989c67089c89 | -3.3739 | -52.4773 | 2024-11-21 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 35c6af0f-abb2-3a6a-b4cc-61309fa75834 | -3.2014 | -54.3243 | 2024-11-21 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 7a274e02-5966-3b24-9b9c-244a0180ea65 | -5.1183 | -43.1731 | 2024-11-21 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 74aeeb18-9a10-346a-a43b-327ab60329f1 | -4.6446 | -49.5544 | 2024-11-21 00:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ec642131-1dff-328f-8442-f615555347d7 | -3.4725 | -43.4074 | 2024-11-21 00:30:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 170.4 |
| c71eca5c-93b9-321d-9ff9-9ec8262b9d0e | -1.7372 | -52.0639 | 2024-11-21 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9bf0ad34-c857-3956-a34f-e829f4f82393 | -2.7676 | -52.1045 | 2024-11-21 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |


[Clique aqui para ver as próximas entradas](README6.md)
