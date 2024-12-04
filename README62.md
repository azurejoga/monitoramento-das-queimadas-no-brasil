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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd9f1a5d-b0fa-359d-a5cc-28c44275dce0 | -5.5695 | -45.1425 | 2024-12-04 07:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f5911283-3faf-31eb-8a66-4b3592ea5dff | -3.1269 | -54.6263 | 2024-12-04 08:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d54a247b-b0a8-3620-9011-8819903e354b | -1.7361 | -52.6162 | 2024-12-04 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f5215466-39f5-3dfa-8f92-8822bd9b7eef | -3.127 | -54.6063 | 2024-12-04 08:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 85626cdc-4509-3c84-8e8c-0f7fa0f893ad | -1.7545 | -52.6159 | 2024-12-04 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| aef01277-8623-3e3d-bee2-d04699f72243 | -3.1086 | -54.6268 | 2024-12-04 08:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 890ce227-20b0-3bd7-8b80-f55bbaea400e | -1.7544 | -52.6363 | 2024-12-04 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| bf517003-c56a-3398-bdd2-9d7790009a78 | -2.8197 | -53.0425 | 2024-12-04 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 435c06cd-0104-30fb-9d47-0768308be3c4 | -1.7728 | -52.636 | 2024-12-04 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2921acb7-c604-3eb6-8de7-2bbb2fa5927b | -2.8196 | -53.0629 | 2024-12-04 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5a611c48-628d-3818-a2df-6a11f2a0e30e | -3.259 | -53.659 | 2024-12-04 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1e3cb997-b24a-3dc1-9b43-1e69ddf8bd84 | -3.1269 | -54.6263 | 2024-12-04 08:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| bd9c7142-f657-3080-9601-de823d7a0ce7 | -3.259 | -53.659 | 2024-12-04 08:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e08232ae-5e73-39eb-8bf1-5502b718a2d4 | -3.1086 | -54.6268 | 2024-12-04 08:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 31381407-03d8-30e3-8f9a-41d302461f0f | -1.7729 | -52.6156 | 2024-12-04 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c14eac0a-2b5c-3ad4-829b-bf7575199eb9 | -1.7361 | -52.6162 | 2024-12-04 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f38f59d5-d3b6-3616-b2a2-d2d8bba2d0fe | -3.127 | -54.6063 | 2024-12-04 08:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b69aa1e7-79f7-3ea0-ae84-f1057e127a89 | -1.7545 | -52.6159 | 2024-12-04 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 6f55a437-9eef-3aaf-b30a-92ab89ee7480 | -2.8196 | -53.0629 | 2024-12-04 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d2ba3d20-0d99-3c82-9910-2bd4d325d349 | -2.8197 | -53.0425 | 2024-12-04 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c31256fc-0e2a-3bbd-8a86-a341b0548b23 | -1.7544 | -52.6363 | 2024-12-04 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 0aa2a5cc-718b-3a7d-ab1d-df0afb5e1bf8 | -1.7728 | -52.636 | 2024-12-04 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 16a50fa6-9498-3328-9b54-355a476529ee | -3.127 | -54.6063 | 2024-12-04 08:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1f497e8e-6396-3cce-8f88-4ff3f6488886 | -1.7728 | -52.636 | 2024-12-04 08:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 254b4bd5-b673-35eb-aa22-4a39baff3b74 | -2.8196 | -53.0629 | 2024-12-04 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7ddca880-763e-3e73-91ef-322a8af18298 | -3.1269 | -54.6263 | 2024-12-04 08:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2cadc5bb-e9c3-3788-aa1c-371724fdc4e2 | -3.259 | -53.659 | 2024-12-04 08:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 267ca463-e9d5-3ccb-b140-761eb040996c | -1.7544 | -52.6363 | 2024-12-04 08:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| cecdf5bc-57a7-3114-b433-b34b0a6d88c6 | -3.259 | -53.6388 | 2024-12-04 08:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 014420e0-c729-37ab-9c57-95cf425c2fa5 | -1.7545 | -52.6159 | 2024-12-04 08:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 5cd110ad-bf7d-319e-b1bb-36c7a27556c6 | -3.1086 | -54.6268 | 2024-12-04 08:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 7e16bc9c-a3df-30cf-aa5d-64069508c2c3 | -2.8196 | -53.0629 | 2024-12-04 08:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 19528f50-ddb3-37df-b446-5be15da726dc | -3.127 | -54.6063 | 2024-12-04 08:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3a85b20d-ec26-3005-8dbe-52be4f1a73aa | -1.7728 | -52.636 | 2024-12-04 08:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a5ef982f-9abb-367a-af0d-f89d689435ed | -2.8197 | -53.0425 | 2024-12-04 08:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c06fd9ea-4f29-34eb-8626-f24fcd2e41f0 | -3.1269 | -54.6263 | 2024-12-04 08:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ed831802-b00f-3373-9bb7-57b0865cb8a0 | -1.7545 | -52.6159 | 2024-12-04 08:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 573a8e11-103f-3411-a707-e9601e6cf434 | -1.7544 | -52.6363 | 2024-12-04 08:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b40a325a-f6de-3613-879d-df0af04069f9 | -3.1086 | -54.6268 | 2024-12-04 08:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3330d929-ed9a-3e5e-9ad4-35bc5806ced0 | -7.45 | -39.9 | 2024-12-04 12:00:00 | MSG-03 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | nan |


