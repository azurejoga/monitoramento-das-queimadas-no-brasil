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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcac9a9e-b065-39a6-a674-4a23d341915f | -8.9401 | -60.7288 | 2025-08-12 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a3273967-ed80-39ff-9f38-14d0a5fb8067 | -17.5707 | -45.3108 | 2025-08-12 14:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 90dceaf5-d5f9-3c6f-994e-79cbbbe0a177 | -8.5602 | -54.7175 | 2025-08-12 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 37bf3d77-914d-37c8-957f-a7041491786c | -8.9401 | -60.7288 | 2025-08-12 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a30e58bb-3bff-318d-ac06-8f724cfce035 | -7.0615 | -59.1779 | 2025-08-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 722ede61-0a99-3d50-a06e-ffdd7ee48e75 | -16.3153 | -52.9201 | 2025-08-12 14:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8da063bb-f5d7-398e-862c-5d16c303d3ad | -6.0992 | -59.9267 | 2025-08-12 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| daee0a7f-0804-3a7d-9802-ea357298893b | -7.1299 | -60.1182 | 2025-08-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 569e9f56-3ac8-3206-ad94-772fccb76370 | -8.5602 | -54.7175 | 2025-08-12 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| dc58f18f-5740-3053-81e4-a079d5c429c6 | -17.5707 | -45.3108 | 2025-08-12 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4ccc7fe4-6aca-3c30-a3fb-7807a83ca711 | -11.7896 | -51.9033 | 2025-08-12 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| e7ecc12b-1e6b-30bc-aacd-8f10a8c13334 | -7.1482 | -60.1366 | 2025-08-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 7aa05cdc-bd56-3412-8bec-efb0160e4299 | -7.0799 | -59.1964 | 2025-08-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 02a61b39-9710-3f90-aa40-9664f140dbc0 | -17.5701 | -45.3346 | 2025-08-12 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 314.5 |
| 26f9b780-fb58-3b28-b86a-fe7b063544fc | -12.3565 | -59.8473 | 2025-08-12 14:40:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8fe718ea-20f0-38aa-99e3-4ddf079fb9d4 | -17.5695 | -45.3584 | 2025-08-12 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 41a1a4f6-2318-3055-acb2-b0d63a22daeb | -14.1017 | -44.8968 | 2025-08-12 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 7ff8f83f-3593-3048-ad81-770d623953cf | -7.1483 | -60.1174 | 2025-08-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 1c34b66c-0486-3de3-8778-197099e96c30 | -7.0614 | -59.1972 | 2025-08-12 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 32e7f619-0a88-3548-af3c-c0bf0fd5eca2 | -9.2079 | -59.6742 | 2025-08-12 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| d70f9d2f-41c0-3144-8759-1f9cc794c5de | -14.1212 | -44.8933 | 2025-08-12 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 834ab5b6-49bc-3e61-b054-00fa8083ce3a | -8.5788 | -54.7162 | 2025-08-12 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |


