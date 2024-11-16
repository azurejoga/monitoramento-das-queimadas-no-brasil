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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1015d447-e5d8-347d-9a40-cc76e3730f8f | -2.6325 | -48.4775 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 27015028-5647-35bc-a709-7ed7d9ccb101 | -2.6509 | -48.4985 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4b1d2c82-f668-3b26-9b91-f15b8de4cb4d | -3.5851 | -50.5255 | 2024-11-16 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 28ce9faf-163b-333a-a7d7-9b3ae8e131c0 | -6.1413 | -35.1565 | 2024-11-16 00:20:00 | GOES-16 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 07bbd147-388b-3040-9327-84536955722f | -2.7986 | -48.5586 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ec544a14-0af3-33a0-85e6-c6dbd3d9435b | -17.5688 | -57.4529 | 2024-11-16 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 5f4cd1a5-77e9-3ce1-aa55-d31ab074674d | -2.1379 | -53.7043 | 2024-11-16 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 8f1a3bea-cafd-3fe9-a8d3-5160f9d69a69 | -3.7685 | -50.7908 | 2024-11-16 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1cfccdac-f244-3e9c-a0d3-4eee26082cf3 | -2.1563 | -53.6838 | 2024-11-16 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| dd97c0ac-ea34-3c45-92f1-cc4ed85a135a | -2.78 | -48.5806 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 4abeec8b-e7c5-3e7b-85d4-a7ccaddada25 | -3.1272 | -54.5464 | 2024-11-16 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d1c3ee25-af48-3504-9bbb-1740293e06ff | -4.9971 | -44.3149 | 2024-11-16 00:20:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 395fadcd-1fea-358b-bb76-bce8c2e58525 | -2.651 | -48.477 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| c364f3ad-799c-3dde-9c10-84c4cde9ba41 | -17.5885 | -57.4506 | 2024-11-16 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 449fcdd5-f309-3ea7-b18a-9fe3ca48af52 | -3.2411 | -53.5181 | 2024-11-16 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 56afaa1a-4e51-38c0-8a84-b1a32c251a95 | -3.6255 | -53.9912 | 2024-11-16 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| dce0a9db-a242-33ea-a93d-6435858699f2 | -3.5043 | -44.419 | 2024-11-16 00:20:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5d24907c-c48c-31a2-90ad-a9a5ac484d5a | -3.1457 | -54.5059 | 2024-11-16 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5e1106ed-640a-3c56-beb5-077eef50e3d0 | -17.5882 | -57.4711 | 2024-11-16 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 5a2cc89c-50cb-3175-a75c-e5710c8cd72c | -3.1273 | -54.5264 | 2024-11-16 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 2cef7158-69f5-3665-a312-c7fecfeff491 | -2.1562 | -53.7241 | 2024-11-16 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| b6f73aff-7ce5-31c9-bfd9-a7830e7fc1c2 | -3.5439 | -51.4844 | 2024-11-16 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bd983ee4-9157-367a-955c-58690e8bbe8f | -6.14886 | -35.17113 | 2024-11-16 00:22:00 | TERRA_M-M | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 450.4 |
| d9011c2d-48b8-302c-8011-ba7198976441 | -6.50062 | -39.71132 | 2024-11-16 00:22:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c461b591-a9d7-3f6b-b861-06c019d49a58 | -6.9407 | -40.02528 | 2024-11-16 00:22:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1974a475-e32e-3659-bf88-f063629172ed | -6.99121 | -39.66547 | 2024-11-16 00:22:00 | TERRA_M-M | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 44507965-b29a-34af-a32a-3a637454a483 | -6.14632 | -35.15432 | 2024-11-16 00:22:00 | TERRA_M-M | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 42fe4c2f-5fb5-3b70-a107-42473b1a4961 | -8.28266 | -45.98388 | 2024-11-16 00:22:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d4827ae4-cf74-3857-9054-f56746dff377 | -7.04532 | -41.04937 | 2024-11-16 00:22:00 | TERRA_M-M | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7fb0fc0e-8bdb-3e89-9ee8-01faab83d3d5 | -9.33677 | -44.35559 | 2024-11-16 00:22:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5da44389-38d3-3c98-ab9d-e9b9b4a8adf8 | -6.86929 | -39.06657 | 2024-11-16 00:22:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7c7be484-fa1b-32db-a0b7-69c497e57b2b | -6.6657 | -40.30651 | 2024-11-16 00:22:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2cce3e37-8836-3f3e-b91a-c9eef3875d1f | -7.58489 | -39.04264 | 2024-11-16 00:22:00 | TERRA_M-M | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4805111a-8708-3d40-ad58-030aa13dc9ce | -7.18203 | -39.12576 | 2024-11-16 00:22:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9a27a859-1814-3344-b816-79b0da35001a | -6.50954 | -39.71003 | 2024-11-16 00:22:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7f7dd707-7979-3390-a7f1-6c74a8bcd295 | -7.45899 | -38.42113 | 2024-11-16 00:22:00 | TERRA_M-M | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 968f7425-deab-3361-a92b-4bcaad5f66af | -7.06923 | -35.85409 | 2024-11-16 00:22:00 | TERRA_M-M | SÃO SEBASTIÃO DE LAGOA DE ROÇA | PARAÍBA | Brasil | 2515104 | 25 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 105ec107-4c48-3b87-8246-0ec86d6e8d23 | -10.83714 | -44.45956 | 2024-11-16 00:22:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1e1d42fa-156c-3445-aed6-cc42fbc0818f | -6.81048 | -39.29852 | 2024-11-16 00:22:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f0b46d00-6c09-3c34-8655-da95c43b38f3 | -6.13704 | -35.17296 | 2024-11-16 00:22:00 | TERRA_M-M | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 70f15460-4217-3ada-b11d-ee17d18c38e3 | -8.2804 | -45.96589 | 2024-11-16 00:22:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 648c41c4-2bf9-38ed-8a56-bb571d8e797a | -7.39719 | -40.39693 | 2024-11-16 00:22:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 94780706-f3a6-36bb-a2a8-b974c5c1a613 | -9.39492 | -40.32175 | 2024-11-16 00:22:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 59dcecc7-1811-36a4-afe8-4478098cee83 | -7.4048 | -40.38681 | 2024-11-16 00:22:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 05b7deda-7b0c-3a89-9be7-f43923a7c049 | -11.87205 | -38.34709 | 2024-11-16 00:22:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f7083b18-3a68-33e4-8d6a-28400c7556ca | -8.52345 | -40.74494 | 2024-11-16 00:22:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 496ba46e-34d9-3460-bdc8-f730fffe1022 | -6.86185 | -38.88561 | 2024-11-16 00:22:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 58a96373-0c2d-3c24-8414-d3fdc4f4f496 | -7.58619 | -39.05182 | 2024-11-16 00:22:00 | TERRA_M-M | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 28f7ffb1-0419-3ea8-8c73-d6476326a40b | -8.78839 | -35.65285 | 2024-11-16 00:22:00 | TERRA_M-M | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| beaff9b9-eb32-3bd7-ae8b-a74be58c40c4 | -8.74185 | -36.41994 | 2024-11-16 00:22:00 | TERRA_M-M | JUCATI | PERNAMBUCO | Brasil | 2608255 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 08ad2b55-4760-373c-9fc3-b34922e4b565 | -7.40603 | -40.39567 | 2024-11-16 00:22:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a4591652-6c56-39be-a7db-eeb6eda1fccf | -6.98132 | -38.88085 | 2024-11-16 00:22:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9fb6e69e-d09c-3a83-9d93-bce5599359e1 | -6.97712 | -38.47265 | 2024-11-16 00:22:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3cd2da00-a828-37ff-8eba-a27d0f5360c0 | -6.97998 | -38.87143 | 2024-11-16 00:22:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 3eafbafd-d6fe-317e-b79f-ec4ddeb03ed8 | -7.92379 | -39.55157 | 2024-11-16 00:22:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f78c6535-a163-3f7b-9201-72ed540167f8 | -6.66693 | -40.31538 | 2024-11-16 00:22:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 662c9f45-ce33-37c9-9b81-e22d8afffb09 | -7.45759 | -38.41135 | 2024-11-16 00:22:00 | TERRA_M-M | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1743453c-48ed-3bb1-a245-101e64854db4 | -6.97856 | -38.48251 | 2024-11-16 00:22:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 767f9564-f4dc-3558-b1fa-e3eaed6036f3 | -6.67187 | -40.3508 | 2024-11-16 00:22:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8f262029-9435-33c8-ab42-a7c094586da5 | -10.66958 | -44.49194 | 2024-11-16 00:22:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4b25bfa0-2bfd-37a2-84c5-0dd712712886 | -8.74006 | -36.40797 | 2024-11-16 00:22:00 | TERRA_M-M | JUPI | PERNAMBUCO | Brasil | 2608305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 7e43f412-30cd-3cc3-b353-4b599f817d84 | -10.5444 | -44.6765 | 2024-11-16 00:22:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 1a1c2182-f258-3d1e-a113-155134dd1518 | -6.86795 | -39.05724 | 2024-11-16 00:22:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 7de56226-1f07-3cf2-a475-4d191ff69d05 | -4.33111 | -43.81654 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f7ffb3f3-7b4b-3cd8-b92a-a3170c68ec7f | -4.32963 | -43.80565 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 919b179c-c63e-3f20-9650-9cb9e6919f4a | -2.5702 | -45.22303 | 2024-11-16 00:24:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0560f655-130d-3630-8c63-d13303bf3431 | -2.10105 | -46.5811 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 36e5388e-5cf7-359d-afe1-ec8073c5a20e | -3.7556 | -50.78325 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 8972d1ad-0674-3c60-93ea-8d1ee84cd990 | -3.72719 | -45.65189 | 2024-11-16 00:24:00 | TERRA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4ea346e4-8797-35c1-81ff-f5bf153f99f1 | -2.55419 | -46.88614 | 2024-11-16 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| e67c8ed6-e43e-358e-a166-27acdbf057ce | -5.93037 | -43.78785 | 2024-11-16 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e9d46548-db8a-34e1-864d-4ae989392c43 | -2.31843 | -45.43921 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b6fba1ea-c492-3fe0-b78d-b4441e8ef5a0 | -2.1418 | -46.55333 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 111f02c9-27ac-31a3-9d4e-fa0fef3175ff | -3.9645 | -44.04781 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 684e4127-4b55-3f06-b78d-4c201011ee09 | -4.15807 | -45.42831 | 2024-11-16 00:24:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5c744de3-6693-3a23-a3d2-12add074a9d5 | -4.00332 | -44.33755 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 512f1edb-cdc7-39b1-bfb5-79bb3e70ab35 | -1.23289 | -47.46021 | 2024-11-16 00:24:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f08be00b-0067-38a9-845b-916e8f09974e | -5.66817 | -35.64225 | 2024-11-16 00:24:00 | TERRA_M-M | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 5396dcbb-8370-35a8-be93-92fc7584ad4a | -3.92826 | -42.41415 | 2024-11-16 00:24:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ff4d8fa8-9495-3747-8ced-964073d878b8 | -2.69547 | -45.66146 | 2024-11-16 00:24:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 58372c3f-42cc-3d85-9672-1af3d90b4afd | -5.00778 | -37.54254 | 2024-11-16 00:24:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 32c02145-3a8c-36ba-9680-8aaba244ef1a | -4.55777 | -45.76432 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1d6d73c1-8bbf-359b-b892-407080b3718a | -0.96659 | -46.94121 | 2024-11-16 00:24:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 76335569-a482-3c24-b524-5f2f6cf229e0 | -3.72993 | -45.6602 | 2024-11-16 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 413c577d-bf0e-3c42-95a8-e39839b4691d | -4.00378 | -44.34291 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1e6dd7fb-fb8a-39be-b0b4-58f7a6ef6a3a | -5.72336 | -44.80951 | 2024-11-16 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| fda72c19-2b4a-321e-a858-e7b28a0ec8f9 | -2.64278 | -48.47429 | 2024-11-16 00:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| f8bc30e7-4e2b-37b2-8bb3-935586d36ada | -2.65277 | -48.49063 | 2024-11-16 00:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b2e227e9-4e3c-38b6-919e-efd4dd389a81 | -4.29623 | -48.06746 | 2024-11-16 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8c9e37dd-6d5c-325e-a895-f6e3c84e4067 | -4.39916 | -43.71329 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e3f3946-9ab3-3404-9ce4-64732854053b | -4.21986 | -47.21451 | 2024-11-16 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| ae23e65b-544c-3cfe-b06d-e69b705763d4 | -4.18596 | -45.64008 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 83b64594-7b93-3172-bc29-203ebb629fa3 | -1.52245 | -47.11841 | 2024-11-16 00:24:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 755d032d-9ad9-3529-b9b5-be07785c5d5f | -3.76515 | -43.24741 | 2024-11-16 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8aba11d7-d988-307c-8e3b-5a327b097042 | -4.28705 | -48.20739 | 2024-11-16 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a5425637-bed5-3e9d-918e-0eb452bc04e5 | -3.51437 | -44.42306 | 2024-11-16 00:24:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 198.0 |
| e98bb189-2142-3064-bc2a-b0ca888e5536 | -1.22966 | -47.46638 | 2024-11-16 00:24:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6263cd4b-827e-3e57-a1c4-053b0643b3b8 | -6.17018 | -41.17296 | 2024-11-16 00:24:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 373f3bc6-195d-32e1-a7ba-b36482ab45db | -5.331 | -40.90395 | 2024-11-16 00:24:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 027a153c-fffb-3a81-b7cb-2b9318148a89 | -5.30202 | -40.89008 | 2024-11-16 00:24:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |


[Clique aqui para ver as próximas entradas](README3.md)
