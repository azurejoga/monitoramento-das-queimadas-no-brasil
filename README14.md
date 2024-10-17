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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 782782d2-6fe9-352b-a6ed-7a2748ea262c | -10.3593 | -67.949203 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 96999345-1461-3345-8e6f-3a1590f6c33a | -10.6318 | -69.154404 | 2024-10-17 02:00:49 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6b7700-20de-378f-b480-78497c6cc72c | -10.3479 | -67.944199 | 2024-10-17 02:00:50 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 341648aa-afa3-33fc-a4d9-fb03a4dae2d2 | -10.3495 | -67.951401 | 2024-10-17 02:00:50 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 43188b16-c62d-3067-ae1a-10c3508d6eee | -10.3544 | -67.973099 | 2024-10-17 02:00:50 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 844ae17e-66a2-3836-89e9-036b65c3cab9 | -10.3561 | -67.980301 | 2024-10-17 02:00:50 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b369a1d4-3acc-38d7-b09e-00e372c947f9 | -10.3446 | -67.975403 | 2024-10-17 02:00:50 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4a29d6bc-2b95-3f29-b556-8b9a346ac208 | -10.3463 | -67.982597 | 2024-10-17 02:00:50 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bf406f36-642e-33fd-b900-0112a54db026 | -10.3546 | -68.064102 | 2024-10-17 02:00:50 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fbb8c0a5-e5b1-3638-b742-66b0e7e93f1e | -10.3039 | -68.022797 | 2024-10-17 02:00:51 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 95a9cc19-b6eb-36da-8a7e-53fd320542b6 | -10.5907 | -69.338699 | 2024-10-17 02:00:51 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 81fae649-54a0-3831-ade3-919d55fa1fc2 | -10.0943 | -67.333702 | 2024-10-17 02:00:51 | METOP-B | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 96577280-461f-39c6-9d85-a3d53fcb29da | -10.0961 | -67.341301 | 2024-10-17 02:00:51 | METOP-B | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 59c2f94a-9c11-3fff-91da-ed0c91b06e09 | -10.394 | -69.150101 | 2024-10-17 02:00:53 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bbb175b8-6e4a-31c0-a93b-17816af356dc | -10.3955 | -69.157097 | 2024-10-17 02:00:53 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1c753dba-026c-329b-8544-a5d25ad45b77 | -10.2926 | -68.836899 | 2024-10-17 02:00:54 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 08b67ed2-ce2e-33ff-9515-e0537a328e20 | -10.4575 | -69.711304 | 2024-10-17 02:00:54 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 064f5f1c-8fdd-37be-a1c6-8e1f8535aca9 | -10.0736 | -68.053398 | 2024-10-17 02:00:54 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 29a46b80-2df3-3291-9b76-1cec65c5dad6 | -10.2039 | -69.084 | 2024-10-17 02:00:56 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 78a7060b-f050-354b-ace3-6ccb6e28d676 | -9.8156 | -67.557297 | 2024-10-17 02:00:57 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 50442f32-fe24-304a-aee1-6e37661a6e4c | -9.5701 | -66.629997 | 2024-10-17 02:00:57 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7585e6-559b-32f2-8e52-5a5d94ef7700 | -9.7808 | -67.675102 | 2024-10-17 02:00:58 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1f548800-a804-39a9-a57e-a012822f5312 | -10.1184 | -69.161797 | 2024-10-17 02:00:58 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 41c5368f-fdae-3776-8e21-2bb9b102413d | -10.0037 | -69.063904 | 2024-10-17 02:00:59 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 74d8220f-0570-3c74-b3fc-537eb654d1a3 | -9.4689 | -67.083 | 2024-10-17 02:01:01 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 176f3af8-58f0-3142-93ac-8bb4aec068bc | -9.4708 | -67.090797 | 2024-10-17 02:01:01 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9965f760-a840-3743-b639-767cd791532f | -9.4504 | -67.136703 | 2024-10-17 02:01:01 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ceae63c1-5aef-3c4f-9f81-9a0dcbd0e0ed | -9.4522 | -67.144501 | 2024-10-17 02:01:01 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f82edbef-630c-3637-b4c9-fe16f53a30d7 | -9.7679 | -68.795197 | 2024-10-17 02:01:02 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 61e9fa2f-3a1b-38d3-bb89-dafa90531bf7 | -9.7695 | -68.8022 | 2024-10-17 02:01:02 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5129c2-3edb-3d8f-bafc-8eb5fe758b37 | -9.0715 | -65.910698 | 2024-10-17 02:01:03 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22445bc7-930e-3e37-ace2-ef35e133f521 | -9.6828 | -68.556099 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 65bb8df5-5e27-3cd7-a319-4048cd862a6d | -9.6844 | -68.563103 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 44a0fd06-258b-322a-8cbe-ae17f7e2cf0b | -9.6778 | -68.579399 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| dd52a117-c9c7-3833-9f90-063b8ccd92ae | -9.6794 | -68.586502 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7923bd-6312-32f0-8983-3cb5bd3a10bf | -9.668 | -68.581703 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b0788a13-a4a8-35ee-88bc-79ea554f6c85 | -9.6696 | -68.588799 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c5ed847c-be91-3f10-ba7d-03c7435e5670 | -9.6534 | -68.562798 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 468effb4-a424-3232-b9a7-03b5180dbca7 | -9.6566 | -68.576897 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7e81a8be-9cc4-3be4-818d-7918e444a05b | -9.6516 | -68.600403 | 2024-10-17 02:01:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb14a5a-97db-3221-9f5e-9f5a6425dc54 | -9.6334 | -68.656403 | 2024-10-17 02:01:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1c28dd33-7127-39d8-93b6-e33a919be42c | -9.635 | -68.663399 | 2024-10-17 02:01:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cd374a21-f415-31b0-8879-a398b3603f65 | -9.6268 | -68.6726 | 2024-10-17 02:01:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a569347d-4240-33d7-a50a-0af2abc16e5d | -9.5684 | -68.597099 | 2024-10-17 02:01:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7625cd37-8b16-3f09-b60a-692ce117d8d1 | -9.5238 | -68.718399 | 2024-10-17 02:01:06 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 07cbefed-dfc2-3897-b61b-911e32c9fce5 | -9.4788 | -68.565697 | 2024-10-17 02:01:06 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ae3eb1e9-c109-318e-8c24-53db6701a67a | -9.3961 | -68.292801 | 2024-10-17 02:01:06 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| dc236a8c-f3a7-364a-824b-65c1a364e7ce | -9.456 | -68.556 | 2024-10-17 02:01:06 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f0ad96c3-3473-3eb2-96a7-b087bf3050d7 | -9.4034 | -68.642403 | 2024-10-17 02:01:07 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 303e4122-dcd3-3f47-bef4-a8fcee263534 | -9.3964 | -68.975502 | 2024-10-17 02:01:09 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 28a22891-708e-3f4c-95e0-e610521637fe | -9.3979 | -68.982399 | 2024-10-17 02:01:09 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e09cf73c-3a0c-3b9a-a4a7-f09002f75952 | -9.0795 | -67.720398 | 2024-10-17 02:01:09 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3ebaa5-907b-3a43-a9c1-0c49f72b0172 | -9.3338 | -68.835503 | 2024-10-17 02:01:09 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2be484-b86f-3a0d-9d01-0b7ed30d4fe9 | -9.5069 | -70.436699 | 2024-10-17 02:01:12 | METOP-B | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bc62e528-423f-3f7c-aa61-2bd91cfd3eba | -9.5084 | -70.443703 | 2024-10-17 02:01:12 | METOP-B | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7602a9bf-1714-3eea-818f-b822d6b9c8c9 | -9.0433 | -68.509003 | 2024-10-17 02:01:13 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c304444-252a-31fe-9902-929fc25fa287 | -8.4582 | -66.950996 | 2024-10-17 02:01:16 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9b026be-53e2-37b8-a78e-a21f56a43176 | -8.4484 | -66.9533 | 2024-10-17 02:01:17 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d33b8ab1-e54f-3a42-b690-0ddc414e4af2 | -8.4503 | -66.961403 | 2024-10-17 02:01:17 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff7753bd-4604-386c-bcac-c2a806b9b7c0 | -8.8924 | -71.288399 | 2024-10-17 02:01:25 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 186aaac8-d449-379b-adaa-cd4b48659f92 | -7.8889 | -72.430298 | 2024-10-17 02:01:46 | METOP-B | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b812ecbd-3ea0-3296-b2e6-4d893daae202 | -7.8906 | -72.438004 | 2024-10-17 02:01:46 | METOP-B | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 65b3c739-e416-3c7b-84cc-5e10f531da79 | -7.8923 | -72.445801 | 2024-10-17 02:01:46 | METOP-B | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| da119324-372c-32ff-80d8-c45ec9ee81c5 | -7.8088 | -73.099197 | 2024-10-17 02:01:49 | METOP-B | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0d78f1ed-414a-3d4d-9f81-311a350c7772 | -7.3379 | -72.494003 | 2024-10-17 02:01:55 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f78d7e2-03c6-3858-b2b0-0bf9075ce927 | -7.251 | -72.472702 | 2024-10-17 02:01:56 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8e51ae-ac50-3e96-addb-98995dd5667f | -2.6147 | -48.2629 | 2024-10-17 02:05:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| f4974864-5dc5-3d04-8b7e-3acc6c72254d | -2.6148 | -48.2413 | 2024-10-17 02:05:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 254b733d-2a5e-39b2-82a4-b6f3be1a8aa5 | -2.8979 | -51.6896 | 2024-10-17 02:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c56c719e-8650-3f2b-bb13-9cb267acadac | -2.9859 | -47.9925 | 2024-10-17 02:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 832a2221-1f3f-3add-b78a-b29612a91ad2 | -2.9674 | -47.9931 | 2024-10-17 02:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e3147b49-1a16-3e9e-8290-0583f9967c0a | -2.9673 | -48.0147 | 2024-10-17 02:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 0fb0fc7f-e410-368b-bdba-2e4f43941dd8 | -3.2503 | -46.8709 | 2024-10-17 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d2321458-a660-3b75-9ca0-b4917a777ecb | -3.7009 | -45.9 | 2024-10-17 02:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| de5d34ad-f6f9-3ace-bc77-37f3f43b25ef | -3.7007 | -45.9223 | 2024-10-17 02:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6a488ba2-68eb-3628-9f0c-4deb37dfb983 | -5.5718 | -44.87 | 2024-10-17 02:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 7670586c-72fd-3b97-8c61-8e64b2daa485 | -5.5716 | -44.8927 | 2024-10-17 02:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7fd86a91-25dc-399f-a6ff-841d8ed0f717 | -5.6714 | -48.6872 | 2024-10-17 02:05:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ab4610b2-f44f-351b-82f6-42cc4a10ca91 | -5.9788 | -45.3621 | 2024-10-17 02:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ee10b7d3-50ea-3f12-acf5-0296b2af8b3c | -6.7274 | -43.5589 | 2024-10-17 02:05:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 391230c1-aca4-339c-b297-370edfc30809 | -7.8727 | -45.3593 | 2024-10-17 02:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d025afdf-4f57-32a1-908e-c31d7f88642e | -10.1477 | -56.7709 | 2024-10-17 02:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9f3ac200-df63-3b74-b1e3-b11cc2c0ab5d | -10.1292 | -56.7523 | 2024-10-17 02:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0ba5416d-0347-328a-8b17-2098c77c2db5 | -10.129 | -56.7722 | 2024-10-17 02:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 0304004c-2a70-337e-a515-e8a0574bc886 | -17.1667 | -56.8232 | 2024-10-17 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 24bac0ed-12dc-368b-bdf9-44cddc7a472a | -17.2177 | -57.3102 | 2024-10-17 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| b6cd40b1-eed0-3bfa-8b31-5a5b2b3d6c9c | -17.8444 | -57.4607 | 2024-10-17 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 213a8803-d016-3300-a938-1c8af8e87108 | -17.8246 | -57.4631 | 2024-10-17 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| f22b00df-1e3c-3dd2-bca8-5d1e70398218 | -17.8052 | -57.4449 | 2024-10-17 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 1512d93c-fc9c-3815-86c9-7abbd03109f9 | -17.8049 | -57.4655 | 2024-10-17 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 6fd7ebb6-8453-359d-a865-036579bbacfa | -2.6147 | -48.2629 | 2024-10-17 02:15:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a49d0e68-08e8-36a1-baeb-ed8470d1026b | -2.9859 | -47.9925 | 2024-10-17 02:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dec7b6d1-7b3a-35d8-b32c-b8ca92a22a96 | -2.9674 | -47.9931 | 2024-10-17 02:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 7f890f96-b915-34e1-b292-1b60d624efb2 | -2.9673 | -48.0147 | 2024-10-17 02:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 6472cc7e-1346-3d7f-9000-d13ae0eab05c | -3.3526 | -53.2112 | 2024-10-17 02:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e5316b01-7391-3f75-8995-6a46ad2724a6 | -3.5086 | -51.1122 | 2024-10-17 02:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9d01c5ca-5e89-391f-95f1-904c452ff948 | -3.7009 | -45.9 | 2024-10-17 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f14bea4d-38bb-3484-97c3-946d50b33c92 | -3.7007 | -45.9223 | 2024-10-17 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 30d60b22-aecd-369a-8828-bfead5254367 | -5.5716 | -44.8927 | 2024-10-17 02:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 24a69954-42ec-34bb-a22c-fddae41eb9a4 | -5.6714 | -48.6872 | 2024-10-17 02:15:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |


[Clique aqui para ver as próximas entradas](README15.md)
