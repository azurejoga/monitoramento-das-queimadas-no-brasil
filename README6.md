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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72a00bdb-45d4-3fe0-9405-bcc9e0dd315a | 2.69516 | -60.23661 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7dbfa98-4ec8-352c-9679-b03f2c6e050d | 2.69448 | -60.23921 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6060c3e2-bb9d-3797-86ec-c8df5fac7a11 | 2.53525 | -60.72331 | 2026-02-19 07:05:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ebf0201c-77eb-39e7-a4b9-e665ac60446b | 2.68949 | -60.15803 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2f98cc07-7c40-38f6-ab0a-de642dafb93a | 2.68803 | -60.1481 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a8559505-c27d-3a8a-836e-dea4783de184 | 2.53367 | -60.71273 | 2026-02-19 07:05:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b43af5bf-0f66-322f-802a-beb34d04ece4 | 2.69518 | -60.23536 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 74b3d950-b1ec-393e-8d47-112ca4bfe701 | 3.07579 | -60.92309 | 2026-02-19 07:05:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54af9f7b-7b41-3b68-b69e-67fff11fcccf | 2.68309 | -60.15558 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 57923fb4-4240-3703-8e05-f8abfccba8ee | 2.68159 | -60.14568 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 118b1972-26a1-3610-aec3-199c0ec3bea6 | 2.7012 | -60.23793 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 19e48c8f-58c7-3eb2-9276-4e9270efacfc | 2.69973 | -60.2279 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e93c9fd4-440d-3eab-a338-37b2baa14677 | 3.92815 | -60.58138 | 2026-02-19 07:05:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 096e87a5-17ab-3c9b-976f-a1e9d2b01c42 | 2.65999 | -60.12857 | 2026-02-19 07:05:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6db4839-7661-3fc8-86b3-59464dfa2706 | 0.94139 | -60.25767 | 2026-02-19 07:07:00 | AQUA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 192e7350-7bb8-3778-9399-4aaea9be8a23 | -12.0196 | -45.34626 | 2026-02-19 12:31:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 476da7bc-f846-3c15-a8ee-c5938772799a | -12.2833 | -54.09348 | 2026-02-19 12:31:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| db67b442-7cc2-3909-8032-2bc3521c5d9f | -12.74918 | -54.97455 | 2026-02-19 12:31:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3d879774-ede6-3772-b9e9-89379b411ea2 | -13.04767 | -45.05956 | 2026-02-19 12:31:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 39f75afe-ca55-3e49-9b78-7ceb4d6d46fc | -14.46665 | -48.4481 | 2026-02-19 12:31:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dce3e78a-64f2-347a-a4db-d1b631dc5b35 | -12.04473 | -45.35383 | 2026-02-19 12:31:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ed58cc99-63e8-37b3-8dbc-61e72fd4aef0 | -13.27309 | -54.26649 | 2026-02-19 12:31:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 36139058-88b5-3dbf-8590-4852668eeef8 | -12.04838 | -45.32028 | 2026-02-19 12:31:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 025e61dd-6a18-3b0f-9da9-0b121ddc0b07 | -12.08532 | -50.1641 | 2026-02-19 12:31:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cadb580f-dd9b-3b83-b96e-c0aef594dc4c | -12.83918 | -52.10403 | 2026-02-19 12:31:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9e9f171-0456-3000-9251-ef0d8db3f44e | -17.92531 | -55.07748 | 2026-02-19 12:33:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d7abd881-8f56-3f7f-8a6a-fc7aab2c58fc | -17.91672 | -54.12441 | 2026-02-19 12:33:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 730e4f01-5fc3-315a-bfbf-d6e9bfa48a3f | -24.02145 | -53.64954 | 2026-02-19 12:36:00 | TERRA_M-T | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 82bbf6c1-2d10-3ef3-98a9-5291ff9327bf | -24.02294 | -53.63663 | 2026-02-19 12:36:00 | TERRA_M-T | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| fea4a690-e7b5-3fd9-a3d5-e9ad788b884e | -24.02475 | -50.49039 | 2026-02-19 12:36:00 | TERRA_M-T | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 30fc7d95-697c-33ca-86df-9a5ce20463d7 | -25.27386 | -53.98691 | 2026-02-19 12:36:00 | TERRA_M-T | MATELÂNDIA | PARANÁ | Brasil | 4115606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e130521e-89a6-30c8-bcce-33adce3a08a0 | -23.93781 | -53.5074 | 2026-02-19 12:36:00 | TERRA_M-T | CAFEZAL DO SUL | PARANÁ | Brasil | 4103479 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| c988812c-9e9a-3801-88b0-07338af0fe42 | -24.01299 | -53.64259 | 2026-02-19 12:36:00 | TERRA_M-T | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 254ac4a4-dd6c-38a0-bdb1-600b54aa8667 | -25.82522 | -53.1069 | 2026-02-19 12:38:00 | TERRA_M-T | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| a64ebf8a-d55f-3faf-b756-e51414ff43e0 | -25.81734 | -53.11241 | 2026-02-19 12:38:00 | TERRA_M-T | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 36d8c339-3eaa-320a-bdee-973253341f02 | -25.9082 | -53.51107 | 2026-02-19 12:38:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| a53cc890-4ef1-391c-9b30-25ea5ef3a834 | -27.48867 | -52.92648 | 2026-02-19 12:38:00 | TERRA_M-T | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| f3387999-497b-39e7-8949-34a6caece144 | -27.55677 | -53.04465 | 2026-02-19 12:38:00 | TERRA_M-T | LIBERATO SALZANO | RIO GRANDE DO SUL | Brasil | 4311601 | 43 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 73c8cdff-6dd1-352d-a98d-347242a12a73 | -27.3532 | -51.34556 | 2026-02-19 12:38:00 | TERRA_M-T | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 69c956bb-381c-3433-af68-899c17f93421 | -25.68041 | -52.67099 | 2026-02-19 12:38:00 | TERRA_M-T | SULINA | PARANÁ | Brasil | 4126652 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6e57cf97-cbad-3f33-8c03-73035a03131f | -25.81445 | -53.10533 | 2026-02-19 12:38:00 | TERRA_M-T | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 9fd480d9-e5d5-3006-9091-3c3a6403b36d | -12.0477 | -45.3489 | 2026-02-19 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |


