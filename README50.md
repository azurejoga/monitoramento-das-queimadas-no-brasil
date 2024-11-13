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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c2158e9-b398-3132-a036-ad7d07353968 | -3.08959 | -53.26706 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04410cbd-7813-3eb6-9bd8-4ff1d58ef45e | -3.0539 | -50.34306 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d16d30d7-8774-3aa5-960d-53df23b0d839 | -3.80181 | -52.09589 | 2024-11-13 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26611c5e-0331-3874-9e77-bf9ab886e6c5 | -3.53329 | -54.4898 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48da0592-f321-3b25-a8ef-2d551940f603 | -3.04355 | -50.33798 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b58361f-fdcd-3315-b4e4-ebf91d9aa4b5 | -3.71032 | -53.75303 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52275c51-ac8f-304a-a1f6-4e3b2daee504 | -3.4963 | -50.84365 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0479c54f-bce2-39c4-ae1e-744bb388b939 | -3.3421 | -48.95905 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1b87bb42-570c-35c9-a5bc-db0b20b84e20 | -3.34037 | -54.64389 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c14857b-4221-315b-acd2-bb4a4e780ba3 | -3.22917 | -54.86008 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca208dc2-a36b-31c5-97db-894791039c97 | -6.82404 | -46.7756 | 2024-11-13 05:22:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da2b93cd-1ad5-3299-9a83-d16f42dd92c5 | -4.32722 | -46.53771 | 2024-11-13 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3b29b36-ac0e-37a9-8694-fbf53bf01d23 | -3.20123 | -50.63427 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 397da485-6a90-3c14-ad80-73eb8b093513 | -2.88656 | -54.17259 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb75a908-4872-3ae7-ab38-cbd700e1edc2 | -3.98004 | -56.2402 | 2024-11-13 05:22:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11edeb3a-b6bb-3344-bb9c-8d63a55e6da2 | -3.31205 | -50.08601 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1f78a23-4831-3078-b1eb-343e42c4c5a1 | -2.7159 | -57.33879 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26736994-8825-383b-adc6-cc21b16db0c5 | -2.71551 | -54.68986 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e382ff0-7c85-310e-bdd4-1122fae22a05 | -3.19552 | -54.64017 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab5e85b1-79b5-38b5-81d9-ff73ecb93c9f | -2.48011 | -54.0667 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4429acf-d5b4-3487-b8a5-0418cdc82ea9 | -3.23314 | -50.66426 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e8b219e-face-3af9-b6bd-9d755368e67f | -3.25384 | -54.53158 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33c486ab-13bb-340c-8a3a-041ff1260e6c | -3.22519 | -50.29187 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07060160-a55b-3334-ac04-48f1caeb68c9 | -3.40733 | -50.31556 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c595f1e-454f-39c9-be42-195618449e9d | -3.48809 | -59.61175 | 2024-11-13 05:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd4b3c2c-3aad-3009-a266-4cf1790ba266 | -3.8626 | -49.11368 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f20bb38b-87ca-3de7-9a5e-9eab4f1b199b | -3.81197 | -52.35667 | 2024-11-13 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872699e6-59bf-384c-b27c-c5f9ff65ed92 | -3.33415 | -56.95358 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ca6ec4c-8ac1-3f0b-8f39-f03a6d23eb9c | -4.02178 | -53.98373 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc686161-5079-33b4-b7b9-a3c467d5429b | -3.05605 | -50.32904 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10b65cbf-710c-3053-bb6b-623443073bfa | -3.24441 | -50.31274 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 819fb0c6-63ad-3f71-a934-0c1d3ecb4313 | -3.43081 | -50.30822 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4752844-b951-3c29-829d-c2c7b71cffe7 | -2.5593 | -54.00509 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c53de13c-4577-370b-8b2e-c456b53319dd | -2.98644 | -51.34373 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b1df23f-9a76-30e3-984c-15191a627af0 | -4.33468 | -50.42374 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6cd80a9-37d8-3061-a20a-f01afa59ba8b | -2.74383 | -54.66571 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ebe6c24-8e05-3aa9-8731-04b8df9e2c07 | -3.10584 | -53.98055 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05b8bcbe-675c-32d9-85a1-958baea3fa74 | -3.02213 | -50.97046 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7193ee72-9a06-388c-b21c-e219167f25fb | -3.43107 | -54.53524 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a3f40e3-ec2f-3cfe-bbcc-318ed0868236 | -3.37287 | -54.64459 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e17dc1bf-32cd-30ce-9c96-5301ca2370ec | -3.09689 | -54.302 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbb8dd16-4500-38df-8718-0684d45fa82c | -8.80841 | -63.20316 | 2024-11-13 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1418431a-289a-3ca8-b970-cb6d1cc38627 | -9.47257 | -62.27368 | 2024-11-13 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f26b379-bafe-316c-a0dc-6e6214eb219f | -9.25724 | -62.30928 | 2024-11-13 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e19e1b3-6c2d-3748-b1a2-3a9242d480d3 | -8.81188 | -63.20372 | 2024-11-13 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53bd95e7-87ae-3bba-8e5e-c0148b87134c | -9.47593 | -62.27422 | 2024-11-13 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f130b21d-ac11-311c-8548-cc7f2f602d6f | -29.52214 | -49.88232 | 2024-11-13 05:27:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 9.9 |
| 3d527bc7-48ef-376c-aac4-e490a8d92fed | -29.52957 | -49.88267 | 2024-11-13 05:27:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 9.9 |
| b7567313-83c0-38c3-91bc-a0501c9e2715 | -3.0689 | -50.3326 | 2024-11-13 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d88a3db9-1b8e-34f4-a72d-9db96284023d | -4.6581 | -47.4216 | 2024-11-13 05:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f23595fe-5bb8-3879-8dc5-0b6c47f194fe | -3.3518 | -48.9689 | 2024-11-13 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 15b61344-7581-313a-8270-1c69c371a323 | -10.7235 | -49.5265 | 2024-11-13 05:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 4c667903-ee85-3170-9e83-42c372ffa4fa | -3.3519 | -48.9475 | 2024-11-13 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 06128b74-39b3-313d-aea3-958f1efa3ca9 | -10.7425 | -49.5244 | 2024-11-13 05:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7b66797a-be61-33ee-bb8f-1ecf7be26f5d | -6.5631 | -51.1126 | 2024-11-13 05:40:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 142a4a90-0dd0-3d43-a2ad-2fae7de0659e | -10.7425 | -49.5244 | 2024-11-13 05:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 79a88544-bf93-3106-8a33-3b24f3bc62c6 | -3.0689 | -50.3326 | 2024-11-13 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 40100944-19d7-321f-916d-6d4c7e27ea4a | -3.0504 | -50.3332 | 2024-11-13 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 47c61916-7596-39e2-8dfb-46ba5939376b | 1.13883 | -60.59712 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51724ba2-e34c-3a9b-8c5d-137275770cf4 | 0.62229 | -60.08813 | 2024-11-13 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 579bc65a-56da-3ea3-bb5b-fbafb403cd4e | -0.38997 | -51.75152 | 2024-11-13 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3635e197-fa26-35eb-8b77-51e3172dba6f | 4.00494 | -59.65252 | 2024-11-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0de0cb24-1afb-3eff-b935-b13608bdb340 | 1.05437 | -60.59761 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 60a0b175-5274-3970-80ca-facc16cbe21a | 1.0638 | -60.6063 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| db092101-c2ed-3ac5-a1d9-9d7aac1c6971 | 3.60259 | -59.94973 | 2024-11-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 640994d6-ba10-3883-afbe-e2bf63825f82 | 1.05988 | -60.60691 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 965f146e-5917-348d-859b-54d40fa8bb95 | 1.05125 | -60.60316 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c77bbd0b-864d-3783-bea0-5ed251a2c303 | 3.60178 | -59.94471 | 2024-11-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d0362be-1cd3-3682-b859-5a256789d1ea | 1.13964 | -60.60209 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0edd63bc-36f2-349c-92cd-e6e52ecd4815 | 1.11166 | -59.19957 | 2024-11-13 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03354540-a469-3b38-8e3b-993c33c07d00 | 1.01093 | -60.57574 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd7892ff-b961-326e-b6cb-fa90b961c38f | 2.69176 | -60.96681 | 2024-11-13 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffce9b05-bf4e-3526-8c32-7e7ed12dd0ec | -0.37958 | -51.75036 | 2024-11-13 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7fef26c-daed-3a06-8b2a-907e2baa0a16 | 1.59732 | -55.77304 | 2024-11-13 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19d1b4e4-f4e5-35d3-9646-18e2d3f9d5e4 | 1.06772 | -60.60567 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6df0902d-4904-3634-91e9-3b80f0032c5f | 1.06301 | -60.60136 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6767ddde-ce05-34b6-9203-3664ce2b2fd4 | 1.06068 | -60.61185 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e988ea5-75e4-3105-8a3b-33a78f557737 | 1.05749 | -60.59203 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c66ccf8-a194-3e6f-a02e-be6bfe66b546 | 1.05829 | -60.597 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b88b236-4b5a-334c-9037-362a3b1e88b2 | 3.59865 | -59.95037 | 2024-11-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c50a6a26-b3b5-3b38-a767-65aa22214b07 | 0.92368 | -59.40823 | 2024-11-13 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad0ffc43-8577-3755-9011-795a934b899a | 1.59846 | -55.78003 | 2024-11-13 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64967df2-7694-3055-81e8-53c92db68bf4 | 1.59789 | -55.77654 | 2024-11-13 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b146a61-e2c8-351d-9222-e28443bb0362 | -0.38672 | -51.75142 | 2024-11-13 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44bd2ac4-f185-3cff-89c4-4c80e3193bcd | 0.89184 | -60.28658 | 2024-11-13 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3e024eb-e7e4-31b0-a044-e2ee55fc5b4c | 3.60571 | -59.94408 | 2024-11-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f117dfc3-cf22-3cb6-8702-fc1a1f56368d | 3.37647 | -61.19884 | 2024-11-13 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21bbcad1-da87-3354-8a1e-6d17fbcbef90 | 2.69104 | -60.96229 | 2024-11-13 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74856abc-ea68-35a4-b373-8bca22602281 | -1.41613 | -53.47853 | 2024-11-13 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c4544b1-06e2-31fd-8774-7d472925d98c | 1.05909 | -60.60196 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d896c768-fcbb-37f2-90a7-06d43aee134d | 1.06221 | -60.59639 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f46c3e8-69aa-349e-aa79-f08f4626feda | 1.11038 | -59.19146 | 2024-11-13 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74169022-8857-30a5-92cb-1f84fdc88f70 | 1.01014 | -60.57073 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4554cf-14fc-3fba-892b-4a808283f74b | 1.13899 | -60.59957 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 486ab94b-3eec-3828-8639-af04eb0302ed | 1.05517 | -60.60255 | 2024-11-13 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5602bac8-7ff7-3a0f-8f62-d51da1d98cf9 | -0.38283 | -51.75038 | 2024-11-13 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fbd6cf7-06f2-344a-a5b4-69580487aeb5 | -3.65935 | -54.66372 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9560bf42-1887-3c8c-8a85-6c9f2c5238c4 | -3.10543 | -54.30811 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d723084b-76e2-3d5c-bc7b-b58ebdc0f63d | -2.77272 | -54.73469 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f38e432-6974-37e6-a080-c53fb4d84951 | -3.09903 | -54.3074 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README51.md)
