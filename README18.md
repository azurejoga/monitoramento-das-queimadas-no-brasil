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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7b7cb5d-ca4a-30fb-abab-7fdd1e2ccebd | -7.0384 | -44.341 | 2025-07-13 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 24459966-c0d6-32c1-8df7-db00abf6bd5a | -10.5779 | -49.1098 | 2025-07-13 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e57fca69-40d0-3501-be98-b1948c47b13e | -6.4659 | -45.3022 | 2025-07-13 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| ece43eaa-2f86-3e43-abd3-9776e3244968 | -7.0381 | -44.364 | 2025-07-13 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 365.7 |
| da53ae8b-5344-3afe-89be-171122960ffa | -12.4393 | -50.4678 | 2025-07-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 87797659-bb28-3b04-affc-92248f80f00d | -6.1238 | -45.869 | 2025-07-13 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7662fdd1-3474-372b-9ff4-d12cdf9eb194 | -4.5243 | -48.016 | 2025-07-13 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c942ed81-b5a3-36db-aadb-ceac558040a9 | -7.3237 | -44.0377 | 2025-07-13 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| af072be4-bec2-3322-8038-c95704788aaa | -6.4848 | -45.2781 | 2025-07-13 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 271.0 |
| b51b1703-729a-3d12-bb6a-87b16e14fa45 | -12.4393 | -50.4678 | 2025-07-13 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dfb20288-52ac-3b3a-916b-dc7c4d166cb2 | -6.4661 | -45.2796 | 2025-07-13 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 295.1 |
| 5d124b81-b941-3ee5-a5a9-7709aeab29fe | -12.439 | -50.4894 | 2025-07-13 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6481f3a2-9546-38a8-af02-979704e3f193 | -7.0381 | -44.364 | 2025-07-13 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 299.5 |
| a81392ea-7675-3266-8b9f-5ad7cd2280d8 | -10.5776 | -49.1316 | 2025-07-13 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b3be26ad-2dd2-3971-9f69-c69bb6e8403e | -7.0384 | -44.341 | 2025-07-13 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 6d8a7336-7709-3acc-b7a5-581399076fcf | -10.5779 | -49.1098 | 2025-07-13 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 52763fe5-c79a-33b4-a461-d63f71037482 | -8.5497 | -64.0477 | 2025-07-13 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 153.2 |
| bcf0392d-ce97-342b-a7dd-4ee6a596c25d | -6.4659 | -45.3022 | 2025-07-13 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 14d576c1-8163-37a5-aa44-84b6eafd00ea | -10.5779 | -49.1098 | 2025-07-13 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4d1dd783-8dc7-346e-be15-6702dcd63c29 | -6.4848 | -45.2781 | 2025-07-13 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 48b31afc-11ca-339d-8671-c4db587e3b5f | -10.5776 | -49.1316 | 2025-07-13 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 455921ad-46cc-3d7f-b54f-2acdf0bc8f72 | -8.5497 | -64.0477 | 2025-07-13 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e317d1ca-39a3-3919-98b1-29fcbf6870c7 | -7.3091 | -45.3439 | 2025-07-13 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 02dffc55-a59c-3e7b-8b62-a173caf29b3e | -6.4661 | -45.2796 | 2025-07-13 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| dfb7a6a8-c3a9-3495-a8c8-dd7d957c5229 | -6.4659 | -45.3022 | 2025-07-13 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 54bf5b1e-0438-3ee7-b5b9-c6ad16fc0084 | -7.0381 | -44.364 | 2025-07-13 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 261.2 |
| bda8a05f-ea10-3d09-9e04-2258f71609e4 | -4.5243 | -48.016 | 2025-07-13 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e02b1c52-d3bf-3d5c-a28d-76d49aa0d729 | -7.0384 | -44.341 | 2025-07-13 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 4bdf7641-a72a-3318-aa41-fb352e178a1b | -3.1038 | -42.5589 | 2025-07-13 14:30:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f38e5718-cda9-3c24-9017-e8856e2dca66 | -12.439 | -50.4894 | 2025-07-13 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 83ec55f3-e785-36a3-9802-9c991bbe686a | -10.5776 | -49.1316 | 2025-07-13 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9b584b99-12d0-3fe5-9d18-63ca67c1fad7 | -7.3237 | -44.0377 | 2025-07-13 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| aeb4ae84-81ef-36af-bf4e-ac69d2cac5e7 | -6.4659 | -45.3022 | 2025-07-13 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 80ff72e5-fc17-358f-a13b-580d9d060283 | -10.5779 | -49.1098 | 2025-07-13 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 99b3a149-3ea5-3799-b942-4ece18f2cde2 | -4.5243 | -48.016 | 2025-07-13 14:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 40ebf809-7db8-30e6-a425-c79eac82fa42 | -6.6569 | -43.1212 | 2025-07-13 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7278d117-12c4-3ecc-a9e2-1eb04469e6dc | -7.1241 | -46.8826 | 2025-07-13 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 84f7c510-099f-3e83-82de-8aa6a7122a36 | -13.0108 | -46.2557 | 2025-07-13 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 192fda4c-05a5-33a1-b5e7-804ef517c8cb | -7.0384 | -44.341 | 2025-07-13 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 0446eb43-a16c-3681-9e2c-78e0e5225c0c | -6.4279 | -45.3505 | 2025-07-13 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e708a9e5-3c7a-3745-8a1e-059bdf6f6d26 | -7.0381 | -44.364 | 2025-07-13 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 8931b5dd-0472-3aba-a458-e05472dc1737 | -6.4661 | -45.2796 | 2025-07-13 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 27d383c1-7a55-358c-bf3e-8fd72a1156f9 | -6.4848 | -45.2781 | 2025-07-13 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |


