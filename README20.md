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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae8c88a2-57fe-3d88-83d8-0bb20ea775f9 | -12.3703 | -50.0026 | 2025-05-24 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ff23f526-9863-3de2-9bf5-20bc20803fca | -12.3706 | -49.981 | 2025-05-24 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 19438206-bbcf-310b-b723-ba87397c157b | -12.3894 | -50.0002 | 2025-05-24 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| fc8e4373-06d9-3661-84e7-a8e4d53841d0 | -12.3898 | -49.9786 | 2025-05-24 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| a1579c78-a854-3b2e-96eb-b53812f28599 | -12.3703 | -50.0026 | 2025-05-24 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 104caec7-8e0b-3a08-9db9-0e0f3f78bede | -12.3703 | -50.0026 | 2025-05-24 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 227.6 |
| c64d9545-c249-3beb-84b3-3bc8d87f77df | -12.3894 | -50.0002 | 2025-05-24 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| bd385a05-007e-3b2a-a8d4-6cde2a8a8e8a | -8.07 | -43.1216 | 2025-05-24 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 3877c44f-c2df-3780-bb4b-951d321744ef | -12.3706 | -49.981 | 2025-05-24 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 24c221a0-33b3-387e-ab0c-75e5cb8b33d7 | -12.3898 | -49.9786 | 2025-05-24 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 9e75032b-74f5-3693-bb8f-9395971bbe58 | -12.3894 | -50.0002 | 2025-05-24 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 759759fe-5af9-30f8-8cfc-eaeeb20bd490 | -12.3706 | -49.981 | 2025-05-24 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 4e978fdc-7ab0-3585-94a1-5b724419964b | -12.3703 | -50.0026 | 2025-05-24 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 254.5 |
| fa928b78-62ae-3735-a5a9-4deda07535b7 | -7.6574 | -46.1013 | 2025-05-24 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 45cf197e-f650-3400-8e3d-6ddaf41b26d4 | -8.07 | -43.1216 | 2025-05-24 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 56bbedf8-a5f1-3f52-948b-203a9ee9cd6a | -12.3898 | -49.9786 | 2025-05-24 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| ac2b55be-8686-3fe4-8934-5066d938691b | -12.3703 | -50.0026 | 2025-05-24 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| f7f5059c-028a-3dc4-b56a-cfca0475ead4 | -12.3898 | -49.9786 | 2025-05-24 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 175.9 |
| df1256fa-a46f-37ef-9bad-71ce400c9af7 | -8.07 | -43.1216 | 2025-05-24 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.0 |
| a43d1354-79d7-3d72-9bea-69aa1741e2e8 | -12.3706 | -49.981 | 2025-05-24 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 3080dcdb-9326-33ca-82c9-5b56b669ccaa | -7.6574 | -46.1013 | 2025-05-24 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3b714aa1-b4b3-3f97-a587-a8ecb7cd363e | -12.3894 | -50.0002 | 2025-05-24 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 178.1 |
| cbe3f65b-21ea-3353-92ea-27d2d6036db7 | -12.3894 | -50.0002 | 2025-05-24 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 176.7 |
| f3c9342a-f63b-3888-b71d-74a04f0ec7a8 | -8.07 | -43.1216 | 2025-05-24 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 309.5 |
| c9bfc792-4748-34b8-ba09-552d95c55475 | -12.3703 | -50.0026 | 2025-05-24 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| deae20b3-2343-3811-9760-faa96b0f6378 | -7.6574 | -46.1013 | 2025-05-24 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 572b2ae6-a5e3-3538-845a-d4b7b117c60e | -12.3706 | -49.981 | 2025-05-24 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 8e83d08c-1ae1-340b-9923-3e09393f2764 | -12.3898 | -49.9786 | 2025-05-24 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| c6f51d06-baa7-34dd-99f3-1ba35aae1e97 | -12.3898 | -49.9786 | 2025-05-24 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| cb832f25-3f75-3f2c-ba49-89cf7e03cda3 | -8.0889 | -43.1196 | 2025-05-24 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 0c267e66-3a7f-3f1a-bc22-2e1bf377cbea | -8.07 | -43.1216 | 2025-05-24 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 269.8 |
| cd7860f2-9ca3-3fab-8bcb-fb58dc45b1b3 | -7.6574 | -46.1013 | 2025-05-24 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 6758cf84-3aea-3a1d-973c-c91ddd21cb0f | -12.3703 | -50.0026 | 2025-05-24 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 1f287732-4985-32ea-a9b9-f357c38c40e6 | -12.3706 | -49.981 | 2025-05-24 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 004920f3-9be6-3f9d-9879-2a6864802f83 | -12.3894 | -50.0002 | 2025-05-24 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b6790bbf-05b5-39c5-b54d-eab8e69fd34d | -12.3703 | -50.0026 | 2025-05-24 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 25c4b852-b058-3b81-95bc-93d1f1b2b0f5 | -12.3898 | -49.9786 | 2025-05-24 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a9ea745b-34d0-3c8b-ae65-eb92ffca3d63 | -12.3706 | -49.981 | 2025-05-24 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 1b574882-38bf-3148-8b54-f73cbe097a71 | -8.07 | -43.1216 | 2025-05-24 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 382.4 |
| 491a314b-73e7-3b13-a6c7-17e7df19f551 | -7.6574 | -46.1013 | 2025-05-24 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c2185ea3-9bbf-3f60-9acb-0c4fcb4682ec | -12.3894 | -50.0002 | 2025-05-24 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 2ade94d1-d79a-346b-94f1-d72c3ae1ad6b | -8.07 | -43.1216 | 2025-05-24 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 325.7 |
| 871a6d20-fd92-30fb-83cd-798a3a6b79f0 | -8.0889 | -43.1196 | 2025-05-24 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 47f215c6-8dc7-38b1-866d-95ea05636251 | -12.3894 | -50.0002 | 2025-05-24 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a7fd0d48-da69-391d-9964-4e09c28008d5 | -7.6574 | -46.1013 | 2025-05-24 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 1633aa1a-f9c6-328c-a8ab-1eae47355451 | -12.3898 | -49.9786 | 2025-05-24 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 16ab0dff-76ae-393e-a5a9-e2f4bc5d88f4 | -12.3706 | -49.981 | 2025-05-24 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 985247da-e070-3859-80ab-e77c97906f15 | -12.3703 | -50.0026 | 2025-05-24 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 35bfffac-97a4-3960-bf8a-bf6c798aefcb | -12.3894 | -50.0002 | 2025-05-24 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ffdbb595-55a3-31e1-b9db-7ce83f37e11a | -8.0889 | -43.1196 | 2025-05-24 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 888e0ff8-f692-3f3b-ad46-84b63ea36e3b | -12.3706 | -49.981 | 2025-05-24 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 2f964a4f-9225-30a7-ad3f-ac6f9352b104 | -8.07 | -43.1216 | 2025-05-24 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 382.1 |
| a8ce2321-86a6-35a5-8931-d41ee9b1b583 | -12.3703 | -50.0026 | 2025-05-24 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 1afe9a24-f963-3d6e-9c38-871f926d566b | -12.3898 | -49.9786 | 2025-05-24 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a80e31c2-b071-3039-95d3-457d73365a58 | -12.3898 | -49.9786 | 2025-05-24 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 32a2521e-2284-32f1-80bd-73c8de3fff96 | -8.07 | -43.1216 | 2025-05-24 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 449.1 |
| 910b4bef-b809-3204-ae6c-65201cbe17da | -12.3706 | -49.981 | 2025-05-24 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 61a587cb-b9d1-3b01-8d16-b4a0d8b5bd7c | -12.3703 | -50.0026 | 2025-05-24 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 4129bcf4-23ae-392e-b76b-f290edf4b5f0 | -8.0889 | -43.1196 | 2025-05-24 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| aab01353-cffe-3fd1-ab46-236868102930 | -12.3894 | -50.0002 | 2025-05-24 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 12806d07-b87a-31c1-8330-e7dbb636f4a9 | -12.3703 | -50.0026 | 2025-05-24 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 88ad8c61-f072-3978-8c17-688072cb8ec7 | -12.3894 | -50.0002 | 2025-05-24 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| fa6713a2-90a3-38be-8725-930988eccc71 | -12.3706 | -49.981 | 2025-05-24 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| bb61fd51-d485-3c13-b355-5e50e3296098 | -8.07 | -43.1216 | 2025-05-24 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 684.1 |
| 09c2c923-8bd8-3e67-ba47-48b4eae115f5 | -12.3898 | -49.9786 | 2025-05-24 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9d623c61-47ce-3c1a-b46b-f05a31b65c59 | -7.6574 | -46.1013 | 2025-05-24 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| e19ae550-05aa-3a19-9726-72bb3b1d69f0 | -14.1801 | -60.0226 | 2025-05-24 13:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 073866d9-7281-3a90-b6ba-bd523c99dc33 | -7.6574 | -46.1013 | 2025-05-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 89176344-4dbd-3a8a-a728-d1c09c9e8218 | -12.3898 | -49.9786 | 2025-05-24 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f5668349-fca0-3983-8c00-0448dcd94c38 | -12.3703 | -50.0026 | 2025-05-24 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e400c62f-6d6a-3f88-a942-9e6fd524d018 | -12.3894 | -50.0002 | 2025-05-24 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 5845b788-eb66-3d3c-9628-c933879d5de3 | -8.07 | -43.1216 | 2025-05-24 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 631.2 |
| 0cd9b5bc-bb3f-32cc-b9e1-0c88dcb8819f | -8.0889 | -43.1196 | 2025-05-24 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 01b0439c-668a-388e-893c-7d8c041bb716 | -12.3706 | -49.981 | 2025-05-24 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a3bf6dbe-77bc-38ed-b90a-09f111411057 | -8.0889 | -43.1196 | 2025-05-24 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 18738d57-ef30-3533-b39b-aa0d3c4983b2 | -12.3706 | -49.981 | 2025-05-24 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 9297910d-6588-3aef-98a1-3fef3c7d9955 | -12.3898 | -49.9786 | 2025-05-24 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 717599ba-7f89-35a3-8d44-84999ca6a943 | -12.3703 | -50.0026 | 2025-05-24 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| de867687-76b9-3408-a5b5-6ef97bf7e248 | -12.3894 | -50.0002 | 2025-05-24 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 67147b94-4715-3858-b9ae-d369db4984f4 | -8.07 | -43.1216 | 2025-05-24 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 661.6 |
| f36539e5-5c39-357b-be3f-bb6176f48474 | -12.3894 | -50.0002 | 2025-05-24 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 03f8747e-297e-3a6c-949f-8cdc0c3d1277 | -7.6574 | -46.1013 | 2025-05-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7ffa16b2-510f-3e29-a58e-af8fc935aba3 | -12.3898 | -49.9786 | 2025-05-24 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 294cf730-d338-3672-8292-8d6e0563054d | -12.3703 | -50.0026 | 2025-05-24 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c52d7d37-b9a7-37d4-b2cb-4de7b80618db | -12.3706 | -49.981 | 2025-05-24 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6a50e017-7de5-3f10-8893-3c91ffa6c58d | -12.3898 | -49.9786 | 2025-05-24 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ac7af382-0916-394e-8c76-2f460feb31c3 | -13.7572 | -58.5924 | 2025-05-24 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 18cb68a7-1197-362c-9138-8ec4db0287fa | -12.3894 | -50.0002 | 2025-05-24 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 21267069-495b-3704-8faf-285b8b431269 | -12.3706 | -49.981 | 2025-05-24 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 01878ace-b52e-382e-983a-692d0d76c9f6 | -12.3703 | -50.0026 | 2025-05-24 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 3fa34696-65c2-391e-8296-8bc1329db822 | -12.3706 | -49.981 | 2025-05-24 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ab520c9a-0765-3ae2-8176-b1cf1eebddbc | -12.3898 | -49.9786 | 2025-05-24 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8fab8538-6e3d-35f5-b8ad-326af72d269b | -7.5959 | -43.3125 | 2025-05-24 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| abfb3bec-9bda-389e-839d-60995cd900f6 | -12.3703 | -50.0026 | 2025-05-24 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2a0784cd-b67b-3d58-9bcd-e11310bb2a39 | -12.3894 | -50.0002 | 2025-05-24 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 00a36a74-d650-3d62-83ae-bfe1a975abc9 | -12.3898 | -49.9786 | 2025-05-24 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 88291aae-d3f2-380e-8884-df06704dde50 | -8.07 | -43.1216 | 2025-05-24 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1009.7 |
| 64923205-92b3-3d6b-a860-956a4888937d | -13.1941 | -53.569 | 2025-05-24 14:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 67afb815-22a9-3b0f-b173-3367848c2f28 | -12.3706 | -49.981 | 2025-05-24 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 5bae481f-2163-3c72-93b0-c096a6f94f82 | -12.3703 | -50.0026 | 2025-05-24 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |


[Clique aqui para ver as próximas entradas](README21.md)
