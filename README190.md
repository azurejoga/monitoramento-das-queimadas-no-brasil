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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a84f5db-abd7-3e22-aeec-55092511279a | -9.50997 | -68.50628 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c912733-16b2-382d-8858-dcc235495a11 | -9.50801 | -68.50432 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b25e0fa5-3991-3ce9-a3b8-590800ae11c1 | -9.50749 | -68.44566 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 335f001a-985d-3a51-9cf9-d23081283b06 | -9.50681 | -68.45023 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee01e92f-f0a5-30fc-817f-53df0e49229b | -9.50183 | -68.05836 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78dabdee-adb5-373b-a4ca-2463ff2a4c69 | -9.50012 | -68.49551 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2d4c0fb9-1534-37a2-8295-c199f8ded45a | -9.49868 | -68.05299 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e7b2a78-63b0-3b8e-b264-f6a97cbfef67 | -9.498 | -68.05779 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20ff8866-6e27-384e-bfba-b1ba404eb208 | -9.49639 | -68.49496 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79974ea3-fedd-3e94-9316-9a8876a33931 | -9.49572 | -68.49949 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1d5aa03-ab47-3535-9379-42167f2b8086 | -9.49416 | -68.05723 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e00361a-4d16-3d8c-8be1-8975a819144b | -9.49265 | -68.49443 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0cc4b00-0652-32d7-ad06-142be0f4c08b | -9.49212 | -68.54964 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00d37027-5c1b-3edf-a525-12a9854c9b8a | -9.49199 | -68.49895 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54b26432-9ec6-3af8-a776-13714cd5c666 | -9.49146 | -68.55412 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 124d3c22-5da4-34e4-b0ac-04935bf597c2 | -9.46234 | -68.54528 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0d49508-ac1f-3e97-bd4e-5d71afaab5cc | -8.1812 | -70.08779 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27b3620f-0377-3bf7-860f-090570cb7d2b | -9.00172 | -71.57773 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f74c0fe-a57c-36b0-8e33-47688ee1866a | -9.98801 | -66.87409 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1022b366-3191-37ca-ab0e-d2cacec08fcd | -9.98749 | -66.87793 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66eaa0cf-1801-3543-933d-4be6b365224b | -9.9921 | -64.76446 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01a7f48d-f21d-3252-a81e-4c39cfadf7e4 | -9.99139 | -64.76975 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb66e985-6d80-347c-911e-9cd436b3fb14 | -9.9873 | -64.76378 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cd1e4f4-2c76-3531-a736-4c4e462c6270 | -8.6944 | -66.658 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 977e15d1-2c52-3ea5-b94e-5097e87862d6 | -6.39868 | -65.70176 | 2024-10-03 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62e4e81d-eee3-3e47-a49d-7fc3e4d8da4f | -9.46255 | -68.51774 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38ef48e5-d9bb-3898-ae72-deff883c81c3 | -9.46299 | -68.54079 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd25a12e-4ca4-3fcb-a5a6-e416182f6c47 | -9.46321 | -68.51323 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8bd4e1e-307c-359b-b922-d80d5711ce43 | -9.46606 | -68.54581 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 958ecdfc-ec5f-39c3-8866-e4b2015613ca | -9.46628 | -68.5183 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 920617ad-72c7-3199-b355-8c7b1abc518a | -9.46694 | -68.51378 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97cb2a39-f315-3a1a-a87a-f79fb52654fd | -9.47211 | -68.26607 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 486a93df-6f97-3abc-86c8-753774e914c8 | -9.47589 | -68.26662 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f6fe68-f5be-3891-97f1-be694e5f46d8 | -9.48211 | -68.4883 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0775aac4-4bc3-356f-9559-bfcb9d94e25e | -9.48774 | -68.55357 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddbdab1c-cd1c-33ba-a2da-f1a806a5800f | -9.48839 | -68.54912 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf019a5b-1af4-3820-b170-54f0d9d4b674 | -9.16993 | -67.31797 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1adfe175-31a6-3b97-a5b8-d09b200d39c3 | -9.16944 | -67.32146 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e101274c-ab4f-3ef8-b07a-9b4eb693a55f | -9.16643 | -67.31387 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e268e4de-4da0-3d34-9d1f-1169298433be | -9.16594 | -67.31739 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b18e5191-b245-3195-8387-9432026df0ab | -9.16544 | -67.32091 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b656999-9848-3a38-b55c-549620b22618 | -9.16194 | -67.3168 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6513b86-d8e7-34bd-8a1a-ce7fbf1e6ea8 | -9.31302 | -66.62962 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 824e5ba7-91eb-3cb0-a449-94484058d297 | -9.31247 | -66.63347 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4b3daf1-334a-3b89-9f4c-c6f6d6b9c8bb | -9.30883 | -66.62899 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 241ce0fb-c6e8-3dbe-8956-6ccf23845bcb | -8.69622 | -66.66109 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 117daee8-a46c-3a9a-847a-d3bed2355d94 | -8.67096 | -67.02168 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba155c35-c5a5-39ea-8d6b-4b9ea8f79a5c | -8.67046 | -67.02526 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0590ad74-23a4-3e41-bc33-8ba8eaaf71e3 | -8.66692 | -67.02109 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42301c16-11bc-368e-9582-b390b1c0e696 | -8.66003 | -66.60252 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3854c82-c1d3-320e-bd41-d931c31392a7 | -8.65949 | -66.60632 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cf7f073-bd10-378f-97ea-2f218cdd2c62 | -8.65804 | -66.67567 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 367e09b9-4166-30f7-82b9-7f6d64924ab6 | -8.6575 | -66.67943 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc6a0499-6de2-3341-877c-23678fc5da86 | -8.65587 | -66.60192 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe91b5f6-b3e2-3056-b121-271479b6ab7e | -8.65533 | -66.60571 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d29bf89c-99b5-3159-8c66-0c70cb83256d | -8.65391 | -66.67505 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10d5ed54-e09e-3144-a2e9-f95967e99f2e | -8.65337 | -66.67882 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cbef20d-731f-3bcd-9290-5a9d6821eacf | -8.65118 | -66.60509 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9da30e8d-5c9e-330a-9c5e-bc25482e3318 | -8.64854 | -66.71256 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 530180f6-a0f8-355e-aa3c-369e88ec2bc2 | -8.64801 | -66.7163 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81fd7a61-ff65-3711-a783-d526efaf2cd7 | -8.64595 | -66.61206 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30bc261-f209-3e98-8bcf-3f6d571c7f04 | -8.64442 | -66.71196 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68b416e3-e23b-3b7b-bcb7-91e8220d64da | -8.64389 | -66.71569 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1ecb26e-5679-33b6-89b0-c0301d5d6aae | -8.63976 | -66.71507 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e2da773-c08b-3168-a42a-3329526f84bf | -8.63923 | -66.71879 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 703f47d1-7943-35d2-8e33-c096dab6c1fb | -9.37422 | -65.84043 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef0bcbff-dc03-3c96-b396-13e9c60d98f4 | -9.3698 | -65.83978 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29ecb674-abb3-356b-9fab-7e438e4ec0c6 | -9.49792 | -67.14382 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b106289a-23a4-301b-bc87-82658c0e8589 | -9.44572 | -67.15887 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9028f6d-467d-3ad2-81d4-733db81c36f3 | -9.43045 | -67.23724 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9f0bd06-9484-3ecd-80af-ea1c5b928220 | -9.42693 | -67.23309 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49b11622-b6bf-3f53-b365-2c11363b2ba2 | -9.4229 | -67.23252 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5257e305-16d5-37b1-a466-e87358ac5465 | -9.4224 | -67.23606 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4063f810-5a12-3db1-a60d-c0840cab3971 | -9.41836 | -67.35085 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88870c10-87fd-357b-84c5-fef272f2bdaa | -9.6013 | -66.11546 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5199d278-7626-399f-b571-4ebbcf72cefe | -9.60071 | -66.11967 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c2ee7ee-d26c-346c-877e-1f6f0034195d | -9.90339 | -67.33707 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3db9a9b5-bcf2-330d-be80-ea8125789609 | -9.9029 | -67.34062 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee7301bf-4dc4-35a7-97cf-adf895b287c3 | -9.89936 | -67.33647 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0f809e56-a613-37ad-86b3-86d9521bf18b | -9.89887 | -67.34003 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d9256b7-4c8f-31eb-90d6-d173fd8cff96 | -7.95017 | -72.51283 | 2024-10-03 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dc6a96b-fb97-3b31-a33e-9dd20f58a5e7 | -8.00033 | -72.51722 | 2024-10-03 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3734d63-83aa-33cb-a1c3-55f41d14b8e5 | -8.00086 | -72.49236 | 2024-10-03 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7908f9c4-1e7f-39a4-8686-b6095e4bc851 | -8.05799 | -72.3912 | 2024-10-03 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 628f03ed-36db-31b4-9962-d68a200f5823 | -7.00721 | -71.80087 | 2024-10-03 06:08:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7f37170-f6a6-31cc-8c6f-ac20e4aafa69 | -7.21542 | -72.31624 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b311824-f41c-303b-9216-346d1cc6a46f | -7.21873 | -72.31676 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49175ebc-73d0-3a98-83e1-cccbc9e1ecd8 | -7.22203 | -72.31728 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d876560-0d60-3321-9673-4605d506ffe7 | -7.31276 | -72.75407 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 932737de-2f4f-3e69-a652-6906e5f6e3fe | -7.37358 | -72.4985 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a48d38ea-975a-3c85-8a11-10dd395a8983 | -7.37689 | -72.49903 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9a8b4a1-0283-37e2-b688-191bc3e57bce | -7.37744 | -72.49554 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0565d2d-84ac-3b67-8068-a1f16266f5c9 | -7.38374 | -72.50019 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cda23f4-7d22-3da5-b08a-f0ab9edda47b | -7.38705 | -72.50072 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f81b24cb-dbc9-38ec-a565-c80934cac896 | -7.42561 | -72.72884 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a128b9f-6962-3181-8d3b-a3fd5e8286e4 | -7.42616 | -72.72533 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a34066bb-9d05-3b6e-8d81-782dbaf40724 | -7.42893 | -72.72936 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea2bfb18-930c-39b1-b468-c863a6cc0e01 | -7.42948 | -72.72587 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f1b1449-4805-3089-a39a-e6bb90fb85ae | -7.43225 | -72.72989 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f369d5-f16a-3899-a02a-f8da89ff86ec | -7.4328 | -72.72639 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README191.md)
