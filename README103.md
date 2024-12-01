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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4264ebeb-7c1c-3d26-9de0-541f89d3fa90 | -4.8711 | -41.3157 | 2024-12-01 14:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| bf7ba54c-ea3a-3245-bf40-c7cddd338c56 | -4.91 | -41.32 | 2024-12-01 14:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 250ee124-5aa9-322c-aad2-a29951b2cd81 | -4.91 | -41.36 | 2024-12-01 14:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17b2c9f1-be0b-362a-b571-55bf00661db9 | -4.88 | -41.32 | 2024-12-01 14:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0afd4ad-4ba9-32e8-969c-fb8fff5f4e3a | -4.88 | -41.36 | 2024-12-01 14:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1a7f2f36-39ae-3a82-baba-1f5fdcaef5fa | -4.8711 | -41.3157 | 2024-12-01 14:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 66158ecd-5b0c-336e-b160-686b26c3df8c | -4.5375 | -43.304 | 2024-12-01 14:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4ed1b545-d9aa-3421-aa0f-ed96b52e5d2a | -4.8901 | -41.2902 | 2024-12-01 14:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 69b4ccd9-2e1f-37b4-b9ff-4d249fe7369b | -10.667 | -44.5067 | 2024-12-01 14:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 90e99033-36dd-30e5-a72e-5b732a423e22 | -4.5562 | -43.3028 | 2024-12-01 14:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d0d3517e-742d-3d20-a500-e576d720cb2b | -4.8899 | -41.3143 | 2024-12-01 14:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 255.0 |
| 349fa7b7-6463-3741-88bb-4c8d56fdbc6a | -4.8713 | -41.2915 | 2024-12-01 14:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| eea94d62-f9b7-3fe8-bdc8-4a293d8bc3d7 | -0.377 | -51.5419 | 2024-12-01 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.9 |
| bd15e491-de25-370b-ac30-13b71b38ea51 | -4.8901 | -41.2902 | 2024-12-01 14:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| aa352d5f-4df1-3e0f-9979-affaa5fea996 | -4.8899 | -41.3143 | 2024-12-01 14:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 250.9 |
| ae5ac62c-945b-3782-aad5-4ae69a591122 | -4.8713 | -41.2915 | 2024-12-01 14:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| b37cf351-89d8-3f4b-9a70-becfcd03bb48 | -10.2638 | -42.3701 | 2024-12-01 14:20:00 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 27f5714c-72d0-30d3-823c-abf2639df338 | -4.8711 | -41.3157 | 2024-12-01 14:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| bc7abb35-9237-3a0b-8bea-d74e9ac84e7c | -5.2698 | -42.9752 | 2024-12-01 14:30:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 38616b6b-eb04-3cf8-bad6-ba5d8e48ad36 | -4.8713 | -41.2915 | 2024-12-01 14:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| c80f32fe-5c2b-3747-824b-cea4954f17f1 | -4.0776 | -42.2032 | 2024-12-01 14:30:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| c6321bb2-83b1-38bc-8ea6-a383cc8354b2 | -10.6483 | -44.4861 | 2024-12-01 14:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fd162149-9e93-33c1-8db4-ce07126d8346 | -10.2638 | -42.3701 | 2024-12-01 14:30:00 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 72ea0f34-906c-3f34-b78a-0c6aaf8aa956 | -4.8711 | -41.3157 | 2024-12-01 14:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| ca12424f-2dbd-33f8-9cfd-fb5cf6115d2b | -4.8901 | -41.2902 | 2024-12-01 14:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |


