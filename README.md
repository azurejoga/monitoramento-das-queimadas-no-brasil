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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26e15e2b-4fd9-35ad-950a-c07145e8e51f | 2.3071 | -60.2454 | 2026-03-13 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 45e4cf00-727e-39c6-aa8e-086b5f73550c | 2.3253 | -60.2452 | 2026-03-13 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f3d1885a-775f-3538-8173-273ef0d93201 | 2.3254 | -60.2262 | 2026-03-13 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1bc19f71-5004-3519-81bd-087a32f3435d | 2.3071 | -60.2454 | 2026-03-13 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7c808372-937e-350b-b263-e813bbde878d | 2.3071 | -60.2264 | 2026-03-13 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 45f9f516-0e8c-3e4d-9962-d68ae2959b00 | 2.3253 | -60.2452 | 2026-03-13 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 254be183-b711-3ad9-9bd0-56f42fc140e4 | 2.3254 | -60.2262 | 2026-03-13 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2b1d308e-81a2-3068-b168-4cee95a75eef | 2.3071 | -60.2454 | 2026-03-13 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 18afe89f-08b5-3350-ad6c-ce4eb97499fe | 2.3071 | -60.2264 | 2026-03-13 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e691541d-8f09-37ef-bbb8-3b3e02cbf4fd | 2.3254 | -60.2262 | 2026-03-13 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 25757c7b-0959-3520-8441-9881d80a6dfd | 2.3071 | -60.2454 | 2026-03-13 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3382c632-5d97-3e56-af37-afa9abee444f | 2.3253 | -60.2452 | 2026-03-13 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f9386b49-a6ae-3ce8-8cf9-fe4fcfcac7ae | 2.3071 | -60.2264 | 2026-03-13 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4c8004c0-113e-370f-a9ea-10cac4528c48 | 2.3153 | -60.562199 | 2026-03-13 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec6efba-3b77-3f6a-a07d-c4d4b0540c5e | 4.2781 | -59.911499 | 2026-03-13 00:39:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 820e7658-d0cd-37cd-80bb-51edc94aa3ce | 4.2765 | -59.918499 | 2026-03-13 00:39:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0abd221-c390-3783-9d9c-77af63e8c0ed | 4.2797 | -59.904499 | 2026-03-13 00:39:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 30410338-351a-31c8-b014-ef7552406f7a | 2.3094 | -60.226799 | 2026-03-13 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 18a05bdd-c39a-35ac-a958-58afe1ca951d | 2.0565 | -60.567402 | 2026-03-13 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2eec7d-d522-38e0-bce2-fdc1008902a2 | 2.3077 | -60.2341 | 2026-03-13 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f3cef38e-fe94-331a-a80f-be9d8036b6bd | -10.1257 | -36.1441 | 2026-03-13 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 169.2 |
| 108d0ad3-ac87-3515-b039-8b417e475570 | 2.3071 | -60.2454 | 2026-03-13 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ee8d6802-9615-3820-852a-89caa8538dc3 | -10.1262 | -36.117 | 2026-03-13 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 149.3 |
| 35c31dca-2257-3373-98ad-a439d0b1197b | 2.3071 | -60.2264 | 2026-03-13 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1828894b-f2bf-34a2-a920-6d0e4cfcd137 | 2.3254 | -60.2262 | 2026-03-13 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 769d5024-521e-369e-b9b1-23f771a6da7d | 2.3253 | -60.2452 | 2026-03-13 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 71ff9613-b9bb-30ed-bb98-23bf0b692be4 | -10.145 | -36.1406 | 2026-03-13 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 195.5 |
| 82057ac2-a14b-36ff-bc21-1e4de8c167f8 | 2.3253 | -60.2452 | 2026-03-13 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 78380fae-9c22-32d7-a745-6c730ff4757f | -10.0662 | -36.2359 | 2026-03-13 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.4 |
| b08d827f-5946-3850-a55c-8447c960ee09 | 2.3253 | -60.2452 | 2026-03-13 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7ff8db53-3f23-36e3-9c3f-eb1edb4c1a60 | -10.0656 | -36.263 | 2026-03-13 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| babcc363-2f72-32c3-b297-7d52cc4631e9 | -6.5631 | -51.1126 | 2026-03-13 01:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d4df7f02-1895-3742-b2d4-0f57270ad08d | -10.0468 | -36.2394 | 2026-03-13 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 28831f8e-e7f7-3991-91f3-9c10955de79b | 2.3071 | -60.2454 | 2026-03-13 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| eac440f4-8502-3cf1-a51e-62966bb5527b | -10.0656 | -36.263 | 2026-03-13 01:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| b3139fe8-4a77-365a-9f29-87ea1c3986f5 | 4.2739 | -59.914299 | 2026-03-13 01:14:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4eb23a-e9c7-394e-9f67-81c19d241158 | 2.9741 | -60.6782 | 2026-03-13 01:14:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fe7247f3-83d5-35d5-b89c-7451a1150299 | 2.3127 | -60.2351 | 2026-03-13 01:14:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f2825259-36fd-3c35-91a5-3f95c7fb27ae | 4.2755 | -59.907501 | 2026-03-13 01:14:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ea77512f-5e72-32a8-8fd4-3e6712a3a87a | 4.2723 | -59.9212 | 2026-03-13 01:14:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3a8630-9719-3591-876f-4d5068197c5b | 3.0099 | -60.5676 | 2026-03-13 01:14:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aba65d6f-8e9d-3c8b-a142-49b474ac4ee3 | 2.3028 | -60.232899 | 2026-03-13 01:14:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ca3aba4c-efb2-309b-ac2f-a1dca9f42c0f | 2.3012 | -60.239899 | 2026-03-13 01:14:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c85a1558-ef71-333f-8ab2-3c3c01d8d223 | 2.3111 | -60.2421 | 2026-03-13 01:14:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cc525cf4-e291-3aef-aac8-9a31c846346f | -10.026 | -36.324 | 2026-03-13 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 72.8 |
| bd144102-c226-39b9-8a6b-c1e3ab825b63 | 2.31163 | -60.23285 | 2026-03-13 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 858e0186-eebf-3532-b4e8-10a65545c10e | 2.31973 | -60.24108 | 2026-03-13 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| cc165048-3887-355a-a97a-cb5e93d4a338 | 4.27737 | -59.9129 | 2026-03-13 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 6fc05e1d-9419-3a44-a3f8-f4dcc18517b9 | 4.28867 | -59.90919 | 2026-03-13 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 22.6 |
| a6ec2162-ab48-36e9-a06b-64584833782c | 4.28543 | -59.9335 | 2026-03-13 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a60a994c-88fb-327c-8532-b623f6f630a5 | -10.0255 | -36.351 | 2026-03-13 01:30:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 3611c699-dd72-32b8-b83b-21e0b5b55a0f | -10.026 | -36.324 | 2026-03-13 01:30:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 143.4 |
| a207ce66-a31a-38a3-ae81-11fb47967761 | -10.0453 | -36.3205 | 2026-03-13 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 92.1 |
| ccecf53c-e410-36d2-ab71-f732d1ef30bc | -10.0255 | -36.351 | 2026-03-13 01:40:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 114.3 |
| af0b28a6-c74f-38cc-b854-35a3d9b84f50 | -10.026 | -36.324 | 2026-03-13 01:40:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 313.0 |
| 1df9e552-2e64-3857-8801-2f9732ddacea | -10.0453 | -36.3205 | 2026-03-13 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 1cb4db4d-e45f-3a53-8500-4b9d79131a18 | -10.0255 | -36.351 | 2026-03-13 01:50:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 194.7 |
| 1a6f4cff-fb77-3df2-971c-8e83066430b2 | -10.026 | -36.324 | 2026-03-13 01:50:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 350.9 |
| b8d81298-58d6-3547-9152-099cc7b2582e | -10.0448 | -36.3475 | 2026-03-13 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 63ae757f-2cd9-3ca6-9d31-3eb340c53ada | -10.0453 | -36.3205 | 2026-03-13 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 151.0 |
| f7294d73-9231-3285-9264-5da4825cd4b0 | -10.0453 | -36.3205 | 2026-03-13 02:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 46754632-3c0a-38a1-bcfa-6e235051dd97 | -10.026 | -36.324 | 2026-03-13 02:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 149.7 |
| c98b6ca9-19a3-3c11-83ad-94cca2caf483 | -10.0255 | -36.351 | 2026-03-13 02:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 88.9 |
| ce44c930-8efc-3843-9c36-ce63d92de9a6 | 3.0726 | -60.8603 | 2026-03-13 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e74c1024-c02e-3881-9127-3fd5ce793157 | 3.0727 | -60.8414 | 2026-03-13 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| de87cdb7-f572-3424-9c7e-2a374e20d9ee | 3.0726 | -60.8603 | 2026-03-13 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 131d387f-0922-328f-94f9-c46ef70caa70 | 3.0185 | -60.5769 | 2026-03-13 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 06f36b1f-68f6-3b60-843c-05fd18e78047 | -10.0087 | -36.2192 | 2026-03-13 02:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 126.9 |
| 5919dca9-5988-3dbe-b23c-163ee952c407 | 3.0002 | -60.5772 | 2026-03-13 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0c555e6c-ffab-306d-b2c3-4c8b602e025c | 3.0185 | -60.5769 | 2026-03-13 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b5761a36-fb32-3869-adec-298ef71a4622 | 3.0002 | -60.5772 | 2026-03-13 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 05224073-2703-3fc5-9d17-800b8b6b69c1 | 3.0185 | -60.5769 | 2026-03-13 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 84b6890d-3229-395c-bfbc-259e1a627d6a | -10.0458 | -36.2935 | 2026-03-13 03:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 283.3 |
| 18ab25cb-3820-37ee-b0a3-656c94e6c61c | 3.0184 | -60.5958 | 2026-03-13 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fe8f889f-edb2-36d0-8e3d-3723882ceb5a | 3.0002 | -60.5961 | 2026-03-13 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f9380f58-b5f5-30e5-aaa7-975e8923cbb3 | -10.0087 | -36.2192 | 2026-03-13 03:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| c1516d2f-6380-3223-a189-faf85fbd0c45 | -10.0453 | -36.3205 | 2026-03-13 03:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 118.2 |
| d99c9d94-01eb-3c4f-8a29-b9e8fd86adee | -8.30361 | -35.96053 | 2026-03-13 03:23:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78700a40-31b1-3e8f-9968-5be3de48033a | -7.54103 | -37.05503 | 2026-03-13 03:23:00 | NOAA-21 | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8cb61531-160a-3a6d-aa73-5124abfd9c21 | -5.52917 | -35.51919 | 2026-03-13 03:23:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 261c32c6-d1de-340e-8bfc-ffaf8e18205e | -8.2996 | -35.95987 | 2026-03-13 03:23:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 20.1 |
| d68ba3fc-80e7-3540-a2e4-fb752e7387d9 | -5.52509 | -35.51854 | 2026-03-13 03:23:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1eb0799a-ebe4-3113-837e-77858f68d530 | -8.3747 | -42.26081 | 2026-03-13 03:25:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7db999e2-3509-34cd-a71e-9f0c757dd131 | -10.01037 | -36.21363 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 8be36240-3060-3d65-aeb7-b5f24eb309a5 | -15.26128 | -39.27311 | 2026-03-13 03:25:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b0ca16a0-9cb7-3964-87bb-2baf4b334768 | -12.67885 | -38.48869 | 2026-03-13 03:25:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b48a934c-6382-36af-92e1-5fa8b77862c3 | -11.94683 | -41.32903 | 2026-03-13 03:25:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9c83aac-8b9c-3136-8cb6-fb8cda899809 | -10.04426 | -36.30237 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 8.5 |
| eac7d9d8-867a-3ddd-9422-a2101a7c569e | -15.2604 | -39.27772 | 2026-03-13 03:25:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ba9624d-99eb-34db-adfd-e0afc2425383 | -10.02685 | -36.3317 | 2026-03-13 03:25:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ba72fbc-6713-3780-8484-7b357a3f5a1b | -10.00977 | -36.21708 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 7fcd8175-1a46-3fea-bf10-0885568142e5 | -10.04545 | -36.29542 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 945f9b11-7568-3bfe-b202-884e922f6168 | -10.04826 | -36.30302 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c98498c7-bd39-37e3-9da0-2e73e2e312fa | -9.13008 | -41.04246 | 2026-03-13 03:25:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8445c75a-1291-3657-9228-98b29b7a8e7c | -9.12896 | -41.0423 | 2026-03-13 03:25:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6fb87ad7-aa32-3d33-bc12-6c0ecf15346b | -8.37436 | -42.25797 | 2026-03-13 03:25:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 25cfa28e-997e-3343-be25-b0b40b9bb64c | -10.04885 | -36.29954 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 25.9 |
| b8221445-57ec-31eb-9f95-98ff40448502 | -10.04485 | -36.29888 | 2026-03-13 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 25.9 |
| e14483ac-d2e9-3013-ab54-dfb46319e0dd | -10.02382 | -38.12961 | 2026-03-13 03:25:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3c5419f5-0916-3e4b-86e3-fe99b33bfc85 | -10.02625 | -36.3352 | 2026-03-13 03:25:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
