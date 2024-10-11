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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35b0e175-880d-38de-acbd-d7b20e92e085 | -15.43547 | -60.01521 | 2024-10-11 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57283f31-58f1-35b4-8fea-a6dcc9ac759f | -15.4285 | -60.01448 | 2024-10-11 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab77f69a-d1ac-3470-8247-655cc880409d | -10.6975 | -64.11358 | 2024-10-11 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b8b820c-32ce-314f-a1df-68b80441abba | -10.69715 | -64.1164 | 2024-10-11 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ed18450-d91c-3349-b8a9-2bdf0d174491 | -12.04677 | -64.72378 | 2024-10-11 06:08:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd6fbe03-4eb9-3174-ad08-fd8e922d8daf | -4.11 | -48.25 | 2024-10-11 07:05:04 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 432d57ea-7499-3131-aacb-68918122174a | -10.7059 | -64.1138 | 2024-10-11 07:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e346f28b-f836-34c4-b1f9-1c6f60698ac3 | -17.6865 | -56.3033 | 2024-10-11 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| c99df41b-9da1-3064-9863-9e9a1524fd12 | -17.6862 | -56.3241 | 2024-10-11 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 76ee48f9-67a6-3093-93c6-e91d6a553ba9 | -17.6467 | -56.3292 | 2024-10-11 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 03c10461-e27e-3936-b677-dd1e334fafff | -17.7059 | -56.3216 | 2024-10-11 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 2a278027-abc0-3a4d-9815-be2d5b70c917 | -17.7063 | -56.3008 | 2024-10-11 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 2a4d2215-a352-3e2e-ae7c-0d8f67f20b20 | -14.8104 | -54.6081 | 2024-10-11 07:26:30 | GOES-16 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 17cab507-e37b-3cbd-a25c-220d0877c976 | -17.7063 | -56.3008 | 2024-10-11 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 3b88722d-83af-3b1e-9460-ff33fe55d4ae | -17.7059 | -56.3216 | 2024-10-11 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| f34dc71f-372f-3294-b207-8bb3e18a7af9 | -17.6862 | -56.3241 | 2024-10-11 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| dd473a66-70c3-3644-9a2f-977e0472dfa8 | -14.8297 | -54.6058 | 2024-10-11 07:36:30 | GOES-16 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ac0c057a-0550-3ac9-845a-2cf82e62c47a | -14.8107 | -54.5873 | 2024-10-11 07:36:30 | GOES-16 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7e037e23-f432-366f-9635-c811a09ef69f | -14.8104 | -54.6081 | 2024-10-11 07:36:30 | GOES-16 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4259fc7c-9519-3f3b-864f-e2e69a10f0f6 | -17.7063 | -56.3008 | 2024-10-11 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 714c3b41-32a3-385d-aaed-bed46ea01f7e | -17.7059 | -56.3216 | 2024-10-11 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 74340102-92d8-3580-8fb1-c3ebd6d2a5ee | -17.6862 | -56.3241 | 2024-10-11 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| d6a881ae-621c-3cfb-a35d-b623ced36767 | -12.5994 | -55.2162 | 2024-10-11 07:46:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e16ca185-49b6-3033-ac20-9e86f2d30434 | -17.6862 | -56.3241 | 2024-10-11 07:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 87baa314-58ae-32fb-9a7e-e269e2ff711c | -17.7059 | -56.3216 | 2024-10-11 07:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| c90e3710-3663-3b82-b470-d359b8e18eba | -17.7063 | -56.3008 | 2024-10-11 07:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 62cd4aa1-024a-3218-8b05-3b6ab6c12cf8 | -12.5994 | -55.2162 | 2024-10-11 07:56:19 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 6ffc4050-257c-31bc-b6d9-5ade40ec7ba5 | -17.6862 | -56.3241 | 2024-10-11 07:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 15ca781e-1a6b-3517-bb3e-504e7dfd3292 | -17.7059 | -56.3216 | 2024-10-11 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 5fb80f9a-f93f-353c-b3d8-ed0daecdb2b7 | -17.7063 | -56.3008 | 2024-10-11 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 574037e7-0d35-3744-a445-2c8a17a3d8f5 | -4.11 | -48.25 | 2024-10-11 08:05:04 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2f491bf-a0eb-3152-b6e9-e1614ef3457f | -17.7059 | -56.3216 | 2024-10-11 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 00e26e77-8566-3212-869d-f58601a404de | -17.6862 | -56.3241 | 2024-10-11 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 0a1ad300-0f48-32ef-8a70-e07d41a55180 | -17.7063 | -56.3008 | 2024-10-11 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 99c12816-4e6a-3a41-81f6-3ac7f6d33cdd | -17.6862 | -56.3241 | 2024-10-11 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 713ff6ff-0deb-3850-bad2-0a0ac4b99ded | -17.7059 | -56.3216 | 2024-10-11 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 5d9f1fc5-48a0-3a53-b034-de44e796be07 | -17.7063 | -56.3008 | 2024-10-11 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 9f0498ce-44a0-348c-9347-0c6d5e815ae4 | -18.1582 | -56.4286 | 2024-10-11 08:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| cf995bff-24de-33a9-bea1-0f9543c007e5 | -18.1776 | -56.4468 | 2024-10-11 08:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| b9a32788-deb5-3d81-8af7-b9be66e97d38 | -18.178 | -56.4259 | 2024-10-11 08:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 4884b238-bfb0-343d-878f-a6c8f13b479e | -17.7063 | -56.3008 | 2024-10-11 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| cbdac5e9-2b94-36e8-ba3d-4aab8bf13604 | -17.7059 | -56.3216 | 2024-10-11 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 51f89f25-b4e0-3f8b-bb6c-bfd130e2e3c3 | -17.6865 | -56.3033 | 2024-10-11 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 91728d99-ab8b-3b85-b9cc-d4afe4d3fda3 | -17.6862 | -56.3241 | 2024-10-11 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| cd7b6200-bc85-3d60-ba74-dc5544a5da30 | -18.178 | -56.4259 | 2024-10-11 08:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 9168ba06-f8ad-394c-99aa-f7f37a3ab6b0 | -18.1776 | -56.4468 | 2024-10-11 08:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| e5af4679-7b8b-3b20-8c40-c68a615bd8e0 | -18.1978 | -56.4233 | 2024-10-11 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 366335fd-2da8-310f-9934-e7b00cc4af48 | -18.1975 | -56.4441 | 2024-10-11 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 47c7d72c-6ef7-34d5-b132-47ba0ed9a7a5 | -17.7063 | -56.3008 | 2024-10-11 08:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| f8b64b1d-7798-3989-a04c-e8e025cc1233 | -12.852 | -53.4611 | 2024-10-11 11:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| b0948cfa-461e-3290-92bb-6efa9e8bac2a | -12.6909 | -45.8712 | 2024-10-11 11:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4db9fbd4-a7a0-3f87-b52c-c98c5e2e19d8 | -12.852 | -53.4611 | 2024-10-11 11:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| acdb2e3f-d405-3e11-90bd-72371a367b27 | -12.2974 | -45.3343 | 2024-10-11 11:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 45644f1f-93a5-3048-838f-616090f44a2f | -12.3167 | -45.3314 | 2024-10-11 11:36:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 9a8e2f7f-ab69-3d53-ae69-f1bb7f1cc457 | -12.852 | -53.4611 | 2024-10-11 11:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| ba29a0a8-4719-31b6-ac53-dc5431ca77b4 | -12.2974 | -45.3343 | 2024-10-11 11:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 24fd1c44-06ba-3da4-8071-3e1a72c12658 | -12.2978 | -45.3112 | 2024-10-11 11:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 45f3e94e-b055-3b57-aef6-ae3ea88e7db8 | -12.3171 | -45.3083 | 2024-10-11 11:46:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d020b789-85f7-3e2f-bcba-9ff97f4e8565 | -12.3167 | -45.3314 | 2024-10-11 11:46:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 6b1a26d8-a4e9-3bc8-9ce9-28d42669a308 | -12.852 | -53.4611 | 2024-10-11 11:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 74301986-125b-3349-8830-90a98052678f | -14.4257 | -43.4399 | 2024-10-11 11:46:27 | GOES-16 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a2f1a9bf-c7e8-3022-99c8-5d5726ffc34c | -12.2974 | -45.3343 | 2024-10-11 11:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6ee21d4b-2699-3275-96bc-ec6cdfc9896a | -12.3167 | -45.3314 | 2024-10-11 11:56:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| abadb1b0-5dc5-35a4-84f5-6bfc78975528 | -12.852 | -53.4611 | 2024-10-11 11:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7432b66a-b839-3c3a-8f34-cdd3f8b25776 | -12.2974 | -45.3343 | 2024-10-11 12:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 37001ce4-bf3b-339b-9736-442318b40d67 | -12.3171 | -45.3083 | 2024-10-11 12:06:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| bff0f6c9-d2ca-33d8-ac7e-57d319f707df | -12.3167 | -45.3314 | 2024-10-11 12:06:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 289.6 |
| 472208dd-6f59-36e6-b9dd-f1ce8de448d9 | -12.6909 | -45.8712 | 2024-10-11 12:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1889461c-34d6-36ba-8ae1-82465aa07007 | -12.852 | -53.4611 | 2024-10-11 12:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 335627e7-6038-3ad7-a22a-008020a03a5f | -12.2974 | -45.3343 | 2024-10-11 12:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 03c706bf-4a35-3cb5-a6b8-bbe43f88fb1e | -12.3171 | -45.3083 | 2024-10-11 12:16:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 8a623f8b-2d6f-3166-9305-d318852e8039 | -12.3167 | -45.3314 | 2024-10-11 12:16:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 479.1 |
| 19639d5a-ff6a-3aaa-bbfd-d724f31fbcf7 | -12.6909 | -45.8712 | 2024-10-11 12:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 68d71217-f968-3a22-81c2-3735485d2a5e | -12.4182 | -53.1544 | 2024-10-11 12:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 2b15ede5-51ea-31c4-b312-95cfe1dba137 | -12.4566 | -53.1294 | 2024-10-11 12:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| f3338d90-95d2-3c78-8424-9dd185431f17 | -12.6909 | -45.8712 | 2024-10-11 12:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9e401306-bc7d-3514-bca0-1e5aa9856c52 | -11.2597 | -53.272 | 2024-10-11 12:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| b7914a38-c6f8-35d9-964b-171183de74c1 | -12.2974 | -45.3343 | 2024-10-11 12:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 03800369-0437-3eb4-963e-5750350ee032 | -12.3171 | -45.3083 | 2024-10-11 12:46:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 69c49382-04ec-3d2a-8d98-2c987d0f38ee | -12.3167 | -45.3314 | 2024-10-11 12:46:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 318.2 |
| 6c1aeb5e-a1d4-3b9d-a6b1-b57a58e04efc | -12.4563 | -53.1503 | 2024-10-11 12:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 67dc894b-bdca-34fc-9b37-a787b76ef471 | -12.4566 | -53.1294 | 2024-10-11 12:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d95c348b-8c1a-3349-bb22-26e0a9b9d287 | -12.4182 | -53.1544 | 2024-10-11 12:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 28830d0a-f01b-3f0b-b2fb-9ac66e032af8 | -12.6909 | -45.8712 | 2024-10-11 12:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8bf61e2c-f42d-381c-9378-26b1b90efaee | -13.0353 | -42.1577 | 2024-10-11 12:46:19 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 115.0 |
| e8675fd0-35a2-34f8-b5b0-39d13833e477 | -7.0786 | -59.4087 | 2024-10-11 12:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 04b5b846-3cf2-3e37-8a41-7f0f66039840 | -8.4417 | -55.4692 | 2024-10-11 12:55:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 52e0d4a3-3f6b-3e1f-b21c-47069720cd59 | -9.5465 | -44.4433 | 2024-10-11 12:56:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0f1db859-c156-3870-914a-60e9aad3da4c | -11.2597 | -53.272 | 2024-10-11 12:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 8b375575-5559-3a67-bcac-1a670db3bfdc | -12.2974 | -45.3343 | 2024-10-11 12:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b99640a0-3669-3f11-a3f7-a030b96b5c86 | -12.3171 | -45.3083 | 2024-10-11 12:56:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0e10beae-91e6-39f5-951e-e4723330d571 | -12.3167 | -45.3314 | 2024-10-11 12:56:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| d4e57e6c-497e-3936-9a60-d055647c36e5 | -12.3992 | -53.1564 | 2024-10-11 12:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 00110bf2-174b-3890-9b97-9137d9559382 | -12.4182 | -53.1544 | 2024-10-11 12:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| fefbb05e-0f46-34ed-af8c-0249e1e6cd37 | -12.4757 | -53.1274 | 2024-10-11 12:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| c8376adf-ed86-349a-a0e3-e7888ac77302 | -12.4376 | -53.1315 | 2024-10-11 12:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| d0e54ff6-5910-35c0-91f3-6a3164bde903 | -12.5913 | -53.0315 | 2024-10-11 12:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ef7d9430-185f-31e6-929d-e7013b2ab31a | -12.6909 | -45.8712 | 2024-10-11 12:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 63fe27f5-0ce3-3643-a1e5-c382cfe92e28 | -13.0353 | -42.1577 | 2024-10-11 12:56:19 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 75feec7a-c54a-374a-8362-36542a30ee3a | -13.7137 | -42.1999 | 2024-10-11 12:56:23 | GOES-16 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 85.9 |


[Clique aqui para ver as próximas entradas](README119.md)
