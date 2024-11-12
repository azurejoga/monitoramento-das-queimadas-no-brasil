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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f12bd677-3db2-39ac-9896-b5c6e68a306f | -17.2543 | -57.4698 | 2024-11-12 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 8415022c-3ae5-370f-84b0-03d8c80f5edd | -17.2936 | -57.4652 | 2024-11-12 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| fbef8d83-efc5-392d-a849-a5728b93560f | -17.5872 | -57.5328 | 2024-11-12 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 6964d730-5fb9-3d12-b6df-f27aa8896c06 | -17.2737 | -57.488 | 2024-11-12 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| c0ca9e6f-7045-3738-a682-3b6442fa4bee | -17.5875 | -57.5122 | 2024-11-12 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 8727dc47-b9a5-393e-b0d0-19361a39990c | -17.254 | -57.4903 | 2024-11-12 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 5f481006-d64b-3037-a668-8042f28d57a7 | -15.9605 | -59.2885 | 2024-11-12 08:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 63f3f086-cec8-3f47-b2e3-98b62d06e6ce | -17.6066 | -57.551 | 2024-11-12 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 5e125c7b-aa99-3c6e-8b31-bd55ee913ba0 | -17.274 | -57.4675 | 2024-11-12 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| df399cb4-f738-37e2-9b9f-a333437c622e | -15.9602 | -59.3085 | 2024-11-12 08:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4fde2a8c-a04b-3db6-8156-a2c679f6fad0 | -17.2933 | -57.4857 | 2024-11-12 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 98d90cce-e4e1-3fea-bc76-4f8129f81512 | -17.274 | -57.4675 | 2024-11-12 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 17e2166c-4a65-3fe3-b633-96bdc3add08f | -17.2933 | -57.4857 | 2024-11-12 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 88bc720d-2b37-325d-8a7e-89a365339267 | -17.2936 | -57.4652 | 2024-11-12 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| e22f0571-eef9-3a95-a22f-2757eac1e7cf | -17.2737 | -57.488 | 2024-11-12 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 06236b6a-1d15-3aa7-8a46-be6ac54809c5 | -17.254 | -57.4903 | 2024-11-12 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 3f9394f7-89f3-3d35-8708-c3d0d5c75425 | -17.5875 | -57.5122 | 2024-11-12 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| f86b9b0c-e2f9-307f-b141-08e78f3e6e71 | -17.5872 | -57.5328 | 2024-11-12 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 19ff67fd-b513-3ab0-bb65-aa72e1b7e4cd | -17.6069 | -57.5304 | 2024-11-12 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 313c3a76-c35a-35bb-9fc7-cc9785f1b692 | -17.6066 | -57.551 | 2024-11-12 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| b0174c08-5ec9-381c-8f4c-5de07b2abd21 | -3.37679 | -40.62322 | 2024-11-12 11:44:00 | TERRA_M-M | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 143446dd-bba0-3d31-8671-9dcc6509a695 | -7.79876 | -37.16849 | 2024-11-12 11:44:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 37fcd6ce-3145-32a3-b971-5e3ab718bd6e | -5.6062 | -35.4053 | 2024-11-12 13:50:00 | GOES-16 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 101.3 |
| c3ec049c-b485-344d-9d9e-b988e52f0fbd | -3.6701 | -44.7303 | 2024-11-12 14:00:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 96072a11-7a6c-3220-822d-a0fa3b57d5ed | -16.7721 | -55.8188 | 2024-11-12 14:10:00 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |


