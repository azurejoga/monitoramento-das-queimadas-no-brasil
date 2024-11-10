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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43f2a13f-8304-311e-88cb-36a4239821fa | -3.1422 | -50.4562 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5cad7a85-198e-388b-b7ed-08396089f44a | -3.1238 | -50.4568 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 55108965-802b-3a65-9528-f7762ff19330 | -17.59 | -57.51 | 2024-11-10 07:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 138a44fb-5c45-3e34-8a8e-6617ecda7ee2 | -3.1422 | -50.4562 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3dd73a13-20e7-314e-b9e8-b1a224f99975 | -3.2584 | -45.1783 | 2024-11-10 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2d8bf9b4-f36e-3217-9b38-df028f86c6e7 | -3.2352 | -50.3065 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| f29d45d9-440d-32b6-a9f5-b240d02e5bb9 | -3.2168 | -50.2861 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f6e4cd18-c329-3447-933a-efbb26d6f975 | -3.2398 | -45.1791 | 2024-11-10 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| d8213fb6-d197-3eec-8a84-412fde1f459d | -2.0953 | -48.8338 | 2024-11-10 07:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0ca96a04-8fdb-38fd-a40a-b1d9d5dcfc15 | -2.7587 | -49.3497 | 2024-11-10 07:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ff851ba4-3465-3c67-adbd-4567d1a436b4 | -3.2536 | -50.3059 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 71a976e2-8c04-3606-8bbb-7aff71f5be6f | -3.2352 | -50.2855 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 316275f0-64af-3cd6-9ebc-d32d9115a3e6 | -1.5347 | -52.2104 | 2024-11-10 07:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ce5f16ef-c391-3cf7-8dc1-a929a6adb4b7 | -3.2353 | -50.2645 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 44c1e193-c151-3119-aa20-b4545b77141e | -2.931 | -52.7753 | 2024-11-10 07:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2a9cfdcb-0cb0-3aad-8add-1c8a1e433d90 | -2.7772 | -49.3492 | 2024-11-10 07:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a4c28158-3982-3345-a2ee-f8ca4640ced1 | -3.1239 | -50.4358 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c394de64-3bb7-3fbd-af79-cd88014758e1 | -3.1423 | -50.4352 | 2024-11-10 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 0bea2df1-9d48-3cfc-a249-2502ed64a77e | -2.0954 | -48.8125 | 2024-11-10 07:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| be74beb4-e782-3cd5-aca8-0753ff0e0c1c | -2.7587 | -49.3497 | 2024-11-10 07:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 626e482f-66c3-39b6-9f50-c7cc97a32a4d | -2.0953 | -48.8338 | 2024-11-10 07:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cd53bbe0-ea13-3595-a74d-49342dd49ad0 | -2.7772 | -49.3492 | 2024-11-10 07:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| cf7ee1ee-a5d5-3fd2-94c9-f9321dda3d0a | -2.0953 | -48.8338 | 2024-11-10 07:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7799ce6d-07b7-38d7-b174-b4ab9226a811 | -1.5347 | -52.2104 | 2024-11-10 07:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 83fa31f6-c779-3908-98c8-f19c2ef234a1 | -17.6073 | -57.5099 | 2024-11-10 07:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 335.2 |
| 556f074f-6967-3ae4-a3b1-c72976795615 | -17.6266 | -57.5281 | 2024-11-10 07:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.0 |
| a35aa15a-b453-3208-9d77-31a05abb9e66 | -17.6069 | -57.5304 | 2024-11-10 07:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 332.1 |
| a6937034-b312-3109-9a14-0a7a8295670d | -17.627 | -57.5075 | 2024-11-10 07:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 74ad32c1-529e-311d-a421-c7c36a5f551f | -17.2933 | -57.4857 | 2024-11-10 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 395ce704-9741-37c0-b861-ab0606d241c9 | -1.476 | -54.3166 | 2024-11-10 07:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 94da98b3-6c41-3278-9ec1-dee3313a87ec | -17.6266 | -57.5281 | 2024-11-10 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 157.7 |
| f531d2aa-0adf-3712-8acb-9e98cf9e7759 | -1.4576 | -54.3168 | 2024-11-10 07:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 525d92b2-26ec-3251-8fc2-a10122ba3a7c | -17.627 | -57.5075 | 2024-11-10 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.5 |
| 249ef005-0038-3096-af01-00cca2d16617 | -17.5872 | -57.5328 | 2024-11-10 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| b03b9657-46ce-34e8-be25-d9032fb01002 | -17.6069 | -57.5304 | 2024-11-10 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 380.9 |
| e1cbc77b-4376-3df3-b602-642ea7a3662b | -17.6073 | -57.5099 | 2024-11-10 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 344.5 |
| a7571541-9efb-3921-b49a-7004242e6451 | -1.5299 | -54.9941 | 2024-11-10 08:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| da524c94-299e-3636-a4a7-376483d75eaf | -17.5872 | -57.5328 | 2024-11-10 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 8a52ffd2-0fe5-3cd9-98eb-7d447a62c9af | -17.2933 | -57.4857 | 2024-11-10 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 41eb0669-3eab-3526-9ed7-db3872f0ba22 | -17.6073 | -57.5099 | 2024-11-10 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 369.6 |
| 2fcddd96-7d6a-3001-aee6-f964fe40f90d | -17.6266 | -57.5281 | 2024-11-10 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.5 |
| 051f5b1d-5663-3d04-8d73-3a30c6b62645 | -17.627 | -57.5075 | 2024-11-10 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.4 |
| 2c520166-0967-3e96-867e-f7dd6ec949af | -17.6069 | -57.5304 | 2024-11-10 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 469.4 |
| 851cfc29-4859-3310-90e1-251832f2e73d | -17.59 | -57.51 | 2024-11-10 08:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b65cc38-a7a2-350c-9df6-bfe3a43a6dc1 | -17.627 | -57.5075 | 2024-11-10 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| f5783f6c-9c15-37df-997f-1016358f1e0f | -1.5299 | -54.9941 | 2024-11-10 08:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ac804f43-df7e-33af-854b-866a5f5173a6 | -17.5872 | -57.5328 | 2024-11-10 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 1f10cf9b-ebf5-36cf-a76c-00bfdb11c6c5 | -17.2933 | -57.4857 | 2024-11-10 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 5a3ed0b9-2a67-3a45-8e43-48808f5ca840 | -17.5875 | -57.5122 | 2024-11-10 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| e5fbc5e9-90e2-3271-b0b6-f62c26830eb8 | -17.6266 | -57.5281 | 2024-11-10 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.6 |
| 09efd8e9-9302-32bb-a69f-2101bb562bdf | -17.6069 | -57.5304 | 2024-11-10 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 482.7 |
| 82c7020e-33ab-3565-aadd-1ca6d0280a51 | -17.6073 | -57.5099 | 2024-11-10 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 385.2 |
| 6344665b-33aa-3910-8f22-baba491476bc | -17.5872 | -57.5328 | 2024-11-10 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 214f84b7-2d1f-376b-99b7-a1663987b5e6 | -17.6073 | -57.5099 | 2024-11-10 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 413.4 |
| 8cadbefd-7196-3735-86fa-adeaeb4cf583 | -17.6069 | -57.5304 | 2024-11-10 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 456.2 |
| 27ebb147-10ec-3c66-9e50-f73ef6df7921 | -17.5875 | -57.5122 | 2024-11-10 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 743f0d8c-3087-389f-a088-ef88d748e802 | -17.627 | -57.5075 | 2024-11-10 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 1ac1bed6-64be-32ca-be02-691fb7b0209b | -17.2933 | -57.4857 | 2024-11-10 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| bed1df94-0dc9-3882-8cb6-f5dd40c04e18 | -17.6266 | -57.5281 | 2024-11-10 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.1 |
| 08f81349-c75a-3153-aa13-12ce7ada768a | -1.5299 | -54.9941 | 2024-11-10 08:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5afea4ff-7e8f-3de3-98ac-c6383732a9cd | -17.6266 | -57.5281 | 2024-11-10 09:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 71ac5b66-5f56-3ab0-a1e1-cef9fdc0d561 | -17.627 | -57.5075 | 2024-11-10 09:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| f5e18e78-8f67-3857-b702-83fb9846d089 | -17.5872 | -57.5328 | 2024-11-10 09:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| d841ffb0-3da5-3c43-9f3b-88034b17ab44 | -17.6069 | -57.5304 | 2024-11-10 09:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 229.9 |
| fa768606-6bd4-3780-8cc6-7522c238babb | -17.6073 | -57.5099 | 2024-11-10 09:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 202.0 |
| 942156fb-da26-300c-95f2-ff18d660c0c2 | -17.6073 | -57.5099 | 2024-11-10 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 221.0 |
| 9762618e-750c-3624-9eb6-9ffd3acbb1a0 | -17.6266 | -57.5281 | 2024-11-10 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| f2a58ffd-b373-352a-8bdb-4846cfb15210 | -17.6069 | -57.5304 | 2024-11-10 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 273.5 |
| f683159f-54d5-3421-8556-7a27cf0979fa | -17.6073 | -57.5099 | 2024-11-10 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.9 |
| 2a59652d-f348-3f04-9aa0-7988f48bd30b | -17.6266 | -57.5281 | 2024-11-10 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| f0586968-8bb1-394c-93be-8e105c66e521 | -17.627 | -57.5075 | 2024-11-10 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| dc9d7d6f-638b-3e89-ac4e-cb13a1aa374f | -17.6069 | -57.5304 | 2024-11-10 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 213.3 |
| 5a2b72a0-caed-328a-8370-a8b3385bb7a2 | -17.6073 | -57.5099 | 2024-11-10 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 198.8 |
| c02379dc-6382-3505-991a-97b5e55163c8 | -17.6266 | -57.5281 | 2024-11-10 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.4 |
| 39f4bf03-59a5-369c-a67a-081b9c34b2ea | -17.6069 | -57.5304 | 2024-11-10 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 209.7 |
| d32fec75-be98-3311-94ad-a6c4eba40e8b | -17.627 | -57.5075 | 2024-11-10 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 3ed99c94-298c-35e6-8d27-1992d86e47ca | -17.627 | -57.5075 | 2024-11-10 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| 42276f12-c852-3e99-a67a-8b62da1eb600 | -17.6266 | -57.5281 | 2024-11-10 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| c6738179-6a10-3e9c-b577-08a7d8e2fb07 | -17.6073 | -57.5099 | 2024-11-10 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 206.3 |
| 799db451-1867-3506-b04b-8f6ceba1970f | -17.6069 | -57.5304 | 2024-11-10 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 235.3 |
| a2b6c879-c5ad-3152-a794-0714cf75851f | -17.6069 | -57.5304 | 2024-11-10 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 241.4 |
| 68988762-b015-392b-9a65-dc85d141da81 | -17.6266 | -57.5281 | 2024-11-10 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| d04e70ae-ffd4-3174-83ed-a88cdd1a23f6 | -17.6073 | -57.5099 | 2024-11-10 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 208.7 |
| 5e7c7b85-fe06-3ae1-a207-a7fcbefc2e1d | -6.16 | -42.58 | 2024-11-10 10:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| adf45a6a-c999-3d48-9e4f-d0b4680d5459 | -6.13 | -42.57 | 2024-11-10 10:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd9dfdfc-c983-3fdf-a754-bf9f263839e6 | -23.9095 | -54.0606 | 2024-11-10 10:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 124.2 |
| 61a1fa89-ccfa-3cd2-a98f-e420a9533d88 | -17.6069 | -57.5304 | 2024-11-10 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 244.9 |
| 45a7fa10-7d3a-3bae-9531-b0d4639650ef | -17.6266 | -57.5281 | 2024-11-10 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 744a46b5-3b10-3372-a756-2ebd7a61057e | -17.6073 | -57.5099 | 2024-11-10 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.5 |
| a0346ca4-eea5-3f35-b21f-aeae7a356be3 | -17.6266 | -57.5281 | 2024-11-10 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| 74de274f-075a-3fe9-a7f5-941e25a37759 | -17.5872 | -57.5328 | 2024-11-10 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| f8bc0d54-c758-31ef-8981-0e4be4e985d0 | -17.627 | -57.5075 | 2024-11-10 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 1c195772-309f-3736-a488-92e8668fcfde | -17.6073 | -57.5099 | 2024-11-10 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.6 |
| b4bfea33-c151-3938-ad7b-b138f6122d68 | -23.9095 | -54.0606 | 2024-11-10 10:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 195.6 |
| a04b905d-6eaf-3819-9aa3-e85c9f2fc573 | -17.6073 | -57.5099 | 2024-11-10 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 209.0 |
| c7401315-1a3a-3702-85fb-0fe7ec6a1aba | -23.9095 | -54.0606 | 2024-11-10 10:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 151.1 |
| 240198ff-c553-3cbe-a8ca-9629992cc02c | -17.627 | -57.5075 | 2024-11-10 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 65e3dffb-a975-310f-b803-8c9e68e5c158 | -23.9306 | -54.0564 | 2024-11-10 10:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 152.4 |
| 762fe275-8112-3f74-85d0-9aee2b9e576c | -17.6266 | -57.5281 | 2024-11-10 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 69cb702f-a902-37f5-82e9-6f0f0bc418f0 | -23.9089 | -54.083 | 2024-11-10 10:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 183.2 |


[Clique aqui para ver as próximas entradas](README125.md)
