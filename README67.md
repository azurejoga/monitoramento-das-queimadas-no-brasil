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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e2286bf-5b2c-344c-823e-d38be9b9a02a | -17.0184 | -57.5178 | 2024-10-23 13:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 6c915cfc-ce18-339f-8a54-86af6c9d3dc8 | -17.0188 | -57.4973 | 2024-10-23 13:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 0b5cb214-0e3d-3de9-83db-53b260773f75 | -17.7637 | -57.5732 | 2024-10-23 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.0 |
| 3151b221-4f0a-3c35-93c6-347a2968f190 | -17.744 | -57.5756 | 2024-10-23 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 60ac048d-25cb-39d1-92ca-c43777b4efe0 | -17.764 | -57.5526 | 2024-10-23 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| c78a6af8-2057-36d9-9df0-1e87e0250cbb | -17.9664 | -57.2398 | 2024-10-23 13:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 4e7068d5-96e9-390d-8fdc-7eb2227c8096 | -17.9667 | -57.2191 | 2024-10-23 13:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 9221884e-63f2-3300-b550-bb799b87a66e | -18.0636 | -57.3308 | 2024-10-23 13:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 18d3d2a2-7b9e-3ce6-8218-938a6dc0b5e1 | -18.3203 | -56.2195 | 2024-10-23 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 47663551-cbdf-3e2e-9924-f185026dc53c | -18.3004 | -56.2222 | 2024-10-23 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 79da29ed-579e-39f5-933c-2746404fffb5 | -19.641 | -56.9988 | 2024-10-23 13:26:56 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| e921c296-8d8a-3a4c-b81a-31749aa2cc15 | -19.6407 | -57.0197 | 2024-10-23 13:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 0a7fc2b8-bd17-3c52-92de-c8bab6ddcedc | -3.8329 | -42.4533 | 2024-10-23 13:35:28 | GOES-16 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 4fe6cd57-e429-30fc-ba56-c276c592928b | -5.2665 | -41.1899 | 2024-10-23 13:35:36 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 16c4ae4a-dc9b-34b6-9203-a18a56ddbdcd | -5.2479 | -41.1671 | 2024-10-23 13:35:36 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| e4d6d743-c58c-33fa-8d18-29e55822b904 | -5.2667 | -41.1657 | 2024-10-23 13:35:36 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 307560d9-1cb5-3159-b6c3-f71a20a73dc8 | -11.1157 | -48.6343 | 2024-10-23 13:36:09 | GOES-16 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ee790652-289a-3c2d-8d76-9b6514bb84de | -11.0967 | -48.6366 | 2024-10-23 13:36:09 | GOES-16 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ec14af97-1521-30fb-b678-55513bc831c4 | -12.9938 | -47.164 | 2024-10-23 13:36:19 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7d7366b0-81f2-34cf-b39e-2004a3cefe54 | -15.9081 | -51.7383 | 2024-10-23 13:36:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 44a97c67-238b-3e9d-bc91-371ccb813194 | -15.9077 | -51.7598 | 2024-10-23 13:36:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a5f52a7f-4f4d-3b81-a79f-0e9721309750 | -17.0213 | -57.3333 | 2024-10-23 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| e3bc8b57-2d16-3a1e-a286-ef1f8baa5914 | -17.0014 | -57.3561 | 2024-10-23 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 40fe29c0-b9ca-3e1b-a144-618ff824bbaa | -17.0188 | -57.4973 | 2024-10-23 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| c736428b-c3c6-3d7d-ae20-eb2444743e84 | -17.0184 | -57.5178 | 2024-10-23 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 5f1cd461-0173-3d16-b6b9-86a563cfbc6e | -17.0194 | -57.4563 | 2024-10-23 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 2714cc8a-7dd3-3324-9a83-41e9e3a0cabc | -17.021 | -57.3538 | 2024-10-23 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 6763dc2e-50d8-3713-b39a-1dddf246daff | -17.764 | -57.5526 | 2024-10-23 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.7 |
| 4c5f989c-2312-3559-b717-260297b8c9e4 | -17.744 | -57.5756 | 2024-10-23 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.6 |
| b882123c-c07d-301c-b507-0a983319b43c | -17.7637 | -57.5732 | 2024-10-23 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 200.8 |
| 7d7e3c18-a300-3b53-8166-a9c48ea47090 | -17.7644 | -57.532 | 2024-10-23 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 157e8e66-028a-3de9-84fe-280f355f1b29 | -17.7443 | -57.555 | 2024-10-23 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 9ca72765-5ed8-3108-af4c-8103bf1521ae | -18.0632 | -57.3514 | 2024-10-23 13:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| c06468a9-abaf-3e1a-adcd-0c99521df63c | -18.0636 | -57.3308 | 2024-10-23 13:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 245.3 |
| c67e5c95-d419-3658-b726-36fa8c966f5b | -18.16 | -56.3243 | 2024-10-23 13:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| e257740f-cb70-3454-a22b-084403c55aaf | -19.641 | -56.9988 | 2024-10-23 13:36:56 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| a8cdcb8c-c2b6-3204-8937-48f803699f98 | -19.6407 | -57.0197 | 2024-10-23 13:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 856692be-6811-3579-8d5e-00df5248de6a | -3.3459 | -50.3239 | 2024-10-23 13:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c30003cc-8b05-3411-ac9c-46b50dbc1f69 | -5.2665 | -41.1899 | 2024-10-23 13:45:36 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 124.6 |
| 7cc29724-0885-385a-a421-43a4f9690c34 | -5.2667 | -41.1657 | 2024-10-23 13:45:36 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| ab0de87a-5212-34eb-9c77-0a573f28a88d | -13.4211 | -43.1497 | 2024-10-23 13:46:21 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 73.8 |
| f3c69e07-6a2d-3cfb-bbcf-7a6db94afec1 | -15.9081 | -51.7383 | 2024-10-23 13:46:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| bba1e585-e005-3f27-8fb4-355f75953747 | -15.9077 | -51.7598 | 2024-10-23 13:46:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| da4d974b-25f9-3253-9ba1-8a399a6d953e | -17.0213 | -57.3333 | 2024-10-23 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| c847a6c1-8eb6-31ff-9c11-24147d095de2 | -17.021 | -57.3538 | 2024-10-23 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 6b4b5b5c-7b2a-3340-9aa5-cb9b8fb83c6e | -17.9432 | -57.4486 | 2024-10-23 13:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 318919dc-1c03-3177-993c-078e5f85e2aa | -18.0236 | -57.3563 | 2024-10-23 13:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 7d3c9bbf-d376-326b-8821-352dd3b5f9bd | -18.0632 | -57.3514 | 2024-10-23 13:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 144b297d-82e3-3aaf-84cb-cc1f6a43685a | -18.0636 | -57.3308 | 2024-10-23 13:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.8 |
| d7cf0b15-ec81-32d9-aea8-767a9cc60b26 | -18.3008 | -56.2013 | 2024-10-23 13:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| d7ac0a30-c027-34c9-93ee-0aaadf9dfd2a | -18.3004 | -56.2222 | 2024-10-23 13:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 4588349a-e9f9-341c-933d-b84ae2a93a56 | -18.2633 | -56.0812 | 2024-10-23 13:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 2ad2a1fb-5a9a-3878-af22-4ae721fb1330 | -18.2832 | -56.0785 | 2024-10-23 13:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| b7b09f19-d5e5-357e-83fe-7ebd56776cf8 | -18.2435 | -56.0839 | 2024-10-23 13:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 5e5a1e5b-b91f-3576-9ee7-8eba7d9c7456 | -18.2439 | -56.063 | 2024-10-23 13:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 0dc125fd-41e2-3134-910f-db5f6a5024a8 | -19.6407 | -57.0197 | 2024-10-23 13:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 0faff012-e3b7-3af2-bb0b-2bdf94d2b52c | -19.641 | -56.9988 | 2024-10-23 13:46:56 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |


