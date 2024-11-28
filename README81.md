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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ba75f0b-f738-3389-8c0a-21d8e4a0c8b4 | -3.03523 | -48.50083 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d33aafe0-fa5c-3f7c-bdc0-681ae4117b9e | -3.11437 | -53.26131 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fc578ba-b199-3f06-9c12-4860e5dae0b5 | -3.09755 | -53.26234 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfa5f64e-5f92-3c9a-8e7c-2abb090bda56 | -2.72739 | -53.20338 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce04f731-fe42-37e1-9170-91676bbdaed9 | -3.84526 | -50.0897 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f11f453-50f8-3ebc-9679-d81e2c84e4b0 | -3.07796 | -50.25611 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97c94bd6-50be-3b77-82ec-348891c11328 | -3.96686 | -48.06634 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c982068-1577-3aa6-bdba-cd6999854c53 | -3.68385 | -50.8824 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b6d91b2-c8ef-3a1e-a028-56817456ff18 | -3.96633 | -54.60911 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 123e2830-f234-3ffe-9fd3-be9486a388b2 | -3.49232 | -50.08405 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f69f1810-b372-3b7b-bfd7-112971eadf49 | -3.38605 | -50.32035 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2dccb84-9dbc-3960-bf80-d66448df6a6d | -4.18308 | -48.62703 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ee7c1da-44c0-3cc5-8700-9919da283325 | -3.49099 | -50.44648 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6950a43a-5217-3d74-8907-f21dd4a08000 | -5.97938 | -45.36311 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1b58fd74-cd10-35c7-82be-0197ac65a331 | -2.86022 | -53.99001 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96200184-7643-3cb4-a0d0-2266f1ff0d21 | -2.9955 | -53.36094 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cba53e4-7314-314f-b68e-d1b4cde4565a | -3.09657 | -53.81239 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a5f3de0-7b5f-3dd9-9a34-1aee3d09d5ac | -3.3294 | -50.22087 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4158f427-be83-3156-b3fd-a18741c76c76 | -3.3117 | -50.0274 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1facb34-eb55-3ac4-bfa3-084cd896c08a | -2.69769 | -51.99986 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 52f6c860-c13c-3167-8ed0-dd3576bb7a36 | -2.60727 | -54.24462 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f36d3228-9f8c-3e29-8c73-d878b9dd92d0 | -3.99749 | -53.50998 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccaba5fe-5952-3f2e-83c2-673eeca8fb39 | -4.19947 | -48.5679 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf980550-a3da-3ef3-9d67-8bead047044c | -2.58885 | -54.06138 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d48942bb-5949-3077-a740-2a547759ccfc | -2.60962 | -53.97691 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07cefacf-d4e4-3863-9ff6-b399bd7dc410 | -3.37545 | -50.11208 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f28092f-928a-3196-9780-06232893e0c4 | -2.25762 | -53.46813 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87c3c2c9-98ae-3fd8-9a2b-4265ede9b589 | -2.90071 | -51.37088 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0381fb20-4afe-397a-9e09-3744a9e8f7c3 | -6.66777 | -47.87693 | 2024-11-28 05:18:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 310df611-a99d-3544-84ca-1b39cfd2ec27 | -3.10976 | -53.26426 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baed700f-0c4a-3323-b8ce-b04241996a83 | -3.29195 | -51.15647 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b219d7a-c2f2-332f-a6b9-c8af81f98699 | -2.42775 | -54.01987 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e13da5eb-da30-3943-865e-e4bd9ce11d54 | -3.09808 | -53.25871 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6ca6324-3dc1-304b-904b-878a64dff520 | -7.83281 | -48.19029 | 2024-11-28 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2858c112-c86e-39c2-97fd-6b7f843803b5 | -2.59803 | -53.97514 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eb415a6d-ba97-3dae-8a78-5d109063a079 | -3.7025 | -50.22412 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05c9baf9-f202-31cf-b9fd-5a40a36cd309 | -3.37034 | -53.22151 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad049ce0-df00-3624-8809-5884e260a557 | -3.53877 | -50.19149 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f05e9251-2c82-3139-a7ae-083251d50176 | -3.91501 | -53.81339 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cb2d588-b577-3d85-95cd-a9e7ee67a7e5 | -2.34964 | -53.92202 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 443f0ded-c95e-3dc3-ac0d-e7a786ed4f12 | -2.5949 | -53.96972 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01a3b189-f6cb-38e6-abc1-35904dcf7314 | -2.64349 | -54.28815 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 062a88b1-4325-378d-a71b-d6660eacdc89 | -2.31707 | -51.95448 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 240f39a7-f1c4-32aa-8349-958d3bbcc544 | -4.06252 | -48.83661 | 2024-11-28 05:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58ff80bc-c02e-3a89-9d4f-2790dcfc401f | -2.32394 | -51.97032 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84e6668-2522-33d5-a89b-3e26d0a7de33 | -2.65636 | -49.51692 | 2024-11-28 05:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91ae9fa6-3529-3435-85c2-cb71b0edca58 | -3.39907 | -54.28524 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea608cf6-1a03-3dc1-9886-470707a538fa | -3.06127 | -51.29472 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 422bbf22-f8f0-36b2-a514-edde64f5d5c3 | -3.38693 | -50.10457 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9459468a-00fd-3b03-98b9-2ecda23e9ca1 | -3.44143 | -50.12247 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 732ecddf-49e1-3933-b0f6-0545d0236d9b | -3.19289 | -50.82778 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3076402e-9977-3cac-a89e-bba0e318fdd7 | -3.54414 | -50.53485 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b1ba2af-144f-36ea-8e39-330fd3479d75 | -3.03287 | -48.50195 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e517aa6b-92a7-328e-90eb-87d7d0635eff | -2.81102 | -54.02694 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b2efd17-aefd-3274-aba8-d726a640126c | -4.20004 | -48.5638 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 248dac96-ebb4-3e51-8bf1-3629e30808f7 | -3.11606 | -53.10806 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b961968-4a56-32a3-88a0-0aa6e587b62a | -3.28183 | -53.83515 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7970400c-9894-3a7a-8199-215df8c3e3ed | -3.11833 | -50.29503 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db7f7fa5-74f4-3bb7-855f-46fede288029 | -3.31076 | -53.75099 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80224a61-85d8-3a29-8d6a-264627463c63 | -3.06681 | -54.40957 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 238f28e0-4fd0-3291-bfc9-1e0b44d17a38 | -2.75862 | -52.10489 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c77b25f9-68cc-3c03-97ab-a318e2b40909 | -3.1103 | -53.26066 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faf6c5da-a9ab-375e-8db0-f779ad8a9b49 | -3.20032 | -46.59371 | 2024-11-28 05:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee3ecb69-584a-3a3a-b6e3-cef351854149 | -3.69428 | -51.37049 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03af627a-32d2-3a1a-b270-a6d3b0a65553 | -3.1028 | -50.36693 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec5478a3-5a10-3ca3-ab16-9648ac7c7b0d | -3.10623 | -53.26001 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 898723e4-c0d6-37fc-b0dd-76a8fb559691 | -2.88378 | -52.6868 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a887d9b2-fc2a-3ed9-a9a0-1b461859e0eb | -2.88704 | -51.58543 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16c8a6c1-c1dd-3bf9-a471-efa1c39148a2 | -2.53868 | -54.28893 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b63b0c55-8d11-35be-b48e-553cef739185 | -2.7361 | -54.13268 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13030ed4-054b-3898-9dcc-f094203df42e | -2.44028 | -53.66533 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e45c2177-3230-38ed-995e-e92e5c15eba6 | -3.68773 | -50.21884 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d4cc6b8-58a0-369d-89c5-3ca456094344 | -2.60888 | -53.98174 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33a83d6a-d072-3a0c-887a-46d6bc4701a6 | -3.47112 | -50.5407 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9bc787a-efdb-3f5d-b22d-cb1f4fc7dd14 | -3.25342 | -51.14439 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41c38729-cc9e-3d12-a2e5-d778870d86c5 | -3.41876 | -53.8842 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1f44615-910d-39e4-80c5-a7a5d4c808e1 | -3.11361 | -53.75404 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71620459-5da5-3d18-b67b-b74e9abd0084 | -6.47184 | -54.91772 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c686d4-5f20-3b61-86ea-fd4bb16af39a | -3.51888 | -53.78124 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64e71383-fd46-3b22-8bdd-c95d25384832 | -3.7415 | -51.84163 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 819ee529-5c30-3b63-b0dd-a46c53feba06 | -2.80474 | -53.04727 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96b9e1dc-b2e0-384a-bb6e-3e4c07721db5 | -3.27376 | -50.62074 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2b31dc7-4e54-3074-8f50-c329ff758073 | -3.10837 | -53.10308 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c7a1b21-053c-3662-8b6c-09671bda40c9 | -2.91051 | -51.58428 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a52a059-9d91-3ab7-a34b-07ec62fccf34 | -2.62355 | -54.19226 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 818e838e-a375-32bf-9932-c91d81405f03 | -5.51524 | -46.2604 | 2024-11-28 05:18:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bca614d5-b6c1-350e-a616-489bfbcdddaa | -2.80243 | -51.58376 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bafa120d-ea03-3f7d-aca0-edbf8957a9cb | -3.3495 | -53.73627 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf901c7d-8ceb-340e-a257-bd3e55b16cfb | -4.15707 | -54.81226 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa808d7a-cf08-347a-a7e1-f41f25cfd032 | -2.58056 | -56.42404 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf5f1c81-3fc5-3fe3-b442-5bdd39dd04f9 | -2.65781 | -49.50732 | 2024-11-28 05:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e57b75ae-7de9-3ee2-b8f5-5ef9fa7b6ec1 | -2.72954 | -54.13376 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6397e492-b103-30e0-9a52-d8312f697cce | -3.24369 | -53.28851 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96a4a2c4-e692-3562-9076-655587bb8a72 | -3.96911 | -50.19151 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0202e517-43b6-333e-b1bd-25d860892777 | -4.0064 | -54.3361 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 378864b7-7d9e-31ab-8316-13402aa79297 | -3.10677 | -53.25636 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9708d36-39ad-3c7b-9844-a039c2f02af8 | -2.27083 | -52.83979 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a6145ab-f7de-3b5d-9ca3-55ac20bbbf72 | -2.92617 | -51.4494 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d1523bd-ef7f-35b2-a80a-d6008da5c1c3 | -3.69204 | -51.37115 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc297d29-d8e0-33fd-9082-7e728fcc7ec1 | -3.37408 | -50.82566 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README82.md)
