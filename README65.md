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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b1ab32e-61e7-3182-8116-8a040c0ae998 | -3.951 | -50.20119 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89b2869d-a09c-3a57-b0d3-139d1089fcb8 | -2.768 | -46.00529 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1e09990-ef1c-3cd6-ac71-e345aa9e3945 | -3.38941 | -50.31854 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a36b10e1-3e92-3b10-b3f1-ebb070c3527e | -1.58633 | -53.8211 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d67e02e-a19d-3a99-bf40-7e4eb695c7a7 | -2.74514 | -49.11992 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5aff02a3-a09d-3744-9ece-b8f50ebf0f0e | -3.32092 | -51.62878 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5ccd0b5-c382-36be-8bb3-efa51df83732 | -1.13973 | -51.67836 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7ddfd36-abe8-331c-bf3d-9e83e5259b18 | -2.20713 | -48.91864 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6a597cb8-a598-3052-9f7b-dd9c8fd286d0 | -0.98688 | -51.71775 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb6e23f3-39d4-370c-8b46-06ca6b7e31c0 | -2.17869 | -50.22585 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98b2b91f-f708-322c-995a-330cdb6caf3c | -3.54369 | -49.88589 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5eafe94-72ca-3cb1-bda3-dd6fae08e1d5 | -2.62769 | -46.22266 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 157c1e6f-2932-34fd-84d3-e1593f73fcb2 | -2.22696 | -50.57123 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d741acb-b40e-30d7-8163-b96c4354e5d9 | -3.86474 | -50.05691 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 101567fc-8ad9-30c8-9bbd-cfac09aaece1 | -2.82741 | -54.0985 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db3d9952-4902-326b-8d3c-53e8ab54443d | -1.69497 | -52.76189 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef905c24-e6eb-3e7b-bc11-6f6f1fc9f8cd | -1.76152 | -52.70486 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02b7cea0-6027-3740-ae8a-a411fae2ddb9 | -3.20707 | -52.57613 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13138a04-a045-379c-9235-3a3832df3049 | -2.29485 | -50.67963 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0178303c-a2ae-3933-889a-5c12a55e6d82 | -1.44951 | -52.46031 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9caf87fb-4992-359c-b9ca-b7272dc4b411 | -3.18101 | -54.32917 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e968776-629a-3bf2-9f4a-7d3b5075a7b8 | -3.25185 | -42.0267 | 2024-11-24 04:53:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8488d68f-6ed9-3af5-b1b7-a0604addeee8 | -3.06446 | -53.22399 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89260366-1210-3411-a1f4-aa877fa2bfce | -2.11673 | -50.60191 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34fd534-2a5a-3366-aea1-23fb13372ab6 | -2.32741 | -46.3462 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63db6911-104a-3861-9618-1476ced30df0 | -2.58656 | -54.04657 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7ce0473-d0c9-39fe-8a93-ce77ea78ef22 | -0.83697 | -53.13652 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9494e001-32e2-3a60-a466-216cfdd0e957 | -3.86373 | -50.05669 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ca08a3b-26fd-3b2a-bb6a-7e3a55b62854 | -2.63166 | -54.38647 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fbd38f9-81e7-3234-b08d-57d8a1e5e7ad | -2.2232 | -51.84131 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75839d3b-953e-3a41-a7f3-5db7f9fd5509 | -2.32551 | -53.6777 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d33e2cd4-12c5-3c2d-bc03-a9ce97ff0049 | -3.24743 | -54.23933 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c9e01d0-59e9-31a8-bac6-2c9ed67105c6 | -1.61078 | -52.5812 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 351b6571-2623-30aa-a632-fd236e6c3d25 | -2.20897 | -49.87299 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5339a5df-09f0-3b36-9606-9ddf115a2745 | -3.95944 | -52.2222 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c061a51-7069-3bff-bd9e-28d5d9909974 | -2.82493 | -54.02571 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3be4f8f-f9a7-3b73-b72e-88c12373369c | -5.44092 | -46.91405 | 2024-11-24 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be36f446-a0d5-31c4-b529-b7a1ec08e22e | -4.89865 | -50.69901 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f016a8-785e-3a4f-82aa-b8544d62e19a | -3.83193 | -52.25469 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4640b67-6347-3331-9f5e-2bcd04354735 | -3.96957 | -49.94418 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9396d89-bc6b-3114-884f-e3a5dc9e1034 | -2.70586 | -46.10852 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ff7ca3c-be5b-3b80-bb5f-1a8be050c439 | -2.86111 | -53.97441 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c12b091e-f7d8-328b-8d67-f55cc0641ac6 | -3.70236 | -47.59766 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b72b245-3354-3023-8230-17568776b0a8 | -3.33442 | -50.30991 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d65f6c3-4f43-3c52-95bc-65c60af26b28 | -4.09564 | -51.06137 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44dbcafd-c431-38ef-b0e8-2505db62b374 | -2.73985 | -47.53964 | 2024-11-24 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d5c9d17-6488-3220-9437-2f9b1a5d53ce | -2.03405 | -54.47863 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a720b8e-c5a4-33ff-ae01-a6b44484de0f | -2.2272 | -50.39185 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a2e848-80f8-3cc4-8b42-45785ec33a13 | -2.178 | -53.78624 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b6b8ee-8328-3a44-a248-b27ecf21ae5e | -2.95016 | -53.71836 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d611f65e-f4f0-3766-80c0-897fd2e33817 | -1.31389 | -51.87088 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a61a3d54-4299-39f8-bce6-60e2c6981f17 | -3.31614 | -54.09353 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7225cfe4-4fdc-3f68-a0f1-705bf69d21ad | -2.00787 | -46.28377 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 607aa0bb-c47f-309c-9014-14703298446e | -2.24104 | -49.31542 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0f87b57-d8be-37ca-8018-e9c5bfb2cae4 | -2.44865 | -49.09435 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1197d72-0cd9-36bd-accc-5fb78c91abb0 | -3.98586 | -49.93093 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc98b730-9a5b-3736-9407-34a1fd4f798d | -3.68387 | -47.12638 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92b0713b-cddd-3f81-94a2-f15a8f29619f | -3.52507 | -53.8181 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6aa34b4a-604e-3938-90d6-e9d927ff6b61 | -4.93136 | -47.50379 | 2024-11-24 04:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 599f4ae3-2bd2-321d-8f09-f4030af57947 | -3.28368 | -53.78431 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac802c0e-db55-3813-98de-799012d20521 | -3.3215 | -53.19162 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d82c9c50-3417-35b4-9daf-8edf4ad22e78 | -4.53421 | -42.90923 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0d2bc1f-222a-3401-8702-1e2c828a5708 | -2.35329 | -49.10167 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08253213-5b82-347f-a025-4f03b4de4b0e | -2.2804 | -53.62629 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b4a083-3f00-3b40-b63f-5d4b083fbecb | -1.56421 | -52.00856 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04608b23-d501-36a8-986e-a4cb0ed452af | -3.24757 | -53.2739 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b0ad3a8-6d8a-396a-b3aa-a137ba0334a7 | -1.31432 | -51.75508 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52348638-37ff-3a45-a04d-3516624d9402 | -2.92681 | -51.45076 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cba485e-d094-3962-b838-cb4336788025 | -1.64784 | -53.8761 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a48648c2-7b31-3596-9447-81cd00830259 | -2.32446 | -50.68781 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b2b3312-83db-37bf-9cb3-03ec6569b6c6 | -3.53229 | -54.08087 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3a8a3a0-426a-3d82-80b9-afa674b97f16 | -1.63747 | -53.31954 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcea1639-0e33-3171-a0b2-5a48d409df52 | -1.95406 | -50.72841 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eecfd552-ac8a-39c7-a72d-c2fabc1f5f05 | -2.35864 | -48.55891 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef94c385-33dd-391c-a415-8d10aaa91dbb | -3.79393 | -50.96793 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb43d950-bf41-3d2e-a34e-f21049ba7ffb | -2.55946 | -47.2957 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5572b125-3848-3da8-a64e-48682d79ec24 | -2.75151 | -54.11324 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3e275d1-1c17-3c21-bc68-196afa4d9540 | -2.20004 | -50.54522 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20ae50b8-6441-338e-b84b-4126e860f81c | -2.65831 | -46.13406 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22f4c105-45a0-3896-9a9a-f2e5f49ddbd7 | -3.24683 | -54.24311 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b73ead-e3da-3adf-ab90-3f6b72b63111 | -3.50502 | -52.88863 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20eec0b4-c477-3f2d-9dbe-5d0d5c198c73 | -3.23083 | -54.23296 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52e78388-3344-3352-a327-2d2f2cc133ef | -3.426 | -53.28411 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e93cf72d-e96a-3e81-817c-1335ce293f39 | -2.11332 | -50.12617 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc5f415e-24e3-370f-b60d-bf959ca0457b | -1.92268 | -54.42632 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 457ed922-d3a6-3736-9a75-de7e9dcbe5d9 | -2.60081 | -46.25644 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b90bdd8c-2afd-3ff9-aa24-6441a2904962 | -4.84736 | -50.80737 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c1312e6-9566-3815-8576-c843de0c592b | -2.31717 | -53.63568 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7757dbf4-6eae-3626-b407-22513c65c563 | -3.5263 | -53.78853 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 333e9ca6-4ac3-3ce9-9640-60f7139773a4 | -3.077 | -54.55955 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b9c4d0b-b80a-31c2-8705-b74e9620d6da | -1.88647 | -50.11833 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf7d196-3f49-367d-be77-7ca001f13148 | -2.90245 | -46.69876 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fda0fd5d-a351-3054-9ed1-0b1142de14a9 | -1.26266 | -51.76118 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b7bab1b-03ef-3161-9e4b-dc5f0ac75156 | -3.46793 | -50.01022 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00bc3cb8-3c47-3ec8-9a5d-67bf74a61e0b | -3.05443 | -53.22243 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9adf2de0-5285-35f3-bcd3-fc23ea05e4af | -3.48642 | -48.24654 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d1604b2-4550-389b-8f37-81269eb647fa | -5.29878 | -50.74349 | 2024-11-24 04:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a51989-9bbd-3c4d-8c5a-5bc5bcab525e | -3.24732 | -50.12302 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c5b62cd-832d-3ed8-be91-d1aed23f33fe | -1.08628 | -53.67555 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c7260e1-ac25-3591-82af-eafef37c9bb0 | -3.18505 | -54.32592 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README66.md)
