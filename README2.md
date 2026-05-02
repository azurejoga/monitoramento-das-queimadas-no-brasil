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
| 744a4a69-0d07-35e4-a56c-8f6937f04db9 | -10.9624 | -45.09 | 2026-05-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 07daec2d-0c96-338d-bb1e-192b63d604e4 | -12.3696 | -50.0459 | 2026-05-02 02:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| b999950a-01a2-3c4e-9426-3057190e0ade | -12.3887 | -50.0435 | 2026-05-02 02:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| cee2f18f-8c42-3ce8-ae71-eb932db036ad | -12.37 | -50.0242 | 2026-05-02 02:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f77c693a-821b-3f5d-9803-2d0466a0c163 | -10.9819 | -45.0643 | 2026-05-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 050d95cb-e49d-3259-a961-6af80662b4db | -10.9815 | -45.0874 | 2026-05-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 24870fe3-10ce-3946-aa13-61633a10e754 | -12.3891 | -50.0218 | 2026-05-02 02:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f0360383-9734-3d47-bfc5-2be0cf5ba91d | -10.9815 | -45.0874 | 2026-05-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| e0c18c7c-cf8e-3502-95b0-ba45977d5ca5 | -10.9819 | -45.0643 | 2026-05-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| fcc499ab-1bb5-387f-88fa-120b9c09b5d2 | -12.37 | -50.0242 | 2026-05-02 02:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 3864d9f8-bd95-3c5a-a0ac-7919b89b8cf5 | -12.3696 | -50.0459 | 2026-05-02 02:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 0a3277fb-4e99-39df-8809-ec29c3ed5e27 | -10.9624 | -45.09 | 2026-05-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c543fd97-9feb-3861-b0ee-619a9e448675 | -12.3887 | -50.0435 | 2026-05-02 02:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b24e2059-9dd3-39b0-b164-5bb65918e37c | -12.37 | -50.0242 | 2026-05-02 02:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 43816808-1529-3493-b646-4fe9ab798afb | -12.3887 | -50.0435 | 2026-05-02 02:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ba4a9d29-c4da-3544-bbab-9b590120138a | -12.3696 | -50.0459 | 2026-05-02 02:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 188.0 |
| fd553497-e4e8-3a86-bb32-9c930b4e62db | -10.9624 | -45.09 | 2026-05-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 128d48bb-8ece-37a2-95fa-fca1f4d532da | -10.9815 | -45.0874 | 2026-05-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3fb7018c-95fe-3baf-86b3-0b18d9ae5ecc | -10.9819 | -45.0643 | 2026-05-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| eddbc9b2-dc09-32b8-8bcb-8352237a500c | -12.3887 | -50.0435 | 2026-05-02 02:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 630dada2-1dc4-3ff5-844d-af6fb9666c86 | -12.37 | -50.0242 | 2026-05-02 02:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 44db0ca2-0f1e-3f63-b714-3a4af801374b | -12.3891 | -50.0218 | 2026-05-02 02:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2773d0af-27d5-36a5-a14d-7cb7224f39eb | -12.3696 | -50.0459 | 2026-05-02 02:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| a2883c44-6c4a-3e2e-90a8-f021f582c48a | -10.9815 | -45.0874 | 2026-05-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6a02170f-fd7b-3e8a-a335-96e634037f55 | -10.9624 | -45.09 | 2026-05-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 98527499-b648-30c7-851b-2e3bcb5ea6a6 | -12.3891 | -50.0218 | 2026-05-02 02:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| adcc1719-1fc9-3978-992f-883d4f4054c8 | -10.9819 | -45.0643 | 2026-05-02 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 82e13d28-d25c-3d9a-9fb3-c09eeb313fb2 | -12.3696 | -50.0459 | 2026-05-02 02:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 9dd82573-7c0b-36d5-90e9-5fd9ced8e001 | -12.37 | -50.0242 | 2026-05-02 02:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8a08d48e-a9fc-3177-9d1c-93028671e787 | -12.3887 | -50.0435 | 2026-05-02 02:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| fe1e9f49-fb4d-387e-af1e-20d8ade0694d | -10.9815 | -45.0874 | 2026-05-02 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| ea353b14-2b31-3deb-88e2-d276e0e832d4 | -10.9624 | -45.09 | 2026-05-02 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 743fdc3b-4723-35fe-97b0-371c2614f2b3 | -12.37 | -50.0242 | 2026-05-02 03:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5ae2f49e-332f-382d-9aeb-d3d8c320ef8a | -12.3887 | -50.0435 | 2026-05-02 03:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 15943339-1186-330c-b6b2-f49745eb3420 | -10.9624 | -45.09 | 2026-05-02 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6bf72e92-26b8-3690-9883-8263926ed844 | -10.9819 | -45.0643 | 2026-05-02 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d9cd5c5f-2bb6-31a8-af45-03e041363d3a | -10.9815 | -45.0874 | 2026-05-02 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 91c2b9a7-42eb-3414-b087-c64b15941f86 | -12.3891 | -50.0218 | 2026-05-02 03:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 69419d5d-deec-34f4-9a27-837b3118efbb | -12.3696 | -50.0459 | 2026-05-02 03:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 764bce05-e062-398c-880b-c9d67054ce1d | -10.9819 | -45.0643 | 2026-05-02 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 60b87504-61fd-3022-9b2d-f4819d498943 | -12.3887 | -50.0435 | 2026-05-02 03:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7ea96b50-867e-37c4-b46c-2b1f1d3e1703 | -12.37 | -50.0242 | 2026-05-02 03:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 562fbff1-f63b-3835-afb8-fea6135c0956 | -12.3696 | -50.0459 | 2026-05-02 03:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 0215ea31-3f5c-36ca-991f-03c19cad63cd | -10.9815 | -45.0874 | 2026-05-02 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a8ab1060-38bb-3152-ab62-f5305e8da69c | -12.3891 | -50.0218 | 2026-05-02 03:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3459a9b2-0199-31cb-8d23-b2e29ec32091 | -12.3696 | -50.0459 | 2026-05-02 03:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 573d33bf-5feb-33df-8fc7-733bd22da841 | -12.3887 | -50.0435 | 2026-05-02 03:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0350a1a7-b748-3735-a2d3-29bae1925735 | -10.9819 | -45.0643 | 2026-05-02 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 554ad07b-60dc-3bbe-b6cf-2db35628a977 | -12.37 | -50.0242 | 2026-05-02 03:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 84082fb4-dab0-32a6-82ad-6ac6a5f3b65a | -10.9815 | -45.0874 | 2026-05-02 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 337ff58b-f28a-3a55-8600-cbe278f20278 | -12.3887 | -50.0435 | 2026-05-02 03:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e10c3f0c-9259-3fee-8e9e-4cd8eebe2a56 | -12.3696 | -50.0459 | 2026-05-02 03:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 0d82f89e-bc98-3a91-a530-5373d1a4232c | -12.3891 | -50.0218 | 2026-05-02 03:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e05bd27c-d44d-31cf-8d5f-d682b5396c65 | -12.37 | -50.0242 | 2026-05-02 03:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c5bc9173-8001-3a0e-a12f-1b5eeced2c6d | -10.9815 | -45.0874 | 2026-05-02 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 2a17fe08-173e-32a6-86f7-b815efc7c1c8 | -10.9815 | -45.0874 | 2026-05-02 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 860e5306-de2a-35b2-a9ad-63b361f7ff38 | -12.3696 | -50.0459 | 2026-05-02 03:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| aadb84fc-9c8b-32de-ba58-53e05b032a16 | -12.3891 | -50.0218 | 2026-05-02 03:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bbbaf902-e591-3ccf-9613-5836f3c2ca8d | -12.3887 | -50.0435 | 2026-05-02 03:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ede50665-cc52-3d47-b9a2-efd72eb4be6a | -12.37 | -50.0242 | 2026-05-02 03:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c871b682-21db-33d6-8a85-d83818108353 | -10.97448 | -45.09119 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ba72c5f-70b8-373c-bb3c-479c4ac051f4 | -13.78232 | -44.10404 | 2026-05-02 03:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e616ea2-e6de-3b21-bca1-c3cf9ef5428b | -13.78047 | -44.10217 | 2026-05-02 03:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c73e702-34e0-3be6-a5f0-bba16c66b270 | -13.67934 | -44.29265 | 2026-05-02 03:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de1b1d2f-9b3d-34ef-a70f-ff3cf271c71e | -10.9881 | -45.07729 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 783fc893-15e1-3c09-8c66-446194080da2 | -13.80976 | -43.64994 | 2026-05-02 03:40:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eb9603b-1827-3704-b457-b5b4d6e419c0 | -11.04642 | -44.69857 | 2026-05-02 03:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1082381-4cc5-3d05-b104-2a239aed1aa6 | -10.97586 | -45.07913 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ad48520b-6e4a-35a7-a587-7a5179ebf471 | -10.98237 | -45.07622 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cdb6e7f1-de36-3d3d-9d03-d8dd7ce9403d | -10.97509 | -45.08316 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b3e972e-95b7-3581-bed8-63febdc7ac2e | -10.96871 | -45.09024 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 63ead9a8-7446-37c4-a6c2-76e284ac8491 | -10.96282 | -45.08514 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7efdf7d4-4818-3143-b1e0-2ac301c0c7b0 | -10.98837 | -45.08118 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b423d413-bf95-31a6-b5eb-85836382a382 | -10.98025 | -45.09214 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efd2af22-0601-36ef-82fd-37bab39fb9f9 | -10.96856 | -45.08622 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9eb205f6-ccba-3291-b996-8dfa4375e0cf | -10.97609 | -45.08312 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2db000cd-53df-3988-a3c6-e1cbb156ecb7 | -10.98506 | -45.09327 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4ee3aca-9a13-3869-9a43-939384c5dfe6 | -12.27916 | -44.62976 | 2026-05-02 03:40:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e81cc14c-b403-32c5-a476-5bde89e6a73c | -10.98263 | -45.08015 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fa322039-ce29-3f04-83d1-afa2f973f4e6 | -10.986 | -45.09319 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aeb1c85a-a761-3d91-b905-eddcd41e4012 | -10.98184 | -45.08411 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 584fbb5e-619c-3bb5-8a06-b092960e62cd | -10.97432 | -45.0872 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93dc550e-bd0c-3065-bc4a-36bbac3f4830 | -10.70894 | -46.35944 | 2026-05-02 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e9105bc-ec0c-3a6c-ad8e-528508d47cad | -12.27987 | -44.62619 | 2026-05-02 03:40:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96837a0a-1f15-3978-a6ab-82f98162f6ef | -10.97663 | -45.07514 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ea5a7f21-b44f-3a4b-857f-8ffc36f0fe50 | -13.68457 | -44.29351 | 2026-05-02 03:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8981d7f8-e282-3623-82d4-64ad2a9544f0 | -12.92217 | -42.42908 | 2026-05-02 03:40:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| acad8825-28ce-3a83-aa54-65c2ac0624e0 | -10.98009 | -45.08817 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9450f0a4-3e7e-3631-9829-45d6e46f5395 | -10.98518 | -45.09729 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0607ca53-9d43-351c-8ac3-272bb2e74bb7 | -10.96791 | -45.09427 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 057c10e8-31eb-3e11-a107-9a63d7fd116d | -10.96709 | -45.09838 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fe6ac547-4512-3400-b19e-196b4b697b59 | -11.55481 | -48.27216 | 2026-05-02 03:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 954020c3-53ec-36a0-8b12-2763ce279e08 | -10.97528 | -45.08715 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3eead634-5599-3882-81e2-f1a0618561e1 | -10.98428 | -45.09738 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 990d24fd-aa9c-3cba-a2a9-22b4e4b6c9af | -11.55617 | -48.26573 | 2026-05-02 03:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76b51ef0-134f-3c68-ad51-f7d130f7747e | -10.98341 | -45.07621 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a42b4331-c507-3b25-b5ae-b5381479c43b | -10.97355 | -45.09125 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a1eb466-a789-37d8-8ec1-db7818180c05 | -13.7795 | -43.2431 | 2026-05-02 03:40:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03480f83-f940-3258-a384-e802d34f8e8f | -15.58258 | -46.80756 | 2026-05-02 03:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aac8963-6bbe-3fc0-8a82-a0e798fcd6db | -15.58168 | -46.81183 | 2026-05-02 03:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
