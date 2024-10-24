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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3b201f-19b2-3034-8253-9acda7701c8d | -17.7634 | -57.5937 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 06af613e-d5ae-3a2b-ac7a-0dd3b4514ff9 | -17.7637 | -57.5732 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 8d1f24b0-e7cd-3995-bebf-19a5050c5eb5 | -17.765 | -57.4909 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 97b063bd-0e5e-35e2-8df0-92e2ea191643 | -17.7831 | -57.5914 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| fc276af2-5d0c-3479-a4b1-3a70cdc99ebc | -17.7834 | -57.5708 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| be97b777-5081-3dd3-b5f8-56f7434a5fe5 | -17.7841 | -57.5296 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| ffe15593-d7c0-33dd-a226-11d0dfd4acc2 | -17.7844 | -57.5091 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| c2515675-3c62-35cb-993e-8285f52d1493 | -17.9272 | -57.224 | 2024-10-24 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 581071fc-43a4-3f1d-8f88-bcc61377b7b7 | -18.0639 | -57.3101 | 2024-10-24 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| ab727cf6-d869-317d-a975-9acc2cf178c7 | -18.0834 | -57.3283 | 2024-10-24 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 622f9b39-d5be-36b9-bb53-193697d877ac | -18.0837 | -57.3076 | 2024-10-24 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.0 |
| bae8a2a3-67d3-3de0-8b4c-4cd1f2232bb3 | -18.1032 | -57.3258 | 2024-10-24 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 4d67b270-7286-360a-8c22-5f595ee71053 | -19.548 | -56.6143 | 2024-10-24 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| ef4917b6-3d78-368c-8910-24b29eeb84c6 | -19.5681 | -56.6114 | 2024-10-24 00:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| cbab004e-63d8-3263-b87d-c0e254e36721 | -23.795 | -55.2753 | 2024-10-24 00:37:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| f49e730e-28d6-3559-be8b-c1cbdf7ae639 | -23.816 | -55.2713 | 2024-10-24 00:37:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 118.4 |
| ae7f09bf-5827-3e4a-9c68-f2a3a9c099fa | -1.5878 | -53.3292 | 2024-10-24 00:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 0ef86ca1-3148-3563-b95d-4a0c8b46d198 | -1.5878 | -53.3089 | 2024-10-24 00:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 427a23bd-99ac-31d0-aaff-3d783f8ce471 | -1.6062 | -53.3087 | 2024-10-24 00:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0cd2bbfb-6b18-365e-90b1-56455078a569 | -2.9578 | -50.4198 | 2024-10-24 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| c50852a4-b345-372b-83bc-4a1bb8405914 | -2.9763 | -50.4193 | 2024-10-24 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| e0f6039c-66dc-3ab3-afb3-ab57cd715257 | -3.0745 | -53.8252 | 2024-10-24 00:45:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ea981ba7-bf44-3432-882d-e04ad725c705 | -3.0918 | -54.1465 | 2024-10-24 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 16912291-f320-378d-bf3d-b7b768986fa7 | -3.1101 | -54.1661 | 2024-10-24 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2656ef5e-ebfa-3eff-889c-1b9d5b59be0c | -3.1102 | -54.146 | 2024-10-24 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a3e7ab12-4176-3844-9799-3ce56105baff | -3.1454 | -45.4753 | 2024-10-24 00:45:24 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d43118fa-9935-3270-927b-6a171fb97dc3 | -3.1422 | -50.4562 | 2024-10-24 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8e6d1c26-bacb-38cb-92a5-5063494abf42 | -3.164 | -45.4746 | 2024-10-24 00:45:24 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0a19d825-7983-3226-a6f9-499d7154b263 | -3.1641 | -45.4521 | 2024-10-24 00:45:24 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d89f6c34-61c5-3f4c-bb12-1e99e4b8f5e8 | -3.1606 | -50.4766 | 2024-10-24 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5c0717f7-ae26-3fb3-8509-cc81e4b70813 | -3.1607 | -50.4556 | 2024-10-24 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| eacfede6-1116-3951-878d-bc18ae69909f | -3.7066 | -41.6997 | 2024-10-24 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| ac022b1a-42c4-3e67-8281-695330a875b7 | -3.7068 | -41.6758 | 2024-10-24 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| e8ed679c-516e-317e-9c5c-10146279dfde | -3.7255 | -41.6748 | 2024-10-24 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| ee27cc13-91f5-3c5f-92af-a2502c8a50eb | -3.6612 | -54.2715 | 2024-10-24 00:45:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| f91bf639-f184-3d5c-9e16-23bc43f5e272 | -3.6613 | -54.2514 | 2024-10-24 00:45:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7659c664-abdf-32f8-894d-296f53462415 | -3.6796 | -54.271 | 2024-10-24 00:45:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cf92add9-d4a1-3b51-b34d-ec0dbba0bdb6 | -4.2134 | -44.2696 | 2024-10-24 00:45:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bc080751-5056-315a-9939-924c7a6bc987 | -4.5512 | -43.9978 | 2024-10-24 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 95bb8abb-e960-3d40-8055-947b66d820f3 | -4.5698 | -43.9967 | 2024-10-24 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0f35e255-5863-38ff-95ea-c55628c19a34 | -4.6588 | -44.61 | 2024-10-24 00:45:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 78cf45e9-9058-3d15-9607-2a3107a7de9e | -4.6775 | -44.6089 | 2024-10-24 00:45:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c80ebccf-2a83-3c75-b890-73e9ec4ee2ff | -4.7766 | -46.4022 | 2024-10-24 00:45:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| dfebd44b-cd4c-386b-8eda-b21b66079f90 | -4.8423 | -45.0309 | 2024-10-24 00:45:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7f6108af-6189-3952-a3e7-a207b0d77afd | -4.9693 | -45.5199 | 2024-10-24 00:45:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| eb53c1e2-27b6-3fa1-9a13-bee992afbc95 | -5.2935 | -47.0129 | 2024-10-24 00:45:36 | GOES-16 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f3b4599f-de3b-39e0-b5e2-ad22306b4143 | -6.7238 | -40.4754 | 2024-10-24 00:45:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 4bab3404-a88f-39c2-a2b8-2117708b9bb9 | -6.7427 | -40.4735 | 2024-10-24 00:45:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 0267e4c4-1683-3567-9c37-06992872ef7b | -6.9272 | -40.8466 | 2024-10-24 00:45:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 12a55290-b938-3df7-8e1c-61688d74d5c5 | -6.9461 | -40.8447 | 2024-10-24 00:45:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 184.4 |
| 960c5529-d2a3-3538-bba5-f6d06549b9aa | -6.9464 | -40.8203 | 2024-10-24 00:45:45 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| efec1367-1180-3167-a6e8-e5b999a4c185 | -7.0979 | -45.7914 | 2024-10-24 00:45:46 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0ad50ff4-7000-3b76-b3b5-ad0bc9ef7d11 | -7.481 | -63.5577 | 2024-10-24 00:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| afa1ee2b-1e0b-37e0-8cc3-31405502557f | -10.1971 | -53.8617 | 2024-10-24 00:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 7137ed49-7c14-3fec-b726-67aa12b93480 | -12.6914 | -43.8484 | 2024-10-24 00:46:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| f345aa93-afbc-3b48-8a04-0fef4d4665e4 | -12.6918 | -43.8247 | 2024-10-24 00:46:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6df512aa-488e-36f2-ae81-cd816f2282f9 | -13.7417 | -54.0682 | 2024-10-24 00:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6873889d-d1d1-3545-a1d2-5a7cc7d8c634 | -13.742 | -54.0475 | 2024-10-24 00:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 7a90d883-2863-3119-991a-eb45d182a9e4 | -13.7609 | -54.0661 | 2024-10-24 00:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 4aa254d0-6afd-3d71-9f4f-d6aaeb50b0ce | -13.7612 | -54.0453 | 2024-10-24 00:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 77f7f829-d368-3701-aa7e-061cefb11f8b | -14.9145 | -45.1224 | 2024-10-24 00:46:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b7fc39cc-3154-3e78-898d-57010870305e | -14.9341 | -45.1187 | 2024-10-24 00:46:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 791ab7d6-8d5e-3320-880b-a4384ba1d0d8 | -15.558 | -50.6876 | 2024-10-24 00:46:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7e349caf-34e9-308a-99af-3423b388fda8 | -15.5584 | -50.6658 | 2024-10-24 00:46:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 198.3 |
| ff3a9a26-2868-35ce-9b9c-0a221252e465 | -15.5589 | -50.644 | 2024-10-24 00:46:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6dcd6841-b188-3a8c-afc9-48d1246f42d1 | -15.578 | -50.6628 | 2024-10-24 00:46:34 | GOES-16 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 55ba1b89-a0a3-33be-9b87-2c9ce298e1d0 | -16.94 | -57.5268 | 2024-10-24 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 901fb1a7-d28e-3462-8287-c7b3ab188594 | -17.0207 | -57.3743 | 2024-10-24 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 0c63d611-bb0d-3acb-b494-3c7dcf081282 | -17.2383 | -57.2462 | 2024-10-24 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 07bec521-6c7c-37eb-97bf-41ef99564630 | -17.2579 | -57.2439 | 2024-10-24 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 88807c6c-18d9-3f4a-a9f0-6c915628fb1a | -17.765 | -57.4909 | 2024-10-24 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 21d4b0ad-2165-3404-8e43-08ead03785aa | -17.7831 | -57.5914 | 2024-10-24 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| a815656a-4e9a-3277-9dd3-469e58041ac0 | -17.7834 | -57.5708 | 2024-10-24 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 3329ee19-9946-302b-ad95-69d0941f0a56 | -17.7844 | -57.5091 | 2024-10-24 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| a79a5d4b-f893-3cb7-84a1-87488f55bf4c | -17.7848 | -57.4885 | 2024-10-24 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 8f157735-99f3-3c0f-af2d-9c98a199736a | -17.9469 | -57.2216 | 2024-10-24 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| fb70eae2-934e-3f38-be1c-6027c7c003cd | -18.0639 | -57.3101 | 2024-10-24 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 7f168b58-4d51-3373-8af5-241c5a0ae3d3 | -18.0834 | -57.3283 | 2024-10-24 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 2db1c338-6d7c-35ad-abdf-90f85d01ec2d | -18.0837 | -57.3076 | 2024-10-24 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| e59ec602-9367-3770-a1ee-6c1c38c8d9ce | -18.1032 | -57.3258 | 2024-10-24 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 61e9f4b8-bce1-39c6-a832-ca6de3f934ed | -23.7944 | -55.2973 | 2024-10-24 00:47:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| 5f83b5d1-1f1f-34e7-8a6e-66e2fc438d20 | -23.795 | -55.2753 | 2024-10-24 00:47:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 109.0 |
| e8b77f4e-4594-3887-b8e3-d20b93aa4c84 | -23.816 | -55.2713 | 2024-10-24 00:47:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 2a8e7645-c5b7-3676-9513-6641135da780 | -1.5878 | -53.3089 | 2024-10-24 00:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fdaaf657-3591-32f8-b30c-b68ef823ff67 | -1.6062 | -53.3087 | 2024-10-24 00:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0a19a326-d3a2-320e-b441-ab5a18e780df | -2.9578 | -50.4198 | 2024-10-24 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f062fd98-359f-3ef7-9cb6-74799a4e2d9c | -2.9762 | -50.4402 | 2024-10-24 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0ba04f61-5704-37f8-a30d-23df13847593 | -2.9763 | -50.4193 | 2024-10-24 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e7aa720e-fdf3-3c38-abaf-4e92e2347d6c | -3.0745 | -53.8252 | 2024-10-24 00:55:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| aedd4d23-ec77-3a51-8cb9-e9324bdbd4f6 | -3.1101 | -54.1661 | 2024-10-24 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e72a3ca9-8907-3a5c-acb1-9dbaa7d054ee | -3.1102 | -54.146 | 2024-10-24 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4a3e98db-4671-34d4-b82b-267087773238 | -3.1606 | -50.4766 | 2024-10-24 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a3b36e97-681d-3919-8c2e-5e2ee80f3354 | -3.1607 | -50.4556 | 2024-10-24 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| d5d77334-76ce-331d-acab-2e2ace1d22ae | -3.7066 | -41.6997 | 2024-10-24 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| a5e82631-7ac7-38cf-8c90-a4f52bea4fa2 | -3.7068 | -41.6758 | 2024-10-24 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 15afc25a-942a-3419-9740-928ad6442094 | -3.7254 | -41.6987 | 2024-10-24 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| b9873f6f-77ea-3b4d-ba2e-fc95ff602335 | -3.7255 | -41.6748 | 2024-10-24 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 6619565b-3694-3732-872c-9b3713260d1e | -3.6612 | -54.2715 | 2024-10-24 00:55:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| c48cdca1-16e1-35e4-8063-43180a809d8e | -3.6613 | -54.2514 | 2024-10-24 00:55:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 91f83ab0-8b09-351e-a950-10221b7c670b | -4.5698 | -43.9967 | 2024-10-24 00:55:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |


[Clique aqui para ver as próximas entradas](README5.md)
