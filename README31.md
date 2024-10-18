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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e46aba-fc62-3bff-a6c8-755616873876 | -17.8876 | -57.229 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| f73aa0c0-10a1-3b29-be5c-52e439f97d63 | -18.0052 | -57.2762 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 9a189e65-0618-3d1b-9499-42bb0419a900 | -18.0049 | -57.2968 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 292c650a-9388-3b76-b484-05ad48871b94 | -17.9858 | -57.258 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| d60f6856-1268-3fc8-ac80-899a25fd9063 | -17.9855 | -57.2786 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 32c9e3fb-9b79-3cf0-9790-edab801a4cf1 | -17.9234 | -57.451 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 4f954bc9-e5a9-3a6b-b0d1-9f8f6ecedf4a | -17.9036 | -57.4534 | 2024-10-18 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| b9001b94-8935-39ac-8926-811f61ee32ae | -12.5147 | -63.3014 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 81b84d0b-d8cc-32a4-896a-e40d20ebd751 | -12.4966 | -63.2066 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| fc218ad2-cfb4-321a-b7fc-5091e9ff00d2 | -12.496 | -63.2832 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 31edb5f1-6205-32a3-932f-af8fa9cdc1f8 | -12.4958 | -63.3024 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0b7c0afb-e85b-3a2b-acda-ec47fb81cbd9 | -12.5336 | -63.3003 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| fd1749e7-75e8-36b7-a834-62364e30add7 | -12.5149 | -63.2822 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0ad19818-0be4-3d66-8513-9e7ce2136ed4 | -12.5338 | -63.2812 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 51ba558a-ea4d-32fa-a7c7-8c5f881f5c02 | -12.5155 | -63.2055 | 2024-10-18 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a49f9b21-94d7-3cb5-af02-fa84119a9b7c | -17.2077 | -56.7152 | 2024-10-18 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 67b502e2-14a3-3265-bad2-f4f0b4f57bef | -17.2081 | -56.6946 | 2024-10-18 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 75345652-e9fd-34b5-972c-63f8e9ca1ca5 | -17.2277 | -56.6922 | 2024-10-18 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 0d23df6a-99a7-320d-b09a-5d69e44855ae | -17.2373 | -57.3079 | 2024-10-18 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| b9e96259-a2bd-332e-be53-916526718c28 | -17.844 | -57.4813 | 2024-10-18 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 88b710c8-e0eb-3a91-9f16-0b4fa01661aa | -17.8243 | -57.4837 | 2024-10-18 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 514e2ca4-c29c-360e-9a39-f9e1b01709da | -18.0056 | -57.2555 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 98cd141e-1be4-3579-8c72-6b1619cb9f5e | -18.0052 | -57.2762 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 2b695ffc-e1f8-3c26-b3ee-8e0e3e9284ec | -18.0049 | -57.2968 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 59236a43-d4cb-3192-8058-78092b01eeb6 | -17.9858 | -57.258 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 1ea5bd02-afe9-3025-8132-1fa36a90359d | -17.9855 | -57.2786 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 84ab4a03-af6f-30b3-a6eb-ff6e565d0054 | -17.9234 | -57.451 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 4f047bcb-9441-3919-a77e-be09dbd14db0 | -17.9036 | -57.4534 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 7b3effe8-1691-3510-a0c6-6ebae388b9a8 | -17.9033 | -57.474 | 2024-10-18 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| da463726-9282-3d56-aa1e-3f3d8031c405 | -12.5147 | -63.3014 | 2024-10-18 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c0cefa34-fc2a-3c1b-8ff2-1610c566f03a | -12.4966 | -63.2066 | 2024-10-18 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 653d89f6-5d67-3572-9d0d-af9d1bf2a086 | -12.5155 | -63.2055 | 2024-10-18 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| efea990b-6ad3-3af0-8999-3724beaee989 | -12.5149 | -63.2822 | 2024-10-18 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 379b66bc-2b93-347d-bda8-8b33ddcc7dea | -12.5336 | -63.3003 | 2024-10-18 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 559ed1bf-ee30-3e7e-892d-b35eb4039c62 | -12.5338 | -63.2812 | 2024-10-18 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ffbafc7d-14e8-3082-bb2c-0fbb71b8f852 | -17.2173 | -57.3307 | 2024-10-18 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 298b1590-7ed0-377e-80b3-a9199ee13617 | -17.2177 | -57.3102 | 2024-10-18 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 07470704-fd2c-3b59-af7c-2f63eddf92f2 | -17.2277 | -56.6922 | 2024-10-18 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 41e1e947-1278-3a78-ad4a-4f083577c28b | -17.237 | -57.3284 | 2024-10-18 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 532850a1-4662-35f8-a3a5-8dff6f11b407 | -17.2373 | -57.3079 | 2024-10-18 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.5 |
| 39cb9591-a18b-389a-828a-30266e9722fe | -17.8243 | -57.4837 | 2024-10-18 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| a21ed26b-05d8-3d3c-b8bc-3de47491fd19 | -18.0052 | -57.2762 | 2024-10-18 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.3 |
| e33a52bc-bad3-3fde-b1f5-ef5fcf7f0200 | -18.0049 | -57.2968 | 2024-10-18 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| bf12ccd4-4cb6-34a5-b482-cb5edc68c695 | -17.9858 | -57.258 | 2024-10-18 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 4fd90d3a-e7d3-33c1-97e4-880ac37af207 | -17.9855 | -57.2786 | 2024-10-18 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 25c4de90-a0d2-3730-ba7d-ec2823b97249 | -17.9234 | -57.451 | 2024-10-18 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.4 |
| f047fd72-a34c-379e-9724-370637c95b8f | -17.9036 | -57.4534 | 2024-10-18 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.0 |
| b7f8496f-9d66-3ca5-9d81-bc2058dbc1a3 | -12.5336 | -63.3003 | 2024-10-18 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 32976592-3ddd-3e9d-b575-d34a28a89635 | -12.5155 | -63.2055 | 2024-10-18 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1b898779-c52a-3101-a25e-98f9ad74366e | -12.5149 | -63.2822 | 2024-10-18 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ea942d95-0426-3a58-ae79-c4248aed6b11 | -12.5147 | -63.3014 | 2024-10-18 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1093dd8e-8aab-3b9a-b6af-d8a427b0abef | -12.4967 | -63.1874 | 2024-10-18 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f9ec51d2-934f-35c0-8b84-047517366b1d | -12.4966 | -63.2066 | 2024-10-18 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c5aac0ab-0724-36ef-842c-bda850b3c4c9 | -17.2177 | -57.3102 | 2024-10-18 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 6747e552-6b00-36d4-bd69-e2799a74a8e4 | -17.2274 | -56.7128 | 2024-10-18 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 6e52c15b-0fe7-34b6-a7aa-bdce3b12ba51 | -17.2277 | -56.6922 | 2024-10-18 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| ab58524d-b5e5-313e-8329-36b7cbfdc8c2 | -17.237 | -57.3284 | 2024-10-18 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.2 |
| b5e58229-83e6-367d-bbdd-3fe764b02bb8 | -17.2373 | -57.3079 | 2024-10-18 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.7 |
| d78f35a9-d2e8-3b58-bbe0-f981917f98c4 | -17.923 | -57.4716 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| e6ddf85a-cef4-3d04-abfd-eeb46d7c4e4c | -17.9036 | -57.4534 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 21113456-d365-33df-acb8-805050c2678c | -17.9858 | -57.258 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 4c83df1e-cb63-3faa-8416-09ee368efdf4 | -17.8876 | -57.229 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 68a99602-b08f-3c83-b2cd-4db9e4779451 | -18.0049 | -57.2968 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 5fdbec47-6c6f-32f9-a359-d055569c5a80 | -18.0056 | -57.2555 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 44c85b50-9ba4-396b-b70d-b4056567dcc3 | -18.0052 | -57.2762 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.0 |
| 8f6fe67c-ab4d-3045-96ce-f5e54da21e1e | -17.9855 | -57.2786 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.4 |
| 386d987f-bce7-3a13-bd32-2d0236d05000 | -17.9657 | -57.2811 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 28a51963-b15c-371c-bcf2-5cd4184f4ce2 | -17.9234 | -57.451 | 2024-10-18 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.8 |
| 30b410c9-a032-3a82-835e-7fd69b293b62 | -12.5336 | -63.3003 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 36845cac-4855-31b3-a334-63994017a249 | -12.5338 | -63.2812 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 2e9b0835-c915-3005-b69e-6e9d5e5d5a9a | -12.5155 | -63.2055 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7bdd95fa-e746-3617-adb2-caf142cf6359 | -12.5149 | -63.2822 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0d274ca2-703b-3e6c-a00e-31b96ea32bf8 | -12.5147 | -63.3014 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 159a557a-4c3b-37ad-bf92-f8c9384cd791 | -12.4967 | -63.1874 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 30bb8144-4808-34a4-b61e-0da3150b7710 | -12.4966 | -63.2066 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1318f95e-7a9e-38c6-88d0-483bd1f0759a | -12.4958 | -63.3024 | 2024-10-18 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e9e70122-675a-3bd1-9da8-794674e2145c | -17.2277 | -56.6922 | 2024-10-18 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 1d53fd2b-44a8-309b-b74e-3982564f7b6f | -17.2177 | -57.3102 | 2024-10-18 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 21e33ecf-9220-3ccd-868a-0c0bc567f706 | -17.2081 | -56.6946 | 2024-10-18 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| a9ed6183-84d8-3c7a-9dbc-2b8859db503c | -17.237 | -57.3284 | 2024-10-18 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 8475db59-9948-35f7-9879-14b8a6a70c64 | -17.2373 | -57.3079 | 2024-10-18 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.7 |
| 334d283b-ff20-305e-8cdd-4205349e52d7 | -17.9855 | -57.2786 | 2024-10-18 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.4 |
| 2767ded7-8d85-3071-8286-2c1b883106fb | -17.9858 | -57.258 | 2024-10-18 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 78a9ee50-2d08-306a-91b8-f1c718385175 | -17.9036 | -57.4534 | 2024-10-18 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 9569695d-e370-3e76-9b6f-d728405eb4e7 | -18.0056 | -57.2555 | 2024-10-18 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 141ab3ea-334b-320a-b1e6-f1db0e9b5d61 | -18.0052 | -57.2762 | 2024-10-18 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.5 |
| 138e5907-b1b9-372e-b3d0-775580071935 | -17.9234 | -57.451 | 2024-10-18 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 2a5580b5-4d0d-3240-8ee8-691dfd79e06d | -12.5338 | -63.2812 | 2024-10-18 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 86e9c6d9-dc3a-3726-8615-c2beeee00702 | -12.5336 | -63.3003 | 2024-10-18 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a5a8ad20-c2ac-331f-8b54-eca15e8d1c75 | -12.5149 | -63.2822 | 2024-10-18 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 836b8605-871c-33a9-8008-28e2a149e102 | -12.5147 | -63.3014 | 2024-10-18 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b2e15cc5-7723-37cc-b6f9-64012427dfa9 | -12.4958 | -63.3024 | 2024-10-18 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| c8e23847-e240-364f-9028-0ebcac86e5c0 | -17.2277 | -56.6922 | 2024-10-18 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| c6615c10-68ff-32db-a49f-c09d8a1f217e | -17.2373 | -57.3079 | 2024-10-18 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.4 |
| 7ab0d6e0-35dd-33f1-8f5d-63b1a79c3883 | -17.2177 | -57.3102 | 2024-10-18 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| fc610d74-8620-3d68-8ce7-1388eab47a9c | -17.237 | -57.3284 | 2024-10-18 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| e4c172ba-4540-3128-8b9d-dafd1e85f4ba | -17.844 | -57.4813 | 2024-10-18 08:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 068c8559-28f4-37ab-925c-6d8e86891405 | -17.8243 | -57.4837 | 2024-10-18 08:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 96b0900f-939a-3849-a003-5af446d1a8a6 | -18.0056 | -57.2555 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| df822240-6b3c-39ff-a7ae-89b5ed603e03 | -18.0052 | -57.2762 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.9 |


[Clique aqui para ver as próximas entradas](README32.md)
