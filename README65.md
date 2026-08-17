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
| c1b25ae6-d9f5-3e2a-887b-ffe9f9e0e91c | -8.72444 | -62.89786 | 2026-08-17 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d29cc5f-54e4-3c48-b7b5-9f2347505dd2 | -6.86337 | -70.06179 | 2026-08-17 06:37:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35c40681-10cb-39cf-bd37-7d191d52348f | -9.34882 | -63.56755 | 2026-08-17 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d590b1f2-c4d9-314a-b917-936995756650 | -8.73812 | -62.90725 | 2026-08-17 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24150568-2a4a-39e9-88e3-ec70dd2e74b8 | -8.54173 | -69.99308 | 2026-08-17 06:37:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe55bce4-b805-3a83-8c99-c46328b47572 | -6.86225 | -70.0597 | 2026-08-17 06:37:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e04608-8e61-3f13-96d1-ecfc83a6d069 | -11.1299 | -46.5019 | 2026-08-17 06:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| bf82c361-1c7f-3005-a79b-2c3346436772 | -12.7009 | -48.5195 | 2026-08-17 06:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a60ab8bc-b528-3d4b-9c40-7f0bf63160cd | -15.9185 | -55.5518 | 2026-08-17 06:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e869b600-6c90-3af6-9ae6-17fbca4e77ab | -15.9189 | -55.531 | 2026-08-17 06:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| f3881349-35b6-3702-bee0-744bd3db9f8f | -11.1296 | -46.5244 | 2026-08-17 06:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 40b450b0-4037-3b50-b51a-0f512b9ad317 | -15.8994 | -55.5334 | 2026-08-17 06:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 90def65f-46a0-32ba-a028-66a2a019f1a3 | -15.8994 | -55.5334 | 2026-08-17 06:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 01db07b7-8791-3dae-97da-44353a5b92e4 | -11.1299 | -46.5019 | 2026-08-17 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 7a0a85ac-5f22-3988-8cd9-e6a16ef8217d | -12.7009 | -48.5195 | 2026-08-17 06:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c0655ca2-a6d1-3377-ab5f-0ad1253de27f | -15.9185 | -55.5518 | 2026-08-17 06:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cc43b2fc-bb60-3afd-96d8-f84826986e41 | -15.9189 | -55.531 | 2026-08-17 06:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 570e024d-c33b-3e43-adf8-fd4a26c2413e | -11.1296 | -46.5244 | 2026-08-17 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0fbf6ce0-a522-349c-9781-2c2f9bf6bb7b | -6.6568 | -58.9628 | 2026-08-17 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 892fdf27-470c-3d4d-bf97-5f15e448d5f5 | -15.9185 | -55.5518 | 2026-08-17 07:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 3310547b-41f1-3550-b3e6-61cacc68fbdc | -12.6817 | -48.5221 | 2026-08-17 07:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 137755d5-4c49-3e28-a1e3-c7a2ad12bb14 | -15.9189 | -55.531 | 2026-08-17 07:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 89e5f7d5-5367-30a9-9eb0-ead293635854 | -10.5085 | -50.0228 | 2026-08-17 07:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 05d33897-64c5-3755-a152-de6741d82131 | -15.8994 | -55.5334 | 2026-08-17 07:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0a5ee95c-e7ac-3f09-bd25-7ecabf2eb59d | -12.7009 | -48.5195 | 2026-08-17 07:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 8ea436c3-fa45-3b33-9234-8f749400b7b5 | -15.9189 | -55.531 | 2026-08-17 07:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| e7300ba3-ce1c-3771-9f97-77e59401728a | -15.9185 | -55.5518 | 2026-08-17 07:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d8ad5742-9375-3d42-ba2a-72b40bf6a142 | -12.7009 | -48.5195 | 2026-08-17 07:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 771c721b-4145-3d10-a28f-4faea37a3ff9 | -6.6384 | -58.9636 | 2026-08-17 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| bb6e9d34-7d06-3755-b6c1-bfeded71c7a4 | -15.8994 | -55.5334 | 2026-08-17 07:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 52c89fac-4f00-3aa4-92a8-c3ee9cc258bd | -10.5085 | -50.0228 | 2026-08-17 07:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 27a9d939-8c1b-3559-b4dd-df78ebd9ee6a | -10.5275 | -50.0208 | 2026-08-17 07:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| a48a256c-cba1-344d-9b93-c7027e9e664e | -15.9185 | -55.5518 | 2026-08-17 07:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0612de30-88f7-3a2f-bd88-c37147146b66 | -15.8994 | -55.5334 | 2026-08-17 07:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3660bb70-189a-3a53-a131-2eab652a42c3 | -15.9189 | -55.531 | 2026-08-17 07:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1ab698a0-fe35-3a9b-8b7e-3f17e14f1a28 | -6.6568 | -58.9628 | 2026-08-17 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f4c75987-53b5-378e-b922-41738af04622 | -6.6568 | -58.9628 | 2026-08-17 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 765a25a8-5e31-3fdb-b034-3a7a207450e5 | -15.9185 | -55.5518 | 2026-08-17 07:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| bc3b68d6-f811-3761-9d4a-692f8b1d52cb | -15.9189 | -55.531 | 2026-08-17 07:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1e1e7c58-3495-381a-a59d-0e90e06ac7aa | -10.5085 | -50.0228 | 2026-08-17 07:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 92572871-0b9b-3838-b9f9-86d7e5cbca4a | -15.8994 | -55.5334 | 2026-08-17 07:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 33aaca03-5dd1-333f-a9fe-15365a65c1f1 | -15.9189 | -55.531 | 2026-08-17 07:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 00b1600c-8839-349c-adc9-b0103eecc9c0 | -12.7009 | -48.5195 | 2026-08-17 07:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 62397aff-b725-3cae-a0d9-8a6e194c36c4 | -6.10348 | -57.74557 | 2026-08-17 07:46:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c7798cf9-3903-3e59-bc1b-528c11bc999a | -7.6124 | -60.94403 | 2026-08-17 07:46:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e932e166-8d68-3145-8149-3d952b9d2a36 | -7.54618 | -61.17591 | 2026-08-17 07:46:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 68e16ffc-4f5e-3675-b7c5-4cb67916b778 | -6.64455 | -58.95726 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 585d0ead-ee46-3414-a893-b080f8a47baa | -6.59732 | -58.96056 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e3900dd5-0d4e-3498-b092-8b5cf789bbfe | -6.62804 | -59.07499 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 256c57fd-c762-3ef9-bc9b-5aca2127e9ad | -7.37511 | -55.47643 | 2026-08-17 07:46:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 07b56ad8-581d-39cd-9010-0cc2af38aea5 | -6.78051 | -59.456 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8a1c30a9-82e7-3b29-be56-781ffb8818f6 | -6.59521 | -58.97527 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ede9e3ea-c87c-3b0c-8d43-f24d2ef9eebc | -6.59759 | -58.96586 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f9bf2898-9cb3-3841-a9ef-48901b3e95db | -6.10604 | -57.72746 | 2026-08-17 07:46:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 542761fa-dfa0-3071-8c6d-d384dddba584 | -6.11837 | -57.72898 | 2026-08-17 07:46:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9ddff921-e650-30c0-855d-1874bb0c0ae7 | -6.65577 | -58.95892 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 01c1a405-7ba0-3f17-8fc1-65487389f2f8 | -7.60909 | -60.94934 | 2026-08-17 07:46:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76a3fc29-5da4-3df9-9266-999c62ada8d6 | -8.08352 | -61.35556 | 2026-08-17 07:46:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f905a3c1-b8b3-3a23-960f-0852449dd8f5 | -7.3902 | -55.47849 | 2026-08-17 07:46:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 78376156-2769-3592-aa1d-08dd909a7361 | -8.08195 | -61.36637 | 2026-08-17 07:46:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 566bab6c-4408-370d-aac8-a0a9f15da2ba | -6.77003 | -59.75521 | 2026-08-17 07:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da742435-1a6f-38b6-abd7-d55ff6868ffd | -8.89416 | -60.55665 | 2026-08-17 07:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bfbb7d9e-317c-3c73-b504-bb28960ea8e0 | -8.94242 | -60.5127 | 2026-08-17 07:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e5e667d6-89e7-3a5d-8fa6-9a2f12128a28 | -8.89924 | -60.59529 | 2026-08-17 07:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9acad89c-0a2c-3e53-93ee-48f30e6678e0 | -9.20021 | -60.79224 | 2026-08-17 07:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 56907ab2-1438-3519-8253-29139ed1adc3 | -10.91536 | -62.76213 | 2026-08-17 07:48:00 | AQUA_M-M | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 20141c00-f8a3-37f8-a803-187a2ef83eda | -9.19921 | -60.78649 | 2026-08-17 07:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d5d4d8ef-44d7-373b-b7ac-38d6156bf965 | -8.89588 | -60.5443 | 2026-08-17 07:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c377b2cc-3c1f-33c5-a1b8-decec08b3e24 | -8.72428 | -62.90458 | 2026-08-17 07:48:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0f98d96a-aad8-384b-8ace-ccc2e566d0fa | -8.73326 | -62.9059 | 2026-08-17 07:48:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cd5031ef-e6fb-3461-9ad2-625bd380cbff | -12.7009 | -48.5195 | 2026-08-17 07:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 85e37f6d-8763-3e7c-8bd7-83c86b351d67 | -8.5211 | -54.9217 | 2026-08-17 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 9bff811b-1bc4-3311-b93d-0643d8e2bac2 | -15.9189 | -55.531 | 2026-08-17 07:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 379e9a32-7b3b-3717-8c41-74941a090269 | -10.5085 | -50.0228 | 2026-08-17 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 71aa59db-372b-3d3e-a914-fb8e00a878c4 | -8.5212 | -54.9016 | 2026-08-17 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 97d978a5-013d-3d2d-86f5-d893812bc0dd | -15.9185 | -55.5518 | 2026-08-17 07:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ad6b7d39-3380-36e9-9ed3-35ba6bdaf7a9 | -15.90549 | -55.5341 | 2026-08-17 07:50:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 8b7f95fe-ee56-3659-8931-c28ddbe367b8 | -15.90821 | -55.54171 | 2026-08-17 07:50:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 9eb53d85-8aef-3a0a-ac66-7ea1086c958b | -12.7009 | -48.5195 | 2026-08-17 08:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e2471b95-6ea9-3121-ac54-48b22bf18094 | -10.5085 | -50.0228 | 2026-08-17 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 35b4d202-ec79-3973-ac92-4c01d87c033a | -10.5275 | -50.0208 | 2026-08-17 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 66bf4efa-ecf7-36a8-a688-7ec3c40258ea | -10.5085 | -50.0228 | 2026-08-17 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a34aefdb-23a0-38d9-9899-140fad92715b | -10.5275 | -50.0208 | 2026-08-17 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| cb91682a-53b1-3171-8830-d789b3759e49 | -15.8994 | -55.5334 | 2026-08-17 08:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8ba5f8fd-115a-30a8-85b9-d37b95b3e8ef | -15.8994 | -55.5334 | 2026-08-17 08:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 14a2bb4d-c98c-34fd-ad6d-155e90673b13 | -10.5085 | -50.0228 | 2026-08-17 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8805ae04-7272-3aa5-a935-3889dc487562 | -6.6568 | -58.9628 | 2026-08-17 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1d8631eb-908f-3b61-b05f-122166769e0e | -12.7009 | -48.5195 | 2026-08-17 08:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5b50c51a-fe6e-3dd3-ac66-95be9265c5ed | -10.5275 | -50.0208 | 2026-08-17 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 68a96f30-ea8e-37d3-a150-93cf71250cbb | -15.8994 | -55.5334 | 2026-08-17 08:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5d0d443b-7add-3519-9b25-329b2a85d56b | -10.5275 | -50.0208 | 2026-08-17 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 73187ec5-1cab-32b5-b850-0a06873f840c | -15.9189 | -55.531 | 2026-08-17 08:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 874481b7-26cb-3ee4-95a6-a31865bab96a | -6.6384 | -58.9636 | 2026-08-17 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 41cd7dae-6ad2-378c-8d52-f2356ea77599 | -6.6568 | -58.9628 | 2026-08-17 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1c273fb4-64b4-349e-bfcd-535ca2bd8bd5 | -12.7009 | -48.5195 | 2026-08-17 08:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| fdb16b3b-bf9e-3d3a-8413-fb244f1eedab | -10.5085 | -50.0228 | 2026-08-17 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 1523b08b-1b45-3e9b-8bf0-ef4f0ffbe260 | -10.5085 | -50.0228 | 2026-08-17 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 06cbbf93-b540-35ef-8434-d38d81cc5225 | -6.6568 | -58.9628 | 2026-08-17 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b7a18d32-3ee5-3c89-832f-c4465070bd36 | -12.7009 | -48.5195 | 2026-08-17 08:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 04b65f2d-dce4-3956-b8cb-0d2ffdbdc6b2 | -6.6568 | -58.9628 | 2026-08-17 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README66.md)
