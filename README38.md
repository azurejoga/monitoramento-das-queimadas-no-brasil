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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a36d833-7cf4-3bf6-bdcb-973a102cd52c | -5.48566 | -46.34689 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41f8bde8-232d-3f8c-82a5-f5f914053879 | -2.43855 | -46.50611 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64522fa-07f4-3f4f-a3f1-37fbc6a13ca4 | -2.78424 | -55.36484 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e83fcada-7aa9-3164-9eff-beb8b3d16248 | -4.00569 | -49.96888 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1113421c-9d9b-3bef-a9ce-12b768f95409 | -3.95412 | -46.50169 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9bea6bd-e15b-3d10-815c-609e659a5c17 | -5.19634 | -43.73641 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a212cdd-9f89-37d5-9c11-484545157dbc | -2.30351 | -47.47195 | 2024-12-03 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 304f022d-bd79-372c-8269-181888b87a3a | -2.52338 | -53.98252 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8a69f7a-39c7-3d52-b44a-288cfe91ce79 | -4.06092 | -46.81617 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4af2c28d-d896-3457-82bd-c56b40384d28 | -1.72489 | -52.48229 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e285ffcf-a1c6-3e94-8111-71e63655d5e8 | -2.93207 | -46.78054 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff0db339-820a-3883-9beb-411ec1093450 | -3.34738 | -51.21567 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78e3907b-0103-33b9-812a-0f8be7386667 | -3.94764 | -48.18364 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6675c2e1-c2b6-316d-9fbe-09d095629231 | -4.6086 | -46.28829 | 2024-12-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b6fb152-76cb-3295-a828-61ae3ad8028e | -3.37407 | -46.66977 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7de7227f-a292-37f2-8517-63057a7601d9 | -3.18267 | -54.33674 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0812afee-39f9-3685-9385-ba442e0fccd0 | -2.55093 | -53.40546 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85e19cb4-cf0c-361d-bdcf-0384ee1bc28f | -2.72939 | -46.25459 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5d6c537-02c9-3e3f-9e7d-adc49cacdaa1 | -4.05045 | -46.81808 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 216a1bb4-92df-38a8-bf9d-2761b96204b2 | -2.43193 | -46.50508 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79718e46-9652-38ee-a79b-8ad76ca1b9b4 | -3.34507 | -51.20563 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d718ae01-a06c-3d1e-bfd1-1daae5040721 | -3.8948 | -46.40314 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a9277ca-5834-3706-8c4c-52ab74289a76 | -3.98271 | -46.66595 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06b9c7d3-4c4b-3ad7-afcf-97c67995035f | -5.59682 | -42.93109 | 2024-12-03 04:29:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eaae0b77-bc69-3f9e-a492-e9c4d3424939 | -3.95852 | -48.82454 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 961a9020-3550-3123-beec-b05cc40f8e47 | -3.16869 | -46.29077 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c02b5a7b-2b27-35e1-88c3-b319fd2a857a | -3.35283 | -44.35717 | 2024-12-03 04:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4f442bd-4622-3efd-95c5-91f730bf121b | -4.08729 | -46.12469 | 2024-12-03 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d68af466-1973-33a4-9d5b-552360227f3f | -3.08832 | -54.30157 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57485496-e418-3f94-804c-c4cc6104a313 | -4.43215 | -45.79108 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3b59531-28e2-3101-bef2-82513fb2fcf2 | -4.01339 | -49.96535 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 256cf240-2ff6-364a-810f-355daed7e4d2 | -3.82376 | -46.89882 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0bfdc8b-e10d-3c36-bf93-add9f8792d17 | -5.61487 | -44.76983 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f70fe4c-b41b-39fb-92eb-e7034ba6431f | -5.79737 | -46.48206 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e4a61400-afe9-3787-96eb-73165157d095 | -3.0511 | -54.50522 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8ce6a0d-90e2-3b76-8993-35fa5762c769 | -3.43009 | -53.2922 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a4582e5-bcd1-3199-95af-072d1a929b79 | -4.16984 | -48.19652 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c58ffad-4f61-3fb0-970b-5cb1a8e33676 | -5.81964 | -46.47104 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5020d20e-4899-37a4-8d69-ddecd1be940d | -3.03803 | -44.95823 | 2024-12-03 04:29:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1402bd99-552c-3f29-b3e5-90961254da85 | -2.72265 | -46.21093 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d22c42-ae3c-32c8-b10f-d54fdc514cfb | -3.31577 | -49.9346 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35cd55b4-6c1b-33dd-acda-38a2aded0852 | -3.47593 | -47.68433 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8d4f933-8f92-3934-ac97-4129794c88c2 | -3.83116 | -47.45723 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3583c896-a6a6-3dd1-a58e-1cb7b8b4c76e | -3.09549 | -52.499 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41289d77-546a-3a2c-bf19-0917e1e1f917 | -3.2652 | -46.4547 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 937637d7-7fcd-3978-a9d3-d5a59c61aefa | -3.26835 | -46.93176 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e17176aa-9426-3fc6-bd6d-5c280e4a5e8c | -4.05016 | -46.99495 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 341b2cd9-9805-3219-9b2b-0465d8663ff8 | -4.19239 | -51.19094 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d56c4051-b632-38c5-a9fc-2ac5c4ee8dd5 | -5.56827 | -44.88618 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f223d3e9-4b84-3220-9b0a-bbdfa5444df7 | -1.69891 | -52.646 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0a531c2-d070-3ae3-9417-d88020029353 | -5.56854 | -44.88525 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| faad9c9a-d4fd-3e0b-9f39-1099bf92b1ea | -6.75156 | -46.83206 | 2024-12-03 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4c56a07-7dcb-361d-bd7d-e0bab270402d | -4.04606 | -46.82446 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48743c6b-193a-3ecd-ad14-76dadb73be70 | -2.75291 | -46.12666 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96b4b8c8-4af1-32f7-96bb-2c9dc8bfe8ce | -3.93265 | -46.72545 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4db06f73-fe2f-3918-a9a1-e352779ea25d | -3.34037 | -46.0598 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33269a7b-5443-3c57-99ba-eba32374b311 | -5.80905 | -46.47302 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06d66d9d-73b8-31fe-8a48-ea50636a4b26 | -5.11733 | -43.21497 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c51ec8c0-d6b6-33cb-b489-4a627da9905a | -4.05678 | -48.3483 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b98e6717-bedc-338e-876c-6b5708a80d0a | -4.09794 | -46.94947 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc19943e-4e50-3ff2-9dc6-a1bd9e7ab771 | -3.05578 | -54.50492 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89847ac2-5083-35db-8b9f-295a964396b0 | -3.9991 | -48.30698 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b123555-3fa5-3b8d-affa-11f3fff38248 | -3.19723 | -45.47027 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9c606b9-adcc-335e-a937-65803845f075 | -2.67419 | -46.28151 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fad25b1a-9492-3860-a56b-d051e6db7e2a | -2.4361 | -54.00074 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 387bfcaf-24fa-3113-961b-e2cab2d84241 | -2.7104 | -46.1806 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85917797-d62c-3c30-b249-c90dcd47b0ba | -3.09662 | -54.01311 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 749cae41-0927-313c-9def-956fa0c2566d | -3.73911 | -52.43778 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ec87b12-e66b-3bf8-9543-c756af854956 | -3.96882 | -46.62475 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aa2aa8a-6df5-32dd-8444-454e1d1f9ce1 | -3.4726 | -49.92992 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17f43b99-700b-3539-91ae-1cba2a6cc5d8 | -3.887 | -50.07321 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fd2adf8-4186-3f2a-a59c-32789ffbe51d | -1.94842 | -53.34768 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a0d13a6-b1be-3742-9beb-0cc6cad723d4 | -4.00506 | -49.97287 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d081b4fe-3257-3521-9635-3f16cb4b429e | -3.50221 | -53.83571 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 091b07a7-bc4e-3d3d-9bd2-49a84376ce94 | -4.74074 | -45.11412 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc811f8c-5a24-381c-aa59-b0336192af7c | -3.15212 | -50.62658 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f36e9b1e-ee21-3365-8792-c7066fe03821 | -3.99632 | -48.30293 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7219d597-371b-3acd-a7b2-16bc7b3a4d25 | -3.39552 | -50.23177 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c75a4292-6bce-3aaa-88ef-e0c067831498 | -3.28157 | -46.13338 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1333bd73-8045-32b9-999b-e441a871f589 | -3.41973 | -50.83356 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cd97bd7-343d-3e55-92d2-539097e8abed | -2.03432 | -53.4967 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24cc5fc4-393a-353e-b949-d38d60aba7a3 | -4.94327 | -43.77448 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66e8d629-28d7-3f63-a23e-77252d02eefd | -2.84951 | -45.8326 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75727d5c-1419-3030-8929-30679278a6c1 | -3.82452 | -46.59136 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efd67852-8638-3d89-9b11-ab7f6c622924 | -2.33418 | -46.17489 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8bfdc5a-1431-30b9-bbb3-ffdf574f910a | -3.38221 | -45.42432 | 2024-12-03 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25e02edd-8c37-396d-ae74-8babb6309d5b | -5.11805 | -43.21022 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c0756397-ed26-3dfd-be12-559ccf2cac60 | -3.29314 | -53.66813 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d1277da4-80f9-3838-8321-e978dc63933a | -2.65177 | -46.12139 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1a0434d-fe73-39ca-bc2e-945c71b32c60 | -4.75512 | -45.65445 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de430848-b109-3387-8f57-61d940e2c9ec | -3.9663 | -47.24574 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbfc8aef-e754-360f-9eed-6b8dff5711fd | -2.47951 | -46.56886 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f3cc785-609e-3e35-b4da-87b203d2170a | -3.53621 | -50.17988 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b36819a-23c9-3601-a1d5-d9497a957f47 | -2.59603 | -47.03793 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c77212f-e9e4-33dd-9b8a-3dd69cd334c9 | -4.32252 | -48.21722 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d92c44ff-c090-37f9-8f4a-1e5fefcf39f9 | -4.39405 | -46.01268 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d338a128-0f79-3cd1-ac2c-03ea337444f7 | -5.22884 | -44.23315 | 2024-12-03 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e7a722e-ba10-36ce-bc8f-01cfe5358f41 | -3.8154 | -49.84576 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77b73adf-d94a-3adf-b778-9a28275680fc | -3.95103 | -46.39072 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75570a5c-5e4a-3969-9b9c-f5a41244d3ef | -3.02589 | -47.80239 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README39.md)
