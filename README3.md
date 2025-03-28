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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3aa5e8e-ebcc-3746-96a9-d53486bb5a1d | -19.60582 | -40.62531 | 2025-03-28 04:29:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 91b6441c-f9dd-382f-8057-b2fb73738dff | -19.52711 | -44.41949 | 2025-03-28 04:29:00 | NOAA-21 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df736908-990b-342b-be55-86ab2d3e563a | -19.28623 | -50.11226 | 2025-03-28 04:29:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61592180-af44-3d9d-974f-4015f5526f97 | -19.28683 | -50.10856 | 2025-03-28 04:29:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eee04875-ef01-35bd-8a98-7ad23e65132c | -20.60966 | -55.70594 | 2025-03-28 04:29:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 838e0d97-dd7a-360c-8868-842ce4ffdd97 | -20.59531 | -56.09942 | 2025-03-28 04:29:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26f54fc2-c9d0-3041-9b34-34ffa68b9428 | -20.99778 | -51.79298 | 2025-03-28 04:29:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dc93eb0b-d272-3a61-b982-53e83930d448 | -20.59959 | -56.10041 | 2025-03-28 04:29:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1474525f-18d8-3078-a915-2a6fd1fd89ee | -23.39915 | -47.00808 | 2025-03-28 04:29:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ca67def0-840e-3545-9858-6ce1cde0985c | -21.19725 | -44.93648 | 2025-03-28 04:29:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79045005-fcd5-3db8-97f0-cdfc6d313db2 | -18.71616 | -41.78843 | 2025-03-28 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e301b7c7-2402-3e72-a2b5-2cdad973dc9e | -20.58063 | -44.57712 | 2025-03-28 04:29:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6671d3fa-d015-328a-98d9-ae19bc18118d | -20.13812 | -50.71973 | 2025-03-28 04:29:00 | NOAA-21 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a3f6f079-a8cc-35c6-b3d0-74033f6ac15c | -22.04946 | -47.91536 | 2025-03-28 04:29:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34b13254-5754-3588-999d-5b1e35ac2733 | -18.00246 | -52.85573 | 2025-03-28 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 150b582d-0f75-3493-96be-fc2661e2e04e | -21.11569 | -55.66379 | 2025-03-28 04:29:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a839c95-f54d-3741-b46a-766b7db0c852 | -18.3341 | -54.27413 | 2025-03-28 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1af0d897-4059-3f11-9bbe-39c62f63de2f | -20.65863 | -48.45261 | 2025-03-28 04:29:00 | NOAA-21 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c3cda3b-6560-3c49-b17e-ef6d5291b159 | -21.64497 | -48.64593 | 2025-03-28 04:29:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc27b47b-0a6d-38a5-8850-bbce7d2618a4 | -20.29307 | -50.00933 | 2025-03-28 04:29:00 | NOAA-21 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56d2a7ac-c52e-3cfe-8370-811f470d4c2c | -22.89349 | -49.24044 | 2025-03-28 04:29:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3072dd0a-8f93-3e1f-a216-8f632fce3bb0 | -19.144 | -51.56715 | 2025-03-28 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89fcf819-51fd-32f7-871a-3a49a184066c | -19.48047 | -50.98389 | 2025-03-28 04:29:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd1ac05e-2623-3a9b-8fb0-72765bbb3430 | -18.82643 | -53.43755 | 2025-03-28 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a47b2221-f549-3c0a-93a9-d142968ec477 | -20.66199 | -48.45316 | 2025-03-28 04:29:00 | NOAA-21 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7ad93c3-01b0-3d24-bf07-b1a04fb5691c | -22.15168 | -56.12181 | 2025-03-28 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1315d0f6-8d1d-35ef-813e-1514e863ebd1 | -23.42461 | -47.29412 | 2025-03-28 04:32:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a293c2d8-2cb6-3830-84bd-e7d4e849aab8 | -22.0738 | -56.46789 | 2025-03-28 04:32:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 442727c1-9f2c-32be-8507-f7ee51014900 | -22.19115 | -57.08244 | 2025-03-28 04:32:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 810aecfb-b000-394e-9f2e-ff3f778a836a | -22.07133 | -56.46874 | 2025-03-28 04:32:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aad64828-b90c-3eea-b1ff-0e3a256ad0b3 | -22.19558 | -57.08346 | 2025-03-28 04:32:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8531dad-5734-35f0-be3d-ac06340e34f5 | 4.66752 | -60.89909 | 2025-03-28 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1aa6ea4a-b145-3afe-91fb-49787ad8be9e | 4.66921 | -60.89877 | 2025-03-28 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8f451e2-d7a4-3a6f-b4a6-6fb00ee91a14 | 3.96779 | -61.57872 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a06620b-9e1c-3c60-94d6-f24d747aabe0 | 3.96635 | -61.56877 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23153de7-d25e-394f-83db-92cc954afa8c | -2.83219 | -52.12412 | 2025-03-28 04:49:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc17a1c1-d199-3085-a79a-783d73440a3d | 2.17991 | -61.81319 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aed08a4-8811-3587-b237-9a7018faba65 | 2.73609 | -60.39443 | 2025-03-28 04:49:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66ca9bba-bbc1-3871-a568-1702e79f8e47 | 2.73099 | -60.39919 | 2025-03-28 04:49:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8459bd6e-3729-39b2-ac93-947443b165f3 | 2.30665 | -61.61487 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3ecaf95-31d1-31d8-beae-b7b263021f0a | 3.96419 | -61.51009 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adafbb40-5773-3923-ab3b-9f472ac7a7e8 | 2.31218 | -61.6126 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ce8531e-ec07-37ea-b207-e47111fe337f | -5.23052 | -43.52101 | 2025-03-28 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5a9862f-d521-3cf8-bd4d-782955bfd103 | 4.07581 | -61.5504 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43618878-1a21-336e-8ceb-b836cb4aef2d | -5.23096 | -43.51789 | 2025-03-28 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80e451ee-3fbf-354d-899b-1c9463e17e88 | 2.73157 | -60.40306 | 2025-03-28 04:49:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8da0b4da-ec85-3557-9c85-48b7902426b2 | 3.98352 | -61.51195 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82a306a6-76a1-325b-8964-07b3cdfddc15 | 3.96347 | -61.50515 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9d2ffd-0bca-3ad2-8055-8be33d796469 | 3.99043 | -61.51579 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29025619-8ce9-3bd1-b811-e8090cff9f2b | 2.42018 | -61.2058 | 2025-03-28 04:49:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c5b200-4dec-3700-8782-ef6d15b81c31 | 2.41422 | -61.20673 | 2025-03-28 04:49:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e5f4c8-8cd5-3310-b024-a79178978c77 | 2.73667 | -60.39829 | 2025-03-28 04:49:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b060fc7-7e3d-3647-b3e8-3554135fd130 | 3.99114 | -61.52065 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 676ababa-db7e-3326-a0a8-bb64992f7849 | 2.18061 | -61.81786 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36109201-c1a1-39d6-90f0-9d97605e31a6 | 3.96706 | -61.57365 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46b29574-a900-35bd-bf85-a64cdeca7d90 | 2.3115 | -61.60797 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c3d5a1e-a737-381d-a284-3484c8aa8879 | 2.30543 | -61.60919 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f8df178-61ad-3f56-867a-038a1d45edb3 | 2.30594 | -61.61026 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47c02e25-3a26-3381-919c-636903f0528d | 3.9704 | -61.50912 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 073d38f5-bb8b-3c45-97a3-a3f2ccb86e7f | 2.30609 | -61.61374 | 2025-03-28 04:49:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f33828b-48da-3ec9-8832-5f5eae7885c7 | 3.97112 | -61.51403 | 2025-03-28 04:49:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c06e6d5e-20ab-3552-898d-a7c752c4a4f4 | -12.45542 | -41.46752 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| aba6b17e-bc0b-3a0e-87d0-340eca5835bc | -12.44792 | -41.46126 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fe9dc75-c82d-35ef-88d2-b11ae4f380d4 | -12.45215 | -41.4383 | 2025-03-28 04:51:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 634736d4-78e3-3f60-9dfc-4a81ed3da76f | -12.45051 | -41.43726 | 2025-03-28 04:51:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de624d47-991d-34cb-a94a-a3c1f5b9331f | -12.46207 | -41.46741 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4ba23b07-0efc-30ff-a985-c666c96e2aac | -12.45991 | -41.47301 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ca4831fd-723b-3f37-97ed-7a44838b37bd | -12.45292 | -41.43157 | 2025-03-28 04:51:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2083f52-578c-396e-91df-23fd6b068e6b | -8.1168 | -43.12392 | 2025-03-28 04:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5fd96a2-82cb-30a0-8921-59d49ef33265 | -12.45609 | -41.46177 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5ab04313-3a0a-3f86-9c83-d9b20feb0b75 | -12.76611 | -45.4109 | 2025-03-28 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84ee27cf-2233-317d-ae24-a98f1826ee2c | -12.76648 | -45.4079 | 2025-03-28 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aed16de3-7718-3856-ab33-993f2c4e81e8 | -12.45396 | -41.46676 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb999cae-c572-3a11-bdd1-4229b815be61 | -12.46059 | -41.46678 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9d1970ad-f580-36e8-ab1b-6c2f0bf1d0e0 | -12.45455 | -41.46134 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ed98bfa7-1c1b-3d6e-9d1b-6a1d4ffcd65b | -12.44945 | -41.4618 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 936cf97f-34cc-376e-b8f0-843f91cc9a2b | -12.77158 | -45.4086 | 2025-03-28 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 795f5aee-3fd8-3ef5-8892-d25334ea46da | -12.75556 | -45.41245 | 2025-03-28 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40076860-d5d0-3f0f-95d8-f3c73c87543f | -12.76102 | -45.41018 | 2025-03-28 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cd7500f-2d6b-3aa0-822e-c99fe1f53261 | -8.11072 | -43.12687 | 2025-03-28 04:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 030ba728-2716-3c91-a3ab-ea70ca298c7a | -12.46119 | -41.46123 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e769cc86-0974-38f6-84f6-832b2f8fab88 | -12.45504 | -41.45678 | 2025-03-28 04:51:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c3038c0e-cb57-3acd-87e6-843d17bff65a | -12.76065 | -45.41318 | 2025-03-28 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff7017e7-eb31-3a79-9463-36a83c9fd1e7 | -12.46274 | -41.46165 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7056bcce-5305-3109-9b31-7adb1f89a264 | -12.46168 | -41.45676 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 22133750-47a3-3ec7-85a2-2a5e6b808de5 | -12.46134 | -41.47369 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 800424b8-8cb6-3f12-a204-93655094a373 | -12.45124 | -41.43048 | 2025-03-28 04:51:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f72b6acb-48a7-3ebf-b3b6-68f379a789b2 | -12.45661 | -41.45725 | 2025-03-28 04:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4fd88aec-de41-30b2-be41-ecdf629bae6c | -8.11629 | -43.12763 | 2025-03-28 04:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a226e89-51d3-31fb-8130-a7beb6ef8206 | -18.33247 | -54.27276 | 2025-03-28 04:53:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66ec8f76-2273-317d-b0de-8522fac7664e | -15.94957 | -52.31718 | 2025-03-28 04:53:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15651cb8-ff73-3154-9436-968afefdc641 | -18.00006 | -52.85569 | 2025-03-28 04:53:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d04d019d-04ef-3f8b-a0ee-7126e96ac05e | -18.33304 | -54.26906 | 2025-03-28 04:53:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 42c3335a-5cf4-3145-81f1-d451db8ab27b | -15.85705 | -54.13105 | 2025-03-28 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4db44b21-8ffa-3483-bbf8-60b6c7f9eaf0 | -20.5943 | -56.10159 | 2025-03-28 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2642f4bb-3dd1-3988-bc29-cd7ac95a5bd9 | -22.07088 | -56.46906 | 2025-03-28 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ae77f00-d5b9-3576-88ae-1a0edffdfb5c | -19.28345 | -50.11215 | 2025-03-28 04:55:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c411da7-cd51-340c-beb8-79f9e122d692 | -20.76291 | -46.76928 | 2025-03-28 04:55:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ea04869c-f48a-38bd-be2a-40b94548b073 | -18.53859 | -56.1848 | 2025-03-28 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8efcc3a6-fac4-3759-931f-29c0786c35ca | -19.28752 | -50.11277 | 2025-03-28 04:55:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README4.md)
